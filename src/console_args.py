from argparse import ArgumentParser, Namespace
from typing import Union

class ArgsHandler:
    def __init__(self) -> None:
        self.__args = self.__parse_args()

    def __parse_args(self) -> Namespace:
        parser = ArgumentParser(description="Youtube playlist parser")
        parser.add_argument('playlist_url', help='Playlist URL')
        parser.add_argument('-c', '--cookies', required=True, help='Youtube user cookies file')
        parser.add_argument('-n', '--name', default=None, help='Output filename (Default: playlist name)')
        return parser.parse_args()
    
    def get_name(self) -> Union[str, None]:
        return self.__args.name
    
    def get_url(self) -> Union[str, None]:
        return self.__args.playlist_url
    
    def get_cookies(self) -> Union[str, None]:
        return self.__args.cookies