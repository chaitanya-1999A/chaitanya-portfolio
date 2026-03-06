"""
Flask Portfolio Website — Chaitanya Annabathana
------------------------------------------------
Run:
    source .venv/bin/activate
    python app.py
Then open http://127.0.0.1:8080
"""

from flask import Flask, render_template, request

app = Flask(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# SITE DATA  — edit here, templates stay generic
# ─────────────────────────────────────────────────────────────────────────────

OWNER = {
    "name":  "Chaitanya Annabathana",
    "role":  "Platform / DevOps Engineer | AWS | IaC | Reliability | Python Automation",
    "email": "annabathanachaitanya1999@gmail.com",
    "phone": "(475) 345-2920",
    "summary": (
        "Platform/DevOps Engineer with 2+ years of experience designing and operating "
        "AWS infrastructure for data storage, processing, and reporting. "
        "Delivered Infrastructure-as-Code and automation that improved deployment "
        "consistency and reduced operational toil. Hands-on with AWS (EC2, S3, "
        "CloudWatch, IAM), SQL databases, and developer tooling in Python. Known for "
        "partnering with Security and IT to build reliable, scalable, cost-effective "
        "data platforms."
    ),
}

# Skills grouped by category — rendered as labeled chip groups in the UI
SKILL_GROUPS = [
    {
        "label":  "Cloud (AWS)",
        "skills": ["EC2", "S3", "CloudWatch", "IAM", "RDS"],
    },
    {
        "label":  "Infrastructure as Code",
        "skills": ["Terraform", "AWS CloudFormation"],
    },
    {
        "label":  "Programming",
        "skills": ["Python", "Bash"],
    },
    {
        "label":  "Databases",
        "skills": ["PostgreSQL", "MySQL", "SQL"],
    },
    {
        "label":  "Containers",
        "skills": ["Docker", "Kubernetes"],
    },
    {
        "label":  "Monitoring & Dev Tools",
        "skills": ["Prometheus", "Grafana", "Datadog", "Git"],
    },
]

PROJECTS = [
    {
        "title":    "AWS Data Platform Monitoring Pack",
        "subtitle": "Platform / DevOps Project",
        "description": (
            "Monitoring pack to track job health, data freshness, and storage growth "
            "using AWS metrics and logs. Published custom metrics from Python checks; "
            "configured CloudWatch alarms across 30+ scheduled jobs. Built Grafana "
            "dashboards to speed triage and surface reliability and cost signals."
        ),
        "tech":   ["AWS CloudWatch", "Python", "S3", "Grafana"],
        "github": "https://github.com/<your-username>/aws-data-platform-monitoring-pack",
    },
    {
        "title":    "IaC Bootstrap for Multi-Environment AWS Setup",
        "subtitle": "Infrastructure as Code Project",
        "description": (
            "IaC blueprint to provision a secure AWS baseline for dev/stage environments "
            "for data engineers. Codified IAM roles/policies, EC2 templates, and logging "
            "defaults with Git-reviewed changes. Automated validation checks to reduce "
            "misconfigurations and improve consistency."
        ),
        "tech":   ["Terraform", "AWS CloudFormation", "EC2", "IAM", "Git"],
        "github": "https://github.com/<your-username>/iac-bootstrap-multi-env-aws",
    },
]

EXPERIENCE = [
    {
        "company":  "OSI Digital",
        "role":     "Platform Engineer",
        "location": "India",
        "period":   "Jan 2023 – Dec 2023",
        "bullets": [
            "Designed and maintained AWS infrastructure for analytics workloads using EC2, S3, IAM, and CloudWatch across multiple environments",
            "Automated provisioning with Terraform and CloudFormation; reduced setup time from days to a few hours",
            "Implemented CloudWatch alarms and log metrics to improve incident visibility and reduce time to detect recurring issues",
            "Improved PostgreSQL reporting reliability by tuning queries and indexing; improved p95 latency by ~15%",
        ],
    },
    {
        "company":  "Synopsys",
        "role":     "DevOps / Reliability Engineer",
        "location": "India",
        "period":   "Jan 2022 – Dec 2022",
        "bullets": [
            "Built Python automation for operational checks (health validation, backup verification); reduced manual toil 6–8 hrs/week",
            "Maintained MySQL/PostgreSQL services; supported schema changes and integrity checks",
            "Containerized services with Docker; supported Kubernetes deployment patterns",
            "Created dashboards and alerts with Prometheus, Grafana, and Datadog to improve on-call observability",
        ],
    },
]

EDUCATION = [
    {
        "school": "California State University, East Bay",
        "degree": "Master's in Computer Science",
        "gpa":    "3.7",
        "period": "Jan 2024 – Dec 2025",
    }
]

SOCIAL = {
    "github":    "https://github.com/<your-username>",
    "linkedin":  "https://linkedin.com/in/<your-profile>",
    "portfolio": "",
}


# ─────────────────────────────────────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template(
        "index.html",
        owner=OWNER,
        skill_groups=SKILL_GROUPS,
        projects=PROJECTS,
        experience=EXPERIENCE,
        education=EDUCATION,
        social=SOCIAL,
    )


@app.route("/about")
def about():
    return render_template(
        "about.html",
        owner=OWNER,
        skill_groups=SKILL_GROUPS,
        experience=EXPERIENCE,
        education=EDUCATION,
        social=SOCIAL,
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    errors    = {}
    success   = False
    form_data = {}

    if request.method == "POST":
        name    = request.form.get("name",    "").strip()
        email   = request.form.get("email",   "").strip()
        message = request.form.get("message", "").strip()
        form_data = {"name": name, "email": email, "message": message}

        if not name or len(name) < 2:
            errors["name"] = "Please enter your name (at least 2 characters)."
        if not email or "@" not in email or "." not in email.split("@")[-1]:
            errors["email"] = "Please enter a valid email address."
        if not message or len(message) < 10:
            errors["message"] = "Message must be at least 10 characters."

        if not errors:
            success   = True
            form_data = {}

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
    port  = int(os.environ.get("PORT", 8080))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
