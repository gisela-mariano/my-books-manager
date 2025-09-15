from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from src.core.components.v1.user_book_annotations.application.use_cases.user_book_annotation_create_use_case import (
    UseBookAnnotationCreateUseCase,
)
from src.core.components.v1.user_book_annotations.infra.schemas.user_book_annotation import (
    UserBookAnnotationCreate,
    UserBookAnnotationJoinUserBook,
)
from src.core.di.containers import Container
from src.core.middlewares.models.base_response import BaseResponse
from src.core.utils.fastapi.get_responses import get_responses

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
