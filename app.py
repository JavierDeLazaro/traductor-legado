import streamlit as st
import google.generativeai as genai

# 1. Configurar la conexión segura
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# 2. Diseño de la página Enterprise
st.title("Migración de Sistemas Legados con IA 🚀")
st.write("Sube tus archivos de código antiguo o pégalos manualmente para traducirlos a lenguajes modernos listos para producción.")

# ¡NUEVO! Zona de arrastrar y soltar archivos
archivo_subido = st.file_uploader("Sube tu archivo de código (.cob, .txt, .cbl)", type=["cob", "txt", "cbl", "f90"])

st.write("---") # Una línea divisoria elegante
st.write("O si prefieres hacer una prueba rápida, pega el código aquí:")
codigo_manual = st.text_area("Código legado:", height=150)

lenguaje_destino = st.selectbox(
    "¿A qué lenguaje moderno quieres traducir este código?",
    ("Python", "Java", "C#", "JavaScript", "Go")
)

# 3. La Lógica del Botón
if st.button("Analizar y Traducir"):
    
    # Lógica para decidir si usamos el archivo o el texto manual
    codigo_a_traducir = ""
    
    if archivo_subido is not None:
        # Si subieron un archivo, lo leemos y lo decodificamos a texto
        codigo_a_traducir = archivo_subido.read().decode("utf-8")
        st.success(f"Archivo '{archivo_subido.name}' leído correctamente.")
    elif codigo_manual:
        # Si no hay archivo pero escribieron algo en la caja
        codigo_a_traducir = codigo_manual
        
    # Si tenemos código (ya sea de archivo o manual), llamamos a la IA
    if codigo_a_traducir: 
        st.info(f"Procesando el código y convirtiendo a {lenguaje_destino}... por favor espera.")
        
        try:
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            instruccion = f"""
            Eres un Arquitecto de Software Experto en migraciones de sistemas bancarios y gubernamentales. 
            Tu trabajo es:
            1. Analizar el código legado proporcionado.
            2. TRADUCIR y reescribir todo ese código a {lenguaje_destino} usando las mejores prácticas modernas.
            3. Añadir comentarios dentro del nuevo código para que sea fácil de entender.
            4. Al final, dar un breve resumen de las diferencias clave y por qué esta nueva versión es más segura y eficiente.
            
            Código legado a traducir:
            {codigo_a_traducir}
            """
            
            respuesta = model.generate_content(instruccion)
            
            st.success(f"¡Traducción a {lenguaje_destino} completada!")
            st.write(respuesta.text)
            
        except Exception as e:
            st.error(f"Hubo un error de conexión con el motor de IA: {e}")
    else:
        st.warning("Por favor, sube un archivo o pega un poco de código antes de hacer clic en traducir.")
