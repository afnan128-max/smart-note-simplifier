import re

def extract_formulas(text):
    pattern = r"([A-Za-z0-9+\-*/^=().\s]+)\s*=\s*([A-Za-z0-9+\-*/^=().\s]+)"
    matches = re.findall(pattern, text)
    formulas = [f"{lhs.strip()} = {rhs.strip()}" for lhs, rhs in matches]
    return list(set(formulas))[:10]  # limit to 10 formulas
