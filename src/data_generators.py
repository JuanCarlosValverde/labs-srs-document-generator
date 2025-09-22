"""
Synthetic data generators for SRS Document Generator
Creates realistic test data for all property types and data formats
"""

import csv
import json
import random
import string
from datetime import datetime, date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import List, Dict, Any, Optional
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils.dataframe import dataframe_to_rows

from .schemas import (
    RentRollUnit, ComparableProperty, OperatingExpense, TenantInfo,
    NOIDataPoint, MarketAnalysisData, PropertyType, LeaseStatus, TenantType,
    RENT_ROLL_FIELDS, COMPARABLES_FIELDS, OPERATING_EXPENSES_FIELDS,
    TENANT_ROSTER_FIELDS, NOI_FIELDS, MARKET_ANALYSIS_FIELDS
)


class SyntheticDataGenerator:
    """Main class for generating synthetic real estate data"""
    
    def __init__(self, seed: Optional[int] = None):
        """Initialize the generator with optional seed for reproducibility"""
        if seed:
            random.seed(seed)
        
        # Common data pools
        self.first_names = [
            "John", "Jane", "Michael", "Sarah", "David", "Lisa", "Robert", "Emily",
            "James", "Jessica", "William", "Ashley", "Richard", "Amanda", "Joseph",
            "Jennifer", "Thomas", "Michelle", "Christopher", "Kimberly", "Charles",
            "Donna", "Daniel", "Carol", "Matthew", "Sandra", "Anthony", "Ruth",
            "Mark", "Sharon", "Donald", "Nancy", "Steven", "Betty", "Paul", "Helen"
        ]
        
        self.last_names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
            "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
            "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
            "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark",
            "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King",
            "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores"
        ]
        
        self.cities = [
            "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia",
            "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville",
            "Fort Worth", "Columbus", "Charlotte", "San Francisco", "Indianapolis",
            "Seattle", "Denver", "Washington", "Boston", "El Paso", "Nashville",
            "Detroit", "Oklahoma City", "Portland", "Las Vegas", "Memphis", "Louisville"
        ]
        
        self.states = [
            "NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA", "TX", "FL",
            "TX", "OH", "NC", "CA", "IN", "WA", "CO", "DC", "MA", "TX", "TN", "MI",
            "OK", "OR", "NV", "TN", "KY"
        ]
        
        self.expense_categories = [
            "Maintenance", "Utilities", "Insurance", "Property Management",
            "Legal & Professional", "Marketing", "Administrative", "Repairs",
            "Landscaping", "Security", "Cleaning", "Taxes", "Permits",
            "Equipment", "Supplies", "Contractor Services"
        ]
        
        self.expense_subcategories = {
            "Maintenance": ["HVAC", "Plumbing", "Electrical", "General Repairs", "Preventive"],
            "Utilities": ["Electric", "Gas", "Water", "Sewer", "Trash", "Internet"],
            "Insurance": ["Property", "Liability", "Workers Comp", "Umbrella"],
            "Property Management": ["Management Fees", "Leasing Commissions", "Administrative"],
            "Legal & Professional": ["Legal Fees", "Accounting", "Consulting", "Appraisal"],
            "Marketing": ["Advertising", "Signage", "Online Listings", "Brokerage"],
            "Administrative": ["Office Supplies", "Software", "Phone", "Postage"],
            "Repairs": ["Emergency", "Capital", "Tenant", "Common Area"],
            "Landscaping": ["Lawn Care", "Tree Service", "Snow Removal", "Irrigation"],
            "Security": ["Alarm System", "Security Guards", "Cameras", "Access Control"],
            "Cleaning": ["Common Areas", "Unit Turnover", "Window Cleaning", "Carpet"],
            "Taxes": ["Property Tax", "Income Tax", "Sales Tax", "Other Taxes"],
            "Permits": ["Building", "Business", "Occupancy", "Renewal"],
            "Equipment": ["HVAC Units", "Appliances", "Maintenance Tools", "Office Equipment"],
            "Supplies": ["Cleaning", "Maintenance", "Office", "Safety"],
            "Contractor Services": ["General Contractor", "Specialty Trades", "Emergency Services"]
        }
        
        self.vendors = [
            "ABC Maintenance Co.", "City Utilities", "Metro Insurance", "Premier Property Management",
            "Legal Associates", "Marketing Solutions", "Office Depot", "Quick Fix Repairs",
            "Green Thumb Landscaping", "Secure Systems Inc.", "Clean Sweep Services",
            "Tax Professionals", "Permit Express", "Equipment Rentals", "Supply Central",
            "Contractor Plus", "Emergency Services", "Quality Work", "Reliable Solutions"
        ]
        
        self.amenities = [
            "Pool", "Fitness Center", "Parking Garage", "Balcony", "In-Unit Laundry",
            "Dishwasher", "Air Conditioning", "Hardwood Floors", "Granite Countertops",
            "Walk-in Closet", "Pet Friendly", "Garden", "Rooftop Deck", "Concierge",
            "Package Receiving", "Bike Storage", "Storage Unit", "Patio", "Fireplace",
            "High-Speed Internet", "Cable Ready", "Security System", "Elevator"
        ]
    
    def generate_unit_id(self, property_prefix: str = "UNIT") -> str:
        """Generate a unique unit ID"""
        return f"{property_prefix}_{random.randint(1000, 9999)}"
    
    def generate_property_id(self, prefix: str = "PROP") -> str:
        """Generate a unique property ID"""
        return f"{prefix}_{random.randint(10000, 99999)}"
    
    def generate_tenant_id(self, prefix: str = "TENANT") -> str:
        """Generate a unique tenant ID"""
        return f"{prefix}_{random.randint(10000, 99999)}"
    
    def generate_expense_id(self, prefix: str = "EXP") -> str:
        """Generate a unique expense ID"""
        return f"{prefix}_{random.randint(10000, 99999)}"
    
    def generate_random_name(self) -> str:
        """Generate a random tenant name"""
        first = random.choice(self.first_names)
        last = random.choice(self.last_names)
        return f"{first} {last}"
    
    def generate_random_address(self) -> str:
        """Generate a random street address"""
        street_numbers = [str(random.randint(100, 9999))]
        street_names = [
            "Main St", "Oak Ave", "Pine Rd", "Cedar Blvd", "Maple Dr", "Elm St",
            "First Ave", "Second St", "Park Ave", "Broadway", "Washington St",
            "Lincoln Ave", "Jefferson Rd", "Madison St", "Franklin Ave"
        ]
        return f"{random.choice(street_numbers)} {random.choice(street_names)}"
    
    def generate_random_date(self, start_date: date, end_date: date) -> date:
        """Generate a random date between start and end dates"""
        time_between = end_date - start_date
        days_between = time_between.days
        random_days = random.randint(0, days_between)
        return start_date + timedelta(days=random_days)
    
    def generate_random_decimal(self, min_val: float, max_val: float, decimal_places: int = 2) -> Decimal:
        """Generate a random decimal value"""
        value = random.uniform(min_val, max_val)
        return Decimal(str(round(value, decimal_places))).quantize(
            Decimal('0.01'), rounding=ROUND_HALF_UP
        )
    
    def add_edge_cases(self, data: List[Dict[str, Any]], edge_case_probability: float = 0.1) -> List[Dict[str, Any]]:
        """Add edge cases to the data for testing validation"""
        edge_cases = []
        
        for item in data:
            if random.random() < edge_case_probability:
                # Create a copy and modify it
                edge_item = item.copy()
                
                # Randomly introduce edge cases
                edge_type = random.choice([
                    "empty_string", "special_chars", "large_number", "negative_number",
                    "zero_value", "very_long_string", "unicode_chars"
                ])
                
                if edge_type == "empty_string":
                    # Make some fields empty
                    fields_to_empty = random.sample(list(edge_item.keys()), random.randint(1, 3))
                    for field in fields_to_empty:
                        if isinstance(edge_item[field], str):
                            edge_item[field] = ""
                
                elif edge_type == "special_chars":
                    # Add special characters
                    special_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
                    for key, value in edge_item.items():
                        if isinstance(value, str) and random.random() < 0.3:
                            edge_item[key] = f"{value}{random.choice(special_chars)}"
                
                elif edge_type == "large_number":
                    # Make numeric fields very large
                    for key, value in edge_item.items():
                        if isinstance(value, (int, float, Decimal)) and random.random() < 0.3:
                            edge_item[key] = value * random.randint(1000, 10000)
                
                elif edge_type == "negative_number":
                    # Make numeric fields negative
                    for key, value in edge_item.items():
                        if isinstance(value, (int, float, Decimal)) and random.random() < 0.3:
                            edge_item[key] = -abs(value)
                
                elif edge_type == "zero_value":
                    # Make numeric fields zero
                    for key, value in edge_item.items():
                        if isinstance(value, (int, float, Decimal)) and random.random() < 0.3:
                            edge_item[key] = 0
                
                elif edge_type == "very_long_string":
                    # Make string fields very long
                    for key, value in edge_item.items():
                        if isinstance(value, str) and random.random() < 0.3:
                            edge_item[key] = value * random.randint(10, 50)
                
                elif edge_type == "unicode_chars":
                    # Add unicode characters
                    unicode_chars = "αβγδεζηθικλμνξοπρστυφχψω"
                    for key, value in edge_item.items():
                        if isinstance(value, str) and random.random() < 0.3:
                            edge_item[key] = f"{value}{random.choice(unicode_chars)}"
                
                edge_cases.append(edge_item)
        
        return edge_cases


class RentRollGenerator(SyntheticDataGenerator):
    """Generator for rent roll data"""
    
    def generate_rent_roll(self, num_units: int = 100, property_type: PropertyType = PropertyType.MULTIFAMILY) -> List[RentRollUnit]:
        """Generate rent roll data for specified number of units"""
        units = []
        
        for i in range(num_units):
            # Generate unit number based on property type
            if property_type == PropertyType.MULTIFAMILY:
                unit_number = f"{random.randint(1, 20)}{random.choice(['A', 'B', 'C', 'D'])}"
                floor = random.randint(1, 5)
                bedrooms = random.choice([1, 2, 3, 4])
                bathrooms = random.choice([1.0, 1.5, 2.0, 2.5, 3.0])
                sqft_range = (600, 2000)
            elif property_type == PropertyType.OFFICE:
                unit_number = f"Suite {random.randint(100, 999)}"
                floor = random.randint(1, 20)
                bedrooms = None
                bathrooms = random.choice([1.0, 2.0])
                sqft_range = (500, 5000)
            else:  # RETAIL
                unit_number = f"Unit {random.randint(1, 50)}"
                floor = random.randint(1, 3)
                bedrooms = None
                bathrooms = random.choice([1.0, 2.0])
                sqft_range = (1000, 10000)
            
            square_footage = random.randint(*sqft_range)
            
            # Generate rent based on property type and square footage
            if property_type == PropertyType.MULTIFAMILY:
                rent_per_sqft = self.generate_random_decimal(1.5, 4.0)
            elif property_type == PropertyType.OFFICE:
                rent_per_sqft = self.generate_random_decimal(2.0, 6.0)
            else:  # RETAIL
                rent_per_sqft = self.generate_random_decimal(1.0, 8.0)
            
            rent_amount = self.generate_random_decimal(
                float(square_footage * rent_per_sqft * 0.8),
                float(square_footage * rent_per_sqft * 1.2)
            )
            
            # Generate lease dates
            lease_start = self.generate_random_date(
                date.today() - timedelta(days=365),
                date.today() + timedelta(days=30)
            )
            lease_end = lease_start + timedelta(days=random.randint(365, 1095))  # 1-3 years
            
            # Generate lease status
            status_options = [LeaseStatus.OCCUPIED, LeaseStatus.VACANT, LeaseStatus.PENDING]
            weights = [0.85, 0.10, 0.05]  # Most units occupied
            lease_status = random.choices(status_options, weights=weights)[0]
            
            # Generate tenant name if occupied
            tenant_name = None
            if lease_status == LeaseStatus.OCCUPIED:
                tenant_name = self.generate_random_name()
            
            # Generate deposits
            security_deposit = self.generate_random_decimal(
                float(rent_amount * 0.5),
                float(rent_amount * 1.5)
            )
            
            pet_deposit = None
            if random.random() < 0.3:  # 30% chance of pet deposit
                pet_deposit = self.generate_random_decimal(200, 1000)
            
            # Generate parking spaces
            parking_spaces = random.randint(0, 2) if property_type == PropertyType.MULTIFAMILY else None
            
            # Generate amenities
            num_amenities = random.randint(0, 5)
            unit_amenities = random.sample(self.amenities, min(num_amenities, len(self.amenities)))
            
            unit = RentRollUnit(
                unit_id=self.generate_unit_id(),
                unit_number=unit_number,
                floor=floor,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                square_footage=square_footage,
                rent_amount=rent_amount,
                lease_start_date=lease_start,
                lease_end_date=lease_end,
                lease_status=lease_status,
                tenant_name=tenant_name,
                security_deposit=security_deposit,
                pet_deposit=pet_deposit,
                parking_spaces=parking_spaces,
                amenities=unit_amenities if unit_amenities else None,
                notes=f"Generated unit {i+1}" if random.random() < 0.1 else None
            )
            
            units.append(unit)
        
        return units
    
    def rent_roll_to_dict(self, units: List[RentRollUnit]) -> List[Dict[str, Any]]:
        """Convert RentRollUnit objects to dictionaries for CSV export"""
        return [
            {
                "unit_id": unit.unit_id,
                "unit_number": unit.unit_number,
                "floor": unit.floor,
                "bedrooms": unit.bedrooms,
                "bathrooms": unit.bathrooms,
                "square_footage": unit.square_footage,
                "rent_amount": unit.rent_amount,
                "lease_start_date": unit.lease_start_date.isoformat() if unit.lease_start_date else None,
                "lease_end_date": unit.lease_end_date.isoformat() if unit.lease_end_date else None,
                "lease_status": unit.lease_status.value if unit.lease_status else None,
                "tenant_name": unit.tenant_name,
                "security_deposit": unit.security_deposit,
                "pet_deposit": unit.pet_deposit,
                "parking_spaces": unit.parking_spaces,
                "amenities": ", ".join(unit.amenities) if unit.amenities else None,
                "notes": unit.notes
            }
            for unit in units
        ]


class ComparablesGenerator(SyntheticDataGenerator):
    """Generator for comparable properties data"""
    
    def generate_comparables(self, num_properties: int = 30, property_type: PropertyType = PropertyType.MULTIFAMILY) -> List[ComparableProperty]:
        """Generate comparable properties data"""
        comparables = []
        
        for i in range(num_properties):
            # Generate property details
            property_name = f"{random.choice(['The', 'Grand', 'Royal', 'Elite', 'Premier'])} {random.choice(['Towers', 'Plaza', 'Court', 'Manor', 'Gardens'])}"
            address = self.generate_random_address()
            city = random.choice(self.cities)
            state = random.choice(self.states)
            zip_code = f"{random.randint(10000, 99999)}"
            
            # Generate property characteristics
            year_built = random.randint(1950, 2023)
            
            if property_type == PropertyType.MULTIFAMILY:
                total_units = random.randint(20, 500)
                total_sqft = total_units * random.randint(600, 2000)
            elif property_type == PropertyType.OFFICE:
                total_units = random.randint(10, 100)
                total_sqft = total_units * random.randint(1000, 5000)
            else:  # RETAIL
                total_units = random.randint(5, 50)
                total_sqft = total_units * random.randint(2000, 10000)
            
            # Generate sale data
            sale_date = self.generate_random_date(
                date.today() - timedelta(days=1095),  # Last 3 years
                date.today()
            )
            
            # Generate realistic sale price based on property type and size
            if property_type == PropertyType.MULTIFAMILY:
                price_per_unit = self.generate_random_decimal(150000, 500000)
                sale_price = price_per_unit * total_units
            elif property_type == PropertyType.OFFICE:
                price_per_sqft = self.generate_random_decimal(200, 800)
                sale_price = price_per_sqft * total_sqft
            else:  # RETAIL
                price_per_sqft = self.generate_random_decimal(100, 600)
                sale_price = price_per_sqft * total_sqft
            
            price_per_sqft = sale_price / total_sqft if total_sqft > 0 else None
            price_per_unit = sale_price / total_units if total_units > 0 else None
            
            # Generate financial metrics
            cap_rate = self.generate_random_decimal(4.0, 8.0)
            noi = sale_price * (cap_rate / 100) if cap_rate else None
            
            occupancy_rate = self.generate_random_decimal(85.0, 98.0)
            
            # Generate rent data
            if property_type == PropertyType.MULTIFAMILY:
                avg_rent_per_sqft = self.generate_random_decimal(1.5, 4.0)
            elif property_type == PropertyType.OFFICE:
                avg_rent_per_sqft = self.generate_random_decimal(2.0, 6.0)
            else:  # RETAIL
                avg_rent_per_sqft = self.generate_random_decimal(1.0, 8.0)
            
            # Generate amenities
            num_amenities = random.randint(3, 8)
            property_amenities = random.sample(self.amenities, min(num_amenities, len(self.amenities)))
            
            comparable = ComparableProperty(
                property_id=self.generate_property_id(),
                property_name=property_name,
                address=address,
                city=city,
                state=state,
                zip_code=zip_code,
                property_type=property_type,
                year_built=year_built,
                total_units=total_units,
                total_sqft=total_sqft,
                sale_price=sale_price,
                sale_date=sale_date,
                price_per_sqft=price_per_sqft,
                price_per_unit=price_per_unit,
                cap_rate=cap_rate,
                noi=noi,
                occupancy_rate=occupancy_rate,
                avg_rent_per_sqft=avg_rent_per_sqft,
                amenities=property_amenities,
                notes=f"Comparable property {i+1}" if random.random() < 0.2 else None
            )
            
            comparables.append(comparable)
        
        return comparables
    
    def comparables_to_dict(self, comparables: List[ComparableProperty]) -> List[Dict[str, Any]]:
        """Convert ComparableProperty objects to dictionaries for Excel export"""
        return [
            {
                "property_id": comp.property_id,
                "property_name": comp.property_name,
                "address": comp.address,
                "city": comp.city,
                "state": comp.state,
                "zip_code": comp.zip_code,
                "property_type": comp.property_type.value,
                "year_built": comp.year_built,
                "total_units": comp.total_units,
                "total_sqft": comp.total_sqft,
                "sale_price": comp.sale_price,
                "sale_date": comp.sale_date.isoformat() if comp.sale_date else None,
                "price_per_sqft": comp.price_per_sqft,
                "price_per_unit": comp.price_per_unit,
                "cap_rate": comp.cap_rate,
                "noi": comp.noi,
                "occupancy_rate": comp.occupancy_rate,
                "avg_rent_per_sqft": comp.avg_rent_per_sqft,
                "amenities": ", ".join(comp.amenities) if comp.amenities else None,
                "notes": comp.notes
            }
            for comp in comparables
        ]


class OperatingExpensesGenerator(SyntheticDataGenerator):
    """Generator for operating expenses data"""
    
    def generate_operating_expenses(self, num_expenses: int = 200, start_date: date = None, end_date: date = None) -> List[OperatingExpense]:
        """Generate operating expenses data"""
        if not start_date:
            start_date = date.today() - timedelta(days=365)
        if not end_date:
            end_date = date.today()
        
        expenses = []
        
        for i in range(num_expenses):
            # Generate expense details
            category = random.choice(self.expense_categories)
            subcategory = random.choice(self.expense_subcategories.get(category, [""]))
            
            description = f"{category} - {subcategory} - {random.choice(['Service', 'Repair', 'Maintenance', 'Supply', 'Fee'])}"
            
            # Generate amount based on category
            if category in ["Maintenance", "Repairs"]:
                amount = self.generate_random_decimal(100, 5000)
            elif category == "Utilities":
                amount = self.generate_random_decimal(500, 3000)
            elif category == "Insurance":
                amount = self.generate_random_decimal(2000, 15000)
            elif category == "Property Management":
                amount = self.generate_random_decimal(1000, 8000)
            elif category in ["Legal & Professional", "Marketing"]:
                amount = self.generate_random_decimal(500, 3000)
            else:
                amount = self.generate_random_decimal(50, 2000)
            
            # Generate period dates
            period_start = self.generate_random_date(start_date, end_date)
            period_end = period_start + timedelta(days=random.randint(1, 90))
            
            # Generate vendor
            vendor = random.choice(self.vendors)
            
            # Generate invoice number
            invoice_number = f"INV-{random.randint(10000, 99999)}"
            
            # Generate payment date
            payment_date = period_start + timedelta(days=random.randint(1, 30))
            
            # Generate payment method
            payment_methods = ["Check", "ACH", "Wire Transfer", "Credit Card", "Cash"]
            payment_method = random.choice(payment_methods)
            
            # Determine if recurring
            recurring = random.random() < 0.3  # 30% chance of recurring
            
            expense = OperatingExpense(
                expense_id=self.generate_expense_id(),
                category=category,
                subcategory=subcategory if subcategory else None,
                description=description,
                amount=amount,
                period_start=period_start,
                period_end=period_end,
                vendor=vendor,
                invoice_number=invoice_number,
                payment_date=payment_date,
                payment_method=payment_method,
                recurring=recurring,
                notes=f"Generated expense {i+1}" if random.random() < 0.1 else None
            )
            
            expenses.append(expense)
        
        return expenses
    
    def operating_expenses_to_dict(self, expenses: List[OperatingExpense]) -> List[Dict[str, Any]]:
        """Convert OperatingExpense objects to dictionaries for CSV export"""
        return [
            {
                "expense_id": exp.expense_id,
                "category": exp.category,
                "subcategory": exp.subcategory,
                "description": exp.description,
                "amount": exp.amount,
                "period_start": exp.period_start.isoformat(),
                "period_end": exp.period_end.isoformat(),
                "vendor": exp.vendor,
                "invoice_number": exp.invoice_number,
                "payment_date": exp.payment_date.isoformat() if exp.payment_date else None,
                "payment_method": exp.payment_method,
                "recurring": exp.recurring,
                "notes": exp.notes
            }
            for exp in expenses
        ]


class TenantRosterGenerator(SyntheticDataGenerator):
    """Generator for tenant roster data"""
    
    def generate_tenant_roster(self, num_tenants: int = 150, property_type: PropertyType = PropertyType.MULTIFAMILY) -> List[TenantInfo]:
        """Generate tenant roster data"""
        tenants = []
        
        for i in range(num_tenants):
            # Generate tenant details
            tenant_name = self.generate_random_name()
            unit_id = self.generate_unit_id()
            
            # Generate lease dates
            lease_start = self.generate_random_date(
                date.today() - timedelta(days=1095),  # Up to 3 years ago
                date.today() + timedelta(days=30)
            )
            lease_end = lease_start + timedelta(days=random.randint(365, 1095))  # 1-3 years
            
            # Generate rent based on property type
            if property_type == PropertyType.MULTIFAMILY:
                monthly_rent = self.generate_random_decimal(800, 4000)
                tenant_type = TenantType.RESIDENTIAL
            elif property_type == PropertyType.OFFICE:
                monthly_rent = self.generate_random_decimal(2000, 15000)
                tenant_type = TenantType.OFFICE
            else:  # RETAIL
                monthly_rent = self.generate_random_decimal(3000, 25000)
                tenant_type = TenantType.RETAIL
            
            # Generate deposits
            security_deposit = self.generate_random_decimal(
                float(monthly_rent * 0.5),
                float(monthly_rent * 1.5)
            )
            
            pet_deposit = None
            if property_type == PropertyType.MULTIFAMILY and random.random() < 0.3:
                pet_deposit = self.generate_random_decimal(200, 1000)
            
            # Generate demographic data
            age_ranges = ["18-25", "26-35", "36-45", "46-55", "56-65", "65+"]
            age_range = random.choice(age_ranges)
            
            household_size = random.randint(1, 6) if property_type == PropertyType.MULTIFAMILY else random.randint(1, 3)
            
            income_ranges = ["Under $30k", "$30k-$50k", "$50k-$75k", "$75k-$100k", "$100k-$150k", "$150k+"]
            income_range = random.choice(income_ranges)
            
            employment_statuses = ["Employed", "Self-Employed", "Student", "Retired", "Unemployed"]
            employment_status = random.choice(employment_statuses)
            
            credit_score_ranges = ["Poor (300-579)", "Fair (580-669)", "Good (670-739)", "Very Good (740-799)", "Excellent (800-850)"]
            credit_score_range = random.choice(credit_score_ranges)
            
            # Generate move-in date (usually close to lease start)
            move_in_date = lease_start + timedelta(days=random.randint(0, 30))
            
            # Generate move-out date (if applicable)
            move_out_date = None
            if random.random() < 0.1:  # 10% chance of moved out
                move_out_date = self.generate_random_date(lease_start, lease_end)
            
            # Generate lease renewals
            lease_renewals = random.randint(0, 3)
            
            # Generate payment history
            payment_history = []
            current_date = lease_start
            while current_date <= min(lease_end, date.today()):
                payment_status = random.choice(["On Time", "Late", "Partial"])
                payment_amount = monthly_rent if payment_status != "Partial" else monthly_rent * self.generate_random_decimal(0.5, 1.0)
                
                payment_history.append({
                    "date": current_date.isoformat(),
                    "amount": payment_amount,
                    "status": payment_status
                })
                
                current_date += timedelta(days=30)
            
            # Generate emergency contact
            emergency_contact = f"{self.generate_random_name()} - {random.choice(['Parent', 'Spouse', 'Sibling', 'Friend'])}"
            
            tenant = TenantInfo(
                tenant_id=self.generate_tenant_id(),
                tenant_name=tenant_name,
                unit_id=unit_id,
                lease_start_date=lease_start,
                lease_end_date=lease_end,
                monthly_rent=monthly_rent,
                security_deposit=security_deposit,
                pet_deposit=pet_deposit,
                tenant_type=tenant_type,
                age_range=age_range,
                household_size=household_size,
                income_range=income_range,
                employment_status=employment_status,
                credit_score_range=credit_score_range,
                move_in_date=move_in_date,
                move_out_date=move_out_date,
                lease_renewals=lease_renewals,
                payment_history=payment_history,
                emergency_contact=emergency_contact,
                notes=f"Generated tenant {i+1}" if random.random() < 0.1 else None
            )
            
            tenants.append(tenant)
        
        return tenants
    
    def tenant_roster_to_dict(self, tenants: List[TenantInfo]) -> List[Dict[str, Any]]:
        """Convert TenantInfo objects to dictionaries for CSV export"""
        return [
            {
                "tenant_id": tenant.tenant_id,
                "tenant_name": tenant.tenant_name,
                "unit_id": tenant.unit_id,
                "lease_start_date": tenant.lease_start_date.isoformat(),
                "lease_end_date": tenant.lease_end_date.isoformat(),
                "monthly_rent": tenant.monthly_rent,
                "security_deposit": tenant.security_deposit,
                "pet_deposit": tenant.pet_deposit,
                "tenant_type": tenant.tenant_type.value if tenant.tenant_type else None,
                "age_range": tenant.age_range,
                "household_size": tenant.household_size,
                "income_range": tenant.income_range,
                "employment_status": tenant.employment_status,
                "credit_score_range": tenant.credit_score_range,
                "move_in_date": tenant.move_in_date.isoformat() if tenant.move_in_date else None,
                "move_out_date": tenant.move_out_date.isoformat() if tenant.move_out_date else None,
                "lease_renewals": tenant.lease_renewals,
                "payment_history": json.dumps(tenant.payment_history) if tenant.payment_history else None,
                "emergency_contact": tenant.emergency_contact,
                "notes": tenant.notes
            }
            for tenant in tenants
        ]


class NOIGenerator(SyntheticDataGenerator):
    """Generator for Net Operating Income data"""
    
    def generate_noi_data(self, years: int = 3, property_type: PropertyType = PropertyType.MULTIFAMILY) -> List[NOIDataPoint]:
        """Generate historical NOI data for specified number of years"""
        noi_data = []
        
        # Start from 3 years ago
        start_date = date.today() - timedelta(days=years * 365)
        
        current_date = start_date
        while current_date < date.today():
            # Generate monthly data
            period_start = current_date
            period_end = current_date + timedelta(days=30)
            
            # Generate income based on property type
            if property_type == PropertyType.MULTIFAMILY:
                base_rent_per_unit = self.generate_random_decimal(1200, 3000)
                total_units = random.randint(50, 200)
                gross_rental_income = base_rent_per_unit * total_units
            elif property_type == PropertyType.OFFICE:
                base_rent_per_sqft = self.generate_random_decimal(2.0, 6.0)
                total_sqft = random.randint(50000, 200000)
                gross_rental_income = base_rent_per_sqft * total_sqft
            else:  # RETAIL
                base_rent_per_sqft = self.generate_random_decimal(1.0, 8.0)
                total_sqft = random.randint(30000, 150000)
                gross_rental_income = base_rent_per_sqft * total_sqft
            
            # Add some variation to income
            income_variation = self.generate_random_decimal(0.95, 1.05)
            gross_rental_income = gross_rental_income * income_variation
            
            # Generate other income
            other_income = self.generate_random_decimal(
                float(gross_rental_income * 0.05),
                float(gross_rental_income * 0.15)
            )
            
            total_income = gross_rental_income + other_income
            
            # Generate operating expenses (typically 30-50% of gross income)
            expense_ratio = self.generate_random_decimal(0.30, 0.50)
            operating_expenses = gross_rental_income * expense_ratio
            
            # Calculate NOI
            net_operating_income = total_income - operating_expenses
            
            # Generate occupancy rate
            occupancy_rate = self.generate_random_decimal(85.0, 98.0)
            
            # Generate average rent per sqft
            if property_type == PropertyType.MULTIFAMILY:
                avg_rent_per_sqft = self.generate_random_decimal(1.5, 4.0)
            elif property_type == PropertyType.OFFICE:
                avg_rent_per_sqft = self.generate_random_decimal(2.0, 6.0)
            else:  # RETAIL
                avg_rent_per_sqft = self.generate_random_decimal(1.0, 8.0)
            
            noi_point = NOIDataPoint(
                period_start=period_start,
                period_end=period_end,
                gross_rental_income=gross_rental_income,
                other_income=other_income,
                total_income=total_income,
                operating_expenses=operating_expenses,
                net_operating_income=net_operating_income,
                occupancy_rate=occupancy_rate,
                avg_rent_per_sqft=avg_rent_per_sqft,
                notes=f"Monthly NOI data for {period_start.strftime('%Y-%m')}" if random.random() < 0.1 else None
            )
            
            noi_data.append(noi_point)
            current_date += timedelta(days=30)
        
        return noi_data
    
    def noi_data_to_dict(self, noi_data: List[NOIDataPoint]) -> List[Dict[str, Any]]:
        """Convert NOIDataPoint objects to dictionaries for CSV export"""
        return [
            {
                "period_start": point.period_start.isoformat(),
                "period_end": point.period_end.isoformat(),
                "gross_rental_income": point.gross_rental_income,
                "other_income": point.other_income,
                "total_income": point.total_income,
                "operating_expenses": point.operating_expenses,
                "net_operating_income": point.net_operating_income,
                "occupancy_rate": point.occupancy_rate,
                "avg_rent_per_sqft": point.avg_rent_per_sqft,
                "notes": point.notes
            }
            for point in noi_data
        ]


class MarketAnalysisGenerator(SyntheticDataGenerator):
    """Generator for market analysis data"""
    
    def generate_market_analysis(self, num_markets: int = 10, property_type: PropertyType = PropertyType.MULTIFAMILY) -> List[MarketAnalysisData]:
        """Generate market analysis data"""
        markets = []
        
        for i in range(num_markets):
            # Generate market details
            market_name = f"{random.choice(self.cities)} {property_type.value.title()} Market"
            geographic_area = f"{random.choice(self.cities)}, {random.choice(self.states)}"
            analysis_date = self.generate_random_date(
                date.today() - timedelta(days=90),
                date.today()
            )
            
            # Generate market metrics based on property type
            if property_type == PropertyType.MULTIFAMILY:
                avg_sale_price = self.generate_random_decimal(200000, 800000)
                avg_price_per_sqft = self.generate_random_decimal(150, 400)
                avg_price_per_unit = self.generate_random_decimal(150000, 500000)
                avg_cap_rate = self.generate_random_decimal(4.0, 7.0)
                avg_occupancy_rate = self.generate_random_decimal(88.0, 96.0)
                avg_rent_per_sqft = self.generate_random_decimal(1.5, 4.0)
            elif property_type == PropertyType.OFFICE:
                avg_sale_price = self.generate_random_decimal(500000, 2000000)
                avg_price_per_sqft = self.generate_random_decimal(200, 800)
                avg_price_per_unit = None
                avg_cap_rate = self.generate_random_decimal(5.0, 8.0)
                avg_occupancy_rate = self.generate_random_decimal(85.0, 95.0)
                avg_rent_per_sqft = self.generate_random_decimal(2.0, 6.0)
            else:  # RETAIL
                avg_sale_price = self.generate_random_decimal(300000, 1500000)
                avg_price_per_sqft = self.generate_random_decimal(100, 600)
                avg_price_per_unit = None
                avg_cap_rate = self.generate_random_decimal(6.0, 9.0)
                avg_occupancy_rate = self.generate_random_decimal(80.0, 95.0)
                avg_rent_per_sqft = self.generate_random_decimal(1.0, 8.0)
            
            # Generate market trends
            trend_options = [
                "Rising rental rates", "Increasing occupancy", "New development",
                "Market stabilization", "Growing demand", "Supply constraints",
                "Economic growth", "Population increase", "Job market expansion",
                "Infrastructure improvements", "Gentrification", "Tech sector growth"
            ]
            market_trends = random.sample(trend_options, random.randint(3, 6))
            
            # Generate economic indicators
            economic_indicators = {
                "unemployment_rate": round(random.uniform(3.0, 8.0), 1),
                "gdp_growth": round(random.uniform(1.0, 5.0), 1),
                "population_growth": round(random.uniform(0.5, 3.0), 1),
                "median_household_income": random.randint(45000, 120000),
                "job_growth_rate": round(random.uniform(1.0, 4.0), 1)
            }
            
            # Generate demographics
            demographics = {
                "median_age": random.randint(28, 45),
                "college_educated_percent": round(random.uniform(25.0, 65.0), 1),
                "household_size_avg": round(random.uniform(2.0, 3.5), 1),
                "homeownership_rate": round(random.uniform(45.0, 75.0), 1)
            }
            
            # Generate competition analysis
            competition_items = [
                f"{random.randint(5, 20)} new properties under construction",
                f"{random.randint(10, 50)} properties for sale",
                f"{random.randint(2, 8)} major developments planned",
                "Strong institutional investor presence",
                "Limited land availability",
                "High construction costs",
                "Zoning restrictions",
                "Traffic and accessibility concerns"
            ]
            competition_analysis = random.sample(competition_items, random.randint(3, 5))
            
            market = MarketAnalysisData(
                market_id=f"MARKET_{random.randint(10000, 99999)}",
                market_name=market_name,
                geographic_area=geographic_area,
                analysis_date=analysis_date,
                property_type=property_type,
                avg_sale_price=avg_sale_price,
                avg_price_per_sqft=avg_price_per_sqft,
                avg_price_per_unit=avg_price_per_unit,
                avg_cap_rate=avg_cap_rate,
                avg_occupancy_rate=avg_occupancy_rate,
                avg_rent_per_sqft=avg_rent_per_sqft,
                market_trends=market_trends,
                economic_indicators=economic_indicators,
                demographics=demographics,
                competition_analysis=competition_analysis,
                notes=f"Market analysis for {market_name}" if random.random() < 0.2 else None
            )
            
            markets.append(market)
        
        return markets
    
    def market_analysis_to_dict(self, markets: List[MarketAnalysisData]) -> List[Dict[str, Any]]:
        """Convert MarketAnalysisData objects to dictionaries for CSV export"""
        return [
            {
                "market_id": market.market_id,
                "market_name": market.market_name,
                "geographic_area": market.geographic_area,
                "analysis_date": market.analysis_date.isoformat(),
                "property_type": market.property_type.value,
                "avg_sale_price": market.avg_sale_price,
                "avg_price_per_sqft": market.avg_price_per_sqft,
                "avg_price_per_unit": market.avg_price_per_unit,
                "avg_cap_rate": market.avg_cap_rate,
                "avg_occupancy_rate": market.avg_occupancy_rate,
                "avg_rent_per_sqft": market.avg_rent_per_sqft,
                "market_trends": ", ".join(market.market_trends) if market.market_trends else None,
                "economic_indicators": json.dumps(market.economic_indicators) if market.economic_indicators else None,
                "demographics": json.dumps(market.demographics) if market.demographics else None,
                "competition_analysis": ", ".join(market.competition_analysis) if market.competition_analysis else None,
                "notes": market.notes
            }
            for market in markets
        ]
