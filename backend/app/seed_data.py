from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models.models import Menu

def seed_menu():
    db: Session = SessionLocal()
    items = [
        {"name": "Margherita Pizza", "description": "Classic pizza with cheese", "price": 8.5, "available": True},
        {"name": "Cheeseburger", "description": "Juicy beef burger with cheese", "price": 6.5, "available": True},
        {"name": "Caesar Salad", "description": "Fresh lettuce, croutons, parmesan", "price": 5.0, "available": True},
        {"name": "Cappuccino", "description": "Hot Italian coffee with foam", "price": 3.0, "available": True},
        {"name": "Chocolate Cake", "description": "Rich chocolate dessert", "price": 4.5, "available": True},
    ]

    for item in items:
        exists = db.query(Menu).filter_by(name=item["name"]).first()
        if not exists:
            db.add(Menu(**item))
    db.commit()
    db.close()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  # ensure tables exist
    seed_menu()
    print("✅ Menu seeded successfully!")
