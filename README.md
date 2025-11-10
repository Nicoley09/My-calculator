# ⚡ Cool Calculator

A simple, friendly **Streamlit** calculator app with a polished UI — perfect for quick arithmetic and for learning how to deploy Streamlit projects.

---

## 🚀 What this is

This repository contains a lightweight Streamlit app (`app.py`) that lets users perform basic arithmetic (addition, subtraction, multiplication, division) via a modern web interface. It includes a styled title, emoji separators ("sticks"), and user-friendly error handling.

---

## ✨ Features

* Add, subtract, multiply, divide
* Prevents division by zero with an error message
* Clean UI using Streamlit widgets (`number_input`, `radio`, `button`)
* Decorative title and separators for a fun look

---

## 📦 Requirements

* Python 3.8+
* `streamlit` (install with pip)

Install dependencies:

```bash
pip install streamlit
```

---

## 🧾 Files

* `app.py` — The Streamlit app source code
* `README.md` — This file

---

## 🛠️ How to run (step-by-step)

1. Clone or download this repository to your local machine.

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Install Streamlit:

```bash
pip install streamlit
```

4. Run the app:

```bash
streamlit run app.py
```

5. A browser tab will open (usually at `http://localhost:8501`) showing the Cool Calculator interface. Enter two numbers, pick an operator, and click **Calculate**.

---

## 🔍 Usage examples

* Add 3 + 5: enter `3` and `5`, choose **➕ Add**, click **Calculate** → result shown.
* Divide by zero: entering `10` and `0` with **➗ Divide** shows an error message.

---

## 🎨 Customization ideas

* Add a calculation history panel (storing results in `st.session_state`)
* Add keyboard input or hotkeys
* Support for more advanced math functions (power, sqrt, modulo)
* Add animations or dark/light theme support

---

## 🤝 Contributing

PRs and suggestions are welcome! For small changes, open a pull request. For larger features, open an issue first to discuss.

---

## 🧾 License

This project is provided under the MIT License. See `LICENSE` for details (or add your preferred license).

---

## ✉️ Contact

If you want help customizing the app or want features added, open an issue or contact the project owner.

---

Made with ❤️ and Streamlit.
