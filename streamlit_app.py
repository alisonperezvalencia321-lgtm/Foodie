import streamlit as st

# Configuración de la App
st.set_page_config(page_title="SmartBites Ultra", page_icon="🍔", layout="centered")

# Estilos Visuales Mejorados
st.markdown("""
    <style>
        .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
        h1 { color: #1e3a8a; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .stMultiSelect [data-baseweb="tag"] { background-color: #1e3a8a !important; }
        div.stButton > button { 
            background-color: #2563eb; color: white; border-radius: 25px; 
            width: 100%; font-weight: bold; border: none; padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🍔 SmartBites: El Todo-en-Uno</h1>", unsafe_allow_html=True)
st.write("Tu inventario completo: **Saludable, Snacks y Antojos**")
st.write("---")

# --- SECCIÓN DE INVENTARIO COMPLETO ---
st.sidebar.markdown("### 🛒 Mi Despensa Total")

# Categorías de comida
proteinas = ["🍗 Pollo", "🥩 Carne de Res", "🐟 Atún", "🥚 Huevos/Claras", "🥓 Jamón/Pavo", "🌭 Salchichas", "🍤 Gambas", "🍣 Salmón"]
vegetales = ["🥦 Brócoli", "🥒 Pepino", "🥕 Zanahoria", "🫑 Pimiento", "🥗 Lechuga/Espinaca", "🍅 Tomate", "🧅 Cebolla", "🥔 Patata/Papa"]
lacteos = ["🥛 Leche", "🍦 Yogur Light", "🧀 Queso Crema", "🧀 Mozzarella", "🧀 Queso Curado", "🧈 Mantequilla"]
snacks_chatarra = ["🍫 Chocolate 70%", "🍫 Chocolatina/Snickers", "🍪 Galletas", "🍟 Patatas Fritas", "🍕 Pizza Congelada", "🍦 Helado", "🍿 Palomitas", "🥨 Pretzels"]
carbs_basicos = ["🍚 Arroz", "🍝 Pasta", "🍞 Pan Blanco", "🍞 Pan Integral", "🍘 Rice Cakes", "🥣 Avena"]
extras = ["🥑 Aguacate", "🍯 Miel", "🧴 Mayonesa", "🥫 Kétchup", "🥜 Crema de Cacahuete", "🍋 Limón"]

# Unimos todo en un gran buscador
todo_el_alimento = proteinas + vegetales + lacteos + carbs_basicos + snacks_chatarra + extras

seleccionados = st.sidebar.multiselect("¿Qué tienes hoy?", todo_el_alimento)

st.sidebar.write("---")
st.sidebar.info("Tip: Mezcla algo 'chatarra' con algo 'light' para equilibrar.")

# --- LÓGICA DE LA IA CREATIVA ---
if st.button("✨ ¡Generar Combinación Creativa!"):
    if not seleccionados:
        st.warning("Selecciona al menos un par de cosas de la lista.")
    else:
        st.subheader("👨‍🍳 La Propuesta de la IA")
        
        # Ejemplo de lógica cruzada (Saludable + Chatarra)
        if "🍕 Pizza Congelada" in seleccionados and "🥗 Lechuga/Espinaca" in seleccionados:
            st.success("### 🍕 Pizza Balanceada")
            st.write("Hornea la pizza pero añade una montaña de espinacas frescas y tomate encima para dar volumen y fibra.")
        
        elif "🍫 Chocolate 70%" in seleccionados and "🥣 Avena" in seleccionados:
            st.success("### 🥣 Avena 'Ferrero'")
            st.write("Haz la avena con leche y derrite el chocolate dentro. Añade un poco de sal para resaltar el sabor.")
            
        elif "🌭 Salchichas" in seleccionados and "🥒 Pepino" in seleccionados:
            st.success("### 🌭 Hot-Dog 'Fresh'")
            st.write("Corta las salchichas y mézclalas con pepino y limón. ¡Un snack alto en proteína y muy fresco!")
            
        else:
            st.info(f"Tienes una buena mezcla. Prueba a usar la proteína (**{seleccionados[0]}**) como base y añade un toque de tus snacks para el final.")

# --- PLAN DE COMIDAS GUARDADO ---
st.write("---")
st.subheader("📒 Mis Favoritos Guardados")

col1, col2 = st.columns(2)
with col1:
    with st.expander("🥗 Opción Light"):
        st.write("Atún con pepino y limón.")
        st.caption("Bajo en calorías.")
with col2:
    with st.expander("🍕 Opción Cheat"):
        st.write("Rice cakes con crema de cacahuete y chocolate.")
        st.caption("Para el antojo.")

st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>App personalizada para Alison | Leiria 2026</p>", unsafe_allow_html=True)
