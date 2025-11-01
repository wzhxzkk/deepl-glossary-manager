#!/usr/bin/env python3
"""
Export Glossary Terms to File

Export your TERMS dictionary from glossary_manager.py to various formats
for backup, sharing, or version control.

Usage:
    python export_terms.py --format json --output my_terms.json
    python export_terms.py --format tsv --output my_terms.tsv
"""

import sys
import json
import argparse
from pathlib import Path

# Import TERMS from parent directory
sys.path.insert(0, str(Path(__file__).parent.parent))
try:
    from glossary_manager import TERMS
except ImportError:
    print("Error: Cannot import TERMS from glossary_manager.py")
    print("Make sure glossary_manager.py is in the parent directory")
    sys.exit(1)


def export_json(output_file):
    """Export terms to JSON format"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(TERMS, f, ensure_ascii=False, indent=2)
    print(f"✅ Exported {len(TERMS)} terms to {output_file} (JSON format)")


def export_tsv(output_file):
    """Export terms to TSV format (DeepL compatible)"""
    with open(output_file, 'w', encoding='utf-8') as f:
        for source, target in TERMS.items():
            f.write(f"{source}\t{target}\n")
    print(f"✅ Exported {len(TERMS)} terms to {output_file} (TSV format)")


def export_markdown(output_file):
    """Export terms to Markdown table format"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Glossary Terms\n\n")
        f.write("| English | Chinese | Type |\n")
        f.write("|---------|---------|------|\n")
        for source, target in TERMS.items():
            term_type = "保持英文" if source == target else "翻译"
            f.write(f"| {source} | {target} | {term_type} |\n")
    print(f"✅ Exported {len(TERMS)} terms to {output_file} (Markdown format)")


def main():
    parser = argparse.ArgumentParser(description='Export glossary terms to file')
    parser.add_argument('--format', '-f',
                       choices=['json', 'tsv', 'md'],
                       default='json',
                       help='Output format (default: json)')
    parser.add_argument('--output', '-o',
                       default='terms_export',
                       help='Output filename (without extension)')

    args = parser.parse_args()

    # Add extension if not provided
    if args.format == 'json' and not args.output.endswith('.json'):
        output_file = f"{args.output}.json"
    elif args.format == 'tsv' and not args.output.endswith('.tsv'):
        output_file = f"{args.output}.tsv"
    elif args.format == 'md' and not args.output.endswith('.md'):
        output_file = f"{args.output}.md"
    else:
        output_file = args.output

    print(f"\n📦 Exporting {len(TERMS)} terms from glossary_manager.py...")
    print(f"Format: {args.format.upper()}")
    print(f"Output: {output_file}\n")

    # Export based on format
    if args.format == 'json':
        export_json(output_file)
    elif args.format == 'tsv':
        export_tsv(output_file)
    elif args.format == 'md':
        export_markdown(output_file)

    print(f"\n💾 Backup completed!")
    print(f"You can now:")
    print(f"  - Commit {output_file} to version control")
    print(f"  - Share with colleagues")
    print(f"  - Keep as backup before updating terms")


if __name__ == "__main__":
    main()
