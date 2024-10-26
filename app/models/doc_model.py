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
