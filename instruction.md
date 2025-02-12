---

# **SQL Database - Windows Setup Instructions**  
[![Watch the video](https://github.com/user-attachments/assets/906d4e8f-7a71-40d2-b29e-b7d5df4b96fe)](https://youtu.be/NJxkTJFRgvM)

## **Description**  

The **SQL Database** project provides functionality to manage databases with an interactive command-line interface. It includes features for **automatic dependency installation**, making it easy to set up.  

However, if the automatic installation fails, you can follow the **manual setup instructions** below to ensure all dependencies are installed properly.

---

## **1. Clone the Repository**  

To get started, first clone the repository from GitHub.  

### **Prerequisites**  

- **Git**: Ensure Git is installed on your system. If not, download and install it from [Git Downloads](https://git-scm.com/downloads).  

### **Clone the Repository**  

1. Open **Command Prompt (cmd)** or **PowerShell**.
2. Run the following command to clone the repository:  

   ```bash
   git clone https://github.com/mishra9759harshit/sqldatabase.git
   ```

3. Navigate to the project folder:  

   ```bash
   cd sqldatabase
   ```

---

## **2. Install Dependencies**  

### **Automatic Installation (Recommended)**  

The project includes an **automatic dependency installer**. Simply run:

```bash
python run.py
```

If the script detects missing dependencies, it will attempt to install them automatically.

### **Manual Installation (If Automatic Installation Fails)**  

If the automatic installation fails, follow these steps:

#### **Step 1: Install Python**  

1. Download and install **Python 3.6 or later** from the official [Python website](https://www.python.org/downloads/).
2. During installation, **check the box to add Python to PATH**.

#### **Step 2: Install Git**  

If you haven't installed **Git**, download and install it from [Git Downloads](https://git-scm.com/downloads).  

#### **Step 3: Install Required Python Dependencies**  

Run the following command to install the necessary Python packages:

```bash
pip install plotext rich requests pyreadline
```

If you encounter errors with `readline`, install `pyreadline3` instead:

```bash
pip install pyreadline3
```

This will install:
- **plotext** → For terminal-based plotting.
- **rich** → For beautiful CLI text formatting, tables, and progress bars.
- **requests** → For handling HTTP requests.
- **pyreadline3** → A readline alternative for Windows.

#### **Step 4: Verify Dependencies**  

To ensure everything is installed correctly, run:

```bash
pip freeze
```

If you see all the required packages listed, you're good to go!

---

## **3. Running `run.py` with Interactive Visuals**  

### **Step 1: Run the Script**  

1. Ensure you're inside the project folder.
2. Run:

   ```bash
   python run.py
   ```

### **Step 2: Interacting with the Script**  

When running, the script provides **interactive features** like:
- **Tables & Styled Outputs** using `rich.table`.
- **Progress Bars & Animated Text**.
- **ASCII-Based Plots** using `plotext`.

You’ll see options in the terminal like:

```
[bold cyan]Welcome to the Interactive SQL Database![/bold cyan]
Please select an option:
1. View Data
2. Generate Plot
3. Exit

[bold yellow]Enter your choice:[/bold yellow]
```

---

## **4. Troubleshooting**  

### **Issue 1: `readline` Import Error on Windows**  
Try installing `pyreadline3` instead:  

```bash
pip install pyreadline3
```

### **Issue 2: Missing Dependencies**  
Run:

```bash
pip install --upgrade plotext rich requests pyreadline3
```

### **Issue 3: Python Not Found in Terminal**  
Ensure Python is added to the **Windows PATH**. If not, reinstall Python and **check the "Add to PATH" option during installation**.

---

## **4. Try SQL Database Graphical Version** 🎨  
![Description of GIF](https://github.com/mishra9759harshit/SQL-DATABASE/raw/main/Screenshot's/1%20(4).png?raw=true)

If you prefer a **GUI version**, try our **Graphical SQL Database Manager**!  

### 🌟 **[![Try GUI Version](https://img.shields.io/badge/Try_Graphical_Version-Click_Here-green?style=for-the-badge)](https://github.com/mishra9759harshit/SQL-DATABASE)**  

🔹 **Easier navigation**  
🔹 **Visual database operations**  
🔹 **Drag-and-drop support**  

Click the badge above to visit the **GUI repository**! 🚀  

---


## **6. License & Author**  

📌 **Developed by**: **Harshit Mishra**  
📜 **License**: See [LICENSE](LICENSE)  

---


