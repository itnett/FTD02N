python
def reflect_on_social_development(developments, company_impact):
    """
    Reflekterer over samfunnsutvikling og relaterer dette til bedriftens situasjon.

    Parametere:
    developments (list): Liste over samfunnsutviklinger
    company_impact (dict): Ordbok med påvirkning på bedriften

    Returnerer:
    None
    """
    print("Societal Developments:")
    for development in developments:
        print(f" - {development}")
    
    print("\nImpact on Company:")
    for factor, impact in company_impact.items():
        print(f"{factor}: {impact}")

# Eksempel på bruk
developments = ["Technological advancements", "Economic shifts", "Environmental concerns"]
company_impact = {
    "Adoption of new technologies": "Increased efficiency and innovation",
    "Economic downturns": "Potential for reduced sales",
    "Environmental regulations": "Need for sustainable practices"
}
reflect_on_social_development(developments, company_impact)