# BOV Content Specification

This repository contains comprehensive documentation for Broker Opinion of Value (BOV) template requirements for ADK document generation.

## 📋 Acceptance Criteria Status

- ✅ **Complete field mapping document** - All BOV fields identified with data types, required/optional status, validation rules, and sources
- ✅ **Business rules documented** - All calculations (cap rates, NOI, etc.) with formulas and logic
- ✅ **3 sample BOV templates annotated** - Field mappings demonstrated with real-world examples
- ✅ **Validation criteria defined** - Field-specific validation rules with error message templates
- ✅ **Documentation stored in repository** - All files organized and accessible

## 📁 Repository Contents

### Core Documentation
- **`bov_field_mapping.md`** → Master field definitions (data type, required/optional, validation, source)
- **`business_rules.md`** → Business rules for comparables, rent roll, and pricing summary with calculation formulas
- **`validation_rules.md`** → Comprehensive validation rules and error message templates

### Examples
- **`examples/example_retail_pharmacy.md`** → Walgreens pharmacy with field mapping annotations
- **`examples/example_qsr_restaurant.md`** → Taco Bell restaurant with field mapping annotations  
- **`examples/example_medical_office.md`** → Urgent care facility with field mapping annotations

### Templates
- **`templates/`** → PDF template files provided by client for reference

## 🚀 Usage for ADK Implementation

1. **CSV Schema**: Use field definitions from `bov_field_mapping.md` to structure input data
2. **Validation**: Apply rules from `validation_rules.md` before document generation
3. **Calculations**: Implement business logic from `business_rules.md` for automated calculations
4. **Examples**: Reference annotated examples for proper field mapping and data structure

## 📊 Field Coverage

The documentation covers all required sections based on actual PDF templates:
- **Cover Page** (8 fields)
- **Table of Contents** (9 fields)
- **Comparables** (19 fields - Sold + On Market sections)
- **Rent Roll** (25 fields - 4 subsections)
- **Pricing Summary** (9 fields)
- **Case Studies** (66 fields - Grid + Detail pages)

**Total: 136 fields** with complete validation and business rule coverage.
