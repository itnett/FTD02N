python
def recruitment_process(steps=["Need Analysis", "Job Description", "Sourcing Candidates", "Screening and Interviewing", "Selection", "Onboarding"]):
    """
    Describe the recruitment process steps.
    
    Parameters:
    steps (list): List of steps in the recruitment process.
    
    Returns:
    None
    """
    print("Recruitment Process:")
    for i, step in enumerate(steps, start=1):
        print(f"{i}. {step}")
    
    return

# Example usage
recruitment_process()