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
status: current
date_status: approved
version: 1.0
issued_date: 2024-09-30
effective_date: 2024-10-01
review_date: 2025-10-01
approval_date: 2024-09-30
approved_by: Director of Operations
relationships:
  - type: references
    document_id: NU-OPS-012
    scope: Huddle follow-up context; notes may cite but do not amend these definitions
---

# Monthly Operations Metrics Definitions

**NU-OPS-019 · Current**\
Northstar Urgent Care Cooperative (NUCC) · Organization-wide  
Version 1.0 · Effective 2024-10-01 · Access scope: `operations_leads`

> Fictional educational test material. The definitions and reporting rules below are administrative conventions for this corpus. They are not clinical, financial, or professional quality measures.

## Purpose and reporting period

This reference defines a consistent way to count selected administrative operations records across Harbor Point, Alder Creek, and Northgate. It defines measures only; it does not report actual monthly results. No source data or numerical totals are supplied in this document.

The reporting period is a calendar month, based on the date the underlying event occurred. If that date is unknown, exclude the record from the monthly event count and list it separately as undated. A record entered late is assigned to the event month when that date is known; any late entry should be identified in the reporting notes.

These definitions, exclusions, submission rules, and review practices are in effect for the corpus as of 1 October 2024. A later meeting record, including NU-OPS-012, may cite these definitions or record a proposed change, but does not amend them. A change requires an approved revision to this reference.

## Measures

Count distinct administrative record IDs, not messages, updates, people, or estimated events. If one underlying event has separate records in different categories, it may appear in each applicable measure; the measures are independent and must not be added together as a total event count.

| Measure | Definition | Include | Exclude |
| --- | --- | --- | --- |
| Facilities issue records | Number of distinct facilities issue records with an event date in the reporting month. | New administrative records for a facilities condition or repair request. Count one record once, even if it has multiple updates. | Duplicate entries for the same record; status updates without a new record; supply receiving discrepancies counted under the separate supply measure. |
| Supply receiving discrepancy records | Number of distinct administrative discrepancy records for a supply delivery received in the reporting month. | A record identifying a mismatch, damage, or other receiving discrepancy for a delivery. | Routine receipts with no discrepancy; repeated messages or updates for the same discrepancy record. |
| Service interruption records | Number of distinct administrative records for a service interruption that began in the reporting month. | A record that documents an interruption or degradation of an administrative or facility service. | Weather reports without a documented service interruption; repeated status updates for one interruption record. |
| Workplace incident reports | Number of distinct non-clinical workplace incident reports with an event date in the reporting month. | Administrative workplace incident reports and near-miss reports covered by NU-OPS-011. | Clinical events, patient-care records, duplicate reports of the same incident record, or reports with no established event date. |

These are record counts, not rates. No denominator, target, severity weighting, cause attribution, financial impact, or performance judgment is defined. A count must not be interpreted as evidence that one site is safer, more efficient, or better performing than another.

## Submission and review ownership

The approved reporting workflow is:

- **Site leads** submit site-level counts with the supporting record IDs, or an explicit “not available” status, to the Quality and Continuity Analyst by the fifth business day of the following month.
- **Facilities Coordinator** validates the record IDs and eligibility of facilities issue and supply receiving discrepancy entries against available records. This role validates individual record inclusion; it does not re-create or independently confirm duplicate aggregate counts.
- **Director of Operations** confirms the service interruption record list used for the monthly count.
- **Quality and Continuity Analyst** deduplicates the submitted record IDs and compiles the site and central inputs. The Analyst flags missing site returns and marks a summary incomplete when a source, date, or item is not confirmed.
- **Director of Operations** reviews and approves definitions and proposed revisions. This reference does not establish approval of actual numerical results or an external reporting requirement.

Site leads provide site-level counts and supporting record IDs. The Facilities Coordinator validates eligibility for the facilities and supply measures, and the Director of Operations confirms the service interruption record list. The Quality and Continuity Analyst deduplicates and compiles submissions. These assigned steps do not identify a software platform or a single underlying record repository.

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
| 1.0 | 2024-09-30 | 2024-10-01 | Initial administrative measure definitions and reporting rules | Approved — Director of Operations |

**Next review:** 2025-10-01.\
**Owner:** Quality and Continuity Analyst, Northstar Urgent Care Cooperative.
