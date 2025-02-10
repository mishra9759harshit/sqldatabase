# SQLDatabase Termux Program

This is a **SQL Database program** designed to run in **Termux** on Android devices. The program allows you to interact with SQL databases directly from your phone using Python. It features a simple, interactive command-line interface (CLI) to practice SQL queries, take quizzes, and track your progress.

### **Advantages**:
- **Lightweight and Mobile**: Run SQL databases directly on your mobile device via Termux.
- **Interactive CLI**: Practice and learn SQL commands interactively.
- **SQL Quiz Mode**: Test your knowledge with an interactive quiz.
- **Progress Tracking**: Track your learning progress with visual graphs.
- **Developer-friendly**: Modify or extend the functionality as needed.

---

## **Requirements**

To run this program on your Android device, you'll need to install **Termux**, set up the environment, and install Python along with the necessary dependencies.

### **1. Install Termux**

- **Install Termux from the Google Play Store or F-Droid**:
  - [Download Termux from Google Play Store](https://play.google.com/store/apps/details?id=com.termux)
  - [Download Termux from F-Droid](https://f-droid.org/packages/com.termux/)
  
  Once installed, open Termux to start the setup.

### **2. Set Up the Termux Environment**

#### **Update Termux Packages**
First, update the Termux package repository to ensure you have the latest version of all packages:

```bash
pkg update
pkg upgrade
```

#### **Install Dependencies**

To run the program, you need to install Python and a few required libraries. Execute the following commands:

```bash
pkg install python
pkg install git
pkg install clang
pkg install libffi-dev
pkg install libssl-dev
pkg install build-essential
```

These packages will set up the Python environment and essential tools for compiling any dependencies.

### **3. Install Python**

Python should already be installed when you run `pkg install python`. However, you can check the Python version with:

```bash
python --version
```

It should show a Python 3 version (e.g., `Python 3.x.x`).

### **4. Clone the Repository**

Next, clone the **SQLDatabase** repository from GitHub:

```bash
git clone https://github.com/mishra9759harshit/sqldatabase.git
```

This command will create a folder named `sqldatabase` in your Termux home directory.

### **5. Navigate to the Project Directory**

Move to the `sqldatabase` directory:

```bash
cd sqldatabase
```

### **6. Install Python Dependencies**

Install the required Python libraries listed in the `requirements.txt` file. If no `requirements.txt` exists, manually install the necessary packages:

```bash
pip install sqlite3
pip install rich
pip install matplotlib
```

These dependencies are used for the program's SQL functionality, the interactive CLI, and visualizations.

### **7. Run the Program**

Now that everything is set up, you can run the program using:

```bash
python run.py
```

This will launch the interactive SQL database program where you can practice queries, take quizzes, and track your progress.

---

## **Developer Information**

- **Developer**: Harshit Mishra
- **Project Repository**: [https://github.com/mishra9759harshit/sqldatabase.git](https://github.com/mishra9759harshit/sqldatabase.git)
- **License**: MIT License (feel free to contribute or use the code with attribution)

### **Contact Information**:
- **Email**: [mishra9759harshit@gmail.com](mailto:mishra9759harshit@gmail.com)

---

## **Additional Notes**

- The program is designed to run on **Termux**, but you can adapt it for other environments with minor modifications.
- **Future Features**: Support for more databases, advanced query handling, and more interactive modes.
- **Feedback**: If you encounter issues or have suggestions, feel free to open an issue on the GitHub repository.

---

Thank you for using the **SQLDatabase Termux Program**! We hope it helps you practice and learn SQL directly on your mobile device.
```
