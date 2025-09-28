from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.models import Menu
from ..schemas.schemas import MenuCreate, MenuOut
from typing import List

router = APIRouter()

@router.get("/", response_model=List[MenuOut])
def list_menu(db: Session = Depends(get_db), include_unavailable: bool = False):
    """
    List all available menu items.
    Set include_unavailable=true to also return unavailable ones.
    """
    query = db.query(Menu)
    if not include_unavailable:
        query = query.filter(Menu.available == True)
    return query.order_by(Menu.name.asc()).all()

@router.post("/", response_model=MenuOut)
def add_menu_item(payload: MenuCreate, db: Session = Depends(get_db)):
    """
    Add a new menu item.
    """
    item = Menu(**payload.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.patch("/{menu_id}", response_model=MenuOut)
def update_menu_item(menu_id: int, payload: MenuCreate, db: Session = Depends(get_db)):
    """
    Update an existing menu item by ID.
    """
    item = db.query(Menu).get(menu_id)
    if not item:
        raise HTTPException(404, "Menu item not found")
    for key, value in payload.dict().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item
