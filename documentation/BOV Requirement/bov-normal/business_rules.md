# Business Rules for BOV Sections

## Case Studies
- **Title Default**: If not provided, use "Case Studies" as default title.
- **Content Requirements**: Each case study should highlight key property features, tenant strength, or location advantages.
- **Image Requirements**: Images must be JPG/PNG format, max 5MB each, recommended 800x600 resolution.
- **Content Guidelines**:
  - Focus on 3 most compelling property attributes
  - Keep descriptions concise but informative
  - Use professional, marketing-oriented language
  - Highlight tenant credit quality and lease terms

## Comparables
- **Time Window**: Default window: past 24 months. If fewer than 3 comps, extend to 36 months.
- **State Normalization**: Normalize state to uppercase 2-letter US code.
- **Data Quality**: Incomplete comps (missing building_sf or sale_date) should be flagged for manual review.
- **Prioritization Order**: (1) same submarket, (2) same MSA, (3) ±25% building size, (4) similar lease type.
- **Calculations**:
  - `rent_per_sf_per_yr = annual_rent / building_sf`
  - `price_per_sf = sale_price / building_sf`
  - `cap_rate = (annual_rent / sale_price) * 100`

## Rent Roll
- **Lease End Dates**: Lease_end may be null/TBD but should be flagged.
- **Rent Calculations**: 
  - If monthly_rent present but annual_rent missing → auto-calculate: `annual_rent = monthly_rent * 12`
  - If both present but mismatch >1% → flag inconsistency
- **Risk Assessment**: If one tenant occupies >90% of building and lease term remaining <1 year → risk flag.
- **Lease Term Calculation**: `lease_term_remaining = (lease_end - current_date) / 365.25`

## Pricing Summary
- **Currency Formatting**: Show values in USD, formatted with commas (e.g., $[amount]).
- **Cap Rate Validation**: Cap rates must be within 0–100%.
- **Value Matrix**: If value_matrix not provided → note "Client to provide valuation figures."
- **NOI Calculations**:
  - `net_operating_income = total_annual_rent - operating_expenses`
  - `property_value = net_operating_income / (cap_rate / 100)`
- **Price Range Logic**:
  - `go_to_market_price` = highest reasonable asking price
  - `strike_price` = expected sale price
  - `value_floor` = minimum acceptable price

### Broker Biography
- **Required Fields**: broker_name, broker_title, broker_division, broker_email, broker_photo, experience_text
- **Phone Format**: Direct and mobile phones must follow "D: XXX.XXX.XXXX" and "M: XXX.XXX.XXXX" format
- **Email Validation**: Must be valid email format
- **Photo Requirements**: Professional headshot, JPG/PNG, max 5MB

## General
- **Date Format**: Dates must use ISO format (YYYY-MM-DD).
- **Address Normalization**: All addresses normalized to Title Case.
- **Error Handling**: Validation errors must be returned as structured JSON with field, issue, severity.
- **Image Requirements**: Property images must be JPG/PNG format, max 3 images, each <5MB.
