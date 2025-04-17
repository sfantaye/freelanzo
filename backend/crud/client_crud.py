from sqlalchemy.orm import Session
from models import Client

# Create a new client
def create_client(db: Session, name: str, email: str, phone: str = None, address: str = None):
    client = Client(name=name, email=email, phone=phone, address=address)
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

# Get all clients
def get_clients(db: Session):
    return db.query(Client).all()

# Get a client by email
def get_client_by_email(db: Session, email: str):
    return db.query(Client).filter(Client.email == email).first()

# Get client by ID
def get_client_by_id(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

# Update client information
def update_client(db: Session, client_id: int, name: str = None, email: str = None, phone: str = None, address: str = None):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client:
        if name:
            client.name = name
        if email:
            client.email = email
        if phone:
            client.phone = phone
        if address:
            client.address = address
        db.commit()
        db.refresh(client)
    return client

# Delete a client
def delete_client(db: Session, client_id: int):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client:
        db.delete(client)
        db.commit()
    return client
