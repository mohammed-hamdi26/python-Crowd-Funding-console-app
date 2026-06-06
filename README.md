# 🌱 FundRaise — Crowdfunding Console App

> A Python-based console application for launching and managing crowdfunding campaigns, inspired by the global crowdfunding movement that raised over **$34 billion** worldwide in 2015.

---

## 📖 About the Project

Crowdfunding is the practice of funding a project or venture by raising small amounts of money from a large number of people, typically via the Internet. **FundRaise** brings this concept to life as a fully interactive console application where users can register, log in, and manage their own fundraising campaigns.

---

## ✨ Features

### 🔐 Authentication System

#### Registration
New users can create an account by providing:
- First name & Last name
- Email address
- Password & Confirm password
- Mobile phone number *(validated Egyptian phone numbers only)*

#### Login
- Registered users can log in using their **email and password**
- Access is granted only after account activation

---

### 📋 Project Management

Once logged in, users can:

| Feature | Description |
|---|---|
| ➕ Create a Project | Launch a new fundraising campaign |
| 👁️ View All Projects | Browse all active campaigns |
| ✏️ Edit a Project | Modify your own campaigns |
| 🗑️ Delete a Project | Remove your own campaigns |
| 🔍 Search by Date | *(Bonus)* Find campaigns by start/end date |

#### Each campaign includes:
- **Title** — Campaign name
- **Details** — Full description of the project
- **Total Target** — Funding goal (e.g. `250,000 EGP`)
- **Start Date** — Campaign start date *(validated format)*
- **End Date** — Campaign end date *(validated format)*

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Interface:** Console / CLI
- **Storage:** File-based or in-memory (no external database required)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/fundraise-app.git

# Navigate to the project directory
cd fundraise-app

# Run the application
python main.py
```

---

## 📁 Project Structure

```
fundraise-app/
│
├── main.py               # Entry point
├── auth/
│   ├── register.py       # Registration logic
│   └── login.py          # Login logic
├── projects/
│   ├── create.py         # Create a campaign
│   ├── view.py           # View all campaigns
│   ├── edit.py           # Edit a campaign
│   ├── delete.py         # Delete a campaign
│   └── search.py         # Search by date (bonus)
├── utils/
│   ├── validators.py     # Phone, email, date validation
│   └── helpers.py        # Shared utilities
└── data/
    └── users.json        # Stored user data
```

---

## ✅ Validation Rules

- **Egyptian Phone Numbers** — Must match the format: `01[0125][0-9]{8}`
- **Email** — Must follow standard email format
- **Passwords** — Must match during registration
- **Dates** — Must follow `YYYY-MM-DD` format; end date must be after start date

---

## 👥 Contributors

| Name | Role |
|---|---|
| Your Name | Developer |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

> *"The secret to getting ahead is getting started."* — Mark Twain
