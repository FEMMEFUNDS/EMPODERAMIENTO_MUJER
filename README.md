
# ♀️ Asistente Educativo de Empoderamiento de la Mujer

Un chatbot educativo para responder preguntas sobre **empoderamiento de la mujer** en la escuela y universidad, con un tono empático e inclusivo.

## 🧱 Archivos
- `app.py`: aplicación Streamlit.
- `requirements.txt`: dependencias para que Streamlit Cloud instale.
- `README.md`: esta guía.

## 🚀 Despliegue en Streamlit Cloud (paso a paso)
1) **Prepara un repositorio en GitHub**
- Inicia sesión en https://github.com y crea un repositorio nuevo (por ejemplo `empoderamiento_mujer`).
- Sube los 3 archivos (`app.py`, `requirements.txt`, `README.md`) usando **Add file → Upload files** y presiona **Commit**.

2) **Crea la app en Streamlit Cloud**
- Ve a https://share.streamlit.io (inicia sesión con tu cuenta).
- Haz clic en **New app**.
- Conecta tu cuenta de GitHub y selecciona el repositorio y la rama (por lo general `main`).
- En **Main file path** escribe `app.py`.
- Presiona **Deploy**.

3) **Configura tus Secrets**
- En tu app de Streamlit Cloud, abre el menú **⋮ -> Settings -> Secrets**.
- Agrega tu clave de OpenAI y (opcional) el nombre del modelo:
  ```
  OPENAI_API_KEY="tu_api_key_de_openai"
  OPENAI_MODEL="gpt-4o-mini"
  ```
- Guarda los secrets y **rerun** la app si es necesario.

4) **Comparte el enlace**
- Streamlit te dará un enlace público del tipo: `https://tu-app.streamlit.app`.
- Compártelo con tus estudiantes y docentes.

## 🛠️ Solución de problemas
- **ModuleNotFoundError: openai** → Revisa que `requirements.txt` esté en el repo y vuelve a desplegar.
- **API key inválida** → Verifica que `OPENAI_API_KEY` esté bien copiada en **Secrets**.
- **Modelo no disponible** → Cambia `OPENAI_MODEL` por otro (ej. `gpt-4o-mini` o `gpt-4o`) en **Secrets** o en el campo de la barra lateral.
- **App no carga** → Abre **Logs** en Streamlit Cloud para ver el error, corrige y re-deploy.

## 🔐 Privacidad
No ingreses datos personales sensibles. Este asistente no reemplaza asesoría profesional (psicológica, legal o médica).
