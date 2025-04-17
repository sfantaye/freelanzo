from sqlalchemy.orm import Session
from models import IncomeAnalytics

# Create or update income analytics for a given month
def update_income_analytics(db: Session, month: str, total_income: float):
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

# Delete income analytics for a given month
def delete_income_analytics(db: Session, month: str):
    analytics = db.query(IncomeAnalytics).filter(IncomeAnalytics.month == month).first()
    if analytics:
        db.delete(analytics)
        db.commit()
    return analytics
