# Final Walkthrough: Northstar Support Desk

This walkthrough is based on fictional sample data and the review output in this repository. Northstar Support Desk is a synthetic example. Claims marked Needs Validation should not be presented as confirmed facts.

## Demo Objective

Show how a support operations team could review customer-feedback themes, inspect source comments, prioritize high-severity issues, and assign follow-up actions using validated sample or exported data.

## Evidence Classifications

| Item | Classification | Notes |
| --- | --- | --- |
| Customer problem around repeated complaints | Verified | Supported by the provided discovery notes. |
| Dashboard, table, filter, and workflow screens | Visible | Supported by textual screenshot descriptions only. |
| CSV ingestion | Verified | Supported by the provided product notes. |
| Direct CRM integration | Needs Validation | CRM name and integration proof are missing. |
| Time savings | Unknown | No baseline or measurement is provided. |
| Automatic product-area classification for every complaint | Needs Validation | Classification coverage and accuracy are not proven. |
| Security readiness for Northstar | Unknown | No security requirements or review status are provided. |

## Scene-by-Scene Walkthrough

| Scene | What to Show | What to Say | Evidence Status | Validation Notes |
| --- | --- | --- | --- | --- |
| 1. Start with the support-feedback problem | Open with the high-level dashboard showing top themes. | "Based on the discovery notes, the team is trying to understand repeated complaints across multiple feedback sources." | Verified / Visible | Keep the language tied to the provided notes. |
| 2. Filter to high-severity themes | Use the filter panel for source type, date range, theme, and severity. | "I will use severity and source filters to narrow the conversation to the issues that may need the fastest operational response." | Visible | Do not claim live customer data unless validated. |
| 3. Inspect source comments | Show the comments table with source, date, theme, and severity. | "This view keeps the summary connected to the underlying comments, so the team can inspect examples instead of only looking at a chart." | Visible | If real data is unavailable, label it as sample data. |
| 4. Assign follow-up action | Show the workflow screen with owner and due date. | "For a theme that needs action, the team can assign an owner and due date so the insight becomes a follow-up task." | Visible | Avoid implying integration into the customer's existing task system unless validated. |
| 5. Prepare leadership summary | Show a draft weekly summary based on selected themes and actions. | "This could support the weekly leadership reporting process. Before treating it as a replacement, we would map the current report and required approvals." | Inferred / Needs Validation | Validate current reporting requirements and baseline effort. |

## Presenter Guide

### Opening

"The goal today is not to claim that every integration or reporting outcome is already solved. The goal is to review a safer workflow for turning support feedback into themes, examples, and follow-up actions, then identify what we need to validate for Northstar."

### Scene Transitions

- From problem to dashboard: "Let's start with the repeated-complaint problem described in discovery."
- From dashboard to comments: "A theme is only useful if the team can inspect the underlying evidence."
- From comments to workflow: "Once the issue is understood, the next question is who owns the follow-up."
- From workflow to summary: "Finally, let's look at how this could support weekly reporting, while separating what is proven from what still needs validation."

### Pause Points

- "Does this match how your team reviews feedback today?"
- "Which source would be most important to validate first?"
- "Would this severity model reflect how your leadership prioritizes issues?"
- "What needs to be true before this can support weekly reporting?"

### Questions to Ask

- "Which CRM and ticketing systems should we validate?"
- "Can we start with a sanitized export for the first proof point?"
- "What fields are required in the weekly leadership summary?"
- "What level of classification accuracy would your team trust?"
- "Who should approve data access and security requirements?"

### What to Avoid Saying

- "We already connect directly to your CRM."
- "This will save 10 hours per week."
- "This replaces your reporting process."
- "Implementation only takes a few days."
- "Every complaint is automatically classified correctly."

### Fallback Language

- "I would treat that as a validation item before we commit to it."
- "Based on what we have reviewed so far, the safer path is to start with exported or sample data."
- "That is a reasonable hypothesis, but I do not want to present it as confirmed without evidence."
- "Let's separate the workflow we can demonstrate from the integration path we still need to validate."

### Closing

"The main takeaway is that Northstar may have a strong workflow opportunity here, but the next step is validation: confirm the systems, data fields, security requirements, classification expectations, and reporting output before making commitments."

## Objection Guide

| Likely Objection | Risk Behind the Objection | Suggested Response | Evidence Required | Follow-up Action |
| --- | --- | --- | --- | --- |
| "Can this connect directly to our CRM?" | Direct integration is not validated. | "We should validate your CRM and the supported integration path before committing to direct connectivity. For the demo, we can safely use exported or sample data." | CRM name, integration docs, test result. | Schedule technical validation with IT Systems Lead. |
| "Will this replace our weekly report?" | Replacement criteria are unknown. | "It may support parts of the reporting workflow. I would first map the current report, required fields, and approval process." | Current report template and owner requirements. | Collect current weekly reporting artifacts. |
| "How accurate is the classification?" | Classification accuracy is not proven on customer data. | "The right validation is to test a representative sample and compare results against your team's expected labels." | Sample dataset and scoring criteria. | Run a validation pass on sanitized data. |
| "How quickly can we implement?" | Timeline depends on scope and approvals. | "Timing depends on data access, security review, source systems, and success criteria. I would not estimate until those are clear." | Scope, owners, access path, review requirements. | Define implementation assumptions and blockers. |

## Follow-up

### Summary

The demo should proceed as a validated workflow conversation, not as a commitment to live integrations, guaranteed savings, automatic classification coverage, or reporting replacement.

### Open Questions

- Which CRM and ticketing systems are in scope?
- Can Northstar provide a sanitized export?
- What security requirements apply?
- What does the weekly leadership report require?
- What accuracy threshold is acceptable?

### Validation Tasks

- Confirm CRM and ticketing system names.
- Validate CSV export fields.
- Review security and data-handling requirements.
- Test classification on a representative sample.
- Map the current weekly reporting process.

### Assets Needed

- Sanitized support ticket export.
- App review sample.
- Survey comment sample.
- Current leadership report example.
- System list and integration requirements.

### Next Steps

- Schedule a technical validation session.
- Replace sample-data screenshots with validated demo data if approved.
- Update the walkthrough after integration and security assumptions are confirmed.

### Owner

- Placeholder: assign customer-facing technical owner.

### Due Date

- Placeholder: set after the validation session is scheduled.
