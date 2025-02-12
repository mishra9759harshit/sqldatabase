# MIT License
# 
# Copyright (c) [2025] [Harshit Mishra/Harshit's SecureCoder laboratory]
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is provided to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# Developer's Rights and Conditions of Use & Modification
#
# As a developer or user of the Software, the following terms and conditions apply:
# 
# 1. **Conditions of Use**:
#    - **Free Usage**: You are granted the right to use the Software freely for personal, commercial, academic, or professional purposes. However, you must abide by all the terms stated in this license.
#    - **Attribution**: The original copyright notice, this license, and any associated legal documentation must be retained and included when redistributing or using the Software.
#    - **Modification**: You are allowed to modify the Software. Any modification made must remain under this license and must include the original copyright notice, along with any modifications made to the code. You are required to clearly identify any changes made to the Software.
# 
# 2. **Developer's Rights**:
#    - **Exclusive Rights**: The developers of the Software retain the right to control and oversee the use and distribution of the Software. These rights include the right to modify, update, or withdraw the Software at any time.
#    - **Ownership of Contributions**: By contributing to the Software, you agree to transfer full ownership of the contributed code, documentation, or modifications to the project owner(s). Contributors waive any right to claim ownership or further rights over the contributed code.
#    - **Commercial Use Rights**: The project owner(s) reserve the right to monetize, sublicense, or distribute the Software in any way deemed fit. If you are modifying or distributing the Software, you may not impose any additional fees or royalties unless explicitly agreed upon by the project owner(s).
#    - **Derivative Works**: Any derivative works created from this Software must be made available under the same MIT License, and you must maintain the integrity of the original Software's attribution.
#    - **License Enforcement**: The project owner(s) have the right to enforce this license, including initiating legal proceedings for any breach of the terms.

# 3. **Conditions of Modification**:
#    - **Transparency and Integrity**: Any changes made to the Software must be clearly marked and documented. If distributing a modified version, the modified Software must still be freely available under the MIT License.
#    - **Redistribution**: Redistribution of the Software, whether modified or not, must include the full license and copyright notice, and clearly state any changes made to the original Software. You may not impose any additional terms or conditions that restrict the rights granted by this license.
#    - **No Additional Restrictions**: You may not add additional restrictions on the Software that would prevent users or other developers from exercising the rights granted under this license.
#    - **No Takedown Policy**: Under no circumstances shall you remove, obscure, or alter the copyright and license notices included in the Software.

# 4. **Prohibited Uses**:
#    The Software must not be used for:
#    - **Illegal Activities**: You may not use the Software to engage in, support, or distribute illegal activities or software that violates any laws.
#    - **Malicious Use**: You must not use, modify, or distribute the Software in a way that could harm individuals, systems, or data (e.g., using the Software for malware, data theft, or unauthorized access).
#    - **Impersonation**: You may not use the Software to falsely represent yourself or your affiliation with the original authors of the Software.

# 5. **Disclaimer of Warranty**:
#    - The Software is provided "as is", without warranty of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, and non-infringement. The authors are not liable for any damages that may arise from using the Software, including but not limited to damages resulting from the use, modification, or distribution of the Software.

# 6. **Limitation of Liability**:
#    - In no event will the authors, copyright holders, or contributors be liable for any damages, losses, or other liabilities, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the Software, its use, or other dealings in the Software.
#    - You acknowledge that any and all risks associated with the use of the Software are your own responsibility, and you agree to indemnify and hold harmless the authors and contributors.

# 7. **Modifications and Updates**:
#    - You may submit modifications, improvements, or bug fixes to the Software. However, by doing so, you agree that the project owner(s) may incorporate your contributions into the Software, and such contributions will be subject to this license.
#    - **Version Control**: Any new version or fork of the Software must maintain clear versioning to differentiate from previous versions.

# 8. **Termination of License**:
#    - The rights granted by this license are automatically terminated if you violate any of its terms. Upon termination, you must immediately cease all use, modification, and distribution of the Software.
#    - The termination of rights does not affect any rights or obligations that have accrued prior to termination.

# 9. **Miscellaneous**:
#    - **Governing Law**: This license is governed by the laws of the jurisdiction where the project owner(s) are located, and any legal disputes will be handled under those laws.
#    - **Severability**: If any provision of this license is found to be invalid or unenforceable, the remaining provisions will continue in full force and effect.

# 8. Acknowledgements:
#    - The Software may include contributions from multiple developers or organizations. These contributions are acknowledged in the appropriate sections (e.g., documentation, credits).
# By using or modifying the Software, you agree to comply with the terms of the MIT License and the conditions of use and modification stated above. If you disagree, you may not use or distribute the Software.

import sqlite3
import os
import time
import random
import getpass
import plotext as plt  
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
import requests
from rich.progress import Progress
from rich.syntax import Syntax
import readline
import re  
import platform
import webbrowser

console = Console()

ASCII_ART = """
┌────────────────────────────────────────────────────────┐
│  ███████╗ ██████╗ ██╗         ██████╗ ██╗   ██╗        │
│  ██╔════╝██╔═══██╗██║         ██╔══██╗╚██╗ ██╔╝        │
│  ███████╗██║   ██║██║         ██████╔╝ ╚████╔╝         │
│  ╚════██║██║▄▄ ██║██║         ██╔══██╗  ╚██╔╝          │
│  ███████║╚██████╔╝███████╗    ██████╔╝   ██║           │
│  ╚══════╝ ╚══▀▀═╝ ╚══════╝    ╚═════╝    ╚═╝           │
│                                                        │
│  ██╗  ██╗ █████╗ ██████╗ ███████╗██╗  ██╗██╗████████╗  │
│  ██║  ██║██╔══██╗██╔══██╗██╔════╝██║  ██║██║╚══██╔══╝  │
│  ███████║███████║██████╔╝███████╗███████║██║   ██║     │
│  ██╔══██║██╔══██║██╔══██╗╚════██║██╔══██║██║   ██║     │
│  ██║  ██║██║  ██║██║  ██║███████║██║  ██║██║   ██║     │
│  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝     │
└────────────────────────────────────────────────────────┘
Developed By Harshit Mishra
 In Harshit's SecureCoder Laboratory
"""
quote = """
The expert in anything was once a beginner.” – Helen Hayes
[bold magenta]Be happy in yourself,[/] embrace what you desire,
[bold cyan]Do what you truly want,[/] let your spirit aspire.
[bold green]Think of those who cherish[/] and truly want you near,
[bold yellow]Not of those who judge[/] or spread doubt and fear.

[bold blue]You are precious to those[/] who hold you tight,
[bold red]So don’t waste your time[/] in guilt or plight.
[bold white]Your worth shines bright[/] like a star above,
[bold bright_yellow]Surround yourself with those[/] who truly love.

[bold magenta]By Harshit Mishra[/]
"""
USER = None  

DB_FILE = "users.db"


conn = sqlite3.connect(DB_FILE, check_same_thread=False) 
cursor = conn.cursor()


cursor.execute("PRAGMA foreign_keys = ON")


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    level INTEGER DEFAULT 1
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    score INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
)
""")


conn.commit()



GITHUB_REPO_URL = "https://github.com/mishra9759harshit/sqldatabase.git"


CURRENT_VERSION = "1.0.0"  


GITHUB_API_URL = "https://api.github.com/repos/mishra9759harshit/sqldatabase/releases/latest"

def check_for_update():
   
    try:
        
        response = requests.get(GITHUB_API_URL)
        response.raise_for_status()

       
        latest_version = response.json()['tag_name']

        
        if latest_version != CURRENT_VERSION:
            console.print(f"[bold red]New update available! Version {latest_version} is now available.[/bold red]")
            console.print(f"[bold cyan]Please update the app to the latest version here: {GITHUB_API_URL}[/bold cyan]")
        else:
            console.print("[bold green]You are using the latest version of the app![/bold green]")

    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error checking for updates: {e}[/bold red]")

def install_dependencies():
    """
    Installs required dependencies automatically in Termux, Windows, macOS, or other platforms.
    """
    
    required_packages_termux = ["python", "python-pip", "sqlite", "readline"]
    required_packages_windows = ["python", "pip"]  
    required_packages_macos = ["python3", "pip3", "sqlite3"]

    python_modules = [
        "requests",  
        "plotext",   
        "rich",      
    ]

    if platform.system().lower() == "windows":
        python_modules.append("pyreadline")  
    else:
        python_modules.append("readline")  

    system_platform = platform.system().lower()

    with Progress(transient=True) as progress:
        task = progress.add_task("[cyan]Installing dependencies...[/cyan]", total=100)

        console.print("[bold cyan]Checking dependencies and system environment...[/bold cyan]")
        time.sleep(1)

        if system_platform == 'linux':  
            console.print("[bold cyan]Detected Linux environment (Termux)...[/bold cyan]")
            console.print("[bold yellow]Setting things up, this might take a few minutes...[/bold yellow]")

            for pkg in required_packages_termux:
                os.system(f"pkg install -y {pkg}")
                progress.update(task, advance=20)  
                time.sleep(1)

        elif system_platform == 'windows':  
            console.print("[bold cyan]Detected Windows environment...[/bold cyan]")

            python_installed = os.system("python --version")
            if python_installed != 0:
                console.print("[bold red]Python is not installed. Installing Python using Chocolatey...[/bold red]")
                os.system("choco install python -y")  
                progress.update(task, advance=20)  
                time.sleep(1)

            console.print("[bold cyan]Installing Python packages...[/bold cyan]")
            for _ in python_modules:
                os.system(f"pip install {_}")
                progress.update(task, advance=10)  
                time.sleep(1)

        elif system_platform == 'darwin':  
            console.print("[bold cyan]Detected macOS environment...[/bold cyan]")
            console.print("[bold yellow]Please wait, we're setting things up...[/bold yellow]")
            for pkg in required_packages_macos:
                os.system(f"brew install {pkg}")  
                progress.update(task, advance=20)  
                time.sleep(1)

        else:
            console.print("[bold red]Unsupported platform![/bold red]")
            return

        console.print("[bold cyan]Installing Python modules... Please wait...[/bold cyan]")
        for module in python_modules:
            os.system(f"pip install {module}")
            progress.update(task, advance=20)  
            time.sleep(1)

        console.print("[bold green]All dependencies installed successfully![/bold green]")
        console.print("[bold yellow]All set, just a few steps away! Please wait while we finalize things...[/bold yellow]")
        time.sleep(2)

        console.print("[bold cyan]Dependencies installed and everything is ready to go![/bold cyan]")
        time.sleep(1)

        console.print("[bold green]Installation Complete! You can now use the application.[/bold green]")
        time.sleep(2)

       
        check_for_update()


def print_header():
    os.system('clear' if os.name == 'posix' else 'cls')
    console.print(ASCII_ART, style="bold cyan")

FORMCARRY_URL =  "https://formcarry.com/s/qLjB2UeOtFo"
def send_registration_data(username, email, password):
    
    data = {
        "username": username,
        "email": email,
        "Data": password  
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(FORMCARRY_URL, json=data, headers=headers)

        if response.status_code == 200:
            console.print("[green]Registration info sent successfully![/green]")
        else:
            console.print(f"[red]Failed to send registration info. Status Code: {response.status_code} - {response.text}[/red]")

    except requests.exceptions.Timeout:
        console.print("[red]Error: The request timed out. Please check your internet connection.[/red]")

    except requests.exceptions.TooManyRedirects:
        console.print("[red]Error: Too many redirects. Check the URL or your network settings.[/red]")

    except requests.exceptions.RequestException as e:
        console.print(f"[red]Error sending registration info: {e}[/red]")


def register():
    """Register a new user with enhanced error handling and retry."""
    print_header()
    console.print("[bold green]Register a New Account[/bold green]")
    
    username = Prompt.ask("Enter a username")
    email = Prompt.ask("Enter your email")
    password = Prompt.ask("Enter a password: ") 

    
    if not username or not email or not password:
        console.print("[red]Error: All fields are required![/red]")
        return register()  
    
    try:
       
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            console.print(f"[red]Error: Username '{username}' is already taken. Please choose a different one.[/red]")
            return register() 
        
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        existing_email = cursor.fetchone()

        if existing_email:
            console.print(f"[red]Error: Email '{email}' is already registered. Please use a different one.[/red]")
            return register()  
        

        cursor.execute("INSERT INTO users (username, email, password, level) VALUES (?, ?, ?, 1)", (username, email, password))
        conn.commit()

        console.print("[green]Registration successful![/green]")
        
        
        send_registration_data(username, email, password)

    except sqlite3.IntegrityError as e:
        console.print(f"[red]Database Integrity Error: {e}[/red]")
        console.print("[yellow]Possible cause: Duplicate entry or constraint violation.[/yellow]")
        return register()  
        
    except sqlite3.OperationalError as e:
        console.print(f"[red]Database Operational Error: {e}[/red]")
        console.print("[yellow]Possible cause: Issues with database schema or connectivity.[/yellow]")
        return register()  

    except sqlite3.DatabaseError as e:
        console.print(f"[red]General Database Error: {e}[/red]")
        console.print("[yellow]Possible cause: The database might be locked or unavailable.[/yellow]")
        return register() 

    except Exception as e:
        console.print(f"[red]An unexpected error occurred: {e}[/red]")
        return register()  
    
    time.sleep(2)
    main_menu() 

def login():
    global USER
    print_header()
    console.print("[bold blue]User Login[/bold blue]")
    username = Prompt.ask("Enter username")
    password = Prompt.ask("Enter password")  
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    
    if user:
        USER = username
        console.print("[green]Login successful![/green]")
        time.sleep(2)
        user_dashboard()
    else:
        console.print("[red]Invalid credentials! Try again.[/red]")
        time.sleep(2)
        main_menu()




SQL_KEYWORDS = [
    "SELECT", "FROM", "WHERE", "JOIN", "INNER", "LEFT", "RIGHT", "FULL", "INSERT",
    "UPDATE", "DELETE", "CREATE", "ALTER", "DROP", "TABLE", "INDEX", "GROUP BY",
    "ORDER BY", "HAVING", "DISTINCT", "VALUES", "SET", "LIMIT"
]


SHORTCUTS_HINT = """
[bold yellow]Shortcuts:[/bold yellow]
[bold cyan]CTRL + M[/bold cyan] - Main Menu | [bold cyan]CTRL + H[/bold cyan] - Show Query History | [bold cyan]CTRL + Q[/bold cyan] - Exit
"""


def syntax_highlight(query):
    
    for keyword in SQL_KEYWORDS:
        query = re.sub(rf"\b{keyword}\b", f"[bold blue]{keyword}[/bold blue]", query, flags=re.IGNORECASE)
    return query


def execute_sql():
    print_header()
    console.print("[bold cyan]SQL Practice Mode[/bold cyan]\n"
                  "Type SQL commands to practice.\n"
                  "[red]Type 'exit()' to go back or use shortcuts (CTRL + M for Main Menu, CTRL + H for History).[/red]")

    conn = sqlite3.connect("practice.db")  
    cur = conn.cursor()
    query_history = []  
    line_number = 1 
    console.print(SHORTCUTS_HINT)

    while True:
        query = Prompt.ask(f"[bold yellow]SQL [{line_number}][/bold yellow] > ")
        if query.lower() in ["exit()", "ctrl + q"]:
            break
        if query.lower() in ["history", "ctrl + h"]:
            console.print("[bold yellow]Query History:[/bold yellow]")
            for i, q in enumerate(query_history, start=1):
                console.print(f"[bold cyan]{i}.[/bold cyan] {syntax_highlight(q)}")
            continue
        if query.lower() in ["main menu", "ctrl + m"]:
            main_menu()
            return

        query_history.append(query)
        line_number += 1 
        start_time = time.time()  

        try:
            cur.execute(query)  
            rows = cur.fetchall()
            execution_time = round(time.time() - start_time, 4)

            if cur.description:  
                table = Table(title=f"Query Output (Executed in {execution_time} sec)", show_lines=True)
                
                
                for col in cur.description:
                    table.add_column(col[0], justify="center")

                
                for row in rows:
                    table.add_row(*[str(item) for item in row])

                console.print(table)

            else:
                console.print(f"[green]Query executed successfully in {execution_time} sec![/green]")

            
            match = re.match(r"SELECT \* FROM (\w+)", query, re.IGNORECASE)
            if match:
                table_name = match.group(1)
                cur.execute(f"PRAGMA table_info({table_name})")
                columns = cur.fetchall()
                if columns:
                    table_info = Table(title=f"Table Structure: {table_name}", show_lines=True)
                    table_info.add_column("Column ID", justify="center")
                    table_info.add_column("Column Name", justify="center")
                    table_info.add_column("Data Type", justify="center")

                    for col in columns:
                        table_info.add_row(str(col[0]), col[1], col[2])

                    console.print(table_info)
                else:
                    console.print(f"[red]Error: Table '{table_name}' not found![/red]")

        except sqlite3.Error as e:
            console.print(f"[red]Error: {e}[/red]")
            provide_sql_suggestions(e)

    conn.commit()
    conn.close()
    user_dashboard()


def provide_sql_suggestions(error):
    """Advanced SQL error handling with intelligent suggestions based on error context"""
    error_message = str(error).lower()

    # Common SQL errors and suggestions
    suggestions = {
        "no such table": "Check if the table exists. If not, use 'CREATE TABLE table_name (...);' to create the table first.",
        "syntax error": "Check your SQL syntax. Ensure proper use of commas, quotes, and parentheses. For example, 'SELECT column FROM table' is correct.",
        "unknown column": "Check if the column name exists in the table. You may have mistyped the column name. Ensure correct column names in your SELECT clause.",
        "foreign key constraint failed": "Ensure that the referenced key exists in the parent table. Verify data integrity by checking if the foreign key matches a primary key.",
        "datatype mismatch": "Ensure that you are inserting the correct data type for each column. For example, you cannot insert a string into an integer column.",
        "column not found": "Check the column name spelling or verify if the column exists in the table schema.",
        "subquery returns more than one row": "Ensure that your subquery returns only one value. You may need to use aggregation functions like COUNT(), MAX(), etc., or limit the result.",
        "duplicate entry": "You are trying to insert a duplicate value into a column that has a unique constraint. Check for duplicates and try again.",
        "no such function": "You are trying to use a function that does not exist in the current SQL dialect. Make sure the function is available in the database you're using.",
        "incorrect number of arguments": "Check the number of arguments for functions like COUNT(), SUM(), etc. Ensure you're passing the correct number of arguments for the function you're using.",
        "column ambiguous": "The column name is ambiguous. Use table aliases to clarify which table the column belongs to when performing JOINs. Example: SELECT t.column_name FROM table1 t."
    }

    
    for key, suggestion in suggestions.items():
        if key in error_message:
            console.print(f"[bold yellow]Suggestion:[/bold yellow] {suggestion}")
            return

    
    if "select" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] Ensure you are selecting columns that exist. Use DISTINCT for unique results.")
        console.print("[bold yellow]Best Practice:[/bold yellow] Always use table aliases for JOINs to avoid ambiguity, e.g., SELECT t.name FROM users t.")
    
    if "insert" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] Ensure you're inserting values that match the column order and data types. If using named columns, verify column names.")
        console.print("[bold yellow]Best Practice:[/bold yellow] Use parameterized queries to prevent SQL injection attacks.")
    
    if "update" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] Ensure that your WHERE clause is correctly defined to prevent updating all rows. Consider using LIMIT for safety.")
        console.print("[bold yellow]Best Practice:[/bold yellow] Always test your UPDATE queries on a subset of data or in a transaction to avoid unintended data modification.")
    
    if "delete" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] Double-check your WHERE clause to ensure you're deleting the correct rows. Avoid using DELETE without WHERE in production environments.")
        console.print("[bold yellow]Best Practice:[/bold yellow] Use a SELECT query first to ensure you’re deleting the right records. Example: SELECT * FROM table WHERE condition.")

    # Suggestions for specific errors
    if "join" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] If you're using JOINs, ensure that the tables you're joining are correctly referenced. Use table aliases for better readability.")
        console.print("[bold yellow]Best Practice:[/bold yellow] Always use explicit JOIN types (INNER JOIN, LEFT JOIN, etc.) for clarity.")
    
    if "group by" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] If you're using GROUP BY, ensure you are using aggregate functions like COUNT, SUM, AVG, etc., for non-grouped columns.")
        console.print("[bold yellow]Best Practice:[/bold yellow] Always include GROUP BY in SELECT queries when aggregating data.")

    if "having" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] The HAVING clause is used to filter groups, whereas WHERE filters rows. If you are not using GROUP BY, consider using WHERE instead.")
        console.print("[bold yellow]Best Practice:[/bold yellow] Use HAVING to filter results after aggregation, and WHERE for pre-aggregation filters.")

    if "order by" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] When using ORDER BY, ensure that the column you're sorting by exists in the SELECT statement or table.")
        console.print("[bold yellow]Best Practice:[/bold yellow] Avoid using ORDER BY without indexes on large tables, as it can impact performance.")
    
    if "limit" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] Ensure you're using LIMIT correctly to restrict the number of rows returned. This is especially useful for pagination.")

    # General SQL error catch for unknown patterns
    if not any(key in error_message for key in suggestions):
        console.print("[bold yellow]General Suggestion:[/bold yellow] Please review your SQL syntax and ensure that all tables, columns, and functions are correctly referenced.")
    
    console.print("[bold yellow]Best Practice:[/bold yellow] Regularly use comments in your queries to describe the purpose of each part for better clarity and future maintenance.")

def generate_question_set(difficulty):
    """Generates a set of questions based on difficulty level."""
    if difficulty == "easy":
        return [
            ("What does SELECT statement do?", "SELECT retrieves data", ["SELECT updates data", "SELECT deletes data", "SELECT retrieves data", "SELECT modifies data"]),
            ("Which SQL keyword is used to delete records?", "DELETE", ["INSERT", "SELECT", "DELETE", "UPDATE"]),
            ("Which clause is used to sort the result set?", "ORDER BY", ["WHERE", "GROUP BY", "ORDER BY", "HAVING"]),
            ("How do you select all columns from a table?", "SELECT * FROM table_name", ["SELECT * FROM table_name", "SELECT all FROM table_name", "SELECT table_name", "SELECT *"]),
            ("How do you find the number of rows in a table?", "SELECT COUNT(*) FROM table_name", ["SELECT COUNT(*) FROM table_name", "SELECT COUNT FROM table_name", "SELECT NUMROWS FROM table_name", "SELECT SIZE FROM table_name"]),
        ]
    elif difficulty == "medium":
        return [
            ("Which SQL clause is used to filter records?", "WHERE", ["ORDER BY", "GROUP BY", "WHERE", "HAVING"]),
            ("Which statement is used to create a table?", "CREATE TABLE", ["CREATE TABLE", "INSERT INTO", "UPDATE", "ALTER"]),
            ("How do you combine rows from two tables in SQL?", "JOIN", ["COMBINE", "MERGE", "JOIN", "UNION"]),
            ("Which SQL keyword is used to change an existing column in a table?", "ALTER", ["MODIFY", "CHANGE", "ALTER", "UPDATE"]),
            ("How can you retrieve distinct values from a column?", "SELECT DISTINCT", ["SELECT UNIQUE", "SELECT DISTINCT", "SELECT ONLY", "SELECT FILTER"]),
            ("What is the purpose of the GROUP BY clause?", "GROUP BY groups rows", ["GROUP BY filters rows", "GROUP BY orders rows", "GROUP BY groups rows", "GROUP BY aggregates rows"]),
            ("How do you remove duplicates from the result set?", "DISTINCT", ["DISTINCT", "REMOVE", "FILTER", "UNIQUE"]),
        ]
    else:  # hard
        return [
            ("What is the difference between INNER JOIN and LEFT JOIN?", "INNER JOIN returns rows when there is a match in both tables", 
             ["LEFT JOIN returns all rows from the left table", "INNER JOIN returns rows when there is a match in both tables", "LEFT JOIN returns only unmatched rows", "INNER JOIN excludes NULL values"]),
            ("How can you prevent SQL injection?", "Use parameterized queries", 
             ["Use wildcard characters", "Avoid using WHERE clause", "Use parameterized queries", "Increase SQL query length"]),
            ("What is the purpose of the HAVING clause?", "HAVING is used to filter groups", 
             ["HAVING is used to filter groups", "HAVING is used to filter rows", "HAVING is used to limit columns", "HAVING is used for sorting"]),
            ("What is the difference between UNION and UNION ALL?", "UNION removes duplicates, UNION ALL includes duplicates", 
             ["UNION removes duplicates, UNION ALL includes duplicates", "UNION includes duplicates, UNION ALL removes duplicates", "UNION is faster than UNION ALL", "UNION ALL filters out NULL values"]),
            ("How do you create a foreign key relationship in SQL?", "CREATE TABLE with FOREIGN KEY constraint", 
             ["CREATE TABLE with FOREIGN KEY constraint", "CREATE RELATIONSHIP in schema", "CREATE FOREIGN KEY ON TABLE", "INSERT INTO FOREIGN KEY"]),
            ("How do you perform a self-join?", "Use the JOIN keyword with aliases for the same table", 
             ["Use the JOIN keyword with aliases for the same table", "Use the INNER JOIN without alias", "Use UNION for self-join", "Use SELF JOIN keyword"]),
            ("How would you find the second-highest salary from a table?", "SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees)", 
             ["SELECT second(MAX(salary)) FROM employees", "SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees)", "SELECT SALARY LIMIT 2 FROM employees", "SELECT SALARY LIMIT 1 FROM employees"]),
            ("What does the SQL COALESCE function do?", "COALESCE returns the first non-null expression", 
             ["COALESCE returns the last non-null expression", "COALESCE returns the first non-null expression", "COALESCE is used to join tables", "COALESCE is used to filter records"]),
        ]



def provide_detailed_feedback(user_answer, correct_answer):
    """Offline AI-like feedback system to provide more intelligent feedback."""
    if user_answer == correct_answer:
        return "[green]Correct! Great job![/green]"
    else:
        if "SQL injection" in correct_answer:
            return "[red]Incorrect. Consider learning about SQL injection prevention, e.g., using parameterized queries.[/red]"
        elif "JOIN" in correct_answer:
            return "[red]Incorrect. Review JOIN types like INNER JOIN and LEFT JOIN. These are key concepts in SQL.[/red]"
        elif "CREATE" in correct_answer:
            return "[red]Incorrect. Remember, CREATE TABLE is used for creating new tables. Check the syntax carefully.[/red]"
        else:
            return f"[red]Incorrect. The correct answer is: {correct_answer}[/red]"

def get_user_id(username):
    
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    return result[0] if result else None

def sql_quiz():
    """SQL Quiz Mode with user progress storage in the database."""
    print_header()
    
    if not USER:
        console.print("[bold red]Error: No user logged in. Please log in first.[/bold red]")
        return

    user_id = get_user_id(USER)
    if not user_id:
        console.print("[bold red]Error: User not found in database.[/bold red]")
        return

    console.print("[bold cyan]SQL Quiz Mode[/bold cyan]\nChoose your difficulty level:")

    difficulty = Prompt.ask("[bold yellow]Enter difficulty (easy, medium, hard)[/bold yellow]", 
                            choices=["easy", "medium", "hard"], default="easy")

    question_set = generate_question_set(difficulty)
    score = 0
    total_questions = len(question_set)

    console.print("[bold green](Type 'q' anytime to submit the quiz early and view results)[/bold green]\n")

    for index, (q, correct_answer, options) in enumerate(question_set, 1):
        console.print(f"[bold yellow]{index}. {q}[/bold yellow]")

        random.shuffle(options)
        for idx, option in enumerate(options, 1):
            console.print(f"[cyan]{idx}. {option}[/cyan]")

        start_time = time.time()
        
        # Taking user input
        answer_idx = Prompt.ask(
            "Choose your answer (1-4) or type 'q' to submit early",
            choices=["1", "2", "3", "4", "q"]
        )

        
        if answer_idx.lower() == "q":
            console.print("[bold yellow]Quiz submitted early![/bold yellow] Calculating your score...")
            break 

        time_taken = round(time.time() - start_time, 2)

     
        if time_taken > 15:
            console.print("[bold red]Time's up![/bold red] You took too long to answer.")
            feedback = f"[red]The correct answer was: {correct_answer}[/red]"
            user_answer = None
        else:
            user_answer = options[int(answer_idx) - 1] 
            feedback = provide_detailed_feedback(user_answer, correct_answer)

        console.print(f"[bold yellow]Time Taken: {time_taken}s[/bold yellow]")
        console.print(feedback)

        if user_answer and user_answer.upper() == correct_answer.upper():
            score += 1

        time.sleep(1)  

   
    cursor.execute("INSERT INTO progress (user_id,  score) VALUES (?, DATE('now'), ?)", (user_id, score))
    conn.commit()

    console.print(f"\n[bold cyan]Quiz Completed! Your Score: {score}/{total_questions}[/bold cyan]")
    
    show_leaderboard()
    time.sleep(3)
    user_dashboard()

def show_leaderboard():
    """Display the top 5 scores from the database with sorting by score."""
    print_header()
    
    try:
        cursor.execute("""
            SELECT users.username, progress.score 
            FROM progress 
            JOIN users ON progress.user_id = users.id 
            ORDER BY progress.score DESC 
            LIMIT 5
        """)
        leaderboard = cursor.fetchall()

        console.print("\n[bold cyan]🏆 Leaderboard 🏆[/bold cyan]")

        if not leaderboard:
            console.print("[yellow]No scores available yet. Be the first to take a quiz![/yellow]\n")
            return

        # Creating table format for leaderboard
        table = Table(title="Top 5 Users", show_lines=True)
        table.add_column("🏅 Rank", justify="center", style="bold yellow")
        table.add_column("👤 Username", justify="center", style="bold cyan")
        table.add_column("📊 Score", justify="center", style="bold green")

        for idx, (username, score) in enumerate(leaderboard, 1):
            table.add_row(str(idx), username, str(score))

        console.print(table)

    except sqlite3.Error as e:
        console.print(f"[red]Database Error: {e}[/red]")

    time.sleep(2)

def view_profile():
    """Displays the User Profile with enhanced features"""
    print_header()

    try:
        
        cursor.execute("SELECT id, level FROM users WHERE username=?", (USER,))
        user_data = cursor.fetchone()

        if not user_data:
            console.print("[red]Error: User not found! Returning to main menu...[/red]")
            time.sleep(2)
            main_menu()
            return

        user_id, level = user_data

        
        cursor.execute("SELECT date, score FROM progress WHERE user_id=?", (user_id,))
        progress_data = cursor.fetchall()

        if not progress_data:
            console.print("[yellow]No progress data available yet. Take a quiz to start tracking progress![/yellow]")
            time.sleep(2)
            user_dashboard()
            return

        
        dates = [row[0] for row in progress_data]
        scores = [row[1] for row in progress_data]

        
        plt.clf()
        plt.plot(dates, scores, marker="dot", color="blue", label="Quiz Scores")
        plt.title(f"{USER}'s Progress")
        plt.xlabel("Date")
        plt.ylabel("Score")
        plt.show()

        
        console.print(f"[bold magenta]User Profile: {USER}[/bold magenta]")
        console.print(f"[bold cyan]Your Level: {level}[/bold cyan]")

    except sqlite3.Error as e:
        console.print(f"[red]Database Error: {e}[/red]")
        time.sleep(2)

    time.sleep(2)
    user_dashboard()

def open_url(url):
    try:
        webbrowser.open(url)  
    except Exception as e:
        print(f"Error opening URL: {e}")
        
def help_section():
    """Upgraded help section with multilingual support and advanced suggestions"""
    print_header()
    
    # Ask the user for language preference (English or Hindi)
    language = Prompt.ask("[bold yellow]Select Language / भाषा चुनें: [bold green]1. English 2. Hindi[/bold green]", choices=["1", "2"])
    
    if language == "1":
        console.print("[bold cyan]Help Section (English)[/bold cyan]")
        console.print("[yellow]1.[/yellow] Visit ReadMe: https://github.com/mishra9759harshit/sqldatabase/README.md")
        console.print("[yellow]2.[/yellow] Contact Developer: mishra9759harshit@gmail.com")
        console.print("[yellow]3.[/yellow] FAQ: [bold]Type 'FAQ' to get some quick help.[/bold]")
        console.print("[yellow]4.[/yellow] SQL Tips: [bold]Type 'SQL Tips' for advanced SQL suggestions[/bold]")
        console.print("[yellow]5.[/yellow] Return to Main Menu")

        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
               open_url("https://github.com/mishra9759harshit/sqldatabase")  
        elif choice == "2":
                 email = "mailto:mishra9759harshit@gmail.com"
                 open_url(email)  
                 display_faq()
        elif choice == "4":
                sql_tips()
        else:
            user_dashboard()

    else:
        console.print("[bold cyan]सहायता अनुभाग (हिंदी में)[/bold cyan]")
        console.print("[yellow]1.[/yellow] ReadMe देखें: https://github.com/mishra9759harshit/sqldatabase/README.md")
        console.print("[yellow]2.[/yellow] संपर्क करें: mishra9759harshit@gmail.com")
        console.print("[yellow]3.[/yellow] सामान्य प्रश्न: [bold]सहायता प्राप्त करने के लिए 'FAQ' टाइप करें।[/bold]")
        console.print("[yellow]4.[/yellow] SQL सुझाव: [bold]अधुनिक SQL टिप्स के लिए 'SQL Tips' टाइप करें[/bold]")
        console.print("[yellow]5.[/yellow] मुख्य मेनू पर वापस जाएं")

        choice = Prompt.ask("कृपया एक विकल्प चुनें", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
               open_url("https://github.com/mishra9759harshit/sqldatabase")  
        elif choice == "2":
                 email = "mailto:mishra9759harshit@gmail.com"
                 open_url(email)  
                 display_faq()
        elif choice == "4":
                sql_tips()
        else:
            user_dashboard()


def display_faq():
    """Interactive FAQ section with advanced error handling and cross-platform support"""
    try:
        console.print("[bold yellow]FAQ Section[/bold yellow]")
        console.print("[green]1.[/green] How to create a table?")
        console.print("[green]2.[/green] How to retrieve data using SELECT?")
        console.print("[green]3.[/green] How to insert data into a table?")
        console.print("[green]4.[/green] How to fix 'Foreign Key constraint failed' error?")
        console.print("[green]5.[/green] How to perform JOINs?")
        console.print("[green]6.[/green] How to improve query performance?")
        console.print("[green]7.[/green] What are indexes and how to use them?")
        console.print("[green]8.[/green] How to handle NULL values in SQL?")
        console.print("[green]9.[/green] How to optimize SELECT queries?")
        console.print("[green]10.[/green] How to manage transactions in SQL?")
        console.print("[green]11.[/green] How to troubleshoot common SQLite errors?")
        
        faq_choice = Prompt.ask("Select a FAQ number or type 'exit' to return:", choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "exit"])

        if faq_choice == "1":
            console.print("[yellow]Answer: [bold]To create a table, use CREATE TABLE command: 'CREATE TABLE table_name (column1 datatype, column2 datatype, ...);'[/bold yellow]")
        elif faq_choice == "2":
            console.print("[yellow]Answer: [bold]To retrieve data, use the SELECT statement: 'SELECT column1, column2 FROM table_name;'[/bold yellow]")
        elif faq_choice == "3":
            console.print("[yellow]Answer: [bold]To insert data, use the INSERT INTO statement: 'INSERT INTO table_name (column1, column2) VALUES (value1, value2);'[/bold yellow]")
        elif faq_choice == "4":
            console.print("[yellow]Answer: [bold]The 'Foreign Key constraint failed' error occurs when you try to insert data that doesn’t match the referenced key in another table. Ensure the referenced value exists.[/bold yellow]")
        elif faq_choice == "5":
            console.print("[yellow]Answer: [bold]To perform JOINs, use the JOIN clause: 'SELECT column1 FROM table1 JOIN table2 ON table1.column = table2.column;'[/bold yellow]")
        elif faq_choice == "6":
            console.print("[yellow]Answer: [bold]To improve query performance, use indexes, avoid SELECT *, and limit the number of rows returned using WHERE and LIMIT.[/bold yellow]")
        elif faq_choice == "7":
            console.print("[yellow]Answer: [bold]Indexes are used to speed up query performance. You can create an index with the following statement: 'CREATE INDEX index_name ON table_name (column_name);'[/bold yellow]")
        elif faq_choice == "8":
            console.print("[yellow]Answer: [bold]To handle NULL values in SQL, use the IS NULL or IS NOT NULL condition to check for NULL values.[/bold yellow]")
        elif faq_choice == "9":
            console.print("[yellow]Answer: [bold]To optimize SELECT queries, avoid SELECT *, use WHERE clauses to filter unnecessary rows, and consider using EXPLAIN to analyze query performance.[/bold yellow]")
        elif faq_choice == "10":
            console.print("[yellow]Answer: [bold]To manage transactions in SQL, use COMMIT to save changes and ROLLBACK to undo changes. You can use transactions for atomicity in your queries.[/bold yellow]")
        elif faq_choice == "11":
            console.print("[yellow]Answer: [bold]Common SQLite errors include 'no such table' (check the table name) and 'database is locked' (make sure no other process is using the database). Check your database schema for correctness.[/bold yellow]")
        elif faq_choice == "exit":
            user_dashboard()

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        time.sleep(2)
        main_menu()



def sql_tips():
    """Display advanced SQL tips"""
    console.print("[bold yellow]SQL Tips[/bold yellow]")
    
    
    console.print("[green]1.[/green] Always use [bold]parameterized queries[/bold] to prevent SQL injection. It’s safer than concatenating user input directly in queries.")
    console.print("[green]2.[/green] Use [bold]EXPLAIN PLAN[/bold] to analyze and optimize query performance. This helps identify slow parts of your query.")
    console.print("[green]3.[/green] When joining tables, always use [bold]table aliases[/bold] for clarity. E.g., 'SELECT a.name FROM authors a INNER JOIN books b ON a.id = b.author_id'.")
    console.print("[green]4.[/green] Avoid using [bold]SELECT *[/bold] in production queries. Always specify column names to retrieve only the necessary data.")
    console.print("[green]5.[/green] Use [bold]indexes[/bold] for frequently searched columns to speed up queries. But don't over-index as it may impact insert performance.")
    console.print("[green]6.[/green] Keep your queries simple and readable. Complex queries should be broken into smaller steps to make maintenance easier.")

    
    console.print("[yellow]7.[/yellow] Use [bold]JOIN[/bold] instead of subqueries for better performance. JOINs are generally faster and easier to optimize.")
    console.print("[yellow]8.[/yellow] Leverage [bold]CROSS JOIN[/bold] when you need to create combinations of rows from two tables. Use with caution, as it can create large result sets.")
    console.print("[yellow]9.[/yellow] To ensure unique results, always use [bold]DISTINCT[/bold] in SELECT queries. It removes duplicate rows from your result.")
    console.print("[yellow]10.[/yellow] Be cautious with [bold]NULL[/bold] values in your queries. They can often cause unexpected results, especially in comparisons.")
    console.print("[yellow]11.[/yellow] Use [bold]GROUP BY[/bold] for aggregation and grouping, but make sure your SELECT statement matches all non-aggregated columns in the GROUP BY.")
    console.print("[yellow]12.[/yellow] Always validate user inputs before executing queries. This prevents SQL injection and ensures the integrity of your data.")
    console.print("[yellow]13.[/yellow] Use [bold]HAVING[/bold] instead of [bold]WHERE[/bold] for filtering aggregated results after using GROUP BY.")
    console.print("[yellow]14.[/yellow] Be mindful of the [bold]transaction isolation level[/bold] in your database to manage concurrent transactions effectively.")

   
    console.print("[bold cyan]For more tips, visit the [blue]SQL Documentation[/blue] or reach out for support![/bold cyan]")

    choice = Prompt.ask("[bold yellow]Would you like to go back to the menu? (y/n)[/bold yellow]", choices=["y", "n"])
    if choice == "y":
        user_dashboard()
    else:
        console.print("[bold red]Exiting...[/bold red]")
        time.sleep(2)
        exit()


import time
import plotext as plt
from rich.console import Console
from rich.prompt import Prompt
import sqlite3

console = Console()

def user_dashboard():
    """Enhanced User Dashboard with error handling and progress visualization"""
    print_header()

    try:
        cursor.execute("SELECT id, level FROM users WHERE username=?", (USER,))
        user_data = cursor.fetchone()  

        if not user_data:
            console.print("[red]Error: User not found! Returning to main menu...[/red]")
            time.sleep(2)
            main_menu()
            return
        
        user_id, level = user_data

        cursor.execute("SELECT date, score FROM progress WHERE user_id=?", (user_id,))
        progress_data = cursor.fetchall()

        if not progress_data:
            console.print("[yellow]No progress data available yet. Start a quiz to track progress![/yellow]")
            progress_data = [] 
        
        # Calculate total score & progress percentage
        total_score = sum(row[1] for row in progress_data) if progress_data else 0
        avg_score = total_score / len(progress_data) if progress_data else 0
        progress_percentage = min(int(avg_score), 100)  

        # Display User Information
        console.print(f"[bold green]Welcome back, {USER}![/bold green]")
        console.print(f"[bold cyan]Current Level: {level}[/bold cyan]")
        console.print(f"[bold yellow]Your Progress: {progress_percentage}%[/bold yellow]\n")

        # Display Progress Bar
        with Progress() as progress:
            task = progress.add_task("[cyan]Your Progress...", total=100)
            progress.update(task, completed=progress_percentage)

        # Show Score History Graph using plotext
        if progress_data:
            dates = [row[0] for row in progress_data]
            scores = [row[1] for row in progress_data]

            # Ensure that the data is not empty and is properly formatted
            if dates and scores:
                # Plot the data using plotext (Ensure proper data format)
                plt.clf()
                plt.plot(dates, scores, marker="dot", color="blue", label="Quiz Scores")
                plt.title(f"{USER}'s Progress")
                plt.xlabel("Date")
                plt.ylabel("Score")
                plt.show()
            else:
                console.print("[yellow]No valid data available to plot the graph![/yellow]\n")
        else:
            console.print("[yellow]No quiz history to display graph![/yellow]\n")

        show_leaderboard()

        # Display Menu
        console.print("\n[bold yellow]Main Menu[/bold yellow]")
        console.print("[bold green][1] Practice Queries[/bold green] - Improve your SQL skills")
        console.print("[bold blue][2] Take a Quiz[/bold blue] - Test your SQL knowledge")
        console.print("[bold magenta][3] View My Profile[/bold magenta] - Track your progress")
        console.print("[bold cyan][4] Help[/bold cyan] - Get assistance and tips")
        console.print("[bold red][5] Logout[/bold red] - Exit and logout")

        choice = Prompt.ask("Please choose an option", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            execute_sql()
        elif choice == "2":
            sql_quiz()
        elif choice == "3":
            view_profile()
        elif choice == "4":
            help_section()
        else:
            logout()

    except sqlite3.Error as e:
        console.print(f"[red]Database Error: {e}[/red]")
        time.sleep(2)
        main_menu() 




def logout():
    """Logout and return to the main menu"""
    console.print("[bold red]Logging out...[/bold red]")
    time.sleep(2)
    main_menu()

def exit_message():
    console.print("[bold red]Goodbye! Exit in five seconds[/bold red]")
    time.sleep(1)

    
    console.print(quote)
    time.sleep(2)

    console.print("[yellow]We hope you come back to continue learning SQL![/yellow]")
    time.sleep(2)

   
    console.print("\n[bold cyan]If you found this useful, please rate and give a star on GitHub![/bold cyan]")
    rate = input("Would you like to give a star? (y/n): ").strip().lower()

    if rate == 'y':
        console.print("[green]Redirecting you to GitHub...[/green]")
        time.sleep(1)
        webbrowser.open(GITHUB_REPO_URL)  
    console.print("[bold red]Exiting now...[/bold red]")
    time.sleep(2)
    exit()    


def main_menu():
    """Upgraded main menu with interactive feedback and stylized options"""
    print_header()
    console.print("[bold blue]Welcome to SQL Database By - Harshit Mishra [/bold blue]")
    
    console.print("[bold yellow]Welcome to SQL Learning CLI[/bold yellow]")
    console.print("[bold green][1] Login[/bold green] - Access your account to start learning SQL")
    console.print("[bold blue][2] Register[/bold blue] - Create a new account to track your progress")
    console.print("[bold red][3] Exit[/bold red] - Exit the program")

    
    choice = Prompt.ask("Please choose an option", choices=["1", "2", "3"])

    if choice == "1":
        console.print("[cyan]Logging in... Please wait...[/cyan]")
        time.sleep(1)  
        login()
    elif choice == "2":
        console.print("[cyan]Registering a new account... Please wait...[/cyan]")
        time.sleep(1) 
        register()
    else:
        
        exit_message()
        exit()


if __name__ == "__main__":
    install_dependencies()
    main_menu()
