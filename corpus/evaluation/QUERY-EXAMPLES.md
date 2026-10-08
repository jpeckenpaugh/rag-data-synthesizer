# Proposed RAG Query Examples

**Status:** Proposed starter examples, checked against the approved Northstar corpus.  
**PDF snapshot checked:** 2024-10-08 render of the fictional 2024-10-01 corpus snapshot (21 PDFs, 64 pages).  
**Ingestion boundary:** Evaluation material. Do not ingest this file with `corpus/documents/pdf/`.

The first ten queries have answers supported by one or more PDFs. The final five are negative examples: one out-of-domain request and four questions the corpus does not answer. Evidence links identify the relevant PDF page; excerpts are short locators to the supporting text. If a source Markdown file changes and PDFs are rerendered, recheck the cited page numbers and evidence before using these as an evaluation set.

## Answerable queries

### Q-001 — Opening handoff record

**Query:** What information should I record for a routine site opening handoff?

**Expected response:** Record the date, site, scheduled handoff time, and completing role in the site's opening record. Use role labels rather than personal contact details in shared notes.

**Evidence:** [NU-OPS-002.pdf, p. 2](../documents/pdf/NU-OPS-002.pdf#page=2) — “Record the date, site, scheduled opening handoff time, and completing role.”

### Q-002 — Scheduled Harbor Point exception

**Query:** During the approved October after-hours window, what task may the Harbor Point Site Lead perform, and when?

**Expected response:** The Harbor Point Site Lead may inventory and relabel shelves in the designated non-clinical administrative supply storage area, Monday through Friday, October 7–11, 2024, from 18:00 to 19:30 local site time. The exception is approved but was scheduled to become effective October 7, so it was not active at the October 1 corpus snapshot.

**Evidence:** [NU-OPS-004.pdf, p. 1](../documents/pdf/NU-OPS-004.pdf#page=1) — “Inventory and relabel shelves”; “2024-10-07 through 2024-10-11”; “18:00 to 19:30 local site time.”

### Q-003 — Current facilities procedure

**Query:** Which facilities issue routing procedure is current as of October 1, 2024, and what is the status of the prior edition?

**Expected response:** NU-OPS-003, version 2.0, is current and effective September 21, 2024. It supersedes NU-OPS-016 for facilities issue intake, routing, escalation, and follow-up. NU-OPS-016 is retained as a superseded historical copy.

**Evidence:** [NU-OPS-003.pdf, p. 1](../documents/pdf/NU-OPS-003.pdf#page=1) — “effective 21 September 2024, this procedure supersedes NU-OPS-016”; [NU-OPS-016.pdf, p. 1](../documents/pdf/NU-OPS-016.pdf#page=1) — “Superseded historical copy.”

### Q-004 — Schedule request approval

**Query:** Does submitting a schedule-change request—or getting no objection—mean the change is approved?

**Expected response:** No. A schedule change requires an explicit decision attributable to the applicable approver role. A request, copied email, draft calendar entry, or silence is not approval. The request remains pending until an explicit decision is recorded.

**Evidence:** [NU-OPS-005.pdf, p. 2](../documents/pdf/NU-OPS-005.pdf#page=2) — “A submitted request, a copied email, a draft calendar entry, or silence does not constitute approval.”

### Q-005 — General service interruption updates

**Query:** How often should the update owner report during an active service interruption, and what is the rule for severe-weather updates?

**Expected response:** For a general service interruption, provide an update every 60 minutes while the interruption remains active, and sooner if there is a material status change. Severe-weather site updates follow NU-OPS-013's material-change and shift-handoff convention; NU-OPS-013 sets no fixed timed cadence.

**Evidence:** [NU-OPS-006.pdf, p. 2](../documents/pdf/NU-OPS-006.pdf#page=2) — “every 60 minutes, and sooner when a material status change occurs”; [NU-OPS-013.pdf, p. 2](../documents/pdf/NU-OPS-013.pdf#page=2) — next update is triggered by “material change or shift handoff.”

### Q-006 — `operations_leads` eligibility

**Query:** Which employee IDs are eligible for documents labeled `operations_leads`?

**Expected response:** EMP-001, EMP-003, EMP-005, EMP-006, EMP-007, and EMP-008. Eligibility is the explicit set for that label; the document does not imply inheritance from another access label.

**Evidence:** [NU-OPS-010.pdf, p. 2](../documents/pdf/NU-OPS-010.pdf#page=2) — the `operations_leads` row lists “EMP-001, EMP-003, EMP-005, EMP-006, EMP-007, EMP-008.”

### Q-007 — Unclear or out-of-scope record destination

**Query:** If a misdelivered record's destination is unclear or it appears to contain material outside the procedure's scope, what should staff do?

**Expected response:** Do not forward it broadly. Contact the Records Coordinator for direction. The procedure also states that the directory supplies destinations but does not independently grant access to a record.

**Evidence:** [NU-OPS-009.pdf, p. 2](../documents/pdf/NU-OPS-009.pdf#page=2) — “do not forward it broadly; contact the Records Coordinator for direction.”

### Q-008 — Severe-weather status update fields

**Query:** What should the basis field in a severe-weather site update contain, and what should the next-update field avoid?

**Expected response:** The basis should say what was directly confirmed, by which role or source, and when; distinguish direct confirmation from reports. The next-update field should identify the next trigger, such as a material change or shift handoff, and must not predict a restoration or reopening time.

**Evidence:** [NU-OPS-013.pdf, p. 2](../documents/pdf/NU-OPS-013.pdf#page=2) — “What was directly confirmed, by which role/source, and when”; “do not enter a predicted restoration or reopening time.”

### Q-009 — Vendor sign-out

**Query:** What should the site host record before a vendor leaves?

**Expected response:** Record the departure time, work-order or facilities issue reference, reported work status, whether the work area was returned or left awaiting follow-up, and any scope difference or discrepancy plus the role notified.

**Evidence:** [NU-OPS-014.pdf, p. 3](../documents/pdf/NU-OPS-014.pdf#page=3) — “Before the visitor leaves, the site host role records” the departure time, reference, work status, work-area disposition, and scope differences or discrepancies.

### Q-010 — Monthly site submissions

**Query:** What must site leads submit for monthly operations metrics, and by when?

**Expected response:** Site leads submit site-level counts with supporting record IDs, or explicitly mark the submission “not available,” to the Quality and Continuity Analyst by the fifth business day of the following month.

**Evidence:** [NU-OPS-019.pdf, p. 2](../documents/pdf/NU-OPS-019.pdf#page=2) — “site-level counts with the supporting record IDs, or an explicit ‘not available’ status” by “the fifth business day of the following month.”

## Negative examples

For these examples, the expected behavior is to abstain from supplying an unsupported substantive answer. A system may briefly identify the scope limit or missing fact. For the two out-of-domain examples, a scope notice can be cited to explain the abstention, but it is not evidence for the requested medical or insurance answer.

### Q-011 — Out of domain: medication advice

**Query:** What dose of ibuprofen should a patient take for an ankle injury?

**Expected behavior:** Abstain. The corpus contains non-clinical administrative material and provides no diagnosis or medication advice. Do not recommend a dose.

**Scope evidence:** [NU-OPS-011.pdf, p. 1](../documents/pdf/NU-OPS-011.pdf#page=1) states that the guide is not clinical advice. No PDF page supports a medication dose.

### Q-012 — Out of domain: insurance coverage

**Query:** Does Northstar accept my insurance plan, and what would my copay be?

**Expected behavior:** Abstain. Insurance acceptance and patient billing are not covered by this operations corpus. Do not infer coverage or quote a copay.

**Evidence:** No supporting source or PDF page. The corpus contains no insurance-acceptance or patient-billing information.

### Q-013 — Not established: Friday office closing time

**Query:** What time does the office close on Fridays?

**Expected behavior:** State that the corpus does not establish regular office closing hours. Do not infer hours from the separately scoped after-hours exceptions.

**Evidence:** No supporting source or PDF page defines regular Friday office hours. [NU-OPS-004.pdf, p. 1](../documents/pdf/NU-OPS-004.pdf#page=1) describes only a scheduled Harbor Point administrative task window, not normal office hours.

### Q-014 — Unresolved: vendor-record retention

**Query:** How long must a site keep vendor visit and sign-in records?

**Expected behavior:** State that no retention period is established in the corpus. Do not borrow a retention period from another record type.

**Evidence:** [NU-OPS-020.pdf, p. 2](../documents/pdf/NU-OPS-020.pdf#page=2) marks the vendor visit-log retention period “Open — no answer established.”

### Q-015 — Unresolved: Alder Creek backup

**Query:** Who is the designated backup for the Alder Creek Site Lead?

**Expected behavior:** State that the corpus does not establish a named backup or deputy. Do not infer coverage from the role mailbox.

**Evidence:** [NU-OPS-020.pdf, p. 1](../documents/pdf/NU-OPS-020.pdf#page=1) records the backup question as open; [NU-OPS-007.pdf, p. 2](../documents/pdf/NU-OPS-007.pdf#page=2) says the role mailbox does not establish backup coverage.
