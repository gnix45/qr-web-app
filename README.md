# QR Code Generator Web App

A simple, elegant, and minimalistic QR Code Generator built with **Flask** and **Bootstrap**. This web app allows users to generate QR codes from text or URLs.

## 🚀 Features
- 🖼️ **Generate QR codes** from any text or URL
- 🎨 **Elegant UI** with Bootstrap
- 📱 **Responsive Design** (works on mobile & desktop)
- 🖥️ **Fast & Lightweight** using Flask
- 🌐 **Easy Deployment on Render**

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask App
```bash
python app.py
```
🔗 Open **http://127.0.0.1:5000/** in your browser.

---

## 📦 Deployment on Render

1. Push your project to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```
2. Go to **[Render.com](https://render.com/)** & create a **New Web Service**.
3. Connect your GitHub repo.
4. Set the **Start Command** to:
   ```bash
   gunicorn app:app
   ```
5. Click **Deploy** & get your live URL!

---

## 📂 Project Structure
```
📦 QR-Code-Generator
├── 📄 app.py          # Flask application
├── 📂 templates       # HTML templates
│   ├── index.html     # Main UI
├── 📄 requirements.txt # Dependencies
├── 📄 README.md        # Project documentation
```

---

## 📝 License
This project is open-source and free to use.

👨‍💻 **Made with ❤️ by [Your Name]**

