from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.models import Order, OrderItem, Menu
from ..schemas.schemas import OrderCreate, OrderOut
from typing import List

router = APIRouter()

@router.post("/", response_model=OrderOut)
def place_order(payload: OrderCreate, db: Session = Depends(get_db)):
    """
    Place a new order with items.
    """
    # Check menu availability
    menu_ids = [i.menu_id for i in payload.items]
    menus = db.query(Menu).filter(Menu.id.in_(menu_ids), Menu.available == True).all()
    found_ids = {m.id for m in menus}
    missing = [mid for mid in menu_ids if mid not in found_ids]
    if missing:
        raise HTTPException(400, f"Menu items not available: {missing}")

    # Create order
    order = Order(table_number=payload.table_number, status="pending")
    db.add(order)
    db.flush()  # assign ID before commit

    for item in payload.items:
        db.add(OrderItem(order_id=order.id, menu_id=item.menu_id, quantity=item.quantity))

    db.commit()
    db.refresh(order)
    return order

@router.get("/", response_model=List[OrderOut])
def list_orders(db: Session = Depends(get_db), status: str | None = None):
    """
    List all orders (optionally filter by status).
    """
    query = db.query(Order)
    if status:
        query = query.filter(Order.status == status)
    return query.order_by(Order.created_at.desc()).all()

@router.post("/{order_id}/status/{new_status}", response_model=OrderOut)
def set_status(order_id: int, new_status: str, db: Session = Depends(get_db)):
    """
    Update the status of an order (pending, confirmed, completed, cancelled).
    """
    if new_status not in {"pending", "confirmed", "completed", "cancelled"}:
        raise HTTPException(400, "Invalid status")
    order = db.query(Order).get(order_id)
    if not order:
        raise HTTPException(404, "Order not found")
    order.status = new_status
    db.commit()
    db.refresh(order)
    return order
