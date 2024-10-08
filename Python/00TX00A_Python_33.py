python
def recruitment_process(steps=["Need Analysis", "Job Description", "Sourcing Candidates", "Screening and Interviewing", "Selection", "Onboarding"]):
    """
    Describe the recruitment process steps.

    Parametere:
    steps (list): Liste over steg i rekrutteringsprosessen.

    Returnerer:
    None
    """
    print("Recruitment Process:")
    for i, step in enumerate(steps, start=1):
        print(f"{i}. {step}")

# Eksempel på bruk
recruitment_process()