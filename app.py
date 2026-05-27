import streamlit as st
import json
from compare_engine import compare_stories

# PAGE CONFIG
st.set_page_config(
    page_title="SAC Story Compare",
    layout="wide"
)

# TITLE
st.title("📊 SAC Story Measurement Compare Tool")

st.markdown("---")

# LOAD JSON
with open("data/story_a.json", "r") as f:
    story_a = json.load(f)

with open("data/story_b.json", "r") as f:
    story_b = json.load(f)

# COMPARE
df = compare_stories(
    story_a,
    story_b
)

# SHOW TABLE
st.subheader("Comparison Result")

st.dataframe(
    df,
    use_container_width=True
)

# DIFFERENCES
different_rows = df[
    df["Status"] == "Different"
]

if not different_rows.empty:

    st.warning("⚠ Differences Found")

    st.dataframe(
        different_rows,
        use_container_width=True
    )

else:

    st.success("✅ All Measurements Match")

# EXPORT EXCEL
excel_path = "reports/comparison.xlsx"

df.to_excel(
    excel_path,
    index=False
)

with open(excel_path, "rb") as file:

    st.download_button(
        label="⬇ Download Excel Report",
        data=file,
        file_name="comparison.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

st.markdown("---")

st.caption("SAC Story Comparison Tool")
