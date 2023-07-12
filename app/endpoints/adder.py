from app.endpoints.router import router
from app.models.adder import AdderResponse, AdderRequest


@router.get("/add", response_model=AdderResponse)
async def adder(request: AdderRequest) -> dict[str, int]:
    return {"sum": request.x + request.y}
