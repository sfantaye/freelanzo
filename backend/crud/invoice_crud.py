from sqlalchemy.orm import Session
from models import Invoice

# Create a new invoice
def create_invoice(db: Session, invoice_number: str, due_date: str, total_amount: float, client_id: int):
    invoice = Invoice(invoice_number=invoice_number, due_date=due_date, total_amount=total_amount, status="unpaid", client_id=client_id)
    db.add(invoice)
    db.commit()
    db.refresh(invoice)
    return invoice

# Get all invoices for a client
def get_invoices_by_client(db: Session, client_id: int):
    return db.query(Invoice).filter(Invoice.client_id == client_id).all()

# Get an invoice by ID
def get_invoice_by_id(db: Session, invoice_id: int):
    return db.query(Invoice).filter(Invoice.id == invoice_id).first()

# Update invoice status
def update_invoice_status(db: Session, invoice_id: int, status: str):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if invoice:
        invoice.status = status
        db.commit()
        db.refresh(invoice)
    return invoice

# Delete an invoice
def delete_invoice(db: Session, invoice_id: int):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if invoice:
        db.delete(invoice)
        db.commit()
    return invoice
