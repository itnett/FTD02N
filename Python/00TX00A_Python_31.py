python
def evaluate_organization_structure(structure_type='Matrix', culture_type='Collaborative'):
    """
    Evaluate an organization's structure and culture.

    Parametere:
    structure_type (str): Type of organization structure (e.g., 'Functional', 'Divisional', 'Matrix').
    culture_type (str): Type of organization culture (e.g., 'Collaborative', 'Competitive', 'Creative', 'Controlled').

    Returnerer:
    None
    """
    print(f"Organizational Structure: {structure_type}")
    print(f"Organizational Culture: {culture_type}")
    
    if structure_type == 'Matrix':
        print("Matrix structure involves employees reporting to multiple managers, promoting better communication and flexibility.")
    elif structure_type == 'Functional':
        print("Functional structure involves employees grouped by their specialized functions, promoting expertise within the department.")
    elif structure_type == 'Divisional':
        print("Divisional structure involves departments divided by products, markets, or regions, promoting focus on specific business areas.")
    
    if culture_type == 'Collaborative':
        print("Collaborative culture emphasizes teamwork, open communication, and collective decision-making.")
    elif culture_type == 'Competitive':
        print("Competitive culture focuses on achieving results, outperforming competitors, and rewarding high performance.")
    elif culture_type == 'Creative':
        print("Creative culture encourages innovation, risk-taking, and flexibility.")
    elif culture_type == 'Controlled':
        print("Controlled culture values stability, efficiency, and adherence to rules and procedures.")

# Eksempel på bruk
evaluate_organization_structure()