# =========================
# EXPORT EXCEL
# =========================
try:

    # STREAMLIT CLOUD SAFE PATH
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
