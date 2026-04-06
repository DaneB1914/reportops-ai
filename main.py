import json
import argparse
from core.generator import generate_vuln_report

def load_findings(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def calculate_severity(finding):
    av = finding.get("attack_vector", "network")
    complexity = finding.get("complexity", "low")
    priv = finding.get("privileges_required", "none")

    # VERY basic scoring logic (we’ll upgrade this later)
    score = 0

    if av == "network":
        score += 3
    if complexity == "low":
        score += 3
    if priv == "none":
        score += 3

    if score >= 8:
        return "Critical"
    elif score >= 6:
        return "High"
    elif score >= 4:
        return "Medium"
    else:
        return "Low"

def main():
    parser = argparse.ArgumentParser(description="AI Vulnerability Report Generator")
    parser.add_argument("--input", required=True, help="Path to findings JSON file")
    parser.add_argument("--output", default="output/report.md", help="Output report file")

    args = parser.parse_args()

    findings = load_findings(args.input)

    full_report = "# Penetration Test Report\n\n"

    full_report += "## Executive Summary\n"
    full_report += "This report outlines vulnerabilities discovered during testing.\n\n"

    full_report += "## Findings\n\n"
