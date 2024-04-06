from pydantic import BaseModel


class Product(BaseModel):
    cost: float
    url: str
