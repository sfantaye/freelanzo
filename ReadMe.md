# 💼 Freelanzo

**Freelanzo** is a powerful, no-fuss freelance invoice generator and income analytics dashboard. It lets freelancers create professional invoices, send payment reminders, and analyze income trends — all in one place.

Built with:
- 🦋 **FastAPI** – for robust backend APIs
- 🧬 **Reflex (Pynecone)** – for beautiful Python-native UI
- 🔗 **ExchangeRate.host API** – for multi-currency support
- ✉️ **Nylas API** – for sending email reminders (free tier)
- 📊 **Chart.js** – for elegant income analytics
- 📄 **PDFKit / ReportLab** – for invoice PDF export

---

## 🚀 Features

- ✍️ Create invoices with customizable fields
- 💱 Auto currency conversion using ExchangeRate.host
- 📥 Download invoices as PDF
- 📧 Schedule and send invoice reminders via email (Nylas)
- 📊 Visual income analytics (monthly/quarterly trends)
- 🛠️ Admin dashboard to manage invoices, clients, payments

---

## 🧩 Tech Stack

| Layer      | Tech            |
|------------|------------------|
| Frontend   | Reflex (Pynecone) |
| Backend    | FastAPI + SQLModel |
| DB         | PostgreSQL or SQLite |
| Emails     | Nylas API |
| Currency   | ExchangeRate.host |
| PDF Export | PDFKit / ReportLab |

---

## 📦 Installation

### 1. Clone the Repo
```bash
git clone https://github.com/sfantaye/freelanzo.git
cd freelanzo
