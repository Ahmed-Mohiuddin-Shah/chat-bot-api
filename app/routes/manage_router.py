from fastapi import APIRouter,  Request

router = APIRouter()

@router.post("/manage/add-doc")
async def add_pdf(request: Request):

    request_body = await request.json()

    print(request_body)

    

    return {
        "status": True,
        "data": None,
        "msg": "Add PDF"
    }