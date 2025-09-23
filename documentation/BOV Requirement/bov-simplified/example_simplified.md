# Example: Simplified BOV Structure

## Field Mapping Annotations
This example demonstrates the simplified BOV structure focusing only on manual input fields and section titles.

## 1. Cover Page
| Field | Value |
|-------|-------|
| `bov_title` | "Broker's Opinion of Value" |
| `tenant_name` | [Tenant Name] |
| `property_address` | [Property Address] |
| `presented_to` | [Client Company] |
| `client_name` | [Client Name] |
| `client_title` | [Client Title] |
| `client_company` | [Client Company] |
| `property_image` | [Property Image] |

## 2. Table of Contents
| Field | Value |
|-------|-------|
| `toc_background_image` | [Background Image] |
| `page_3_title` | "Property Overview" |
| `page_3_subitems` | "Comparables \| Rent Roll \| Pricing Summary" |
| `page_5_title` | "National Net Lease" |
| `page_5_subitems` | "Team Overview" |
| `page_18_title` | "Marketing Strategy" |
| `page_18_subitems` | "& Timeline" |
| `page_21_title` | "SRS Real Estate Partners" |
| `page_21_subitems` | "Overview" |

## 3. Comparables Section (Auto-generated)
| Field | Value |
|-------|-------|
| `sold_section_title` | [Auto-generated based on property type] |
| `onmarket_section_title` | [Auto-generated based on property type] |

**Note**: All comparable data is generated from CSV input.

## 4. Rent Roll Section (Auto-generated)
| Field | Value |
|-------|-------|
| `rent_roll_title` | "RENT ROLL" |

**Note**: All lease data is generated from CSV input.

## 5. Investment Highlights Section (Manual Input)
| Field | Value |
|-------|-------|
| `investment_highlights_title` | "INVESTMENT HIGHLIGHTS" |
| `highlight_section_1_title` | [Highlight Section 1 Title] |
| `highlight_section_1_point_1` | [Highlight Section 1 Point 1] |
| `highlight_section_1_point_2` | [Highlight Section 1 Point 2] |
| `highlight_section_2_title` | [Highlight Section 2 Title] |
| `highlight_section_2_point_1` | [Highlight Section 2 Point 1] |
| `highlight_section_2_point_2` | [Highlight Section 2 Point 2] |
| `highlight_section_3_title` | [Highlight Section 3 Title] |
| `highlight_section_3_point_1` | [Highlight Section 3 Point 1] |
| `highlight_section_3_point_2` | [Highlight Section 3 Point 2] |
| `highlight_section_4_title` | [Highlight Section 4 Title] |
| `highlight_section_4_point_1` | [Highlight Section 4 Point 1] |
| `highlight_section_4_point_2` | [Highlight Section 4 Point 2] |
| `highlight_section_5_title` | [Highlight Section 5 Title] |
| `highlight_section_5_point_1` | [Highlight Section 5 Point 1] |
| `highlight_section_5_point_2` | [Highlight Section 5 Point 2] |

## 6. Valuation Section (Auto-generated)
| Field | Value |
|-------|-------|
| `valuation_title` | "VALUATION" |

**Note**: All valuation data (offering, property specifications, sales range, demographics, etc.) is generated from CSV input.

## 7. Case Studies Section (Auto-generated)
| Field | Value |
|-------|-------|
| `case_studies_title` | "Case Studies" |

**Note**: All case study data is generated from CSV input.

## 8. Broker Biography Section
| Field | Value |
|-------|-------|
| `page_title` | "BROKER BIOGRAPHY" |
| `company_logo` | [Company Logo] |
| `broker_name` | [Broker Name] |
| `broker_title` | [Broker Title] |
| `broker_division` | [Division | Location] |
| `broker_phone_direct` | [Direct Phone] |
| `broker_phone_mobile` | [Mobile Phone] |
| `broker_email` | [Email Address] |
| `broker_photo` | [Broker Photo] |
| `experience_title` | "Experience" |
| `experience_text` | [Experience Description] |
| `community_title` | "Community/Personal Information" |
| `community_text` | [Community/Personal Description] |
| `education_title` | "Education" |
| `education_text` | [Education Description] |
| `transactions_title` | "Notable Transactions" |
| `transaction_1` | [Transaction 1] |
| `transaction_2` | [Transaction 2] |
| `transaction_3` | [Transaction 3] |
| `transaction_4` | [Transaction 4] |
| `transaction_5` | [Transaction 5] |

---

## Summary

**Manual Input Required**: 52 fields
**Auto-Generated from CSV**: Comparables, Rent Roll, Valuation, Case Studies data
**Focus**: Section structure, titles, and key configuration fields

**Sections Included**:
- Cover Page (8 fields)
- Table of Contents (9 fields) 
- Investment Highlights (15 fields)
- Broker Biography (17 fields)
- Notable Transactions (6 fields within Broker Biography)
