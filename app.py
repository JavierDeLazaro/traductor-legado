import streamlit as st
import google.generativeai as genai
from PIL import Image # Necesario para manejar el icono

# 1. Configuración de seguridad (Mantenemos tu secreto)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Diccionario de extensiones (Mantenemos la funcionalidad)
extensiones = {
    "Python": "py",
    "Java": "java",
    "C#": "cs",
    "JavaScript": "js",
    "Go": "go"
}

# 2. Interfaz de usuario - COREBRIDGE AI PREMIUM BRANDING
# Intentamos cargar el icono profesional.
try:
    image = Image.open('icono_corebridge_ai.png')
    
    # ¡NUEVO! Configuración de la pestaña (favicon y título)
    st.set_page_config(
        page_title="CoreBridge AI - Legacy Migration", # Título en la pestaña
        page_icon=image, # El icono cristalino en la pestaña
        layout="wide"
    )

    # Colocamos el icono principal en la cabecera
    # Usamos columnas para centrar el icono cristalino y que no ocupe todo el ancho
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        # Mostramos la imagen entera con el efecto cristalino
        st.image(image, use_column_width=True)
        
except FileNotFoundError:
    # Si olvidaron guardar la imagen, mostramos configuración por defecto
    st.set_page_config(page_title="CoreBridge AI", page_icon="🚀", layout="wide")
    st.title("CoreBridge AI")
    st.warning("⚠️ Nota del Ingeniero: No se encontró el archivo 'icono_corebridge_ai.png' en la carpeta. Guarda la imagen allí para ver el branding profesional en la cabecera y pestaña.")

st.write("---") # Línea divisoria elegante

# Título y descripción actualizados con la marca Premium
st.header("Plataforma de Modernización de Código Inteligente")
st.write("Transforma tus sistemas Core antiguos (COBOL, Fortran, etc.) en activos modernos, seguros y descargables, utilizando la tecnología cristalina de CoreBridge AI.")

# Zona de archivos (Mantenemos funcionalidad)
archivo_subido = st.file_uploader("Sube tu archivo de código legado (.cob, .txt, .cbl)", type=["cob", "txt", "cbl", "f90"])

st.write("---")
codigo_manual = st.text_area("O pega el código aquí manualmente:", height=150)

lenguaje_destino = st.selectbox(
    "Selecciona el lenguaje moderno de destino:",
    ("Python", "Java", "C#", "JavaScript", "Go")
)

# 3. Lógica de procesamiento y descarga (Mantenemos funcionalidad)
if st.button("Ejecutar Migración Inteligente"):
    codigo_a_traducir = ""
    
    if archivo_subido is not None:
        # Decodificamos el archivo subido
        codigo_a_traducir = archivo_subido.read().decode("utf-8")
        st.success(f"✅ Archivo '{archivo_subido.name}' cargado de forma segura en CoreBridge AI.")
    elif codigo_manual:
        codigo_a_traducir = codigo_manual
        
    if codigo_a_traducir: 
        # Spinner actualizado con la marca
        with st.spinner(f"CoreBridge AI está migrando el sistema a {lenguaje_destino}. Por favor, espera..."):
            try:
                # Usamos el modelo 2.5 flash
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                # Instrucción de Arquitecto Senior
                instruccion = f"""
                Eres un Arquitecto de Software Experto de CoreBridge AI. Tu trabajo es:
                1. Analizar el código legado proporcionado.
                2. Traducirlo y reescribirlo completamente a {lenguaje_destino} aplicando las mejores prácticas modernas, seguridad inherente y patrones de diseño eficientes.
                3. Añadir comentarios detallados en español dentro del nuevo código para explicar la lógica.
                4. Al final, proporcionar una breve explicación técnica de los cambios clave realizados para un Director de IT.
                
                Código original a procesar:
                {codigo_a_traducir}
                """
                
                respuesta = model.generate_content(instruccion)
                resultado_final = respuesta.text
                
                st.write("---")
                st.subheader("Resultado de la Migración Cristalina")
                
                # Mostramos el resultado con formato de código
                st.code(resultado_final, language=lenguaje_destino.lower())
                
                # --- SECCIÓN DE DESCARGA (Mantenemos funcionalidad) ---
                nombre_archivo = f"migracion_corebridge.{extensiones[lenguaje_destino]}"
                
                # Un poco de espacio extra antes del botón
                st.write(" ")
                
                st.download_button(
                    label=f"📥 Descargar Código Convertido ({extensiones[lenguaje_destino].upper()})",
                    data=resultado_final,
                    file_name=nombre_archivo,
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"Error técnico de conexión con CoreBridge AI: {e}")
    else:
        st.warning("Por favor, proporciona un archivo o pega código antes de ejecutar la migración.")
