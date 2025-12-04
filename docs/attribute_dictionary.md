# Attribute Dictionary – Draft v0.1

## A. Core Identification

| Field Name         | Description                                           | Type      | Example                                   | Source                      | Notes |
|--------------------|-------------------------------------------------------|-----------|-------------------------------------------|-----------------------------|-------|
| Product_ID         | Internal unique product identifier                    | String    | `1183850`                                 | BigCommerce `ID`            | Primary key in dataset |
| SKU                | Stock keeping unit / part number                      | String    | `RAS440-9-4ZI`                            | BigCommerce `SKU`           | Unique per sellable item |
| MPN                | Manufacturer part number                              | String    | `RAS-440-9-4`                             | Parsed from `Name`/fields   | Needed for co-marketing |
| Product_Name       | Human-readable display name                           | String    | `Steel Threaded Right Angle Fastener`     | Derived from `Name`         | Clean, standardized naming |
| Product_Family     | Normalized fastener family                            | Enum      | `Self-Clinching Fastener`                 | Derived (taxonomy rules)    | Tied to taxonomy hierarchy |
| Product_Type       | More specific type within family                      | Enum      | `Right-Angle Fastener`, `Hex Head Screw`  | Derived (taxonomy rules)    | Drives filters & SEO |
| Brand              | Normalized brand/manufacturer                         | Enum      | `PennEngineering`, `Panduit`              | `Brand ID` + parsing        | Line-card alignment |
| Bossard_Program    | Strategic program/line-card grouping                  | Enum      | `PEM`, `Data Center Solutions`            | Manual / mapping table      | Optional but helpful |
| Status             | Lifecycle status                                      | Enum      | `Active`, `Obsolete`, `Phase-Out`         | Source system / future use  | Helps control catalog |

## B. Dimensional Attributes

_All numeric fields should be stored as numbers plus an explicit unit field._

| Field Name         | Description                              | Type    | Example     | Unit Field       | Notes |
|--------------------|------------------------------------------|---------|-------------|------------------|-------|
| Thread_Size        | Nominal thread designation               | String  | `M5`, `#10-32`, `1/4-20` | –        | Keep as standard string |
| Thread_Pitch       | Thread pitch (metric)                    | Float   | `0.8`       | `Thread_Pitch_Unit` | Stored in mm where applicable |
| Thread_Pitch_Unit  | Unit for thread pitch                    | Enum    | `mm`        | –                | Typically `mm` |
| Diameter_Value     | Shank or nominal diameter                | Float   | `6.0`       | `Diameter_Unit`  | Use mm internally if possible |
| Diameter_Unit      | Unit for diameter                        | Enum    | `mm`, `in`  | –                | Standardize as much as possible |
| Length_Value       | Overall fastener length                  | Float   | `20.0`      | `Length_Unit`    | Numeric-only value |
| Length_Unit        | Unit for length                          | Enum    | `mm`, `in`  | –                | Drive conversion logic |
| Grip_Range_Min     | Minimum grip range                       | Float   | `0.5`       | `Grip_Range_Unit`| For rivets/clinching fasteners |
| Grip_Range_Max     | Maximum grip range                       | Float   | `3.0`       | `Grip_Range_Unit`| – |
| Grip_Range_Unit    | Unit for grip range                      | Enum    | `mm`, `in`  | –                | – |
| Head_Diameter_Value| Head diameter                            | Float   | `10.5`      | `Head_Diameter_Unit` | – |
| Head_Diameter_Unit | Unit for head diameter                   | Enum    | `mm`, `in`  | –                | – |

## C. Material, Finish & Mechanical Properties

| Field Name           | Description                                | Type    | Example             | Allowed Values / Notes                            |
|----------------------|--------------------------------------------|---------|---------------------|--------------------------------------------------|
| Material             | Base material                              | Enum    | `Steel`, `A2 SS`, `A4 SS`, `Brass`, `Aluminum` | Normalized list; map from many text variants     |
| Material_Grade       | Material grade / alloy                     | String  | `304`, `316`, `Alloy Steel`                   | Optional but useful for spec buyers              |
| Strength_Class       | Strength class / property class            | String  | `8.8`, `10.9`, `12.9`, `A2-70`                | For metric; grade markings for inch if needed    |
| Finish               | Surface finish / coating                   | Enum    | `Zinc Plated`, `Black Oxide`, `Passivated`, `Plain` | Normalize from existing text values       |
| Finish_Notes         | Additional finish/coating details          | String  | `Trivalent Chromate`, `Zinc-Nickel`           | Free text, optional                               |
| Hardness             | Hardness rating (if available)             | String  | `HRC 32–39`                                    | From spec sheets                                 |
| Standard             | Governing standard                         | Enum    | `ISO 4762`, `DIN 933`, `ANSI B18.2.1`         | Could be multi-valued if needed                  |
| RoHS_Compliant       | Compliance flag                            | Boolean | `True` / `False`                               | From supplier data                               |
| REACH_Compliant      | Compliance flag                            | Boolean | `True` / `False`                               | –                                               |

## D. Geometry, Head & Drive

| Field Name     | Description                    | Type   | Example                          | Allowed Values / Notes |
|----------------|--------------------------------|--------|----------------------------------|------------------------|
| Head_Style     | Head geometry                  | Enum   | `Hex`, `Socket`, `Pan`, `Flat`, `Button`, `Truss`, `Countersunk` | Normalize from text |
| Drive_Style    | Drive type                     | Enum   | `Hex`, `Hex Socket`, `Phillips`, `Torx`, `Slotted`, `Combo`     | – |
| Point_Style    | Point type                     | Enum   | `Cup`, `Flat`, `Cone`, `Dog`, `Type A`, `Type 17`               | Family-dependent |
| Recess_Type    | Recess style (if distinct)     | Enum   | `Internal Hex`, `Pozidriv`       | Optional; may merge with Drive_Style |
| Self_Locking   | Thread locking feature flag    | Boolean| `True` / `False`                 | – |
| Self_Tapping   | Self-tapping / thread-forming  | Boolean| `True` / `False`                 | – |

## E. Application, Vertical & Marketing Tags

| Field Name       | Description                                    | Type   | Example                                | Notes |
|------------------|------------------------------------------------|--------|----------------------------------------|-------|
| Vertical_Tags    | High-level vertical markets where product fits | List   | `["Data Center", "EV", "Robotics"]`    | For SEO, landing pages, reporting |
| Application_Tags | Functional/application descriptors             | List   | `["Vibration-Resistant", "EMI Shielding"]` | From supplier docs/specs |
| Environment      | Typical environment                            | Enum   | `Indoor`, `Outdoor`, `Corrosive`, `High-Temp` | Optional for filters |
| Feature_Tags     | Key differentiating features                   | List   | `["Low Profile", "Tamper-Resistant"]`  | Good for filters & marketing copy |

## E. Application, Vertical & Marketing Tags

| Field Name       | Description                                    | Type   | Example                                | Notes |
|------------------|------------------------------------------------|--------|----------------------------------------|-------|
| Vertical_Tags    | High-level vertical markets where product fits | List   | `["Data Center", "EV", "Robotics"]`    | For SEO, landing pages, reporting |
| Application_Tags | Functional/application descriptors             | List   | `["Vibration-Resistant", "EMI Shielding"]` | From supplier docs/specs |
| Environment      | Typical environment                            | Enum   | `Indoor`, `Outdoor`, `Corrosive`, `High-Temp` | Optional for filters |
| Feature_Tags     | Key differentiating features                   | List   | `["Low Profile", "Tamper-Resistant"]`  | Good for filters & marketing copy |
