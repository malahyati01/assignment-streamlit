import streamlit as st

# 1. Title
st.title("Halo 👋")

# 2. Text input
nama = st.text_input("Masukkan nama kamu:")

# 3. Conditional rendering
if nama:
    st.write(f"Halo {nama.title()} 👋, selamat datang di aplikasi Streamlit pertamamu 🎉")

# 4. Header & text
st.header("Test")
st.write("Please play with this site.")

# 5. Markdown
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown(
    ":red[Streamlit] can :orange[write] :green[pretty] :blue[text] "
    "and :blue-background[highlight] text."
)

st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.subheader("Contoh Komponen Tambahan")

hobi = st.selectbox(
    "Pilih hobi kamu:",
    ["Membaca", "Olahraga", "Ngoding", "Traveling"]
)

if st.button("Submit"):
    st.success(f"Hobi kamu adalah {hobi} 👍")









