python
import datetime

class DPIA:
    def __init__(self):
        self.project_info = {}
        self.data_processing = {}
        self.necessity_proportionality = {}
        self.risk_assessment = []
        self.security_measures = {}
        self.conclusion = {}
        self.references = []
        self.attachments = []

    def collect_project_info(self):
        print("=== Prosjektinformasjon ===")
        self.project_info['project_name'] = input("Prosjektnavn: ")
        self.project_info['project_description'] = input("Prosjektbeskrivelse: ")
        self.project_info['project_owner'] = input("Prosjekteier (navn/avdeling): ")
        self.project_info['dpia_date'] = str(datetime.date.today())

    def collect_data_processing_info(self):
        print("\n=== Databehandling Beskrivelse ===")
        self.data_processing['database_system'] = input("Databasesystem (f.eks., MySQL, PostgreSQL): ")
        self.data_processing['data_flow_diagram'] = input("Sti til ER-diagram: ")
        self.data_processing['normalization_level'] = input("Normalisering (1NF, 2NF, 3NF, etc.): ")
        self.data_processing['personal_data'] = input("Beskrivelse av personopplysninger: ")

    def collect_necessity_proportionality_info(self):
        print("\n=== Nødvendighet og Proporsjonalitet ===")
        self.necessity_proportionality['necessity'] = input("Hvorfor er det nødvendig å lagre disse personopplysningene? ")
        self.necessity_proportionality['proportionality'] = input("Er mengden og typen personopplysninger passende og relevant for formålet? ")

    def collect_risk_assessment(self):
        print("\n=== Risikoanalyse ===")
        risks = [
            "SQL-injeksjon",
            "Uautorisert tilgang til data",
            "Tap av tilgjengelighet",
            "Dataintegritet",
            "Utilstrekkelig logging",
            "Lekkasje av ukryptert data",
            "Misbruk av datavisualisering"
        ]
        for risk in risks:
            risk_info = {}
            risk_info['risk'] = risk
            risk_info['likelihood'] = input(f"Sannsynlighet for {risk} (Lav/Middels/Høy): ")
            risk_info['impact'] = input(f"Konsekvens for {risk} (Lav/Middels/Høy): ")
            self.risk_assessment.append(risk_info)

    def collect_security_measures(self):
        print("\n=== Sikkerhetstiltak ===")
        self.security_measures['technical'] = {
            "brukeradministrasjon": input("Brukeradministrasjon: "),
            "indeksering": input("Indeksering: "),
            "logging": input("Logging: "),
            "backup": input("Backup og gjenoppretting: "),
            "kryptering": input("Kryptering: "),
            "sårbarhetshåndtering": input("Sårbarhetshåndtering: "),
            "inputvalidering": input("Inputvalidering: ")
        }
        self.security_measures['organizational'] = {
            "opplæring": input("Opplæring: "),
            "begrensninger_datavisualisering": input("Begrensninger for datavisualisering: "),
            "tilgangskontroll_rapporter": input("Tilgangskontroll for rapporter: ")
        }

    def collect_conclusion(self):
        print("\n=== Konklusjon, Overvåking og Evaluering ===")
        self.conclusion['risk_level'] = input("Samlet risikovurdering (lav, middels, høy): ")
        self.conclusion['decision'] = input("Avgjørelse (fortsette, modifisere, stoppe): ")
        self.conclusion['monitoring'] = input("Hvordan vil sikkerheten overvåkes kontinuerlig? ")
        self.conclusion['review'] = input("Når vil DPIA-en bli gjennomgått på nytt? ")

    def collect_references_attachments(self):
        print("\n=== Referanser og Vedlegg ===")
        while True:
            reference = input("Legg til referanse (trykk enter for å avslutte): ")
            if reference:
                self.references.append(reference)
            else:
                break
        while True:
            attachment = input("Legg til vedlegg (trykk enter for å avslutte): ")
            if attachment:
                self.attachments.append(attachment)
            else:
                break

    def generate_markdown(self):
        with open('DPIA_Rapport.md', 'w') as f:
            f.write(f"# DPIA Mal for Databasesystem: {self.project_info['project_name']}\n")
            f.write(f"**Prosjekteier:** {self.project_info['project_owner']}\n")
            f.write(f"**DPIA Dato:** {self.project_info['dpia_date']}\n")

            f.write("\n## 1. Prosjektbeskrivelse\n")
            f.write(f"* **Formål:** {self.project_info['project_description']}\n")
            f.write(f"* **Databeskrivelse:**\n")
            f.write(f"  * **Databasesystem:** {self.data_processing['database_system']}\n")
            f.write(f"  * **Struktur:** ![ER-diagram]({self.data_processing['data_flow_diagram']})\n")
            f.write(f"  * **Normalisering:** {self.data_processing['normalization_level']}\n")
            f.write(f"  * **Personopplysninger:** {self.data_processing['personal_data']}\n")

            f.write("\n## 2. Nødvendighet og Proporsjonalitet\n")
            f.write(f"* **Behovsvurdering:** {self.necessity_proportionality['necessity']}\n")
            f.write(f"* **Proporsjonalitetsvurdering:** {self.necessity_proportionality['proportionality']}\n")

            f.write("\n## 3. Risikoanalyse\n")
            f.write("| Risiko | Sannsynlighet | Konsekvens |\n")
            f.write("|--------|----------------|------------|\n")
            for risk in self.risk_assessment:
                f.write(f"| {risk['risk']} | {risk['likelihood']} | {risk['impact']} |\n")

            f.write("\n## 4. Sikkerhetstiltak\n")
            f.write("* **Tekniske tiltak:**\n")
            for key, value in self.security_measures['technical'].items():
                f.write(f"  * **{key.replace('_', ' ').title()}:** {value}\n")
            f.write("* **Organisatoriske tiltak:**\n")
            for key, value in self.security_measures['organizational'].items():
                f.write(f"  * **{key.replace('_', ' ').title()}:** {value}\n")

            f.write("\n## 5. Konklusjon, Overvåking og Evaluering\n")
            f.write(f"* **Samlet risikovurdering:** {self.conclusion['risk_level']}\n")
            f.write(f"* **Avgjørelse:** {self.conclusion['decision']}\n")
            f.write(f"* **Overvåking og evaluering:** {self.conclusion['monitoring']}\n")
            f.write(f"* **Gjennomgang:** {self.conclusion['review']}\n")

            f.write("\n## 6. Referanser og Vedlegg\n")
            if self.references:
                f.write("* **Referanser:**\n")
                for reference in self.references:
                    f.write(f"  * {reference}\n")
            if self.attachments:
                f.write("* **Vedlegg:**\n")
                for attachment in self.attachments:
                    f.write(f"  * {attachment}\n")

if __name__ == "__main__":
    dpia = DPIA()
    dpia.collect_project_info()
    dpia.collect_data_processing_info()
    dpia.collect_necessity_proportionality_info()
    dpia.collect_risk_assessment()
    dpia.collect_security_measures()
    dpia.collect_conclusion()
    dpia.collect_references_attachments()
    dpia.generate_markdown()
    print("DPIA rapport generert suksessfullt!")