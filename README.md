# Demo Walkthrough Builder

An evidence-first reviewer for customer-facing technical demos.

The best demos don't start with slides. They start with understanding.

Demo Walkthrough Builder helps Solutions Engineers and Sales Engineers review customer context, identify unsupported claims, expose unknowns, define commitment boundaries, and prepare safer customer-facing technical conversations.

It works like a linter for demos: before you present, it checks whether your narrative is grounded, whether your claims are supported, and whether your assumptions should be validated.

## Why This Exists

Many technical demos fail because they start with product features instead of customer understanding. The presenter may have a good product story, but the customer hears unsupported assumptions, premature commitments, or claims that are not backed by discovery evidence.

Demo Walkthrough Builder exists to slow the preparation process down at the right moment. It helps technical sellers review what they know, what they can safely say, what they need to validate, and what they should avoid saying in front of a customer.

## What This Project Is

Demo Walkthrough Builder is:

- an open source AI playbook
- a Codex Skill
- a demo reviewer
- a preparation assistant
- a linter for customer-facing technical conversations

It is designed for Solutions Engineers, Sales Engineers, Developer Advocates, and technical customer-facing teams who want to prepare demos with more discipline and less risk.

## What This Project Is Not

Demo Walkthrough Builder is not:

- a slide generator
- a generic script writer
- a sales automation tool
- a replacement for Solutions Engineer judgment
- an official OpenAI project

This project is independent and community maintained. It does not imply any affiliation with OpenAI.

## Core Principles

The project is governed by ten principles:

- Customer before Product
- Evidence before Narrative
- Unknowns are Valuable
- Validation before Commitment
- Conversation before Presentation
- Trust before Persuasion
- Never Overpromise
- Prefer Asking over Assuming
- Separate Facts from Inferences
- If Uncertain, Say So

See [CONSTITUTION.md](CONSTITUTION.md) for the full constitution.

## Workflow

```text
Customer Context
↓
Evidence Inventory
↓
Unknown Detection
↓
Risk Review
↓
Commitment Boundaries
↓
Recommendation
↓
Optional Final Deliverables
```

The Skill always starts in review mode. Customer-facing material should be generated only after the review has identified evidence, unknowns, unsupported claims, risks, and commitment boundaries.

## Recommendation Statuses

Use only these recommendation statuses:

| Status | Meaning |
| --- | --- |
| Proceed | The demo appears safe to present based on the available evidence. |
| Proceed with Validation | The demo can move forward, but specific assumptions, missing evidence, or risky claims must be validated before or during the presentation. |
| Do Not Proceed | Critical gaps, unsupported claims, risky commitments, missing customer context, or weak evidence could create customer, commercial, legal, or technical risk. |

## Outputs

Demo Walkthrough Builder can produce:

- Review Summary
- Unsupported Claims
- Commitment Boundaries
- Recommendation
- Demo Walkthrough
- Presenter Guide
- Objection Guide
- Follow-up

## Installation as a Codex Skill

Copy this repository into your local Codex skills directory:

```bash
cp -R demo-walkthrough-builder <your-codex-skills-directory>/demo-walkthrough-builder
```

Then restart or refresh Codex so the Skill metadata can be discovered.

## Usage Examples

Try prompts like:

- "Review this demo walkthrough before I present it."
- "Find unsupported claims in these discovery notes."
- "Create a customer-safe demo strategy from this context."
- "Generate a presenter guide after reviewing the risks."
- "Tell me whether this demo is ready to present."

## Example

The [examples](examples/) folder contains fictional sample data for Northstar Support Desk. The sample shows messy discovery notes, possible demo scenes, unsupported claims, and a final safer walkthrough after review.

All example data is synthetic. Do not treat it as real customer information.

## Validation

Run the built-in validator:

```bash
python scripts/quick_validate.py
```

The script checks the repository structure, required files, templates, example files, core positioning, principles, and Skill presence.

## Contributing

Contributions are welcome. Keep the project conservative, evidence-first, and useful for real demo preparation.

Before opening a pull request:

- keep examples fictional
- do not include private customer data
- preserve evidence classification
- preserve commitment boundaries
- do not add unsupported product, customer, metric, security, compliance, roadmap, or ROI claims
- run `python scripts/quick_validate.py`

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT License. See [LICENSE](LICENSE).
