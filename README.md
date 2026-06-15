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
Company / Website / Files
          |
          v
Context Collection
          |
          v
Company Workspace
          |
          v
Evidence Inventory
          |
          v
Unknown Detection
          |
          v
Risk Review
          |
          v
Commitment Boundaries
          |
          v
Recommendation
          |
          v
Optional Final Deliverables
```

The Skill starts by collecting available company context, then moves into review mode. Customer-facing material should be generated only after the review has identified evidence, unknowns, unsupported claims, risks, and commitment boundaries.

## Company-first usage

Demo Walkthrough Builder can start from a company name, company website, attached company materials, or a mix of those inputs. When a website or company name is provided, the Skill collects available public context first. When files, screenshots, PDFs, Markdown notes, transcripts, README files, or other company-related materials are provided, the Skill inspects those first and treats them as stronger evidence than public search results.

Evidence priority:

1. User-provided files and notes
2. Official company website
3. Official public documentation
4. Public third-party information
5. Inferences

Try prompts like:

```text
Use Demo Walkthrough Builder for https://www.example.com
Use Demo Walkthrough Builder for ExampleCo.
Use Demo Walkthrough Builder using this attached PDF and the company website.
```

If search or browsing is not available, provide a website, document, notes, or screenshots so the Skill can build a Customer Context Inventory before reviewing demo readiness.

## Company Workspaces

Demo Walkthrough Builder can organize each company engagement into a separate workspace so context, evidence, review outputs, and final deliverables stay separated. This prevents materials from different companies or demos from being mixed together.

Company workspaces are file-system based and GitHub-friendly. They do not require a backend, database, or external dependencies, and they are designed to work locally with Codex.

Workspaces live under a top-level `workspaces/` folder. Each company gets a slug-based subfolder derived from the company name or domain.

Examples:

- `https://www.grupomarlan.com.br/` -> `workspaces/grupomarlan-com-br/`
- `Grupo Marlan` -> `workspaces/grupo-marlan/`
- `Acme Corp` -> `workspaces/acme-corp/`

```text
workspaces/
├── grupomarlan-com-br/
│   ├── inputs/
│   ├── research/
│   ├── evidence/
│   ├── outputs/
│   ├── notes/
│   └── workspace.md
└── acme-corp/
    ├── inputs/
    ├── research/
    ├── evidence/
    ├── outputs/
    ├── notes/
    └── workspace.md
```

Folder purposes:

- `inputs/`: User-provided materials, copied notes, uploaded file summaries, screenshot descriptions, discovery notes, raw prompts, and source references.
- `research/`: Public context gathered from official websites, public pages, search summaries, company descriptions, product or service summaries, and other public information.
- `evidence/`: Evidence inventories, source lists, claim mappings, unsupported claims, unknowns, and validation requirements.
- `outputs/`: Generated deliverables including review summary, recommendation, demo walkthrough, presenter guide, objection guide, and follow-up notes.
- `notes/`: Working notes, assumptions, open questions, next research steps, and future-run context.

Each company workspace includes `workspace.md`, an index that summarizes the company name, website, date created, input sources, public sources reviewed, user-provided materials, current recommendation, known unknowns, validation tasks, and latest generated outputs.

On each run, the Skill should identify the company or website, create or reuse the correct workspace, store raw inputs, research summaries, evidence analysis, generated outputs, working assumptions, and open questions in the appropriate folders, then update `workspace.md`.

When outputs are generated for a company workspace, use these numbered filenames:

```text
outputs/
├── 01-review-summary.md
├── 02-unsupported-claims.md
├── 03-commitment-boundaries.md
├── 04-recommendation.md
├── 05-demo-walkthrough.md
├── 06-presenter-guide.md
├── 07-objection-guide.md
└── 08-follow-up.md
```

Workspace rules:

- Never mix materials from different companies.
- Always create or reuse the correct company workspace before generating outputs.
- If the company workspace already exists, update it instead of creating a duplicate.
- If the company name is ambiguous, ask the user to confirm before creating the workspace.
- If only a URL is provided, derive the slug from the domain.
- If only a company name is provided, derive the slug from the normalized company name.
- Use lowercase slugs, replace spaces with hyphens, remove special characters, and for domains remove protocol and slashes.

## Review Gate

```text
                  +----------------------+
                  | Discovery Notes      |
                  | Demo Draft           |
                  | Product Context      |
                  +----------+-----------+
                             |
                             v
                  +----------------------+
                  | Review Mode          |
                  | - evidence check     |
                  | - unknown detection  |
                  | - claim review       |
                  | - risk review        |
                  +----------+-----------+
                             |
                             v
        +--------------------+--------------------+
        |                                         |
        v                                         v
+--------------------------+          +--------------------------+
| Safe / Supported Claims  |          | Unsupported / Risky      |
| can shape the demo       |          | claims need validation   |
+------------+-------------+          +------------+-------------+
             |                                     |
             +-------------------+-----------------+
                                 |
                                 v
                  +----------------------+
                  | Recommendation       |
                  | - Proceed            |
                  | - Proceed with       |
                  |   Validation         |
                  | - Do Not Proceed     |
                  +----------+-----------+
                             |
                             v
                  +----------------------+
                  | Generate final       |
                  | materials only after |
                  | the review gate      |
                  +----------------------+
```

## Evidence Review Model

```text
+----------------------+----------------------+----------------------+
| Claim Type           | Evidence Question    | Presenter Treatment  |
+----------------------+----------------------+----------------------+
| Verified             | Is it directly       | Safe to say with     |
|                      | supported?           | clear wording        |
+----------------------+----------------------+----------------------+
| Visible              | Is it shown in UI,   | Safe to show; avoid  |
|                      | screenshot, diagram? | wider claims         |
+----------------------+----------------------+----------------------+
| Inferred             | Is it reasonable but | Label as hypothesis  |
|                      | not proven?          | or ask a question    |
+----------------------+----------------------+----------------------+
| Placeholder          | Is it temporary?     | Replace before demo  |
+----------------------+----------------------+----------------------+
| Unknown              | Is information       | Do not present as    |
|                      | missing?             | fact                 |
+----------------------+----------------------+----------------------+
| Needs Validation     | Could it create a    | Validate before      |
|                      | commitment?          | presenting as fact   |
+----------------------+----------------------+----------------------+
```

## Recommendation Statuses

Use only these recommendation statuses:

| Status | Meaning |
| :--- | :--- |
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

- "Use Demo Walkthrough Builder for https://www.example.com"
- "Use Demo Walkthrough Builder for ExampleCo."
- "Use Demo Walkthrough Builder using this attached PDF and the company website."
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

## Support

If this project helps you prepare safer, more grounded customer demos, consider giving it a star on GitHub so more Solutions Engineers and Sales Engineers can discover it.

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

Copyright (c) 2026 Fabricio Artur.
