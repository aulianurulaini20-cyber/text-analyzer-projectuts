import re
import streamlit as st


class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        return len(self.text.split())

    def count_characters(self):
        return len(self.text)

    def count_characters_no_space(self):
        return len(self.text.replace(" ", ""))

    def estimate_reading_time(self):
        # asumsi kecepatan baca 200 kata per menit
        words = self.count_words()
        if words == 0:
            return 0
        return int(words / 200 * 60)

    def format_text(self, choice):
        if choice == "UPPERCASE":
            return self.text.upper()
        elif choice == "lowercase":
            return self.text.lower()
        return self.text.title()

    def search_word_frequency(self, keyword):
        if not keyword:
            return 0
        pattern = r"\b" + re.escape(keyword) + r"\b"
        return len(re.findall(pattern, self.text, re.IGNORECASE))


def main():
    st.set_page_config(page_title="Analisis Teks", page_icon="📝", layout="centered")

    st.title("Aplikasi Analisis Teks")
    st.write("Masukkan teks untuk melihat statistik, mengubah format huruf, dan mencari kata.")
    st.markdown("---")

    teks_input = st.text_area(
        "Masukkan teks:",
        height=150,
        placeholder="Ketik atau tempel teks di sini...",
    )

    if not teks_input:
        st.info("Masukkan teks terlebih dahulu untuk memulai.")
        return

    analyzer = TextAnalyzer(teks_input)

    # statistik
    st.subheader("Statistik Teks")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Jumlah Kata", analyzer.count_words())
    col2.metric("Karakter (+ spasi)", analyzer.count_characters())
    col3.metric("Karakter (- spasi)", analyzer.count_characters_no_space())
    col4.metric("Waktu Baca", f"{analyzer.estimate_reading_time()} dtk")

    st.markdown("---")

    # ubah format huruf
    st.subheader("Ubah Format Huruf")
    pilihan = st.selectbox("Pilih format:", ["UPPERCASE", "lowercase", "Title Case"])
    st.text_area("Hasil:", value=analyzer.format_text(pilihan), height=100)

    st.markdown("---")

    # cari kata
    st.subheader("Cari Kata")
    kata = st.text_input("Kata yang dicari:")

    if kata:
        jumlah = analyzer.search_word_frequency(kata)
        if jumlah > 0:
            st.success(f"Kata '{kata}' muncul {jumlah} kali.")
        else:
            st.warning(f"Kata '{kata}' tidak ditemukan.")


if __name__ == "__main__":
    main()