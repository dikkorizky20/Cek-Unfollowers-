# cek_unfollowers_web.py

import streamlit as st
from bs4 import BeautifulSoup

st.set_page_config(page_title="Cek Unfollowers Instagram", layout="centered")

st.title("📉 Cek Siapa yang Tidak Follow Balik")
st.markdown("Upload file `followers.html` dan `following.html` dari data Instagram.")

# Upload file followers
followers_file = st.file_uploader("📥 Upload file followers HTML", type=["html"], key="followers")
following_file = st.file_uploader("📥 Upload file following HTML", type=["html"], key="following")

def extract_usernames_from_html(html_file):
    if html_file is None:
        return set()
    soup = BeautifulSoup(html_file, 'html.parser')
    return set(a.text.strip() for a in soup.find_all('a') if a.text.strip())

# Jika kedua file diunggah
if followers_file and following_file:
    followers = extract_usernames_from_html(followers_file)
    following = extract_usernames_from_html(following_file)

    unfollowers = following - followers

    st.subheader("📋 Hasil:")
    if unfollowers:
        st.markdown("Akun berikut **tidak follow balik**:")
        for user in sorted(unfollowers):
            st.markdown(f"- {user}")
        
        # Opsi download
        result_text = "\n".join(sorted(unfollowers))
        st.download_button("⬇️ Download hasil sebagai TXT", result_text, file_name="hasil_unfollowers.txt")
    else:
        st.success("Semua following kamu juga follow kamu balik! 🎉")

elif followers_file or following_file:
    st.info("Silakan upload kedua file untuk melanjutkan.")