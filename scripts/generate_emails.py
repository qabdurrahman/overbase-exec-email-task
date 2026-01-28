import csv
import re

INPUT_FILE = "data/clean_execs.csv"
OUTPUT_FILE = "output/final_exec_emails.csv"

def clean_domain(company):
    company = company.lower()
    company = re.sub(r"\(.*?\)", "", company)   # remove brackets
    company = company.replace("&", "and")
    company = re.sub(r"[^a-z0-9 ]", "", company)
    company = company.replace(" ", "")
    return company

rows = []

with open(INPUT_FILE, newline="", encoding="utf-8", errors="ignore") as f:
    reader = csv.reader(f)
    for row in reader:
        # we expect at least: name, title, company, url
        if len(row) < 4:
            continue

        name_parts = row[0].strip().split()
        if len(name_parts) < 2:
            continue

        first_name = name_parts[0].lower()
        last_name = name_parts[1].lower()
        full_name = f"{name_parts[0]} {name_parts[1]}"

        # company is SECOND LAST column
        company_raw = row[-2].strip()
        if not company_raw:
            continue

        domain = clean_domain(company_raw)
        if len(domain) < 3:
            continue

        email_1 = f"{first_name}.{last_name}@{domain}.com"
        email_2 = f"{first_name}@{domain}.com"

        rows.append([full_name, company_raw, email_1, email_2])

# write final CSV
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Company", "Email 1", "Email 2"])
    for r in rows[:50]:
        writer.writerow(r)

print(f"Generated emails for {len(rows[:50])} executives.")
print(f"Saved to {OUTPUT_FILE}")
