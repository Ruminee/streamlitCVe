import streamlit as st

def main():
    st.title("Curriculum Vitae")

    menu = ["Foto", "Biodata", "Pendidikan", "Pengalaman Kerja", "Pengalaman Organisasi", "Pengalaman Pelatihan", "Skill"]
    choice = st.sidebar.selectbox("Pilih Halaman", menu)

    if choice == "Foto":
        st.header("Foto")
        # Tambahkan elemen untuk menampilkan foto
        st.image("https://awsimages.detik.net.id/community/media/visual/2022/12/07/ai-avatar-5.png?w=600&q=90", caption="", use_column_width=True)

    elif choice == "Biodata":
        st.header("Biodata")
        st.subheader("Nama: Iqbal Dima Naufal")
        st.write("Alamat: Tangerang, Indonesia")
        st.write("Email: Iqbal.dima@ymail.com")
        st.write("Telepon: +62 877 8917 8937")

    elif choice == "Pendidikan":
        st.header("Pendidikan")
        st.subheader("Sarjana Teknik Mesin")
        st.write("Politeknik Negeri Jakarta, Depok")
        st.write("Tahun: 2014 - 2018")

    elif choice == "Pengalaman Kerja":
        st.header("Pengalaman Kerja")
        st.subheader("Sr. Business Excecutive")
        st.write("Perusahaan ABC, Jakarta")
        st.write("Tahun: 2019 - Sekarang")
        st.write("Deskripsi: Bertanggung jawab untuk pengembangan Bisnis Service After Sales suatu brand.")

    elif choice == "Pengalaman Organisasi":
        st.header("Pengalaman Organisasi")
        st.subheader("MAPALA")
        st.write("Politeknik Negeri Jakarta")
        st.write("Tahun: 2016 - 2018")
        st.write("Deskripsi: Memimpin kegiatan-kegiatan MAPALA dan kegiatan sosial.")

    elif choice == "Pengalaman Pelatihan":
        st.header("Pengalaman Pelatihan")
        st.subheader("Pelatihan Data Science")
        st.write("Tahun: 2024")
        st.write("Deskripsi: Pelatihan intensif dalam Data Science.")

    elif choice == "Skill":
        st.header("Skill")
        st.subheader("Bahasa Pemrograman")
        st.write("- Python")
        st.write("- Java")
        st.subheader("Framework")
        st.write("- Django")
        st.write("- Flask")
        st.subheader("Keterampilan Lainnya")
        st.write("- Manajemen Proyek")
        st.write("- Komunikasi Tim")
        st.write("- Analisis Kebutuhan Pengguna")

if __name__ == "__main__":
    main()
