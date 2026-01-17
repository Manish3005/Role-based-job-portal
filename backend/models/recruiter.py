from db import get_db_connection

def start(user):
    while True:
        print("\nRecruiter Panel")
        print("1. Add company")
        print("2. Post job")
        print("3. View applicants")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_company()
        elif choice == "2":
            post_job()
        elif choice == "3":
            view_applicants()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def add_company():
    name = input("Company name: ")
    website = input("Website: ")
    email = input("Email: ")
    contact = input("Contact number: ")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO companies(name, website, email, contact_number) VALUES (%s, %s, %s, %s)",
        (name, website, email, contact)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("Company added successfully!")

def post_job():
    company_id = input("Enter company ID: ")
    title = input("Job title: ")
    description = input("Job description: ")
    location = input("Location: ")
    salary = input("Salary: ")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO jobs(company_id, title, description, location, salary) VALUES (%s, %s, %s, %s, %s)",
        (company_id, title, description, location, salary)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("Job posted successfully!")

def view_applicants():
    job_id = input("Enter job ID: ")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT users.email, applications.status
        FROM applications
        JOIN users ON applications.user_id = users.id
        WHERE applications.job_id = %s
    """, (job_id,))
    applicants = cursor.fetchall()
    cursor.close()
    conn.close()

    print("\nApplicants:")
    for a in applicants:
        print(f"{a['email']} | Status: {a['status']}")
