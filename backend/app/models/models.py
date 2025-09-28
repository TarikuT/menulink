from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DECIMAL, TIMESTAMP, func
from sqlalchemy.orm import relationship
from ..database import Base

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    price = Column(DECIMAL(10, 2), nullable=False)
    available = Column(Boolean, default=True)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    table_number = Column(Integer, nullable=True)
    status = Column(String(20), default="pending")  # pending | confirmed | completed | cancelled
    created_at = Column(TIMESTAMP, server_default=func.now())

    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"))
    menu_id = Column(Integer, ForeignKey("menus.id"))
    quantity = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="items")
