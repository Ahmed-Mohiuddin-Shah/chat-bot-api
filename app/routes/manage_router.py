from fastapi import APIRouter,  Request

router = APIRouter()

@router.get("/manage/add-doc")
async def add_pdf(request: Request):

    # Get the PDF file from the request
    # Save the PDF file to the disk
    # Return the success message

    return {
        "status": True,
        "data": None,
        "msg": "Add PDF"
    }