from fastapi import FastAPI, UploadFile, File
from src.routes import router

app = FastAPI()

# Include the API router
app.include_router(router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Speech Recognition API"}
