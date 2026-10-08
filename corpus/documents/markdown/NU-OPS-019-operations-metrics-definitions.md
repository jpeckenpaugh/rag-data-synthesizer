---
document_id: NU-OPS-019
title: Monthly Operations Metrics Definitions
document_type: reference
department: Quality and Continuity
site_scope: organization_wide
owner_role: Quality and Continuity Analyst
author: Niko Fen
author_employee_id: EMP-006
intended_audience: Operations-lead-eligible employees in NU-OPS-010 (EMP-001, EMP-003, EMP-005, EMP-006, EMP-007, EMP-008)
access_scope: operations_leads
status: draft
planned_status: current
date_status: proposed
version: 1.0
issued_date: 2024-09-30
effective_date: 2024-10-01
review_date: 2025-10-01
relationships:
  - type: references
    document_id: NU-OPS-012
    scope: Huddle follow-up context; notes may cite but do not amend these definitions
---

# Monthly Operations Metrics Definitions

**NU-OPS-019 · Draft for corpus review**  
Northstar Urgent Care Cooperative (NUCC) · Organization-wide  
Version 1.0 · Effective 2024-10-01 (proposed) · Access scope: `operations_leads`

> Fictional educational test material. The definitions and reporting rules below are proposed administrative conventions for this corpus. They are not clinical, financial, or professional quality measures.

## Purpose and reporting period

This reference proposes a consistent way to count selected administrative operations records across Harbor Point, Alder Creek, and Northgate. It defines measures only; it does not report actual monthly results. No source data or numerical totals are supplied in this document.

The proposed reporting period is a calendar month, based on the date the underlying event occurred. If that date is unknown, exclude the record from the monthly event count and list it separately as undated. A record entered late is assigned to the event month when that date is known; any late entry should be identified in the reporting notes.

All definitions, exclusions, submission rules, and review practices in this draft are pending approval by the Director of Operations. A later meeting record, including NU-OPS-012, may cite these definitions or record a proposed change, but does not amend them. A change requires an approved revision to this reference.

## Proposed measures

Count distinct administrative record IDs, not messages, updates, people, or estimated events. If one underlying event has separate records in different categories, it may appear in each applicable measure; the measures are independent and must not be added together as a total event count.

| Measure | Proposed definition | Include | Exclude |
| --- | --- | --- | --- |
| Facilities issue records | Number of distinct facilities issue records with an event date in the reporting month. | New administrative records for a facilities condition or repair request. Count one record once, even if it has multiple updates. | Duplicate entries for the same record; status updates without a new record; supply receiving discrepancies counted under the separate supply measure. |
| Supply receiving discrepancy records | Number of distinct administrative discrepancy records for a supply delivery received in the reporting month. | A record identifying a mismatch, damage, or other receiving discrepancy for a delivery. | Routine receipts with no discrepancy; repeated messages or updates for the same discrepancy record. |
| Service interruption records | Number of distinct administrative records for a service interruption that began in the reporting month. | A record that documents an interruption or degradation of an administrative or facility service. | Weather reports without a documented service interruption; repeated status updates for one interruption record. |
| Workplace incident reports | Number of distinct non-clinical workplace incident reports with an event date in the reporting month. | Administrative workplace incident reports and near-miss reports covered by NU-OPS-011. | Clinical events, patient-care records, duplicate reports of the same incident record, or reports with no established event date. |

These are record counts, not rates. No denominator, target, severity weighting, cause attribution, financial impact, or performance judgment is defined. A count must not be interpreted as evidence that one site is safer, more efficient, or better performing than another.

## Submission and review ownership

The following workflow is proposed and pending approval:

- **Site leads** check their site’s relevant administrative records and send a monthly count or an explicit “not available” status to the Quality and Continuity Analyst by the fifth business day of the following month.
- **Facilities Coordinator** confirms the facilities issue and supply receiving discrepancy counts from the designated administrative records.
- **Director of Operations** confirms the service interruption record list used for the monthly count.
- **Quality and Continuity Analyst** compiles the site and central submissions, checks for duplicate record IDs and missing site returns, and labels the summary as incomplete when a source or date is not confirmed.
- **Director of Operations** reviews and approves the definitions and any proposed revision. This draft does not establish an approval of actual numerical results or an external reporting requirement.

The corpus does not identify the software platform, underlying record repository, or a monthly results dataset. Do not infer that a measure has a value when no source records or approved summary are available.

## Known data limits

- No actual record-level source data or monthly totals are included in this corpus.
- A missing submission is not a zero count. Mark it missing or not available.
- Records may be late, duplicated, undated, or incomplete; report these limits rather than silently correcting or estimating values.
- These definitions do not establish a common incident-severity scale, a complete denominator, or a causal explanation for changes in counts.
- Different measure counts may concern the same underlying event and are not additive.
- NU-OPS-012 may refer to a measure by its defined name and record a follow-up, but meeting notes do not change the definition or fill in an unsupported numerical result.

## Access and revision record

This reference is labeled `operations_leads`. NU-OPS-010 defines the fictional eligibility mapping for this label; apply that scope together with this document’s organization-wide site scope. The label is a retrieval-test convention, not real authorization.

| Version | Issued | Effective | Change | Approval |
| --- | --- | --- | --- | --- |
| 1.0 | Proposed: 2024-09-30 | Proposed: 2024-10-01 | Initial proposed administrative measure definitions and reporting rules | Director of Operations (approval pending) |

**Next review:** proposed 2025-10-01.  
**Owner:** Quality and Continuity Analyst, Northstar Urgent Care Cooperative.

---

**Drafting basis:** Prepared for corpus plan `nucc-ops-v1` as a proposed reference for the October 2024 corpus snapshot. The measures, event-date assignment, inclusion/exclusion rules, fifth-business-day submission deadline, source-owner assignments, compilation checks, and approval flow are assumptions pending Director of Operations approval. No actual metric values, underlying records, reporting platform, or denominators are established. NU-OPS-012 may cite these definitions but cannot change them by itself. This Stage 2 draft is not an approved reporting standard.
