from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.client_crud import create_client, get_clients, get_client_by_email, update_client, delete_client
from database import get_db
from models import Client

router = APIRouter()

# Create a new client
@router.post("/clients/", response_model=Client)
def create_new_client(name: str, email: str, phone: str = None, address: str = None, db: Session = Depends(get_db)):
    db_client = get_client_by_email(db, email=email)
    if db_client:
        raise HTTPException(status_code=400, detail="Client already exists")
    return create_client(db=db, name=name, email=email, phone=phone, address=address)

# Get all clients
@router.get("/clients/", response_model=list[Client])
def get_all_clients(db: Session = Depends(get_db)):
    return get_clients(db)

# Get client by email
@router.get("/clients/{email}", response_model=Client)
def get_client_by_email_route(email: str, db: Session = Depends(get_db)):
    db_client = get_client_by_email(db, email=email)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

# Update client information
@router.put("/clients/{client_id}", response_model=Client)
def update_client_route(client_id: int, name: str = None, email: str = None, phone: str = None, address: str = None, db: Session = Depends(get_db)):
    db_client = update_client(db, client_id, name, email, phone, address)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

# Delete a client
@router.delete("/clients/{client_id}", response_model=Client)
def delete_client_route(client_id: int, db: Session = Depends(get_db)):
    db_client = delete_client(db, client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client
