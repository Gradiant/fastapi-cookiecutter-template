from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.get(
    "/status",
    description="Get API status."
)
def get_status():
    """Returns 200 and "OK" when the API is running."""
    return PlainTextResponse(status_code=200, content="OK")
