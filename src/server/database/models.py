from peewee import Model, SqliteDatabase, CharField, IntegerField, FloatField, DateTimeField, BooleanField, ForeignKeyField

db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Venue(BaseModel):
    name = CharField(default="")
    capacity = IntegerField(default=0)
    location = CharField(default="")
    phone = CharField(default="")


class Concert(BaseModel):
    venue_id = ForeignKeyField(Venue, backref='concerts')
    artist = CharField(default="")
    date = DateTimeField()
    ticket_price = FloatField(default=0.0)


class Ticket(BaseModel):
    concert_id = ForeignKeyField(Concert, backref='tickets')
    seat_number = IntegerField(default=0)
    is_sold = BooleanField(default=False)


class Band(BaseModel):
    name = CharField(default="")
    genre = CharField(default="")
    formed_year = IntegerField(default=0)


class Musician(BaseModel):
    band_id = ForeignKeyField(Band, backref='musicians')
    name = CharField(default="")
    instrument = CharField(default="")


class Attendee(BaseModel):
    name = CharField(default="")
    email = CharField(default="")


class TicketSale(BaseModel):
    ticket_id = ForeignKeyField(Ticket, backref='sales')
    attendee_id = ForeignKeyField(Attendee, backref='ticket_sales')
    sale_date = DateTimeField()


class Review(BaseModel):
    concert_id = ForeignKeyField(Concert, backref='reviews')
    attendee_id = ForeignKeyField(Attendee, backref='reviews')
    rating = IntegerField(default=0)
    comment = CharField(default="")


class ArtistSchedule(BaseModel):
    artist = CharField(default="")
    date = DateTimeField()
    venue_id = ForeignKeyField(Venue, backref='artist_schedules')


class EventStaff(BaseModel):
    name = CharField(default="")
    role = CharField(default="")
    venue_id = ForeignKeyField(Venue, backref='event_staff')


class Sponsor(BaseModel):
    name = CharField(default="")
    logo_url = CharField(default="")


class ConcertSponsorship(BaseModel):
    concert_id = ForeignKeyField(Concert, backref='sponsorships')
    sponsor_id = ForeignKeyField(Sponsor, backref='concert_sponsorships')


# Создание таблиц в базе данных
db.connect()
db.create_tables([Venue, Concert, Ticket, Band, Musician, Attendee, TicketSale, Review, ArtistSchedule, EventStaff, Sponsor, ConcertSponsorship])
