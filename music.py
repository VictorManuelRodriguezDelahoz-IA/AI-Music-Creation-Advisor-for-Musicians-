import streamlit as st
import google.generativeai as genai
import json

# Reemplaza con tu API Key
api_key = ""  # Reemplaza con tu API key real
genai.configure(api_key=api_key)

generation_config = genai.GenerationConfig(
    temperature=0.7,
    top_p=0.95,
    max_output_tokens=1024,
)

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",  # Reemplaza con el ID de tu endpoint si usas un modelo fine-tuneado
  generation_config=generation_config,
)

# Título de la aplicación
st.title("Arreglista IA")

# Obtener la entrada del usuario
user_input = st.text_input("Introduce tu texto aquí:")

# Guardar la entrada del usuario en una variable
texto_usuario = user_input

input = {"prompt":"Eres un asistente de IA especializado en la generación de arreglos musicales, instrumentales, bandas sonoras , canciones. **Formato de respuesta:*** **Consejo** Orientacion sobre como crear las cosas que te pida el usuario.* **Instrucciones** Instrucciones de como crear eso que te pide el usuario.",
         "user_input":texto_usuario}

input_str = json.dumps(input)

# Mostrar la entrada del usuario y procesarla solo si hay entrada
if st.button("Generar:"):
    response = model.generate_content(
    input_str)
    st.write("Mira:", response.text)
