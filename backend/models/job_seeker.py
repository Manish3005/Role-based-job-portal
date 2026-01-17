from db import get_db_connection

def start(user):
    while True:
        print("\nJob Seeker Panel")
        print("1. View jobs")
        print("2. Apply for job")
        print("3. View my applications")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_jobs()
        elif choice == "2":
            apply_job(user)
        elif choice == "3":
            view_applications(user)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def view_jobs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT jobs.id, jobs.title, jobs.location, jobs.salary, companies.name AS company
        FROM jobs
        JOIN companies ON jobs.company_id = companies.id
    """)
    jobs = cursor.fetchall()
    cursor.close()
    conn.close()
    print("\nAvailable Jobs:")
    for j in jobs:
        print(f"ID: {j['id']} | {j['title']} | {j['company']} | {j['location']} | {j['salary']}")

def apply_job(user):
    job_id = input("Enter job ID to apply: ")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO applications(user_id, job_id) VALUES (%s, %s)",
        (user["id"], job_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("Applied successfully!")

def view_applications(user):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT jobs.title, companies.name AS company, applications.status
        FROM applications
        JOIN jobs ON applications.job_id = jobs.id
        JOIN companies ON jobs.company_id = companies.id
        WHERE applications.user_id = %s
    """, (user["id"],))
    apps = cursor.fetchall()
    cursor.close()
    conn.close()
    print("\nMy Applications:")
    for a in apps:
        print(f"{a['title']} | {a['company']} | Status: {a['status']}")
