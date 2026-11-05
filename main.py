import uvicorn
from fastapi import FastAPI

# Initialize the FastAPI app for the Integrated Border Management System
app = FastAPI(
    title="CSC411: Integrated Border Management System", 
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "API Gateway is running successfully."}
