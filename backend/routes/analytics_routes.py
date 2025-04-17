from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.analytics_crud import update_income_analytics, get_income_analytics, delete_income_analytics
from database import get_db
from models import IncomeAnalytics

router = APIRouter()

# Update income analytics for a given month
@router.post("/analytics/{month}", response_model=IncomeAnalytics)
def update_analytics(month: str, total_income: float, db: Session = Depends(get_db)):
    return update_income_analytics(db, month, total_income)

# Get income analytics for a given month
@router.get("/analytics/{month}", response_model=IncomeAnalytics)
def get_analytics(month: str, db: Session = Depends(get_db)):
    db_analytics = get_income_analytics(db, month)
    if db_analytics is None:
        raise HTTPException(status_code=404, detail="Analytics not found")
    return db_analytics

# Delete income analytics for a given month
@router.delete("/analytics/{month}", response_model=IncomeAnalytics)
def delete_analytics(month: str, db: Session = Depends(get_db)):
    db_analytics = delete_income_analytics(db, month)
    if db_analytics is None:
        raise HTTPException(status_code=404, detail="Analytics not found")
    return db_analytics
