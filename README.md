# SHAYAK — Community-Powered Emergency Assistance

SHAYAK is a Flask-based web prototype designed to support community-level disaster preparedness and emergency assistance by providing a simple platform for volunteer registration and administrator-managed volunteer coordination.

## Problem Statement

During emergencies and local disasters, people may struggle to find nearby assistance quickly, while willing volunteers may lack a simple way to coordinate support. SHAYAK aims to provide a digital foundation for more organized community assistance.

## Current Features

- Volunteer registration through a web form.
- Required-field validation and basic email validation.
- Duplicate-email prevention.
- SQLite database storage for registered volunteers.
- Protected administrator login.
- Administrator volunteer directory.
- Volunteer search and status filtering.
- Administrator-managed volunteer verification statuses: Pending verification, Verified, and Rejected.
- Session-based administrator access and logout.

## Technology Stack

- **Language:** Python
- **Web framework:** Flask
- **Frontend:** HTML and CSS
- **Database:** SQLite
- **Version control:** Git and GitHub

## Application Workflow

1. A volunteer opens the SHAYAK website.
2. The volunteer submits the registration form.
3. The application validates the submitted information.
4. Valid registration details are stored in the SQLite database.
5. An administrator logs in to view, search, filter, and update volunteer statuses.

## Getting Started

### Prerequisites

- Python installed on your computer.
- Git (optional, for cloning the repository).

### Installation

Clone the repository:

```bash
git clone https://github.com/Anjali-Anjali-2005/Shayak.git
cd Shayak
```

Create and activate a virtual environment on Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install Flask:

```powershell
python -m pip install Flask
```

### Configure Environment Variables

Set the Flask secret key and administrator credentials in PowerShell before starting the application:

```powershell
$env:SHAYAK_SECRET_KEY = python -c "import secrets; print(secrets.token_hex(32))"
$env:SHAYAK_ADMIN_USERNAME = "your_admin_username"
$env:SHAYAK_ADMIN_PASSWORD = "your_strong_admin_password"
```

Replace the example administrator credentials with your own private values. Do not commit secrets or real credentials to GitHub.

### Run the Application

```powershell
python app.py
```

Open the local address displayed in the terminal in your web browser. The SQLite database is initialized by the application when it starts.

**Note:** The environment variables above apply to the current PowerShell session. Keep the secret key stable between restarts if you want existing Flask sessions to remain valid.

## Planned Future Enhancements

The following are planned and are not yet implemented:

- Incident and emergency reporting.
- Location-based volunteer matching.
- Emergency alerts and notifications.
- Further improvements to disaster-response coordination.

## Current Limitations

SHAYAK is a prototype, not a live emergency dispatch service. Volunteer verification and coordination require administrative oversight. It does not currently provide real-time location tracking, automated emergency alerts, or guaranteed emergency assistance.

## Social Impact

SHAYAK aims to support safer and more resilient communities. Its intended social impact aligns with:

- **UN Sustainable Development Goal 11:** Sustainable Cities and Communities.
- **UN Sustainable Development Goal 13:** Climate Action.

These are intended contributions; the prototype's real-world impact has not yet been measured.

## Project Repository

[View SHAYAK on GitHub](https://github.com/Anjali-Anjali-2005/Shayak)

## Author

**Anjali** — Team Lead and sole team member.

Developed as a prototype for the VBYLD 2027 Hack for Social Cause initiative under the theme *Disaster Mitigation & Resilience*.