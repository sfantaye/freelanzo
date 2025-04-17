from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.invoice_crud import create_invoice, get_invoices_by_client, get_invoice_by_id, update_invoice_status, delete_invoice
from database import get_db
from models import Invoice

router = APIRouter()

# Create a new invoice
@router.post("/invoices/", response_model=Invoice)
def create_new_invoice(invoice_number: str, due_date: str, total_amount: float, client_id: int, db: Session = Depends(get_db)):
    return create_invoice(db=db, invoice_number=invoice_number, due_date=due_date, total_amount=total_amount, client_id=client_id)

# Get all invoices for a client
@router.get("/invoices/client/{client_id}", response_model=list[Invoice])
def get_invoices_for_client(client_id: int, db: Session = Depends(get_db)):
    return get_invoices_by_client(db, client_id)

# Get an invoice by ID
@router.get("/invoices/{invoice_id}", response_model=Invoice)
def get_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = get_invoice_by_id(db, invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice

# Update invoice status
@router.put("/invoices/{invoice_id}/status", response_model=Invoice)
def update_invoice_status_route(invoice_id: int, status: str, db: Session = Depends(get_db)):
    db_invoice = update_invoice_status(db, invoice_id, status)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice

# Delete an invoice
@router.delete("/invoices/{invoice_id}", response_model=Invoice)
def delete_invoice_route(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = delete_invoice(db, invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice
