# Business Rules - Simplified Version

## General Rules
- **Date Format**: Dates must use ISO format (YYYY-MM-DD)
- **Address Normalization**: All addresses normalized to Title Case
- **Error Handling**: Validation errors must be returned as structured JSON with field, issue, severity
- **Image Requirements**: Property images must be JPG/PNG format, max 3 images, each <5MB

## Manual Input Sections

### Cover Page
- **Required Fields**: bov_title, tenant_name, property_address, presented_to, client_name, property_image
- **Optional Fields**: client_title, client_company
- **Validation**: 
  - All text fields ≤120 chars (except client_title, client_company ≤100 chars)
  - property_address must include street, city, state, ZIP
  - property_image must be valid JPG/PNG format

### Table of Contents
- **Required Fields**: toc_background_image, page_3_title, page_3_subitems, page_5_title, page_5_subitems, page_18_title, page_18_subitems, page_21_title, page_21_subitems
- **Static Content**: All titles and subitems are predefined with default values
- **Background Image**: Must be valid JPG/PNG file
- **Default Values**:
  - page_3_title: "Property Overview"
  - page_3_subitems: "Comparables | Rent Roll | Pricing Summary"
  - page_5_title: "National Net Lease"
  - page_5_subitems: "Team Overview"
  - page_18_title: "Marketing Strategy"
  - page_18_subitems: "& Timeline"
  - page_21_title: "SRS Real Estate Partners"
  - page_21_subitems: "Overview"

### Broker Biography
- **Page Header Fields**: page_title, company_logo
- **Required Fields**: broker_name, broker_title, broker_division, broker_email, broker_photo, experience_text
- **Optional Fields**: broker_phone_direct, broker_phone_mobile, community_text
- **Phone Format**: Direct and mobile phones must follow "D: XXX.XXX.XXXX" and "M: XXX.XXX.XXXX" format
- **Email Validation**: Must be valid email format
- **Photo Requirements**: Professional headshot, JPG/PNG, max 5MB
- **Default Values**:
  - page_title: "BROKER BIOGRAPHY"
  - experience_title: "Experience"
  - community_title: "Community/Personal Information"

## Auto-Generated Sections (from CSV)

### Comparables
- **Required Fields**: sold_section_title, onmarket_section_title
- **Auto-Generated Titles**: Based on property type (e.g., "Medical Office (Dallas) - Sold Comparables - Trailing 2 Years")
- **Time Window**: Default window: past 24 months. If fewer than 3 comps, extend to 36 months
- **State Normalization**: Normalize state to uppercase 2-letter US code
- **Data Quality**: Incomplete comps (missing building_sf or sale_date) should be flagged for manual review
- **Prioritization Order**: (1) same submarket, (2) same MSA, (3) ±25% building size, (4) similar lease type
- **Calculations**:
  - `rent_per_sf_per_yr = annual_rent / building_sf`
  - `price_per_sf = sale_price / building_sf`
  - `cap_rate = (annual_rent / sale_price) * 100`

### Rent Roll
- **Required Fields**: rent_roll_title
- **Default Title**: "Lease Term & Rental Rates"
- **Lease End Dates**: Lease_end may be null/TBD but should be flagged
- **Rent Calculations**: 
  - If monthly_rent present but annual_rent missing → auto-calculate: `annual_rent = monthly_rent * 12`
  - If both present but mismatch >1% → flag inconsistency
- **Risk Assessment**: If one tenant occupies >90% of building and lease term remaining <1 year → risk flag
- **Lease Term Calculation**: `lease_term_remaining = (lease_end - current_date) / 365.25`

### Pricing Summary
- **Required Fields**: pricing_title
- **Default Title**: "Pricing Summary"
- **Auto-Generated**: All pricing data (price, NOI, cap rates, value matrix, etc.) is generated automatically from CSV input
- **Data Source**: Pricing information comes from client CSV data, no manual calculations required

### Case Studies
- **Required Fields**: case_studies_title
- **Default Title**: "Case Studies"
- **Content Requirements**: Each case study should highlight key property features, tenant strength, or location advantages
- **Image Requirements**: Images must be JPG/PNG format, max 5MB each, recommended 800x600 resolution
- **Content Guidelines**:
  - Focus on 3 most compelling property attributes
  - Keep descriptions concise but informative
  - Use professional, marketing-oriented language
  - Highlight tenant credit quality and lease terms
