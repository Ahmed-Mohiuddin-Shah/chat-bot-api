import os

from fastapi import APIRouter,  Request
from app.cruds.doc_cruds import add_doc

router = APIRouter()

@router.post("/add-doc")
async def add_pdf(request: Request):

    try:
        # Next form data
        form = await request.form()
        # print(form)

        # Save the file
        pdf = form["pdf"]
        # print(pdf.filename)

        # check path exists
        if not os.path.exists("app/static"):
            os.makedirs("app/static")

        # Save the file
        with open(f"app/static/{pdf.filename}", "wb") as f:
            f.write(await pdf.read())

        # Add the file to the database
        new_doc = await add_doc(pdf.filename)

        print(new_doc)

        return {
            "status": True,
            "data": None,
            "msg": "Add PDF"
        }
    except Exception as e:
        print(e)
        return {
            "status": False,
            "data": None,
            "msg": str(e)
        }