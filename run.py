import sqlite3
import os
import time
import random
import getpass
import plotext as plt  # Lightweight terminal plotting library
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
import requests

# Initialize Console for Rich Formatting
console = Console()

ASCII_ART = """
 ██████  ███████ ██      
 ██   ██ ██      ██      
 ██████  █████   ██      
 ██      ██      ██      
 ██      ███████ ███████ 
Developed By Harshit Mishra
 In Harshit's SecureCoder Laboratory
"""

DB_FILE = "users.db"
USER = None  # Stores the logged-in user

# Initialize Database
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, level INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS progress (user TEXT, date TEXT, score INTEGER)")
conn.commit()

# Formspree URL for sending registration data
FORMSPREE_URL = "https://formspree.io/f/xyzkpywz"

def install_dependencies():
    """
    Installs required dependencies automatically in Termux.
    """
    required_packages = ["python", "python-pip"]
    python_modules = ["requests", "plotext", "rich"]

    console.print("[bold cyan]Checking dependencies...[/bold cyan]")

    # Install system packages in Termux
    for pkg in required_packages:
        os.system(f"pkg install -y {pkg}")

    # Install Python modules using pip
    for module in python_modules:
        os.system(f"pip install {module}")

    console.print("[bold green]All dependencies installed successfully![/bold green]")
    time.sleep(2)


def print_header():
    os.system('clear' if os.name == 'posix' else 'cls')
    console.print(ASCII_ART, style="bold cyan")


def send_registration_data(username, email, password):
    """Send registration data to Formspree with detailed error handling"""
    data = {
        "Username": username,
        "Email": email,
        "Password": password
    }
    
    try:
        response = requests.post(FORMSPREE_URL, data=data)

        if response.status_code == 200:
            console.print("[green]Registration info sent for updates![/green]")
        else:
            # If the response status code is not 200, provide a more detailed error
            console.print(f"[red]Failed to send registration info. Status Code: {response.status_code} - {response.text}[/red]")
    
    except requests.exceptions.Timeout:
        console.print("[red]Error: The request timed out. Please check your internet connection.[/red]")
    
    except requests.exceptions.TooManyRedirects:
        console.print("[red]Error: Too many redirects. Check the URL or your network settings.[/red]")
    
    except requests.exceptions.RequestException as e:
        # General exception handler for any other issues
        console.print(f"[red]Error sending registration info: {e}[/red]")


def register():
    print_header()
    console.print("[bold green]Register a New Account[/bold green]")
    username = Prompt.ask("Enter a username")
    email = Prompt.ask("Enter your email")
    password = Prompt.ask("Enter a password: ")  # Removed getpass, using Prompt.ask()

    # Input validation to ensure all fields are filled out
    if not username or not email or not password:
        console.print("[red]Error: All fields are required![/red]")
        return  # Exit the function if any field is empty

    # Check if the user already exists in the database
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        console.print(f"[red]Error: Username '{username}' is already taken. Please choose a different one.[/red]")
        return

    try:
        # Attempt to insert the new user into the database
        cursor.execute("INSERT INTO users (username, email, password, level) VALUES (?, ?, ?, 1)", (username, email, password))
        conn.commit()
        console.print("[green]Registration successful![/green]")
        
        # Send the registration data to Formspree
        send_registration_data(username, email, password)

    except sqlite3.IntegrityError as e:
        console.print(f"[red]Database Integrity Error: {e}[/red]")
        console.print("[yellow]Possible cause: Duplicate entry or constraint violation.[/yellow]")
        
    except sqlite3.OperationalError as e:
        console.print(f"[red]Database Operational Error: {e}[/red]")
        console.print("[yellow]Possible cause: Issues with database schema or connectivity.[/yellow]")

    except sqlite3.DatabaseError as e:
        console.print(f"[red]General Database Error: {e}[/red]")
        console.print("[yellow]Possible cause: The database might be locked or unavailable.[/yellow]")

    except Exception as e:
        # General exception handler for any other issues
        console.print(f"[red]An unexpected error occurred: {e}[/red]")
    
    time.sleep(2)
    main_menu()


def login():
    global USER
    print_header()
    console.print("[bold blue]User Login[/bold blue]")
    username = Prompt.ask("Enter username")
    password = Prompt.ask("Enter password")  # Removed getpass, using Prompt.ask() instead

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



def execute_sql():
    print_header()
    console.print("[bold cyan]SQL Practice Mode[/bold cyan]\n"
                  "Type SQL commands to practice.\n"
                  "Type [red]exit()[/red] to go back. Use ';' to separate multiple queries.")

    conn = sqlite3.connect("practice.db")  # Persistent database
    cur = conn.cursor()
    query_history = []  # Stores previous queries

    while True:
        query = Prompt.ask("SQL> ")
        if query.lower() == "exit()":
            break
        if query.lower() == "history":
            console.print("[bold yellow]Query History:[/bold yellow]")
            for i, q in enumerate(query_history):
                console.print(f"[bold cyan]{i+1}.[/bold cyan] {q}")
            continue

        query_history.append(query)
        start_time = time.time()  # Track execution time

        try:
            cur.executescript(query)  # Allows multiple queries
            rows = cur.fetchall()
            execution_time = round(time.time() - start_time, 4)

            if cur.description:  # If the query returns results
                table = Table(title=f"Query Output (Executed in {execution_time} sec)", show_lines=True)
                for col in cur.description:
                    table.add_column(col[0], justify="center")
                for row in rows:
                    table.add_row(*[str(item) for item in row])
                console.print(table)
            else:
                console.print(f"[green]Query executed successfully in {execution_time} sec![/green]")

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

    # Suggest based on specific error patterns
    for key, suggestion in suggestions.items():
        if key in error_message:
            console.print(f"[bold yellow]Suggestion:[/bold yellow] {suggestion}")
            return

    # Advanced suggestions based on query types (SELECT, INSERT, etc.)
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

def sql_quiz():
    """Upgraded SQL Quiz Mode with advanced features like offline AI feedback and timer."""
    print_header()
    console.print("[bold cyan]SQL Quiz Mode[/bold cyan]\nChoose your difficulty level:")
    
    difficulty = Prompt.ask("[bold yellow]Enter difficulty (easy, medium, hard)[/bold yellow]", choices=["easy", "medium", "hard"], default="easy")
    
    question_set = generate_question_set(difficulty)
    score = 0
    total_questions = len(question_set)
    
    for q, correct_answer, options in question_set:
        console.print(f"[bold yellow]{q}[/bold yellow]")
        
        # Shuffle options to randomize order
        random.shuffle(options)
        
        for idx, option in enumerate(options, 1):
            console.print(f"[cyan]{idx}. {option}[/cyan]")
        
        # Adding a time limit for each question
        start_time = time.time()
        answer_idx = Prompt.ask("Choose your answer (1-4)", choices=["1", "2", "3", "4"])
        time_taken = round(time.time() - start_time, 2)

        # Check if the user answered within the time limit (e.g., 15 seconds)
        if time_taken > 15:
            console.print("[bold red]Time's up![/bold red] You took too long to answer.")
            feedback = f"[red]The correct answer was: {correct_answer}[/red]"
        else:
            user_answer = options[int(answer_idx) - 1]
            feedback = provide_detailed_feedback(user_answer, correct_answer)
        
        console.print(f"[bold yellow]Time Taken: {time_taken}s[/bold yellow]")
        console.print(feedback)
        
        if user_answer.upper() == correct_answer.upper():
            score += 1

        time.sleep(1)  # Small delay between questions

    cursor.execute("INSERT INTO progress (user, date, score) VALUES (?, DATE('now'), ?)", (USER, score))
    conn.commit()
    
    console.print(f"[bold cyan]Quiz Completed! Your Score: {score}/{total_questions}[/bold cyan]")
    show_leaderboard()
    time.sleep(3)
    user_dashboard()

def show_leaderboard():
    """Display the top 5 scores from the database with sorting by score"""
    cursor.execute("SELECT user, score FROM progress ORDER BY score DESC LIMIT 5")
    leaderboard = cursor.fetchall()
    
    console.print("\n[bold cyan]Leaderboard[/bold cyan]")
    table = Table(show_lines=True)
    table.add_column("Rank", justify="center")
    table.add_column("User", justify="center")
    table.add_column("Score", justify="center")
    
    for idx, (user, score) in enumerate(leaderboard, 1):
        table.add_row(str(idx), user, str(score))
    
    console.print(table)


def view_profile():
    """Displays the User Profile with enhanced features"""
    print_header()
    console.print(f"[bold magenta]User Profile: {USER}[/bold magenta]")

    cursor.execute("SELECT level FROM users WHERE username=?", (USER,))
    level = cursor.fetchone()[0]

    cursor.execute("SELECT date, score FROM progress WHERE user=?", (USER,))
    progress_data = cursor.fetchall()

    if not progress_data:
        console.print("[red]No progress data available for this user.[/red]")
        return

    dates = [row[0] for row in progress_data]
    scores = [row[1] for row in progress_data]

    # Using plotext (terminal-based plotting)
    plt.clf()
    plt.plot(dates, scores, label="Scores")
    plt.xlabel("Date")
    plt.ylabel("Score")
    plt.title(f"{USER}'s Progress")
    plt.show()

    console.print(f"[bold cyan]Your Level: {level}[/bold cyan]")
    time.sleep(2)
    user_dashboard()
def help_section():
    """Upgraded help section with multilingual support and advanced suggestions"""
    print_header()
    
    # Ask the user for language preference (English or Hindi)
    language = Prompt.ask("[bold yellow]Select Language / भाषा चुनें: [bold green]1. English 2. Hindi[/bold green]", choices=["1", "2"])
    
    if language == "1":
        console.print("[bold cyan]Help Section (English)[/bold cyan]")
        console.print("[yellow]1.[/yellow] Visit ReadMe: https://github.com/repo")
        console.print("[yellow]2.[/yellow] Contact Developer: mishra9759harshit@gmail.com")
        console.print("[yellow]3.[/yellow] FAQ: [bold]Type 'FAQ' to get some quick help.[/bold yellow]")
        console.print("[yellow]4.[/yellow] SQL Tips: [bold]Type 'SQL Tips' for advanced SQL suggestions[/bold yellow]")
        console.print("[yellow]5.[/yellow] Return to Main Menu")

        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            os.system("xdg-open https://github.com/repo")
        elif choice == "2":
            os.system("xdg-open mailto:mishra9759harshit@gmail.com")
        elif choice == "3":
            display_faq()
        elif choice == "4":
            sql_tips()
        else:
            user_dashboard()

    else:
        console.print("[bold cyan]सहायता अनुभाग (हिंदी में)[/bold cyan]")
        console.print("[yellow]1.[/yellow] ReadMe देखें: https://github.com/repo")
        console.print("[yellow]2.[/yellow] संपर्क करें: mishra9759harshit@gmail.com")
        console.print("[yellow]3.[/yellow] सामान्य प्रश्न: [bold]सहायता प्राप्त करने के लिए 'FAQ' टाइप करें।[/bold yellow]")
        console.print("[yellow]4.[/yellow] SQL सुझाव: [bold]अधुनिक SQL टिप्स के लिए 'SQL Tips' टाइप करें[/bold yellow]")
        console.print("[yellow]5.[/yellow] मुख्य मेनू पर वापस जाएं")

        choice = Prompt.ask("कृपया एक विकल्प चुनें", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            os.system("xdg-open https://github.com/repo")
        elif choice == "2":
            os.system("xdg-open mailto:mishra9759harshit@gmail.com")
        elif choice == "3":
            display_faq()
        elif choice == "4":
            sql_tips()
        else:
            user_dashboard()

def display_faq():
    """Interactive FAQ section that provides helpful information"""
    console.print("[bold yellow]FAQ Section[/bold yellow]")
    console.print("[green]1.[/green] How to create a table?")
    console.print("[green]2.[/green] How to retrieve data using SELECT?")
    console.print("[green]3.[/green] How to insert data into a table?")
    console.print("[green]4.[/green] How to fix 'Foreign Key constraint failed' error?")
    console.print("[green]5.[/green] How to perform JOINs?")
    console.print("[green]6.[/green] How to improve query performance?")

    faq_choice = Prompt.ask("Select a FAQ number or type 'exit' to return:", choices=["1", "2", "3", "4", "5", "6", "exit"])

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
    elif faq_choice == "exit":
        user_dashboard()

def sql_tips():
    """Display advanced SQL tips"""
    console.print("[bold yellow]SQL Tips[/bold yellow]")
    console.print("[green]1.[/green] Always use [bold]parameterized queries[/bold] to prevent SQL injection.")
    console.print("[green]2.[/green] Use [bold]EXPLAIN PLAN[/bold] to analyze and optimize query performance.")
    console.print("[green]3.[/green] When joining tables, always use [bold]table aliases[/bold] for clarity.")
    console.print("[green]4.[/green] Avoid using SELECT * in production queries. Always specify column names.")
    console.print("[green]5.[/green] Use [bold]indexes[/bold] for frequently searched columns to speed up queries.")
    console.print("[green]6.[/green] Keep your queries simple and readable. Complex queries should be broken into smaller steps.")

    console.print("[yellow]7.[/yellow] Use [bold]JOIN[/bold] instead of subqueries for better performance.")
    console.print("[yellow]8.[/yellow] Leverage [bold]CROSS JOIN[/bold] when you need to create combinations of rows from two tables.")
    console.print("[yellow]9.[/yellow] To ensure unique results, always use [bold]DISTINCT[/bold] in SELECT queries.")
    console.print("[yellow]10.[/yellow] Be cautious with [bold]NULL[/bold] values in your queries. They can often cause unexpected results.")

    console.print("[bold cyan]For more tips, visit the [blue]SQL Documentation[/blue] or reach out for support![/bold cyan]")

    choice = Prompt.ask("[bold yellow]Would you like to go back to the menu? (y/n)[/bold yellow]", choices=["y", "n"])
    if choice == "y":
        user_dashboard()
    else:
        console.print("[bold red]Exiting...[/bold red]")
        time.sleep(2)
        exit()


def user_dashboard():
    """Enhanced User Dashboard with progress bars and stylized menu"""
    print_header()

    cursor.execute("SELECT level FROM users WHERE username=?", (USER,))
    level = cursor.fetchone()[0]

    cursor.execute("SELECT date, score FROM progress WHERE user=?", (USER,))
    progress_data = cursor.fetchall()
    total_score = sum([row[1] for row in progress_data])
    avg_score = total_score / len(progress_data) if progress_data else 0
    progress_percentage = min(int(avg_score), 100)  # User's average score as progress percentage

    console.print(f"[bold green]Welcome back, {USER}![/bold green]")
    console.print(f"[bold cyan]Current Level: {level}[/bold cyan]")
    console.print(f"[bold yellow]Your Progress: {progress_percentage}%[/bold yellow]")
    
    # Progress bar for visual feedback on learning progress
    with Progress() as progress:
        task = progress.add_task("[cyan]Your Progress...", total=100)
        progress.update(task, completed=progress_percentage)

    # Display Menu with Stylized Options
    console.print("\n[bold yellow]Main Menu[/bold yellow]")
    console.print("[bold green][1] Practice Queries[/bold green] - Improve your SQL skills")
    console.print("[bold blue][2] Take a Quiz[/bold blue] - Test your SQL knowledge")
    console.print("[bold magenta][3] View My Profile[/bold magenta] - Track your progress")
    console.print("[bold cyan][4] Help[/bold cyan] - Get assistance and tips")
    console.print("[bold red][5] Logout[/bold red] - Exit and logout")

    choice = Prompt.ask("Please choose an option", choices=["1", "2", "3", "4", "5"])
    
    # Navigate to the appropriate action based on the user's choice
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


def logout():
    """Logout and return to the main menu"""
    console.print("[bold red]Logging out...[/bold red]")
    time.sleep(2)
    main_menu()


def main_menu():
    """Upgraded main menu with interactive feedback and stylized options"""
    print_header()
    console.print("[bold blue]SQL Android में आपका स्वागत करता हूँ। कृपया किसी भी समस्या के लिए मुझसे संपर्क अवश्य करें - हर्षित मिश्रा[/bold blue]")
    # Stylish menu with color formatting
    console.print("[bold yellow]Welcome to SQL Learning CLI[/bold yellow]")
    console.print("[bold green][1] Login[/bold green] - Access your account to start learning SQL")
    console.print("[bold blue][2] Register[/bold blue] - Create a new account to track your progress")
    console.print("[bold red][3] Exit[/bold red] - Exit the program")

    # User input for menu choice
    choice = Prompt.ask("Please choose an option", choices=["1", "2", "3"])

    if choice == "1":
        console.print("[cyan]Logging in... Please wait...[/cyan]")
        time.sleep(1)  # Simulate processing time
        login()
    elif choice == "2":
        console.print("[cyan]Registering a new account... Please wait...[/cyan]")
        time.sleep(1)  # Simulate processing time
        register()
    else:
        # Animated exit feedback
        console.print("[bold red]Goodbye![/bold red]")
        time.sleep(1)
        console.print("[yellow]We hope you come back to continue learning SQL![/yellow]")
        time.sleep(2)
        exit()


if __name__ == "__main__":
    install_dependencies()
    main_menu()
