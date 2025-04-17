import reflex as rx

def IndexPage():
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to Freelancer Invoice Generator & Analytics", size="xl"),
            rx.text("Create and manage your freelance invoices, track payments, and view analytics."),
            rx.button("Get Started", on_click=lambda: rx.navigate("/dashboard"))
        )
    )

# Define the route for the index page
index = rx.page(IndexPage)
