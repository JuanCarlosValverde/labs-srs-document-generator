# Example C: Medical Office (Urgent Care) - Simplified

## Field Mapping Annotations
This example demonstrates the simplified BOV structure for a medical office property. Data tables (Comparables, Rent Roll, Case Studies) are auto-generated from CSV input.

## 1. Cover Page
| Field | Value |
|-------|-------|
| `bov_title` | "Broker's Opinion of Value" |
| `tenant_name` | "Urgent Care Group" |
| `property_address` | "411 Elm St, Dallas, TX 75202" |
| `presented_to` | "DEF Healthcare Investors" |
| `client_name` | "Dr. James Wilson" |
| `client_title` | "Portfolio Manager" |
| `client_company` | "DEF Healthcare Investors" |
| `property_image` | [Urgent Care facility image] |

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
| `sold_section_title` | "Medical Office (Dallas) - Sold Comparables - Trailing 2 Years" |
| `onmarket_section_title` | "Medical Office (Texas) - On Market Comparables" |

**Note**: All comparable data (properties, prices, cap rates, etc.) is generated automatically from CSV input.

## 4. Rent Roll Section (Auto-generated from CSV)
| Field | Value |
|-------|-------|
| `rent_roll_title` | "Lease Term & Rental Rates" |

**Note**: All lease data (tenant info, dates, amounts, etc.) is generated automatically from CSV input.

## 5. Pricing Summary
| Field | Value |
|-------|-------|
| `asking_price` | 3,750,000 |
| `net_operating_income` | 324,000 |
| `cap_rate` | 6.15 |
| `lease_type` | "NNN" |
| `value_matrix` | [{"cap_rate": 6.15, "price": 3750000}, {"cap_rate": 6.40, "price": 3600000}] |
| `go_to_market_price` | 3,600,000 |
| `strike_price` | 3,500,000 |
| `value_floor` | 3,400,000 |
| `valuation_notes` | "Modern medical facility with excellent parking and accessibility. Located in high-traffic medical corridor." |

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
| `broker_name` | "DAVID JOHNSON, CCIM" |
| `broker_title` | "Managing Principal" |
| `broker_division` | "National Net Lease \| Dallas, TX" |
| `broker_phone_direct` | "D: 214.555.0123" |
| `broker_phone_mobile` | "M: 214.555.0456" |
| `broker_email` | "david.johnson@srsre.com" |
| `broker_photo` | [David Johnson professional headshot] |
| `experience_title` | "Experience" |
| `experience_text` | "David joined SRS in 2020 with more than 7 years of transactional brokerage experience in the commercial real estate industry and over $600 million in closed transactions, representing over 180 individual properties. David specializes in medical office and healthcare properties, focusing on single-tenant, NNN-leased investments including national portfolios, merchant developer representation, sale-leasebacks, and lease restructuring throughout the Texas market." |
| `community_title` | "Community/Personal Information" |
| `community_text` | "David was recognized as a top medical office broker in the Dallas market in 2023. He is an active member of the International Council of Shopping Centers (ICSC) and CCIM communities and enjoys tennis and volunteering at local healthcare charities in his free time." |

---

## Summary

**Manual Input Required**: 35 fields
**Auto-Generated from CSV**: Comparables, Rent Roll, Case Studies data
**Focus**: Section structure, titles, and key configuration fields
