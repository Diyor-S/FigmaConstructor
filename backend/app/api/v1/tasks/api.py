from fastapi import APIRouter

router = APIRouter(tags=["tasks/"])


@router.get('/')
def get_tasks() -> str:
    return "Hello World"
