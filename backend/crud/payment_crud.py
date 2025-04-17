from sqlalchemy.orm import Session
from models import Payment

# Create a new payment
def create_payment(db: Session, invoice_id: int, amount: float, method: str, status: str):
    payment = Payment(invoice_id=invoice_id, amount=amount, method=method, status=status)
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment

# Get all payments for an invoice
def get_payments_by_invoice(db: Session, invoice_id: int):
    return db.query(Payment).filter(Payment.invoice_id == invoice_id).all()

# Get payment by ID
def get_payment_by_id(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.id == payment_id).first()

# Update payment status
def update_payment_status(db: Session, payment_id: int, status: str):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if payment:
        payment.status = status
        db.commit()
        db.refresh(payment)
    return payment

# Delete a payment
def delete_payment(db: Session, payment_id: int):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if payment:
        db.delete(payment)
        db.commit()
    return payment
