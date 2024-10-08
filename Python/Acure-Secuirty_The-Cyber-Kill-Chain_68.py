python
import requests
import json
import subprocess
import logging
from shodan import Shodan

# Set up logging
logging.basicConfig(filename='osint.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configure your API keys here
SHODAN_API_KEY = 'your_shodan_api_key'
CRTSH_API_URL = 'https://crt.sh/?q={}&output=json'

# Target domain
domain = 'example.com'

# Function to fetch DNS records
def get_dns_records(domain):
    logging.info("Fetching DNS records...")
    try:
        result = subprocess.run(['dig', 'ANY', domain], stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except Exception as e:
        logging.error(f"Error fetching DNS records: {e}")
        return str(e)

# Function to fetch WHOIS information
def get_whois_info(domain):
    logging.info("Fetching WHOIS information...")
    try:
        result = subprocess.run(['whois', domain], stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except Exception as e:
        logging.error(f"Error fetching WHOIS information: {e}")
        return str(e)

# Function to fetch SSL certificates from crt.sh
def get_ssl_certificates(domain):
    logging.info("Fetching SSL certificates...")
    try:
        response = requests.get(CRTSH_API_URL.format(domain))
        if response.status_code == 200:
            return response.json()
        logging.warning(f"crt.sh returned status code {response.status_code}")
        return []
    except Exception as e:
        logging.error(f"Error fetching SSL certificates: {e}")
        return str(e)

# Function to fetch Shodan data
def get_shodan_info(domain):
    logging.info("Fetching Shodan information...")
    api = Shodan(SHODAN_API_KEY)
    try:
        host = api.search(domain)
        return host
    except Exception as e:
        logging.error(f"Error fetching Shodan information: {e}")
        return str(e)

# Function to fetch Google Dorking results (requires custom scraping)
def get_google_dorks(domain):
    logging.info("Fetching Google Dorking results...")
    dorks = [
        f"site:{domain} inurl:sharepoint",
        f"site:{domain} inurl:teams",
        f"site:{domain} inurl:sites",
        f"site:{domain} inurl:calendar"
    ]
    # Placeholder for actual Google Dorking implementation
    return dorks

# Function to fetch Bing search results
def get_bing_search_results(domain):
    logging.info("Fetching Bing search results...")
    try:
        bing_api_url = f"https://api.bing.microsoft.com/v7.0/search?q=site:{domain}"
        headers = {"Ocp-Apim-Subscription-Key": "your_bing_api_key"}
        response = requests.get(bing_api_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        logging.warning(f"Bing API returned status code {response.status_code}")
        return []
    except Exception as e:
        logging.error(f"Error fetching Bing search results: {e}")
        return str(e)

# Function to fetch VirusTotal domain report
def get_virustotal_report(domain):
    logging.info("Fetching VirusTotal domain report...")
    try:
        virustotal_api_url = f"https://www.virustotal.com/api/v3/domains/{domain}"
        headers = {"x-apikey": "your_virustotal_api_key"}
        response = requests.get(virustotal_api_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        logging.warning(f"VirusTotal API returned status code {response.status_code}")
        return []
    except Exception as e:
        logging.error(f"Error fetching VirusTotal report: {e}")
        return str(e)

# Fetch DNS records
dns_records = get_dns_records(domain)
logging.info(f"DNS records: {dns_records}")

# Fetch WHOIS information
whois_info = get_whois_info(domain)
logging.info(f"WHOIS information: {whois_info}")

# Fetch SSL certificates
ssl_certificates = get_ssl_certificates(domain)
logging.info(f"SSL certificates: {json.dumps(ssl_certificates, indent=2)}")

# Fetch Shodan information
shodan_info = get_shodan_info(domain)
logging.info(f"Shodan information: {json.dumps(shodan_info, indent=2)}")

# Fetch Google Dorking results
google_dorks = get_google_dorks(domain)
logging.info(f"Google Dorking results: {google_dorks}")

# Fetch Bing search results
bing_results = get_bing_search_results(domain)
logging.info(f"Bing search results: {json.dumps(bing_results, indent=2)}")

# Fetch VirusTotal report
virustotal_report = get_virustotal_report(domain)
logging.info(f"VirusTotal report: {json.dumps(virustotal_report, indent=2)}")

# Write results to file
with open(f'osint_results_{domain}.txt', 'w') as f:
    f.write("DNS Records:\n")
    f.write(dns_records + "\n\n")
    f.write("WHOIS Information:\n")
    f.write(whois_info + "\n\n")
    f.write("SSL Certificates:\n")
    f.write(json.dumps(ssl_certificates, indent=2) + "\n\n")
    f.write("Shodan Information:\n")
    f.write(json.dumps(shodan_info, indent=2) + "\n\n")
    f.write("Google Dorking Results:\n")
    for dork in google_dorks:
        f.write(dork + "\n")
    f.write("\nBing Search Results:\n")
    f.write(json.dumps(bing_results, indent=2) + "\n\n")
    f.write("VirusTotal Report:\n")
    f.write(json.dumps(virustotal_report, indent=2) + "\n")