from typing import Optional

from src.core.utils.exceptions.errors import ValidationError


async def get_pagination_parameters(
    limit: Optional[int] = 25,
    offset: Optional[int] = 0,
):

    return {
        "limit": limit,
        "offset": offset,
    }
