from fastapi import FastAPI
from . import models
from .database import engine
from .routes import auth_routes
import logging

logging.basicConfig(level=logging.DEBUG)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_routes.router)
