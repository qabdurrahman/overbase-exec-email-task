import csv
import re

INPUT_FILE = "data/clean_execs.csv"
OUTPUT_FILE = "output/final_exec_emails.csv"

KNOWN_TLDS = [".io", ".ai", ".co", ".net", ".org"]

def infer_domain(company):
    company = company.lower().strip()

    # remove bracketed info like (Salesforce)
    company = re.sub(r"\(.*?\)", "", company).strip()

    # remove spaces
    company_nospace = company.replace(" ", "")

    # if company already ends with known TLD, keep it
    for tld in KNOWN_TLDS:
        if company_nospace.endswith(tld):
            return company_nospace

    # otherwise, normalize and assume .com
    company = company.replace("&", "and")
    company = re.sub(r"[^a-z0-9]", "", company)
    return company + ".com"


rows = []

with open(INPUT_FILE, newline="", encoding="utf-8", errors="ignore") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 4:
            continue

        name_parts = row[0].strip().split()
        if len(name_parts) < 2:
            continue

        first = name_parts[0].lower()
        last = name_parts[1].lower()
        full_name = f"{name_parts[0]} {name_parts[1]}"

        company_raw = row[-2].strip()
        if not company_raw:
            continue

        domain = infer_domain(company_raw)

        email_1 = f"{first}.{last}@{domain}"
        email_2 = f"{first}@{domain}"

        rows.append([full_name, company_raw, email_1, email_2])


with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Company", "Email 1", "Email 2"])
    for r in rows[:50]:
        writer.writerow(r)

print(f"Generated emails for {len(rows[:50])} executives.")
print(f"Saved to {OUTPUT_FILE}")
