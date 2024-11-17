from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.upload import upload_router
from routes.ask import ask_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router
# In main.py, remove the trailing slash for the router prefix
app.include_router(upload_router, prefix="/upload", tags=["upload"])
app.include_router(ask_router, tags=["ask"])