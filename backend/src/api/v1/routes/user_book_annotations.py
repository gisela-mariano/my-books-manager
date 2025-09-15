from typing import Annotated, List, Optional

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends
from src.core.components.v1.user_book_annotations.application.use_cases.user_book_annotation_create_use_case import (
    UseBookAnnotationCreateUseCase,
)
from src.core.components.v1.user_book_annotations.application.use_cases.user_book_annotation_get_annotations_use_case import (
    UserBookAnnotationGetAnnotationsUseCase,
)
from src.core.components.v1.user_book_annotations.application.use_cases.user_book_annotation_get_by_id_user_case import (
    UserBookAnnotationGetByIdUseCase,
)
from src.core.components.v1.user_book_annotations.application.use_cases.user_book_annotation_update_use_case import (
    UserBookAnnotationUpdateUseCase,
)
from src.core.components.v1.user_book_annotations.infra.schemas.user_book_annotation import (
    UserBookAnnotationCreate,
    UserBookAnnotationJoinUserBook,
    UserBookAnnotationUpdate,
)
from src.core.di.containers import Container
from src.core.middlewares.models.base_response import BaseResponse
from src.core.utils.fastapi.get_responses import get_responses
from src.core.utils.routes.get_pagination_parameters import get_pagination_parameters

user_book_annotations_router = APIRouter(
    prefix="/user-book-annotations", tags=["User Book Annotations"]
)


@user_book_annotations_router.post(
    "", responses=get_responses(UserBookAnnotationJoinUserBook)
)
@inject
async def create_user_book_annotation(
    payload: UserBookAnnotationCreate,
    user_book_annotation_create_use_case: UseBookAnnotationCreateUseCase = Depends(
        Provide[
            Container.components.user_book_annotation.user_book_annotation_create_use_case
        ]
    ),
):
    res = await user_book_annotation_create_use_case.execute(payload)

    return BaseResponse(message="User Book Annotation successfully created", data=res)


@user_book_annotations_router.get(
    "/user-book/{user_book_id}",
    responses=get_responses(List[UserBookAnnotationJoinUserBook]),
)
@inject
async def get_user_book_annotations_by_user_book_id(
    user_book_id: str,
    params: Annotated[dict, Depends(get_pagination_parameters)],
    user_book_annotation_get_annotations_use_case: UserBookAnnotationGetAnnotationsUseCase = Depends(
        Provide[
            Container.components.user_book_annotation.user_book_annotation_get_annotations_use_case
        ]
    ),
):
    res = await user_book_annotation_get_annotations_use_case.execute(
        user_book_id=user_book_id, **params
    )

    return BaseResponse(message="User Book Annotations successfully obtained", data=res)


@user_book_annotations_router.get(
    "/{user_book_annotation_id}",
    responses=get_responses(Optional[UserBookAnnotationJoinUserBook]),
)
@inject
async def get_user_book_annotation_by_id(
    user_book_annotation_id: str,
    user_book_annotation_get_by_id_user_case: UserBookAnnotationGetByIdUseCase = Depends(
        Provide[
            Container.components.user_book_annotation.user_book_annotation_get_by_id_user_case
        ]
    ),
):
    res = await user_book_annotation_get_by_id_user_case.execute(
        id=user_book_annotation_id
    )

    return BaseResponse(message="User Book Annotation successfully obtained", data=res)


@user_book_annotations_router.patch(
    "/{user_book_annotation_id}",
    responses=get_responses(Optional[UserBookAnnotationJoinUserBook]),
)
@inject
async def update_user_book_annotation(
    user_book_annotation_id: str,
    payload: UserBookAnnotationUpdate = Body(...),
    user_book_annotation_update_use_case: UserBookAnnotationUpdateUseCase = Depends(
        Provide[
            Container.components.user_book_annotation.user_book_annotation_update_use_case
        ]
    ),
):
    res = await user_book_annotation_update_use_case.execute(
        id=user_book_annotation_id,
        payload=payload,
    )

    return BaseResponse(message="User Book Annotation successfully updated", data=res)
