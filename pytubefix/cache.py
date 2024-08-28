from abc import ABC, abstractmethod
from typing import Optional, Dict
import os


class TokenCache(ABC):
    def __init__(self):
        self._token_cache = None

    @abstractmethod
    def save_token(self, data: Dict) -> None:
        """
        Method to save the token data (as a dictionary) in the cache.

        :param data: A dictionary containing the token data to be saved
        """
        pass

    @abstractmethod
    def get_token(self) -> Optional[Dict]:
        """
        Method to retrieve the token data from the cache.

        :return: The token data as a dictionary if it exists, otherwise None
        """
        pass


class FileTokenCache(TokenCache):
    def __init__(self, file_path: str):
        super().__init__()
        self.file_path = file_path

    def save_token(self, data: Dict) -> None:
        """
        Saves the token data (as a dictionary) to a file.

        :param data: A dictionary containing the token data to be saved
        """
        with open(self.file_path, 'w') as file:
            json.dump(data, file)

    def get_token(self) -> Optional[Dict]:
        """
        Retrieves the token data from a file.

        :return: The token data as a dictionary if it exists, otherwise None
        """
        if not os.path.exists(self.file_path):
            return None

        with open(self.file_path, 'r') as file:
            data = json.load(file)

        return data if data else None