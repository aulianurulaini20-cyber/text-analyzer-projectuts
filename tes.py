import re
import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Analisis Teks", page_icon="📝", layout="centered"
)

st.title("📝 Aplikasi Analisis Teks Sederhana")
st.write(
    "Masukkan teks Anda ke dalam kotak di bawah untuk melihat statistik dan melakukan manipulasi teks secara instan."
)

# Input teks dari pengguna
teks_input = st.text_area(
    "Ketik atau tempel teks Anda di sini:",
    height=150,
    placeholder="Contoh: Belajar Python dengan Streamlit sangat menyenangkan dan cepat...",
)

# Cek apakah pengguna sudah memasukkan teks
if teks_input:
    # 1. Perhitungan Statistik Dasar
    jumlah_karakter = len(teks_input)
    jumlah_karakter_tanpa_spasi = len(teks_input.replace(" ", ""))

    # Menghitung jumlah kata menggunakan split()
    kata_list = teks_input.split()
    jumlah_kata = len(kata_list)

    # Estimasi waktu baca (asumsi rata-rata orang membaca 200 kata per menit)
    waktu_baca_detik = int((jumlah_kata / 200) * 60) if jumlah_kata > 0 else 0

    st.markdown("---")
    st.subheader("📊 Statistik Teks")

    # Menampilkan metrik menggunakan 4 kolom sejajar
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Jumlah Kata", jumlah_kata)
    with col2:
        st.metric("Karakter (+ Spasi)", jumlah_karakter)
    with col3:
        st.metric("Karakter (- Spasi)", jumlah_karakter_tanpa_spasi)
    with col4:
        st.metric("Est. Waktu Baca", f"{waktu_baca_detik} dtk")

    # 2. Fitur Pengubahan Format Teks
    st.markdown("---")
    st.subheader("🛠️ Pengubahan Format Teks")

    pilihan_format = st.selectbox(
        "Pilih format huruf:",
        [
            "Huruf Kapital Semua (UPPERCASE)",
            "Huruf Kecil Semua (lowercase)",
            "Format Judul (Title Case)",
        ],
    )

    if pilihan_format == "Huruf Kapital Semua (UPPERCASE)":
        hasil_format = teks_input.upper()
    elif pilihan_format == "Huruf Kecil Semua (lowercase)":
        hasil_format = teks_input.lower()
    else:
        hasil_format = teks_input.title()

    st.text_area("Hasil Format:", value=hasil_format, height=100)

    # 3. Fitur Pencarian Kata Spesifik
    st.markdown("---")
    st.subheader("🔍 Cari Kata dalam Teks")
    kata_dicari = st.text_input("Masukkan kata yang ingin Anda cari:")

    if kata_dicari:
        # Mencari kata secara akurat (mengabaikan huruf besar/kecil)
        frekuensi = len(
            re.findall(
                r"\b" + re.escape(kata_dicari) + r"\b",
                teks_input,
                re.IGNORECASE,
            )
        )

        if frekuensi > 0:
            st.success(
                f"Kata **'{kata_dicari}'** ditemukan sebanyak **{frekuensi}** kali dalam teks."
            )
        else:
            st.warning(f"Kata **'{kata_dicari}'** tidak ditemukan.")
else:
    st.info(
        "Silakan ketik atau tempel teks di atas untuk memulai analisis. 💡"
    )
    