import streamlit as st
import json
import os

from compare_engine import compare_stories

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="SAC Story Compare",
    layout="wide"
)

# =========================
# LOAD CSS
# =========================
def load_css():

    try:
        with open("styles.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except:
        pass

load_css()

# =========================
# TITLE
# =========================
st.title("📊 SAC Story Measurement Compare Tool")

st.markdown("---")

# =========================
# LOAD JSON FILES
# =========================
try:

    with open("data/story_a.json", "r") as f:
        story_a = json.load(f)

    with open("data/story_b.json", "r") as f:
        story_b = json.load(f)

except Exception as e:

    st.error(f"Error loading JSON files: {e}")
    st.stop()

# =========================
# COMPARE STORIES
# =========================
try:

    df = compare_stories(
        story_a,
        story_b
    )

except Exception as e:

    st.error(f"Comparison Error: {e}")
    st.stop()

# =========================
# SHOW RESULT
# =========================
st.subheader("Comparison Result")

st.dataframe(
    df,
    use_container_width=True
)

# =========================
# SHOW DIFFERENCES
# =========================
try:

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

except:
    pass

# =========================
# CREATE REPORTS FOLDER
# =========================
# SAFE TEMP FOLDER
report_folder = "/tmp"

excel_path = f"{report_folder}/comparison.xlsx"

# =========================
# EXPORT EXCEL
# =========================
try:

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

except Exception as e:

    st.error(f"Excel Export Error: {e}")

# =========================
# FOOTER
# =========================
st.markdown("---")

st.caption("SAC Story Comparison Tool")
