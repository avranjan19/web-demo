---
source_url: https://rbidocs.rbi.org.in/rdocs/notification/PDFs/107MDITGOVERNANCE3303572008604C67AC25B84292D85567.PDF
query: RBI IT security controls internet banking audit log retention
scraped_at: 2026-06-30T00:00:00+00:00
---

# RBI IT Governance, Risk, Controls and Assurance Practices Directions 2023
# Key Security Controls for Banks and NBFCs

Source: RBI/2023-24/107, DoS.CO.CSITEG/SEC.7/31.01.015/2023-24, November 7, 2023
Effective: April 1, 2024

---

## Internet Banking IT Security Controls (Chapter III)

### Access Controls (Section 19)
Regulated entities must implement the following IT security controls for internet banking:
- **Multi-Factor Authentication (MFA)**: Mandatory for all internet banking transactions and privileged system access. At least two independent authentication factors required.
- **Role-Based Access Control (RBAC)**: Access to systems must be granted on a need-to-know and need-to-do basis. Privileged access must be strictly controlled and logged.
- **Session Management**: Automatic session timeout after a defined period of inactivity. Concurrent sessions must be restricted.
- **Encryption**: All internet banking communications must use TLS 1.2 or higher. Data at rest must be encrypted using industry-standard algorithms.
- **Firewalls and DMZ**: Banks must implement firewalls and a demilitarised zone (DMZ) architecture to separate internet-facing systems from internal networks.
- **Intrusion Detection and Prevention**: Banks must deploy Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) for internet banking infrastructure.
- **Teleworking Controls (Section 20)**: Remote access to core banking systems must use encrypted VPN with MFA.

### Vulnerability Assessment and Penetration Testing (Section 26)
- Vulnerability Assessment (VA): At least once every six months for critical systems.
- Penetration Testing (PT): At least once every 12 months for critical systems.
- Independent and qualified experts must conduct VA/PT.
- Identified vulnerabilities must be remediated in a timely manner.

### Information Security Governance
- Banks must appoint a Chief Information Security Officer (CISO) with requisite technical expertise.
- An Information Security Committee (ISC) must be established to oversee cyber security.
- An IT Strategy Committee of the Board must meet at least quarterly.

---

## Audit Trail and Log Retention Requirements (Section 15)

Regulated entities must implement and maintain audit trails for all critical systems including core banking, internet banking, and payment systems.

### Key Requirements:
- **Audit Trail Coverage**: All user activities, system events, financial transactions, configuration changes, and access events must be logged.
- **Log Integrity**: Audit logs must be protected from unauthorised modification or deletion. Logs must be stored in a tamper-evident manner.
- **Retention Period**: Audit logs must be retained for a minimum period of **5 years** for core banking systems and critical IT systems. Logs related to financial transactions must be preserved for a period consistent with the applicable statute of limitations.
- **Log Review**: Regulated entities must review audit logs regularly. Automated tools for log analysis and alerting are recommended for critical systems.
- **Centralised Logging**: Banks must maintain centralised log management with real-time alerting for suspicious activities.

---

## Cyber Incident Response (Section 27)
- Banks must establish a Cyber Incident Response and Recovery Management process.
- Incident response procedures must be documented, tested, and updated regularly.
- Material cyber incidents must be reported to RBI as per prescribed timelines.

---

## Business Continuity and Disaster Recovery (Chapter V)
- Banks must maintain a Business Continuity Plan (BCP) and Disaster Recovery (DR) policy.
- Regular DR drills must be conducted to test the effectiveness of recovery plans.
- Recovery Time Objective (RTO) and Recovery Point Objective (RPO) must be defined and tested for all critical systems.
