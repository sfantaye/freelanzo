import reflex as rx
from pages.index import index
from pages.dashboard import dashboard
from pages.invoice import invoice
from pages.analytics import analytics

# Initialize the Reflex app
app = rx.App()

# Add pages to the app (these pages will be routed based on the URL)
app.add_page(index, route="/")
app.add_page(dashboard, route="/dashboard")
app.add_page(invoice, route="/invoice")
app.add_page(analytics, route="/analytics")

# Run the app
if __name__ == "__main__":
    app.run()
