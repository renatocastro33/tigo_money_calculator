# Tigo Money Calculator

A web application to calculate Tigo Money transfer fees, costs, and final amounts using Flask.

## 🚀 Features

- Calculate Tigo Money transaction costs dynamically.
- User-friendly web interface.
- Summary of transaction breakdown (fees, amounts).
- History of past calculations.
- Mobile and desktop responsive design.

---

## 💻 Technologies Used

- **Python 3.x**
- **Flask** (Web framework)
- **HTML5 / CSS3** (User interface)
- **Bootstrap** (Optional based on CSS observed)
- **Jinja2** (Template engine)

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your_username/tigo_money_calculator.git
cd tigo_money_calculator
```

### 2. Create Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## ⚙️ Usage

### 1. Run the Flask App

```bash
python app.py
```

### 2. Access the App

Go to `http://127.0.0.1:5000` in your browser.

---

## 📁 File Overview

| File/Folder                   | Description                                      |
|------------------------------|--------------------------------------------------|
| `app.py`                     | Main Flask app managing routes and logic        |
| `requirements.txt`            | Python dependencies                             |
| `static/styles_result.css`   | CSS styles for result page                      |
| `templates/index.html`       | Form for entering transaction details           |
| `templates/result.html`      | Displays calculated transaction breakdown       |
| `templates/history.html`     | (Optional) History of past transactions         |
| `templates/images/logo.jpeg` | Logo image                                      |

---

## 🌐 Pages

- **Home Page** (`/`): Input transaction amount and see calculated fees.
- **Results Page** (`/result`): Display fee breakdown and final amount.
- **History Page** (`/history`): (Optional) Past transactions if implemented.

---

## ⚙️ Requirements

- Python 3.x
- Flask (see `requirements.txt` for details)

---

## ✨ Screenshots

*(You can add screenshots of the app running here)*

---

## 📝 License

MIT License. Feel free to use, modify, and share!

---

## 🙌 Contributing

Contributions, issues, and feature requests are welcome!
