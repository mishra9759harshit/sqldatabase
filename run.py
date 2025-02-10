import sqlite3
import os
import time
import random
import getpass
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text

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

def install_dependencies():
    """
    Installs required depautomatically in Termux.
    """
    required_packages = ["python", "python-pip"]
    python_modules = ["requests", "matplotlib", "rich"]

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
            console.print("[red]Failed to send registration info.[/red]")
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Error sending registration info: {e}[/red]")


def register():
    print_header()
    console.print("[bold green]Register a New Account[/bold green]")
    username = Prompt.ask("Enter a username")
    email = Prompt.ask("Enter your email")
    password = getpass.getpass("Enter a password: ")

    cursor.execute("INSERT INTO users (username, email, password, level) VALUES (?, ?, ?, 1)", (username, email, password))
    conn.commit()

    console.print("[green]Registration successful![/green]")
    send_registration_data(username, email, password)  # Send user data to Formspree
    time.sleep(2)
    main_menu()



def login():
    global USER
    print_header()
    console.print("[bold blue]User Login[/bold blue]")
    username = Prompt.ask("Enter username")
    password = getpass.getpass("Enter password: ")
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
    """Improved SQL error handling with intelligent suggestions based on error context"""
    error_message = str(error).lower()
    
    # Common SQL errors and suggestions
    suggestions = {
        "no such table": "Check if the table exists. If not, use CREATE TABLE to create the table first.",
        "syntax error": "Check your SQL syntax. Ensure proper use of commas, quotes, and parentheses. For example, 'SELECT column FROM table' is correct.",
        "unknown column": "Check if the column name exists in the table. You may have mistyped the column name.",
        "foreign key constraint failed": "Ensure the referenced key exists in the parent table. Ensure the data you're inserting is valid and matches the foreign key constraint.",
        "datatype mismatch": "Ensure that you are inserting the correct data type for each column. For example, you cannot insert a string into an integer column.",
        "column not found": "Check the column name spelling or verify if the column exists in the table schema.",
        "subquery returns more than one row": "Ensure that your subquery returns only one value. Consider using aggregation functions or limiting the result of the subquery.",
        "duplicate entry": "You are trying to insert a duplicate value into a column that has a unique constraint. Check for duplicates and try again.",
        "no such function": "You are trying to use a function that does not exist. Make sure the function is available in the database you're using.",
        "incorrect number of arguments": "Check the number of arguments for functions like COUNT(), SUM(), etc. Ensure you're passing the correct number of arguments for the function you're using."
    }

    # Suggest based on specific error pattern
    for key, suggestion in suggestions.items():
        if key in error_message:
            console.print(f"[bold yellow]Suggestion:[/bold yellow] {suggestion}")
            return
    
    # More advanced suggestions based on query types (SELECT, INSERT, etc.)
    if "select" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] Ensure you are selecting columns that exist. Use DISTINCT for unique results.")
        console.print("[bold yellow]Best Practice:[/bold yellow] Always use aliases for tables and columns to avoid ambiguity, e.g., SELECT t.name FROM users t.")
    
    if "insert" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] Make sure you're inserting values that match the column order and data types. If using named columns, verify column names.")
        console.print("[bold yellow]Best Practice:[/bold yellow] Use parameterized queries to prevent SQL injection attacks.")
    
    if "update" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] Ensure that your WHERE clause is correctly defined to prevent updating all rows. Consider using LIMIT for safety.")
    
    if "delete" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] Always double-check your WHERE clause to ensure you're deleting the right rows. Avoid using DELETE without WHERE in production.")

    # Suggestions for specific errors
    if "join" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] If you're using JOINs, ensure that the tables you're joining are correctly referenced. Use table aliases for better readability.")
    
    if "group by" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] If you're using GROUP BY, ensure you are using aggregate functions like COUNT, SUM, AVG, etc., for non-grouped columns.")
    
    if "having" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] The HAVING clause is used to filter groups. If you're not using GROUP BY, consider using WHERE instead.")
    
    if "order by" in error_message:
        console.print("[bold yellow]Advanced Suggestion:[/bold yellow] When using ORDER BY, ensure that the column you're sorting by exists in the SELECT statement or table.")

    # Provide a general suggestion for unknown errors
    if not any(key in error_message for key in suggestions):
        console.print("[bold yellow]General Suggestion:[/bold yellow] Please review your SQL syntax and make sure all tables and columns are properly referenced.")
    
    console.print("[bold yellow]Best Practice:[/bold yellow] Regularly use comments in your queries to describe what each part does for better clarity and maintenance.")


def sql_quiz():
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
        
        answer_idx = Prompt.ask("Choose your answer (1-4)", choices=["1", "2", "3", "4"])
        user_answer = options[int(answer_idx) - 1]
        
        feedback = provide_detailed_feedback(user_answer, correct_answer)
        console.print(feedback)
        
        if user_answer.upper() == correct_answer.upper():
            score += 1

        time.sleep(1)  # Small delay between questions

    # Save score to progress table
    cursor.execute("INSERT INTO progress (user, date, score) VALUES (?, DATE('now'), ?)", (USER, score))
    conn.commit()
    
    # Show results
    console.print(f"[bold cyan]Quiz Completed! Your Score: {score}/{total_questions}[/bold cyan]")
    
    # Show Leaderboard (top scores)
    show_leaderboard()
    
    time.sleep(3)
    user_dashboard()

def show_leaderboard():
    """Display the top 5 scores from the database"""
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

    # Fetch user's level and progress data
    cursor.execute("SELECT level FROM users WHERE username=?", (USER,))
    level = cursor.fetchone()[0]

    cursor.execute("SELECT date, score FROM progress WHERE user=?", (USER,))
    progress_data = cursor.fetchall()

    if not progress_data:
        console.print("[red]No progress data available for this user.[/red]")
        return

    # Extract dates and scores for plotting
    dates = [row[0] for row in progress_data]
    scores = [row[1] for row in progress_data]

    # Create an interactive graph
    plt.figure(figsize=(8, 6))
    plt.plot(dates, scores, marker="o", linestyle="-", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Score")
    plt.title(f"{USER}'s Progress")
    plt.xticks(rotation=45)
    plt.grid(True)
    
    # Show graph with interactive zoom (requires matplotlib to be set up properly in Termux)
    plt.show()

    # Display user's progress with a progress bar
    console.print(f"\n[bold cyan]Your Level: {level}[/bold cyan]\n")
    progress = Progress()
    task = progress.add_task("[cyan]Level Progress...", total=100)

    # Simulate progress bar based on the user's score
    score_percentage = min(int(sum(scores) / (len(scores) * 100) * 100), 100)  # Normalize score to percentage
    progress.update(task, completed=score_percentage)
    while not progress.finished:
        progress.advance(task)

    console.print(f"\n[bold yellow]Your overall performance is at {score_percentage}%[/bold yellow]")
    
    # Motivation based on the user's performance
    if score_percentage == 100:
        console.print("[bold green]Outstanding! You're a SQL master! Keep it up![/bold green]")
    elif score_percentage >= 75:
        console.print("[bold green]Great job! You're making excellent progress.[/bold green]")
    elif score_percentage >= 50:
        console.print("[bold yellow]Good progress, but keep practicing to improve.[/bold yellow]")
    else:
        console.print("[bold red]Don't give up! Keep practicing and you'll get there.[/bold red]")

    # Provide detailed score breakdown
    console.print("\n[bold cyan]Score Breakdown by Date:[/bold cyan]")
    table = Table(show_lines=True)
    table.add_column("Date", justify="center")
    table.add_column("Score", justify="center")
    for date, score in zip(dates, scores):
        table.add_row(date, str(score))
    console.print(table)

    # Sleep for a bit before going back to the dashboard
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
        console.print("[yellow]4.[/yellow] Return to Main Menu")

        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4"])

        if choice == "1":
            os.system("xdg-open https://github.com/repo")
        elif choice == "2":
            os.system("xdg-open mailto:mishra9759harshit@gmail.com")
        elif choice == "3":
            display_faq()
        else:
            user_dashboard()

    else:
        console.print("[bold cyan]सहायता अनुभाग (हिंदी में)[/bold cyan]")
        console.print("[yellow]1.[/yellow] ReadMe देखें: https://github.com/repo")
        console.print("[yellow]2.[/yellow] संपर्क करें: mishra9759harshit@gmail.com")
        console.print("[yellow]3.[/yellow] सामान्य प्रश्न: [bold]सहायता प्राप्त करने के लिए 'FAQ' टाइप करें।[/bold yellow]")
        console.print("[yellow]4.[/yellow] मुख्य मेनू पर वापस जाएं")

        choice = Prompt.ask("कृपया एक विकल्प चुनें", choices=["1", "2", "3", "4"])

        if choice == "1":
            os.system("xdg-open https://github.com/repo")
        elif choice == "2":
            os.system("xdg-open mailto:mishra9759harshit@gmail.com")
        elif choice == "3":
            display_faq()
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


def user_dashboard():
    """Enhanced User Dashboard with progress bars and stylized menu"""
    print_header()
    
    # Display current progress level dynamically
    cursor.execute("SELECT level FROM users WHERE username=?", (USER,))
    level = cursor.fetchone()[0]

    cursor.execute("SELECT date, score FROM progress WHERE user=?", (USER,))
    progress_data = cursor.fetchall()
    total_score = sum([row[1] for row in progress_data])
    avg_score = total_score / len(progress_data) if progress_data else 0
    progress_percentage = min(int(avg_score), 100)  # User's average score as progress percentage

    # Display User Information and Progress
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
