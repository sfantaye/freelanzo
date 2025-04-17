from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.payment_crud import create_payment, get_payments_by_invoice, get_payment_by_id, update_payment_status, delete_payment
from database import get_db
from models import Payment

router = APIRouter()

# Create a new payment
@router.post("/payments/", response_model=Payment)
def create_new_payment(invoice_id: int, amount: float, method: str, status: str, db: Session = Depends(get_db)):
    return create_payment(db=db, invoice_id=invoice_id, amount=amount, method=method, status=status)

# Get all payments for an invoice
@router.get("/payments/invoice/{invoice_id}", response_model=list[Payment])
def get_payments_for_invoice(invoice_id: int, db: Session = Depends(get_db)):
    return get_payments_by_invoice(db, invoice_id)

# Get payment by ID
@router.get("/payments/{payment_id}", response_model=Payment)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = get_payment_by_id(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

# Update payment status
@router.put("/payments/{payment_id}/status", response_model=Payment)
def update_payment_status_route(payment_id: int, status: str, db: Session = Depends(get_db)):
    db_payment = update_payment_status(db, payment_id, status)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

# Delete a payment
@router.delete("/payments/{payment_id}", response_model=Payment)
def delete_payment_route(payment_id: int, db: Session = Depends(get_db)):
    db_payment = delete_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment
