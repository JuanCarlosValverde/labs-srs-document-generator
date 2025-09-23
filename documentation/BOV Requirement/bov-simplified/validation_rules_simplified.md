# Validation Rules - Simplified Version

## Standard Messages
- **Missing required field** → "The field '{field}' is required in section {section}."
- **Invalid format** → "Invalid format for '{field}': '{value}'. Expected format: {expected}."
- **Out of range** → "Value out of range for '{field}': {value}. Allowed range: {min}–{max}."
- **Inconsistent fields** → "Inconsistency detected: '{field_a}' ({value_a}) vs '{field_b}' ({value_b}). Review required."

## Field-Specific Validation Rules

### Cover Page
- `presented_to`: Required, max 120 chars, cannot be empty
- `tenant_name`: Required, max 120 chars, cannot be empty
- `property_address`: Required, must include street, city, state, ZIP
- `client_name`: Required, max 120 chars
- `client_title`: Optional, max 100 chars
- `client_company`: Optional, max 100 chars
- `property_image`: Required, must be valid JPG/PNG file

### Table of Contents
- `toc_background_image`: Required, must be valid JPG/PNG file
- All page titles and subitems: Static values, no validation needed

### Investment Highlights
- `investment_highlights_title`: Required, default: "INVESTMENT HIGHLIGHTS"
- `highlight_section_1_title`: Optional, max 100 chars
- `highlight_section_1_point_1`: Optional, max 300 chars
- `highlight_section_1_point_2`: Optional, max 300 chars
- `highlight_section_2_title`: Optional, max 100 chars
- `highlight_section_2_point_1`: Optional, max 300 chars
- `highlight_section_2_point_2`: Optional, max 300 chars
- `highlight_section_3_title`: Optional, max 100 chars
- `highlight_section_3_point_1`: Optional, max 300 chars
- `highlight_section_3_point_2`: Optional, max 300 chars
- `highlight_section_4_title`: Optional, max 100 chars
- `highlight_section_4_point_1`: Optional, max 300 chars
- `highlight_section_4_point_2`: Optional, max 300 chars
- `highlight_section_5_title`: Optional, max 100 chars
- `highlight_section_5_point_1`: Optional, max 300 chars
- `highlight_section_5_point_2`: Optional, max 300 chars

### Broker Biography
- `broker_name`: Required, max 100 chars
- `broker_title`: Required, max 100 chars
- `broker_division`: Required, max 100 chars
- `broker_phone_direct`: Optional, format: "D: XXX.XXX.XXXX"
- `broker_phone_mobile`: Optional, format: "M: XXX.XXX.XXXX"
- `broker_email`: Required, valid email format
- `broker_photo`: Required, JPG/PNG file, max 5MB
- `experience_text`: Required, max 3000 chars
- `community_text`: Optional, max 1500 chars
- `education_title`: Required, default: "Education"
- `education_text`: Optional, max 1500 chars
- `transactions_title`: Required, default: "Notable Transactions"
- `transaction_1`: Optional, max 200 chars
- `transaction_2`: Optional, max 200 chars
- `transaction_3`: Optional, max 200 chars
- `transaction_4`: Optional, max 200 chars
- `transaction_5`: Optional, max 200 chars

## Auto-Generated Sections (CSV Validation)

### Comparables (from CSV)
- `comp_id`: Required, must be unique per BOV
- `property_name`: Required, max 120 chars
- `address`: Required, must include street, city, state, ZIP
- `state`: Required, must be 2-letter US state code
- `sale_date`: Optional, must be ≤ report_date
- `sale_price`: Optional, must be ≥ 0
- `building_sf`: Optional, must be > 0
- `cap_rate`: Optional, must be between 0-100

### Rent Roll (from CSV)
- `tenant_name`: Required, max 120 chars
- `leased_sf`: Required, must be > 0
- `lease_start`: Required, valid date
- `lease_end`: Required, must be ≥ lease_start
- `monthly_rent`: Required, must be ≥ 0
- `annual_rent`: Optional, if provided must match monthly_rent * 12 (±1%)
- `rent_type`: Required, must be one of {NNN, Gross, Modified}

### Case Studies (from CSV)
- `case_study_title`: Required, max 100 chars, default: "Case Studies"
- `case_study_image`: Optional, must be valid JPG/PNG file
- `case_study_description`: Optional, max 1000 chars

## Example JSON Error Response
```json
{
  "errors": [
    {
      "section": "Cover Page",
      "field": "property_address",
      "value": "123 Main St",
      "message": "Invalid address format: missing city, state, or ZIP code.",
      "severity": "error"
    },
    {
      "section": "Broker Biography",
      "field": "broker_phone_direct",
      "value": "713-555-0123",
      "message": "Invalid phone format: '713-555-0123'. Expected format: 'D: XXX.XXX.XXXX'.",
      "severity": "error"
    }
  ]
}
```
