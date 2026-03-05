"""
Flask Portfolio Website — Chaitanya Annabathana
------------------------------------------------
Run:
    python -m venv venv
    source venv/bin/activate   # Windows: venv\\Scripts\\activate
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5000
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# SITE DATA  — edit here, templates stay generic
# ─────────────────────────────────────────────────────────────────────────────

OWNER = {
    "name": "Chaitanya Annabathana",
    "role": "Software Engineer | Distributed Systems | Backend (Python/C++)",
    "email": "annabathanachaitanya1999@gmail.com",
    "phone": "(475) 345-2920",
    "summary": (
        "Software Engineer with 3+ years of experience building and supporting "
        "cloud-based distributed systems in production. Strong foundation in "
        "Python and C++, backend services and microservices, AWS/GCP, "
        "Docker/Kubernetes. Comfortable owning features end-to-end, "
        "troubleshooting production issues, and delivering reliable, "
        "high-performance systems."
    ),
}

SKILLS = [
    # Languages
    "Python", "Go", "C++", "Scala",
    # Core CS
    "Distributed Systems Design", "Concurrency", "Networking", "Operating Systems",
    # Cloud
    "AWS", "Google Cloud Platform (GCP)", "Microsoft Azure",
    # Infra / DevOps
    "Docker", "Kubernetes", "Microservices Architecture",
    # Engineering
    "System Design", "REST APIs", "Performance Optimization", "Scalability",
    # Tooling
    "Git", "CI/CD", "Monitoring", "Debugging", "Linux",
]

PROJECTS = [
    {
        "title": "Cloud File Management System",
        "subtitle": "Learning Project",
        "description": (
            "Simulates cloud file upload, storage, and retrieval. "
            "REST APIs for upload/download/metadata in Python. "
            "Deployed on AWS, containerized with Docker. "
            "Includes logging/monitoring and concurrency testing."
        ),
        "tech": ["Python", "AWS", "Docker", "REST APIs", "Git"],
        "github": "https://github.com/<your-username>/cloud-file-management",
    },
    {
        "title": "Distributed Log Aggregation System",
        "subtitle": "Learning Project",
        "description": (
            "Simulates log collection and analysis from multiple services. "
            "Microservices design with producers/consumers. "
            "Python services to process and aggregate logs. "
            "Parallel processing and performance testing."
        ),
        "tech": ["Python", "Linux", "Microservices", "Git"],
        "github": "https://github.com/<your-username>/distributed-log-aggregation",
    },
]

EXPERIENCE = [
    {
        "company": "OSI Digital",
        "role": "Software Engineer",
        "location": "Hyderabad, India",
        "period": "Jan 2023 – Dec 2023",
        "bullets": [
            "Built backend services using Python and C++ in microservices architecture",
            "Designed distributed systems handling large volumes of application data",
            "Cloud deployments on AWS with Docker containerization and Kubernetes orchestration",
            "Developed REST APIs for service-to-service communication",
            "Profiled and optimized performance and scalability bottlenecks",
            "Linux debugging using OS, networking, and concurrency fundamentals",
            "Set up monitoring and logging pipelines for customer issue resolution",
            "Maintained CI/CD workflows using Git and Jenkins",
        ],
    },
    {
        "company": "Synopsys",
        "role": "Systems / Software Support Engineer",
        "location": "Hyderabad, India",
        "period": "Jan 2021 – Dec 2022",
        "bullets": [
            "Supported large-scale distributed backend systems in enterprise environments",
            "Linux troubleshooting using OS fundamentals",
            "Debugged networking and concurrency issues in production",
            "Assisted with cloud infrastructure setup on AWS/GCP",
            "Managed Docker deployments and Kubernetes clusters",
            "Maintained CI/CD workflows and monitored production systems",
        ],
    },
]

EDUCATION = [
    {
        "school": "California State University, East Bay",
        "degree": "Master's in Computer Science",
        "gpa": "3.7",
        "period": "Jan 2024 – Dec 2025",
    }
]

SOCIAL = {
    "github": "https://github.com/<your-username>",
    "linkedin": "https://linkedin.com/in/<your-profile>",
    "portfolio": "",   # add your blog/portfolio URL here if you have one
}


# ─────────────────────────────────────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Home page — hero, skills, projects, experience, education, footer."""
    return render_template(
        "index.html",
        owner=OWNER,
        skills=SKILLS,
        projects=PROJECTS,
        experience=EXPERIENCE,
        education=EDUCATION,
        social=SOCIAL,
    )


@app.route("/about")
def about():
    """About page — bio, strengths, education, experience highlights, resume."""
    return render_template(
        "about.html",
        owner=OWNER,
        skills=SKILLS,
        experience=EXPERIENCE,
        education=EDUCATION,
        social=SOCIAL,
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Contact page — form with basic validation; success message on same page."""
    errors = {}
    success = False
    form_data = {}

    if request.method == "POST":
        name    = request.form.get("name", "").strip()
        email   = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        form_data = {"name": name, "email": email, "message": message}

        # Basic validation
        if not name or len(name) < 2:
            errors["name"] = "Please enter your name (at least 2 characters)."
        if not email or "@" not in email or "." not in email.split("@")[-1]:
            errors["email"] = "Please enter a valid email address."
        if not message or len(message) < 10:
            errors["message"] = "Message must be at least 10 characters."

        if not errors:
            success = True
            form_data = {}   # clear form fields on success

    return render_template(
        "contact.html",
        owner=OWNER,
        social=SOCIAL,
        errors=errors,
        success=success,
        form_data=form_data,
    )


# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import os
    # PORT env var is set by Render/Railway in production.
    # Fallback to 8080 locally (5000 is grabbed by macOS AirPlay Receiver).
    port = int(os.environ.get("PORT", 8080))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
