import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración Inicial (Debe ser la primera línea)
try:
    image = Image.open('icono_corebridge_ai.png')
    st.set_page_config(page_title="CoreBridge AI | Legacy Migration", page_icon=image, layout="centered")
except:
    st.set_page_config(page_title="CoreBridge AI", page_icon="🚀", layout="centered")

# 2. Inyección de CSS Minimalista (Ocultar basura visual)
st.markdown("""
    <style>
        /* Ocultar el menú superior y el pie de página de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Darle un respiro al contenido superior */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Estilo sutil para los títulos */
        h1, h2, h3 {
            font-weight: 300 !important;
            letter-spacing: -0.5px;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Configuración de seguridad
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

extensiones = {
    "Python": "py", "Java": "java", "C#": "cs",
    "JavaScript": "js", "Go": "go"
}

# 4. Cabecera Minimalista
try:
    # Mostramos el logo centrado y pequeño
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.image(Image.open('icono_corebridge_ai.png'), use_column_width=True)
except:
    st.markdown("<h1 style='text-align: center;'>CoreBridge AI</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray; font-size: 1.1rem; margin-bottom: 2rem;'>Plataforma Inteligente de Modernización de Código Core</p>", unsafe_allow_html=True)

# 5. Interfaz Intuitiva (El usuario sabe exactamente qué hacer)
st.markdown("### 1. Sube tu sistema legado")
archivo_subido = st.file_uploader("Formatos soportados: .cob, .txt, .cbl, .f90", type=["cob", "txt", "cbl", "f90"], label_visibility="collapsed")

# Escondemos el pegado manual para mantener el minimalismo
with st.expander("⌨️ Opcional: Introducir código de forma manual"):
    codigo_manual = st.text_area("Pega tu código aquí:", height=150, label_visibility="collapsed")

st.markdown("### 2. Configura la modernización")
lenguaje_destino = st.selectbox(
    "Lenguaje de destino:",
    ("Python", "Java", "C#", "JavaScript", "Go")
)

st.write("") # Espacio en blanco

# 6. Lógica de procesamiento
# Usamos un contenedor para centrar el botón de acción
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    ejecutar = st.button("🚀 Ejecutar Migración", use_container_width=True)

if ejecutar:
    codigo_a_traducir = ""
    if archivo_subido is not None:
        codigo_a_traducir = archivo_subido.read().decode("utf-8")
    elif codigo_manual:
        codigo_a_traducir = codigo_manual
        
    if codigo_a_traducir: 
        st.divider() # Línea elegante
        
        with st.spinner("Procesando arquitectura a través de CoreBridge AI..."):
            try:
                model = genai.GenerativeModel('gemini-2.5-flash')
                instruccion = f"""
                Eres un Arquitecto de Software Experto de CoreBridge AI. 
                Traduce y reescribe completamente este código a {lenguaje_destino} aplicando mejores prácticas, seguridad y patrones modernos.
                Añade comentarios en español en el código.
                Al final, da una breve explicación técnica corporativa.
                Código: {codigo_a_traducir}
                """
                
                respuesta = model.generate_content(instruccion)
                resultado_final = respuesta.text
                
                st.success("Migración completada con éxito.")
                st.code(resultado_final, language=lenguaje_destino.lower())
                
                nombre_archivo = f"migracion_corebridge.{extensiones[lenguaje_destino]}"
                
                col_dl1, col_dl2, col_dl3 = st.columns([1, 2, 1])
                with col_dl2:
                    st.download_button(
                        label="📥 Descargar Archivo Modernizado",
                        data=resultado_final,
                        file_name=nombre_archivo,
                        mime="text/plain",
                        use_container_width=True
                    )
                
            except Exception as e:
                st.error(f"Error de conexión con el núcleo de IA: {e}")
    else:
        st.warning("⚠️ Debes subir un archivo o introducir código manual antes de continuar.")
