from fastapi import FastAPI
from routes.client_routes import router as client_router
from routes.invoice_routes import router as invoice_router
from routes.payment_routes import router as payment_router
from routes.analytics_routes import router as analytics_router
from routes.email_routes import router as email_router
from database import engine
import models

# Create the FastAPI app
app = FastAPI()

# Include all the routes
app.include_router(client_router, prefix="/api", tags=["clients"])
app.include_router(invoice_router, prefix="/api", tags=["invoices"])
app.include_router(payment_router, prefix="/api", tags=["payments"])
app.include_router(analytics_router, prefix="/api", tags=["analytics"])
app.include_router(email_router, prefix="/api", tags=["emails"])

# Initialize the database (this will create the tables if they don't exist)
models.Base.metadata.create_all(bind=engine)

# Define a simple home route to verify the app is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the Freelancer Invoice Generator API"}

# Optional: Define a health check route
@app.get("/health")
def health_check():
    return {"status": "healthy"}
