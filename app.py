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

# LOAD JSON FILES
with open("data/story_a.json") as f:
    story_a = json.load(f)

with open("data/story_b.json") as f:
    story_b = json.load(f)

# COMPARE
df = compare_stories(
    story_a,
    story_b
)

# COLOR STATUS
def highlight_status(val):

    if val == "Different":
        return "background-color: #ffcccc"

    elif val == "Same":
        return "background-color: #ccffcc"

    return ""

styled_df = df.style.applymap(
    highlight_status,
    subset=["Status"]
)

# SHOW TABLE
st.dataframe(
    styled_df,
    use_container_width=True
)

# EXPORT
excel_path = "reports/comparison.xlsx"

df.to_excel(
    excel_path,
    index=False
)

with open(excel_path, "rb") as file:

    st.download_button(
        label="⬇ Download Excel Report",
        data=file,
        file_name="comparison.xlsx"
    )
