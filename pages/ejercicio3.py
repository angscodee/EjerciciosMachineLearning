import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import base64

# ==========================
# 🌿 FUNCIÓN PARA BANNER SUPERIOR
# ==========================
def get_image_as_base64(file):
    with open(file, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return data

img_base64 = get_image_as_base64("img/flowers_bg.jpg")

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
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.25);
        margin-bottom: 20px;
    }}
    .banner h1, .banner h4 {{
        background: rgba(255, 255, 255, 0.85);
        padding: 8px 18px;
        border-radius: 15px;
        display: inline-block;
    }}
    .banner h1 {{
        color: #2E8B57; /* SeaGreen */
        font-size: 2.3em;
    }}
    .banner h4 {{
        color: #228B22; /* ForestGreen */
        font-weight: normal;
    }}
    .main {{
        background-color: #2a2a3e; /* Color de contenedor oscuro */
        padding: 25px;
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
# 🌷 ENCABEZADO SUPERIOR
# ==========================
st.markdown("""
<div class="banner">
    <h1>🌺 Iris Data Preprocessing</h1>
    <h4>Estandarización y visualización natural del dataset Iris</h4>
</div>
""", unsafe_allow_html=True)

# ==========================
# 📦 CARGA O DATASET DE RESPALDO
# ==========================
st.markdown('<div class="main">', unsafe_allow_html=True)
st.subheader("1️⃣ Carga del Dataset")

use_example = st.checkbox("Usar dataset de ejemplo (por si no carga el Iris real)", value=True)

try:
    if not use_example:
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['target'] = iris.target
        iris_loaded = True
    else:
        raise Exception("Ejemplo activado manualmente.")
except Exception:
    # Dataset de respaldo si falla o el usuario lo elige
    data = {
        'sepal length (cm)': [5.1, 4.9, 6.7, 5.9, 6.3],
        'sepal width (cm)': [3.5, 3.0, 3.1, 3.0, 2.9],
        'petal length (cm)': [1.4, 1.4, 4.4, 5.1, 5.6],
        'petal width (cm)': [0.2, 0.2, 1.4, 1.8, 2.4],
        'target': [0, 0, 1, 2, 2]
    }
    df = pd.DataFrame(data)
    iris_loaded = False

# ==========================
# 🔍 2. EXPLORACIÓN
# ==========================
st.write("**Primeros registros del dataset:**")
st.dataframe(df.head())

if iris_loaded:
    st.success("✅ Dataset original de *scikit-learn* cargado correctamente.")
else:
    st.info("📄 Mostrando dataset de ejemplo (por si el Iris real no está disponible).")

# ==========================
# 🌾 3. ESTANDARIZACIÓN
# ==========================
st.subheader("2️⃣ Estandarización con StandardScaler")

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.iloc[:, :-1])
df_scaled = pd.DataFrame(scaled_data, columns=df.columns[:-1])
df_scaled['target'] = df['target']

st.write("**Datos estandarizados (primeros 5 registros):**")
st.dataframe(df_scaled.head())

# ✂️ 4. DIVISIÓN DE DATOS
st.subheader("3️⃣ División de Datos (70% Entrenamiento / 30% Prueba)")
X = df_scaled.drop('target', axis=1)
y = df_scaled['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

st.write("**Tamaño de entrenamiento:**", X_train.shape)
st.write("**Tamaño de prueba:**", X_test.shape)

# 🌺 5. VISUALIZACIÓN
st.subheader("4️⃣ Visualización: Sepal Length vs Petal Length 🌼")

fig, ax = plt.subplots(figsize=(7, 5))
colors = ['#FF69B4', '#32CD32', '#1E90FF']  # rosa, verde, azul

for i, color in enumerate(colors):
    subset = df_scaled[df_scaled['target'] == i]
    ax.scatter(subset.iloc[:, 0], subset.iloc[:, 2],
               label=f'Clase {i}',
               color=color, alpha=0.7, edgecolor='black')

ax.set_xlabel("Sepal length (estandarizado)")
ax.set_ylabel("Petal length (estandarizado)")
ax.set_title("🌸 Distribución de Iris por especie")
ax.legend()

st.pyplot(fig)

# 📊 6. ESTADÍSTICAS
st.subheader("5️⃣ Estadísticas descriptivas del dataset estandarizado")
st.write(df_scaled.describe())

st.markdown('</div>', unsafe_allow_html=True)
