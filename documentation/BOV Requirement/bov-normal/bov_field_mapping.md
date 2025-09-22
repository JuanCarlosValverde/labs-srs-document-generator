# BOV Field Mapping

This document defines all fields required in BOV templates for ADK generation based on actual PDF templates.  
Scope includes **Cover Page, Table of Contents, Property Overview (Comparables, Rent Roll, Pricing Summary), and Case Studies.**  
Sections from **National Net Lease onward are excluded** (static content in template).

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

## 3. Comparables

### 3.1 Sold Comparables Section
| Field                | Type     | Required | Validation                                    | Source   |
|----------------------|----------|----------|-----------------------------------------------|----------|
| sold_section_title   | string   | Yes      | Default: "Dental (South) - Sold Comparables - Trailing 2 Years" | Static |
| comp_id              | string   | Yes      | Unique per BOV                                | System   |
| property_name        | string   | Yes      | ≤120 chars                                    | CSV      |
| property_address     | string   | Yes      | Must include street, city, state, ZIP         | CSV      |
| city                 | string   | Yes      | ≤50 chars                                     | CSV      |
| state                | string   | Yes      | Must be 2-letter US code                      | CSV      |
| sale_date            | date     | No       | ≤ report_date                                 | CSV      |
| sale_price           | decimal  | No       | ≥0                                            | CSV      |
| lease_term_remaining | integer  | No       | ≥0 (years)                                    | CSV      |
| year_built           | integer  | No       | 1800 ≤ year ≤ current                         | CSV      |
| building_sf          | integer  | No       | >0                                            | CSV      |
| land_acres           | decimal  | No       | ≥0                                            | CSV      |
| annual_rent          | decimal  | No       | ≥0                                            | CSV      |
| rent_per_sf_per_yr   | decimal  | No       | ≥0                                            | CSV/Calc |
| price_per_sf         | decimal  | No       | ≥0                                            | CSV      |
| cap_rate             | decimal  | No       | 0–100                                         | CSV      |
| market_time_days     | integer  | No       | ≥0                                            | CSV      |

### 3.2 On Market Comparables Section
| Field                | Type     | Required | Validation                                    | Source   |
|----------------------|----------|----------|-----------------------------------------------|----------|
| onmarket_section_title| string  | Yes      | Default: "Dental (Texas) - On Market Comparables" | Static |
| asking_price         | decimal  | No       | ≥0                                            | CSV      |
| subject_property_flag| boolean | No       | True if this is the subject property           | CSV      |

---

## 4. Rent Roll

### 4.1 Lease Term & Rental Rates Table
| Field               | Type    | Required | Validation                                    | Source   |
|---------------------|---------|----------|-----------------------------------------------|----------|
| tenant_name         | string  | Yes      | ≤120 chars                                    | CSV      |
| square_feet         | int     | Yes      | >0                                            | CSV      |
| lease_start         | date    | Yes      | Valid date                                    | CSV      |
| lease_end           | date    | Yes      | ≥ lease_start                                 | CSV      |
| begin_period        | string  | No       | ≤50 chars (e.g., "Current", "1/1/2027 - 12/31/2030") | CSV |
| increase_rate       | decimal | No       | 0–100 (percentage)                           | CSV      |
| monthly_rent        | decimal | Yes      | ≥0                                            | CSV      |
| annual_rent         | decimal | Yes      | ≥0; check = monthly*12                        | CSV/Calc |
| recovery_type       | string  | Yes      | {NNN, Gross, Modified}                        | CSV      |
| options             | string  | No       | ≤200 chars                                    | CSV      |
| rofr_note           | text    | No       | ≤500 chars (e.g., "Tenant Has a 20-Day Right Of First Refusal") | CSV |

### 4.2 Financial Information Section
| Field                | Type     | Required | Validation                                | Source   |
|----------------------|----------|----------|-------------------------------------------|----------|
| price                | decimal  | Yes      | ≥0                                        | CSV      |
| net_operating_income | decimal  | Yes      | ≥0                                        | CSV      |
| cap_rate             | decimal  | Yes      | 0–100                                     | CSV      |
| lease_type           | enum     | Yes      | {NNN, Gross, Modified}                    | CSV      |

### 4.3 Value Matrix Section
| Field                | Type     | Required | Validation                                | Source   |
|----------------------|----------|----------|-------------------------------------------|----------|
| go_to_market_rate    | decimal  | Yes      | 0–100                                     | CSV      |
| go_to_market_price   | decimal  | Yes      | ≥0                                        | CSV      |
| strike_price_rate    | decimal  | Yes      | 0–100                                     | CSV      |
| strike_price         | decimal  | Yes      | ≥0                                        | CSV      |
| value_floor_rate     | decimal  | Yes      | 0–100                                     | CSV      |
| value_floor          | decimal  | Yes      | ≥0                                        | CSV      |

### 4.4 Property Specifications Section
| Field                | Type     | Required | Validation                                | Source   |
|----------------------|----------|----------|-------------------------------------------|----------|
| year_built           | integer  | No       | 1800 ≤ year ≤ current                     | CSV      |
| rentable_area        | integer  | Yes      | >0                                        | CSV      |
| land_area            | decimal  | No       | ≥0                                        | CSV      |
| property_address     | string   | Yes      | Must include street, city, state, ZIP     | CSV      |

---

## 5. Pricing Summary

| Field                | Type     | Required | Validation                                | Source   |
|----------------------|----------|----------|-------------------------------------------|----------|
| asking_price         | decimal  | No       | ≥0                                        | CSV      |
| net_operating_income | decimal  | No       | ≥0                                        | Client   |
| cap_rate             | decimal  | No       | 0–100                                     | Client   |
| lease_type           | enum     | No       | {NNN, Gross, Modified}                    | CSV      |
| value_matrix         | list     | No       | Must be valid JSON (cap_rate, price pairs)| Client   |
| go_to_market_price   | decimal  | No       | ≥0                                        | Client   |
| strike_price         | decimal  | No       | ≥0                                        | Client   |
| value_floor          | decimal  | No       | ≥0                                        | Client   |
| valuation_notes      | text     | No       | ≤1000 chars                               | Agent    |

---

## 6. Case Studies

### 6.1 Case Studies Grid (6 Properties)
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| case_study_status_1  | enum     | No       | {CLOSED, IN_ESCROW, ON_MARKET}                | Agent         |
| case_study_image_1   | image    | No       | Must be valid JPG/PNG file                    | Uploaded      |
| case_study_city_state_1| string | No       | ≤50 chars (e.g., "CITY, ST")                 | Agent         |
| case_study_property_name_1| string| No       | ≤80 chars                                     | Agent         |
| case_study_price_1   | decimal  | No       | ≥0                                            | Agent         |
| case_study_cap_rate_1| decimal | No       | 0–100                                         | Agent         |
| case_study_sf_1      | integer  | No       | >0                                            | Agent         |
| case_study_status_2  | enum     | No       | {CLOSED, IN_ESCROW, ON_MARKET}                | Agent         |
| case_study_image_2   | image    | No       | Must be valid JPG/PNG file                    | Uploaded      |
| case_study_city_state_2| string | No       | ≤50 chars                                     | Agent         |
| case_study_property_name_2| string| No       | ≤80 chars                                     | Agent         |
| case_study_price_2   | decimal  | No       | ≥0                                            | Agent         |
| case_study_cap_rate_2| decimal | No       | 0–100                                         | Agent         |
| case_study_sf_2      | integer  | No       | >0                                            | Agent         |
| case_study_status_3  | enum     | No       | {CLOSED, IN_ESCROW, ON_MARKET}                | Agent         |
| case_study_image_3   | image    | No       | Must be valid JPG/PNG file                    | Uploaded      |
| case_study_city_state_3| string | No       | ≤50 chars                                     | Agent         |
| case_study_property_name_3| string| No       | ≤80 chars                                     | Agent         |
| case_study_price_3   | decimal  | No       | ≥0                                            | Agent         |
| case_study_cap_rate_3| decimal | No       | 0–100                                         | Agent         |
| case_study_sf_3      | integer  | No       | >0                                            | Agent         |
| case_study_status_4  | enum     | No       | {CLOSED, IN_ESCROW, ON_MARKET}                | Agent         |
| case_study_image_4   | image    | No       | Must be valid JPG/PNG file                    | Uploaded      |
| case_study_city_state_4| string | No       | ≤50 chars                                     | Agent         |
| case_study_property_name_4| string| No       | ≤80 chars                                     | Agent         |
| case_study_price_4   | decimal  | No       | ≥0                                            | Agent         |
| case_study_cap_rate_4| decimal | No       | 0–100                                         | Agent         |
| case_study_sf_4      | integer  | No       | >0                                            | Agent         |
| case_study_status_5  | enum     | No       | {CLOSED, IN_ESCROW, ON_MARKET}                | Agent         |
| case_study_image_5   | image    | No       | Must be valid JPG/PNG file                    | Uploaded      |
| case_study_city_state_5| string | No       | ≤50 chars                                     | Agent         |
| case_study_property_name_5| string| No       | ≤80 chars                                     | Agent         |
| case_study_price_5   | decimal  | No       | ≥0                                            | Agent         |
| case_study_cap_rate_5| decimal | No       | 0–100                                         | Agent         |
| case_study_sf_5      | integer  | No       | >0                                            | Agent         |
| case_study_status_6  | enum     | No       | {CLOSED, IN_ESCROW, ON_MARKET}                | Agent         |
| case_study_image_6   | image    | No       | Must be valid JPG/PNG file                    | Uploaded      |
| case_study_city_state_6| string | No       | ≤50 chars                                     | Agent         |
| case_study_property_name_6| string| No       | ≤80 chars                                     | Agent         |
| case_study_price_6   | decimal  | No       | ≥0                                            | Agent         |
| case_study_cap_rate_6| decimal | No       | 0–100                                         | Agent         |
| case_study_sf_6      | integer  | No       | >0                                            | Agent         |

### 6.2 Individual Case Study Detail Page
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| case_study_property_name| string | Yes      | ≤120 chars                                    | Agent         |
| case_study_city_state| string   | Yes      | ≤50 chars                                     | Agent         |
| case_study_image     | image    | Yes      | Must be valid JPG/PNG file                    | Uploaded      |
| challenges_title     | string   | Yes      | Default: "Challenges"                         | Static        |
| challenge_1          | string   | No       | ≤200 chars                                    | Agent         |
| challenge_2          | string   | No       | ≤200 chars                                    | Agent         |
| challenge_3          | string   | No       | ≤200 chars                                    | Agent         |
| marketing_strategy_title| string| Yes      | Default: "Marketing Strategy"                 | Static        |
| strategy_1           | string   | No       | ≤200 chars                                    | Agent         |
| strategy_2           | string   | No       | ≤200 chars                                    | Agent         |
| strategy_3           | string   | No       | ≤200 chars                                    | Agent         |
| results_title        | string   | Yes      | Default: "Results"                            | Static        |
| result_1             | string   | No       | ≤200 chars                                    | Agent         |
| result_2             | string   | No       | ≤200 chars                                    | Agent         |
| result_3             | string   | No       | ≤200 chars                                    | Agent         |
| result_4             | string   | No       | ≤200 chars                                    | Agent         |
| case_study_description| text   | No       | ≤1000 chars                                   | Agent         |
| sale_price           | decimal  | No       | ≥0                                            | Agent         |
| square_footage       | integer  | No       | >0                                            | Agent         |

---

## 7. Broker Biography Section

### 7.1 Page Header
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| page_title           | string   | Yes      | Default: "BROKER BIOGRAPHY"                   | Static        |
| company_logo         | image    | Yes      | SRS Capital Markets logo                      | Static        |

### 7.2 Broker Information Fields (Based on screenshot)
| Field                | Type     | Required | Validation                                    | Source        |
|----------------------|----------|----------|-----------------------------------------------|---------------|
| broker_name          | string   | Yes      | e.g., "PATRICK R. LUTHER, CCIM"               | Agent/CSV     |
| broker_title         | string   | Yes      | e.g., "Managing Principal"                    | Agent/CSV     |
| broker_division      | string   | Yes      | e.g., "National Net Lease \| Newport Beach, CA" | Agent/CSV     |
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