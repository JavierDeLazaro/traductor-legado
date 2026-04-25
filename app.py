import streamlit as st
import google.generativeai as genai

# 1. Configuración de seguridad
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Diccionario para saber qué extensión poner al archivo descargable
extensiones = {
    "Python": "py",
    "Java": "java",
    "C#": "cs",
    "JavaScript": "js",
    "Go": "go"
}

# 2. Interfaz de usuario
st.set_page_config(page_title="Legacy Migrator Pro", page_icon="🚀")
st.title("Migración de Sistemas Legados con IA 🚀")
st.write("Transforma código antiguo en activos modernos y descargables.")

archivo_subido = st.file_uploader("Sube tu archivo de código (.cob, .txt, .cbl)", type=["cob", "txt", "cbl", "f90"])

st.write("---")
codigo_manual = st.text_area("O pega el código aquí:", height=150)

lenguaje_destino = st.selectbox(
    "Selecciona el lenguaje moderno de destino:",
    ("Python", "Java", "C#", "JavaScript", "Go")
)

# 3. Lógica de procesamiento
if st.button("Ejecutar Migración"):
    codigo_a_traducir = ""
    
    if archivo_subido is not None:
        codigo_a_traducir = archivo_subido.read().decode("utf-8")
    elif codigo_manual:
        codigo_a_traducir = codigo_manual
        
    if codigo_a_traducir: 
        with st.spinner(f"Migrando sistema a {lenguaje_destino}..."):
            try:
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                instruccion = f"""
                Eres un Arquitecto de Software Experto. Traduce este código a {lenguaje_destino}.
                Devuelve únicamente el código limpio, bien comentado y una breve explicación al final.
                
                Código original:
                {codigo_a_traducir}
                """
                
                respuesta = model.generate_content(instruccion)
                resultado_final = respuesta.text
                
                st.success("✅ Migración completada con éxito.")
                
                # Mostramos el resultado en pantalla
                st.code(resultado_final, language=lenguaje_destino.lower())
                
                # --- ¡NUEVO! SECCIÓN DE DESCARGA ---
                nombre_archivo = f"migracion_legada.{extensiones[lenguaje_destino]}"
                
                st.download_button(
                    label="📥 Descargar Código Convertido",
                    data=resultado_final,
                    file_name=nombre_archivo,
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"Error técnico: {e}")
    else:
        st.warning("Debes proporcionar código para traducir.")
