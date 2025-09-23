"""
Data input schemas for SRS Document Generator
Defines the structure and validation rules for all data types
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from enum import Enum


class PropertyType(Enum):
    """Property types supported by the system"""

    MULTIFAMILY = "multifamily"
    OFFICE = "office"
    RETAIL = "retail"
    INDUSTRIAL = "industrial"
    MIXED_USE = "mixed_use"


class LeaseStatus(Enum):
    """Lease status options"""

    OCCUPIED = "occupied"
    VACANT = "vacant"
    PENDING = "pending"
    NOT_AVAILABLE = "not_available"


class TenantType(Enum):
    """Tenant type classifications"""

    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"
    RETAIL = "retail"
    OFFICE = "office"


@dataclass
class RentRollUnit:
    """Schema for rent roll unit data"""

    unit_id: str
    unit_number: str
    floor: Optional[int] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[float] = None
    square_footage: Optional[int] = None
    rent_amount: Optional[Decimal] = None
    lease_start_date: Optional[date] = None
    lease_end_date: Optional[date] = None
    lease_status: Optional[LeaseStatus] = None
    tenant_name: Optional[str] = None
    security_deposit: Optional[Decimal] = None
    pet_deposit: Optional[Decimal] = None
    parking_spaces: Optional[int] = None
    amenities: Optional[List[str]] = None
    notes: Optional[str] = None


@dataclass
class ComparableProperty:
    """Schema for comparable property data"""

    property_id: str
    property_name: str
    address: str
    city: str
    state: str
    zip_code: str
    property_type: PropertyType
    year_built: Optional[int] = None
    total_units: Optional[int] = None
    total_sqft: Optional[int] = None
    sale_price: Optional[Decimal] = None
    sale_date: Optional[date] = None
    price_per_sqft: Optional[Decimal] = None
    price_per_unit: Optional[Decimal] = None
    cap_rate: Optional[Decimal] = None
    noi: Optional[Decimal] = None
    occupancy_rate: Optional[Decimal] = None
    avg_rent_per_sqft: Optional[Decimal] = None
    amenities: Optional[List[str]] = None
    notes: Optional[str] = None


@dataclass
class OperatingExpense:
    """Schema for operating expense data"""

    expense_id: str
    category: str
    description: str
    amount: Decimal
    period_start: date
    period_end: date
    subcategory: Optional[str] = None
    vendor: Optional[str] = None
    invoice_number: Optional[str] = None
    payment_date: Optional[date] = None
    payment_method: Optional[str] = None
    recurring: bool = False
    notes: Optional[str] = None


@dataclass
class TenantInfo:
    """Schema for tenant demographic and lease data"""

    tenant_id: str
    tenant_name: str
    unit_id: str
    lease_start_date: date
    lease_end_date: date
    monthly_rent: Decimal
    security_deposit: Optional[Decimal] = None
    pet_deposit: Optional[Decimal] = None
    tenant_type: Optional[TenantType] = None
    age_range: Optional[str] = None
    household_size: Optional[int] = None
    income_range: Optional[str] = None
    employment_status: Optional[str] = None
    credit_score_range: Optional[str] = None
    move_in_date: Optional[date] = None
    move_out_date: Optional[date] = None
    lease_renewals: Optional[int] = None
    payment_history: Optional[List[Dict[str, Any]]] = None
    emergency_contact: Optional[str] = None
    notes: Optional[str] = None


@dataclass
class NOIDataPoint:
    """Schema for Net Operating Income data point"""

    period_start: date
    period_end: date
    gross_rental_income: Decimal
    operating_expenses: Decimal
    other_income: Optional[Decimal] = None
    total_income: Optional[Decimal] = None
    net_operating_income: Optional[Decimal] = None
    occupancy_rate: Optional[Decimal] = None
    avg_rent_per_sqft: Optional[Decimal] = None
    notes: Optional[str] = None


@dataclass
class MarketAnalysisData:
    """Schema for market analysis data"""

    market_id: str
    market_name: str
    geographic_area: str
    analysis_date: date
    property_type: PropertyType
    avg_sale_price: Optional[Decimal] = None
    avg_price_per_sqft: Optional[Decimal] = None
    avg_price_per_unit: Optional[Decimal] = None
    avg_cap_rate: Optional[Decimal] = None
    avg_occupancy_rate: Optional[Decimal] = None
    avg_rent_per_sqft: Optional[Decimal] = None
    market_trends: Optional[List[str]] = None
    economic_indicators: Optional[Dict[str, Any]] = None
    demographics: Optional[Dict[str, Any]] = None
    competition_analysis: Optional[List[str]] = None
    notes: Optional[str] = None


# Data dictionaries for field documentation
RENT_ROLL_FIELDS = {
    "unit_id": "Unique identifier for the unit",
    "unit_number": "Unit number or identifier",
    "floor": "Floor number where the unit is located",
    "bedrooms": "Number of bedrooms in the unit",
    "bathrooms": "Number of bathrooms (can be fractional)",
    "square_footage": "Total square footage of the unit",
    "rent_amount": "Monthly rent amount",
    "lease_start_date": "Start date of the current lease",
    "lease_end_date": "End date of the current lease",
    "lease_status": "Current status of the lease (occupied, vacant, pending, not_available)",
    "tenant_name": "Name of the current tenant",
    "security_deposit": "Security deposit amount",
    "pet_deposit": "Pet deposit amount if applicable",
    "parking_spaces": "Number of parking spaces assigned to the unit",
    "amenities": "List of amenities included with the unit",
    "notes": "Additional notes about the unit",
}

COMPARABLES_FIELDS = {
    "property_id": "Unique identifier for the comparable property",
    "property_name": "Name of the property",
    "address": "Street address",
    "city": "City",
    "state": "State",
    "zip_code": "ZIP code",
    "property_type": "Type of property (multifamily, office, retail, industrial, mixed_use)",
    "year_built": "Year the property was built",
    "total_units": "Total number of units",
    "total_sqft": "Total square footage",
    "sale_price": "Sale price of the property",
    "sale_date": "Date of sale",
    "price_per_sqft": "Sale price per square foot",
    "price_per_unit": "Sale price per unit",
    "cap_rate": "Capitalization rate",
    "noi": "Net Operating Income",
    "occupancy_rate": "Occupancy rate percentage",
    "avg_rent_per_sqft": "Average rent per square foot",
    "amenities": "List of property amenities",
    "notes": "Additional notes",
}

OPERATING_EXPENSES_FIELDS = {
    "expense_id": "Unique identifier for the expense",
    "category": "Expense category (e.g., Maintenance, Utilities, Insurance)",
    "subcategory": "Subcategory within the main category",
    "description": "Detailed description of the expense",
    "amount": "Expense amount",
    "period_start": "Start date of the expense period",
    "period_end": "End date of the expense period",
    "vendor": "Vendor or service provider",
    "invoice_number": "Invoice or reference number",
    "payment_date": "Date when payment was made",
    "payment_method": "Method of payment",
    "recurring": "Whether this is a recurring expense",
    "notes": "Additional notes",
}

TENANT_ROSTER_FIELDS = {
    "tenant_id": "Unique identifier for the tenant",
    "tenant_name": "Name of the tenant",
    "unit_id": "Unit identifier",
    "lease_start_date": "Start date of the lease",
    "lease_end_date": "End date of the lease",
    "monthly_rent": "Monthly rent amount",
    "security_deposit": "Security deposit amount",
    "pet_deposit": "Pet deposit amount if applicable",
    "tenant_type": "Type of tenant (residential, commercial, retail, office)",
    "age_range": "Age range of the tenant",
    "household_size": "Number of people in the household",
    "income_range": "Income range of the tenant",
    "employment_status": "Employment status",
    "credit_score_range": "Credit score range",
    "move_in_date": "Actual move-in date",
    "move_out_date": "Move-out date if applicable",
    "lease_renewals": "Number of lease renewals",
    "payment_history": "Payment history data",
    "emergency_contact": "Emergency contact information",
    "notes": "Additional notes",
}

NOI_FIELDS = {
    "period_start": "Start date of the period",
    "period_end": "End date of the period",
    "gross_rental_income": "Total gross rental income",
    "other_income": "Other income sources",
    "total_income": "Total income",
    "operating_expenses": "Total operating expenses",
    "net_operating_income": "Net Operating Income",
    "occupancy_rate": "Occupancy rate percentage",
    "avg_rent_per_sqft": "Average rent per square foot",
    "notes": "Additional notes",
}

MARKET_ANALYSIS_FIELDS = {
    "market_id": "Unique identifier for the market analysis",
    "market_name": "Name of the market",
    "geographic_area": "Geographic area covered",
    "analysis_date": "Date of the analysis",
    "property_type": "Type of property analyzed",
    "avg_sale_price": "Average sale price in the market",
    "avg_price_per_sqft": "Average price per square foot",
    "avg_price_per_unit": "Average price per unit",
    "avg_cap_rate": "Average capitalization rate",
    "avg_occupancy_rate": "Average occupancy rate",
    "avg_rent_per_sqft": "Average rent per square foot",
    "market_trends": "List of market trends",
    "economic_indicators": "Economic indicators data",
    "demographics": "Demographic data",
    "competition_analysis": "Competition analysis",
    "notes": "Additional notes",
}
