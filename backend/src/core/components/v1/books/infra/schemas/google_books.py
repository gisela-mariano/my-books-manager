from enum import Enum
from typing import List, Optional, Union

from pydantic import Field
from src.core.utils.models.base import BaseConfig


class GoogleVolumeIdentifierTypeEnum(Enum):
    ISBN_10 = "ISBN_10"
    ISBN_13 = "ISBN_13"
    ISSN = "ISSN"
    OTHER = "OTHER"


class GoogleVolumeIdentifier(BaseConfig):
    type: str = Field(
        description="Identifier type. Possible values are ISBN_10, ISBN_13, ISSN, and OTHER."
    )
    identifier: str = Field(description="ISBN code")


class GoogleVolumeImageLinks(BaseConfig):
    small_thumbnail: Optional[str]
    thumbnail: Optional[str]


class GoogleVolumeInfo(BaseConfig):
    title: str
    subtitle: Optional[str] = None
    authors: Optional[List[str]] = None
    publisher: Optional[str] = None
    published_date: Optional[str] = None
    description: Optional[str] = Field(
        default=None,
        description="A synopsis of the volume. The description text is formatted in HTML and includes simple formatting elements such as b, i, and br tags.",
    )
    industry_identifiers: Optional[List[GoogleVolumeIdentifier]] = None
    page_count: Optional[int] = None
    categories: Optional[List[str]] = None
    image_links: Optional[GoogleVolumeImageLinks] = None


class GoogleVolume(BaseConfig):
    id: str
    kind: str = Field(description="Type of resource")
    etag: Optional[str] = None
    self_link: Optional[str] = Field(default=None, description="Individual link")
    volume_info: Optional[GoogleVolumeInfo] = None


class GoogleVolumeSearch(BaseConfig):
    kind: str = Field(description="Type of resource")
    total_items: int = Field(
        description="Total number of volumes found. This number may be greater than the number of volumes returned in this response if the results were paginated."
    )
    items: Optional[List[GoogleVolume]] = None
