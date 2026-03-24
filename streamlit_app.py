import streamlit as st
import random

# Configuración de página
st.set_page_config(page_title="SmartBites Ultra Pro", page_icon="👩‍🍳", layout="wide")

# Diseño Visual
st.markdown("""
    <style>
        .stApp { background-color: #f1f5f9; }
        .recipe-card { background: white; padding: 25px; border-radius: 15px; border-left: 8px solid #1e40af; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 20px; }
        .macro-tag { background: #3b82f6; color: white; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 0.85rem; }
        .ing-card { border: 1px solid #e2e8f0; padding: 10px; border-radius: 10px; text-align: center; background: #f8fafc; }
    </style>
""", unsafe_allow_html=True)

st.title("👩‍🍳 SmartBites: Chef IA Real")
st.write("Recetas con lógica culinaria, macros por ingrediente y base de datos extendida.")

# --- BASE DE DATOS EXTENDIDA DE MACROS (por 100g) ---
DB = {
    # Proteínas (Carnes, Mariscos, Embutidos)
    "Pollo": {"c": 165, "p": 31, "g": 3.6, "h": 0}, "Carne de Res": {"c": 250, "p": 26, "g": 15, "h": 0},
    "Lomo de Cerdo": {"c": 242, "p": 27, "g": 14, "h": 0}, "Tocino/Beicon": {"c": 541, "p": 37, "g": 42, "h": 1.4},
    "Atún": {"c": 116, "p": 26, "g": 1, "h": 0}, "Salmón": {"c": 208, "p": 20, "g": 13, "h": 0},
    "Gambas/Camarones": {"c": 99, "p": 24, "g": 0.3, "h": 0.2}, "Huevos": {"c": 155, "p": 13, "g": 11, "h": 1.1},
    "Jamón Serrano": {"c": 240, "p": 30, "g": 12, "h": 0}, "Salchichas": {"c": 301, "p": 12, "g": 25, "h": 2},
    "Chorizo": {"c": 455, "p": 24, "g": 38, "h": 2}, "Nuggets": {"c": 296, "p": 15, "g": 20, "h": 14},
    # Carbohidratos (Sanos y Chatarra)
    "Arroz": {"c": 130, "p": 2.7, "g": 0.3, "h": 28}, "Pasta": {"c": 158, "p": 5.8, "g": 0.9, "h": 31},
    "Patatas/Papas": {"c": 77, "p": 2, "g": 0.1, "h": 17}, "Pan de Molde": {"c": 265, "p": 9, "g": 3, "h": 49},
    "Pizza Congelada": {"c": 266, "p": 11, "g": 10, "h": 33}, "Hamburguesa": {"c": 295, "p": 17, "g": 14, "h": 24},
    "Patatas Fritas (Bolsa)": {"c": 536, "p": 7, "g": 35, "h": 53}, "Quinoa": {"c": 120, "p": 4.4, "g": 1.9, "h": 21},
    "Rice Cakes": {"c": 387, "p": 8, "g": 2.8, "h": 82}, "Nachos": {"c": 497, "p": 7, "g": 25, "h": 61},
    # Vegetales y Frutas
    "Aguacate": {"c": 160, "p": 2, "g": 15, "h": 9}, "Brócoli": {"c": 34, "p": 2.8, "g": 0.4, "h": 7},
    "Tomate": {"c": 18, "p": 0.9, "g": 0.2, "h": 3.9}, "Pepino": {"c": 15, "p": 0.7, "g": 0.1, "h": 3.6},
    "Zanahoria": {"c": 41, "p": 0.9, "g": 0.2, "h": 10}, "Espinacas": {"c": 23, "p": 2.9, "g": 0.4, "h": 3.6},
    "Cebolla": {"c": 40, "p": 1.1, "g": 0.1, "h": 9}, "Plátano": {"c": 89, "p": 1.1, "g": 0.3, "h": 23},
    # Salsas y Dulces
    "Mayonesa": {"c": 680, "p": 1, "g": 75, "h": 1}, "Kétchup": {"c": 112, "p": 1.3, "g": 0.1, "h": 27},
    "Nutella": {"c": 539, "p": 6, "g": 31, "h": 57}, "Chocolate 70%": {"c": 546, "p": 5, "g": 31, "h": 61},
    "Queso Crema": {"c": 342, "p": 6, "g": 34, "h": 4}, "Mantequilla de Mani": {"c": 588, "p": 25, "g": 50, "h": 20},
    "Miel": {"c": 304, "p": 0.3, "g": 0, "h": 82}, "Mostaza": {"c": 66, "p": 4.4, "g": 4, "h": 5}
}

# --- SIDEBAR: CATEGORÍAS ---
st.sidebar.header("🛒 Inventario Maestro")
tipo_cocina = st.sidebar.radio("Estilo de comida:", ["Fitness", "Equilibrada", "Cheat Meal"])

def cat(titulo, lista):
    with st.sidebar.expander(titulo):
        return st.multiselect(f"Añadir {titulo}:", lista)

p_sel = cat("🥩 Proteínas", ["Pollo", "Carne de Res", "Lomo de Cerdo", "Atún", "Salmón", "Gambas/Camarones", "Huevos", "Jamón Serrano", "Salchichas", "Chorizo", "Nuggets"])
c_sel = cat("🍞 Carbohidratos", ["Arroz", "Pasta", "Patatas/Papas", "Pan de Molde", "Pizza Congelada", "Hamburguesa", "Patatas Fritas (Bolsa)", "Quinoa", "Rice Cakes", "Nachos"])
v_sel = cat("🥦 Vegetales y Frutas", ["Aguacate", "Brócoli", "Tomate", "Pepino", "Zanahoria", "Espinacas", "Cebolla", "Plátano"])
s_sel = cat("🥫 Salsas y Dulces", ["Mayonesa", "Kétchup", "Mostaza", "Nutella", "Chocolate 70%", "Queso Crema", "Mantequilla de Mani", "Miel"])

todos = p_sel + c_sel + v_sel + s_sel

# --- MOTOR DE RECETAS INTELIGENTES ---
if st.button("✨ GENERAR MENÚ CON COHERENCIA"):
    if not p_sel and not c_sel:
        st.error("Selecciona al menos una base (Proteína o Carbohidrato).")
    else:
        st.subheader(f"📋 Propuestas {tipo_cocina}")
        
        # Lógica para 3 recetas distintas
        for i in range(1, 4):
            # Selección de ingredientes por "afinidad"
            if i == 1 and p_sel: # Receta principal Salada
                ing_main = [p_sel[0]] + (v_sel[:2] if v_sel else []) + (c_sel[:1] if c_sel else [])
                nombre = f"Plato Fuerte: {p_sel[0]} al Estilo {tipo_cocina}"
                instrucciones = f"Cocina el {p_sel[0]} a la plancha. Acompáñalo con {' y '.join(ing_main[1:])}. Usa una pizca de sal y pimienta."
            elif i == 2 and s_sel: # Receta Dulce o Snack
                ing_main = [s_sel[0]] + (c_sel[-1:] if c_sel else []) + (v_sel[-1:] if v_sel else [])
                nombre = f"Snack/Postre: Capricho de {s_sel[0]}"
                instrucciones = f"Usa el/la {ing_main[1] if len(ing_main)>1 else 'base'} y añade {s_sel[0]} por encima. Ideal para calmar el antojo."
            else: # Receta Mix Rápida
                ing_main = random.sample(todos, min(3, len(todos)))
                nombre = f"Receta Rápida: Mix {ing_main[0]}"
                instrucciones = f"Saltea {ing_main[0]} con {' y '.join(ing_main[1:])}. ¡Rápido y efectivo!"

            # Renderizado
            st.markdown(f"<div class='recipe-card'>", unsafe_allow_html=True)
            st.write(f"### {nombre}")
            st.write(f"**Preparación:** {instrucciones}")
            
            # Macros Detallados
            cols = st.columns(len(ing_main))
            t_c, t_p, t_g = 0, 0, 0
            for idx, item in enumerate(ing_main):
                data = DB.get(item, {"c":0,"p":0,"g":0,"h":0})
                t_c += data['c']; t_p += data['p']; t_g += data['g']
                with cols[idx]:
                    st.markdown(f"<div class='ing-card'><b>{item}</b><br>🔥 {data['c']} kcal<br>💪 {data['p']}g P</div>", unsafe_allow_html=True)
            
            st.info(f"**TOTAL ESTIMADO:** 🔥 {t_c} kcal | 💪 {t_p}g Proteína | 🥑 {t_g}g Grasas")
            st.button(f"⭐ Guardar Receta {i}", key=f"save_{i}_{random.randint(0,999)}")
            st.markdown("</div>", unsafe_allow_html=True)

# --- GUARDADOS ---
st.write("---")
st.subheader("📒 Mis Recetas Guardadas")
st.write("Tus favoritos de Leiria (650 kcal) están siempre seguros aquí.")
