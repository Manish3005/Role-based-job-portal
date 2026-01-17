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
    print("\nAll Users:")
    for u in users:
        print(f"ID: {u['id']}, Email: {u['email']}, Role: {u['role']}, Active: {u['is_active']}, Created: {u['created_at']}")

def view_all_companies():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id,name,website,email,contact_number FROM companies")
    companies = cursor.fetchall()
    cursor.close()
    conn.close()
    print("\nAll Companies:")
    for c in companies:
        print(f"ID: {c['id']}, Name: {c['name']}, Website: {c['website']}, Email: {c['email']}, Contact: {c['contact_number']}")

def view_all_jobs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT jobs.id, jobs.title, jobs.location, jobs.salary, companies.name AS company_name
        FROM jobs
        JOIN companies ON jobs.company_id = companies.id
    """)
    jobs = cursor.fetchall()
    cursor.close()
    conn.close()
    print("\nAll Jobs:")
    for j in jobs:
        print(f"ID: {j['id']}, Title: {j['title']}, Location: {j['location']}, Salary: {j['salary']}, Company: {j['company_name']}")








