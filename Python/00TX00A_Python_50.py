python
def create_business_plan(company_name="My Company", mission="To provide quality services", objectives=None):
    """
    Utarbeider en enkel forretningsplan.

    Parametere:
    company_name (str): Navn på selskapet (standardverdi "My Company")
    mission (str): Misjonserklæring (standardverdi "To provide quality services")
    objectives (list): Liste over mål (standardverdi None)

    Returnerer:
    str: Forretningsplan
    """
    if objectives is None:
        objectives = ["Increase market share", "Expand product line", "Enhance customer satisfaction"]

    plan = (
        f"Business Plan\n\n"
        f"Company Name: {company_name}\n"
        f"Mission: {mission}\n\n"
        f"Objectives:\n"
    )
    for obj in objectives:
        plan += f" - {obj}\n"
    
    return plan

# Eksempel på bruk
business_plan = create_business_plan()
print(business_plan)