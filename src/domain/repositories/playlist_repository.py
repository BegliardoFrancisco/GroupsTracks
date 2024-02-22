from abc import ABC, abstractmethod
from typing import List
from src.domain.models.play_list import PlayList
from src.domain.repositories.track_repository import TrackRepository
from src.domain.repositories.playlist_track_repository import TracksInPlaylistRepository

class PlayListRepositories(ABC):

    def __init__(self, track_repository: TrackRepository,  track_in_playlist_repository: TracksInPlaylistRepository) -> None:
        self.track_repository = track_repository
        self.track_in_pl = track_in_playlist_repository 

    @abstractmethod
    async def get_all_playlist(cls) -> List[PlayList]:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_all_playlist no implemented method in class: {__class__}")

    @abstractmethod
    async def get_playlist_id(cls, id: int) -> PlayList:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"get_playlist_id no implemented method in class: {__class__}")

    @abstractmethod
    async def add_playlist(cls, playlist: PlayList) -> None:
        raise NotImplementedError(f"NotImplementedError: "
                                  f"add_playlist no implemented method in class: {__class__}")

    @abstractmethod
    async def delete_playlist(cls, playlist_id: int) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'delete_playlist method in {__class__}')

    @abstractmethod
    async def update_playlist(cls, playlist: PlayList) -> None:
        raise NotImplementedError('NotImplementedError: '
                                  f'update_playlist method in {__class__}')
        
    @abstractmethod
    async def add_track_from_playlist(cls, track_id: int, playlist_id: int) -> None:
        raise NotImplementedError('NotImplementedError: '
                                f'add_track_from_playlist method in {__class__}')
    
    @abstractmethod
    async def add_tracks_from_playlist(cls, tracks_id: List[int], playlist_id: int) -> None:
        raise NotImplementedError('NotImplementedError: '
                                f'add_tracks_from_playlist method in {__class__}')
    
    @abstractmethod
    async def delete_track_from_playlist(cls, track_id: int, playlist_id: int) -> None:
        raise NotImplementedError('NotImplementedError: '
                                f'delete_track_from_playlist method in {__class__}')
    
    @abstractmethod
    async def delete_tracks_from_playlist(cls, tracks_id: List[int], playlist_id: int) -> None:
        raise NotImplementedError('NotImplementedError: '
                                f'delete_tracks_from_playlist method in {__class__}')        

    @abstractmethod
    async def check_exist_playlist(cls, playlists_ids: List[PlayList]) -> bool:
        raise NotImplementedError('NotImplementedError: '
                                f' check_exist_playlist method in {__class__}')