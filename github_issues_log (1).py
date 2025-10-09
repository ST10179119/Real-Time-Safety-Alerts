"""
Question 3.2 – GitHub Issues Log (Python version)
Project: Real-Time Safety Alerts
Purpose: Notify residents of emergencies, accidents, or suspicious activities
to enhance neighbourhood security.

Team Members:
1. Yoliswa Maduna
2. Ayanda Ngwenya
3. Adivhaho Muthambi
4. Pierre Mpapele
"""

# Define a list of dictionaries, one for each issue
issues = [
    {
        "Issue name": "Identify system stakeholder",
        "Assignees": "Yoliswa Maduna, Ayanda Ngwenya",
        "Labels": "Initiation, Meeting",
        "Projects": "Real-Time Safety Alerts",
        "Milestones": "Month 1 - Identify system "
    },
    {
        "Issue name": "conduct requirements interview",
        "Assignees": "Adivhaho Muthambi, Pierre Mpapele",
        "Labels": "Research, Planning",
        "Projects": "Real-Time Safety Alerts",
        "Milestones": "Month 2 – requirement interview"
    },
    {
        "Issue name": "Document stakeholder needs",
        "Assignees": "Ayanda Ngwenya, Pierre Mpapele",
        "Labels": "Architecture, Backend",
        "Projects": "Real-Time Safety Alerts",
        "Milestones": "Month 3 – Document needed "
    },
    {
        "Issue name": "Draft functional requirements",
        "Assignees": "Yoliswa Maduna, Adivhaho Muthambi",
        "Labels": "Design,",
        "Projects": "Real-Time Safety Alerts",
        "Milestones": "Month 4 – Draft requirement"
    },
    {
        "Issue name": "Draft non-functional requirements",
        "Assignees": "Pierre Mpapele, Ayanda Ngwenya",
        "Labels": "Backend, Development",
        "Projects": "Real-Time Safety Alerts",
        "Milestones": "Month 5 - Backend Development"
    },
    {
        "Issue name": "Review and finalize requirements",
        "Assignees": "Adivhaho Muthambi, Yoliswa Maduna",
        "Labels": "Integration, Testing",
        "Projects": "Real-Time Safety Alerts",
        "Milestones": "Month 6 - Integration and Testing"
    },
    {
        "Issue name": "Create initial sketches and layout",
        "Assignees": "Pierre Mpapele, Ayanda Ngwenya",
        "Labels": "Deployment, Release",
        "Projects": "Real-Time Safety Alerts",
        "Milestones": "Month 7 - Deployment and Launch"
    },
    {
        "Issue name": "Review wireframes with stakeholders",
        "Assignees": "Yoliswa Maduna, Adivhaho Muthambi",
        "Labels": "Feedback, Maintenance",
        "Projects": "Real-Time Safety Alerts",
        "Milestones": "Month 8 - Feedback Collection"
    },
    {
        "Issue name": "refine interface design",
        "Assignees": "All Team Members",
        "Labels": "Training, Community",
        "Projects": "Real-Time Safety Alerts",
        "Milestones": "Month 9 - Community Training"
    },
    {
        "Issue name": "Develop clickable prototype",
        "Assignees": "Yoliswa Maduna, Ayanda Ngwenya, Adivhaho Muthambi, Pierre Mpapele",
        "Labels": "Evaluation, Closeout",
        "Projects": "Real-Time Safety Alerts",
        "Milestones": "Month 12 - Project Completion"
    },
]

# Display header
print("=== GitHub Issues Log for Real-Time Safety Alerts ===\n")

# Print each issue
for i, issue in enumerate(issues, start=1):
    print(f"Issue {i}: {issue['Issue name']}")
    print(f"  Assignees : {issue['Assignees']}")
    print(f"  Labels    : {issue['Labels']}")
    print(f"  Projects  : {issue['Projects']}")
    print(f"  Milestones: {issue['Milestones']}")
    print("-" * 60)

print("\nAll issues have been listed successfully.")
print("Take a screenshot of this output for your submission.")
