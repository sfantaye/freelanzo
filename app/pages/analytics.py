import reflex as rx

def AnalyticsPage():
    return rx.center(
        rx.vstack(
            rx.heading("Analytics", size="xl"),
            rx.text("Track your earnings, payment history, and trends."),
            # Example of a simple chart (can be integrated with data)
            rx.chart(
                data=[{"x": "Jan", "y": 100}, {"x": "Feb", "y": 150}, {"x": "Mar", "y": 200}],
                x="x",
                y="y",
                chart_type="line",
                title="Earnings Over Time",
            ),
            rx.text("Earnings Chart: Total earnings per month"),
        )
    )

# Define the route for the analytics page
analytics = rx.page(AnalyticsPage)
