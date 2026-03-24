import streamlit as st
import random

st.set_page_config(page_title="Chef Inteligente Ultra", page_icon="👩‍🍳", layout="wide")

# Diseño Visual Profesional
st.markdown("""
    <style>
        .stApp { background-color: #f0f4f8; }
        .recipe-card { background: white; padding: 25px; border-radius: 15px; border-top: 6px solid #1e40af; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); margin-bottom: 30px; }
        .macro-tag { background: #e2e8f0; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 0.9rem; margin-right: 5px; color: #1e293b; }
        .ingredient-box { border: 1px solid #cbd5e1; border-radius: 10px; padding: 10px; background: #f8fafc; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("👩‍🍳 SmartBites: Chef IA Definitivo")
st.write("Recetas coherentes con desglose de macros ingrediente por ingrediente.")

# --- BASE DE DATOS MASIVA DE MACROS (por 100g) ---
DB = {
    # Proteínas
    "Pollo": {"c": 165, "p": 31, "g": 3.6, "h": 0}, "Carne de Res": {"c": 250, "p": 26, "g": 15, "h": 0}, 
    "Atún": {"c": 116, "p": 26, "g": 1, "h": 0}, "Huevos": {"c": 155, "p": 13, "g": 11, "h": 1},
    "Salmón": {"c": 208, "p": 20, "g": 13, "h": 0}, "Cerdo": {"c": 242, "p": 27, "g": 14, "h": 0},
    "Gambas": {"c": 99, "p": 24, "g": 0.3, "h": 0.2}, "Tofu": {"c": 76, "p": 8, "g": 4.8, "h": 1.9},
    "Lentejas": {"c": 116, "p": 9, "g": 0.4, "h": 20}, "Garbanzos": {"c": 164, "p": 9, "g": 2.6, "h": 27},
    "Chorizo": {"c": 455, "p": 24, "g": 38, "h": 2}, "Jamón Serrano": {"c": 240, "p": 30, "g": 12, "h": 0},
    # Carbohidratos y Chatarra
    "Arroz": {"c": 130, "p": 2.7, "g": 0.3, "h": 28}, "Pasta": {"c": 158, "p": 5.8, "g": 0.9, "h": 31},
    "Patatas": {"c": 77, "p": 2, "g": 0.1, "h": 17}, "Pan": {"c": 265, "p": 9, "g": 3, "h": 49},
    "Pizza": {"c": 266, "p": 11, "g": 10, "h": 33}, "Patatas Fritas": {"c": 536, "p": 7, "g": 35, "h": 53},
    "Hamburguesa": {"c": 295, "p": 17, "g": 14, "h": 24}, "Quinoa": {"c": 120, "p": 4.4, "g": 1.9, "h": 21},
    # Vegetales y Frutas
    "Aguacate": {"c": 160, "p": 2, "g": 15, "h": 9}, "Brócoli": {"c": 34, "p": 2.8, "g": 0.4, "h": 7},
    "Tomate": {"c": 18, "p": 0.9, "g": 0.2, "h": 3.9}, "Espinacas": {"c": 23, "p": 2.9, "g": 0.4, "h": 3.6},
    "Plátano": {"c": 89, "p": 1.1, "g": 0.3, "h": 23}, "Manzana": {"c": 52, "p": 0.3, "g": 0.2, "h": 14},
    # Dulces y Salsas
    "Nutella": {"c": 539, "p": 6, "g": 31, "h": 57}, "Chocolate Negro": {"c": 546, "p": 5, "g": 31, "h": 61},
    "Mayonesa": {"c": 680, "p": 1, "g": 75, "h": 1}, "Kétchup": {"c": 112, "p": 1.3, "g": 0.1, "h": 27},
    "Mantequilla de Cacahuete": {"c": 588, "p": 25, "g": 50, "h": 20}, "Miel": {"c": 304, "p": 0.3, "g": 0, "h": 82}
}

# --- SIDEBAR: INVENTARIO TOTAL ---
st.sidebar.header("🛒 Tu Despensa Total")
tipo_menu = st.sidebar.selectbox("Tipo de Menú:", ["Equilibrado", "Bajo en Carbs", "Cheat Day", "Postres/Snacks"])

def crear_seccion(titulo, lista):
    with st.sidebar.expander(titulo):
        return st.multiselect(f"Añadir {titulo}:", lista)

p = crear_seccion("🥩 Proteínas/Carnes", ["Pollo", "Carne de Res", "Cerdo", "Atún", "Salmón", "Huevos", "Gambas", "Jamón Serrano", "Chorizo", "Tofu"])
c = crear_seccion("🍞 Carbs/Acompañantes", ["Arroz", "Pasta", "Patatas", "Pan", "Pizza", "Patatas Fritas", "Hamburguesa", "Quinoa", "Lentejas", "Garbanzos"])
v = crear_seccion("🥦 Vegetales/Frutas", ["Brócoli", "Aguacate", "Tomate", "Espinacas", "Pepino", "Zanahoria", "Manzana", "Plátano", "Cebolla", "Ajo"])
s = crear_seccion("🥫 Salsas/Dulces", ["Mayonesa", "Kétchup", "Mostaza", "Nutella", "Chocolate Negro", "Mantequilla de Cacahuete", "Miel", "Queso Crema"])

inventario = p + c + v + s

# --- LÓGICA DE GENERACIÓN ---
if st.button("✨ GENERAR MENÚ COHERENTE"):
    if len(inventario) < 2:
        st.error("Selecciona más ingredientes para crear algo real.")
    else:
        st.subheader(f"📋 Tu Menú Sugerido ({tipo_menu})")
        
        # --- RECETA 1: PLATO PRINCIPAL ---
        main_p = p[0] if p else (c[0] if c else inventario[0])
        main_v = v[0] if v else (c[0] if c else inventario[-1])
        
        with st.container():
            st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
            st.markdown(f"### 🍽️ Opción 1: Plato Fuerte")
            st.write(f"**Preparación:** Cocina {main_p} a la plancha o al horno. Acompáñalo con {main_v} y un toque de {s[0] if s else 'especias'}.")
            
            # Desglose de Macros
            cols = st.columns(3)
            tot_c, tot_p, tot_g = 0, 0, 0
            for i, ing in enumerate([main_p, main_v]):
                val = DB.get(ing, {"c":100,"p":10,"g":5,"h":10})
                tot_c += val['c']; tot_p += val['p']; tot_g += val['g']
                with cols[i]:
                    st.markdown(f"<div class='ingredient-box'><b>{ing}</b><br>🔥{val['c']} kcal | 💪{val['p']}g P</div>", unsafe_allow_html=True)
            
            st.info(f"**TOTAL ESTIMADO:** 🔥 {tot_c} kcal | 💪 {tot_p}g Proteína | 🥑 {tot_g}g Grasas")
            st.markdown("</div>", unsafe_allow_html=True)

        # --- RECETA 2: SNACK O POSTRE ---
        if s or "Pan" in c or "Aguacate" in v:
            with st.container():
                st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
                st.markdown(f"### 🍫 Opción 2: El Antojo")
                snack_base = "Pan" if "Pan" in inventario else (inventario[1] if len(inventario)>1 else inventario[0])
                snack_top = s[0] if s else "Aguacate"
                st.write(f"**Preparación:** Usa {snack_base} y úntale {snack_top}. Perfecto para matar el hambre.")
                
                # Macros snack
                v1 = DB.get(snack_base, {"c":100,"p":5,"g":2,"h":20})
                v2 = DB.get(snack_top, {"c":150,"p":2,"g":10,"h":5})
                st.markdown(f"<span class='macro-tag'>🔥 {v1['c']+v2['c']} kcal</span> <span class='macro-tag'>💪 {v1['p']+v2['p']}g P</span>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

# --- SISTEMA DE GUARDADO ---
st.write("---")
st.subheader("📒 Mis Recetas Guardadas")
if 'favs' not in st.session_state: st.session_state.favs = []
if st.button("⭐ Guardar Menú Actual"):
    st.session_state.favs.append("Menú Generado el " + str(random.randint(100,999)))
    st.toast("¡Guardado en la memoria de la sesión!")

for f in st.session_state.favs:
    st.write(f"- {f}")
