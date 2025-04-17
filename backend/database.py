import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, Field
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the database URL from the environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Initialize the database engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create the async session maker
SessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Create the database tables if they don't exist
async def init_db():
    async with engine.begin() as conn:
        # Create all tables from the models
        await conn.run_sync(SQLModel.metadata.create_all)

# Dependency to get the database session
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()

