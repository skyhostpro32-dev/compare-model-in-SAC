import streamlit as st
import json
from compare_engine import compare_stories

# PAGE CONFIG
st.set_page_config(
    page_title="SAC Story Compare",
    layout="wide"
)

# LOAD CSS
def load_css():
    with open("styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# TITLE
st.title("📊 SAC Story Measurement Compare Tool")

st.markdown("---")

# LOAD JSON FILES
with open("data/story_a.json", "r") as f:
    story_a = json.load(f)

with open("data/story_b.json", "r") as f:
    story_b = json.load(f)

# COMPARE STORIES
df = compare_stories(
    story_a,
    story_b
)

# STATUS COLOR FUNCTION
def highlight_status(val):

    if val == "Different":
        return "background-color: #ffcccc; color: black;"

    elif val == "Same":
        return "background-color: #ccffcc; color: black;"

    return ""

# FIXED PANDAS STYLE
styled_df = df.style.map(
    highlight_status,
    subset=["Status"]
)

# DISPLAY TABLE
st.subheader("Comparison Result")

st.dataframe(
    styled_df,
    use_container_width=True
)

st.markdown("---")

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

# FOOTER
st.caption("SAC Story Comparison Tool")
