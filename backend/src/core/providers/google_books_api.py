import requests
from src.core.components.v1.books.infra.schemas.google_books import GoogleVolumeSearch
from src.core.utils.api.base import BaseAPI
from src.core.utils.exceptions.errors import ApiServiceCodeError


class GoogleBooksApiProvider(BaseAPI):
    base_url = "https://www.googleapis.com/books/v1/volumes"

    def search_volume(
        self, query: str, limit: int = 25, offset: int = 0
    ) -> GoogleVolumeSearch:
        try:
            url = f"{self.base_url}?q={query}&maxResults={limit}&startIndex={offset}"

            res = self._get(url)

            data = res.json()

            return GoogleVolumeSearch(**data)
        except Exception as e:
            raise ApiServiceCodeError(
                message="Failed to search volume from Google Books API",
                metadata=[{"error": str(e)}],
            )
