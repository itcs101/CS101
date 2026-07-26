# 3. Five-Level Regulatory Requirements Taxonomy for AME

## 3.1 Unified Five-Level Taxonomy

To enable a layered platform design, we define a five-level classification for regulatory reporting requirements:

| Level | Name                                  | Scope                                                                   | Examples                                                                                                                                          |
| ----- | ------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| L1    | Top-level categories (5 areas)        | Cross-regional uniform categories; platform top-level partitioning      | Prudential capital & liquidity; transaction-level reporting; cross-border FX flows; AML/CFT & tax; local-specific modules                         |
| L2    | Sub-categories (~25)                  | Fixed breakdown under each top-level area; group field mapping baseline | Capital adequacy RWA; LCR/NSFR; Large exposure; corporate credit transaction-level; BOP reporting; CTR; ...                                       |
| L3    | Regulator & jurisdiction              | Routing, permissions and regulator-specific handling                    | HKMA, NFRA/PBOC (CN), FSC (TW), FSA (JP), FSS (KR), MAS (SG), APRA (AU), RBNZ (NZ), BNM (MY), OJK/BI (ID), BOT (TH), SBV (VN), BSP (PH), RBI (IN) |
| L4    | Official report identifier / template | Official regulator report IDs and templates                             | G01/G11/G40 (China 1104 family); MA(BS) series (HK); MAS600 series (SG); AP S-series (AU); B-series (TW); S10/S21/S50 (NZ)                        |
| L5    | Reporting frequency                   | Scheduling windows for the dispatch engine                              | Daily / Weekly / Monthly / Quarterly / Semi-annual / Annual / Real-time triggers                                                                  |

: 3.1 Unified Five-Level Taxonomy

## 3.2 Core-market-by-market regulatory inventory (selected highlights)

The report lists key regulatory returns and constraints per market in four regional blocks: Greater China, Northeast Asia, Southeast Asia, South Asia & Oceania. Key examples:

### Greater China — sample highlights

#### A. Hong Kong (HKMA + SFC)

**Regulators Overview:** The Hong Kong Monetary Authority (HKMA) is the primary banking regulator responsible for monetary stability and prudential supervision. The Securities and Futures Commission (SFC) oversees the securities and futures markets, including investment banking activities and conduct.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| ---- | ---- | ---- |
| 1. Prudential Capital & Liquidity | Monthly MA(BS) returns, KM1 core indicators, CC1 capital composition, LR leverage ratio, LCR/NSFR templates, semi-annual Pillar 3 disclosures, dedicated LAC (Loss Absorbing Capacity) reports | Full implementation of Basel III Final Reform; **the LAC framework is exclusive to Hong Kong** |
| 2. Granular Transaction Reporting | Item-by-item records of credit assets, detailed derivative transaction data | GDR 3.0 is being implemented under the principle of "Submit Once, Reuse Multiple Times" |
| 3. Cross-border Foreign Exchange Receipts & Payments | Offshore RMB cross-border business statistics, monthly foreign currency exposure statements, cross-border interbank business (MA(BS)9) | Special regulatory supervision applicable to the offshore RMB centre |
| 4. AML & Tax Compliance | CTR large cash transaction reports, STR suspicious transaction reports, CRS tax declarations, FATCA US tax reporting | Dual compliance regime for both FATCA and CRS requirements |
| 5. Local Specific Regimes | **Securities & investment banking conflict-of-interest disclosure**, deposit insurance filings, HKD currency issuance reserve reporting | Regulatory penalty case of HKD 4.2 million imposed in 2025 |

: A. Hong Kong (HKMA + SFC)


#### B. Mainland China (NFRA + PBOC + SAFE)

**Regulators Overview:** The National Financial Regulatory Administration (NFRA) is the principal regulator for the banking and insurance sectors, focusing on prudential and conduct supervision. The People's Bank of China (PBOC) oversees monetary policy, macroeconomic stability, and AML regulations. The State Administration of Foreign Exchange (SAFE) manages foreign exchange controls and cross-border capital flows.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| ---- | ---- | ---- |
| 1. Prudential Capital & Liquidity | 1104 Reporting Suite: G01 / G03 / G40 / G21 / G11 / G14 / S63 | Quarterly submission in accordance with the *Commercial Bank Capital Management Measures* |
| 2. Granular Transaction Reporting | **Full EAST granular datasets**: corporate credit, residential mortgage loans, interbank businesses, wealth management products, beneficial ownership penetration data | Primary evidence used by regulators during on-site inspections |
| 3. Cross-border Foreign Exchange Receipts & Payments | T+1 BOP (Balance of Payments) declarations, external debt statistics, cross-border RMB transactions, ODI (Outward Direct Investment) filings | Strict foreign exchange control enforced by SAFE (State Administration of Foreign Exchange) |
| 4. AML & Tax Compliance | Large-value & suspicious transaction reports, CRS overseas tax resident information submissions | Mandatory stringent monitoring over cash transactions |
| 5. Local Specific Regimes | Dedicated real estate lending reports, inclusive finance statistical filings, local government financing vehicle (LGFV) special returns | Three core structural regulatory supervision priorities |
| 🚫 Data Mandate | **All customer and transaction data must be stored domestically; unauthorized cross-border data export is prohibited** | Constrained by the *Cybersecurity Law* and *Personal Information Protection Law of the People's Republic of China* |

: B. Mainland China (NFRA + PBOC + SAFE)

### C. Taiwan, China (Financial Supervisory Commission + Central Bank)

**Regulators Overview:** The Financial Supervisory Commission (FSC) acts as the unified regulator for banking, securities, and insurance, enforcing prudential and conduct rules. The Central Bank of the Republic of China (Taiwan) oversees foreign exchange regulations, monetary policy, and specific cross-strait capital flow reporting.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| ---- | ---- | ---- |
| 1. Prudential Capital & Liquidity | Monthly B-series Capital Adequacy Report, Liquidity Maturity Gap Schedule, Quarterly Non-performing Loan Report | Report submission independently by local legal entities |
| 2. Transaction-level Details | **Daily full-account transaction-level detailed reports**, corporate credit exposure penetration data, personal trust asset breakdown data | High submission frequency with comprehensive data fields |
| 3. Cross-border Foreign Exchange Receipts & Payments | **Special cross-strait financial business statements (Unique across APAC)**, transaction-by-transaction declaration for foreign exchange receipts and payments | Strict penetrating supervision for cross-strait businesses |
| 4. AML / Tax Compliance | Large-value CTR reports, suspicious activity STR reports, CRS tax resident filing | — |
| 5. Local Special Requirements | Special statistics on cross-strait capital flows, dedicated real estate mortgage reports, dedicated securities & trust distribution filings | Exclusive cross-strait regulatory rules applicable only within APAC |
| 🚫 Data Governance Restriction | **Original ledgers for cross-strait dedicated reporting are prohibited from being stored outside the region** | Comply with financial information security regulations issued by the Financial Supervisory Commission |

: C. Taiwan, China (Financial Supervisory Commission + Central Bank)


### Northeast Asia — sample highlights

#### E. Japan (FSA+BOJ)

**Regulators Overview:** The Financial Services Agency (FSA) is the integrated financial regulator responsible for overseeing banking, securities, and insurance sectors to ensure stability and protect depositors/investors. The Bank of Japan (BOJ) implements monetary policy, ensures smooth settlement systems, and monitors FX transactions and macroprudential stability.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| --- | --- | --- |
| 1. Prudential Capital & Liquidity | Monthly simplified capital adequacy statement, quarterly foreign currency liquidity position report, large exposure ledger | Branches are not required to hold standalone legal entity capital |
| 2. Transaction-level Details | **Transaction-by-transaction derivatives records, full interbank lending ledgers** | ⚠️ 100% retention of transaction data; regulators are entitled to retrospective audits over any time period |
| 3. Cross-border FX Receipts & Payments | Daily foreign exchange transaction reports, quarterly cross-border investment & financing schedules, external claims and liabilities statistics | Strict supervision on cross-border Yen capital flows |
| 4. AML / Tax | Large-value CTR reports, cross-border IFT, suspicious transaction STR reports, CRS tax residency reporting | — |
| 5. Local Specific Requirements | Special report for Yen derivative risk exposure, cross-border capital ledger for Japan-focused foreign-funded entities | — |

: E. Japan (FSA+BOJ)

#### F. South Korea (FSS + BOK)

**Regulators Overview:** The Financial Supervisory Service (FSS) acts as the integrated executive arm of the Financial Services Commission (FSC), conducting examinations and enforcing compliance across all financial sectors. The Bank of Korea (BOK) focuses on monetary policy, systemic stability, and specific cross-border capital flow monitoring.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| ---- | ---- | ---- |
| 1. Prudential Capital & Liquidity | Branch-level simplified capital risk statement, monthly foreign currency liquidity stress test | Apply branch regulatory regime |
| 2. Transaction-level Details | **Detailed disclosure statements for financial conglomerate affiliated credit penetration**, transaction-by-transaction foreign exchange derivative records | Financial conglomerate affiliated transactions are marked as high reporting-risk items |
| 3. Cross-border FX Receipts & Payments | Real-time submission of cross-border capital flows, quarterly overseas investment reports, centralized collection of group cash pool data | ⚠️ Dual penalties for zero tolerance on FX reporting breaches + senior management accountability |
| 4. AML / Tax | Large-value CTR, cross-border IFT, suspicious STR reports, CRS tax compliance | — |
| 5. Local Features | **Special reporting for large financial conglomerate affiliated transactions**, cross-border capital statistics for semiconductor supply chains | Unique financial conglomerate supervision rules exclusive to South Korea |
| ⚠️ Data Constraints | **Raw data of KRW FX transactions and financial conglomerate affiliated transactions must be retained locally** | Comply with Personal Information Protection Act & FSS overall security guidelines |

: F. South Korea (FSS + BOK)


### Southeast Asia

#### G. Singapore (MAS)

**Regulators Overview:** The Monetary Authority of Singapore (MAS) serves as both the central bank and the integrated financial regulator, overseeing monetary policy, prudential regulations, and market conduct across banking, insurance, and capital markets.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| ---- | ---- | ---- |
| 1. Prudential Capital & Liquidity | **MAS 600 Series** monthly reports for capital adequacy, liquidity & leverage ratio; Pillar 3 disclosure; large risk exposure reports | Follow MAS Notice 637/651 |
| 2. Transaction-level Details | Loans, credit assets, derivatives & full-volume transaction records; **All cross-border transaction traceability data shall be stored locally for a minimum of 5 years** | — |
| 3. Cross-border FX Receipts & Payments | ASEAN cross-border capital pool statistics, multi-currency foreign exchange position monthly reports | Serve as ASEAN cross-border financial hub |
| 4. AML / Tax | CTR/IFT/STR reporting, CRS / FATCA obligations, MAS official Compliance Toolkit | — |
| 5. Local Features | Islamic finance dedicated filings, ASEAN cross-border treasury management reports, deposit insurance arrangements | Dual financial system framework |

: G. Singapore (MAS)


#### H. Malaysia (BNM) — Core of Dual-track Regulatory Regime

**Regulators Overview:** Bank Negara Malaysia (BNM) is the central bank and the primary regulatory authority, uniquely overseeing a dual-track financial system by enforcing both the Financial Services Act (FSA) for conventional banking and the Islamic Financial Services Act (IFSA) for Islamic banking.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| ---- | ---- | ---- |
| 1. Prudential Capital & Liquidity | BNM Quarterly Capital Adequacy Report, Liquidity Gap Statement, NPL Quality Report | Dual reporting for Conventional Banks & Islamic Banks |
| 2. Transaction-level Details | Full transaction records for corporate & retail credit, **Shariah-compliant transaction breakdown** | Dual-track data submission requirements |
| 3. Cross-border FX Receipts & Payments | Dedicated cross-border trade financing reports, monthly foreign currency position statements | Ringgit exchange control regulation |
| 4. AML / Tax Compliance | CTR/STR filings, CRS tax reporting, **DCR data compliance report (effective from 2020)** | — |
| 5. Local Characteristics | **Full set of dedicated IFSA Islamic finance reports**, Shariah non-compliance incident reports, palm oil lending statistics | Governed jointly by FSA and IFSA legislations |

: H. Malaysia (BNM) — Core of Dual-track Regulatory Regime


#### I. Indonesia (BI + OJK)

**Regulators Overview:** The Financial Services Authority (OJK) is the integrated regulator supervising the banking, capital markets, and non-bank financial sectors for prudential and market conduct. Bank Indonesia (BI), the central bank, governs monetary policy, payment systems, and strict foreign exchange controls.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| ---- | ---- | ---- |
| 1. Prudential Capital & Liquidity | Monthly OJK capital, liquidity & asset quality reports, semi-annual core prudential assessment | Mandatory semi-annual core prudential review |
| 2. Transaction-level Details | Transaction-by-transaction records for commodity trade finance, corporate credit exposure transparency, dedicated ledgers for commodities (palm oil / mineral resources) | — |
| 3. Cross-border FX Receipts & Payments | **Transaction-by-transaction declaration** for import & export FX flows, external debt & credit statistics | Strict Indonesian Rupiah foreign exchange control |
| ⚠️ Data Constraints | **All transaction data shall be stored domestically; cross-border data outflow is strictly forbidden** | Compliant with GR71 Electronic Transactions Regulation |

: I. Indonesia (BI + OJK)

#### J. Thailand (BOT)

**Regulators Overview:** The Bank of Thailand (BOT) is the central bank responsible for monetary policy, financial system stability, and the prudential supervision of financial institutions, as well as managing foreign exchange regulations.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| ---- | ---- | ---- |
| 1. Prudential Capital & Liquidity | Quarterly simplified statement for branch capital & foreign currency liquidity, large exposure ledgers | Rules apply to overseas branch institutions |
| 2. Transaction-level Details | Transaction-by-transaction records for import & export trade finance, credit records of foreign-invested enterprises | Mandatory real-time CTR reporting for cash transactions over 2 million Thai Baht |
| 3. Cross-border FX Receipts & Payments | Monthly cross-border FX receipt & payment filings, quarterly outbound investment statistics | Dynamic supervision on cross-border THB capital movement |

: J. Thailand (BOT)

#### K. Vietnam (SBV)

**Regulators Overview:** The State Bank of Vietnam (SBV) is the central bank and the primary regulatory body for the banking sector, responsible for monetary policy, licensing, prudential supervision, and enforcing strict data security and cross-border data transfer rules.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| ---- | ---- | ---- |
| 1. Prudential Capital & Liquidity | Monthly SBV reports on capital adequacy, liquidity and asset quality, semi-annual core prudential review | — |
| 2. Transaction-level Details | Credit details for foreign-funded manufacturing enterprises, transaction-by-transaction ledgers for real estate loans, special statistics for foreign capital supply chains | — |
| ⚠️ Data Constraints | **All financial data of local users must be stored domestically; special approval from the Ministry of Public Security is mandatory for data cross-border outflow** | Comply with Article 26 of the Cybersecurity Law of Vietnam |

: K. Vietnam (SBV)

#### L. Philippines (BSP)

**Regulators Overview:** The Bangko Sentral ng Pilipinas (BSP) serves as the central bank, providing comprehensive prudential supervision over banks and non-bank financial institutions, while also managing monetary policy and critical remittance reporting frameworks.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| ---- | ---- | ---- |
| 1. Prudential Capital & Liquidity | Monthly foreign currency liquidity reports for branches, large exposure ledgers, quarterly core prudential assessment | — |
| 2. Transaction-level Details | Itemized records of import & export trade financing, credit information of foreign-invested firms, **Overseas migrant worker remittance dedicated filings (Exclusive to the Philippines)** | — |
| 3. Cross-border FX Receipts & Payments | **Special statistical statements for overseas remittances**, monthly cross-border FX receipt & payment reports | Overseas remittance constitutes a major pillar of the Philippines' GDP |

: L. Philippines (BSP)

#### Oceania & South Asia — sample highlights

#### M. India (RBI)

**Regulators Overview:** The Reserve Bank of India (RBI) is the central bank and supreme regulatory authority for the banking sector, overseeing monetary policy, prudential regulations, foreign exchange management, and strictly enforcing domestic payment data localization mandates.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| ---- | ---- | ---- |
| 1. Prudential Capital & Liquidity | Monthly RBI reports covering capital adequacy, liquidity and NPL asset quality, independent prudential governance framework | — |
| 2. Transaction-level Details | Penetration data of corporate credit grants, full transaction details for retail banking, mandatory statistics for SME & agricultural credit | — |
| 3. Cross-border FX Receipts & Payments | Quarterly FDI & foreign investment reports, transaction-wise declaration for import & export FX settlements, external debt statistics | Rupee exchange control is rigorously enforced |
| ⚠️ Data Constraints | **Payment system data must be stored 100% locally; data cross-border transmission is banned without explicit regulatory clearance** | Follow RBI official circular for payment data localisation requirements |

: M. India (RBI)


#### N. Australia (APRA + AUSTRAC)

**Regulators Overview:** The Australian Prudential Regulation Authority (APRA) oversees the prudential stability of banks, insurers, and superannuation funds. The Australian Transaction Reports and Analysis Centre (AUSTRAC) acts as the financial intelligence agency and AML/CTF regulator, wielding independent enforcement authority over transaction reporting.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| ---- | ---- | ---- |
| 1. Prudential Capital & Liquidity | Quarterly APRA APS capital & liquidity reports, S-series filings, monthly S50 loan reports, Pillar 3 disclosures, CPS 234 Information Security standard | — |
| 2. Transaction-level Details | Item-by-item residential mortgage records, corporate credit penetration data, securities custody transaction details | Mandatory protection for consumer data privacy |
| 3. Cross-border FX Receipts & Payments | **Mandatory full-volume transaction-by-transaction reporting for cross-border IFT (International Funds Transfer)** | AUSTRAC is vested with independent law enforcement authority |
| 4. AML / Tax Compliance | TTR (Threshold Transaction Report) for large cash transactions, **SMR (Suspicious Matter Report) for suspicious activities**, annual AML compliance reports | Independent stringent supervision administered by AUSTRAC |
| ⚠️ Penalty Reference | AUD 35 million penalty imposed in 2026 for anti-fraud reporting deficiencies | Largest single compliance fine across the Asia-Pacific region in recent years |

: N. Australia (APRA + AUSTRAC)


#### O. New Zealand (RBNZ + FMA)

**Regulators Overview:** The Reserve Bank of New Zealand (RBNZ) is the central bank responsible for monetary policy and the prudential regulation of banks, insurers, and non-bank deposit takers. The Financial Markets Authority (FMA) regulates capital markets, financial services, and market conduct.

| Category | Core Reports / Specifications | Key Compliance Constraints |
| ---- | ---- | ---- |
| 1. Prudential Capital & Liquidity | RBNZ S10/S21/S50 filings, quarterly capital adequacy & liquidity statements, **ring-fencing regime for locally-incorporated entities’ capital** | — |
| ⚠️ Data Constraints | **Physical isolation for underlying business data of local legal entities; raw transaction detail data is prohibited from being stored overseas** | Governed by the RBNZ Prudential Information Security Standards |

: O. New Zealand (RBNZ + FMA)


## 3.3 Regional heatmap of common regulatory requirements

(Heatmap legend: ● = mandatory requirement; ◐ = partial/limited; ○ = not mandatory/free-flow)

| Market         | Prudential (capital/liquidity) | Transaction-level reporting | Cross-border FX flows | AML/CFT & tax | Local-special requirements | Data localization intensity |
| -------------- | ------------------------------ | --------------------------- | --------------------- | ------------- | -------------------------- | --------------------------- |
| Hong Kong      | ●                             | ●                          | ●                    | ●            | ●                         | ○ (free flow)              |
| Mainland China | ●                             | ●                          | ●                    | ●            | ●                         | ● (strong mandatory)       |
| Taiwan         | ●                             | ●                          | ●                    | ●            | ●                         | ● (strong mandatory)       |
| Japan          | ●                             | ●                          | ●                    | ●            | ○                         | ◐ (local copy)             |
| Korea          | ●                             | ●                          | ●                    | ●            | ●                         | ● (strong mandatory)       |
| Singapore      | ●                             | ●                          | ●                    | ●            | ●                         | ○ (free flow)              |
| Malaysia       | ●                             | ●                          | ●                    | ●            | ●                         | ● (strong mandatory)       |
| Indonesia      | ●                             | ●                          | ●                    | ●            | ○                         | ● (strong mandatory)       |
| Thailand       | ●                             | ◐                          | ●                    | ●            | ○                         | ◐ (local copy)             |
| Vietnam        | ●                             | ●                          | ●                    | ●            | ○                         | ● (strong mandatory)       |
| Philippines    | ●                             | ◐                          | ●                    | ●            | ●                         | ◐ (local copy)             |
| India          | ●                             | ●                          | ●                    | ●            | ●                         | ● (strong mandatory)       |
| Australia      | ●                             | ●                          | ●                    | ●            | ●                         | ◐ (local copy)             |
| New Zealand    | ●                             | ●                          | ●                    | ●            | ○                         | ● (strong mandatory)       |

: 3.3 Regional heatmap of common regulatory requirements

Key cross-regional conclusions:

1. Prudential capital/liquidity + AML/CFT + cross-border FX coverage is universal across all core markets — making these top priorities for group-level standardization.
2. Advanced jurisdictions are moving to transaction-level granular reporting; other markets are catching up rapidly.
3. 9/14 core markets (64%) impose mandatory local data storage constraints — raw transaction-level data cannot be centrally merged.
4. AML reporting templates are converging across the region (CTR/STR/IFT/CRS) — enabling a unified group AML module.
5. Most jurisdictional variance is concentrated in local-special requirements — this is the largest source of customization cost.

## 3.4 Special Regulation Statement on Dual-track Islamic Finance Supervision

| Dimension | Conventional Banks | Islamic Banks | HSBC Covered Markets |
| --- | --- | --- | --- |
| Legal Framework | Financial Services Act 2013 (FSA) | Islamic Financial Services Act 2013 (IFSA) | Malaysia |
| Financial Reporting Standards | MFRS | MFRS + Shariah contract disclosure + dividend payment compliance requirements | Malaysia |
| Operational Risk Reporting | ORR System (LED + KRI + SA) | ORR System + dedicated reporting for Shariah non-compliance incidents | Malaysia |
| Accounting Standards | IFRS / IAS Standards | **AAOIFI Standards** (Accounting and Auditing Organization for Islamic Financial Institutions) | Malaysia + Middle East |
| Prudential Rules | Basel III Framework | Basel III + additional prudential requirements for Islamic finance (e.g. supplementary credit & market risk rules issued by SAMA) | Malaysia + Middle East |
| Governance Structure | Board of Directors + Audit Committee | Board of Directors + **Independent Shariah Committee** + **Shariah Auditor** (appointment subject to regulatory approval) | All Islamic finance jurisdictions |

: 3.4 Special Regulation Statement on Dual-track Islamic Finance Supervision

TODO

* [ ] Deep dive into "Local-special requirements" to quantify the customization cost across top 5 priority markets.
* [ ] Validate the exact report mappings (L4) for India and Indonesia with local compliance teams.
