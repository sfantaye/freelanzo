from sqlalchemy.future import select
from sqlmodel import Session
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
    result = db.execute(select(Client))
    return result.scalars().all()

# Get a client by email
def get_client_by_email(db: Session, email: str):
    return db.query(Client).filter(Client.email == email).first()

# Get client by ID
def get_client_by_id(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()
