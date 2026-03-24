import streamlit as st

st.set_page_config(page_title="SmartBites Mega", page_icon="🍱", layout="centered")

# Diseño Visual Pro
st.markdown("""
    <style>
        .stApp { background: #f8fafc; }
        h1 { color: #1e293b; text-align: center; font-weight: 800; }
        div.stButton > button { 
            background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
            color: white; border-radius: 12px; border: none; padding: 15px;
            font-size: 1.2rem; font-weight: bold; width: 100%;
        }
        .recipe-card { background: white; padding: 20px; border-radius: 15px; border-left: 5px solid #2563eb; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🍱 SmartBites: El Todo-en-Uno</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Inventario Maestro: Comida Real, Chatarra, Snacks y Salsas</p>", unsafe_allow_html=True)

# --- BASE DE DATOS GIGANTE ---
categorias = {
    "🥩 Proteínas": ["Pollo", "Carne de Res", "Cerdo", "Tocino/Beicon", "Atún", "Salmón", "Gambas", "Huevos", "Salchichas", "Chorizo", "Salami", "Jamón Serrano", "Jamón York", "Pavo", "Tofu", "Nuggets", "Carne de Kebab"],
    "🥦 Vegetales/Legumbres": ["Brócoli", "Espinacas", "Lechuga", "Pepino", "Tomate", "Zanahoria", "Pimiento", "Cebolla", "Ajo", "Patata", "Batata", "Aguacate", "Lentejas", "Garbanzos", "Frijoles", "Maíz", "Champiñones"],
    "🍞 Carbohidratos": ["Arroz", "Pasta", "Pan de Molde", "Pan de Hamburguesa", "Tortillas", "Avena", "Cereal", "Rice Cakes", "Pizza Congelada", "Patatas Fritas (bolsa)", "Galletas Saladas"],
    "🧀 Lácteos": ["Leche", "Yogur", "Queso Crema", "Mozzarella", "Cheddar", "Queso Curado", "Mantequilla", "Nata", "Helado"],
    "🍫 Dulces/Snacks": ["Chocolate Negro", "Chocolate con Leche", "Chocolatina/Snickers", "Galletas Oreo", "Donas", "Croissants", "Gomitas", "Palomitas", "Nutella", "Miel", "Mermelada", "Frutos Secos"],
    "🥫 Salsas/Especias": ["Kétchup", "Mayonesa", "Mostaza", "Salsa BBQ", "Salsa de Soja", "Teriyaki", "Pesto", "Tomate Frito", "Tabasco", "Alioli", "Guacamole", "Aceite de Oliva", "Vinagre", "Sal", "Pimienta", "Orégano", "Curry", "Pimentón", "Chimichurri", "Salsa César"],
    "🥤 Bebidas": ["Agua", "Coca-Cola", "Refresco Zero", "Zumo", "Café", "Cerveza", "Vino", "Bebida Energética"]
}

# Inventario en el Sidebar
st.sidebar.header("🎒 Tu Despensa Total")
seleccion_total = []
for cat, items in categorias.items():
    sel = st.sidebar.multiselect(cat, items)
    seleccion_total.extend(sel)

# --- BOTÓN DE IA ---
if st.button("✨ ¡GENERAR RECETA CON TODO!"):
    if len(seleccion_total) < 2:
        st.warning("Selecciona al menos 2 o 3 cosas.")
    else:
        st.subheader("👨‍🍳 El Chef IA dice:")
        st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
        
        # Lógica creativa simple
        if any(x in seleccion_total for x in ["Pizza Congelada", "Salchichas", "Nuggets"]):
            st.success("### 🚀 Estilo 'Cheat Meal' Pro")
            st.write(f"Usa **{seleccion_total[0]}** y dale potencia con la salsa **{seleccion_total[-1]}**.")
        elif "Chocolate Negro" in seleccion_total or "Galletas Oreo" in seleccion_total:
            st.success("### 🍫 Antojo Dulce")
            st.write("Mezcla tus dulces con el yogur o lácteos para un postre rápido.")
        else:
            st.success(f"### 🥘 Mix Creativo: {seleccion_total[0]}")
            st.write(f"Cocina **{seleccion_total[0]}** con un toque de **{seleccion_total[-1]}**. ¡Sabor garantizado!")
        
        st.markdown("</div>", unsafe_allow_html=True)

# Rutinas de Leiria
st.write("---")
with st.expander("⭐ Mis Rutinas Guardadas (Plan 650 kcal)"):
    st.write("Recuerda: Pollo cremoso (Almuerzo) y Revuelto Pro (Desayuno).")

st.markdown("<br><p style='text-align: center; color: gray;'>SmartBites v2.1 | Leiria 2026</p>", unsafe_allow_html=True)
