from typing import Optional
from typing_extensions import Annotated
from pydantic import ConfigDict, BaseModel, Field
from pydantic.functional_validators import BeforeValidator

from bson import ObjectId

PyObjectId = Annotated[str, BeforeValidator(ObjectId)]

class DocModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    title: str
    description: str
    file_path: str
    file_name: str
    file_type: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "title": "Test",
                "description": "Test",
                "file_path": "Test",
                "file_name": "Test",
                "file_type": "Test",
            }
        }
