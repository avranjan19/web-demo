---
source_url: unknown-source
query: RBI data localization payment systems circular India
scraped_at: 2026-06-30T17:03:20.241194+00:00
---

India data localisation – Corporates and Institutions

Skip to main content open navigation close Navigation [![Deutsche Bank](/application/project/images/logos/identifier_retina.png) ](/ "Home")[Home](https://www.db.com/ "Deutsche Bank Logo") Skip main navigation

Pause

*   ## India Data Localisation
    

The way in which we store and route payment data in India is changing; in view of the emerging cyber security concerns around digital payments and to ensure better monitoring, Reserve Bank of India (RBI) introduced a new regulation, which requires that all data pertaining to domestic payments in India must be stored in India.  
  
RBI outlined this in circular reference RBI/2017-18/153 - DPSS.CO.OD No.2785/06.08.005/2017-2018 dated 6 April 2018 [(https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244)](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244 "RBI/2017-18/153 - DPSS.CO.OD No.2785/06.08.005/2017-2018 dated 6 April 2018").  
  
In order to comply with this regulation, Deutsche Bank is upgrading its systems. In preparation for this upgrade, we will continuously inform you of potential impact on your processes as well as the initial changes that you may notice to your channels/platforms and how to get ready for this.  
  
Please take note of the Impact and FAQs sections of this website and return regularly for the latest updates.

## Impact

If you have accounts in India, you are impacted. Regardless of whether you initiate domestic payments/collections or receive account information only. Please note below how different Deutsche Bank products/services are impacted.

## DB Direct Internet (DBDI):

In case you use DBDI we do not foresee that you will need to make any changes. The domain set-up, user entitlements, payment data, templates and beneficiaries will be ported to a newly created, separate India instance by us. User profiles, user credentials, administration process to access India account information and payment processing will remain unchanged. If you have an active user preference, alerts, schedulers etc. the same will be replicated into the new India instance by default.  
  

### [Show content of Further information on DB Direct Internet (DBDI)](#Further information on DB Direct Internet \(DBDI\) "Further information on DB Direct Internet (DBDI)")

✓ If you have a global domain which contains the Indian accounts and you initiate or upload payments manually, you will need to toggle between a new India instance and your existing global domain in order to view your transactions and account reporting or initiate and authorize payments

✓ If you use the file upload or file export functionality, the files will need to be in the “India only” and “non-India” accounts in the new set-up

### EBICS Electronic Data Transmission (EDT) Services:

In case you are enabled for EBICS channel for EDT, Request for Payment execution and/or Account Information services, a new, separate India instance will be created in EBICS.  
  

### [Show content of Further information on EBICS Electronic Data Transmission (EDT) Services:](#Further information on EBICS Electronic Data Transmission \(EDT\) Services: "Further information on EBICS Electronic Data Transmission (EDT) Services:")

✓ You are required to set up user access and corporate signatures for your India instance  
✓ You are required to send a separate payment file for Indian held accounts and another file for all your other countries  
✓ We will reach out to you bilaterally to provide further details on the change

### DB Application Programming Interface (API):

If you are calling any DB-hosted API endpoint for initiating payments related instructions from your Indian accounts, there will be a new endpoint (a new hostname) which is hosted to segregate India flows.

Old hostname: [https://corporateapi.db.com](https://corporateapi.db.com)

New hostname: [https://api.corporatebank.db.com](https://api.corporatebank.db.com)

### [Show content of Further information on DB Application Programming Interface (API):](#Further information on DB Application Programming Interface \(API\): "Further information on DB Application Programming Interface (API):")

✓ You will need to make the relevant changes on your side to connect to the new endpoint for all API traffic as outlined above  
✓ We will reach out to you bilaterally to provide further details on the change

### DB Direct Connect (Host-to-Host):

If you are currently sending/uploading a single payment file with debit accounts of different countries, under the new regulatoion, we will not be able to process combined transaction files containing information and data pertaining to accounts both in India and overseas. Where payment instructions are received in such instances, they will be treated as invalid and will be cancelled.

### [Show content of Further information on DB Direct Connect (host-to-host):](#Further information on DB Direct Connect \(host-to-host\): "Further information on DB Direct Connect (host-to-host):")

✓ You are required to send a separate payment file for Indian held accounts and another file for all your other countries  
✓ India payment files incoming to global instances will be automatically relayed to India instances and information will be retained for max. 24 hrs. before being deleted from global instances.  
✓ In case you receive reports, you need to retrieve these separately for India and the rest of world  
✓ We will reach out to you bilaterally to provide further details on the change

### SWIFT-FileAct (MaCUG/Score):

In addition to segregating local Indian and other global payment files, a new SWIFT BIC Code DEUTINBB to be used for MACUG & SCORE Services with all other parameters for payment files relating to India accounts remain as is. All responses including Payment Status Reports (PSR) and Bank Statements will be received from the new BIC code. This ensures that the payment files relating to India accounts are routed to the new SWIFT India instance and stored locally in India.

### [Show content of Further information on SWIFT-FileAct (MaCUG/Score):](#Further information on SWIFT-FileAct \(MaCUG/Score\): "Further information on SWIFT-FileAct (MaCUG/Score):")

✓ You are required to update your systems & stationary accordingly  
✓ We will reach out to you bilaterally to provide further details on the change

### SWIFT Services/FIN:

If you or your forwarding agent are exchanging payment request information or sending Money Transfer (MX/MT) messages using the SWIFT protocol to Deutsche Bank India as executing Bank, you will need to use a separate FIN channel and the new SWIFT BIC code:

DEUTINBBP9V. All responses received will also come from the new BIC code.

If you are exchanging payment request information to Deutsche Bank India to relay (MX/MT) messages using SWIFT protocol to executing Banks in India, executing banks shall receive messages from new SWIFT BIC code: DEUTINBBP9V.

### [Show content of Further information on SWIFT Services/FIN:](#Further information on SWIFT Services/FIN: "Further information on SWIFT Services/FIN:")

✓ You are required to update your systems & stationary accordingly  
✓ We will reach out to you bilaterally to provide further details on the change

### Relationship Management Application (RMA) Exchange:

(Only applicable in case of SWIFT Service/FIN are used)

If you or your forwarding agents / execution banks on your behalf are sending or receiving Money Transfer (MT) requests, then please be informed that the new SWIFT BIC code DEUTINBBP9V will be valid without format changes to MT101 structure.

### [Show content of Further information on Relationship Management Application (RMA) Exchange:](#Further information on Relationship Management Application \(RMA\) Exchange: "Further information on Relationship Management Application (RMA) Exchange:")

(Only applicable in case of SWIFT Service/FIN are used)

✓ You will be required to exchange the SWIFT BIC Code DEUTINB