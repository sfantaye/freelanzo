from sqlalchemy.future import select
from sqlmodel import Session
from models import Payment, Invoice

# Create a new payment
def create_payment(db: Session, invoice_id: int, amount: float, method: str, status: str):
    payment = Payment(invoice_id=invoice_id, amount=amount, method=method, status=status)
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment

# Get all payments for an invoice
def get_payments_by_invoice(db: Session, invoice_id: int):
    result = db.execute(select(Payment).filter(Payment.invoice_id == invoice_id))
    return result.scalars().all()

# Update payment status
def update_payment_status(db: Session, payment_id: int, status: str):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if payment:
        payment.status = status
        db.commit()
        db.refresh(payment)
    return payment
