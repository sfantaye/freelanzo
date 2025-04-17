from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.email_crud import send_invoice_reminder
from database import get_db

router = APIRouter()

# Send invoice reminder to the client
@router.post("/email/reminder/{invoice_id}")
def send_reminder(invoice_id: int, db: Session = Depends(get_db)):
    # Get invoice details
    db_invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    
    # Get client email
    client_email = db_invoice.client.email

    # Send email reminder
    reminder_response = send_invoice_reminder(client_email, db_invoice.invoice_number, db_invoice.due_date)
    
    return {"message": "Reminder sent successfully", "data": reminder_response}
