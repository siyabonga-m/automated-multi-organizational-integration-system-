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
from pydantic import BaseModel

class HealthVerifyRequest(BaseModel):
    passport_number: str
    has_yellow_fever_vaccine: bool
    temperature: float

class CustomsDeclarationRequest(BaseModel):
    passport_number: str
    item_description: str
    declared_value_emalangeni: float
    tax_paid_at_post_office: bool

class FinalClearanceRequest(BaseModel):
    passport_number: str
    driver_name: str
    passport_cleared: bool
    health_cleared: bool
