# Example A: Retail Pharmacy (Walgreens)

## Field Mapping Annotations
This example demonstrates a single-tenant retail pharmacy property with NNN lease structure based on actual PDF template structure.

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
| `toc_background_image` | [Whole Foods Market image] |
| `page_3_title` | "Property Overview" |
| `page_3_subitems` | "Comparables \| Rent Roll \| Pricing Summary" |
| `page_5_title` | "National Net Lease" |
| `page_5_subitems` | "Team Overview" |
| `page_18_title` | "Marketing Strategy" |
| `page_18_subitems` | "& Timeline" |
| `page_21_title` | "SRS Real Estate Partners" |
| `page_21_subitems` | "Overview" |

## 3. Comparables

### 3.1 Sold Comparables Section
| Field | Value |
|-------|-------|
| `sold_section_title` | "Retail Pharmacy (South) - Sold Comparables - Trailing 2 Years" |
| `comp_id` | "COMP001" |
| `property_name` | "Walgreens Sugar Land" |
| `property_address` | "222 Hwy 6, Sugar Land, TX 77478" |
| `city` | "Sugar Land" |
| `state` | "TX" |
| `sale_date` | "2024-05-15" |
| `sale_price` | 4,200,000 |
| `lease_term_remaining` | 14 |
| `year_built` | 2018 |
| `building_sf` | 14,800 |
| `land_acres` | 1.25 |
| `annual_rent` | 354,000 |
| `rent_per_sf_per_yr` | 23.92 |
| `price_per_sf` | 283.78 |
| `cap_rate` | 5.75 |
| `market_time_days` | 45 |

### 3.2 On Market Comparables Section
| Field | Value |
|-------|-------|
| `onmarket_section_title` | "Retail Pharmacy (Texas) - On Market Comparables" |
| `asking_price` | 4,250,000 |
| `subject_property_flag` | true |

## 4. Rent Roll

### 4.1 Lease Term & Rental Rates Table
| Field | Value |
|-------|-------|
| `tenant_name` | "Walgreens" |
| `square_feet` | 14,800 |
| `lease_start` | "2018-01-01" |
| `lease_end` | "2038-12-31" |
| `begin_period` | "Current" |
| `increase_rate` | 0 |
| `monthly_rent` | 29,500 |
| `annual_rent` | 354,000 |
| `recovery_type` | "NNN" |
| `options` | "-" |
| `rofr_note` | "Tenant Has a 20-Day Right Of First Refusal (ROFR)" |

### 4.2 Financial Information Section
| Field | Value |
|-------|-------|
| `price` | 1,690,000 |
| `net_operating_income` | 354,000 |
| `cap_rate` | 6.00 |
| `lease_type` | "NNN" |

### 4.3 Value Matrix Section
| Field | Value |
|-------|-------|
| `go_to_market_rate` | 6.00 |
| `go_to_market_price` | 1,690,000 |
| `strike_price_rate` | 6.35 |
| `strike_price` | 1,597,000 |
| `value_floor_rate` | 6.70 |
| `value_floor` | 1,514,000 |

### 4.4 Property Specifications Section
| Field | Value |
|-------|-------|
| `year_built` | 2018 |
| `rentable_area` | 14,800 |
| `land_area` | 1.25 |
| `property_address` | "222 Hwy 6, Sugar Land, TX 77478" |

## 5. Pricing Summary
| Field | Value |
|-------|-------|
| `asking_price` | 4,250,000 |
| `net_operating_income` | 354,000 |
| `cap_rate` | 5.75 |
| `lease_type` | "NNN" |
| `value_matrix` | [{"cap_rate": 5.75, "price": 4250000}, {"cap_rate": 6.00, "price": 4000000}] |
| `go_to_market_price` | 4,200,000 |
| `strike_price` | 4,050,000 |
| `value_floor` | 3,900,000 |
| `valuation_notes` | "Prime corner location with excellent visibility and traffic counts. Long-term NNN lease with national credit tenant." |

## 6. Case Studies

### 6.1 Case Studies Grid (6 Properties)
| Property | Status | City/State | Property Name | Price | Cap Rate | SF |
|----------|--------|------------|---------------|-------|----------|-----|
| 1 | CLOSED | Sugar Land, TX | Walgreens | $4,200,000 | 5.75% | 14,800 |
| 2 | CLOSED | Richmond, TX | CVS Pharmacy | $3,950,000 | 5.90% | 13,200 |
| 3 | CLOSED | Katy, TX | Walgreens | $4,100,000 | 5.80% | 15,000 |
| 4 | IN_ESCROW | Houston, TX | CVS Pharmacy | $3,800,000 | 6.00% | 12,500 |
| 5 | IN_ESCROW | Pearland, TX | Walgreens | $4,000,000 | 5.85% | 14,200 |
| 6 | ON_MARKET | Spring, TX | CVS Pharmacy | $3,900,000 | 6.10% | 13,800 |

### 6.2 Individual Case Study Detail Page
| Field | Value |
|-------|-------|
| `case_study_property_name` | "Walgreens - Sugar Land" |
| `case_study_city_state` | "Sugar Land, TX" |
| `case_study_image` | [Walgreens store image] |
| `challenges_title` | "Challenges" |
| `challenge_1` | "Competitive pharmacy market with multiple national chains" |
| `challenge_2` | "High construction costs for modern pharmacy layouts" |
| `challenge_3` | "Regulatory requirements for pharmacy operations" |
| `marketing_strategy_title` | "Marketing Strategy" |
| `strategy_1` | "Targeted institutional investors seeking stable NNN income" |
| `strategy_2` | "Emphasized prime corner location and high traffic counts" |
| `strategy_3` | "Highlighted Fortune 500 tenant credit quality" |
| `results_title` | "Results" |
| `result_1` | "Multiple competitive offers received within 30 days" |
| `result_2` | "Sold at 5.75% cap rate, 50 basis points below market" |
| `result_3` | "Transaction closed in 45 days with minimal due diligence" |
| `result_4` | "Achieved premium pricing due to tenant credit and location" |
| `case_study_description` | "This Walgreens pharmacy investment represented an exceptional opportunity in the competitive Houston market. The property's prime corner location, combined with the tenant's investment-grade credit rating, attracted significant investor interest and resulted in a premium sale price." |
| `sale_price` | 4,200,000 |
| `square_footage` | 14,800 |


## 7. Broker Biography Section

### 7.1 Page Header
| Field | Value |
|-------|-------|
| `page_title` | "BROKER BIOGRAPHY" |
| `company_logo` | [SRS Capital Markets logo] |

### 7.2 Broker Information Fields
| Field | Value |
|-------|-------|
| `broker_name` | "JOHN SMITH, CCIM" |
| `broker_title` | "Managing Principal" |
| `broker_division` | "National Net Lease | Houston, TX" |
| `broker_phone_direct` | "D: 713.555.0123" |
| `broker_phone_mobile` | "M: 713.555.0456" |
| `broker_email` | "john.smith@srsre.com" |
| `broker_photo` | [John Smith professional headshot] |

### 7.3 Experience Section
| Field | Value |
|-------|-------|
| `experience_title` | "Experience" |
| `experience_text` | "John joined SRS in 2018 with more than 8 years of transactional brokerage experience in the commercial real estate industry and over $750 million in closed transactions, representing over 200 individual properties. John specializes in retail pharmacy and healthcare properties, focusing on single-tenant, NNN-leased investments including national portfolios, merchant developer representation, sale-leasebacks, and lease restructuring throughout the Texas market." |

### 7.4 Community/Personal Section
| Field | Value |
|-------|-------|
| `community_title` | "Community/Personal Information" |
| `community_text` | "John was recognized as a top retail pharmacy broker in the Houston market in 2022. He is an active member of the International Council of Shopping Centers (ICSC) and CCIM communities and enjoys golfing and spending time with his family in his free time." |