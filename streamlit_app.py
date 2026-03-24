import streamlit as st

# Configuración de la App
st.set_page_config(page_title="SmartBites Mega", page_icon="🍱", layout="centered")

# Estilos Visuales Premium (Modo Oscuro/Moderno)
st.markdown("""
    <style>
        .stApp { background: #f8fafc; }
        h1 { color: #1e293b; text-align: center; font-family: 'Inter', sans-serif; font-weight: 800; }
        .stMultiSelect [data-baseweb="tag"] { background-color: #3b82f6 !important; border-radius: 5px; }
        div.stButton > button { 
            background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
            color: white; border-radius: 12px; border: none; padding: 15px;
            font-size: 1.2rem; font-weight: bold; width: 100%; transition: 0.3s;
        }
        div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3); }
        .recipe-card { background: white; padding: 20px; border-radius: 15px; border-left: 5px solid #2563eb; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🍱 SmartBites: El Todo-en-Uno</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Inventario Maestro: Comida Real, Chatarra, Snacks y Salsas</p>", unsafe_allow_html=True)

# --- BASE DE DATOS GIGANTE ---
categorias = {
    "🥩 Proteínas (Animal y Vegetal)": [
        "Pollo (Pechuga/Muslo)", "Carne de Res (Filete/Molida)", "Cerdo (Lomo/Chuleta)", "Tocino/Beicon", 
        "Atún (Lata/Fresco)", "Salmón", "Gambas/Camarones", "Merluza/Bacalao", "Pulpo",
        "Huevos", "Claras de huevo", "Jamón Serrano", "Jamón York/Pavo", "Salchichas/Frankfurt",
        "Chorizo", "Salami", "Tofu", "Seitán", "Salchichón", "Mortadela"
    ],
    "🥦 Vegetales y Legumbres": [
        "Brócoli", "Espinacas", "Lechuga", "Pepino", "Tomate", "Zanahoria", "Pimiento (Rojo/Verde/Amarillo)",
        "Cebolla (Blanca/Morada)", "Ajo", "Calabacín", "Berenjena", "Champiñones", "Patata/Papa", 
        "Batata/Camote", "Aguacate", "Lentejas", "Garbanzos", "Judías/Frijoles", "Maíz en lata", "Guisantes"
    ],
    "🍞 Carbohidratos y Pastas": [
        "Arroz Blanco", "Arroz Integral", "Pasta (Espagueti/Macarrones)", "Pan de Molde", "Pan Artesanal",
        "Pan de Hamburguesa/Hot Dog", "Tortillas de Trigo/Maíz", "Avena", "Quinoa", "Cuscús",
        "Cereal de Desayuno", "Granola", "Rice Cakes (Tortitas de arroz)"
    ],
    "🧀 Lácteos y Quesos": [
        "Leche Entera/Desnatada", "Yogur Natural/Griego", "Yogur de Sabores", "Queso Crema (Philadelphia)",
        "Queso Mozzarella", "Queso Cheddar", "Queso Manchego/Curado", "Queso Parmesano", "Mantequilla",
        "Nata/Crema de leche", "Kéfir"
    ],
    "🍟 Comida Chatarra y Congelados": [
        "Pizza Congelada", "Nuggets de Pollo", "Patatas Fritas (Bolsa)", "Patatas Fritas (Congeladas)",
        "Hamburguesa Congelada", "Lasaña Preparada", "Varitas de Pescado", "Empanadillas", "Kebab (Carne)"
    ],
    "🍫 Dulces, Snacks y Repostería": [
        "Chocolate Negro (70%+)", "Chocolate con Leche", "Chocolatina (Snickers/Mars)", "Galletas (Oreo/Maria)",
        "Donas/Donuts", "Croissants/Bollería", "Helado", "Gomitas/Chuches", "Palomitas de maíz", 
        "Frutos Secos (Almendras/Nueces)", "Crema de Cacahuete", "Nutella/Nocilla", "Miel", "Mermelada"
    ],
    "🥫 Salsas y Condimentos": [
        "Kétchup", "Mayonesa", "Mostaza", "Salsa BBQ", "Salsa de Soja", "Salsa Teriyaki", 
        "Salsa Pesto", "Salsa de Tomate/Frito", "Tabasco/Picante", "Alioli", "Guacamole", 
        "Vinagre (Módena/Manzana)", "Aceite de Oliva", "Aceite de Girasol", "Sal e Himayala", 
        "Pimienta", "Orégano", "Pimentón", "Curry", "Salsa César"
    ],
    "🥤 Bebidas": [
        "Agua", "Coca-Cola/Pepsi", "Refresco Light/Zero", "Zumo de Naranja", "Café", "Té",
        "Cerveza", "Vino", "Bebida Energética"
    ]
}

# --- INTERFAZ ---
st.sidebar.header("🎒 Tu Mochila de Comida")
seleccion_total = []
for cat, items in categorias.items():
    sel = st.sidebar.multiselect(cat, items)
    seleccion_total.extend(sel)

st.sidebar.write("---")
st.sidebar.caption(f"Tienes {len(seleccion_total)} ingredientes listos.")

# --- EL MOTOR DE IA CREATIVA ---
if st.button("✨ ¡GENERAR RECETA CON TODO!"):
    if len(seleccion_total) < 2:
        st.warning("Selecciona al menos 2 o 3 cosas para que pueda ser creativa.")
    else:
        st.subheader("👨‍🍳 El Chef IA dice:")
        
        # Lógica de Combinación Dinámica
        if any(x in seleccion_total for x in ["🍕 Pizza Congelada", "🌭 Salchichas/Frankfurt", "🍔 Hamburguesa Congelada"]):
            st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
            st.success("### 🚀 Nivel: 'Cheat Meal' Mejorado")
            st.write(f"Vas a usar **{seleccion_total[0]}** como base, pero para que sea una receta pro, añade **{seleccion_total[-1]}** por encima.")
            st.write("**Truco:** Si tienes alguna salsa como **Mayonesa o BBQ**, mézclala con un poco de limón para que no sea tan pesada.")
            st.markdown("</div>", unsafe_allow_html=True)
        
        elif "🍫 Chocolate Negro (70%+)" in seleccion_total or "🍪 Galletas (Oreo/Maria)" in seleccionados:
            st.success("### 🍫 Momento Dulce")
            st.write("Crea un bowl usando el yogur o la avena como base, pica el chocolate y añade frutas si tienes.")
            
        else:
            st.success(f"### 🍲 Combinación: {seleccion_total[0]} Estilo Gourmet")
            st.write(f"Crea una base con **{seleccion_total[1]}**, cocina la proteína (**{seleccion_total[0]}**) y dale el toque final con la salsa **{seleccion_total[-1] if len(seleccion_total)>2 else 'que elijas'}**.")

# --- PLAN DE COMIDAS FIJO ---
st.write("---")
with st.expander("⭐ Mis Rutinas Guardadas (Leiria)"):
    st.write("**Saludable:** Pollo con Brócoli y Queso Crema.")
    st.write("**Snack:** Rice Cakes con Jamón y Chocolate 70%.")
    st.write("**Antojo:** Pizza con extra de vegetales y salsa picante.")

st.markdown("<br><p style='text-align: center; color: #94a3b8;'>SmartBites v2.0 - Todo lo que necesitas en una App</p>", unsafe_allow_html=True)
