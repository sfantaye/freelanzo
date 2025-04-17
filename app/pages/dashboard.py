import reflex as rx

def DashboardPage():
    return rx.center(
        rx.vstack(
            rx.heading("Dashboard", size="xl"),
            rx.text("Manage your invoices, payments, and track analytics here."),
            rx.button("View Invoices", on_click=lambda: rx.navigate("/invoice")),
            rx.button("View Analytics", on_click=lambda: rx.navigate("/analytics")),
        )
    )

# Define the route for the dashboard page
dashboard = rx.page(DashboardPage)
