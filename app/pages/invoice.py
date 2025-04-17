import reflex as rx

def InvoicePage():
    return rx.center(
        rx.vstack(
            rx.heading("Create Invoice", size="xl"),
            rx.form(
                rx.input(label="Client Name", name="client_name"),
                rx.input(label="Service Description", name="description"),
                rx.input(label="Amount", name="amount", type="number"),
                rx.input(label="Due Date", name="due_date", type="date"),
                rx.button("Generate Invoice", on_click=lambda: generate_invoice()),
            ),
            rx.heading("Existing Invoices", size="md"),
            # Display a list of invoices (this can be populated dynamically)
            rx.text("No invoices generated yet. Create one above."),
        )
    )

# Simulate the invoice generation logic
def generate_invoice():
    print("Invoice generated!")
    # Add logic to call the backend and create an invoice
    # Then update the list of existing invoices.

# Define the route for the invoice page
invoice = rx.page(InvoicePage)
