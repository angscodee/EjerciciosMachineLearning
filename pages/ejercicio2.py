import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import base64

# ==========================
# 🎨 FUNCIÓN PARA BANNER SUPERIOR
# ==========================
def get_image_as_base64(file):
    with open(file, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return data

img_base64 = get_image_as_base64("img/school_bg.jpg")

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
        padding: 40px 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        margin-bottom: 25px;
    }}
    .banner h1 {{
        background: rgba(0, 51, 0, 0.8);
        padding: 10px 20px;
        border-radius: 12px;
        color: #FFF5EE;
        font-size: 2.2em;
    }}
    .banner h4 {{
        background: rgba(25, 51, 25, 0.7);
        padding: 5px 15px;
        border-radius: 8px;
        color: #C1FFC1;
    }}
    .main {{
        background-color: #2a2a3e; /* Color de contenedor oscuro */
        padding: 30px;
        border-radius: 20px;
        color: #e0e7ff; /* Color de texto claro */
    }}
    h1, h2, h3, h4, h5, h6, p, strong {{
        color: #e0e7ff; /* Color de texto claro */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================
# 🏫 ENCABEZADO
# ==========================
st.markdown("""
<div class="banner">
    <h1>📚 Student Performance Data Processing</h1>
    <h4>Análisis para predecir la nota final (G3)</h4>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)

# ==========================
# ⚙️ 1. CARGA DEL DATASET
# ==========================
st.subheader("1️⃣ Carga del Dataset")
file = st.file_uploader("Sube el archivo student-mat.csv", type=["csv"])

if file:
    df = pd.read_csv(file, sep=";")  # Este dataset usa ';' como separador
else:
    st.info("⚠️ No se ha subido ningún archivo. Se cargará un dataset de ejemplo.")
    # Dataset de ejemplo (simula el de 'student-mat.csv')
    df = pd.DataFrame({
        "school": ["GP", "MS", "GP", "GP", "MS"],
        "sex": ["F", "M", "F", "F", "M"],
        "age": [17, 18, 17, 16, 19],
        "address": ["U", "R", "U", "U", "R"],
        "famsize": ["GT3", "LE3", "GT3", "GT3", "LE3"],
        "studytime": [2, 3, 2, 1, 4],
        "failures": [0, 1, 0, 2, 0],
        "absences": [4, 10, 2, 8, 6],
        "G1": [12, 10, 15, 8, 14],
        "G2": [13, 11, 14, 9, 15],
        "G3": [14, 12, 15, 10, 16]
    })

# ==========================
# 🔍 2. EXPLORACIÓN
# ==========================
st.subheader("2️⃣ Exploración Inicial")
st.write(df.head())
st.write("**Variables categóricas detectadas:**")
cat_cols = df.select_dtypes(include=['object']).columns.tolist()
st.write(cat_cols)

# ==========================
# 🧹 3. LIMPIEZA
# ==========================
st.subheader("3️⃣ Limpieza de Datos")
df.drop_duplicates(inplace=True)

# ==========================
# 🔠 4. ONE HOT ENCODING
# ==========================
st.subheader("4️⃣ Codificación One Hot")
df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)

# ==========================
# 📏 5. NORMALIZACIÓN
# ==========================
st.subheader("5️⃣ Normalización de Variables Numéricas")
scaler = StandardScaler()
cols_to_scale = ['age', 'absences', 'G1', 'G2']
df_encoded[cols_to_scale] = scaler.fit_transform(df_encoded[cols_to_scale])

# ==========================
# 🎯 6. SEPARACIÓN X / y
# ==========================
X = df_encoded.drop('G3', axis=1)
y = df_encoded['G3']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

st.write("**Tamaño entrenamiento:**", X_train.shape)
st.write("**Tamaño prueba:**", X_test.shape)

# ==========================
# 🔍 RETO ADICIONAL
# ==========================
st.subheader("📊 Correlación entre G1, G2 y G3")
st.write(df[['G1', 'G2', 'G3']].corr())

# ==========================
# ✅ RESULTADO
# ==========================
st.subheader("✅ Datos procesados (primeros 5 registros)")
st.dataframe(df_encoded.head())

st.markdown('</div>', unsafe_allow_html=True)
