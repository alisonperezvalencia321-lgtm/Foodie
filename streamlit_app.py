import streamlit as st

st.set_page_config(page_title="SmartBites Pro", page_icon="🥘", layout="wide")

# Estilos visuales para que se vea como una App real
st.markdown("""
    <style>
        .stApp { background-color: #f8fafc; }
        .recipe-card { background: white; padding: 25px; border-radius: 15px; border-top: 5px solid #1e40af; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); margin-bottom: 25px; }
        .macro-box { background: #f1f5f9; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #e2e8f0; }
        .category-header { color: #1e40af; font-weight: bold; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("🥘 SmartBites Pro: Menú Inteligente")

# --- BASE DE DATOS DE MACROS (Valores por 100g) ---
DB = {
    "Pollo": {"c": 165, "p": 31, "g": 3.6, "h": 0},
    "Carne de Res": {"c": 250, "p": 26, "g": 15, "h": 0},
    "Atún": {"c": 116, "p": 26, "g": 1, "h": 0},
    "Huevos": {"c": 155, "p": 13, "g": 11, "h": 1},
    "Pasta": {"c": 158, "p": 5.8, "g": 0.9, "h": 31},
    "Arroz": {"c": 130, "p": 2.7, "g": 0.3, "h": 28},
    "Pizza": {"c": 266, "p": 11, "g": 10, "h": 33},
    "Chocolate": {"c": 546, "p": 5, "g": 31, "h": 61},
    "Nutella": {"c": 539, "p": 6, "g": 31, "h": 57},
    "Pan": {"c": 265, "p": 9, "g": 3, "h": 49},
    "Aguacate": {"c": 160, "p": 2, "g": 15, "h": 9},
    "Brócoli": {"c": 34, "p": 2.8, "g": 0.4, "h": 7},
    "Patatas": {"c": 77, "p": 2, "g": 0.1, "h": 17},
    "Mayonesa": {"c": 680, "p": 1, "g": 75, "h": 1}
}

# --- SIDEBAR: CATEGORÍAS Y CONFIGURACIÓN ---
st.sidebar.header("🎯 Preferencias")
modo = st.sidebar.radio("Tipo de comida:", ["Fitness (Saludable)", "Gourmet (Equilibrado)", "Cheat Meal (Antojo)"])

st.sidebar.write("---")
st.sidebar.header("🛒 Tu Inventario")

# Secciones por categorías
seleccion = []
with st.sidebar.expander("🥩 Proteínas"):
    p = st.multiselect("Selecciona:", ["Pollo", "Carne de Res", "Atún", "Huevos"])
    seleccion.extend(p)

with st.sidebar.expander("🍞 Carbohidratos"):
    c = st.multiselect("Selecciona:", ["Arroz", "Pasta", "Pan", "Patatas", "Pizza"])
    seleccion.extend(c)

with st.sidebar.expander("🥦 Vegetales"):
    v = st.multiselect("Selecciona:", ["Brócoli", "Aguacate", "Pepino", "Tomate"])
    seleccion.extend(v)

with st.sidebar.expander("🍯 Salsas y Dulces"):
    s = st.multiselect("Selecciona:", ["Nutella", "Chocolate", "Mayonesa", "Kétchup"])
    seleccion.extend(s)

# --- GENERADOR DE RECETAS ---
if st.button("✨ GENERAR MI MENÚ PERSONALIZADO"):
    if len(seleccion) < 2:
        st.error("Selecciona al menos 2 ingredientes para cocinar.")
    else:
        st.subheader(f"📋 Recetas sugeridas ({modo})")
        
        # Generar 3 variaciones de recetas
        for i in range(1, 4):
            st.markdown(f"<div class='recipe-card'>", unsafe_allow_html=True)
            st.write(f"### 🍽️ Receta #{i}: Combinación {modo}")
            
            # Lógica de macros por ingrediente
            total_c, total_p, total_g = 0, 0, 0
            
            cols = st.columns(len(seleccion[:3]))
            for idx, ing in enumerate(seleccion[:3]):
                data = DB.get(ing, {"c": 100, "p": 10, "g": 5, "h": 10})
                total_c += data['c']; total_p += data['p']; total_g += data['g']
                with cols[idx]:
                    st.markdown(f"""
                    <div class='macro-box'>
                        <b>{ing}</b> (100g)<br>
                        🔥 {data['c']} kcal<br>
                        💪 {data['p']}g P | 🥑 {data['g']}g G
                    </div>
                    """, unsafe_allow_html=True)
            
            st.write(f"**Preparación:** Combina {seleccion[0]} con una base de {seleccion[1]}. Si usas {seleccion[-1]}, añádelo como toque final.")
            
            # Resumen Total de la receta
            st.info(f"**TOTAL RECETA:** 🔥 {total_c} kcal | 💪 {total_p}g Proteína | 🥑 {total_g}g Grasas")
            
            if st.button(f"⭐ Guardar esta receta", key=f"btn_{i}"):
                st.toast(f"Receta #{i} guardada en favoritos!")
            
            st.markdown("</div>", unsafe_allow_html=True)

# --- RECETARIO ---
st.write("---")
st.subheader("📒 Mis Recetas Guardadas")
st.caption("Aquí aparecerán las recetas que marques con la estrella.")
