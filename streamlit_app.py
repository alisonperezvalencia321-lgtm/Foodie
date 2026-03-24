import streamlit as st
import random

# Configuración Pro
st.set_page_config(page_title="SmartBites Ultra: Modo Estricto", page_icon="⚖️", layout="wide")

# Diseño Visual de Alta Gama
st.markdown("""
    <style>
        .stApp { background-color: #f8fafc; }
        .recipe-card { background: white; padding: 25px; border-radius: 20px; border-left: 10px solid #10b981; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); margin-bottom: 30px; }
        .fitness-tag { background: #dcfce7; color: #166534; padding: 5px 15px; border-radius: 20px; font-weight: bold; border: 1px solid #bbf7d0; }
        .chatarra-tag { background: #fee2e2; color: #991b1b; padding: 5px 15px; border-radius: 20px; font-weight: bold; border: 1px solid #fecaca; }
        .macro-pill { background: #f1f5f9; color: #475569; padding: 4px 12px; border-radius: 15px; font-weight: bold; font-size: 0.8rem; }
        .ing-card { background: white; border: 1px solid #e2e8f0; padding: 12px; border-radius: 12px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("⚖️ SmartBites Pro: Inteligencia Nutricional")
st.write("Sistema con Modo Estricto y Filtrado de Categorías | Leiria 2026")

# --- BASE DE DATOS MAESTRA CLASIFICADA ---
# Tipos: 1 = Fitness, 2 = Chatarra/Snack, 3 = Salsa/Dulce
DB = {
    # FITNESS (Proteínas Magras, Carbs Complejos, Vegetales)
    "Pollo": {"c": 165, "p": 31, "g": 3, "t": 1}, "Claras de Huevo": {"c": 52, "p": 11, "g": 0.2, "t": 1},
    "Atún al Natural": {"c": 116, "p": 26, "g": 1, "t": 1}, "Pavo": {"c": 135, "p": 29, "g": 1, "t": 1},
    "Salmón": {"c": 208, "p": 20, "g": 13, "t": 1}, "Arroz Integral": {"c": 111, "p": 2.6, "g": 0.9, "t": 1},
    "Quinoa": {"c": 120, "p": 4.4, "g": 1.9, "t": 1}, "Brócoli": {"c": 34, "p": 3, "g": 0.4, "t": 1},
    "Espinacas": {"c": 23, "p": 2.9, "g": 0.4, "t": 1}, "Aguacate": {"c": 160, "p": 2, "g": 15, "t": 1},
    "Pepino": {"c": 15, "p": 0.7, "g": 0.1, "t": 1}, "Berenjena": {"c": 25, "p": 1, "g": 0.2, "t": 1},
    
    # CHATARRA / ANTOJOS
    "Pizza": {"c": 266, "p": 11, "g": 10, "t": 2}, "Hamburguesa": {"c": 295, "p": 17, "g": 14, "t": 2},
    "Nuggets": {"c": 290, "p": 15, "g": 18, "t": 2}, "Salchichas": {"c": 300, "p": 12, "g": 25, "t": 2},
    "Patatas Fritas": {"c": 536, "p": 7, "g": 35, "t": 2}, "Beicon": {"c": 541, "p": 37, "g": 42, "t": 2},
    "Nachos": {"c": 497, "p": 7, "g": 25, "t": 2}, "Donas": {"c": 452, "p": 5, "g": 25, "t": 2},
    "Galletas Oreo": {"c": 480, "p": 5, "g": 20, "t": 2}, "Croissant": {"c": 406, "p": 8, "g": 21, "t": 2},
    
    # SALSAS Y DULCES
    "Nutella": {"c": 539, "p": 6, "g": 31, "t": 3}, "Chocolate 70%": {"c": 546, "p": 5, "g": 31, "t": 3},
    "Mayonesa": {"c": 680, "p": 1, "g": 75, "t": 3}, "Kétchup": {"c": 112, "p": 1, "g": 0.1, "t": 3},
    "Miel": {"c": 304, "p": 0.3, "g": 0, "t": 3}, "Queso Crema": {"c": 342, "p": 6, "g": 34, "t": 3},
    "Mantequilla de Mani": {"c": 588, "p": 25, "g": 50, "t": 3}, "Alioli": {"c": 700, "p": 1, "g": 78, "t": 3}
}

# --- SIDEBAR: CONFIGURACIÓN Y FILTRADO ---
st.sidebar.header("🎯 Configuración de Dieta")
modo_dieta = st.sidebar.radio("Modo de Inteligencia:", ["Estricto Fitness", "Equilibrado", "Modo Antojo"])

st.sidebar.write("---")
st.sidebar.header("🛒 Tu Inventario")

def build_cat(name, items):
    with st.sidebar.expander(name):
        return st.multiselect(f"Añadir {name}:", items)

fit_sel = build_cat("🥗 Fitness / Limpio", [k for k, v in DB.items() if v['t'] == 1])
junk_sel = build_cat("🍔 Chatarra / Antojos", [k for k, v in DB.items() if v['t'] == 2])
sauce_sel = build_cat("🥫 Salsas / Dulces", [k for k, v in DB.items() if v['t'] == 3])

# --- LÓGICA DE GENERACIÓN ---
if st.button("✨ GENERAR MENÚ INTELIGENTE"):
    todos = fit_sel + junk_sel + sauce_sel
    if not todos:
        st.error("Selecciona ingredientes en el panel izquierdo.")
    else:
        st.subheader(f"👨‍🍳 Menú Sugerido: {modo_dieta}")
        
        # --- RECETA 1: PLATO PRINCIPAL ---
        st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
        if modo_dieta == "Estricto Fitness":
            st.markdown("<span class='fitness-tag'>Modo Fitness Activo</span>", unsafe_allow_html=True)
            main = fit_sel[0] if fit_sel else "Proteína Magra"
            side = fit_sel[1] if len(fit_sel) > 1 else "Vegetales al vapor"
            st.write(f"### 🍴 Opción Fitness: {main} Clean")
            st.write(f"**Instrucciones:** Cocina el/la {main} a la plancha o vapor (sin aceites añadidos). Acompaña con {side}. Esta opción ignora cualquier alimento chatarra seleccionado para mantener tus macros limpios.")
        else:
            st.markdown("<span class='chatarra-tag'>Modo Libre Activo</span>", unsafe_allow_html=True)
            main = junk_sel[0] if junk_sel else (todos[0])
            side = todos[-1] if len(todos) > 1 else "acompañamiento"
            st.write(f"### 🍽️ Opción Variada: {main} Mix")
            st.write(f"**Instrucciones:** Prepara tu {main} y combínalo con {side}. ¡Disfruta tu comida sin restricciones!")

        # Macros del plato principal
        st.write("---")
        cols = st.columns(3)
        t_c, t_p, t_g = 0, 0, 0
        for i, item in enumerate([main, side] if side != "acompañamiento" and side != "Vegetales al vapor" else [main]):
            if item in DB:
                d = DB[item]; t_c += d['c']; t_p += d['p']; t_g += d['g']
                with cols[i if i < 3 else 0]:
                    st.markdown(f"<div class='ing-card'><b>{item}</b><br>🔥{d['c']} kcal | 💪{d['p']}g P</div>", unsafe_allow_html=True)
        st.info(f"**TOTAL ESTIMADO:** 🔥 {t_c} kcal | 💪 {t_p}g Proteína | 🥑 {t_g}g Grasas")
        st.markdown("</div>", unsafe_allow_html=True)

        # --- RECETA 2: EL SNACK ---
        if sauce_sel or len(todos) > 2:
            st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
            st.write("### 🥪 Opción 2: El Snack del Chef")
            base_s = fit_sel[-1] if fit_sel else todos[0]
            top_s = sauce_sel[0] if sauce_sel else "un toque de limón"
            st.write(f"**Idea:** Usa {base_s} y añade {top_s}. Una forma rápida de saciar el hambre entre horas.")
            st.markdown("</div>", unsafe_allow_html=True)

st.write("---")
st.subheader("📒 Mis Recetas Guardadas")
st.caption("Tus planes de 650 kcal y macros de Leiria están a salvo aquí.")
