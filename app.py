import os
from flask import (
    Flask, render_template, request, redirect,
    url_for, flash, session
)
import sqlite3
from pathlib import Path

app = Flask(__name__)

app.secret_key = os.environ.get("SHAYAK_SECRET_KEY")

if not app.secret_key:
    raise RuntimeError(
        "SHAYAK_SECRET_KEY environment variable is not configured."
    )

DATABASE = Path(__file__).resolve().parent / "shayak.db"
ADMIN_USERNAME = os.environ.get("SHAYAK_ADMIN_USERNAME")
ADMIN_PASSWORD = os.environ.get("SHAYAK_ADMIN_PASSWORD")


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            area TEXT NOT NULL,
            skills TEXT NOT NULL,
            availability TEXT NOT NULL,
            affiliation TEXT,
            verification_status TEXT NOT NULL DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        phone = request.form.get("phone", "").strip()
        area = request.form.get("area", "").strip()
        skills = request.form.get("skills", "").strip()
        availability = request.form.get("availability", "").strip()
        affiliation = request.form.get("affiliation", "").strip()

        if not all([
            full_name, email, phone, area,
            skills, availability
        ]):
            flash("Please complete all required fields.", "error")
            return render_template("register.html")

        if "@" not in email or "." not in email.split("@")[-1]:
            flash("Please enter a valid email address.", "error")
            return render_template("register.html")

        try:
            connection = get_db_connection()

            connection.execute("""
                INSERT INTO volunteers
                (full_name, email, phone, area, skills,
                 availability, affiliation)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                full_name, email, phone, area, skills,
                availability, affiliation
            ))

            connection.commit()
            connection.close()

            flash(
                "Registration submitted! Your verification status is Pending.",
                "success"
            )
            return redirect(url_for("register"))

        except sqlite3.IntegrityError:
            if "connection" in locals():
                connection.close()

            flash(
                "This email is already registered. Please use another email.",
                "error"
            )

        except sqlite3.Error:
            if "connection" in locals():
                connection.close()

            app.logger.exception("Database operation failed")
            flash("Unable to save your registration. Please try again.", "error")

    return render_template("register.html")
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not ADMIN_USERNAME or not ADMIN_PASSWORD:
            flash("Admin credentials are not configured.", "error")
            return render_template("admin_login.html")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session.clear()
            session["admin_logged_in"] = True
            flash("Admin login successful.", "success")
            return redirect(url_for("admin_volunteers"))

        flash("Invalid username or password.", "error")

    return render_template("admin_login.html")




@app.route("/admin/volunteers")
def admin_volunteers():
    if not session.get("admin_logged_in"):
        flash("Please log in as administrator to access this page.", "error")
        return redirect(url_for("admin_login"))

    search_query = request.args.get("search", "").strip()
    status_filter = request.args.get("status", "").strip()

    allowed_statuses = {
        "Pending verification",
        "Verified",
        "Rejected"
    }

    if status_filter not in allowed_statuses:
        status_filter = ""

    query = """
        SELECT id, full_name, email, phone, area,
               skills, availability, affiliation,
               verification_status
        FROM volunteers
        WHERE 1=1
    """
    parameters = []

    if search_query:
        pattern = f"%{search_query}%"
        query += """
            AND (
                full_name LIKE ?
                OR email LIKE ?
                OR area LIKE ?
            )
        """
        parameters.extend([pattern, pattern, pattern])

    if status_filter:
        query += " AND verification_status = ?"
        parameters.append(status_filter)

    query += " ORDER BY created_at DESC, id DESC"

    connection = get_db_connection()

    try:
        volunteers = connection.execute(
            query, parameters
        ).fetchall()
    finally:
        connection.close()

    return render_template(
        "admin_volunteers.html",
        volunteers=volunteers,
        search_query=search_query,
        status_filter=status_filter
    )


@app.route("/admin/volunteers/<int:volunteer_id>/status", methods=["POST"])
def update_volunteer_status(volunteer_id):
    if not session.get("admin_logged_in"):
        flash("Please log in as administrator to access this page.", "error")
        return redirect(url_for("admin_login"))

    new_status = request.form.get("verification_status", "").strip()

    allowed_statuses = {
        "Pending verification",
        "Verified",
        "Rejected"
    }

    if new_status not in allowed_statuses:
        flash("Invalid volunteer status.", "error")
        return redirect(url_for("admin_volunteers"))

    connection = get_db_connection()

    try:
        result = connection.execute(
            """
            UPDATE volunteers
            SET verification_status = ?
            WHERE id = ?
            """,
            (new_status, volunteer_id)
        )
        connection.commit()

        if result.rowcount == 0:
            flash("Volunteer not found.", "error")
        else:
            flash("Volunteer status updated successfully.", "success")
    finally:
        connection.close()

    return redirect(url_for("admin_volunteers"))

@app.route("/admin/logout")
def admin_logout():
    session.clear()
    flash("You have been logged out successfully.", "success")
    return redirect(url_for("home"))


@app.route("/api/status")
def status():
    return {
        "project": "SHAYAK",
        "status": "success",
        "message": "SHAYAK backend is running!"
    }


initialize_database()


if __name__ == "__main__":
    app.run(debug=True)
