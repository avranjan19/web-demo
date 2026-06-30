---
source_url: unknown-source
query: CERT-In directions 2025 breach notification 6 hours India
scraped_at: 2026-06-30T17:02:38.548242+00:00
---

CERT-In Directions Compliance Guide (2025): 6-Hour Reporting, 180-Day Logs, VPN/Cloud KYC

*   [info@amlegals.com](mailto:info@amlegals.com)
*   [+91-8448548549](tel:++91-8448548549)
*   9:30AM - 06:00 PM

[Get in Touch](https://amlegals.com/get-in-touch/)

[![](https://amlegals.com/wp-content/uploads/2025/08/MAIN-AMLEGALS-LOGO-2.png)](https://amlegals.com/)

[![](https://amlegals.com/wp-content/uploads/2025/08/MAIN-AMLEGALS-LOGO-2.png)](https://amlegals.com/)

# CERT-In Directions Compliance in 2025: A Practical Counsel’s Guide

[](https://amlegals.com "Go to .") > CERT-In Directions Compliance in 2025: A Practical Counsel’s Guide

### CERT-In Directions Compliance in 2025: A Practical Counsel’s Guide

India’s cybersecurity regime under Section 70B of the Information Technology Act has matured into a clear, enforceable framework. The CERT-In Directions require 6-hour cyber incident reporting, 180-day retention of security logs in India, synchronization of system clocks with trusted NTP sources, and robust subscriber/customer information retention by VPN, cloud, hosting, and allied service providers. These obligations apply broadly to Indian entities and foreign businesses serving the Indian market. Penalties for non-compliance can be significant.

This note sets out, in practical terms, how to operationalize compliance without disrupting business: who is in scope, what must be reported and when, how to structure log retention and time synchronization, how to align contracts and vendors, and how to implement a 90‑day compliance program that stands up to regulatory scrutiny.

#### Applicability: Who Should Prepare

The Directions are drafted with wide reach. Intermediaries, body corporates, data centers, VPS, cloud and VPN providers, and virtual asset service providers fall squarely within scope. Government bodies and critical infrastructure players are explicitly covered. Foreign providers that offer services into India or process Indian user or system data should assume applicability and take advice. If your networks, applications, or security operations touch Indian traffic, compliance preparation is prudent.

#### What Is Reportable

Reportable incidents include unauthorized access, compromise of critical systems, malware and ransomware, DDoS/DoS events, identity theft and spoofing, exfiltration or leaks of data, attacks on web, API and database layers, supply-chain compromises, and attacks on OT/ICS where applicable. From a counsel’s perspective, materiality is key: if the incident affects availability, integrity, or confidentiality in a way that could be reasonably significant—or if it would concern a regulator, sector supervisor, or major customer—treat it as reportable and proceed accordingly.

#### The Six-Hour Rule: How to Comply Without Guesswork

The six-hour clock starts when the organization notices or is brought to notice of a qualifying incident. “Noticing” is not limited to the CISO’s desk; an MSSP alert, a P1 SOC ticket, or a credible third‑party disclosure can suffice. An initial notification should be timely, factual, and proportionate; it can be supplemented as investigations progress.

A sound first notice typically addresses:

*   Your legal entity, sector, and a 24×7 primary and alternate contact.
*   The incident category and the detection timestamp (with time zone).
*   Affected systems and business processes; whether cloud or on‑prem.
*   Indicators known at the time (hashes, IPs, domains, TTPs).
*   Steps taken for containment and eradication.
*   Preliminary impact on availability, integrity, confidentiality, and personal data.
*   Whether other authorities or customers have been informed.

Do not wait for perfect forensics. Send a clear initial report within six hours and follow with updates as facts stabilize.

#### Logging and Time Synchronization: What “Good” Looks Like

The Directions require at least 180 days of security logs to be retained in India. For most organizations, that will cover firewall, IDS/IPS, WAF, EDR/XDR, identity providers (SSO/IdP), application access, database activity, VPN gateways, cloud network flow logs, and cloud control-plane logs. Retention can be tiered for cost control, but critical sources should be placed on write-once (WORM) or similarly tamper‑resistant storage.

Time synchronization must be enforced across the estate with trusted NTP sources (e.g., NIC/NPL). From a legal defensibility standpoint, implement:

*   A central NTP hierarchy with configuration baselines.
*   Automated monitoring for drift beyond a defined threshold.
*   Documentation of time sources and change control on time settings.

Well-structured timestamps (ISO 8601 with timezone), consistent host/app identifiers, user/session IDs, and correlation IDs greatly simplify investigations and evidencing.

#### VPN, Cloud, Hosting, and Subscriber Information

Providers are expected to maintain validated subscriber/customer information and usage metadata for prescribed periods (commonly five years after the end of engagement). The minimum set typically includes identity and contact details, corporate ownership where relevant, allocated IPs and timestamps, authorized contacts, and provisioning location. Embed these requirements in onboarding, privacy notices, and MSAs/SOWs, and align your retention schedule to Indian law.

#### Governance: Making Compliance Routine

Appoint a 24×7 incident reporting coordinator with a designated alternate. Maintain a CERT‑In‑ready incident response (IR) SOP with:

*   A classification matrix tied to the Directions’ categories.
*   Clear triggers for the six-hour clock and a decision log.
*   Counsel checkpoints that complement, not delay, reporting.
*   Ready-to-use templates and a maintained contact directory.
*   Evidence handling and chain‑of‑custody protocols.
*   Board/CXO notification thresholds and investor/customer communication lines.

Exercises matter. Run at least one tabletop focused on the six-hour workflow and one technical drill annually to validate detection, logging, and time-sync controls.

#### Contracts That Withstand Scrutiny

Strengthen your contractual posture with targeted clauses:

*   Incident Notification: “Vendor shall notify within two (2) hours of discovering an incident that may be reportable under the CERT‑In Directions and provide details sufficient to enable six-hour regulatory reporting.”
*   Logging and Retention: “Vendor shall retain and, upon request, furnish security logs and audit trails for at least one hundred eighty (180) days stored in India.”
*   Time Synchronization: “Vendor shall maintain synchronized system time with trusted NTP sources and provide attestation upon request.”
*   Audit and Cooperation: “Company may audit CERT‑In-relevant controls and require participation in incident drills, subject to reasonable notice.”
*   Flow‑Down: “Vendor shall impose equivalent obligations on all sub‑processors.”

These clauses are not ornamental; they are the difference between smooth regulatory engagement and a scramble.

#### Technical Baseline: Counsel’s Minimum

*   SIEM/XDR with clear “reportable incident” tagging and one‑click export packs.
*   Centralized log collection with immutability for critical sources.
*   MFA by default, PAM for elevated access, and just‑in‑time privilege.
*   Asset inventory of internet‑facing systems and SBOM for key applications.
*   Immutable NTP configurations with alerting on drift.
*   Data discovery for personal/sensitive data to assess DPDP interactions.

#### Penalties and Overlapping Regimes

Non‑compliance with the Directions or failure to furnish information can attract penalties under the IT Act. Regulated entities may also face sectoral consequences (RBI, SEBI, IRDAI, etc.). Your IR playbook should map obligations across these frameworks to avoid duplication and inconsistency.

The [DPDP Act](https://amlegals.com/digital-personal-data-protection-rules-2025/) introduces breach‑related duties that often aris