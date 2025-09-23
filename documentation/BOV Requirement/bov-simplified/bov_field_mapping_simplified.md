# BOV Field Mapping - Simplified Version

This document defines the simplified field structure for BOV templates for ADK generation.  
**Note**: Data tables (Comparables, Rent Roll, Case Studies) are generated automatically from CSV input - only section structure and titles are mapped here.

---

## 1. Cover Page

| Field            | Type    | Required | Validation                                    | Source        |
|------------------|---------|----------|-----------------------------------------------|---------------|
| bov_title        | string  | Yes      | Default: "Broker's Opinion of Value"          | Static/Text   |
| tenant_name      | string  | Yes      | ≤120 chars                                    | CSV/Agent     |
| property_address | string  | Yes      | Must include street, city, state, ZIP         | CSV/Agent     |
| presented_to     | string  | Yes      | ≤120 chars, cannot be empty                   | Agent/CSV     |
| client_name      | string  | Yes      | ≤120 chars                                    | Agent/CSV     |
| client_title     | string  | No       | ≤100 chars                                    | Agent/CSV     |
| client_company   | string  | No       | ≤100 chars                                    | Agent/CSV     |
| property_image   | image   | Yes      | Must be valid image file (JPG/PNG)            | Uploaded      |

---

## 2. Table of Contents

| Field                | Type    | Required | Validation                                    | Source        |
|----------------------|---------|----------|-----------------------------------------------|---------------|
| toc_background_image | image   | Yes      | Must be valid image file (JPG/PNG)            | Static        |
| page_3_title         | string  | Yes      | Default: "Property Overview"                  | Static        |
| page_3_subitems      | string  | Yes      | Default: "Comparables \| Rent Roll \| Pricing Summary" | Static |
| page_5_title         | string  | Yes      | Default: "National Net Lease"                 | Static        |
| page_5_subitems      | string  | Yes      | Default: "Team Overview"                      | Static        |
| page_18_title        | string  | Yes      | Default: "Marketing Strategy"                 | Static        |
| page_18_subitems     | string  | Yes      | Default: "& Timeline"                         | Static        |
| page_21_title        | string  | Yes      | Default: "SRS Real Estate Partners"           | Static        |
| page_21_subitems     | string  | Yes      | Default: "Overview"                           | Static        |

---

## 3. Comparables Section (Auto-generated from CSV)

| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| sold_section_title   | string   | Yes      | Auto-generated based on property type         | System        |
| onmarket_section_title| string  | Yes      | Auto-generated based on property type         | System        |

**Note**: All comparable data (properties, prices, cap rates, etc.) is generated automatically from CSV input.

---

## 4. Rent Roll Section (Auto-generated from CSV)

| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| rent_roll_title      | string   | Yes      | Default: "RENT ROLL"                          | Static        |

**Note**: All lease data (tenant info, dates, amounts, financial information, value matrix, property specifications, etc.) is generated automatically from CSV input.

---

## 5. Investment Highlights Section (Manual Input)

| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| investment_highlights_title| string| Yes      | Default: "INVESTMENT HIGHLIGHTS"              | Static        |
| highlight_section_1_title| string| No       | ≤100 chars (e.g., "8+ Years Remaining | Options To Extend | 2% Annual Rent Increases") | Agent/CSV |
| highlight_section_1_point_1| string| No       | ≤300 chars                                    | Agent/CSV     |
| highlight_section_1_point_2| string| No       | ≤300 chars                                    | Agent/CSV     |
| highlight_section_2_title| string| No       | ≤100 chars (e.g., "Absolute NNN Lease | Zero Landlord Responsibilities") | Agent/CSV |
| highlight_section_2_point_1| string| No       | ≤300 chars                                    | Agent/CSV     |
| highlight_section_2_point_2| string| No       | ≤300 chars                                    | Agent/CSV     |
| highlight_section_3_title| string| No       | ≤100 chars (e.g., "Clark Crossing Shopping Center | Dense Retail Corridor") | Agent/CSV |
| highlight_section_3_point_1| string| No       | ≤300 chars                                    | Agent/CSV     |
| highlight_section_3_point_2| string| No       | ≤300 chars                                    | Agent/CSV     |
| highlight_section_4_title| string| No       | ≤100 chars (e.g., "Atlanta Highway / US-78 (27,400 VPD) | Regional Connectivity") | Agent/CSV |
| highlight_section_4_point_1| string| No       | ≤300 chars                                    | Agent/CSV     |
| highlight_section_4_point_2| string| No       | ≤300 chars                                    | Agent/CSV     |
| highlight_section_5_title| string| No       | ≤100 chars (e.g., "Strong Demographics") | Agent/CSV |
| highlight_section_5_point_1| string| No       | ≤300 chars                                    | Agent/CSV     |
| highlight_section_5_point_2| string| No       | ≤300 chars                                    | Agent/CSV     |

**Note**: This section allows for flexible content creation with up to 5 highlight sections, each with a title and 2 bullet points. All fields are optional to allow for varying content needs.

---

## 6. Valuation Section (Auto-generated from CSV)

| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| valuation_title      | string   | Yes      | Default: "VALUATION"                          | Static        |

**Note**: All valuation data (offering, property specifications, sales range, demographics, etc.) is generated automatically from CSV input.

---

## 7. Case Studies Section (Auto-generated from CSV)

| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| case_studies_title   | string   | Yes      | Default: "Case Studies"                       | Static        |

**Note**: All case study data (properties, status, prices, etc.) is generated automatically from CSV input.

---

## 8. Broker Biography Section

### 8.1 Page Header
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| page_title           | string   | Yes      | Default: "BROKER BIOGRAPHY"                   | Static        |
| company_logo         | image    | Yes      | SRS Capital Markets logo                      | Static        |

### 8.2 Broker Information Fields
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| broker_name          | string   | Yes      | e.g., "FIRST LAST, CREDENTIALS"               | Agent/CSV     |
| broker_title         | string   | Yes      | e.g., "Managing Principal"                    | Agent/CSV     |
| broker_division      | string   | Yes      | e.g., "Division \| City, State"               | Agent/CSV     |
| broker_phone_direct  | string   | No       | Format: "D: XXX.XXX.XXXX"                     | Agent/CSV     |
| broker_phone_mobile  | string   | No       | Format: "M: XXX.XXX.XXXX"                     | Agent/CSV     |
| broker_email         | string   | Yes      | Valid email format                            | Agent/CSV     |
| broker_photo         | image    | Yes      | Professional headshot, JPG/PNG, max 5MB       | Uploaded      |

### 8.3 Experience Section
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| experience_title     | string   | Yes      | Default: "Experience"                         | Static        |
| experience_text      | text     | Yes      | Professional background paragraph              | Agent/CSV     |

### 8.4 Community/Personal Section
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| community_title      | string   | Yes      | Default: "Community/Personal Information"     | Static        |
| community_text       | text     | No       | Personal/community information paragraph       | Agent/CSV     |

### 8.5 Education Section
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| education_title      | string   | Yes      | Default: "Education"                         | Static        |
| education_text       | text     | No       | Educational background paragraph               | Agent/CSV     |

### 8.6 Notable Transactions Section
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| transactions_title   | string   | Yes      | Default: "Notable Transactions"              | Static        |
| transaction_1        | string   | No       | ≤200 chars (e.g., "Wawa - Brooklawn, NJ ($8.9M)") | Agent/CSV |
| transaction_2        | string   | No       | ≤200 chars (e.g., "Stock Plaza Shopping Center - Naples, FL ($26.5M)") | Agent/CSV |
| transaction_3        | string   | No       | ≤200 chars (e.g., "University Plaza - Vestal, NY ($20M)") | Agent/CSV |
| transaction_4        | string   | No       | ≤200 chars (e.g., "Associated Medical Professionals of NY - Syracuse, NY ($13.6M)") | Agent/CSV |
| transaction_5        | string   | No       | ≤200 chars (e.g., "Sherwin Williams Distribution Facility - Effingham, IL ($58.2M)") | Agent/CSV |

---

## Summary

**Total Fields**: 52 fields (vs 136 in full version)

**Auto-generated Sections**:
- Comparables (from CSV)
- Rent Roll (from CSV)
- Valuation (from CSV)
- Case Studies (from CSV)

**Manual Input Sections**:
- Cover Page (8 fields)
- Table of Contents (9 fields)
- Investment Highlights (15 fields)
- Broker Biography (17 fields)

This simplified version focuses on the structural elements that need manual configuration, while data-heavy sections are handled automatically by the ADK system from CSV input. The ADK will generate all table content from CSV data based on the section titles provided.
