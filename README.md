# Executive Email Inference – Overbase Task

This project processes a messy executive dataset and generates two likely corporate email addresses for 50 senior executives.

## Approach
- Preserved raw input data
- Filtered only senior executive roles (C-suite, VP, Founder)
- Handled inconsistent CSV formatting and embedded URLs
- Inferred company domains heuristically
- Generated two common enterprise email formats per executive

## Output
The final output is a CSV containing:
- Executive name
- Company
- Two likely email addresses

> Emails are inferred, not verified.

## Tools
- Python
- VS Code
- Linux (WSL)