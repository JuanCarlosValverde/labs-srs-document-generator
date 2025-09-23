# Example A: Retail Pharmacy (Walgreens) - Simplified

## Field Mapping Annotations
This example demonstrates the simplified BOV structure for a retail pharmacy property. Data tables (Comparables, Rent Roll, Case Studies) are auto-generated from CSV input.

## 1. Cover Page
| Field | Value |
|-------|-------|
| `bov_title` | "Broker's Opinion of Value" |
| `tenant_name` | "Walgreens" |
| `property_address` | "222 Hwy 6, Sugar Land, TX 77478" |
| `presented_to` | "ABC Investment Group" |
| `client_name` | "Steve Velez" |
| `client_title` | "Managing Director" |
| `client_company` | "ABC Investment Group" |
| `property_image` | [Walgreens store image] |

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
| `sold_section_title` | "Retail Pharmacy (South) - Sold Comparables - Trailing 2 Years" |
| `onmarket_section_title` | "Retail Pharmacy (Texas) - On Market Comparables" |

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
| `broker_name` | "JOHN SMITH, CCIM" |
| `broker_title` | "Managing Principal" |
| `broker_division` | "National Net Lease \| Houston, TX" |
| `broker_phone_direct` | "D: 713.555.0123" |
| `broker_phone_mobile` | "M: 713.555.0456" |
| `broker_email` | "john.smith@srsre.com" |
| `broker_photo` | [John Smith professional headshot] |
| `experience_title` | "Experience" |
| `experience_text` | "John joined SRS in 2018 with more than 8 years of transactional brokerage experience in the commercial real estate industry and over $750 million in closed transactions, representing over 200 individual properties. John specializes in retail pharmacy and healthcare properties, focusing on single-tenant, NNN-leased investments including national portfolios, merchant developer representation, sale-leasebacks, and lease restructuring throughout the Texas market." |
| `community_title` | "Community/Personal Information" |
| `community_text` | "John was recognized as a top retail pharmacy broker in the Houston market in 2022. He is an active member of the International Council of Shopping Centers (ICSC) and CCIM communities and enjoys golfing and spending time with his family in his free time." |

---

## Summary

**Manual Input Required**: 26 fields
**Auto-Generated from CSV**: Comparables, Rent Roll, Pricing Summary, Case Studies data
**Focus**: Section structure, titles, and key configuration fields
