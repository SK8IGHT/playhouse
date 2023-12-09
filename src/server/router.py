from src.server.database import models as database_models
from src.server.database import pydantic_models
from src.server.service import RouterManager

# Создание роутеров
router_venue = RouterManager(database_model=database_models.Venue, pydantic_model=pydantic_models.Venue, prefix='/venue', tags=['Venue']).fastapi_router
router_concert = RouterManager(database_model=database_models.Concert, pydantic_model=pydantic_models.Concert, prefix='/concert', tags=['Concert']).fastapi_router
router_ticket = RouterManager(database_model=database_models.Ticket, pydantic_model=pydantic_models.Ticket, prefix='/ticket', tags=['Ticket']).fastapi_router
router_band = RouterManager(database_model=database_models.Band, pydantic_model=pydantic_models.Band, prefix='/band', tags=['Band']).fastapi_router
router_musician = RouterManager(database_model=database_models.Musician, pydantic_model=pydantic_models.Musician, prefix='/musician', tags=['Musician']).fastapi_router
router_attendee = RouterManager(database_model=database_models.Attendee, pydantic_model=pydantic_models.Attendee, prefix='/attendee', tags=['Attendee']).fastapi_router
router_ticket_sale = RouterManager(database_model=database_models.TicketSale, pydantic_model=pydantic_models.TicketSale, prefix='/ticket_sale', tags=['TicketSale']).fastapi_router
router_review = RouterManager(database_model=database_models.Review, pydantic_model=pydantic_models.Review, prefix='/review', tags=['Review']).fastapi_router
router_artist_schedule = RouterManager(database_model=database_models.ArtistSchedule, pydantic_model=pydantic_models.ArtistSchedule, prefix='/artist_schedule', tags=['ArtistSchedule']).fastapi_router
router_event_staff = RouterManager(database_model=database_models.EventStaff, pydantic_model=pydantic_models.EventStaff, prefix='/event_staff', tags=['EventStaff']).fastapi_router
router_sponsor = RouterManager(database_model=database_models.Sponsor, pydantic_model=pydantic_models.Sponsor, prefix='/sponsor', tags=['Sponsor']).fastapi_router
router_concert_sponsorship = RouterManager(database_model=database_models.ConcertSponsorship, pydantic_model=pydantic_models.ConcertSponsorship, prefix='/concert_sponsorship', tags=['ConcertSponsorship']).fastapi_router

# Список роутеров
routers = (
    router_venue,
    router_concert,
    router_ticket,
    router_band,
    router_musician,
    router_attendee,
    router_ticket_sale,
    router_review,
    router_artist_schedule,
    router_event_staff,
    router_sponsor,
    router_concert_sponsorship,
)
