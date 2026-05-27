import streamlit as st
import json
import pandas as pd

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
# SIDEBAR
# =========================
st.sidebar.header("Upload SAC Story JSON")

story_a_file = st.sidebar.file_uploader(
    "Upload Story A JSON",
    type=["json"]
)

story_b_file = st.sidebar.file_uploader(
    "Upload Story B JSON",
    type=["json"]
)

# =========================
# MAIN LOGIC
# =========================
if story_a_file and story_b_file:

    try:

        # LOAD JSON
        story_a = json.load(story_a_file)
        story_b = json.load(story_b_file)

        # COMPARE
        df = compare_stories(
            story_a,
            story_b
        )

        # =========================
        # SHOW TABLE
        # =========================
        st.subheader("📋 Comparison Result")

        st.dataframe(
            df,
            use_container_width=True
        )

        # =========================
        # DIFFERENCE FILTER
        # =========================
        try:

            different_rows = df[
                df["Status"] == "Different"
            ]

            st.markdown("---")

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
        # EXPORT EXCEL
        # =========================
        try:

            excel_path = "/tmp/comparison.xlsx"

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

    except Exception as e:

        st.error(f"Application Error: {e}")

else:

    st.info("⬅ Upload both JSON files to start comparison")

# =========================
# FOOTER
# =========================
st.markdown("---")

st.caption("SAC Story Comparison Tool")
