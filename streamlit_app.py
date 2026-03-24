import streamlit as st
import random

# Configuración Pro
st.set_page_config(page_title="SmartBites Ultra Pro", page_icon="🍔", layout="wide")

# Diseño Visual
st.markdown("""
    <style>
        .stApp { background-color: #f8fafc; }
        .recipe-card { background: white; padding: 25px; border-radius: 20px; border-left: 10px solid #2563eb; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); margin-bottom: 30px; }
        .macro-pill { background: #e0f2fe; color: #0369a1; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 0.85rem; border: 1px solid #bae6fd; }
        .ing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(110px, 1fr)); gap: 12px; margin: 15px 0; }
        .ing-card { background: #ffffff; border: 1px solid #e2e8f0; padding: 10px; border-radius: 12px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

st.title("🍔 SmartBites: Variedad Ilimitada")
st.write("Selecciona tus ingredientes por categorías en el menú de la izquierda.")

# --- BASE DE DATOS GIGANTE (Macros por 100g aprox) ---
DB = {
    # PROTEÍNAS (MAGRAS Y CHATARRA)
    "Pollo": {"c": 165, "p": 31, "g": 3}, "Carne de Res": {"c": 250, "p": 26, "g": 15}, "Atún": {"c": 116, "p": 26, "g": 1},
    "Huevos": {"c": 155, "p": 13, "g": 11}, "Salmón": {"c": 208, "p": 20, "g": 13}, "Gambas/Camarones": {"c": 99, "p": 24, "g": 0.3},
    "Beicon/Tocino": {"c": 541, "p": 37, "g": 42}, "Salchichas": {"c": 300, "p": 12, "g": 25}, "Nuggets": {"c": 290, "p": 15, "g": 18},
    "Jamón Serrano": {"c": 240, "p": 30, "g": 12}, "Carne de Kebab": {"c": 230, "p": 15, "g": 18}, "Lomo de Cerdo": {"c": 242, "p": 27, "g": 14},
    "Pavo": {"c": 135, "p": 29, "g": 1}, "Chorizo": {"c": 450, "p": 24, "g": 38}, "Salami": {"c": 330, "p": 13, "g": 28},
    "Pescado Blanco": {"c": 90, "p": 20, "g": 1}, "Carne Molida": {"c": 240, "p": 24, "g": 15}, "Pulpo": {"c": 82, "p": 15, "g": 1},
    "Costillas": {"c": 290, "p": 20, "g": 22}, "Pato": {"c": 337, "p": 19, "g": 28}, "Mortadela": {"c": 311, "p": 12, "g": 28},

    # CARBOHIDRATOS (LIMPIOS Y CHATARRA)
    "Arroz": {"c": 130, "p": 3, "g": 0}, "Pasta": {"c": 158, "p": 6, "g": 1}, "Patatas/Papas": {"c": 77, "p": 2, "g": 0},
    "Pan de Molde": {"c": 265, "p": 9, "g": 3}, "Pizza": {"c": 266, "p": 11, "g": 10}, "Hamburguesa": {"c": 295, "p": 17, "g": 14},
    "Patatas Fritas (Bolsa)": {"c": 536, "p": 7, "g": 35}, "Nachos": {"c": 497, "p": 7, "g": 25}, "Rice Cakes": {"c": 387, "p": 8, "g": 3},
    "Cereal": {"c": 370, "p": 7, "g": 2}, "Croissant": {"c": 406, "p": 8, "g": 21}, "Yuca": {"c": 160, "p": 1.4, "g": 0.3},
    "Tortillas de Maíz": {"c": 218, "p": 6, "g": 3}, "Donas": {"c": 452, "p": 5, "g": 25}, "Avena": {"c": 389, "p": 17, "g": 7},
    "Quinoa": {"c": 120, "p": 4, "g": 2}, "Pan Artesanal": {"c": 250, "p": 8, "g": 1}, "Galletas Saladas": {"c": 421, "p": 9, "g": 11},

    # VEGETALES Y FRUTAS
    "Aguacate": {"c": 160, "p": 2, "g": 15}, "Brócoli": {"c": 34, "p": 3, "g": 0}, "Tomate": {"c": 18, "p": 1, "g": 0},
    "Pepino": {"c": 15, "p": 1, "g": 0}, "Cebolla": {"c": 40, "p": 1, "g": 0}, "Plátano": {"c": 89, "p": 1, "g": 0},
    "Zanahoria": {"c": 41, "p": 1, "g": 0}, "Espinacas": {"c": 23, "p": 3, "g": 0}, "Lechuga": {"c": 15, "p": 1, "g": 0},
    "Pimiento": {"c": 20, "p": 1, "g": 0}, "Champiñones": {"c": 22, "p": 3, "g": 0}, "Manzana": {"c": 52, "p": 0.3, "g": 0.2},
    "Fresas": {"c": 32, "p": 0.7, "g": 0.3}, "Mango": {"c": 60, "p": 0.8, "g": 0.4}, "Piña": {"c": 50, "p": 0.5, "g": 0.1},

    # SALSAS, DULCES Y SNACKS
    "Mayonesa": {"c": 680, "p": 1, "g": 75}, "Kétchup": {"c": 112, "p": 1, "g": 0}, "Nutella": {"c": 539, "p": 6, "g": 31},
    "Chocolate 70%": {"c": 546, "p": 5, "g": 31}, "Queso Crema": {"c": 342, "p": 6, "g": 34}, "Miel": {"c": 304, "p": 0, "g": 0},
    "Mantequilla de Mani": {"c": 588, "p": 25, "g": 50}, "Salsa BBQ": {"c": 172, "p": 1, "g": 1}, "Alioli": {"c": 700, "p": 1, "g": 78},
    "Mostaza": {"c": 66, "p": 4, "g": 4}, "Mermelada": {"c": 250, "p": 0.4, "g": 0.1}, "Yogur Griego": {"c": 59, "p": 10, "g": 0.4},
    "Galletas Oreo": {"c": 480, "p": 5, "g": 20}, "Papas Lay's": {"c": 536, "p": 7, "g": 35}, "Doritos": {"c": 510, "p": 7, "g": 26}
}

# --- SIDEBAR: CATEGORÍAS (TU ESTRUCTURA) ---
st.sidebar.header("🛒 Mi Despensa Total")

# Función para no repetir código
def crear_cat(nombre, lista):
    with st.sidebar.expander(nombre):
        return st.multiselect(f"Añadir {nombre}:", sorted(lista))

p_sel = crear_cat("🥩 Proteínas", [k for k in DB if k in ["Pollo", "Carne de Res", "Atún", "Huevos", "Salmón", "Gambas/Camarones", "Beicon/Tocino", "Salchichas", "Nuggets", "Jamón Serrano", "Carne de Kebab", "Lomo de Cerdo", "Pavo", "Chorizo", "Salami", "Pescado Blanco", "Carne Molida", "Pulpo", "Costillas", "Pato", "Mortadela"]])
c_sel = crear_cat("🍞 Carbohidratos", [k for k in DB if k in ["Arroz", "Pasta", "Patatas/Papas", "Pan de Molde", "Pizza", "Hamburguesa", "Patatas Fritas (Bolsa)", "Nachos", "Rice Cakes", "Cereal", "Croissant", "Yuca", "Tortillas de Maíz", "Donas", "Avena", "Quinoa", "Pan Artesanal", "Galletas Saladas"]])
v_sel = crear_cat("🥦 Vegetales y Frutas", [k for k in DB if k in ["Aguacate", "Brócoli", "Tomate", "Pepino", "Cebolla", "Plátano", "Zanahoria", "Espinacas", "Lechuga", "Pimiento", "Champiñones", "Manzana", "Fresas", "Mango", "Piña"]])
s_sel = crear_cat("🥫 Salsas y Dulces", [k for k in DB if k in ["Mayonesa", "Kétchup", "Nutella", "Chocolate 70%", "Queso Crema", "Miel", "Mantequilla de Mani", "Salsa BBQ", "Alioli", "Mostaza", "Mermelada", "Yogur Griego", "Galletas Oreo", "Papas Lay's", "Doritos"]])

seleccionados = p_sel + c_sel + v_sel + s_sel

# --- GENERADOR DE RECETAS ---
if st.button("✨ GENERAR MIS RECETAS"):
    if len(seleccionados) < 2:
        st.warning("Selecciona al menos 2 ingredientes.")
    else:
        st.subheader("📋 Propuestas del Chef")
        
        # Receta 1: El Plato Principal
        st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
        st.write("### 🍽️ Opción 1: Plato Fuerte")
        p_main = p_sel[0] if p_sel else seleccionados[0]
        c_main = c_sel[0] if c_sel else (v_sel[0] if v_sel else seleccionados[-1])
        st.write(f"**Preparación:** Cocina {p_main} y acompáñalo con {c_main}. Usa las salsas que elegiste para dar el toque final.")
        
        # Macros Receta 1
        st.markdown("<div class='ing-grid'>", unsafe_allow_html=True)
        t_c, t_p, t_g = 0, 0, 0
        for item in [p_main, c_main]:
            if item in DB:
                d = DB[item]; t_c+=d['c']; t_p+=d['p']; t_g+=d['g']
                st.markdown(f"<div class='ing-card'><b>{item}</b><br>{d['c']} kcal | {d['p']}g P</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.info(f"**Total:** 🔥 {t_c} kcal | 💪 {t_p}g P | 🥑 {t_g}g G")
        st.markdown("</div>", unsafe_allow_html=True)

        # Receta 2: El Snack o Postre
        if s_sel or len(seleccionados) > 2:
            st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
            st.write("### 🍫 Opción 2: El Antojo")
            snack = s_sel[0] if s_sel else seleccionados[1]
            base = c_sel[-1] if c_sel else "una base ligera"
            st.write(f"**Preparación:** Combina {snack} con {base}. ¡Disfruta!")
            st.markdown("</div>", unsafe_allow_html=True)

st.write("---")
st.subheader("📒 Mis Recetas Guardadas")
st.caption("Leiria 2026 | Sistema Nutricional")
