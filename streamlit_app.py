import streamlit as st
import random

# Configuración de página
st.set_page_config(page_title="SmartBites Ultra Pro", page_icon="🥘", layout="wide")

# Diseño Visual Profesional
st.markdown("""
    <style>
        .stApp { background-color: #f1f5f9; }
        .recipe-card { background: white; padding: 25px; border-radius: 15px; border-left: 10px solid #2563eb; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 25px; }
        .macro-tag { background: #eff6ff; color: #1e40af; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 0.85rem; border: 1px solid #bfdbfe; }
        .ing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); gap: 10px; margin-top: 10px; }
        .ing-item { background: #f8fafc; border: 1px solid #e2e8f0; padding: 8px; border-radius: 10px; text-align: center; font-size: 0.8rem; }
    </style>
""", unsafe_allow_html=True)

st.title("🥘 SmartBites Ultra Pro")
st.write("Sistema Inteligente de Nutrición | Leiria 2026")

# --- BASE DE DATOS GIGANTE (Macros por 100g) ---
DB = {
    # PROTEÍNAS
    "Pollo": {"c": 165, "p": 31, "g": 3}, "Carne de Res": {"c": 250, "p": 26, "g": 15}, "Lomo de Cerdo": {"c": 242, "p": 27, "g": 14},
    "Atún": {"c": 116, "p": 26, "g": 1}, "Salmón": {"c": 208, "p": 20, "g": 13}, "Gambas": {"c": 99, "p": 24, "g": 0},
    "Huevos": {"c": 155, "p": 13, "g": 11}, "Beicon": {"c": 541, "p": 37, "g": 42}, "Salchichas": {"c": 300, "p": 12, "g": 25},
    "Nuggets": {"c": 290, "p": 15, "g": 18}, "Jamón Serrano": {"c": 240, "p": 30, "g": 12}, "Carne de Kebab": {"c": 230, "p": 15, "g": 18},
    "Pavo": {"c": 135, "p": 29, "g": 1}, "Chorizo": {"c": 450, "p": 24, "g": 38}, "Salami": {"c": 330, "p": 13, "g": 28},
    # CARBS / CHATARRA
    "Arroz": {"c": 130, "p": 3, "g": 0, "h": 28}, "Pasta": {"c": 158, "p": 6, "g": 1, "h": 31}, "Patatas": {"c": 77, "p": 2, "g": 0, "h": 17},
    "Pan de Molde": {"c": 265, "p": 9, "g": 3, "h": 49}, "Pizza": {"c": 266, "p": 11, "g": 10, "h": 33}, "Hamburguesa": {"c": 295, "p": 17, "g": 14},
    "Patatas Fritas": {"c": 536, "p": 7, "g": 35}, "Nachos": {"c": 497, "p": 7, "g": 25}, "Rice Cakes": {"c": 387, "p": 8, "g": 3},
    "Cereal": {"c": 370, "p": 7, "g": 2}, "Croissant": {"c": 406, "p": 8, "g": 21}, "Galletas Oreo": {"c": 480, "p": 5, "g": 20},
    # VEGETALES / FRUTAS
    "Aguacate": {"c": 160, "p": 2, "g": 15}, "Brócoli": {"c": 34, "p": 3, "g": 0}, "Tomate": {"c": 18, "p": 1, "g": 0},
    "Pepino": {"c": 15, "p": 1, "g": 0}, "Cebolla": {"c": 40, "p": 1, "g": 0}, "Plátano": {"c": 89, "p": 1, "g": 0},
    "Zanahoria": {"c": 41, "p": 1, "g": 0}, "Espinacas": {"c": 23, "p": 3, "g": 0}, "Lechuga": {"c": 15, "p": 1, "g": 0},
    # SALSAS / DULCES
    "Mayonesa": {"c": 680, "p": 1, "g": 75}, "Kétchup": {"c": 112, "p": 1, "g": 0}, "Nutella": {"c": 539, "p": 6, "g": 31},
    "Chocolate": {"c": 546, "p": 5, "g": 31}, "Queso Crema": {"c": 342, "p": 6, "g": 34}, "Miel": {"c": 304, "p": 0, "g": 0},
    "Mantequilla de Mani": {"c": 588, "p": 25, "g": 50}, "Salsa BBQ": {"c": 172, "p": 1, "g": 1}, "Alioli": {"c": 700, "p": 1, "g": 78},
    "Mostaza": {"c": 66, "p": 4, "g": 4}
}

# --- SIDEBAR: CATEGORÍAS ---
st.sidebar.header("🛒 Mi Despensa")
modo = st.sidebar.selectbox("Estilo de recetas:", ["Variado", "Fitness", "Cheat Meal", "Ecuatoriano/Portugués"])

def build_cat(name, items):
    with st.sidebar.expander(name):
        return st.multiselect(f"Añadir {name}:", items)

p_s = build_cat("🥩 Proteínas", ["Pollo", "Carne de Res", "Lomo de Cerdo", "Atún", "Salmón", "Gambas", "Huevos", "Beicon", "Salchichas", "Nuggets", "Jamón Serrano", "Pavo", "Chorizo", "Salami"])
c_s = build_cat("🍞 Carbohidratos", ["Arroz", "Pasta", "Patatas", "Pan de Molde", "Pizza", "Hamburguesa", "Patatas Fritas", "Nachos", "Rice Cakes", "Cereal", "Croissant", "Galletas Oreo"])
v_s = build_cat("🥦 Vegetales y Frutas", ["Aguacate", "Brócoli", "Tomate", "Pepino", "Cebolla", "Plátano", "Zanahoria", "Espinacas", "Lechuga"])
s_s = build_cat("🥫 Salsas y Dulces", ["Mayonesa", "Kétchup", "Nutella", "Chocolate", "Queso Crema", "Miel", "Mantequilla de Mani", "Salsa BBQ", "Alioli", "Mostaza"])

# --- GENERADOR DE RECETAS ---
if st.button("✨ GENERAR MENÚ PROFESIONAL"):
    if not (p_s or c_s or s_s):
        st.error("Selecciona ingredientes para cocinar algo.")
    else:
        st.subheader(f"👨‍🍳 Menú del día ({modo})")
        
        # OPCIÓN 1: PLATO PRINCIPAL (COHERENTE)
        if p_s:
            st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
            st.write("### 🍽️ Opción 1: Plato Fuerte")
            main = p_s[0]
            side = c_s[0] if c_s else (v_s[0] if v_s else "una base ligera")
            extra = v_s[0] if (v_s and v_s[0] != side) else "especias"
            st.write(f"**Receta:** {main} a la plancha con acompañamiento de {side}. Saltea con {extra} para dar sabor.")
            
            t_c, t_p, t_g = 0, 0, 0
            st.markdown("<div class='ing-grid'>", unsafe_allow_html=True)
            for item in [main, side]:
                if item in DB:
                    d = DB[item]
                    t_c+=d['c']; t_p+=d['p']; t_g+=d['g']
                    st.markdown(f"<div class='ing-item'><b>{item}</b><br>{d['c']} kcal | {d['p']}g P</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.write(f"**Total:** 🔥 {t_c} kcal | 💪 {t_p}g Prot | 🥑 {t_g}g Grasas")
            st.markdown("</div>", unsafe_allow_html=True)

        # OPCIÓN 2: EL SNACK O ANTOJO
        if s_s or c_s:
            st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
            st.write("### 🍫 Opción 2: El Snack")
            base_s = c_s[-1] if len(c_s)>1 else (p_s[-1] if len(p_s)>1 else "base")
            dulce = s_s[0] if s_s else "Queso Crema"
            st.write(f"**Receta:** Toma {base_s} y úntale {dulce}. Perfecto para un snack rápido.")
            st.markdown("</div>", unsafe_allow_html=True)

        # OPCIÓN 3: MIX CREATIVO
        st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
        st.write("### 🥗 Opción 3: El Bowl Rápido")
        mix = random.sample(p_s + c_s + v_s, min(3, len(p_s + c_s + v_s)))
        st.write(f"**Receta:** Corta en cubitos {' y '.join(mix)}. Mézclalo todo en un bowl con un toque de {s_s[-1] if s_s else 'aceite'}.")
        st.markdown("</div>", unsafe_allow_html=True)

st.write("---")
st.subheader("📒 Mis Recetas Guardadas")
st.caption("Tus recetas de 650 kcal para la UFC y más están seguras aquí.")
