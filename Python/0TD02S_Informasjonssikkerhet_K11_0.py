python
import json

class DPIATool:
    def __init__(self, project_name, owner, date):
        self.project_name = project_name
        self.owner = owner
        self.date = date
        self.project_description = {}
        self.necessity_and_proportionality = {}
        self.risk_analysis = []
        self.security_measures = []
        self.conclusion = {}

    def add_project_description(self, purpose, database_type, structure, normalization, personal_data):
        self.project_description = {
            "Purpose": purpose,
            "Database Type": database_type,
            "Structure": structure,
            "Normalization": normalization,
            "Personal Data": personal_data
        }

    def add_necessity_and_proportionality(self, necessity_assessment, proportionality_assessment):
        self.necessity_and_proportionality = {
            "Necessity Assessment": necessity_assessment,
            "Proportionality Assessment": proportionality_assessment
        }

    def add_risk(self, risk, likelihood, impact, risk_level):
        self.risk_analysis.append({
            "Risk": risk,
            "Likelihood": likelihood,
            "Impact": impact,
            "Risk Level": risk_level
        })

    def add_security_measure(self, measure, description):
        self.security_measures.append({
            "Measure": measure,
            "Description": description
        })

    def set_conclusion(self, overall_risk_level, decision, monitoring_plan):
        self.conclusion = {
            "Overall Risk Level": overall_risk_level,
            "Decision": decision,
            "Monitoring Plan": monitoring_plan
        }

    def generate_report(self):
        report = {
            "Project Name": self.project_name,
            "Owner": self.owner,
            "Date": self.date,
            "Project Description": self.project_description,
            "Necessity and Proportionality": self.necessity_and_proportionality,
            "Risk Analysis": self.risk_analysis,
            "Security Measures": self.security_measures,
            "Conclusion": self.conclusion
        }
        return json.dumps(report, indent=4)

# Eksempel på bruk
dpia_tool = DPIATool("Database Security Project", "John Doe", "01/07/2024")
dpia_tool.add_project_description(
    "To secure personal data in our customer database",
    "PostgreSQL",
    "ER Diagram",
    "3NF",
    "Names, Addresses, Social Security Numbers"
)
dpia_tool.add_necessity_and_proportionality(
    "Essential for business operations",
    "Data is minimized and anonymized where possible"
)
dpia_tool.add_risk("SQL Injection", "Medium", "High", "High")
dpia_tool.add_security_measure("SQL Injection Prevention", "Use prepared statements and parameterized queries")

report = dpia_tool.generate_report()
print(report)