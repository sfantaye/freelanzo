from sqlalchemy.future import select
from sqlmodel import Session
from models import IncomeAnalytics, Payment

# Create or update income analytics for a given month
def update_income_analytics(db: Session, month: str):
    total_income = db.execute(select(Payment).filter(Payment.payment_date.like(f"{month}%"))).scalars().sum(Payment.amount)
    
    analytics = db.query(IncomeAnalytics).filter(IncomeAnalytics.month == month).first()
    if analytics:
        analytics.total_income = total_income
        db.commit()
        db.refresh(analytics)
    else:
        analytics = IncomeAnalytics(month=month, total_income=total_income)
        db.add(analytics)
        db.commit()
        db.refresh(analytics)
    
    return analytics

# Get income analytics for a given month
def get_income_analytics(db: Session, month: str):
    return db.query(IncomeAnalytics).filter(IncomeAnalytics.month == month).first()
