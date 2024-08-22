import streamlit as st
from recom import vaksin_predict, obat_predict

st.write("""
# DSS for Diphtheria Treatments
Aplikasi pendukung keputusan untuk penanganan gejala difteri
""")

col1, col2 = st.columns(2)
with col1:
    sex = st.radio("Jenis kelamin : ", horizontal=True, options=["Perempuan", "Laki-laki"])
    f0 = 0 if sex=="Perempuan" else 1

with col2:
    age = st.number_input("Usia : ", min_value=1, max_value=84, step=1)
    f1 = (age-1)/83

col3, col4, col5 = st.columns(3)
with col3:
    st.write("""##### Gejala : """)
    fever = st.checkbox('Demam')
    f2 = 1 if fever else 0
    sorethroat = st.checkbox('Nyeri telan')
    f3 = 1 if sorethroat else 0
    cough = st.checkbox('Batuk')
    f4 = 1 if cough else 0
    flu = st.checkbox('Pilek')
    f5 = 1 if flu else 0
    headache = st.checkbox('Pusing')
    f6 = 1 if headache else 0
    hardbreathe = st.checkbox('Sesak')
    f7 = 1 if hardbreathe else 0
    nausea = st.checkbox('Mual')
    f8 = 1 if nausea else 0

with col4:
    st.write("""##### Status Vaksinasi : """)
    dpt1 = st.checkbox('DPT 1')
    f9 = 1 if dpt1 else 0
    dpt2 = st.checkbox('DPT 2')
    f10 = 1 if dpt2 else 0
    dpt3 = st.checkbox('DPT 3')
    f11 = 1 if dpt3 else 0
    boost = st.checkbox('Booster')
    f12 = 1 if boost else 0
    dt = st.checkbox('Diphteria Tetanus')
    f13 = 1 if dt else 0
    td = st.checkbox('Tetanus Diphteria')
    f14 = 1 if td else 0

with col5:
    st.write("""##### Hasil Pemeriksaan : """)
    diagnosis = st.selectbox('Diagnosis :', ('D. Tonsil', 'D. Pharynx', 'D. Lharynx', 'D. Bibir', 'D. Lidah', 'D. Oropharyn', 'Unknown'))
    if diagnosis=="D. Tonsil": f15 = 0
    elif diagnosis=="D. Pharynx": f15 = 1
    elif diagnosis=="D. Lharynx": f15 = 2
    elif diagnosis=="Unknown": f15 = 3
    elif diagnosis=="D. Bibir": f15 = 4
    elif diagnosis=="D. Lidah": f15 = 5
    else: f15 = 5
    
    ku = st.selectbox('Kulit :', ("Baik", "Lemah", "Cyanosis", "Shock"))
    f16 = 0
    epis = st.checkbox('Epis')
    f17 = 1 if epis else 0
    bullneck = st.checkbox('Bullneck')
    f18 = 1 if bullneck else 0
    stridor = st.checkbox('Stridor')
    f19 = 1 if stridor else 0

feature = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19]
dosis = f9 + f10 + f11 + f12 + f13 + f14

button = st.button("Berikan Rekomendasi", type="primary", use_container_width=True)

if button:
    vaksin = vaksin_predict(feature)
    pengobatan = obat_predict(feature)

    if vaksin != 'Tidak perlu':
        if dosis < 3:
            if age < 6:
                st.warning("Segera lengkapi imunisasi dasar (3 dosis) dan imunisasi lanjutan.")
            if age > 6:
                st.warning("Berikan 3 dosis dengan interval waktu 1 bulan antara dosis pertama, kedua, dan ketiga.")
        elif dosis == 3:
            st.warning("Berikan 1 dosis imunisasi ulangan difteri.")
        st.write(f"#### Rekomendasi Vaksin : {vaksin}")

    if len(pengobatan) > 0:
        st.write(f"#### Rekomendasi Pengobatan : {pengobatan}")