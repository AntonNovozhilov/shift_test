from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from shift.core.user import current_superuser
from shift.core.db import get_async_session
from shift.crud.grade.grade import grade_crud
from shift.models.grade import Grade
from shift.schemas.grade import GradeCreate, Grade
from shift.api.api_v1.validation import check_unique_title


grade = APIRouter(tags=["grade"], prefix="/grade")


@grade.post("/", response_model=Grade, dependencies=[Depends(current_superuser)])
async def post_grade(
    data: GradeCreate, session: AsyncSession = Depends(get_async_session)
) -> Grade:
    """Только для администраторов. Создание должности."""
    await check_unique_title(data.title, session)
    grader = await grade_crud.create(session, data)
    return grader
