from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from bson import ObjectId
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

# Clase que hereda de ObjectId para validación personalizada
# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError('Invalid ObjectId')
#         return str(v)
    
PyObjectId = Annotated[str, BeforeValidator(str)]
    

class Task(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    title: str
    description: Optional[str] = None
    completed: bool = False
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "title": "Task title",
                "description": "Task description",
                "completed": False,
            }
        },
    )


class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "title": "Task title",
                "description": "Task description",
                "completed": False,
            }
        },
    )