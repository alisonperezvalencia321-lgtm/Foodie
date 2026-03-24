import streamlit as st

st.set_page_config(page_title="SmartBites Ultra Pro", page_icon="👨‍🍳", layout="wide")

# Diseño Visual de Alta Calidad
st.markdown("""
    <style>
        .stApp { background: #f0f2f6; }
        .main-title { color: #1e3a8a; text-align: center; font-size: 3rem; font-weight: 800; margin-bottom: 0; }
        .macro-card { background: white; padding: 15px; border-radius: 10px; border-top: 4px solid #3b82f6; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        .recipe-box { background: #ffffff; padding: 25px; border-radius: 20px; border: 1px solid #e2e8f0; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>👨‍🍳 SmartBites Ultra Pro</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Tu Chef Personal con Macros Detallados</p>", unsafe_allow_html=True)

# --- BASE DE DATOS DE MACROS (Valores aprox por 100g) ---
db_macros = {
    "Pollo": {"cal": 165, "prot": 31, "grasas": 3.6, "carbs": 0},
    "Carne de Res": {"cal": 250, "prot": 26, "grasas": 15, "carbs": 0},
    "Atún": {"cal": 116, "prot": 26, "grasas": 1, "carbs": 0},
    "Huevos": {"cal": 155, "prot": 13, "grasas": 11, "carbs": 1.1},
    "Arroz": {"cal": 130, "prot": 2.7, "grasas": 0.3, "carbs": 28},
    "Pasta": {"cal": 158, "prot": 5.8, "grasas": 0.9, "carbs": 31},
    "Aguacate": {"cal": 160, "prot": 2, "grasas": 15, "carbs": 9},
    "Chocolate Negro": {"cal": 546, "prot": 5, "grasas": 31, "carbs": 61},
    "Pizza Congelada": {"cal": 266, "prot": 11, "grasas": 10, "carbs": 33},
    "Pan de Molde": {"cal": 265, "prot": 9, "grasas": 3, "carbs": 49},
    "Pepino": {"cal": 15, "prot": 0.7, "grasas": 0.1, "carbs": 3.6},
    "Brócoli": {"cal": 34, "prot": 2.8, "grasas": 0.4, "carbs": 7}
}

# --- SIDEBAR: CONFIGURACIÓN ---
st.sidebar.header("⚙️ Configuración")
tipo_cocina = st.sidebar.radio("¿Qué te apetece hoy?", ["🥗 Saludable / Fitness", "🍔 Cheat Meal / Antojo", "⚡ Rápido / Snack"])

st.sidebar.write("---")
st.sidebar.header("🛒 Tu Despensa")
categorias = {
    "Proteínas": ["Pollo", "Carne de Res", "Atún", "Huevos", "Jamón Serrano", "Nuggets", "Salchichas"],
    "Carbs/Base": ["Arroz", "Pasta", "Pan de Molde", "Rice Cakes", "Pizza Congelada", "Patatas Fritas"],
    "Vegetales": ["Brócoli", "Pepino", "Tomate", "Zanahoria", "Aguacate", "Espinacas"],
    "Extras/Dulces": ["Chocolate Negro", "Queso Crema", "Mayonesa", "Kétchup", "Salsa César", "Nutella"]
}

seleccionados = []
for cat, items in categorias.items():
    sel = st.sidebar.multiselect(cat, items)
    seleccionados.extend(sel)

# --- MOTOR DE RECETAS ---
if st.button("✨ ¡GENERAR MIS RECETAS!"):
    if len(seleccionados) < 2:
        st.error("Por favor, selecciona al menos una proteína y un acompañamiento.")
    else:
        st.subheader(f"📋 Opciones {tipo_cocina}")
        
        # Generamos 2 opciones
        for i in range(2):
            with st.container():
                st.markdown(f"<div class='recipe-box'>", unsafe_allow_html=True)
                nombre_receta = f"Opción {i+1}: Mix de {seleccionados[0]} y {seleccionados[-1]}"
                st.markdown(f"### 🍴 {nombre_receta}")
                
                total_cal, total_prot, total_grasas, total_carbs = 0, 0, 0, 0
                
                st.write("**Desglose de Ingredientes (por 100g aprox):**")
                cols = st.columns(len(seleccionados[:3])) # Mostramos macros de los primeros 3
                
                for idx, ing in enumerate(seleccionados[:3]):
                    data = db_macros.get(ing, {"cal": 100, "prot": 10, "grasas": 5, "carbs": 10})
                    total_cal += data['cal']; total_prot += data['prot']
                    total_grasas += data['grasas']; total_carbs += data['carbs']
                    
                    with cols[idx]:
                        st.markdown(f"""
                        <div class='macro-card'>
                            <b>{ing}</b><br>
                            🔥 {data['cal']} kcal<br>
                            💪 {data['prot']}g P | 🥑 {data['grasas']}g G
                        </div>
                        """, unsafe_allow_html=True)
                
                st.write(f"**Pasos:** Cocina el/la {seleccionados[0]} a la plancha. Usa el/la {seleccionados[-1]} como base fresca o salteada. Aliña al gusto.")
                
                # Resumen Total
                st.info(f"**TOTAL ESTIMADO:** 🔥 {total_cal} kcal | 💪 {total_prot}g Proteína | 🥑 {total_grasas}g Grasas | 🍞 {total_carbs}g Carbs")
                
                if st.button(f"⭐ Guardar {nombre_receta}", key=f"save_{i}"):
                    st.toast("¡Receta guardada en tu perfil!", icon="✅")
                st.markdown("</div>", unsafe_allow_html=True)

# --- SECCIÓN DE GUARDADOS ---
st.write("---")
st.subheader("📒 Mi Recetario Guardado")
st.write("Aquí aparecerán las recetas que vayas guardando durante tu sesión.")
