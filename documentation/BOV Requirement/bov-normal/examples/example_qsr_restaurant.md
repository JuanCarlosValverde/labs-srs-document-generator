# Example B: Quick Service Restaurant (Taco Bell)

## Field Mapping Annotations
This example demonstrates a single-tenant QSR property with NNN lease structure and drive-through based on actual PDF template structure.

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
| `sold_section_title` | "QSR (South) - Sold Comparables - Trailing 2 Years" |
| `comp_id` | "COMP002" |
| `property_name` | "Taco Bell San Antonio" |
| `property_address` | "1555 Broadway, San Antonio, TX 78215" |
| `city` | "San Antonio" |
| `state` | "TX" |
| `sale_date` | "2024-08-20" |
| `sale_price` | 2,150,000 |
| `lease_term_remaining` | 16 |
| `year_built` | 2020 |
| `building_sf` | 2,700 |
| `land_acres` | 0.75 |
| `annual_rent` | 174,000 |
| `rent_per_sf_per_yr` | 64.44 |
| `price_per_sf` | 796.30 |
| `cap_rate` | 6.25 |
| `market_time_days` | 35 |

### 3.2 On Market Comparables Section
| Field | Value |
|-------|-------|
| `onmarket_section_title` | "QSR (Texas) - On Market Comparables" |
| `asking_price` | 2,250,000 |
| `subject_property_flag` | true |

## 4. Rent Roll

### 4.1 Lease Term & Rental Rates Table
| Field | Value |
|-------|-------|
| `tenant_name` | "Taco Bell" |
| `square_feet` | 2,700 |
| `lease_start` | "2020-06-01" |
| `lease_end` | "2040-05-31" |
| `begin_period` | "Current" |
| `increase_rate` | 0 |
| `monthly_rent` | 14,500 |
| `annual_rent` | 174,000 |
| `recovery_type` | "NNN" |
| `options` | "-" |
| `rofr_note` | "Tenant Has a 20-Day Right Of First Refusal (ROFR)" |

### 4.2 Financial Information Section
| Field | Value |
|-------|-------|
| `price` | 1,690,000 |
| `net_operating_income` | 174,000 |
| `cap_rate` | 6.25 |
| `lease_type` | "NNN" |

### 4.3 Value Matrix Section
| Field | Value |
|-------|-------|
| `go_to_market_rate` | 6.25 |
| `go_to_market_price` | 1,690,000 |
| `strike_price_rate` | 6.50 |
| `strike_price` | 1,600,000 |
| `value_floor_rate` | 6.75 |
| `value_floor` | 1,520,000 |

### 4.4 Property Specifications Section
| Field | Value |
|-------|-------|
| `year_built` | 2020 |
| `rentable_area` | 2,700 |
| `land_area` | 0.75 |
| `property_address` | "1555 Broadway, San Antonio, TX 78215" |

## 5. Pricing Summary
| Field | Value |
|-------|-------|
| `asking_price` | 2,250,000 |
| `net_operating_income` | 174,000 |
| `cap_rate` | 6.20 |
| `lease_type` | "NNN" |
| `value_matrix` | [{"cap_rate": 6.20, "price": 2250000}, {"cap_rate": 6.50, "price": 2150000}] |
| `go_to_market_price` | 2,150,000 |
| `strike_price` | 2,050,000 |
| `value_floor` | 1,950,000 |
| `valuation_notes` | "High-traffic location with drive-through service. Modern building with excellent visibility and access." |

## 6. Case Studies

### 6.1 Case Studies Grid (6 Properties)
| Property | Status | City/State | Property Name | Price | Cap Rate | SF |
|----------|--------|------------|---------------|-------|----------|-----|
| 1 | CLOSED | San Antonio, TX | Taco Bell | $2,150,000 | 6.25% | 2,700 |
| 2 | CLOSED | Austin, TX | Burger King | $2,050,000 | 6.40% | 2,800 |
| 3 | CLOSED | Houston, TX | Taco Bell | $2,200,000 | 6.15% | 2,600 |
| 4 | IN_ESCROW | Dallas, TX | McDonald's | $2,100,000 | 6.30% | 2,900 |
| 5 | IN_ESCROW | Fort Worth, TX | Taco Bell | $2,180,000 | 6.20% | 2,750 |
| 6 | ON_MARKET | Plano, TX | Burger King | $2,120,000 | 6.35% | 2,850 |

### 6.2 Individual Case Study Detail Page
| Field | Value |
|-------|-------|
| `case_study_property_name` | "Taco Bell - San Antonio" |
| `case_study_city_state` | "San Antonio, TX" |
| `case_study_image` | [Taco Bell store image] |
| `challenges_title` | "Challenges" |
| `challenge_1` | "Competitive QSR market with multiple national brands" |
| `challenge_2` | "High construction costs for drive-through facilities" |
| `challenge_3` | "Labor shortage affecting QSR operations" |
| `marketing_strategy_title` | "Marketing Strategy" |
| `strategy_1` | "Targeted QSR-focused investors and 1031 exchange buyers" |
| `strategy_2` | "Emphasized high-traffic Broadway location and drive-through" |
| `strategy_3` | "Highlighted YUM! Brands corporate backing and brand strength" |
| `results_title` | "Results" |
| `result_1` | "Multiple offers received within 20 days of listing" |
| `result_2` | "Sold at 6.25% cap rate, competitive for QSR market" |
| `result_3` | "Transaction closed in 35 days with streamlined due diligence" |
| `result_4` | "Achieved strong pricing due to location and tenant quality" |
| `case_study_description` | "This Taco Bell investment represented a strong opportunity in the competitive San Antonio QSR market. The property's high-traffic Broadway location, combined with the modern drive-through configuration and YUM! Brands backing, attracted significant investor interest and resulted in a competitive sale price." |
| `sale_price` | 2,150,000 |
| `square_footage` | 2,700 |


## 7. Broker Biography Section

### 7.1 Page Header
| Field | Value |
|-------|-------|
| `page_title` | "BROKER BIOGRAPHY" |
| `company_logo` | [SRS Capital Markets logo] |

### 7.2 Broker Information Fields
| Field | Value |
|-------|-------|
| `broker_name` | "MARIA RODRIGUEZ" |
| `broker_title` | "Managing Principal" |
| `broker_division` | "National Net Lease | San Antonio, TX" |
| `broker_phone_direct` | "D: 210.555.0123" |
| `broker_phone_mobile` | "M: 210.555.0456" |
| `broker_email` | "maria.rodriguez@srsre.com" |
| `broker_photo` | [Maria Rodriguez professional headshot] |

### 7.3 Experience Section
| Field | Value |
|-------|-------|
| `experience_title` | "Experience" |
| `experience_text` | "Maria joined SRS in 2019 with more than 6 years of transactional brokerage experience in the commercial real estate industry and over $500 million in closed transactions, representing over 150 individual properties. Maria specializes in QSR and restaurant properties, focusing on single-tenant, NNN-leased investments including national portfolios, merchant developer representation, and sale-leasebacks throughout the Texas market." |
