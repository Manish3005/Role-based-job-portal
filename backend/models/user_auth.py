from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db_connection

def create_user():
    email = input("Enter email: ")
    passwd = input("Enter password: ")
    role = input("Enter role (admin/recruiter/job_seeker): ").lower()
    if role not in ["admin", "recruiter", "job_seeker"]:
        print("Invalid role!")
        return False
    hashed_passwd = generate_password_hash(passwd)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users(email, password_hash, role) VALUES (%s, %s, %s)",
        (email, hashed_passwd, role)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"{role} created successfully!")
    return True

def verify_user():
    email = input("Enter email: ")
    passwd = input("Enter password: ")
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, email, password_hash, role FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user and check_password_hash(user["password_hash"], passwd):
        return user
    return None

def login_flow():
    user = verify_user()
    if not user:
        print("Invalid credentials!")
        return None
    print(f"Login successful! Role: {user['role']}")
    if user["role"] == "admin":
        import admin
        admin.start(user)
    elif user["role"] == "recruiter":
        import recruiter
        recruiter.start(user)
    elif user["role"] == "job_seeker":
        import job_seeker
        job_seeker.start(user)

if __name__ == "__main__":
    while True:
        print("1. Login")
        print("2. Create new account")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            login_flow()
        elif choice == "2":
            create_user()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")
