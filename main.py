from fastapi import FastAPI
import models
from database import engine
from routes import router

app = FastAPI(title="Player Inventory API", version="1.0.0")
models.Base.metadata.create_all(bind=engine)
app.include_router(router)
