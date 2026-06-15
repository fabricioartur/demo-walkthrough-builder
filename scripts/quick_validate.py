#!/usr/bin/env python3
"""Validate the Demo Walkthrough Builder repository structure."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "CONSTITUTION.md",
    "SKILL.md",
    "openai.yaml",
    "LICENSE",
    "CONTRIBUTING.md",
    ".gitignore",
    "examples/sample-input.md",
    "examples/review-output.md",
    "examples/final-walkthrough.md",
    "scripts/quick_validate.py",
]

REQUIRED_FOLDERS = [
    "templates",
    "examples",
    "scripts",
    "workspaces",
]

REQUIRED_TEMPLATES = [
    "templates/01-review-summary.md",
    "templates/02-unsupported-claims.md",
    "templates/03-commitment-boundaries.md",
    "templates/04-recommendation.md",
    "templates/05-demo-walkthrough.md",
    "templates/06-presenter-guide.md",
    "templates/07-objection-guide.md",
    "templates/08-follow-up.md",
]

REQUIRED_SAMPLE_WORKSPACE_FILES = [
    "workspaces/northstar-support-desk/workspace.md",
]

REQUIRED_SAMPLE_WORKSPACE_FOLDERS = [
    "workspaces/northstar-support-desk/inputs",
    "workspaces/northstar-support-desk/research",
    "workspaces/northstar-support-desk/evidence",
    "workspaces/northstar-support-desk/outputs",
    "workspaces/northstar-support-desk/notes",
]

POSITIONING_PHRASES = [
    "Demo Walkthrough Builder",
    "An evidence-first reviewer for customer-facing technical demos.",
    "The best demos don't start with slides. They start with understanding.",
    "linter for demos",
]

PRINCIPLES = [
    "Customer before Product",
    "Evidence before Narrative",
    "Unknowns are Valuable",
    "Validation before Commitment",
    "Conversation before Presentation",
    "Trust before Persuasion",
    "Never Overpromise",
    "Prefer Asking over Assuming",
    "Separate Facts from Inferences",
    "If Uncertain, Say So",
]


def read_text(path):
    return (ROOT / path).read_text(encoding="utf-8")


def check_exists(path):
    return (ROOT / path).exists()


def main():
    checks = []

    for folder in REQUIRED_FOLDERS:
        checks.append((f"required folder: {folder}", (ROOT / folder).is_dir()))

    for file_path in REQUIRED_FILES:
        checks.append((f"required file: {file_path}", check_exists(file_path)))

    for template in REQUIRED_TEMPLATES:
        checks.append((f"required template: {template}", check_exists(template)))

    for folder in REQUIRED_SAMPLE_WORKSPACE_FOLDERS:
        checks.append((f"sample workspace folder: {folder}", (ROOT / folder).is_dir()))

    for file_path in REQUIRED_SAMPLE_WORKSPACE_FILES:
        checks.append((f"sample workspace file: {file_path}", check_exists(file_path)))

    if check_exists("README.md"):
        readme = read_text("README.md")
        for phrase in POSITIONING_PHRASES:
            checks.append((f"README positioning phrase: {phrase}", phrase in readme))

    if check_exists("CONSTITUTION.md"):
        constitution = read_text("CONSTITUTION.md")
        for principle in PRINCIPLES:
            checks.append((f"constitution principle: {principle}", principle in constitution))

    if check_exists("SKILL.md"):
        skill = read_text("SKILL.md")
        checks.append(("SKILL starts in Context Collection Mode", "Start in Context Collection Mode by default" in skill))
        checks.append(("SKILL includes Customer Context Inventory", "Customer Context Inventory" in skill))
        checks.append(("SKILL includes Company Workspace Mode", "Company Workspace Mode" in skill))
        checks.append(("SKILL defines workspace output filenames", "outputs/01-review-summary.md" in skill))
        checks.append(("SKILL requires review before generation", "reviews before it generates" in skill))
        checks.append(("SKILL includes evidence classification", "Evidence Classification" in skill))

    if check_exists("examples/review-output.md"):
        review = read_text("examples/review-output.md")
        checks.append(("example recommendation is Proceed with Validation", "Status: Proceed with Validation" in review))

    failures = [name for name, passed in checks if not passed]

    print("Demo Walkthrough Builder validation")
    print("=" * 38)

    for name, passed in checks:
        status = "PASS" if passed else "FAIL"
        print(f"{status}  {name}")

    print("=" * 38)
    if failures:
        print(f"FAIL: {len(failures)} check(s) failed.")
        return 1

    print(f"PASS: {len(checks)} check(s) passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
