from flask import Flask, render_template, request, redirect, url_for
from models.user_auth import verify_user
from models import admin 

app = Flask(__name__,
            template_folder="../frontend/templates",
            static_folder="../frontend/static"
            )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/job-seeker", methods=["GET", "POST"]) 
def job_seeker_login(): 
    if request.method == "POST": 
        email = request.form["email"] 
        password = request.form["password"] 
        print(email, password) 
        return "Job Seeker Login Submitted" 
    return render_template("job_seeker_login.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")

@app.route("/admin", methods = ["GET", "POST"])
def admin_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = verify_user(email,password)
        if user and user["role"] == "admin":
            return redirect(url_for("admin_dashboard"))
    return render_template("admin_login.html")

@app.route("/recruiter-login", methods = ["GET","POST"])
def recruiter_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(email,password)
    return render_template("recruiter_login.html")

if __name__ == "__main__":
    app.run(debug=True)