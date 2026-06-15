# Review Output: Northstar Support Desk

This output is based on fictional sample data from `examples/sample-input.md`. All customer information is synthetic.

## Review Summary

Northstar Support Desk appears to have a real operational problem: repeated customer complaints are scattered across support tickets, app reviews, survey comments, and CRM notes. The strongest demo path is to show how a support operations team can inspect feedback themes, review source comments, and create follow-up actions.

The current draft is directionally useful, but it includes unsupported claims about direct CRM connectivity, automatic classification coverage, time savings, implementation effort, and replacing weekly reporting. Those claims should not be presented as facts.

## Strengths

- Customer problem is clear enough to frame the demo around support-feedback overload.
- Audience is identified and includes both business and technical stakeholders.
- Textual screenshot descriptions provide visible evidence for dashboard, table, workflow, and filtering concepts.
- The proposed scenes follow a practical workflow from feedback review to action assignment.
- The demo can create a useful discovery conversation if it avoids overclaiming.

## Weaknesses

- No actual customer files are provided.
- CRM and ticketing systems are not named.
- No validated integration evidence is provided.
- No security or compliance requirements are documented.
- Reporting time savings are not supported by a baseline.
- Classification accuracy and coverage are unknown.

## Unsupported Claims

| Claim | Evidence Found | Classification | Risk | Suggested Rewrite | Validation Needed |
| --- | --- | --- | --- | --- | --- |
| "We can connect directly to their CRM." | Generic API support is mentioned, but the CRM is not named and no integration test is documented. | Needs Validation | Could create an integration commitment. | "We should validate your CRM and integration path before committing to direct connectivity." | Confirm CRM name, supported integration path, implementation owner, and test result. |
| "The dashboard will save the team 10 hours every week." | No reporting baseline or measured time study is provided. | Unknown | Creates unsupported ROI expectation. | "If your current reporting process is time-intensive, we can explore where this workflow may reduce manual effort." | Capture current reporting time and define measurement method. |
| "The system can automatically classify every complaint by product area." | Product has theme and sentiment screens, but classification coverage is not proven. | Needs Validation | Overstates automation and accuracy. | "The demo can show classification examples, then validate accuracy expectations with your team." | Test sample data and define acceptable accuracy threshold. |
| "Implementation is straightforward and should only take a few days." | No implementation scope, security review, data source details, or owner is provided. | Unknown | Creates timeline and delivery risk. | "Implementation timing depends on data access, security review, and integration scope." | Confirm data sources, access process, review requirements, and success criteria. |
| "This can replace their weekly reporting process." | Customer wants faster reporting, but replacement criteria are not defined. | Inferred | May imply a change-management commitment. | "This could support parts of the weekly reporting workflow; we should validate what must remain in the current process." | Map current reporting process and required outputs. |

## Unknowns

- Which CRM does Northstar use?
- Which ticketing system does Northstar use?
- What data can be exported for the demo?
- Who owns security approval?
- What data retention requirements apply?
- What reporting baseline exists today?
- What accuracy level would be trusted for classification?
- What does leadership need in the weekly summary?
- Who is the decision maker for the next step?

## Risks

- Integration risk: direct connectivity is not proven.
- Security risk: no security review or data-handling requirements are documented.
- Commercial risk: unsupported ROI may create unrealistic expectations.
- Technical risk: classification accuracy is unknown.
- Change-management risk: replacing weekly reporting may be more complex than the demo narrative suggests.

## Commitment Boundaries

### Safe to Say

- "Based on the sample workflow, we can show how support feedback could be reviewed by theme, source, severity, and owner."
- "The described screenshots show dashboard, table, filter, and workflow concepts."
- "CSV ingestion is supported based on the provided product notes."

### Unsafe to Say

- "We already connect directly to your CRM."
- "This will save 10 hours every week."
- "This will replace your weekly reporting process."
- "Implementation should only take a few days."
- "Every complaint will be classified automatically."

### Say Only with Validation

- "Direct CRM integration is available."
- "The workflow can use live ticketing data."
- "Classification accuracy is sufficient for leadership reporting."
- "The solution meets Northstar's security requirements."

### Avoid Saying

- "Guaranteed."
- "Automatic for everything."
- "No implementation work required."
- "Fully replaces your current process."

## Recommended Questions

- Which CRM and ticketing systems are in scope?
- Can the demo use a sanitized export instead of direct integration?
- What does the weekly leadership report include today?
- How much time does the team spend preparing weekly reporting?
- What accuracy threshold would make classification useful?
- Who needs to approve data access and security review?
- Which stakeholders should be able to assign or own follow-up actions?

## Recommendation

Status: Proceed with Validation

Reason: The demo can proceed if it is framed as a support-feedback review workflow using validated or clearly labeled sample data. Direct integration, ROI, automation coverage, implementation timeline, security readiness, and reporting replacement claims must be validated or removed from the presenter script.

Next action: Revise the demo narrative to focus on visible workflow value, use CSV or sample-data language, and validate the CRM, ticketing, security, accuracy, and reporting assumptions before the customer presentation.
