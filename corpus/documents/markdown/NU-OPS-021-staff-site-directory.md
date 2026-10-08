---
document_id: NU-OPS-021
title: Staff and Site Directory
document_type: reference_directory
department: People Operations
site_scope: organization_wide
owner_role: People Operations Coordinator
author: Ren Solis
author_employee_id: EMP-004
intended_audience: All staff
access_scope: all_staff
status: draft
planned_status: current
date_status: proposed
version: 1.0
issued_date: 2024-10-01
effective_date: 2024-10-01
review_date: 2025-10-01
relationships:
  - type: derived_from
    source_path: corpus/staff.yml
    scope: Employee ID, name, role, department, home_site, and responsibilities registry fields
  - type: references
    document_id: NU-OPS-007
    scope: Role-based operational routing; this directory does not replace it
---

# Staff and Site Directory

**Northstar Urgent Care Cooperative (NUCC)**

**Document ID:** NU-OPS-021 · **Status:** Draft (planned status: current) · **Version:** 1.0

**Proposed issue and effective date:** 1 October 2024, subject to approval · **Proposed review date:** 1 October 2025

**Scope:** Organization-wide · **Access label:** `all_staff`

> All names, roles, employee IDs, and organization details in this directory are fictional and created for an educational RAG test corpus. This is administrative reference material, not a clinical directory.

> **Draft notice:** This directory is proposed for review. The proposed effective date does not make it an approved or current directory. Use only after the required approval is recorded.

## How to read this directory

The entries below reproduce the employee ID, name, role, department, and `home_site` values in the fictional staff registry (`corpus/staff.yml`). The role-focus summaries are condensed from that registry's responsibility fields. A home-site value records the registry entry; it does not establish a person's current shift, physical presence, availability, reporting line, or site coverage.

This document does not provide contact information, backup assignments, an on-call roster, or approval authority. For operational routing, use the role-based destinations in NU-OPS-007 and the applicable procedure. Do not infer a route or substitute a person based on this list.

## Staff directory

| Portrait | Employee ID | Name | Role | Department | Home site (registry value) |
| --- | --- | --- | --- | --- | --- |
| ![Decorative fictional illustration, not a likeness](asset:avatar-emp-001) | EMP-001 | Mara Venn | Director of Operations | Central Operations | Central office (`central_office`) |
| ![Decorative fictional illustration, not a likeness](asset:avatar-emp-002) | EMP-002 | Ilan Rook | Facilities Coordinator | Facilities and Administration | Central office (`central_office`) |
| ![Decorative fictional illustration, not a likeness](asset:avatar-emp-003) | EMP-003 | Tessa Quill | Harbor Point Site Lead | Site Operations | Harbor Point (`harbor_point`) |
| ![Decorative fictional illustration, not a likeness](asset:avatar-emp-004) | EMP-004 | Ren Solis | People Operations Coordinator | People Operations | Central office (`central_office`) |
| ![Decorative fictional illustration, not a likeness](asset:avatar-emp-005) | EMP-005 | Dev Arlen | Records Coordinator | Records and Administration | Central office (`central_office`) |
| ![Decorative fictional illustration, not a likeness](asset:avatar-emp-006) | EMP-006 | Niko Fen | Quality and Continuity Analyst | Quality and Continuity | Central office (`central_office`) |
| ![Decorative fictional illustration, not a likeness](asset:avatar-emp-007) | EMP-007 | Oren Pike | Operations Desk Coordinator | Central Operations | Central office (`central_office`) |
| ![Decorative fictional illustration, not a likeness](asset:avatar-emp-008) | EMP-008 | Lio Marr | Northgate Site Lead | Site Operations | Northgate (`northgate`) |

## Role focus from the staff registry

The summaries below condense the responsibility fields in `corpus/staff.yml`. They describe registry-listed topics; they do not define approval authority, access eligibility, current assignments, site coverage, or on-call responsibility.

- **EMP-001 — Mara Venn:** Organization-wide operational governance and approvals; service continuity coordination; controlled document policy ownership.
- **EMP-002 — Ilan Rook:** Facilities issue intake and routing; non-clinical supplies and receiving; vendor visit coordination; maintaining historical facilities procedure records.
- **EMP-003 — Tessa Quill:** Harbor Point opening and closing handoffs; local site coordination and exception records; facilitating site quality huddles.
- **EMP-004 — Ren Solis:** Administrative schedule-change process; staff-facing notices and revision history for that process.
- **EMP-005 — Dev Arlen:** Administrative records routing and misdelivery reporting; maintaining the fictional information access matrix for the corpus.
- **EMP-006 — Niko Fen:** Non-clinical incident reporting guidance; severe-weather coordination materials; operations metrics definitions and reporting notes.
- **EMP-007 — Oren Pike:** Maintaining role-based site contact and escalation routing; recording unresolved operations desk questions and follow-ups.
- **EMP-008 — Lio Marr:** Northgate site operations and receiving handoffs; maintaining records for time-limited local exceptions.

Portraits are decorative fictional illustrations assigned to employee IDs for this test corpus. They are not photographs or likenesses of real people and do not encode or establish a person's identity, age, appearance, role, or personality. The text fields in each row provide the directory information.

## Registry snapshot by home site

The staff registry contains eight employee entries: six with `central_office` as `home_site`, one with `harbor_point`, and one with `northgate`. These are counts of registry entries grouped by the recorded home-site field only. They are not headcounts of people assigned to work at each site, staffing levels, shift coverage, or current attendance.

| Registry `home_site` value | Entries in staff registry |
| --- | ---: |
| `central_office` | 6 |
| `harbor_point` | 1 |
| `northgate` | 1 |
| `alder_creek` | 0 |

![Chart of registry entries grouped by recorded home_site; these counts do not represent staffing coverage](asset:staff-home-site-count)

**Chart caption:** Registry entries by recorded `home_site`. This graphic summarizes the table above and does not represent actual staffing coverage. The table and prose remain authoritative.

## Site-role note

The staff registry names Tessa Quill as Harbor Point Site Lead and Lio Marr as Northgate Site Lead. It contains no employee whose role is Alder Creek Site Lead and no employee with `alder_creek` as `home_site`. This means the registry does not identify a named Alder Creek incumbent; it does not establish whether the role is vacant, covered by an unlisted person, or assigned temporarily. NU-OPS-007 lists role-based routing separately and should be consulted for routing details.

## Updates and limits

This directory reflects the staff registry used for the proposed 1 October 2024 corpus snapshot. The registry is the source for these identity and home-site fields. A proposed correction should be made to the registry first and then reconciled here; this draft does not independently establish a personnel change.

This document does not define employment status, schedule, reporting lines, backup coverage, contact routes, or responsibilities beyond the role-focus summary sourced from the registry. For role routing, consult NU-OPS-007. For corpus access labels, consult NU-OPS-010.

---

**Drafting basis:** Drafted by Ren Solis (EMP-004), People Operations Coordinator, solely from the fictional employee ID, name, role, department, `home_site`, and responsibilities fields in `corpus/staff.yml`. The 1 October 2024 dates are proposed scenario metadata consistent with the planned corpus snapshot and require coordinator confirmation. The home-site counts are simple counts of those registry values, not a separate staffing dataset. No contact details, reporting lines, shift information, employment status, or other personnel facts were inferred. The portrait illustrations are decorative visual identifiers, not likenesses; the chart visualizes only the adjacent registry count table.
