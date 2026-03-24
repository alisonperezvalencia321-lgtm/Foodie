import streamlit as st

# 🎨 Configuración de la App y Diseño Visual (Fresco y Moderno)
st.set_page_config(
    page_title="SmartBites IA",
    page_icon="🥑",
    layout="centered", # Centrado para móviles
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para "embellecer" la App
st.markdown("""
    <style>
        /* Fondo degradado suave */
        .stApp {
            background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        }
        /* Títulos principales */
        h1 {
            color: #2e7d32;
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            text-align: center;
        }
        /* Subtítulos */
        .stMarkdown p {
            font-size: 1.1rem;
            color: #555;
            text-align: center;
        }
        /* Botones personalizados */
        div.stButton > button:first-child {
            background-color: #43a047;
            color: white;
            border-radius: 20px;
            border: none;
            padding: 10px 30px;
            font-size: 1.1rem;
            font-weight: 600;
            transition: all 0.3s ease;
            display: block;
            margin: 0 auto;
        }
        div.stButton > button:first-child:hover {
            background-color: #2e7d32;
            transform: scale(1.05);
        }
        /* Tarjetas de macros */
        div[data-testid="stMetricValue"] {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 15px;
            border: 1px solid #ddd;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
        div[data-testid="stMetricLabel"] {
            color: #666;
            font-weight: 500;
        }
        /* Sidebar personalizado */
        .css-1d391kg {
            background-color: #f1f8e9;
        }
    </style>
""", unsafe_allow_html=True)

# 🥑 Cabecera de la App
st.write("") # Espaciado
st.markdown("<h1>🥑 SmartBites: Tu IA de Nutrición</h1>", unsafe_allow_html=True)
st.write("Día Completo: **650 kcal | 60g Proteína**")
st.write("---")

# 🛒 INVENTARIO INTELIGENTE (En el Sidebar con Iconos)
st.sidebar.markdown("### 🛒 Mi Nevera Hoy")
st.sidebar.write("Selecciona qué ingredientes tienes:")

ingredientes = {
    "🍗 Pollo": "Pechuga magra",
    "🥚 Huevo": "Entero y Claras",
    "🐟 Atún": "Lata al natural",
    "🥓 Jamón": "Lonchas extra finas",
    "🥛 Queso Crema/Yogur Light": "Base cremosa",
    "🥦 Brócoli": "Fibra y volumen",
    "🫑 Pimiento": "Crujiente y Vitamina C",
    "🥒 Pepino": "Fresco y bajo en kcal",
    "🥕 Zanahoria": "Fibra y dulzor",
    "🥑 Aguacate": "Grasas saludables",
    "🍫 Chocolate 70% sin azúcar": "El toque dulce",
    "🍘 Rice Cakes": "Carbs crujientes"
}

# Crear multiselect usando solo los nombres con iconos
seleccionados_iconos = st.sidebar.multiselect(
    label="", # Sin label encima para diseño limpio
    options=list(ingredientes.keys())
)

st.sidebar.write("---")
st.sidebar.caption("App optimizada para el plan de 650 kcal de Leiria.")

# 👨‍🍳 GENERADOR DE RECETAS CREATIVAS (Con más Diseño)
st.subheader("👨‍🍳 ¿Qué cocinamos hoy?")
if st.button("✨ ¡Crear Receta Mágica!"):
    if not seleccionados_iconos:
        st.warning("⚠️ ¡Dime qué tienes en la nevera primero!")
    else:
        # Lógica inteligente basada en tus ingredientes (más estética)
        if "🐟 Atún" in seleccionados_iconos and "🥒 Pepino" in seleccionados_iconos:
            st.markdown("### 🌟 Sushi-Fit de Pepino y Atún")
            st.info("Usa láminas de pepino para envolver la mezcla de atún con un toque de limón. ¡Es fresco y saciante!")
            
            # Mostrar Macros en tarjetas bonitas
            col1, col2, col3 = st.columns(3)
            col1.metric("🔥 Calorías", "133 kcal")
            col2.metric("💪 Proteína", "24.5g")
            col3.metric("🥑 Grasas", "2g")

        elif "🍗 Pollo" in seleccionados_iconos and "🫑 Pimiento" in seleccionados_iconos:
            st.markdown("### 🌟 Salteado Cremoso Leiria")
            st.info("Saltea el pollo y pimiento con agua y limón. Apaga el fuego y liga con la yema y queso crema para la salsa.")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("🔥 Calorías", "303 kcal")
            col2.metric("💪 Proteína", "31.5g")
            col3.metric("🥑 Grasas", "14.5g")
        
        else:
            st.markdown("### 🌟 Bowl Volumen Proteico")
            st.info(f"Combina tu {seleccionados_iconos[0]} con los vegetales verdes para llenar el plato. ¡Máxima proteína y fibra!")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("🔥 Calorías", "<200 kcal")
            col2.metric("💪 Proteína", ">15g")
            col3.metric("🥑 Grasas", "Bajas")

# ⭐ TUS RECETAS GUARDADAS (El plan de 650 kcal)
st.write("")
st.write("---")
st.subheader("📒 Mis Recetas Guardadas (650 kcal Totales)")

# Usar expanders bonitos para organizar tus platos
with st.expander("🌅 Desayuno: Revuelto de Brócoli Pro (180 kcal)"):
    st.write("150g Brócoli + 1 Huevo + 1 Clara + Jamón + 1 cda Queso Crema Light.")
    st.caption("20g Proteína | Prepara sin mantequilla, usa agua para el vapor.")

with st.expander("☀️ Almuerzo: Pollo Cremoso Leiria (303 kcal)"):
    st.write("120g Pechuga + 1 Pimiento + 1 Yema (salsa) + 1 cda Queso Crema + 1/4 Aguacate.")
    st.caption("31.5g Proteína | Saciante y cremoso para aguantar sin cena.")

with st.expander("🍓 Merienda: Dúo Saciedad (167 kcal)"):
    st.write("2 Rice Cakes + 1 Jamón + 2 cdas Yogur Light + Zanahoria + **7.5g Chocolate 70%**.")
    st.caption("9g Proteína | Divide en dos: uno salado y uno dulce con chocolate picado.")

st.write("")
st.write("---")
st.markdown("Made with ❤️ for Leiria | SmartBites IA v1.1", unsafe_allow_html=True)
