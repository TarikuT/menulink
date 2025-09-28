from pydantic import BaseModel, Field
from typing import List, Optional

# -------- Menu --------
class MenuCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0)
    available: bool = True

class MenuOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    available: bool

    class Config:
        from_attributes = True  # works with SQLAlchemy models

# -------- Order --------
class OrderItemIn(BaseModel):
    menu_id: int
    quantity: int = Field(gt=0)

class OrderCreate(BaseModel):
    table_number: Optional[int] = None
    items: List[OrderItemIn]

class OrderOut(BaseModel):
    id: int
    table_number: Optional[int]
    status: str

    class Config:
        from_attributes = True
