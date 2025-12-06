# Bossard BigCommerce Attribute Discovery Report

**Prepared by:** Golden Data Toolkit  
**Data Source:** bossard_raw.csv  
**Records Analyzed:** 175917 products (raw export)  
**Custom Field Sample:** First 5,000 product rows

---

## 1. Objective

This analysis reviews the current BigCommerce custom field structure and attribute usage
to identify:

- Gaps and inconsistencies in product attributes
- High-value attributes for normalization and taxonomy design
- Priority steps to enable Bossard’s 2026 North American marketing objectives:

1. **Brand Expansion Across North America**  
2. **Industry-Specific Demand Generation**  
3. **Digital Excellence & Marketing Automation**  
4. **Tight Sales Alignment With Measurable Revenue Impact**

---

## 2. Data Validation Summary

- **File path:** `/Users/csmiller/projects/bossard-golden-data/data/raw/bossard_raw.csv`
- **Total rows in export:** 175917
- **Total columns in export:** 50
- **Contains 'Custom Fields' column:** Yes
- **Contains 'Item' filter column:** Yes

A subset of up to 5,000 product rows was used for custom field analysis.

---

## 3. Top Custom Attributes (Usage Snapshot)

The table below shows the most frequently used custom fields across the analyzed products:

| Field_Name | Product_Count | Usage_Percent | Example_Values |
| --- | --- | --- | --- |
| Material | 2479 | 49.58 | Steel, Soft Urethane, Nylon 6/6, Polypropylene (Housing), Copper Alloy (Contact), 300 SERIES STAINLESS STEEL |
| Spec Sheet | 1975 | 39.5 | <a href=/content/ProductSpecSheets/FCIAMPE00003_1-14.pdf&quot; target=&quot;_blank&quot;>Specification Sheet</a>, <a href=/content/ProductSpecSheets/LAIRTCE00001_3_54-58.pdf&quot; target=&quot;_blank&quot;>Specification Sheet</a>, <a href=/content/ProductSpecSheets/NORTONE00217_79-81.pdf&quot; target=&quot;_blank&quot;>Specification Sheet</a>, <a href=/content/ProductSpecSheets/NORTONE00217_104_105.pdf&quot; target=&quot;_blank&quot;>Specification Sheet</a>, <a href=/content/ProductSpecSheets/NORTONE00217_90_93_94.pdf&quot; target=&quot;_blank&quot;>Specification Sheet</a> |
| Type | 1506 | 30.12 | Single Row, Vertical, Flexible, Light Weight, Fabric-Over-Foam, Shielding/Grounding/Compression/Shear Gasket, Quick Change, TS (Type II), Closed Coat |
| Length | 1437 | 28.74 | 60 in., 8.000  in., 11 in., 12 in., 75 in. |
| Color | 1297 | 25.94 | Black, Natural, Bright, White, Gray |
| Finish | 1275 | 25.5 | Natural, Bright Electro Plated Zinc, Clear Electro Plated, Black, Powder Coat |
| RoHS Compliant | 972 | 19.44 | yes, RoHS Compliant, RoHS Comliant, Gray, Matte Black |
| Class | 789 | 15.78 | 47/4C - Captive Screws, E5 - Cam Latches, 96 - Removable Lift-Off Hinges, CM - Cam Lock Latches, 09/12/17 - Fast Lead Captive Screws |
| Width | 780 | 15.6 | 1/2 in., 37 in., 9 in., 0.25  in., 0.395  in. |
| Height | 691 | 13.82 | 0.08  in., 0.04  in., 0.12  in., 0.06  in., 0.25  in. |
| Thread | 598 | 11.96 | #6-32, #10, M5, #8, M4, 03/08/2016, 01/04/2020 |
| Diameter | 579 | 11.58 | 5 in., 2 in., 0.013  in., 4-1/2 in., 7 in. |
| Shape | 424 | 8.48 | Hexagon, Dome Head, Rectangle, Round, Countersunk Head |
| Head Style | 381 | 7.62 | Phillips Recess, Slotted Recess, Phillips/Slot Combination, 8  mm Hex Recess, Locking |
| Mounting Type | 320 | 6.4 | Side, Front Mount, Concealed Mount, Side/Bracket/Hard, Side/Flat, Diamond/Square Shaped Hole |
| Installation | 320 | 6.4 | Flare-in, Rivet / Screw (thru hole), Press-in, Floating, Snap-In |
| Access Restriction | 312 | 6.24 | No Restriction, Tool, Key Locking, Secondary Catch Accessory, Pad Lockable |
| Size | 286 | 5.72 | Medium Size, Small Size, Large Size, 5 in. X NH, Standard |
| Grip Range | 284 | 5.68 | 1, 1.5, 2, 3, 0.085 to 0.135 in. |
| Temperature Rating | 283 | 5.66 | -40 to 158 Deg F, -4 to 221 Deg F, 85 Deg C, -40 to 105 Deg C, 105 Deg F |


---

## 4. Phase-1 Attribute Coverage

The following attributes are proposed as **Phase 1** for normalization:

- Material, Finish, Type, Thread  
- Length, Diameter, Width, Height  
- Head Style, RoHS Compliant

Coverage across the catalog:

| Field_Name | Products_With_Value | Coverage_Percent | Unique_Values |
| --- | --- | --- | --- |
| Material | 6178 | 6.94 | 205 |
| Type | 3994 | 4.49 | 1609 |
| Finish | 3557 | 4.0 | 137 |
| Thread | 3223 | 3.62 | 204 |
| Length | 2937 | 3.3 | 1098 |
| RoHS Compliant | 1381 | 1.55 | 7 |
| Width | 1024 | 1.15 | 352 |
| Height | 832 | 0.93 | 319 |
| Diameter | 806 | 0.91 | 257 |
| Head Style | 636 | 0.71 | 72 |


**Interpretation:**

- High-coverage fields are ideal for first-wave normalization because improvements will benefit a large portion of the catalog.
- Fields with many unique values (especially Material and Finish) are strong candidates for mapping tables and controlled vocabularies.

---

## 5. Sample Raw Values (Material & Finish)

These tables illustrate the kind of raw values that will be normalized.

### 5.1 Material (top examples)

| Material_Value | Count |
| --- | --- |
| Steel | 1613 |
| 300 SERIES STAINLESS STEEL | 936 |
| Stainless Steel | 607 |
| Aluminum | 381 |
| Nylon 6/6 | 350 |
| Zinc Alloy | 271 |
| 400 SERIES STAINLESS STEEL | 151 |
| Copper | 114 |
| 303 Stainless Steel | 90 |
| Soft Urethane | 89 |
| Dry Film Lubricant | 89 |
| Brass | 82 |
| Plastic | 78 |
| SEE TABLE | 73 |
| FREE-MACHINING,LEADED BRASS | 67 |


### 5.2 Finish (top examples)

| Finish_Value | Count |
| --- | --- |
| Passivated and/or tested per ASTM A380 | 1096 |
| Natural | 256 |
| Zinc Plate, Bright chromate | 244 |
| Powder Coat | 230 |
| Passivated | 155 |
| Bright Electro Plated Zinc | 103 |
| Plain | 95 |
| Chrome Plated | 91 |
| SEE TABLE | 73 |
| Non-Plated | 60 |
| Black | 56 |
| Zinc Plated | 56 |
| Natural (Rivet) | 50 |
| Clear Electro Plated | 47 |
| Electro-Plated Tin, ASTM B545, Class B with Preservative Coating, Annealed | 46 |


These samples highlight:

- Synonymous or near-duplicate values (e.g., “Stainless”, “Stainless Steel”, “SS”)
- Supplier-specific or overly detailed strings that should be mapped to clean, customer-facing terms
- Spelling or formatting inconsistencies that will be addressed in the golden dataset

---

## 6. AI Taxonomist Analysis

The following analysis was generated by an AI “senior taxonomist” agent tuned to Bossard’s 2026 strategy.
It reviews attribute quality, severity of issues, and recommends a roadmap for normalization and governance.

To analyze the provided dataset effectively, we will focus on the following goals:

1. **Identify Key Attributes**: Determine which attributes are most significant for product categorization and customer decision-making.
2. **Assess Data Completeness**: Evaluate the completeness of the data for each attribute and identify any gaps.
3. **Understand Usage Trends**: Analyze the usage percentage of each attribute to understand which are most commonly utilized.
4. **Categorize Attributes**: Group attributes into relevant categories for better organization and navigation.
5. **Recommendations for Improvement**: Provide actionable recommendations based on the analysis.

### 1. Identify Key Attributes
From the dataset, the following attributes stand out as key for product categorization:

- **Material**: High product count and diverse examples indicate its importance in product differentiation.
- **Type**: Essential for understanding product functionality and application.
- **Spec Sheet**: Critical for providing detailed product information to customers.
- **Dimensions (Length, Width, Height, Diameter, Thickness)**: Important for ensuring compatibility and fit for various applications.
- **Color and Finish**: Aesthetic attributes that influence customer choices.

### 2. Assess Data Completeness
- **Material**: High product count (2479), indicating good coverage.
- **Spec Sheet**: 1975 products have this attribute, but it could be improved by ensuring all products have a spec sheet.
- **Type**: 1506 products, but there may be opportunities to standardize types for better clarity.
- **Dimensions**: Length (1437), Width (780), Height (691), Diameter (579), and Thickness (222) show varying levels of completeness, with Thickness being the least populated.
- **Color and Finish**: Both attributes have a decent number of products, but there may be additional colors or finishes that could be added.

### 3. Understand Usage Trends
- The **Material** attribute has the highest usage percentage (49.58%), suggesting it is a critical factor for customers.
- **Spec Sheet** (39.5%) and **Type** (30.12%) also show significant usage, indicating that customers value detailed specifications and product classifications.
- Attributes like **Grip Range** (5.68%) and **Temperature Rating** (5.66%) have lower usage percentages, suggesting they may not be as critical for the majority of products.

### 4. Categorize Attributes
Attributes can be grouped into the following categories:

- **Product Specifications**: Material, Type, Dimensions (Length, Width, Height, Diameter, Thickness), Temperature Rating.
- **Aesthetic Attributes**: Color, Finish.
- **Functional Attributes**: RoHS Compliant, Class, Mounting Type, Installation, Access Restriction, Grip Range.
- **Product Documentation**: Spec Sheet.

### 5. Recommendations for Improvement
- **Enhance Data Completeness**: Encourage the addition of missing spec sheets for products and ensure all relevant dimensions are captured.
- **Standardize Attribute Values**: For attributes like Type and Class, consider creating a standardized list to improve consistency and searchability.
- **Increase Visibility of Low-Usage Attributes**: Promote attributes like Grip Range and Temperature Rating in product descriptions to educate customers on their importance.
- **Utilize Analytics for Customer Insights**: Implement analytics to track which attributes customers filter by or inquire about, allowing for data-driven decisions on which attributes to prioritize.

### Conclusion
The analysis of the dataset reveals that while many attributes are well-represented, there are opportunities for improvement in data completeness and standardization. By focusing on key attributes and enhancing the overall data quality, the ecommerce platform can better serve its customers and improve the shopping experience.

---

## 7. Recommended Normalization Roadmap

Based on the attribute scan and AI analysis, the following **Phase 1** attributes are recommended
for normalization and governance:

- **Core dimensional attributes:** Length, Width, Height, Diameter, Grip Range  
- **Core material & finish attributes:** Material, Finish, Plating/Coating  
- **Fastener identity attributes:** Type, Head Style, Thread, Size/Class  
- **Compliance & restrictions:** RoHS Compliant, Access Restriction  

(Additional narrative can stay as previously drafted, or be lightly edited here.)

---

## 8. Actions for Bossard Marketing Excellence

(Reuse or adapt the earlier “Actions aligned to the four pillars” section – your previous text already fits nicely.)

---

## 9. Next Steps

1. Approve Phase 1 attribute scope and normalization approach.
2. Build mapping tables for Material and Finish (seeded from the exported `*_top_values.csv` files).
3. Design and implement parsing & unit standardization rules for Length and other dimensional fields.
4. Validate the golden attribute set on a targeted subset (e.g., one supplier, one fastener family).
5. Deploy normalized attributes into BigCommerce and review SEO, navigation, and AI search behavior.
6. Formalize governance so new products are onboarded with normalized attributes from day one.
