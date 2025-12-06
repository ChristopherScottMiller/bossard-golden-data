from golden_data.analysis.custom_field_scan import scan_custom_fields
from golden_data.markdown_utils import df_to_markdown
from golden_data.ai.ai_taxonomist import analyze_custom_fields

# 1. Scan up to 5000 product rows
cf_summary = scan_custom_fields(max_rows=5000)
print(cf_summary.head())

# 2. Convert to markdown (top 25 fields)
cf_md = df_to_markdown(cf_summary, max_rows=25)

# 3. Send to AI taxonomist
analysis_text = analyze_custom_fields(cf_md)
print(analysis_text)