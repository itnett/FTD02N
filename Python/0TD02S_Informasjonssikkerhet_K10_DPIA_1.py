python
import os
import datetime

class DPIA:
    def __init__(self):
        self.project_info = {}
        self.data_processing = {}
        self.necessity_proportionality = {}
        self.risk_assessment = []
        self.risk_mitigation = []
        self.stakeholder_consultation = {}
        self.approval_signoff = {}

    def collect_project_info(self):
        print("=== Project Information ===")
        self.project_info['project_name'] = input("Project Name: ")
        self.project_info['project_description'] = input("Project Description: ")
        self.project_info['project_manager'] = input("Project Manager (name and contact): ")
        self.project_info['dpia_lead'] = input("DPIA Lead (name and contact): ")
        self.project_info['date'] = str(datetime.date.today())

    def collect_data_processing_info(self):
        print("\n=== Data Processing Description ===")
        self.data_processing['purpose'] = input("Purpose of Processing: ")
        self.data_processing['nature'] = input("Nature of Data: ")
        self.data_processing['data_subjects'] = input("Data Subjects: ")
        self.data_processing['data_flow_diagram'] = input("Data Flow Diagram (path to file): ")

    def collect_necessity_proportionality_info(self):
        print("\n=== Necessity and Proportionality ===")
        self.necessity_proportionality['legal_basis'] = input("Legal Basis for Processing: ")
        self.necessity_proportionality['data_minimization'] = input("Data Minimization: ")
        self.necessity_proportionality['retention_period'] = input("Retention Period: ")

    def collect_risk_assessment(self):
        print("\n=== Risk Assessment ===")
        while True:
            risk = {}
            risk['description'] = input("Risk Description: ")
            risk['likelihood'] = input("Likelihood (Low/Medium/High): ")
            risk['severity'] = input("Severity (Low/Medium/High): ")
            self.risk_assessment.append(risk)
            more = input("Add another risk? (y/n): ")
            if more.lower() != 'y':
                break

    def collect_risk_mitigation(self):
        print("\n=== Measures to Address Risks ===")
        for risk in self.risk_assessment:
            mitigation = {}
            mitigation['risk_description'] = risk['description']
            mitigation['measure'] = input(f"Mitigation Measure for '{risk['description']}': ")
            mitigation['responsible_party'] = input("Responsible Party: ")
            mitigation['deadline'] = input("Deadline: ")
            self.risk_mitigation.append(mitigation)

    def collect_stakeholder_consultation(self):
        print("\n=== Consultation with Stakeholders ===")
        self.stakeholder_consultation['internal'] = input("Internal Stakeholders Consulted: ")
        self.stakeholder_consultation['external'] = input("External Stakeholders Consulted: ")
        self.stakeholder_consultation['feedback'] = input("Consultation Feedback: ")

    def collect_approval_signoff(self):
        print("\n=== Approval and Sign-off ===")
        self.approval_signoff['dpo_name'] = input("DPO Name: ")
        self.approval_signoff['dpo_signature'] = input("DPO Signature: ")
        self.approval_signoff['dpo_date'] = input("DPO Date: ")
        self.approval_signoff['project_owner_name'] = input("Project Owner Name: ")
        self.approval_signoff['project_owner_signature'] = input("Project Owner Signature: ")
        self.approval_signoff['project_owner_date'] = input("Project Owner Date: ")

    def generate_markdown(self):
        with open('DPIA_Report.md', 'w') as f:
            f.write("# Data Protection Impact Assessment (DPIA) Report\n\n")
            f.write("## 1. Project Information\n")
            for key, value in self.project_info.items():
                f.write(f"**{key.replace('_', ' ').title()}:** {value}\n")
            f.write("\n## 2. Data Processing Description\n")
            for key, value in self.data_processing.items():
                f.write(f"**{key.replace('_', ' ').title()}:** {value}\n")
            f.write("\n## 3. Necessity and Proportionality\n")
            for key, value in self.necessity_proportionality.items():
                f.write(f"**{key.replace('_', ' ').title()}:** {value}\n")
            f.write("\n## 4. Risk Assessment\n")
            f.write("| Risk Description | Likelihood | Severity |\n")
            f.write("|------------------|------------|----------|\n")
            for risk in self.risk_assessment:
                f.write(f"| {risk['description']} | {risk['likelihood']} | {risk['severity']} |\n")
            f.write("\n## 5. Measures to Address Risks\n")
            f.write("| Risk Description | Mitigation Measure | Responsible Party | Deadline |\n")
            f.write("|------------------|--------------------|-------------------|----------|\n")
            for mitigation in self.risk_mitigation:
                f.write(f"| {mitigation['risk_description']} | {mitigation['measure']} | {mitigation['responsible_party']} | {mitigation['deadline']} |\n")
            f.write("\n## 6. Consultation with Stakeholders\n")
            for key, value in self.stakeholder_consultation.items():
                f.write(f"**{key.replace('_', ' ').title()}:** {value}\n")
            f.write("\n## 7. Approval and Sign-off\n")
            for key, value in self.approval_signoff.items():
                f.write(f"**{key.replace('_', ' ').title()}:** {value}\n")

if __name__ == "__main__":
    dpia = DPIA()
    dpia.collect_project_info()
    dpia.collect_data_processing_info()
    dpia.collect_necessity_proportionality_info()
    dpia.collect_risk_assessment()
    dpia.collect_risk_mitigation()
    dpia.collect_stakeholder_consultation()
    dpia.collect_approval_signoff()
    dpia.generate_markdown()
    print("DPIA report generated successfully!")