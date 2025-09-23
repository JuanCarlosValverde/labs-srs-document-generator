# Example B: Quick Service Restaurant (Taco Bell) - Simplified

## Field Mapping Annotations
This example demonstrates the simplified BOV structure for a QSR property. Data tables (Comparables, Rent Roll, Case Studies) are auto-generated from CSV input.

## 1. Cover Page
| Field | Value |
|-------|-------|
| `bov_title` | "Broker's Opinion of Value" |
| `tenant_name` | "Taco Bell" |
| `property_address` | "1555 Broadway, San Antonio, TX 78215" |
| `presented_to` | "XYZ Capital Partners" |
| `client_name` | "Maria Rodriguez" |
| `client_title` | "Investment Manager" |
| `client_company` | "XYZ Capital Partners" |
| `property_image` | [Taco Bell store image] |

## 2. Table of Contents
| Field | Value |
|-------|-------|
| `toc_background_image` | [Background image] |
| `page_3_title` | "Property Overview" |
| `page_3_subitems` | "Comparables \| Rent Roll \| Pricing Summary" |
| `page_5_title` | "National Net Lease" |
| `page_5_subitems` | "Team Overview" |
| `page_18_title` | "Marketing Strategy" |
| `page_18_subitems` | "& Timeline" |
| `page_21_title` | "SRS Real Estate Partners" |
| `page_21_subitems` | "Overview" |

## 3. Comparables Section (Auto-generated from CSV)
| Field | Value |
|-------|-------|
| `sold_section_title` | "QSR (South) - Sold Comparables - Trailing 2 Years" |
| `onmarket_section_title` | "QSR (Texas) - On Market Comparables" |

**Note**: All comparable data (properties, prices, cap rates, etc.) is generated automatically from CSV input.

## 4. Rent Roll Section (Auto-generated from CSV)
| Field | Value |
|-------|-------|
| `rent_roll_title` | "Lease Term & Rental Rates" |

**Note**: All lease data (tenant info, dates, amounts, etc.) is generated automatically from CSV input.

## 5. Pricing Summary (Auto-generated)
| Field | Value |
|-------|-------|
| `pricing_title` | "Pricing Summary" |

**Note**: All pricing data (asking price, NOI, cap rates, value matrix, etc.) is generated from CSV input.

## 6. Case Studies Section (Auto-generated from CSV)
| Field | Value |
|-------|-------|
| `case_studies_title` | "Case Studies" |

**Note**: All case study data (properties, status, prices, etc.) is generated automatically from CSV input.

## 7. Broker Biography Section
| Field | Value |
|-------|-------|
| `page_title` | "BROKER BIOGRAPHY" |
| `company_logo` | [SRS Capital Markets logo] |
| `broker_name` | "MARIA RODRIGUEZ" |
| `broker_title` | "Managing Principal" |
| `broker_division` | "National Net Lease \| San Antonio, TX" |
| `broker_phone_direct` | "D: 210.555.0123" |
| `broker_phone_mobile` | "M: 210.555.0456" |
| `broker_email` | "maria.rodriguez@srsre.com" |
| `broker_photo` | [Maria Rodriguez professional headshot] |
| `experience_title` | "Experience" |
| `experience_text` | "Maria joined SRS in 2019 with more than 6 years of transactional brokerage experience in the commercial real estate industry and over $500 million in closed transactions, representing over 150 individual properties. Maria specializes in QSR and restaurant properties, focusing on single-tenant, NNN-leased investments including national portfolios, merchant developer representation, and sale-leasebacks throughout the Texas market." |
| `community_title` | "Community/Personal Information" |
| `community_text` | "Maria was recognized as a top QSR broker in the San Antonio market in 2023. She is an active member of the International Council of Shopping Centers (ICSC) and enjoys cooking and traveling in her free time." |

---

## Summary

**Manual Input Required**: 26 fields
**Auto-Generated from CSV**: Comparables, Rent Roll, Pricing Summary, Case Studies data
**Focus**: Section structure, titles, and key configuration fields
