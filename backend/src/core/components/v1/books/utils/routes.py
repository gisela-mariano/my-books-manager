from typing import Optional

from src.core.utils.exceptions.errors import ValidationError


async def get_book_search_parameters(
    search_term: str = None,
    author: Optional[str] = None,
    publisher: Optional[str] = None,
    title: Optional[str] = None,
    isbn: Optional[str] = None,
    limit: Optional[int] = 25,
    offset: Optional[int] = 0,
):
    if not search_term and not author and not publisher and not title and not isbn:
        raise ValidationError(
            "At least one filter parameter (search_term, author, publisher, title, isbn) must be informed"
        )

    return {
        "search_term": search_term,
        "author": author,
        "publisher": publisher,
        "title": title,
        "isbn": isbn,
        "limit": limit,
        "offset": offset,
    }
