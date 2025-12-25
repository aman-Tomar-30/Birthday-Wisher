# 🎉 Birthday Wisher 

Birthday Wisher is a simple yet powerful Python automation project that helps you automatically send or generate birthday wishes based on stored birthday data. The program checks today’s date, matches it with saved birthdays, and generates personalized birthday messages using pre-defined templates.

This project is ideal for beginners who want to practice:
- Python file handling
- CSV data processing
- Date and time handling
- Automation concepts

---

## 🚀 Features

- 📅 Reads birthday details from a CSV file  
- 🧠 Automatically checks today’s date  
- ✉️ Generates personalized birthday wishes  
- 📝 Uses reusable and customizable letter templates  
- 🐍 Written in pure Python (easy to understand and modify)  
- 🔄 Easily extendable (email, WhatsApp, scheduler, etc.)

---

## 📂 Project Structure

- **main.py** → Core Python script that runs the birthday logic  
- **birthdays.csv** → Stores birthday data of people  
- **letter_templates/** → Contains birthday message templates  
- **README.md** → Project documentation  

---

## 🧪 Technologies Used

- **Python 3**
- **CSV module**
- **Datetime module**
- **Random module**
- **File handling**

No external libraries are required.

---

## 📄 birthdays.csv Format

The CSV file should contain the following columns:

| name | year | month | day | email |
|------|------|-------|-----|-------|

### Example:

> The program matches `month` and `day` with today’s date.

---

## ✏️ Letter Templates

Templates are stored inside the `letter_templates` folder.

### Example Template (`letter_1.txt`)


> `[NAME]` is automatically replaced with the person’s name.

---

## 🛠 Installation & Setup

### ✅ Prerequisites
- Python 3.7 or higher
- Git installed

