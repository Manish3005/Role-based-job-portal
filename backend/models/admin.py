from db import get_db_connection

def start(user):
    while(True):
        print("\nAdmin panel")
        print("1.View All users")
        print("2.View All Companies")
        print("3.View All Jobs")
        print("4.Logout")
        choice = int(input("Enter yr choice:"))
        if(choice == 1):
            view_all_users()
        elif(choice == 2):
            view_all_companies()
        elif(choice == 3):
            view_all_jobs()
        elif(choice == 4):
            print("Logging out...")
            break
        else:
            print("Invalid choice")

def view_all_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, email, role, is_active, created_at FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

def view_all_companies():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id,name,website,email,contact_number FROM companies")
    companies = cursor.fetchall()
    cursor.close()
    conn.close()
    return companies

def view_all_jobs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT jobs.id, jobs.title, jobs.location, jobs.salary,jobs.posted_date, companies.name AS company_name
        FROM jobs
        JOIN companies ON jobs.company_id = companies.id
    """)
    jobs = cursor.fetchall()
    cursor.close()
    conn.close()
    return jobs







