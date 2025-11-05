import streamlit as st
import base64

# ==========================
# 헬 FUNCIÓN PARA BANNER SUPERIOR
# ==========================
def get_image_as_base64(file):
    with open(file, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return data

img_base64 = get_image_as_base64("img/home_bg.jpg")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #1a1a2e; /* Fondo oscuro */
    }}
    .banner {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        color: white;
        padding: 50px 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 30px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }}
    .banner h1 {{
        background: rgba(30, 58, 138, 0.85);
        padding: 10px 20px;
        border-radius: 15px;
        color: #ffffff;
        margin-bottom: 10px;
        font-size: 2.5em;
    }}
    .banner h3 {{
        background: rgba(0, 0, 0, 0.6);
        padding: 5px 15px;
        border-radius: 10px;
        color: #e0e7ff;
        font-weight: normal;
    }}
    .card-link {{
        text-decoration: none;
    }}
    .card {{
        background-color: #2a2a3e;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        transition: all 0.3s ease;
        height: 100%;
        color: #e0e7ff;
    }}
    .card:hover {{
        transform: scale(1.03);
        box-shadow: 0 6px 12px rgba(0,0,0,0.25);
        background-color: #3a3a4e;
    }}
    .card img {{
        width: 100%;
        border-radius: 10px;
        margin-bottom: 15px;
    }}
    .card h4 {{
        color: #ffffff;
        font-weight: bold;
        text-align: center;
    }}
    .card p {{
        color: #c0c5e0;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================
# 🏠 BANNER PRINCIPAL
# ==========================
st.markdown("""
<div class="banner">
    <h1>💫 Proyecto: Procesamiento de Datasets en Machine Learning</h1>
    <h3>Estudiante: Anghela Herrera 🌸</h3>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

img_titanic = get_image_as_base64("img/titanic_bg.jpg")
img_school = get_image_as_base64("img/school_bg.jpg")
img_flowers = get_image_as_base64("img/flowers_bg.jpg")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <a href="ejercicio1" class="card-link">
        <div class="card">
            <img src="data:image/png;base64,{img_titanic}">
            <h4>Ejercicio 1 – Sobrevivientes del Titanic 🚢</h4>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <a href="ejercicio2" class="card-link">
        <div class="card">
            <img src="data:image/png;base64,{img_school}">
            <h4>Ejercicio 2 – Rendimiento de estudiantes 📚</h4>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <a href="ejercicio3" class="card-link">
        <div class="card">
            <img src="data:image/png;base64,{img_flowers}">
            <h4>Ejercicio 3 – Estandarización Iris 🌸</h4>
        </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<h4 style='text-align:center; color: #e0e7ff;'>✨ Proyecto desarrollado en Streamlit ✨</h4>", unsafe_allow_html=True)
