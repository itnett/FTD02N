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
HUNTER_API_KEY = 'your_hunter_api_key'
SECURITYTRAILS_API_KEY = 'your_securitytrails_api_key'

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

# Function to fetch subdomains using SecurityTrails
def get_subdomains(domain):
    logging.info("Fetching subdomains from SecurityTrails...")
    try:
        url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
        headers = {"APIKEY": SECURITYTRAILS_API_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        logging.warning(f"SecurityTrails API returned status code {response.status_code}")
        return []
    except Exception as e:
        logging.error(f"Error fetching subdomains: {e}")
        return str(e)

# Function to fetch email addresses using Hunter.io
def get_email_addresses(domain):
    logging.info("Fetching email addresses from Hunter.io...")
    try:
        url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={HUNTER_API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.warning(f"Hunter.io API returned status code {response.status_code}")
        return []
    except Exception as e:
        logging.error(f"Error fetching email addresses: {e}")
        return str(e)

# Function to fetch historical DNS data using SecurityTrails
def get_historical_dns(domain):
    logging.info("Fetching historical DNS data from SecurityTrails...")
    try:
        url = f"https://api.securitytrails.com/v1/history/{domain}/dns"
        headers = {"APIKEY": SECURITYTRAILS_API_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        logging.warning(f"SecurityTrails API returned status code {response.status_code}")
        return []
    except Exception as e:
        logging.error(f"Error fetching historical DNS data: {e}")
        return str(e)

# Function to check Exchange Online and legacy services using PowerShell
def check_exchange_and_legacy_services(domain):
    logging.info("Checking Exchange Online and legacy services...")
    powershell_script = f"""
    function Get-DnsRecord {{
        param (
            [string]$domain,
            [string]$recordType
        )
        $dnsRecord = Resolve-DnsName -Name $domain -Type $recordType
        return $dnsRecord
    }}

    $mxRecords = Get-DnsRecord -domain "{domain}" -recordType "MX"
    $autodiscoverRecord = Get-DnsRecord -domain "autodiscover.{domain}" -recordType "CNAME"

    if ($mxRecords.NameHost -match "protection.outlook.com") {{
        "Domain uses Exchange Online"
    }} else {{
        "Domain does not use Exchange Online"
    }}

    $legacyServices = @("smtp.{domain}", "pop3.{domain}", "imap.{domain}")
    foreach ($service in $legacyServices) {{
        try {{
            $connection = Test-NetConnection -ComputerName $service -Port 25, 110, 143
            if ($connection.TcpTestSucceeded) {{
                "$service is reachable on port $($connection.RemotePort)"
            }} else {{
                "$service is not reachable on port $($connection.RemotePort)"
            }}
        }} catch {{
            "Could not connect to $service"
        }}
    }}
    """
    try:
        result = subprocess.run(["powershell", "-Command", powershell_script], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        logging.error(f"Error running PowerShell script: {e}")
        return str(e)

# Function to find tenant domain.onmicrosoft.com UPN
def get_tenant_info(domain):
    logging.info("Fetching tenant information...")
    powershell_script = f"""
    function Get-TenantInfo {{
        param (
            [string]$domain
        )
        $record = Resolve-DnsName -Name $domain -Type TXT | Where-Object {{ $_.Strings -match "MS=" }}
        return $record
    }}

    $tenantInfo = Get-TenantInfo -domain "{domain}"
    if ($tenantInfo) {{
        $tenantInfo.Strings -match "MS=(.*)"
        "Tenant UPN: $($matches[1]).onmicrosoft.com"
    }} else {{
        "Tenant UPN not found"
    }}
    """
    try:
        result = subprocess.run(["powershell", "-Command", powershell_script], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        logging.error(f"Error running PowerShell script: {e}")
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

# Fetch subdomains
subdomains = get_subdomains(domain)
logging.info(f"Subdomains: {json.dumps(subdomains, indent=2)}")

# Fetch email addresses
email_addresses = get_email_addresses(domain)
logging.info(f"Email addresses: {json.dumps(email_addresses, indent=2)}")

# Fetch historical DNS data
historical_dns = get_historical_dns(domain)
logging.info(f"Historical DNS data: {json.dumps(historical_dns, indent=2)}")

# Check Exchange Online and legacy services
exchange_and_legacy_services = check_exchange_and_legacy_services(domain)
logging.info(f"Exchange and legacy services: {exchange_and_legacy_services}")

# Fetch tenant information
tenant_info = get_tenant_info(domain)
logging.info(f"Tenant information: {tenant_info}")

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
    f.write(json.dumps(virustotal_report, indent=2) + "\n\n")
    f.write("Subdomains:\n")
    f.write(json.dumps(subdomains, indent=2) + "\n\n")
    f.write("Email Addresses:\n")
    f.write(json.dumps(email_addresses, indent=2) + "\n\n")
    f.write("Historical DNS Data:\n")
    f.write(json.dumps(historical_dns, indent=2) + "\n\n")
    f.write("Exchange and Legacy Services:\n")
    f.write(exchange_and_legacy_services + "\n\n")
    f.write("Tenant Information:\n")
    f.write(tenant_info + "\n")