from fastapi import APIRouter
from .usuario import router as usuario_router

router = APIRouter()
router.include_router(usuario_router)

__all__ = ["router"]
