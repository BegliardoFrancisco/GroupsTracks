from fastapi import HTTPException, status, APIRouter
from typing import List
from src.application.requests.artist_request import NewArtistRequest, ArtistRequestUpdate
from src.application.responses.artist_responses import SimpleArtistResponses
from src.infraestructure.repositories.artist_repository_impl import ArtistRepositoryImpl
from src.infraestructure.services.artist_service_impl import ArtistServiceImpl

artist_repo = ArtistRepositoryImpl()

artist_service = ArtistServiceImpl(artist_repo)

router_artist = APIRouter(prefix='/artist/v1')


@router_artist.get('/')
async def get_all() -> List[SimpleArtistResponses]:
    try:
        artists = await artist_service.get_all_artist()
        return artists
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f'Internal Server Error in Resquest {e}')


@router_artist.get('/{artist_id}')
async def get_by_id(artist_id: int) -> SimpleArtistResponses:
    try:
        response = await artist_service.get_artist_id(artist_id)
        return response

    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'ID Artist is not find')


@router_artist.post('/', status_code=status.HTTP_201_CREATED)
async def add_artist(artist: NewArtistRequest):
    try:
        if artist.name == '':
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="The artist's name must not be empty.")

        await artist_service.add_artist(artist)
        return {'mensaje': 'artist create'}

    except ValueError as e:
        return {'mensaje': f'{e}'}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{e} {type(e)}')


@router_artist.delete('/{artist_id}')
async def delete_artist(artist_id: int):
    try:
        await artist_service.delete_artist(artist_id)
        return {'mensaje': f'artist {artist_id} delete'}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'{e}')


@router_artist.put('/')
async def update_artist(artist: ArtistRequestUpdate):
    try:
        if not artist.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='The artist ID has not been specified for the update.')

        else:
            await artist_service.update_artist(artist)
            return {'mensaje': 'Update is complete'}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f'{e}'
                            )
