#!/usr/bin/env python3
"""
SRS Document Generator - Synthetic Data Generation Script
Generates comprehensive test data for all property types and formats
"""

print("🚀 Starting SRS Document Generator...")

import argparse
import sys
from pathlib import Path
from datetime import date
from typing import List, Dict, Any

# Add src to path for imports
sys.path.append(str(Path(__file__).parent / "src"))

print("📦 Importing modules...")

from schemas import (
    PropertyType, RENT_ROLL_FIELDS, COMPARABLES_FIELDS, OPERATING_EXPENSES_FIELDS,
    TENANT_ROSTER_FIELDS, NOI_FIELDS, MARKET_ANALYSIS_FIELDS
)
from data_generators import (
    RentRollGenerator, ComparablesGenerator, OperatingExpensesGenerator,
    TenantRosterGenerator, NOIGenerator, MarketAnalysisGenerator
)
from file_exporters import FileExporter

print("✅ Modules imported successfully")


class SRSDataGenerator:
    """Main class for generating all SRS test data"""
    
    def __init__(self, output_dir: Path, seed: int = None):
        """Initialize the generator"""
        self.output_dir = output_dir
        self.exporter = FileExporter(output_dir)
        
        # Initialize generators
        self.rent_roll_gen = RentRollGenerator(seed)
        self.comparables_gen = ComparablesGenerator(seed)
        self.expenses_gen = OperatingExpensesGenerator(seed)
        self.tenant_gen = TenantRosterGenerator(seed)
        self.noi_gen = NOIGenerator(seed)
        self.market_gen = MarketAnalysisGenerator(seed)
        
        self.generated_files = []
    
    def generate_all_data(self, include_edge_cases: bool = True, include_errors: bool = True):
        """Generate all required data files"""
        print("🚀 Starting SRS Document Generator...")
        print(f"📁 Output directory: {self.output_dir}")
        
        # Generate data for each property type
        property_types = [PropertyType.MULTIFAMILY, PropertyType.OFFICE, PropertyType.RETAIL]
        
        for prop_type in property_types:
            print(f"\n📊 Generating data for {prop_type.value} properties...")
            self._generate_property_type_data(prop_type, include_edge_cases, include_errors)
        
        # Generate data dictionaries
        self._generate_data_dictionaries()
        
        # Generate summary report
        self._generate_summary_report()
        
        print(f"\n✅ Data generation complete! Generated {len(self.generated_files)} files.")
        print(f"📁 All files saved to: {self.output_dir}")
    
    def _generate_property_type_data(self, prop_type: PropertyType, include_edge_cases: bool, include_errors: bool):
        """Generate all data files for a specific property type"""
        prop_name = prop_type.value
        
        # 1. Rent Roll CSV (50-500 units)
        print(f"  📋 Generating rent roll for {prop_name}...")
        units = self.rent_roll_gen.generate_rent_roll(
            num_units=random.randint(50, 500),
            property_type=prop_type
        )
        rent_roll_data = self.rent_roll_gen.rent_roll_to_dict(units)
        
        # Export in multiple formats and encodings
        self._export_rent_roll(rent_roll_data, prop_name, include_edge_cases, include_errors)
        
        # 2. Comparables Excel (20-50 properties)
        print(f"  🏢 Generating comparables for {prop_name}...")
        comparables = self.comparables_gen.generate_comparables(
            num_properties=random.randint(20, 50),
            property_type=prop_type
        )
        comparables_data = self.comparables_gen.comparables_to_dict(comparables)
        
        self._export_comparables(comparables_data, prop_name)
        
        # 3. Operating Expenses CSV
        print(f"  💰 Generating operating expenses for {prop_name}...")
        expenses = self.expenses_gen.generate_operating_expenses(
            num_expenses=random.randint(100, 300)
        )
        expenses_data = self.expenses_gen.operating_expenses_to_dict(expenses)
        
        self._export_operating_expenses(expenses_data, prop_name, include_edge_cases, include_errors)
        
        # 4. Tenant Roster
        print(f"  👥 Generating tenant roster for {prop_name}...")
        tenants = self.tenant_gen.generate_tenant_roster(
            num_tenants=random.randint(100, 200),
            property_type=prop_type
        )
        tenants_data = self.tenant_gen.tenant_roster_to_dict(tenants)
        
        self._export_tenant_roster(tenants_data, prop_name, include_edge_cases, include_errors)
        
        # 5. Historical NOI Data (3-5 years)
        print(f"  📈 Generating NOI data for {prop_name}...")
        years = random.randint(3, 5)
        noi_data = self.noi_gen.generate_noi_data(years=years, property_type=prop_type)
        noi_data_dict = self.noi_gen.noi_data_to_dict(noi_data)
        
        self._export_noi_data(noi_data_dict, prop_name, include_edge_cases, include_errors)
        
        # 6. Market Analysis
        print(f"  📊 Generating market analysis for {prop_name}...")
        markets = self.market_gen.generate_market_analysis(
            num_markets=random.randint(8, 15),
            property_type=prop_type
        )
        markets_data = self.market_gen.market_analysis_to_dict(markets)
        
        self._export_market_analysis(markets_data, prop_name, include_edge_cases, include_errors)
    
    def _export_rent_roll(self, data: List[Dict[str, Any]], prop_name: str, include_edge_cases: bool, include_errors: bool):
        """Export rent roll data in multiple formats"""
        # Standard CSV files
        encodings = ['utf-8', 'ascii', 'utf-16']
        for encoding in encodings:
            filename = f"rent_roll_{prop_name}_{encoding}"
            file_path = self.exporter.export_csv(
                data, filename, encoding=encoding, include_edge_cases=include_edge_cases
            )
            self.generated_files.append(file_path)
        
        # Excel formats
        file_path = self.exporter.export_excel(data, f"rent_roll_{prop_name}")
        self.generated_files.append(file_path)
        
        file_path = self.exporter.export_excel_legacy(data, f"rent_roll_{prop_name}_legacy")
        self.generated_files.append(file_path)
        
        # Error files for validation testing
        if include_errors:
            error_files = self.exporter.create_error_files(data, f"rent_roll_{prop_name}_errors")
            self.generated_files.extend(error_files)
    
    def _export_comparables(self, data: List[Dict[str, Any]], prop_name: str):
        """Export comparables data"""
        # Excel formats
        file_path = self.exporter.export_excel(data, f"comparables_{prop_name}")
        self.generated_files.append(file_path)
        
        file_path = self.exporter.export_excel_legacy(data, f"comparables_{prop_name}_legacy")
        self.generated_files.append(file_path)
        
        # CSV format
        file_path = self.exporter.export_csv(data, f"comparables_{prop_name}")
        self.generated_files.append(file_path)
    
    def _export_operating_expenses(self, data: List[Dict[str, Any]], prop_name: str, include_edge_cases: bool, include_errors: bool):
        """Export operating expenses data"""
        # CSV files with different encodings
        encodings = ['utf-8', 'ascii', 'utf-16']
        for encoding in encodings:
            filename = f"operating_expenses_{prop_name}_{encoding}"
            file_path = self.exporter.export_csv(
                data, filename, encoding=encoding, include_edge_cases=include_edge_cases
            )
            self.generated_files.append(file_path)
        
        # Excel format
        file_path = self.exporter.export_excel(data, f"operating_expenses_{prop_name}")
        self.generated_files.append(file_path)
        
        # Error files
        if include_errors:
            error_files = self.exporter.create_error_files(data, f"operating_expenses_{prop_name}_errors")
            self.generated_files.extend(error_files)
    
    def _export_tenant_roster(self, data: List[Dict[str, Any]], prop_name: str, include_edge_cases: bool, include_errors: bool):
        """Export tenant roster data"""
        # CSV files with different encodings
        encodings = ['utf-8', 'ascii', 'utf-16']
        for encoding in encodings:
            filename = f"tenant_roster_{prop_name}_{encoding}"
            file_path = self.exporter.export_csv(
                data, filename, encoding=encoding, include_edge_cases=include_edge_cases
            )
            self.generated_files.append(file_path)
        
        # Excel format
        file_path = self.exporter.export_excel(data, f"tenant_roster_{prop_name}")
        self.generated_files.append(file_path)
        
        # Error files
        if include_errors:
            error_files = self.exporter.create_error_files(data, f"tenant_roster_{prop_name}_errors")
            self.generated_files.extend(error_files)
    
    def _export_noi_data(self, data: List[Dict[str, Any]], prop_name: str, include_edge_cases: bool, include_errors: bool):
        """Export NOI data"""
        # CSV files with different encodings
        encodings = ['utf-8', 'ascii', 'utf-16']
        for encoding in encodings:
            filename = f"noi_data_{prop_name}_{encoding}"
            file_path = self.exporter.export_csv(
                data, filename, encoding=encoding, include_edge_cases=include_edge_cases
            )
            self.generated_files.append(file_path)
        
        # Excel format
        file_path = self.exporter.export_excel(data, f"noi_data_{prop_name}")
        self.generated_files.append(file_path)
        
        # Error files
        if include_errors:
            error_files = self.exporter.create_error_files(data, f"noi_data_{prop_name}_errors")
            self.generated_files.extend(error_files)
    
    def _export_market_analysis(self, data: List[Dict[str, Any]], prop_name: str, include_edge_cases: bool, include_errors: bool):
        """Export market analysis data"""
        # CSV files with different encodings
        encodings = ['utf-8', 'ascii', 'utf-16']
        for encoding in encodings:
            filename = f"market_analysis_{prop_name}_{encoding}"
            file_path = self.exporter.export_csv(
                data, filename, encoding=encoding, include_edge_cases=include_edge_cases
            )
            self.generated_files.append(file_path)
        
        # Excel format
        file_path = self.exporter.export_excel(data, f"market_analysis_{prop_name}")
        self.generated_files.append(file_path)
        
        # Error files
        if include_errors:
            error_files = self.exporter.create_error_files(data, f"market_analysis_{prop_name}_errors")
            self.generated_files.extend(error_files)
    
    def _generate_data_dictionaries(self):
        """Generate data dictionaries for all field types"""
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
            file_path = self.exporter.export_data_dictionary(fields_dict, dict_name)
            self.generated_files.append(file_path)
    
    def _generate_summary_report(self):
        """Generate a summary report of all generated files"""
        print("\n📄 Generating summary report...")
        
        summary_data = {
            "generation_date": date.today().isoformat(),
            "total_files_generated": len(self.generated_files),
            "files_by_type": {},
            "files_by_property_type": {},
            "files_by_encoding": {},
            "files_by_format": {}
        }
        
        # Analyze generated files
        for file_path in self.generated_files:
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
            
            # Count by format
            if filename.endswith(".csv"):
                summary_data["files_by_format"]["csv"] = summary_data["files_by_format"].get("csv", 0) + 1
            elif filename.endswith(".xlsx"):
                summary_data["files_by_format"]["xlsx"] = summary_data["files_by_format"].get("xlsx", 0) + 1
            elif filename.endswith(".xls"):
                summary_data["files_by_format"]["xls"] = summary_data["files_by_format"].get("xls", 0) + 1
        
        # Export summary report
        summary_file = self.output_dir / "generation_summary.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary_data, f, indent=2)
        
        self.generated_files.append(summary_file)
        
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
        
        summary_text += "\n## Files by Format\n"
        for format_type, count in summary_data["files_by_format"].items():
            summary_text += f"- **{format_type.upper()}**: {count} files\n"
        
        summary_text += "\n## Files by Encoding\n"
        for encoding, count in summary_data["files_by_encoding"].items():
            summary_text += f"- **{encoding.upper()}**: {count} files\n"
        
        summary_text += f"""
## Generated Files
"""
        for file_path in sorted(self.generated_files):
            summary_text += f"- {file_path.name}\n"
        
        summary_text += """
## Usage Notes
- All CSV files include headers
- Excel files include formatting and auto-sized columns
- Error files are included for validation testing
- Edge cases are included in some files for comprehensive testing
- Data dictionaries document all field meanings and formats

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
        summary_text_file = self.output_dir / "README.md"
        with open(summary_text_file, 'w', encoding='utf-8') as f:
            f.write(summary_text)
        
        self.generated_files.append(summary_text_file)


def main():
    """Main entry point for the script"""
    parser = argparse.ArgumentParser(description="Generate synthetic test data for SRS Document Generator")
    parser.add_argument("--output-dir", "-o", type=Path, default=Path("test_resources"),
                       help="Output directory for generated files (default: test_resources)")
    parser.add_argument("--seed", "-s", type=int, default=None,
                       help="Random seed for reproducible generation")
    parser.add_argument("--no-edge-cases", action="store_true",
                       help="Skip generating edge cases")
    parser.add_argument("--no-errors", action="store_true",
                       help="Skip generating error files")
    
    args = parser.parse_args()
    
    # Create output directory
    args.output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize and run generator
    generator = SRSDataGenerator(args.output_dir, args.seed)
    
    try:
        generator.generate_all_data(
            include_edge_cases=not args.no_edge_cases,
            include_errors=not args.no_errors
        )
        print("\n🎉 Data generation completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error during data generation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    import random
    import json
    main()
