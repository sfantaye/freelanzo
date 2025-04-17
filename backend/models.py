from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import List, Optional


# ========================
# Client Model
# ========================
class Client(SQLModel, table=True):
    __tablename__ = "clients"

    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(index=True, unique=True)
    phone: Optional[str] = None
    address: Optional[str] = None

    invoices: List["Invoice"] = Relationship(back_populates="client")


# ========================
# Invoice Model
# ========================
class Invoice(SQLModel, table=True):
    __tablename__ = "invoices"

    id: int = Field(default=None, primary_key=True)
    invoice_number: str = Field(index=True, unique=True)
    issue_date: datetime = Field(default_factory=datetime.utcnow)
    due_date: datetime
    total_amount: float
    status: str  # 'paid', 'unpaid', 'overdue'

    client_id: int = Field(foreign_key="clients.id")
    client: Client = Relationship(back_populates="invoices")

    payments: List["Payment"] = Relationship(back_populates="invoice")

    def __str__(self):
        return f"Invoice #{self.invoice_number} - {self.status}"


# ========================
# Payment Model
# ========================
class Payment(SQLModel, table=True):
    __tablename__ = "payments"

    id: int = Field(default=None, primary_key=True)
    payment_date: datetime = Field(default_factory=datetime.utcnow)
    amount: float
    method: str  # 'credit', 'debit', 'cash', etc.
    status: str  # 'completed', 'pending'

    invoice_id: int = Field(foreign_key="invoices.id")
    invoice: Invoice = Relationship(back_populates="payments")


# ========================
# Income Analytics Model
# ========================
class IncomeAnalytics(SQLModel, table=True):
    __tablename__ = "income_analytics"

    id: int = Field(default=None, primary_key=True)
    total_income: float = 0.0
    month: str  # Format: 'YYYY-MM'

    payments: List[Payment] = Relationship(back_populates="analytics")

    def __str__(self):
        return f"Income Analytics for {self.month} - Total Income: {self.total_income}"
