import streamlit as st
import pandas as pd
import os
import shutil
from PIL import Image

st.title("📁 VPC Backup System")

data_path = "data"
backup_path = "backup"

# ✅ Ensure folders exist
os.makedirs(data_path, exist_ok=True)
os.makedirs(backup_path, exist_ok=True)

# 📂 Show Data Folder Files
st.header("📂 Data Folder")
data_files = os.listdir(data_path)
st.write(data_files)

# 💾 Show Backup Folder Files
st.header("💾 Backup Folder")
backup_files = os.listdir(backup_path)
st.write(backup_files)

# 🚀 Backup Button
if st.button("🚀 Run Backup"):
    for file in data_files:
        src = os.path.join(data_path, file)
        dst = os.path.join(backup_path, file)

        if os.path.isfile(src):
            shutil.copy(src, dst)

    st.success("✅ Backup Completed!")

# 📄 Backup File Viewer (TEXT + CSV + IMAGE)
st.header("📄 Backup File Viewer")

for file in backup_files:
    file_path = os.path.join(backup_path, file)

    if os.path.isfile(file_path):
        st.subheader(f"File: {file}")

        try:
            # 📄 TEXT FILE
            if file.lower().endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as f:
                    st.text(f.read())

            # 📊 CSV FILE
            elif file.lower().endswith(".csv"):
                df = pd.read_csv(file_path)
                st.dataframe(df)

            # 🖼 IMAGE FILE
            elif file.lower().endswith((".png", ".jpg", ".jpeg")):
                img = Image.open(file_path)
                st.image(img, caption=file, width=300)

            # ❌ Unsupported
            else:
                st.warning("Unsupported file type")

        except Exception as e:
            st.error(f"Error opening file: {e}")