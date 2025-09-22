# Validation Rules & Error Messages

## Standard Messages
- **Missing required field** → "The field '{field}' is required in section {section}."
- **Invalid format** → "Invalid format for '{field}': '{value}'. Expected format: {expected}."
- **Out of range** → "Value out of range for '{field}': {value}. Allowed range: {min}–{max}."
- **Inconsistent fields** → "Inconsistency detected: '{field_a}' ({value_a}) vs '{field_b}' ({value_b}). Review required."
- **Incomplete row** → "Row {row}: Incomplete data. Missing fields: {fields_missing}."

## Field-Specific Validation Rules

### Cover Page
- `presented_to`: Required, max 120 chars, cannot be empty
- `property_name`: Required, max 120 chars, cannot be empty
- `property_address`: Required, must include street, city, state, ZIP
- `report_date`: Required, ISO format (YYYY-MM-DD), cannot be future date

### Property Overview
- `property_type`: Required, must be one of {Retail, Office, Industrial, Medical}
- `year_built`: Optional, must be between 1800 and current year
- `rentable_area_sf`: Required, must be > 0
- `land_acres`: Optional, must be ≥ 0
- `tenant_name`: Required, max 120 chars

### Case Studies
- `case_study_title`: Required, max 100 chars, default: "Case Studies"
- `case_study_1_title`: Optional, max 80 chars
- `case_study_1_desc`: Optional, max 300 chars
- `case_study_1_image`: Optional, must be valid JPG/PNG file
- `case_study_2_title`: Optional, max 80 chars
- `case_study_2_desc`: Optional, max 300 chars
- `case_study_2_image`: Optional, must be valid JPG/PNG file
- `case_study_3_title`: Optional, max 80 chars
- `case_study_3_desc`: Optional, max 300 chars
- `case_study_3_image`: Optional, must be valid JPG/PNG file

### Comparables
- `comp_id`: Required, must be unique per BOV
- `property_name`: Required, max 120 chars
- `address`: Required, must include street, city, state, ZIP
- `state`: Required, must be 2-letter US state code
- `sale_date`: Optional, must be ≤ report_date
- `sale_price`: Optional, must be ≥ 0
- `building_sf`: Optional, must be > 0
- `cap_rate`: Optional, must be between 0-100
- `source`: Required, must be one of {CoStar, LoopNet, Client, Broker, ThirdParty}

### Rent Roll
- `tenant_name`: Required, max 120 chars
- `leased_sf`: Required, must be > 0
- `lease_start`: Required, valid date
- `lease_end`: Required, must be ≥ lease_start
- `monthly_rent`: Required, must be ≥ 0
- `annual_rent`: Optional, if provided must match monthly_rent * 12 (±1%)
- `rent_type`: Required, must be one of {NNN, Gross, Modified}

### Pricing Summary
- `asking_price`: Optional, must be ≥ 0
- `net_operating_income`: Optional, must be ≥ 0
- `cap_rate`: Optional, must be between 0-100
- `go_to_market_price`: Optional, must be ≥ 0
- `strike_price`: Optional, must be ≥ 0
- `value_floor`: Optional, must be ≥ 0

## Example JSON Error Response
```json
{
  "errors": [
    {
      "section": "Comparables",
      "field": "state",
      "value": "Texas",
      "message": "Invalid state code: 'Texas'. Expected 2-letter code (e.g., TX).",
      "severity": "error"
    },
    {
      "section": "Rent Roll",
      "field": "lease_end",
      "value": "2019-01-01",
      "message": "Invalid lease dates: lease_end precedes lease_start.",
      "severity": "error"
    },
    {
      "section": "Rent Roll",
      "field": "annual_rent",
      "value": "180000",
      "message": "Inconsistency detected: 'annual_rent' (180000) vs calculated value (174000). Review required.",
      "severity": "warning"
    }
  ]
}
```
