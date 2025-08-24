
import streamlit as st
import os
from openai import OpenAI

# ---------- Configuración de la app ----------
st.set_page_config(page_title="Asistente de Empoderamiento de la Mujer", page_icon="♀️")

st.title("♀️ Asistente Educativo de Empoderamiento de la Mujer")
st.write("""
Este asistente responde consultas sobre **empoderamiento de la mujer** en el entorno educativo.
Puedes preguntar sobre:
- Liderazgo, igualdad y derechos.
- Consejos prácticos (confianza, participación, negociación).
- Prevención de violencia y recursos de apoyo.

⚠️ Nota: No sustituye orientación profesional (psicológica, legal o médica). 
Si hay riesgo de violencia o acoso, busca apoyo inmediato en docentes, familia o líneas de ayuda locales.
""")

st.markdown("### Ejemplos de preguntas:")
examples = [
    "¿Qué significa empoderamiento de la mujer en la educación?",
    "¿Cómo puedo ganar más confianza para hablar en público?",
    "¿Qué hacer si sufro acoso en la escuela?",
    "¿Cómo fomentar la igualdad de género en mi clase?",
]
for ex in examples:
    st.markdown(f"- *{ex}*")

# ---------- Configurar API Key y modelo ----------
if "OPENAI_API_KEY" not in st.secrets:
    st.error("⚠️ Falta configurar la clave OPENAI_API_KEY en los Secrets de Streamlit.")
    st.stop()

# Setear la API key como variable de entorno para el SDK
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Modelo por defecto; puedes sobreescribirlo en los Secrets con OPENAI_MODEL
default_model = st.secrets.get("OPENAI_MODEL", "gpt-4o-mini")
model = st.sidebar.text_input("Modelo de OpenAI", value=default_model, help="Ej: gpt-4o-mini, gpt-4o, etc.")

st.sidebar.markdown("### Notas de seguridad")
st.sidebar.write(
    "- Respuestas con lenguaje inclusivo y enfoque en derechos.\n"
    "- En consultas de riesgo/violencia: validar, priorizar seguridad y derivar a ayuda local.\n"
    "- No inventar teléfonos ni estadísticas."
)

# ---------- Prompt del asistente ----------
system_prompt = """
Eres una asesora experta en empoderamiento de la mujer en el contexto educativo.
Respondes con empatía, claridad y ejemplos sencillos.
Tu meta es:
- Explicar conceptos (liderazgo, igualdad, derechos, ODS 5).
- Dar consejos prácticos (confianza, participación, negociación, prevención de violencia).
- Usar lenguaje inclusivo y respetuoso.
- Si la pregunta sugiere riesgo (violencia, acoso), valida la situación y recomienda buscar ayuda de docentes, familia o líneas locales de apoyo. 
  Ofrece un plan breve de seguridad de 3–5 pasos cuando corresponda.
No inventes números de teléfono ni datos estadísticos específicos.
"""

# ---------- Lógica del chat ----------
question = st.text_area("✍️ Escribe tu consulta:")

if st.button("Consultar"):
    if question.strip() == "":
        st.warning("Por favor ingresa una pregunta.")
    else:
        try:
            client = OpenAI()  # usa OPENAI_API_KEY desde el entorno
            with st.spinner("Generando respuesta..."):
                resp = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": question},
                    ],
                    temperature=0.5,
                )
            answer = resp.choices[0].message.content
            st.markdown("### 📌 Respuesta")
            st.write(answer)
        except Exception as e:
            st.error(f"Ocurrió un error al consultar el modelo: {e}")
