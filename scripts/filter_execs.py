# Step 4: Filter senior executives from messy raw CSV

RAW_FILE = "data/raw_list.csv"
OUTPUT_FILE = "data/clean_execs.csv"

# Keywords that indicate senior executives
EXEC_KEYWORDS = [
    "chief",
    "cmo",
    "ceo",
    "cto",
    "cfo",
    "coo",
    "cro",
    "founder",
    "co-founder",
    "president",
    "vp",
    "svp",
    "evp",
    "head",
    "director"
]

filtered_lines = []

with open(RAW_FILE, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

for line in lines:
    line_lower = line.lower()
    if any(keyword in line_lower for keyword in EXEC_KEYWORDS):
        filtered_lines.append(line.strip())

# Write filtered executive rows
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for row in filtered_lines:
        f.write(row + "\n")

print(f"Filtered {len(filtered_lines)} senior executive records.")
print(f"Saved to {OUTPUT_FILE}")
