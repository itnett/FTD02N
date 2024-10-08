python
def generate_cv(name="John Doe", contact_info="john.doe@example.com", experience=["Software Engineer at XYZ", "Intern at ABC"], education=["B.Sc. in Computer Science", "High School Diploma"]):
    """
    Generate a CV.
    
    Parameters:
    name (str): Name of the person.
    contact_info (str): Contact information.
    experience (list): List of work experiences.
    education (list): List of educational qualifications.
    
    Returns:
    str: Curriculum Vitae (CV).
    """
    cv = (
        f"Curriculum Vitae\n\n"
        f"Name: {name}\n"
        f"Contact Information: {contact_info}\n\n"
        f"Experience:\n"
    )
    for exp in experience:
        cv += f"- {exp}\n"
    
    cv += "\nEducation:\n"
    for edu in education:
        cv += f"- {edu}\n"
    
    print(cv)
    return cv

# Example usage
generate_cv()