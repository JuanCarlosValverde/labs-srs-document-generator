#!/usr/bin/env python3
"""
SRS Document Generator - Simplified CSV Data Generation Script
Generates comprehensive test data for all property types in CSV format
"""

print("🚀 Starting SRS Document Generator (CSV Version)...")

import csv
import json
import random
import sys
from pathlib import Path
from datetime import date, datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
from typing import List, Dict, Any, Optional

# Add src to path for imports
sys.path.append(str(Path(__file__).parent / "src"))

print("📦 Importing modules...")

from schemas import (
    PropertyType, LeaseStatus, TenantType,
    RENT_ROLL_FIELDS, COMPARABLES_FIELDS, OPERATING_EXPENSES_FIELDS,
    TENANT_ROSTER_FIELDS, NOI_FIELDS, MARKET_ANALYSIS_FIELDS
)

print("✅ Modules imported successfully")


class SimpleDataGenerator:
    """Simplified data generator for CSV files only"""
    
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
    
    def generate_rent_roll(self, num_units: int = 100, property_type: PropertyType = PropertyType.MULTIFAMILY) -> List[Dict[str, Any]]:
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
                float(square_footage * float(rent_per_sqft) * 0.8),
                float(square_footage * float(rent_per_sqft) * 1.2)
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
                float(rent_amount) * 0.5,
                float(rent_amount) * 1.5
            )
            
            pet_deposit = None
            if random.random() < 0.3:  # 30% chance of pet deposit
                pet_deposit = self.generate_random_decimal(200, 1000)
            
            # Generate parking spaces
            parking_spaces = random.randint(0, 2) if property_type == PropertyType.MULTIFAMILY else None
            
            # Generate amenities
            num_amenities = random.randint(0, 5)
            unit_amenities = random.sample(self.amenities, min(num_amenities, len(self.amenities)))
            
            unit = {
                "unit_id": self.generate_unit_id(),
                "unit_number": unit_number,
                "floor": floor,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "square_footage": square_footage,
                "rent_amount": rent_amount,
                "lease_start_date": lease_start.isoformat(),
                "lease_end_date": lease_end.isoformat(),
                "lease_status": lease_status.value,
                "tenant_name": tenant_name,
                "security_deposit": security_deposit,
                "pet_deposit": pet_deposit,
                "parking_spaces": parking_spaces,
                "amenities": ", ".join(unit_amenities) if unit_amenities else None,
                "notes": f"Generated unit {i+1}" if random.random() < 0.1 else None
            }
            
            units.append(unit)
        
        return units
    
    def generate_comparables(self, num_properties: int = 30, property_type: PropertyType = PropertyType.MULTIFAMILY) -> List[Dict[str, Any]]:
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
                sale_price = float(price_per_unit) * total_units
            elif property_type == PropertyType.OFFICE:
                price_per_sqft = self.generate_random_decimal(200, 800)
                sale_price = float(price_per_sqft) * total_sqft
            else:  # RETAIL
                price_per_sqft = self.generate_random_decimal(100, 600)
                sale_price = float(price_per_sqft) * total_sqft
            
            price_per_sqft = sale_price / total_sqft if total_sqft > 0 else None
            price_per_unit = sale_price / total_units if total_units > 0 else None
            
            # Generate financial metrics
            cap_rate = self.generate_random_decimal(4.0, 8.0)
            noi = sale_price * (float(cap_rate) / 100) if cap_rate else None
            
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
            
            comparable = {
                "property_id": self.generate_property_id(),
                "property_name": property_name,
                "address": address,
                "city": city,
                "state": state,
                "zip_code": zip_code,
                "property_type": property_type.value,
                "year_built": year_built,
                "total_units": total_units,
                "total_sqft": total_sqft,
                "sale_price": sale_price,
                "sale_date": sale_date.isoformat(),
                "price_per_sqft": price_per_sqft,
                "price_per_unit": price_per_unit,
                "cap_rate": cap_rate,
                "noi": noi,
                "occupancy_rate": occupancy_rate,
                "avg_rent_per_sqft": avg_rent_per_sqft,
                "amenities": ", ".join(property_amenities),
                "notes": f"Comparable property {i+1}" if random.random() < 0.2 else None
            }
            
            comparables.append(comparable)
        
        return comparables
    
    def generate_operating_expenses(self, num_expenses: int = 200) -> List[Dict[str, Any]]:
        """Generate operating expenses data"""
        expenses = []
        start_date = date.today() - timedelta(days=365)
        end_date = date.today()
        
        for i in range(num_expenses):
            # Generate expense details
            category = random.choice(self.expense_categories)
            description = f"{category} - {random.choice(['Service', 'Repair', 'Maintenance', 'Supply', 'Fee'])}"
            
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
            
            expense = {
                "expense_id": self.generate_expense_id(),
                "category": category,
                "subcategory": random.choice(["General", "Emergency", "Preventive", "Tenant", "Capital"]),
                "description": description,
                "amount": amount,
                "period_start": period_start.isoformat(),
                "period_end": period_end.isoformat(),
                "vendor": vendor,
                "invoice_number": invoice_number,
                "payment_date": payment_date.isoformat(),
                "payment_method": payment_method,
                "recurring": recurring,
                "notes": f"Generated expense {i+1}" if random.random() < 0.1 else None
            }
            
            expenses.append(expense)
        
        return expenses
    
    def generate_tenant_roster(self, num_tenants: int = 150, property_type: PropertyType = PropertyType.MULTIFAMILY) -> List[Dict[str, Any]]:
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
                tenant_type = TenantType.RESIDENTIAL.value
            elif property_type == PropertyType.OFFICE:
                monthly_rent = self.generate_random_decimal(2000, 15000)
                tenant_type = TenantType.OFFICE.value
            else:  # RETAIL
                monthly_rent = self.generate_random_decimal(3000, 25000)
                tenant_type = TenantType.RETAIL.value
            
            # Generate deposits
            security_deposit = self.generate_random_decimal(
                float(monthly_rent) * 0.5,
                float(monthly_rent) * 1.5
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
            
            # Generate emergency contact
            emergency_contact = f"{self.generate_random_name()} - {random.choice(['Parent', 'Spouse', 'Sibling', 'Friend'])}"
            
            tenant = {
                "tenant_id": self.generate_tenant_id(),
                "tenant_name": tenant_name,
                "unit_id": unit_id,
                "lease_start_date": lease_start.isoformat(),
                "lease_end_date": lease_end.isoformat(),
                "monthly_rent": monthly_rent,
                "security_deposit": security_deposit,
                "pet_deposit": pet_deposit,
                "tenant_type": tenant_type,
                "age_range": age_range,
                "household_size": household_size,
                "income_range": income_range,
                "employment_status": employment_status,
                "credit_score_range": credit_score_range,
                "move_in_date": move_in_date.isoformat(),
                "move_out_date": move_out_date.isoformat() if move_out_date else None,
                "lease_renewals": lease_renewals,
                "emergency_contact": emergency_contact,
                "notes": f"Generated tenant {i+1}" if random.random() < 0.1 else None
            }
            
            tenants.append(tenant)
        
        return tenants
    
    def generate_noi_data(self, years: int = 3, property_type: PropertyType = PropertyType.MULTIFAMILY) -> List[Dict[str, Any]]:
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
                gross_rental_income = float(base_rent_per_unit) * total_units
            elif property_type == PropertyType.OFFICE:
                base_rent_per_sqft = self.generate_random_decimal(2.0, 6.0)
                total_sqft = random.randint(50000, 200000)
                gross_rental_income = float(base_rent_per_sqft) * total_sqft
            else:  # RETAIL
                base_rent_per_sqft = self.generate_random_decimal(1.0, 8.0)
                total_sqft = random.randint(30000, 150000)
                gross_rental_income = float(base_rent_per_sqft) * total_sqft
            
            # Add some variation to income
            income_variation = self.generate_random_decimal(0.95, 1.05)
            gross_rental_income = gross_rental_income * float(income_variation)
            
            # Generate other income
            other_income = self.generate_random_decimal(
                gross_rental_income * 0.05,
                gross_rental_income * 0.15
            )
            
            total_income = gross_rental_income + float(other_income)
            
            # Generate operating expenses (typically 30-50% of gross income)
            expense_ratio = self.generate_random_decimal(0.30, 0.50)
            operating_expenses = gross_rental_income * float(expense_ratio)
            
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
            
            noi_point = {
                "period_start": period_start.isoformat(),
                "period_end": period_end.isoformat(),
                "gross_rental_income": gross_rental_income,
                "other_income": other_income,
                "total_income": total_income,
                "operating_expenses": operating_expenses,
                "net_operating_income": net_operating_income,
                "occupancy_rate": occupancy_rate,
                "avg_rent_per_sqft": avg_rent_per_sqft,
                "notes": f"Monthly NOI data for {period_start.strftime('%Y-%m')}" if random.random() < 0.1 else None
            }
            
            noi_data.append(noi_point)
            current_date += timedelta(days=30)
        
        return noi_data
    
    def generate_market_analysis(self, num_markets: int = 10, property_type: PropertyType = PropertyType.MULTIFAMILY) -> List[Dict[str, Any]]:
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
            
            market = {
                "market_id": f"MARKET_{random.randint(10000, 99999)}",
                "market_name": market_name,
                "geographic_area": geographic_area,
                "analysis_date": analysis_date.isoformat(),
                "property_type": property_type.value,
                "avg_sale_price": avg_sale_price,
                "avg_price_per_sqft": avg_price_per_sqft,
                "avg_price_per_unit": avg_price_per_unit,
                "avg_cap_rate": avg_cap_rate,
                "avg_occupancy_rate": avg_occupancy_rate,
                "avg_rent_per_sqft": avg_rent_per_sqft,
                "market_trends": ", ".join(market_trends),
                "economic_indicators": json.dumps(economic_indicators),
                "demographics": json.dumps(demographics),
                "competition_analysis": ", ".join(competition_analysis),
                "notes": f"Market analysis for {market_name}" if random.random() < 0.2 else None
            }
            
            markets.append(market)
        
        return markets


def export_csv(data: List[Dict[str, Any]], file_path: Path, encoding: str = 'utf-8'):
    """Export data to CSV file with specified encoding"""
    if not data:
        raise ValueError("No data provided for export")
    
    # Get fieldnames from first record
    fieldnames = list(data[0].keys())
    
    with open(file_path, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def export_data_dictionary(fields_dict: Dict[str, str], file_path: Path):
    """Export data dictionary to CSV file"""
    data = [{"field_name": field, "description": description} 
            for field, description in fields_dict.items()]
    
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["field_name", "description"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def main():
    """Main entry point for the script"""
    print("🚀 Starting SRS Document Generator (CSV Version)...")
    
    # Create output directory
    output_dir = Path("test_resources")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"📁 Output directory: {output_dir}")
    
    # Initialize generator
    generator = SimpleDataGenerator(seed=42)
    
    generated_files = []
    
    try:
        # Generate data for each property type
        property_types = [PropertyType.MULTIFAMILY, PropertyType.OFFICE, PropertyType.RETAIL]
        
        for prop_type in property_types:
            prop_name = prop_type.value
            print(f"\n📊 Generating data for {prop_name} properties...")
            
            # 1. Rent Roll CSV (50-500 units)
            print(f"  📋 Generating rent roll for {prop_name}...")
            units = generator.generate_rent_roll(
                num_units=random.randint(50, 500),
                property_type=prop_type
            )
            
            # Export in multiple encodings
            encodings = ['utf-8', 'ascii', 'utf-16']
            for encoding in encodings:
                filename = f"rent_roll_{prop_name}_{encoding}.csv"
                file_path = output_dir / filename
                export_csv(units, file_path, encoding=encoding)
                generated_files.append(file_path)
            
            # 2. Comparables CSV (20-50 properties)
            print(f"  🏢 Generating comparables for {prop_name}...")
            comparables = generator.generate_comparables(
                num_properties=random.randint(20, 50),
                property_type=prop_type
            )
            
            filename = f"comparables_{prop_name}.csv"
            file_path = output_dir / filename
            export_csv(comparables, file_path)
            generated_files.append(file_path)
            
            # 3. Operating Expenses CSV
            print(f"  💰 Generating operating expenses for {prop_name}...")
            expenses = generator.generate_operating_expenses(
                num_expenses=random.randint(100, 300)
            )
            
            filename = f"operating_expenses_{prop_name}.csv"
            file_path = output_dir / filename
            export_csv(expenses, file_path)
            generated_files.append(file_path)
            
            # 4. Tenant Roster
            print(f"  👥 Generating tenant roster for {prop_name}...")
            tenants = generator.generate_tenant_roster(
                num_tenants=random.randint(100, 200),
                property_type=prop_type
            )
            
            filename = f"tenant_roster_{prop_name}.csv"
            file_path = output_dir / filename
            export_csv(tenants, file_path)
            generated_files.append(file_path)
            
            # 5. Historical NOI Data (3-5 years)
            print(f"  📈 Generating NOI data for {prop_name}...")
            years = random.randint(3, 5)
            noi_data = generator.generate_noi_data(years=years, property_type=prop_type)
            
            filename = f"noi_data_{prop_name}.csv"
            file_path = output_dir / filename
            export_csv(noi_data, file_path)
            generated_files.append(file_path)
            
            # 6. Market Analysis
            print(f"  📊 Generating market analysis for {prop_name}...")
            markets = generator.generate_market_analysis(
                num_markets=random.randint(8, 15),
                property_type=prop_type
            )
            
            filename = f"market_analysis_{prop_name}.csv"
            file_path = output_dir / filename
            export_csv(markets, file_path)
            generated_files.append(file_path)
        
        # Generate data dictionaries
        print("\n📚 Generating data dictionaries...")
        
        dictionaries = {
            "rent_roll_fields": RENT_ROLL_FIELDS,
            "comparables_fields": COMPARABLES_FIELDS,
            "operating_expenses_fields": OPERATING_EXPENSES_FIELDS,
            "tenant_roster_fields": TENANT_ROSTER_FIELDS,
            "noi_fields": NOI_FIELDS,
            "market_analysis_fields": MARKET_ANALYSIS_FIELDS
        }
        
        for dict_name, fields_dict in dictionaries.items():
            filename = f"{dict_name}.csv"
            file_path = output_dir / filename
            export_data_dictionary(fields_dict, file_path)
            generated_files.append(file_path)
        
        # Generate summary report
        print("\n📄 Generating summary report...")
        
        summary_data = {
            "generation_date": date.today().isoformat(),
            "total_files_generated": len(generated_files),
            "files_by_type": {},
            "files_by_property_type": {},
            "files_by_encoding": {}
        }
        
        # Analyze generated files
        for file_path in generated_files:
            filename = file_path.name
            
            # Count by type
            if "rent_roll" in filename:
                summary_data["files_by_type"]["rent_roll"] = summary_data["files_by_type"].get("rent_roll", 0) + 1
            elif "comparables" in filename:
                summary_data["files_by_type"]["comparables"] = summary_data["files_by_type"].get("comparables", 0) + 1
            elif "operating_expenses" in filename:
                summary_data["files_by_type"]["operating_expenses"] = summary_data["files_by_type"].get("operating_expenses", 0) + 1
            elif "tenant_roster" in filename:
                summary_data["files_by_type"]["tenant_roster"] = summary_data["files_by_type"].get("tenant_roster", 0) + 1
            elif "noi_data" in filename:
                summary_data["files_by_type"]["noi_data"] = summary_data["files_by_type"].get("noi_data", 0) + 1
            elif "market_analysis" in filename:
                summary_data["files_by_type"]["market_analysis"] = summary_data["files_by_type"].get("market_analysis", 0) + 1
            
            # Count by property type
            for prop_type in ["multifamily", "office", "retail"]:
                if prop_type in filename:
                    summary_data["files_by_property_type"][prop_type] = summary_data["files_by_property_type"].get(prop_type, 0) + 1
            
            # Count by encoding
            for encoding in ["utf-8", "ascii", "utf-16"]:
                if encoding in filename:
                    summary_data["files_by_encoding"][encoding] = summary_data["files_by_encoding"].get(encoding, 0) + 1
        
        # Export summary report
        summary_file = output_dir / "generation_summary.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary_data, f, indent=2)
        
        generated_files.append(summary_file)
        
        # Create a human-readable summary
        summary_text = f"""
# SRS Document Generator - Data Generation Summary

## Generation Details
- **Generation Date**: {summary_data['generation_date']}
- **Total Files Generated**: {summary_data['total_files_generated']}

## Files by Type
"""
        for file_type, count in summary_data["files_by_type"].items():
            summary_text += f"- **{file_type.replace('_', ' ').title()}**: {count} files\n"
        
        summary_text += "\n## Files by Property Type\n"
        for prop_type, count in summary_data["files_by_property_type"].items():
            summary_text += f"- **{prop_type.title()}**: {count} files\n"
        
        summary_text += "\n## Files by Encoding\n"
        for encoding, count in summary_data["files_by_encoding"].items():
            summary_text += f"- **{encoding.upper()}**: {count} files\n"
        
        summary_text += f"""
## Generated Files
"""
        for file_path in sorted(generated_files):
            summary_text += f"- {file_path.name}\n"
        
        summary_text += """
## Usage Notes
- All CSV files include headers
- Data dictionaries document all field meanings and formats
- Files cover all property types (multifamily, office, retail)
- Data includes realistic financial calculations and relationships
- Files stored in project test resources directory

## Property Types Covered
- **Multifamily**: Apartment buildings, condos, townhouses
- **Office**: Commercial office buildings, business parks
- **Retail**: Shopping centers, strip malls, standalone stores

## Data Relationships
- Rent roll units correspond to tenant roster entries
- Operating expenses relate to property maintenance and management
- NOI data shows financial performance over time
- Market analysis provides comparative market data
- Comparables show similar property sales and metrics
"""
        
        # Save human-readable summary
        summary_text_file = output_dir / "README.md"
        with open(summary_text_file, 'w', encoding='utf-8') as f:
            f.write(summary_text)
        
        generated_files.append(summary_text_file)
        
        print(f"\n✅ Data generation complete! Generated {len(generated_files)} files.")
        print(f"📁 All files saved to: {output_dir}")
        
    except Exception as e:
        print(f"\n❌ Error during data generation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
