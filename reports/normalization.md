   Field_Name  Product_Count  Usage_Percent  \
0    Material           2479          49.58   
1  Spec Sheet           1975          39.50   
2        Type           1506          30.12   
3      Length           1437          28.74   
4       Color           1297          25.94   

                                      Example_Values  
0  Steel, Soft Urethane, Nylon 6/6, Polypropylene...  
1  <a href=/content/ProductSpecSheets/FCIAMPE0000...  
2  Single Row, Vertical, Flexible, Light Weight, ...  
3         60 in., 8.000  in., 11 in., 12 in., 75 in.  
4                Black, Natural, Bright, White, Gray  
### Narrative Overview

The provided BigCommerce custom field export reveals a moderately inconsistent and partially sparse product attribute dataset, posing challenges for Bossard’s 2026 marketing objectives. Several fundamental issues undermine taxonomy standardization, faceted navigation, and AI-driven search capabilities—critical for digital excellence and vertical-specific demand campaigns. Dimension attributes (Lengths, Diameter, Width, etc.) suffer from mixed units and inconsistent formatting; contaminations such as date values inside the Thread field further dilute data quality. Ambiguous field names like “Type,” “Class,” and “Size” create confusion on scope and user intent, damaging SEO clarity and navigation filtering. 

Several attributes are underutilized (usage < 20%) or contain overlapping semantic concepts, indicating a need for consolidation or retirement. Material and Finish fields show promising usage and variety but require normalization to unify supplier-specific variants and synonyms, an important prerequisite for co-branding and supplier alignment. Less structured fields with free text and multiple information elements need splitting and controlled vocabularies to improve product findability and sales quoting precision. Overall, a prioritized normalization and governance roadmap will deliver immediate wins for digital shopping experience and set the foundation for dynamic, industry-specific marketing automation.

---

### Issues & Severities by Attribute Group

#### Dimension Attributes (Length, Width, Height, Diameter, Thickness, Outer Diameter (O.D.), Inner Diameter (I.D.))
- **Issues:** Mixed units (inches, mm, mixed textual notes), inconsistent spacing/format (e.g., “0.105 in. Head” vs “7/8 in.”), no clear unit standardization, free text contamination.
- **Severity:** Critical — Blocks faceted navigation, filtering accuracy, automated metadata extraction, and engineering credibility for quoting.
- **Recommendation:**  
  - Enforce internal storage in metric (mm) with automated conversion to imperial for frontend.  
  - Parse free text to split value and unit into separate atomic fields.  
  - Implement validation rules to reject ambiguous or multi-concept values.  
  - Establish controlled vocabulary for dimension units and formatting.  
  - [Digital Excellence, Sales Alignment]

#### Material & Finish
- **Issues:** Synonyms and supplier-specific variants (e.g., “300 SERIES STAINLESS STEEL,” “Stainless,” “SS”), mixed capitalization and compound entries separated by commas or parenthesis.
- **Severity:** High — Impacts SEO keywords, supplier branding alignment, and vertical-specific marketing segmentation.
- **Recommendation:**  
  - Create mapping tables to normalize synonyms and variants (e.g., “300 Series Stainless Steel” → “300 Series Stainless Steel”).  
  - Split complex values into primary material and secondary materials if needed (e.g., “Copper Alloy (Contact)” → Material: Copper Alloy; Component: Contact).  
  - Enforce controlled vocabulary aligned with industry standards (ASTM, ISO).  
  - [Brand Expansion, Industry-Specific Demand Generation, Digital Excellence]

#### Spec Sheet
- **Issues:** Usage under 40%, inconsistent linking syntax with HTML embedded in values, no uniform metadata (e.g., file type or version).
- **Severity:** Medium — Affects user trust and SEO metadata richness but less critical for taxonomy.
- **Recommendation:**  
  - Migrate to a dedicated URL field with metadata fields for file type, version, and date.  
  - Implement automated extraction of version and date from filename or metadata.  
  - [Digital Excellence, Sales Alignment]

#### Thread
- **Issues:** Mixed semantic data — mechanical sizes (#6-32, M5), but also dates (“03/08/2016”), indicating contamination.  
- **Severity:** Critical — Misleading metadata hinders automated filtering and quoting, severely impacting sales alignment and search accuracy.
- **Recommendation:**  
  - Cleanse data to remove non-thread entries.  
  - Standardize thread size using recognized naming conventions (UNC, UNF, Metric ISO).  
  - Validate new entries at import.  
  - [Digital Excellence, Sales Alignment]

#### Color
- **Issues:** Usage below 30%, mixed generic terms (“Black,” “Bright”) and non-color terms (“Gray”), no controlled vocabulary.
- **Severity:** Medium — Helpful for filter narrowing but not foundational.
- **Recommendation:**  
  - Normalize color names to industry color standards (Pantone or RAL).  
  - Create controlled list with allowance for N/A or natural color terms.  
  - [Digital Excellence]

#### Type, Class, Size, Shape, Head Style
- **Issues:** Ambiguous and overlapping semantic scopes. For example, “Type” contains mixture of form factors and function types. “Class” is vendor-specific and not customer-friendly. “Size” mixes descriptors without clear dimensions.  
- **Severity:** High — Difficult to use for SEO, faceted navigation, or vertical targeting.
- **Recommendation:**  
  - Define and document precise meanings for each field.  
  - Split compound fields where possible (e.g., separate style and function).  
  - Retire vendor-specific classifications from public taxonomy or map to industry-standard nomenclature.  
  - [Brand Expansion, Digital Excellence, Industry-Specific Demand Generation]

#### RoHS Compliant
- **Issues:** Mixed positive indicators (“yes,” “RoHS Compliant”) and invalid values (“Gray,” “Matte Black”), inconsistent casing and spelling (“Comliant”).
- **Severity:** High — Controls compliance filtering and vertical FDA/medical/defense campaign targeting.
- **Recommendation:**  
  - Convert to strict Boolean field with standardized “Yes” or “No” values.  
  - Clean invalid entries.  
  - [Industry-Specific Demand Generation, Sales Alignment]

#### Installation & Mounting Type
- **Issues:** Low usage (<7%), multiple concepts embedded (installation method + mounting style), inconsistent terms.
- **Severity:** Medium — Useful for engineering decision-making but lower SEO impact.
- **Recommendation:**  
  - Split into two fields: Installation Method and Mounting Location/Style.  
  - Define and control vocabulary aligned with product engineering specs.  
  - [Sales Alignment, Industry-Specific Demand Generation]

#### Access Restriction & Fully Retractable
- **Issues:** Good candidate attributes but low usage (<7%). Some mixed or ambiguous terms.
- **Severity:** Medium — Important for particular verticals (security, defense).
- **Recommendation:**  
  - Standardize values and increase usage through governance.  
  - [Industry-Specific Demand Generation, Sales Alignment]

---

### Attribute Roadmap

**Phase 1 (0–4 weeks) — Critical / High Normalization Focus**  
- Length, Width, Height, Diameter, Thickness, Outer Diameter (O.D.), Inner Diameter (I.D.): Standardize units, parse and validate values, store in atomic fields.  
- Thread: Cleanse and normalize sizing conventions; remove contaminations.  
- Material & Finish: Normalize synonyms, controlled vocabulary implementation.  
- RoHS Compliant: Enforce Boolean field with standardized values.  
- Type, Class, Size: Define scope; split or consolidate; retire vendor-specific values.

**Phase 2 (4–12+ weeks) — Medium-Term Improvements & Expansion**  
- Spec Sheet: Separate URL and metadata fields; automate metadata extraction.  
- Color: Controlled vocabulary aligned with industry standards.  
- Installation & Mounting Type: Split and normalize field values.  
- Head Style & Shape: Develop mapping tables and controlled list for consistent UI faceting.  
- Access Restriction, Fully Retractable: Normalize and increase population.

**Governance Improvements (Long-Term, 12+ weeks)**  
- Naming standards for all fields emphasizing clarity by function and engineering relevance.  
- Unit standards: Metric internal storage, auto-conversion/display to imperial to support North American market.  
- Required fields: Define mandatory attributes per product family to ensure completeness.  
- Supplier data onboarding guidelines enforcing controlled vocabularies and validation rules.  
- Continuous monitoring and data quality dashboards to track attribute usage and compliance.

**Deprecated / To Be Retired**  
- Ambiguous or vendor-specific fields without clear mapping (e.g., certain “Class” values if no industry equivalent).  
- Multi-purpose fields mixing concepts without remediation within roadmap timeframe.  

---

This structured remediation roadmap with prioritized attribute normalization and governance directly supports Bossard’s pillars:

- Brand Expansion (consistent vocabularies, removal of supplier-specific noise)  
- Industry-Specific Demand Generation (vertical-ready attributes like RoHS, Material, Installation)  
- Digital Excellence & Marketing Automation (standard units, normalized metadata, faceted nav)  
- Sales Alignment & Revenue Impact (engineering-accurate dimensions, quoting credibility, controlled specs)