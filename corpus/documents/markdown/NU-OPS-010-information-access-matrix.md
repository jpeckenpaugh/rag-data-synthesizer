---
document_id: NU-OPS-010
title: Internal Information Access Matrix
document_type: access_matrix
department: Records and Administration
site_scope: organization_wide
owner_role: Records Coordinator
author: Dev Arlen
author_employee_id: EMP-005
intended_audience: All staff; operations leads; RAG integration evaluators
access_scope: all_staff
status: draft
planned_status: current
version: 1.0
issued_date: 2023-12-18
effective_date: 2024-01-01
review_date: 2025-01-01
date_status: proposed
relationships:
  - type: governs_access_for
    document_id: all_documents
    scope: Test labels and expected filtering behavior
---

# Internal Information Access Matrix

**Northstar Urgent Care Cooperative (NUCC)**  
**Document ID:** NU-OPS-010 · **Status:** Draft (planned status: current) · **Version:** 1.0  
**Proposed effective date:** 2024-01-01 · **Owner:** Records Coordinator  
**Corpus access scope:** `all_staff`

**Fictional corpus snapshot:** 2024-10-01

> Fiction notice: NUCC, its employees, and the conventions in this document are invented for an educational RAG test corpus. This matrix is a test fixture, not a real security policy or a guide to handling actual records.

## Purpose and limits

This reference defines the three access-scope labels used in the NUCC corpus and the fictional role groups that may retrieve documents carrying each label. The labels support access-filter tests in a retrieval system. They do not establish identity, authenticate a user, grant access to any real system, or describe legal or clinical permissions.

Apply the scope attached to an individual document as a retrieval filter. A role’s eligibility for one scope does not imply eligibility for every document, record, or system in an actual organization. Site scope is a separate metadata filter: access to `site_operations` does not make a Harbor Point-only document relevant to Northgate.

## Fictional role groups

For this corpus only, use these role groups:

- **All staff:** fictional employees assigned to any NUCC site or central office, regardless of department.
- **Site operations:** all staff, site leads, and central staff assigned an operational support role for site procedures. The group is intended for routine site-level operational material.
- **Operations leads:** the Director of Operations, site leads, and explicitly assigned central operations owners. This group is intended for documents whose audience is limited to coordination or oversight roles.

These groups are not a personnel directory. A document’s audience may be narrower than its scope. The employee IDs below are explicit corpus-only eligibility assignments based on the fictional staff registry; they are not real security rules and do not establish authorization in any actual organization.

## Access-scope definitions and role mapping

| Scope label | Eligible fictional employee IDs | Typical document class |
| --- | --- | --- |
| `all_staff` | EMP-001, EMP-002, EMP-003, EMP-004, EMP-005, EMP-006, EMP-007, EMP-008 | NU-OPS-001, NU-OPS-005, NU-OPS-010, NU-OPS-015, NU-OPS-017, and NU-OPS-021 |
| `site_operations` | EMP-001, EMP-002, EMP-003, EMP-006, EMP-007, EMP-008 | NU-OPS-002, NU-OPS-003, NU-OPS-006, NU-OPS-007, NU-OPS-008, NU-OPS-011, NU-OPS-013, NU-OPS-014, and NU-OPS-016 |
| `operations_leads` | EMP-001, EMP-003, EMP-005, EMP-006, EMP-007, EMP-008 | NU-OPS-004, NU-OPS-009, NU-OPS-012, NU-OPS-018, NU-OPS-019, and NU-OPS-020 |

Each row is the explicit set eligible for documents carrying that exact label; there is no implicit inheritance between labels. Employees appearing in multiple rows are eligible for each of those labels: EMP-001, EMP-003, EMP-006, EMP-007, and EMP-008 appear in all three rows; EMP-002 appears in `all_staff` and `site_operations`; EMP-005 appears in `all_staff` and `operations_leads`; EMP-004 appears only in `all_staff`. These labels are exact strings. Do not infer a fourth scope or silently translate a missing label. This employee mapping exists solely for deterministic tests of this fictional corpus.

## Document-class mapping

Use the document’s front matter or manifest value as the source of its scope. The following are examples to make the mapping concrete; they do not replace per-document metadata:

| Scope | Examples in this corpus |
| --- | --- |
| `all_staff` | NU-OPS-001 Operations Governance and Document Control; NU-OPS-005 Staff Schedule Change Notice; NU-OPS-010 Internal Information Access Matrix; NU-OPS-015 Document Revision Bulletin 24-03; NU-OPS-017 Staff Schedule Change Notice, Prior Edition; NU-OPS-021 Staff and Site Directory |
| `site_operations` | NU-OPS-002 Site Opening and Closing Checklist; NU-OPS-003 Facilities Issue Intake and Escalation; NU-OPS-006 Service Interruption Response; NU-OPS-007 Site Contact and Escalation Directory; NU-OPS-008 Supply Request and Receiving Guide; NU-OPS-011 Workplace Incident Reporting Guide; NU-OPS-013 Severe Weather Site Coordination Card; NU-OPS-014 Vendor Visit and Contractor Sign-In; NU-OPS-016 Facilities Issue Routing, Revision 1 |
| `operations_leads` | NU-OPS-004 Harbor Point After-Hours Access Exception; NU-OPS-009 Records Handling and Misdelivery Procedure; NU-OPS-012 Quality Huddle Notes, September; NU-OPS-018 Northgate Supply Receiving Exception; NU-OPS-019 Monthly Operations Metrics Definitions; NU-OPS-020 Unresolved Service Desk Questions Log |

This list is an initial fixture mapping based on the corpus plan. If an individual document’s metadata differs, treat the matrix and that document as inconsistent and route the discrepancy to the corpus coordinator; do not guess which value was intended.

## Site-specific visibility

Apply both the access scope and `site_scope` metadata. A user may be eligible for a scope while a site-specific document remains outside the requested site filter. For example, an `operations_leads` document scoped to `northgate` should not be returned for a Harbor Point-only query unless the query explicitly asks for cross-site material and the caller is eligible.

Organization-wide documents may be considered for any site when their content applies across the network. This does not broaden the access scope of a document with a narrower label.

## Handling ambiguous authorization

When a retrieval request does not provide a caller role or authorization context, do not assume that the caller belongs to the broadest group. For a corpus test, either:

1. Ask for the required role or scope context before retrieving scope-limited material; or
2. Restrict retrieval to `all_staff` material if the integration is configured to use that safe default, and state that no authorization context was provided.

If the role is unknown, the requested scope is missing or unrecognized, or metadata conflicts, do not return the potentially restricted result. Ask for clarification or report that the corpus does not establish eligibility. Do not infer role membership from a person’s name, site, question wording, or the fact that a document appears in search results.

This behavior is for testing retrieval logic only. It is not a substitute for an access-control system or an authorization decision.

## Review owner and revision record

The fictional Records Coordinator maintains this matrix for the corpus. Report a mismatch between this reference and document metadata to the primary-agent coordinating the corpus; until resolved, use the narrower applicable filter and mark the result for review.

| Version | Proposed issued | Proposed effective | Change |
| --- | --- | --- | --- |
| 1.0 | Proposed: 2023-12-18 | Proposed: 2024-01-01 | Initial corpus scope labels, role mapping, and unknown-authorization handling. |

**Proposed fixture dates:** issued 2023-12-18; effective 2024-01-01; next review 2025-01-01. Its planned status is current, but it is a draft and is not operative until approval is recorded. If approved on the proposed dates, it would take effect before NU-OPS-001's proposed 2024-01-15 effective date and would be current at the 2024-10-01 corpus snapshot.  
**Related corpus document:** NU-OPS-007 Site Contact and Escalation Directory defines fictional role-based routing; it does not establish authorization beyond the scope metadata described here.
