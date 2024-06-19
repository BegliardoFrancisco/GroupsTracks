from fastapi import FastAPI
from src.infraestructure.repositories.artist_repository_impl import ArtistRepositoryImpl
from src.infraestructure.services.artist_service_impl import ArtistServiceImpl
from src.application.routers.artist_router import router_artist

app = FastAPI()

app.include_router(router_artist)


