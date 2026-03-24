import streamlit as st

st.set_page_config(page_title="SmartBites: Chef IA", page_icon="👨‍🍳", layout="centered")

# --- ESTILO VISUAL ---
st.markdown("""
    <style>
        .stApp { background: #fdfdfd; }
        .recipe-card { background: white; padding: 20px; border-radius: 15px; border-left: 5px solid #ff4b4b; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 20px; }
        .macro-tag { background: #f1f5f9; padding: 5px 10px; border-radius: 8px; font-weight: bold; color: #475569; }
    </style>
""", unsafe_allow_html=True)

st.title("👨‍🍳 SmartBites: Chef IA Real")
st.write("Ahora con lógica culinaria y macros precisos.")

# --- BASE DE DATOS DE MACROS REALES ---
# (Valores por 100g)
MACROS = {
    "Pollo": {"c": 165, "p": 31, "g": 3.6, "h": 0},
    "Atún": {"c": 116, "p": 26, "g": 1, "h": 0},
    "Huevos": {"c": 155, "p": 13, "g": 11, "h": 1},
    "Carne de Res": {"c": 250, "p": 26, "g": 15, "h": 0},
    "Arroz": {"c": 130, "p": 2.7, "g": 0.3, "h": 28},
    "Pasta": {"c": 158, "p": 5.8, "g": 0.9, "h": 31},
    "Pan": {"c": 265, "p": 9, "g": 3, "h": 49},
    "Chocolate": {"c": 546, "p": 5, "g": 31, "h": 61},
    "Nutella": {"c": 539, "p": 6, "g": 31, "h": 57},
    "Aguacate": {"c": 160, "p": 2, "g": 15, "h": 9},
    "Pizza": {"c": 266, "p": 11, "g": 10, "h": 33},
    "Brócoli": {"c": 34, "p": 2.8, "g": 0.4, "h": 7},
    "Pepino": {"c": 15, "p": 0.7, "g": 0.1, "h": 3.6}
}

# --- SIDEBAR ---
st.sidebar.header("🛒 Mi Nevera")
tipo_plato = st.sidebar.selectbox("¿Qué quieres comer?", ["Comida Principal (Salada)", "Postre o Snack Dulce"])

proteinas = st.sidebar.multiselect("Proteínas/Bases:", ["Pollo", "Carne de Res", "Atún", "Huevos", "Pizza", "Pasta", "Arroz"])
extras = st.sidebar.multiselect("Complementos/Salsas:", ["Aguacate", "Brócoli", "Pepino", "Nutella", "Chocolate", "Pan"])

# --- LÓGICA DE COCINA INTELIGENTE ---
if st.button("✨ Generar Recetas Coherentes"):
    todos = proteinas + extras
    if not todos:
        st.error("Dime qué tienes para poder cocinar.")
    else:
        st.subheader(f"🍴 Sugerencias para {tipo_plato}")
        
        # Filtro de sentido común
        if tipo_plato == "Comida Principal (Salada)":
            # Quitamos lo dulce de la comida salada
            ing = [x for x in todos if x not in ["Nutella", "Chocolate"]]
            if not ing:
                st.warning("No tienes ingredientes salados seleccionados.")
            else:
                # RECETA 1
                st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
                st.markdown(f"### 🥗 {ing[0]} con toque de {ing[-1] if len(ing)>1 else 'especias'}")
                st.write(f"**Preparación:** Cocina el {ing[0]} a la plancha con sal y pimienta. Acompáñalo con una base de {ing[-1] if len(ing)>1 else 'vegetales'}.")
                
                # Cálculo de Macros
                m = MACROS.get(ing[0], {"c":0,"p":0,"g":0,"h":0})
                st.markdown(f"<span class='macro-tag'>🔥 {m['c']} kcal</span> <span class='macro-tag'>💪 {m['p']}g P</span> <span class='macro-tag'>🥑 {m['g']}g G</span>", unsafe_allow_html=True)
                st.button("⭐ Guardar Receta Salada", key="save1")
                st.markdown("</div>", unsafe_allow_html=True)

        else: # POSTRES
            ing = [x for x in todos if x in ["Nutella", "Chocolate", "Pan", "Huevos", "Aguacate"]]
            if not ing:
                st.warning("Selecciona algo dulce (Nutella, Chocolate) para el postre.")
            else:
                st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
                st.markdown(f"### 🍫 Delicia de {ing[0]}")
                st.write(f"**Preparación:** Usa el {ing[0]} como topping o relleno. Si tienes pan, tuesta una rebanada y úntalo.")
                m = MACROS.get(ing[0], {"c":0,"p":0,"g":0,"h":0})
                st.markdown(f"<span class='macro-tag'>🔥 {m['c']} kcal</span> <span class='macro-tag'>💪 {m['p']}g P</span> <span class='macro-tag'>🥑 {m['g']}g G</span>", unsafe_allow_html=True)
                st.button("⭐ Guardar Postre", key="save2")
                st.markdown("</div>", unsafe_allow_html=True)

# --- RECETARIO GUARDADO ---
st.write("---")
st.subheader("📒 Mis Recetas Guardadas")
st.caption("Las recetas que guardes aparecerán aquí abajo (Simulación de base de datos).")
