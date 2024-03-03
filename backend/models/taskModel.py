from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

# Clase que hereda de ObjectId para validación personalizada
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return str(v)
    

class Task(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    title: str
    description: Optional[str] = None
    completed: bool = False

    class Config:
        orm_mode = True  # Configuración para habilitar el modo ORM
        allow_population_by_field_name = True  # Permite la población por nombre de campo
        json_encoders = {
            ObjectId: str  # Convierte ObjectId a cadena al serializar a JSON
        }


class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

    # class Config:
    #     orm_mode = True
    #     allow_population_by_field_name = True
    #     json_encoders = {
    #         ObjectId: str
    #     }