🧩 Bossard Golden Data Toolkit

A Fastener-Centric Data Normalization & Taxonomy Engine for BigCommerce

The Bossard Golden Data Toolkit is a Python-based framework for analyzing, cleaning, normalizing, and enriching product data extracted from BigCommerce.
It is designed to support Bossard’s 2026 North American Marketing Objectives, including:
	1.	Brand Expansion Across North America
	2.	Industry-Specific Demand Generation
	3.	Digital Excellence & Marketing Automation
	4.	Tight Sales Alignment with Measurable Revenue Impact

This toolkit provides a repeatable playbook for developing industrial-grade taxonomies, mapping raw supplier values into controlled vocabularies, standardizing dimensional units, and producing executive-ready reports using AI-assisted analysis.

⸻

📁 Repository Structure

bossard-golden-data/
│
├── src/golden_data/
│   ├── config.py                # Path management for raw/interim/mapping directories
│   ├── data_profiling.py       # Initial dataset validation, sampling, diagnostics
│   ├── custom_field_scan.py    # Custom field discovery + frequency analysis
│   ├── markdown_utils.py       # DataFrame → Markdown conversion for AI agents
│   ├── normalization.py        # Mapping tables + normalization utilities
│   ├── ai_taxonomist.py        # LLM-powered attribute analysis + strategy summaries
│   └── __init__.py
│
├── mappings/                   # Mapping tables generated from top-value analysis
│   ├── material_mapping.csv
│   ├── finish_mapping.csv
│   └── …
│
├── data/
│   ├── raw/                    # BigCommerce input files (not tracked in Git)
│   ├── interim/                # Saved samples, summaries, normalized slices
│   └── processed/              # Golden dataset exports (future)
│
├── reports/
│   └── attributes_report.md    # Executive-facing analysis output
│
├── notebooks/
│   ├── 01_data_profiling.ipynb
│   ├── 02_custom_fields_attributes_discovery.ipynb
│   └── 03_normalization_workflow.ipynb
│
├── pyproject.toml              # Project dependencies + dev/nb extras
├── README.md                   # (This file)
└── LICENSE (optional)

🚀 What This Toolkit Does

1. Data Profiling & Validation
	•	Loads BigCommerce CSVs
	•	Confirms required columns
	•	Saves sample slices (raw_sample_head50.csv)
	•	Produces overview tables (rows, columns, column preview)

2. Custom Field Discovery
	•	Parses JSON-based BigCommerce Custom Fields
	•	Counts usage frequency
	•	Extracts representative example values
	•	Produces:
	•	custom_field_summary.csv
	•	Top 20–50 values for normalization (Material, Finish, Thread, etc.)

3. Attribute Coverage Analysis
	•	Identifies Phase-1 target attributes
	•	Calculates:
	•	% coverage
	•	number of unique values
	•	data quality indicators
	•	Results feed into mapping table generation and AI analysis.

4. Mapping Table Generation
	•	Creates editable CSVs for:
	•	material_mapping.csv
	•	finish_mapping.csv
	•	…and any other attribute (Thread, Head Style, etc.)
	•	Allows humans (marketing + engineering) to standardize:
	•	Synonyms
	•	Noisy supplier values
	•	Spelling/format inconsistencies

5. Value Normalization Engine
	•	Applies mappings to raw fields
	•	Handles unmapped values using policies:
	•	keep_raw
	•	set_nan
	•	flag
	•	Ready for:
	•	BigCommerce enriched exports
	•	Data warehouse ingestion
	•	Analytics workflows

6. AI-Assisted Analysis

The ai_taxonomist module includes:

analyze_custom_fields()
Detailed diagnostic:
	•	attribute issues
	•	severities
	•	normalization recommendations
	•	structured roadmaps
	•	pillar alignment

summarize_attribute_strategy()
Executive-facing strategic summary:
	•	data quality snapshot
	•	Phase 1 plan (0–4 weeks)
	•	Phase 2 plan (4–12 weeks)
	•	explicit mapping to all four Bossard marketing pillars

This produces the narrative included in reports/attributes_report.md.

⸻

🧠 Why This Project Matters

Bossard’s BigCommerce catalog is a critical customer-facing gateway.
But raw supplier product data is inconsistent across:
	•	dimensional units
	•	material & finish naming
	•	thread formats
	•	head style descriptions
	•	compliance and features

This toolkit produces the Golden Dataset—a unified, normalized, marketing-aligned dataset that powers:
	•	SEO automation
	•	faceted navigation
	•	AI search
	•	vertical landing pages
	•	co-marketing with suppliers
	•	faster, more accurate quoting
	•	attribute-driven ABM targeting

⸻

🛠 Installation

Standard installation

pip install -e .

With dev + notebook extras
pip install -e ".[dev,notebook]"

Requirements
	•	Python 3.10+
	•	Pydantic, Pandas, Rich
	•	OpenAI Python SDK
	•	Jupyter, ipykernel
	•	dotenv for environment variables

⸻

🔧 Environment Configuration
1.	Create a .env file:
    OPENAI_API_KEY=your_key_here
    GOLDEN_DATA_MODEL=gpt-4.1-mini
2.  Place your BigCommerce product CSV into:data/raw/bigcommerce_export.csv
data/raw/bigcommerce_export.csv

📓 Workflow Summary (Notebooks)

Notebook 01 — Data Profiling
	•	Load / validate raw CSV
	•	Inspect column distribution
	•	Save reference sample

Notebook 02 — Attribute Discovery
	•	Run custom field scan
	•	Generate top-value tables
	•	Analyze coverage
	•	Feed data into AI taxonomist
	•	Produce attributes_report.md

Notebook 03 — Normalization
	•	Generate mapping templates
	•	Normalize Material, Finish, etc.
	•	Prepare Phase-1 golden dataset slices
	•	Export: data/processed/golden_products_phase1.csv

✨ Outputs

📄 custom_field_summary.csv

Frequency & examples of all custom fields.

📄 *_top_values.csv

Top raw values for key attributes.

📄 material_mapping.csv, finish_mapping.csv, …

Stakeholder-editable mapping tables.

📄 attributes_report.md

Executive-ready strategy brief.

⸻

🧭 Roadmap
Phase
Outcome
Phase 1
Normalize Material, Finish, Thread, Dimensions
Phase 2
Expand vocabularies, parse dimensions, enrich SEO metadata
Phase 3
Full Golden Product Dataset powering BigCommerce + CDP + Marketing Automation
Phase 4
Governance automation for new product onboarding

🤝 Contributing

This project is designed to evolve. New mappings, attribute rules, dimension parsers, and AI prompt refinements are welcomed.

📝 License

You may add MIT, Apache, or internal-use licensing as preferred.

⸻

Questions or Enhancements?

Open an issue or reach out directly if you want:
	•	Additional agents (SEO agent, vertical-copy agent)
	•	A CLI wrapper to run the full pipeline end-to-end
	•	Automatic mapping suggestions from AI
	•	Integration with Supabase or Snowflake for production deployment
