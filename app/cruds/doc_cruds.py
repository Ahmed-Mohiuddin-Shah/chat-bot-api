from app.models.doc_model import DocModel
from app.utils.database import get_db


async def add_doc(title: str):

    doc = DocModel(
        title=title,
        description="Test",
        file_path="Test",
        file_name="Test",
        file_type="Test",
    )

    db = await get_db()

    # check if collection exists
    if "docs" not in await db.list_collection_names():
        print("Creating collection")
        await db.create_collection("docs")

    # print docs in the collection
    docs = db["docs"].find()
    async for docets in docs:
        print(docets)

    docet = await db["docs"].insert_one(doc.model_dump())
    new_doc = await db["docs"].find_one({"_id": docet.inserted_id})

    return new_doc

async def get_pdf_names():
    db = await get_db()
    docs = db["docs"].find()

    pdfs = []
    async for docet in docs:
        pdfs.append(
            {
                "id": str(docet["_id"]),
                "title": docet["title"],
            }
        )

    return pdfs