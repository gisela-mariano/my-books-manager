from typing import List

from src.core.components.v1.books.infra.schemas.book import Book
from src.core.components.v1.books.infra.schemas.google_books import (
    GoogleVolumeIdentifier,
    GoogleVolumeIdentifierTypeEnum,
    GoogleVolumeInfo,
)


def volume_to_book(volume: GoogleVolumeInfo) -> Book:
    return Book(
        title=volume.title,
        subtitle=volume.subtitle,
        description=volume.description,
        cover_url=getattr(volume.image_links, "thumbnail", None),
        isbn_10=get_identifiers(
            volume.industry_identifiers, GoogleVolumeIdentifierTypeEnum.ISBN_10.value
        ),
        isbn_13=get_identifiers(
            volume.industry_identifiers, GoogleVolumeIdentifierTypeEnum.ISBN_13.value
        ),
        page_count=volume.page_count,
        published_date=volume.published_date,
    )


def get_identifiers(
    identifiers: List[GoogleVolumeIdentifier], type: GoogleVolumeIdentifierTypeEnum
) -> str:
    if not identifiers or not len(identifiers):
        return None

    for identifier in identifiers:
        if identifier.type == type:
            return identifier.identifier

    return None
