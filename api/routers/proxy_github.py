import logging
from fastapi import APIRouter


logger = logging.getLogger("uvicorn.error")
router = APIRouter(prefix='/users', tags=['Users'])