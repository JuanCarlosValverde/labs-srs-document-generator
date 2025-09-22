# Example C: Medical Office (Urgent Care)

## Field Mapping Annotations
This example demonstrates a single-tenant medical office property with NNN lease structure based on actual PDF template structure.

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
| `sold_section_title` | "Medical Office (Dallas) - Sold Comparables - Trailing 2 Years" |
| `comp_id` | "COMP003" |
| `property_name` | "Urgent Care Dallas" |
| `property_address` | "411 Elm St, Dallas, TX 75202" |
| `city` | "Dallas" |
| `state` | "TX" |
| `sale_date` | "2024-04-01" |
| `sale_price` | 3,600,000 |
| `lease_term_remaining` | 5 |
| `year_built` | 2019 |
| `building_sf` | 8,500 |
| `land_acres` | 0.50 |
| `annual_rent` | 324,000 |
| `rent_per_sf_per_yr` | 38.12 |
| `price_per_sf` | 423.53 |
| `cap_rate` | 6.10 |
| `market_time_days` | 60 |

### 3.2 On Market Comparables Section
| Field | Value |
|-------|-------|
| `onmarket_section_title` | "Medical Office (Texas) - On Market Comparables" |
| `asking_price` | 3,750,000 |
| `subject_property_flag` | true |

## 4. Rent Roll

### 4.1 Lease Term & Rental Rates Table
| Field | Value |
|-------|-------|
| `tenant_name` | "Urgent Care Group" |
| `square_feet` | 8,500 |
| `lease_start` | "2019-01-01" |
| `lease_end` | "2029-12-31" |
| `begin_period` | "Current" |
| `increase_rate` | 0 |
| `monthly_rent` | 27,000 |
| `annual_rent` | 324,000 |
| `recovery_type` | "NNN" |
| `options` | "-" |
| `rofr_note` | "Tenant Has a 20-Day Right Of First Refusal (ROFR)" |

### 4.2 Financial Information Section
| Field | Value |
|-------|-------|
| `price` | 1,690,000 |
| `net_operating_income` | 324,000 |
| `cap_rate` | 6.10 |
| `lease_type` | "NNN" |

### 4.3 Value Matrix Section
| Field | Value |
|-------|-------|
| `go_to_market_rate` | 6.10 |
| `go_to_market_price` | 1,690,000 |
| `strike_price_rate` | 6.35 |
| `strike_price` | 1,600,000 |
| `value_floor_rate` | 6.60 |
| `value_floor` | 1,520,000 |

### 4.4 Property Specifications Section
| Field | Value |
|-------|-------|
| `year_built` | 2019 |
| `rentable_area` | 8,500 |
| `land_area` | 0.50 |
| `property_address` | "411 Elm St, Dallas, TX 75202" |

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

## 6. Case Studies

### 6.1 Case Studies Grid (6 Properties)
| Property | Status | City/State | Property Name | Price | Cap Rate | SF |
|----------|--------|------------|---------------|-------|----------|-----|
| 1 | CLOSED | Dallas, TX | Urgent Care | $3,600,000 | 6.10% | 8,500 |
| 2 | CLOSED | Plano, TX | Family Clinic | $3,400,000 | 6.25% | 9,000 |
| 3 | CLOSED | Frisco, TX | Urgent Care | $3,500,000 | 6.15% | 8,200 |
| 4 | IN_ESCROW | McKinney, TX | Medical Office | $3,300,000 | 6.30% | 7,800 |
| 5 | IN_ESCROW | Allen, TX | Urgent Care | $3,450,000 | 6.20% | 8,600 |
| 6 | ON_MARKET | Richardson, TX | Family Clinic | $3,350,000 | 6.35% | 8,000 |

### 6.2 Individual Case Study Detail Page
| Field | Value |
|-------|-------|
| `case_study_property_name` | "Urgent Care - Dallas" |
| `case_study_city_state` | "Dallas, TX" |
| `case_study_image` | [Urgent Care facility image] |
| `challenges_title` | "Challenges" |
| `challenge_1` | "Competitive medical office market with multiple healthcare providers" |
| `challenge_2` | "High construction costs for medical-grade facilities" |
| `challenge_3` | "Regulatory compliance requirements for healthcare facilities" |
| `marketing_strategy_title` | "Marketing Strategy" |
| `strategy_1` | "Targeted healthcare-focused investors and medical REITs" |
| `strategy_2` | "Emphasized Dallas Medical District location and hospital proximity" |
| `strategy_3` | "Highlighted established healthcare operator with multiple locations" |
| `results_title` | "Results" |
| `result_1` | "Multiple competitive offers received within 25 days" |
| `result_2` | "Sold at 6.10% cap rate, competitive for medical office market" |
| `result_3` | "Transaction closed in 60 days with comprehensive due diligence" |
| `result_4` | "Achieved strong pricing due to location and tenant stability" |
| `case_study_description` | "This Urgent Care investment represented a solid opportunity in the competitive Dallas medical office market. The property's location in the Dallas Medical District, combined with the established healthcare operator and modern facility design, attracted significant investor interest and resulted in a competitive sale price." |
| `sale_price` | 3,600,000 |
| `square_footage` | 8,500 |


## 7. Broker Biography Section

### 7.1 Page Header
| Field | Value |
|-------|-------|
| `page_title` | "BROKER BIOGRAPHY" |
| `company_logo` | [SRS Capital Markets logo] |

### 7.2 Broker Information Fields
| Field | Value |
|-------|-------|
| `broker_name` | "DAVID JOHNSON, CCIM" |
| `broker_title` | "Managing Principal" |
| `broker_division` | "National Net Lease | Dallas, TX" |
| `broker_phone_direct` | "D: 214.555.0123" |
| `broker_phone_mobile` | "M: 214.555.0456" |
| `broker_email` | "david.johnson@srsre.com" |
| `broker_photo` | [David Johnson professional headshot] |

### 7.3 Experience Section
| Field | Value |
|-------|-------|
| `experience_title` | "Experience" |
| `experience_text` | "David joined SRS in 2020 with more than 7 years of transactional brokerage experience in the commercial real estate industry and over $600 million in closed transactions, representing over 180 individual properties. David specializes in medical office and healthcare properties, focusing on single-tenant, NNN-leased investments including national portfolios, merchant developer representation, sale-leasebacks, and lease restructuring throughout the Texas market." |

### 7.4 Community/Personal Section
| Field | Value |
|-------|-------|
| `community_title` | "Community/Personal Information" |
| `community_text` | "David was recognized as a top medical office broker in the Dallas market in 2023. He is an active member of the International Council of Shopping Centers (ICSC) and CCIM communities and enjoys tennis and volunteering at local healthcare charities in his free time." |
