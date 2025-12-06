from __future__ import annotations

import os
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Configure OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Default model (can override via env)
DEFAULT_MODEL = os.getenv("GOLDEN_DATA_MODEL", "gpt-4.1-mini")

# ---------------------------------------------------------------------------
# System prompt: Bossard-focused senior taxonomist / information architect
# ---------------------------------------------------------------------------

system_prompt = """
You are a senior ecommerce data taxonomist, information architect, and industrial product
strategist specializing in fasteners, electromechanical components, and engineered hardware.

Your primary context is Bossard’s North American BigCommerce catalog and the 2026
marketing strategy. You think like:

- A **data taxonomist** (fields, vocabularies, mappings, governance)
- An **industrial engineer** (fit, form, function, standards, dimensions)
- A **B2B marketer** (SEO, ABM, vertical campaigns, sales enablement)

All your assessments and recommendations must be guided by Bossard’s four 2026
North American Marketing Objectives (pillars):

1. Brand Expansion Across North America
   - Unified naming, standardized taxonomy, consistent attribute presentation
   - Stronger brand authority and co-marketing alignment with strategic suppliers

2. Industry-Specific Demand Generation
   - Data structures that enable vertical campaigns for:
     Data Center, EV, Robotics, Medical, Defense, Industrial Automation, etc.
   - Attributes that support vertical landing pages, assortments, and ABM targeting

3. Digital Excellence & Marketing Automation
   - Structured attributes that drive:
     - SEO titles and meta descriptions
     - Faceted navigation and filters
     - AI-powered search and recommendations
     - Automated metadata and content generation

4. Tight Sales Alignment With Measurable Revenue Impact
   - Product data that supports:
     - Fast, accurate quoting and engineering credibility
     - Upsell / cross-sell pathways
     - Supplier co-marketing and reporting by vertical, product family, and attribute
     - Pipeline attribution and forecasting

General behavior:

- Be specific and practical, not hand-wavy.
- When you suggest actions, explicitly map them back to one or more pillars.
- Distinguish clearly between:
  - Short-term fixes (0–4 weeks)
  - Medium-term roadmap (4–12+ weeks)
  - Long-term governance improvements.

Your outputs will be shared with Bossard’s Director of Marketing and internal stakeholders,
so they must be clear, structured, and executive-friendly.
"""

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _extract_text_from_response(resp) -> str:
    """
    Extract concatenated text from a Responses API response.
    Adjust this if your response object shape differs.
    """
    chunks: list[str] = []
    # responses.create → resp.output[0].content[*].text
    if hasattr(resp, "output"):
        for item in resp.output[0].content:
            # Newer SDKs: item has .type and .text
            if getattr(item, "type", None) in ("output_text", "message"):
                text = getattr(item, "text", None)
                if text:
                    chunks.append(text)
    # Fallback if structure differs
    if not chunks and hasattr(resp, "choices"):
        chunks.append(resp.choices[0].message.content)
    return "\n".join(chunks).strip()


def _get_model(model: Optional[str] = None) -> str:
    """
    Use explicit model if provided, otherwise fall back to DEFAULT_MODEL.
    """
    return model or DEFAULT_MODEL


# ---------------------------------------------------------------------------
# 1) Detailed custom field analysis
# ---------------------------------------------------------------------------


def _build_custom_fields_user_prompt(cf_md: str) -> str:
    """
    Build the user prompt for detailed custom field / attribute analysis.
    `cf_md` is a markdown table of custom fields (name, usage, example values).
    """
    return f"""
Below is a markdown table summarizing custom fields from a BigCommerce product export.
Each row includes the field name, product count, usage percent, and example values.

Custom Field Summary (subset):
{cf_md}

Your task is to analyze this dataset with the following goals:

1. Identify **attribute issues** including:
   - Unit inconsistencies (e.g., inches vs mm, mixed formats)
   - Missing values / sparse fields
   - Contaminated fields (mixed semantic types, e.g., dates in thread size)
   - Overloaded fields (multiple concepts in one field, e.g., size + unit + notes)
   - Supplier-specific or non-customer-friendly values
   - Duplicated or synonymous attributes (e.g., Material vs Materials vs Base Material)
   - Ambiguous labels (“Size”, “Class”, “Type”, etc.) and what they actually represent

2. For each issue, classify severity:
   - **Critical** — blocks SEO, taxonomy, AI search, or sales alignment
   - **High** — major normalization required, impacts navigation or filters
   - **Medium** — helpful but not foundational
   - **Low** — noise, cosmetic, or should be deprecated

3. Provide **specific recommendations** for remediation:
   - Mapping tables needed (e.g., Material, Finish, Thread Size, Head Style)
   - Value normalization rules (e.g., “Stainless”, “SS” → “Stainless Steel”)
   - Unit standardization rules (e.g., store mm internally, show in inches as needed)
   - Field splitting or merging (e.g., “Size” into Length / Width / Height)
   - Controlled vocabulary proposals for key attributes
   - Transformations to extract structured dimensional values from free text

4. Explicitly connect each recommendation to one or more Bossard marketing pillars:
   - Brand Expansion
   - Industry-Specific Demand Generation
   - Digital Excellence & Marketing Automation
   - Sales Alignment & Revenue Impact

5. End with a recommended **attribute roadmap** answering:
   - Which 8–12 attributes should be normalized first (Phase 1)
   - Which attributes should be deferred to Phase 2
   - Which attributes should be deprecated entirely
   - Which attributes require new governance rules (naming standards, required fields, units)

Format your answer as:

- A short narrative overview (2–4 paragraphs)
- A structured list of issues & severities by attribute or attribute group
- A clear, bullet-point roadmap (Phase 1, Phase 2, Governance)
- Pillar tags in square brackets where relevant, e.g. [Brand Expansion, Digital Excellence]
"""


def analyze_custom_fields(cf_md: str, model: Optional[str] = None) -> str:
    """
    Analyze custom field summary markdown and return a detailed, pillar-aware narrative.

    Parameters
    ----------
    cf_md : str
        Markdown table produced from custom field summary (Field_Name, Product_Count, etc.)
    model : str, optional
        Override default model if desired.

    Returns
    -------
    str
        Human-readable analysis suitable for internal documentation or reports.
    """
    user_prompt = _build_custom_fields_user_prompt(cf_md)

    resp = client.responses.create(
        model=_get_model(model),
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return _extract_text_from_response(resp)


# ---------------------------------------------------------------------------
# 2) Higher-level strategy & next-step summary
# ---------------------------------------------------------------------------


def summarize_attribute_strategy(
    cf_md: str,
    coverage_md: Optional[str] = None,
    material_md: Optional[str] = None,
    finish_md: Optional[str] = None,
    mapping_status_notes: Optional[str] = None,
    model: Optional[str] = None,
) -> str:
    """
    Produce an executive-friendly summary and next-step plan tied to Bossard's marketing pillars.

    Inputs (markdown tables and notes):
      - cf_md:       custom field summary (top fields, usage, example values)
      - coverage_md: Phase 1 coverage table (Field_Name, Products_With_Value, Coverage_Percent)
      - material_md: top Material values table (for normalization context)
      - finish_md:   top Finish values table
      - mapping_status_notes: free text notes on current normalization work
        (e.g., "Material/Finish mappings drafted, normalization functions implemented")

    Output:
      - Narrative suitable for an executive brief or strategy slide.
    """

    context_parts: list[str] = [f"Custom Field Summary:\n{cf_md}\n"]

    if coverage_md:
        context_parts.append(f"Phase 1 Attribute Coverage:\n{coverage_md}\n")
    if material_md:
        context_parts.append(f"Sample Material Values (top raw values):\n{material_md}\n")
    if finish_md:
        context_parts.append(f"Sample Finish Values (top raw values):\n{finish_md}\n")
    if mapping_status_notes:
        context_parts.append(f"Current Mapping / Normalization Status:\n{mapping_status_notes}\n")

    context_block = "\n\n".join(context_parts)

    user_prompt = f"""
You are advising Bossard's North American Director of Marketing.

Below is structured attribute analysis from the BigCommerce catalog export,
including custom field usage, Phase 1 coverage, and sample raw values for
Material and Finish:

{context_block}

Using this information, produce a **clear, executive-friendly summary** with
the following structure:

1. **Data Quality Snapshot (3–5 bullets)**
   - Describe the overall state of the product attribute data.
   - Highlight strengths (e.g., widely used fields like Material, Finish, Type, Thread).
   - Highlight risks/gaps (e.g., dimensional unit inconsistencies, noisy free-text fields).

2. **Phase 1 Priorities (0–4 weeks)**
   - List 5–8 concrete actions focused on:
     - Normalizing high-impact attributes (Material, Finish, Type, Thread, core dimensions).
     - Creating and validating mapping tables.
     - Establishing basic unit and formatting standards.
   - For each action, add pillar tags in square brackets:
     [Brand Expansion], [Vertical Demand], [Digital Excellence], [Sales Alignment]

3. **Phase 2 Roadmap (4–12 weeks)**
   - List 5–8 follow-on actions that build on Phase 1:
     - Expanding normalization to additional attributes (Head Style, RoHS, Temperature Rating, etc.).
     - Leveraging normalized attributes for SEO, vertical landing pages, AI search, reporting.
     - Formalizing governance and onboarding rules for new products.
   - Again, tag each action with relevant pillar(s).

4. **Bossard Marketing Objectives Alignment Summary**
   - For each pillar, write 2–3 sentences explaining:
     - How the golden dataset initiative advances that pillar.
     - What “good” will look like once Phase 1 + Phase 2 are implemented.

Tone and style:
- Professional and concise.
- Action-oriented: clearly state what should be done next and why.
- Suitable to paste into an internal strategy memo or slide deck.
"""

    resp = client.responses.create(
        model=_get_model(model),
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return _extract_text_from_response(resp)


# ---------------------------------------------------------------------------
# Optional: simple CLI entry for quick testing
# ---------------------------------------------------------------------------


def main():
    """
    Simple CLI harness for manual testing.

    Example usage:
        python -m golden_data.ai_taxonomist
    """
    sample_md = """| Field_Name | Product_Count | Usage_Percent | Example_Values |
| --- | --- | --- | --- |
| Material | 2479 | 2.78 | Steel, Stainless Steel, Nylon 6/6, Polypropylene |
| Finish | 1275 | 1.43 | Zinc Plated, Black Oxide, Plain, Tin |
| Length | 1437 | 1.61 | 8.000 in., 12 in., 75 mm |
"""
    print("=== Detailed Custom Field Analysis ===\n")
    print(analyze_custom_fields(sample_md))
    print("\n\n=== Strategy Summary ===\n")
    print(
        summarize_attribute_strategy(
            cf_md=sample_md,
            coverage_md=None,
            material_md=None,
            finish_md=None,
            mapping_status_notes="Demo run with synthetic sample_md.",
        )
    )


if __name__ == "__main__":
    main()