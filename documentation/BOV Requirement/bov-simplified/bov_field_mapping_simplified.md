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
| rent_roll_title      | string   | Yes      | Default: "Lease Term & Rental Rates"          | Static        |

**Note**: All lease data (tenant info, dates, amounts, etc.) is generated automatically from CSV input.

---

## 5. Pricing Summary (Auto-generated from CSV)

| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| pricing_title        | string   | Yes      | Default: "Pricing Summary"                    | Static        |

**Note**: All pricing data (price, NOI, cap rates, value matrix, etc.) is generated automatically from CSV input.

---

## 6. Case Studies Section (Auto-generated from CSV)

| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| case_studies_title   | string   | Yes      | Default: "Case Studies"                       | Static        |

**Note**: All case study data (properties, status, prices, etc.) is generated automatically from CSV input.

---

## 7. Broker Biography Section

### 7.1 Page Header
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| page_title           | string   | Yes      | Default: "BROKER BIOGRAPHY"                   | Static        |
| company_logo         | image    | Yes      | SRS Capital Markets logo                      | Static        |

### 7.2 Broker Information Fields
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| broker_name          | string   | Yes      | e.g., "FIRST LAST, CREDENTIALS"               | Agent/CSV     |
| broker_title         | string   | Yes      | e.g., "Managing Principal"                    | Agent/CSV     |
| broker_division      | string   | Yes      | e.g., "Division \| City, State"               | Agent/CSV     |
| broker_phone_direct  | string   | No       | Format: "D: XXX.XXX.XXXX"                     | Agent/CSV     |
| broker_phone_mobile  | string   | No       | Format: "M: XXX.XXX.XXXX"                     | Agent/CSV     |
| broker_email         | string   | Yes      | Valid email format                            | Agent/CSV     |
| broker_photo         | image    | Yes      | Professional headshot, JPG/PNG, max 5MB       | Uploaded      |

### 7.3 Experience Section
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| experience_title     | string   | Yes      | Default: "Experience"                         | Static        |
| experience_text      | text     | Yes      | Professional background paragraph              | Agent/CSV     |

### 7.4 Community/Personal Section
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| community_title      | string   | Yes      | Default: "Community/Personal Information"     | Static        |
| community_text       | text     | No       | Personal/community information paragraph       | Agent/CSV     |

---

## Summary

**Total Fields**: 26 fields (vs 136 in full version)

**Auto-generated Sections**:
- Comparables (from CSV)
- Rent Roll (from CSV)
- Pricing Summary (from CSV)
- Case Studies (from CSV)

**Manual Input Sections**:
- Cover Page (8 fields)
- Table of Contents (9 fields)
- Broker Biography (9 fields)

This simplified version focuses on the structural elements that need manual configuration, while data-heavy sections are handled automatically by the ADK system from CSV input.
