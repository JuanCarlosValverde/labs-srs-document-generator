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
| `rent_roll_title` | "Lease Term & Rental Rates" |

**Note**: All lease data is generated from CSV input.

## 5. Pricing Summary
| Field | Value |
|-------|-------|
| `asking_price` | [Asking Price] |
| `net_operating_income` | [NOI] |
| `cap_rate` | [Cap Rate] |
| `lease_type` | [Lease Type] |
| `value_matrix` | [Value Matrix JSON] |
| `go_to_market_price` | [Price] |
| `strike_price` | [Price] |
| `value_floor` | [Price] |
| `valuation_notes` | [Valuation Notes] |

## 6. Case Studies Section (Auto-generated)
| Field | Value |
|-------|-------|
| `case_studies_title` | "Case Studies" |

**Note**: All case study data is generated from CSV input.

## 7. Broker Biography Section
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

---

## Summary

**Manual Input Required**: 35 fields
**Auto-Generated from CSV**: Comparables, Rent Roll, Case Studies data
**Focus**: Section structure, titles, and key configuration fields
