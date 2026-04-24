import streamlit as st
import google.generativeai as genai

# Buscaremos la clave en los secretos del servidor
genai.configure(api_key=st.secrets["AIzaSyBxfxDLa-Eq8j1QXzkyGu-nFyY5AFjMzYE"])

# 2. Diseño de la página
st.title("Traductor de Sistemas Legados a Lenguaje Moderno 🚀")
st.write("Esta herramienta no solo explica, sino que REESCRIBE código antiguo en lenguajes modernos listos para usar.")

codigo_antiguo = st.text_area("Pega el código antiguo (COBOL, Fortran, etc.) aquí:", height=200)

# ¡NUEVO! Menú desplegable para elegir el lenguaje moderno
lenguaje_destino = st.selectbox(
    "¿A qué lenguaje moderno quieres traducir este código?",
    ("Python", "Java", "C#", "JavaScript")
)

# 3. La Lógica del Botón
if st.button("Analizar y Traducir"):
    if codigo_antiguo: 
        st.info(f"Convirtiendo el código a {lenguaje_destino}... por favor espera.")
        
        try:
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            # ¡NUEVO! Instrucciones más agresivas para la IA
            instruccion = f"""
            Eres un Ingeniero de Software Experto en migraciones de sistemas. Tu trabajo es:
            1. Analizar el código legado proporcionado.
            2. TRADUCIR y reescribir todo ese código a {lenguaje_destino} usando las mejores prácticas modernas.
            3. Añadir comentarios dentro del nuevo código para que sea fácil de entender.
            4. Al final, dar un breve resumen de las diferencias clave entre el código viejo y tu nueva versión.
            
            Código legado a traducir:
            {codigo_antiguo}
            """
            
            respuesta = model.generate_content(instruccion)
            
            # Mostramos el resultado en pantalla
            st.success(f"¡Traducción a {lenguaje_destino} completada!")
            st.write(respuesta.text)
            
        except Exception as e:
            st.error(f"Hubo un error de conexión: {e}")
    else:
        st.warning("Por favor, pega un poco de código antes de analizar.")