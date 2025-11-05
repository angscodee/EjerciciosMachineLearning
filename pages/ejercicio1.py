import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# ==========================
# ⚙️ CONFIGURACIÓN GENERAL
# ==========================
st.set_page_config(page_title="Ejercicio 1 - Titanic", layout="wide")

# ==========================
# 🎨 ESTILOS Y CABECERA
# ==========================
st.markdown("""
    <style>
    .stApp {
        background-color: #1a1a2e; /* Fondo oscuro */
    }
    .banner {
        background-color: #003049;
        color: white;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .banner h1 {
        font-size: 38px;
        margin: 0;
    }
    .banner p {
        font-size: 18px;
        margin-top: 6px;
        color: #f0f0f0;
    }
    .main {
        background-color: #2a2a3e; /* Color de contenedor oscuro */
        padding: 30px;
        border-radius: 15px;
        color: #e0e7ff; /* Color de texto claro */
    }
    h1, h2, h3, h4, h5, h6, p, strong {
        color: #e0e7ff; /* Color de texto claro */
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="banner">
    <h1>🚢 Titanic Data Processing</h1>
    <p>Preparando datos para predecir la supervivencia de los pasajeros</p>
</div>
""", unsafe_allow_html=True)

# ==========================
# 🧊 CONTENEDOR PRINCIPAL
# ==========================
st.markdown('<div class="main">', unsafe_allow_html=True)

# ==========================
# ⚙️ 1. CARGA DEL DATASET
# ==========================
st.subheader("1️⃣ Carga del Dataset")
file = st.file_uploader("Sube el archivo titanic.csv", type=["csv"])

if file:
    df = pd.read_csv(file)
else:
    st.info("No se subió ningún archivo. Se usará un dataset de ejemplo 🧩")
    data = {
        "PassengerId": [1, 2, 3, 4, 5],
        "Survived": [0, 1, 1, 1, 0],
        "Pclass": [3, 1, 3, 1, 3],
        "Name": ["Braund, Mr. Owen", "Cumings, Mrs. John", "Heikkinen, Miss. Laina", "Futrelle, Mrs. Jacques", "Allen, Mr. William"],
        "Sex": ["male", "female", "female", "female", "male"],
        "Age": [22, 38, 26, 35, 35],
        "SibSp": [1, 1, 0, 1, 0],
        "Parch": [0, 0, 0, 0, 0],
        "Ticket": ["A/5 21171", "PC 17599", "STON/O2. 3101282", "113803", "373450"],
        "Fare": [7.25, 71.2833, 7.925, 53.1, 8.05],
        "Cabin": [None, "C85", None, "C123", None],
        "Embarked": ["S", "C", "S", "S", "S"]
    }
    df = pd.DataFrame(data)

# ==========================
# 🔍 2. EXPLORACIÓN INICIAL
# ==========================
st.subheader("2️⃣ Exploración Inicial")
st.write("**Vista previa:**")
st.dataframe(df.head())

st.write("**Valores nulos por columna:**")
st.write(df.isnull().sum())

# ==========================
# 🧹 3. LIMPIEZA DE DATOS
# ==========================
st.subheader("3️⃣ Limpieza de Datos")

st.write("Eliminando columnas irrelevantes (`Name`, `Ticket`, `Cabin`)...")
df = df.drop(['Name', 'Ticket', 'Cabin'], axis=1)

st.write("Rellenando valores nulos en `Age` (media) y `Embarked` (moda)...")
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# ==========================
# 🔠 4. CODIFICACIÓN
# ==========================
st.subheader("4️⃣ Codificación de Variables Categóricas")

label_enc = LabelEncoder()
df['Sex'] = label_enc.fit_transform(df['Sex'])
df['Embarked'] = label_enc.fit_transform(df['Embarked'])

st.write("Variables categóricas codificadas con LabelEncoder ✅")

# ==========================
# 📏 5. ESTANDARIZACIÓN
# ==========================
st.subheader("5️⃣ Estandarización de Variables Numéricas")

scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
st.write("Variables `Age` y `Fare` estandarizadas correctamente ✅")

# ==========================
# 🔀 6. DIVISIÓN DE DATOS
# ==========================
st.subheader("6️⃣ División de Datos")

X = df.drop('Survived', axis=1)
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

st.write("**Tamaño del conjunto de entrenamiento:**", X_train.shape)
st.write("**Tamaño del conjunto de prueba:**", X_test.shape)

# ==========================
# 🧾 RESULTADO FINAL
# ==========================
st.subheader("✅ Datos Procesados (primeros 5 registros)")
st.dataframe(df.head())

st.markdown('</div>', unsafe_allow_html=True)
