from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from src.application.responses.artist_responses import ArtistResponses
from src.domain.services.artist_service import ArtistService
from src.application.requests.artist_request import ArtistRequest

router_artist = APIRouter(prefix='/artist/v1')


@router_artist.get("/")
async def get_all(artist_service: ArtistService = Depends()) -> List[ArtistResponses] | HTTPException:
    try:
        artists = await artist_service.get_all_artist()
        return artists
    except Exception as e:
        return HTTPException(status_code=500,
                             detail=f'Internal Server Error in Resquest {e}')


@router_artist.get('/{artist_id}')
async def get_by_id(artist_id: int, artist_service: ArtistService = Depends()) -> ArtistResponses | HTTPException:
    try:
        artist = await artist_service.get_artist_id(artist_id)
        return artist
    except Exception as e:
        return HTTPException(status_code=400,
                             detail=f'ID Artist is not find {e}')


@router_artist.post('/')
async def add_artist(artist: ArtistRequest, artist_service: ArtistService = Depends()) -> HTTPException | JSONResponse:
    try:
        if artist.name == '':
            return HTTPException(status_code=400,
                                 detail="The artist's name must not be empty.")
        else:
            await artist_service.add_artist(artist)
            return JSONResponse(status_code=200, content={'mensaje': 'artist create'})
    except Exception as e:
        return HTTPException(status_code=500, detail=f'{e}')


@router_artist.delete('/{artist_id}')
async def del_artist(artist_id: int, artist_service: ArtistService = Depends()) -> HTTPException | JSONResponse:
    try:
        await artist_service.delete_artist(artist_id)
    except Exception as e:
        return HTTPException(status_code=400, detail=f'{e}')


@router_artist.put('/')
async def update_artist(artist: ArtistRequest, artist_service: ArtistService = Depends()
                        ) -> HTTPException | JSONResponse:
    try:
        if not artist.id:
            return HTTPException(status_code=400,
                                 detail='The artist ID has not been specified for the update.')

        else:
            await artist_service.update_artist(artist)
            return JSONResponse(status_code=200,
                                content={'mensaje': 'Update is complete'}
                                )

    except Exception as e:
        return HTTPException(status_code=500,
                             detail=f'{e}'
                             )
