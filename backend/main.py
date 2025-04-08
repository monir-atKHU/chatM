# backend/main.py
from fastapi import FastAPI
from . import models, database
from .routes import auth_routes
from .routes import auth_routes, chat_routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(auth_routes.router)
app.include_router(chat_routes.router)

@app.get("/")
def root():
    return {"message": "API is live"}

