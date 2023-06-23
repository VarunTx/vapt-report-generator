from fetch_vulnerability import getVulnDetails

url = "www.test.com"
poc = "poc.png"

with open('found_vulnerabilities.cfg', 'r') as file:
    found_vulnerability_names = [line.strip() for line in file]
print(found_vulnerability_names)

for name in found_vulnerability_names:
    details = getVulnDetails(name)
    if details:
        print(f"Details for {name}")
        print(details)
    else:
        print(f"No details found for {name}")
    print('\n\n\n')