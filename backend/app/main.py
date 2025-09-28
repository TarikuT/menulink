from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import API_TITLE, API_DEBUG
from .database import Base, engine
from .routes import menu, order

# Create tables (MVP only; later replace with Alembic migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(title=API_TITLE, debug=API_DEBUG)

# ✅ Enable CORS so frontend (localhost:3000) can talk to backend (localhost:8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # customer app
        "http://localhost:3001"   # dashboard app
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(menu.router, prefix="/menu", tags=["Menu"])
app.include_router(order.router, prefix="/order", tags=["Order"])

@app.get("/")
def root():
    return {"message": "MenuLink QR Ordering is running 🚀"}
