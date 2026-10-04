import streamlit as st
import random
import time

# 1. Configuración de la página
st.set_page_config(page_title="Quiz de Machine Learning", page_icon="🤖")

# 2. Banco de 20 Preguntas (Nivel Básico)
# Formato: "Pregunta": ["Opción Correcta", "Opción Incorrecta 1", "Opción Incorrecta 2", "Opción Incorrecta 3"]
banco_preguntas = {
    "¿Qué es el Machine Learning?": [
        "Una rama de la IA que permite a las máquinas aprender de datos sin ser programadas explícitamente.",
        "Un lenguaje de programación orientado a objetos.",
        "Un tipo de hardware especializado en cálculos matemáticos.",
        "Una base de datos relacional avanzada."
    ],
    "¿Cuál es un ejemplo de aprendizaje supervisado?": [
        "Clasificación de correos como spam o no spam.",
        "Agrupar clientes por similitud de compras.",
        "Un robot que aprende a caminar por ensayo y error.",
        "Reducción de dimensionalidad de datos."
    ],
    "¿Qué es el aprendizaje no supervisado?": [
        "El modelo busca patrones ocultos en datos sin etiquetas.",
        "El modelo recibe datos etiquetados para predecir.",
        "El modelo recibe recompensas por sus acciones.",
        "El modelo necesita un supervisor humano constante."
    ],
    "¿Qué es una variable objetivo (target)?": [
        "La variable que el modelo intenta predecir.",
        "La variable que usamos para entrenar al modelo.",
        "El error del modelo.",
        "El nombre del algoritmo."
    ],
    "¿Qué es el overfitting (sobreajuste)?": [
        "Cuando el modelo memoriza los datos de entrenamiento y no generaliza bien.",
        "Cuando el modelo es demasiado simple y no aprende.",
        "Cuando el modelo tarda mucho en entrenar.",
        "Cuando faltan datos en el dataset."
    ],
    "¿Qué es el underfitting (subajuste)?": [
        "Cuando el modelo es demasiado simple y no captura la tendencia de los datos.",
        "Cuando el modelo memoriza los datos de entrenamiento.",
        "Cuando el modelo tiene demasiados parámetros.",
        "Cuando el modelo predice perfectamente."
    ],
    "¿Qué tipo de aprendizaje se basa en recompensas y castigos?": [
        "Aprendizaje por Refuerzo (Reinforcement Learning).",
        "Aprendizaje Supervisado.",
        "Aprendizaje No Supervisado.",
        "Aprendizaje Semisupervisado."
    ],
    "¿Qué es un dataset de entrenamiento?": [
        "Los datos que usa el modelo para aprender los patrones.",
        "Los datos que usa el modelo para evaluar su rendimiento final.",
        "Los datos que se descartan.",
        "Los datos que el modelo intenta predecir."
    ],
    "¿Qué es un dataset de prueba (test)?": [
        "Los datos que se usan para evaluar el rendimiento final del modelo.",
        "Los datos que usa el modelo para aprender.",
        "Los datos que se usan para ajustar los hiperparámetros.",
        "Los datos que se usan para limpiar el ruido."
    ],
    "¿Qué es la regresión en Machine Learning?": [
        "Predecir un valor numérico continuo.",
        "Predecir una categoría o clase.",
        "Agrupar datos similares.",
        "Reducir la cantidad de variables."
    ],
    "¿Qué es la clasificación en Machine Learning?": [
        "Predecir una categoría o clase discreta.",
        "Predecir un valor numérico continuo.",
        "Agrupar datos similares.",
        "Reducir la cantidad de variables."
    ],
    "¿Qué es el clustering?": [
        "Una técnica no supervisada para agrupar datos similares.",
        "Una técnica supervisada para predecir números.",
        "Una técnica para limpiar datos nulos.",
        "Una técnica para aumentar la resolución de imágenes."
    ],
    "¿Qué es una feature (característica)?": [
        "Una variable de entrada que describe los datos.",
        "La variable que queremos predecir.",
        "El resultado del modelo.",
        "El error del modelo."
    ],
    "¿Qué es un modelo en Machine Learning?": [
        "Una representación matemática que aprende patrones de los datos.",
        "Un programa de computadora tradicional.",
        "Una base de datos.",
        "Un tipo de servidor."
    ],
    "¿Qué es el sesgo (bias) en un modelo?": [
        "Un error sistemático debido a suposiciones incorrectas en el algoritmo.",
        "La variación del modelo ante pequeños cambios en los datos.",
        "La cantidad de datos que tiene el modelo.",
        "La velocidad de entrenamiento."
    ],
    "¿Qué es la varianza en un modelo?": [
        "La sensibilidad del modelo a pequeñas fluctuaciones en el conjunto de entrenamiento.",
        "El error sistemático del modelo.",
        "La cantidad de características.",
        "El tiempo que tarda en predecir."
    ],
    "¿Qué es la validación cruzada (Cross-Validation)?": [
        "Una técnica para evaluar el modelo dividiendo los datos en múltiples pliegues.",
        "Una técnica para aumentar los datos.",
        "Una técnica para limpiar datos.",
        "Una técnica para elegir el mejor algoritmo."
    ],
    "¿Qué es la Ingeniería de Características (Feature Engineering)?": [
        "El proceso de crear nuevas variables a partir de las existentes para mejorar el modelo.",
        "El proceso de eliminar variables.",
        "El proceso de recolectar datos.",
        "El proceso de entrenar el modelo."
    ],
    "¿Qué librería de Python es fundamental para Machine Learning?": [
        "Scikit-Learn",
        "Django",
        "Flask",
        "Requests"
    ],
    "¿Qué es el descenso del gradiente (Gradient Descent)?": [
        "Un algoritmo de optimización para minimizar la función de error.",
        "Un algoritmo para clasificar datos.",
        "Un algoritmo para agrupar datos.",
        "Un algoritmo para limpiar datos."
    ]
}

# 3. Inicializar el estado de la sesión
if 'preguntas_actuales' not in st.session_state:
    # Seleccionar 5 preguntas aleatorias del banco de 20
    preguntas_seleccionadas = random.sample(list(banco_preguntas.keys()), 5)
    st.session_state.preguntas_actuales = preguntas_seleccionadas
    
    # Preparar las opciones desordenadas para cada pregunta
    opciones_desordenadas = {}
    for preg in preguntas_seleccionadas:
        opciones = banco_preguntas[preg].copy()
        random.shuffle(opciones) # Mezclar opciones
        opciones_desordenadas[preg] = opciones
        
    st.session_state.opciones = opciones_desordenadas
    st.session_state.respuestas_usuario = {}

# 4. Interfaz de Usuario
st.title("🤖 Quiz Básico de Machine Learning")
st.write("Responde las siguientes 5 preguntas. ¡Si aciertas todas, tendrás una sorpresa!")

# Formulario para las preguntas
with st.form("quiz_form"):
    for i, preg in enumerate(st.session_state.preguntas_actuales):
        st.subheader(f"Pregunta {i+1}: {preg}")
        # Radio buttons para seleccionar la alternativa
        st.session_state.respuestas_usuario[preg] = st.radio(
            "Selecciona una opción:",
            st.session_state.opciones[preg],
            key=f"preg_{i}"
        )
        st.markdown("---")
    
    # Botón para enviar respuestas
    boton_enviar = st.form_submit_button("Enviar Respuestas")

# 5. Lógica de Evaluación
if boton_enviar:
    puntaje = 0
    respuestas_correctas = 0
    
    for preg in st.session_state.preguntas_actuales:
        respuesta_usuario = st.session_state.respuestas_usuario[preg]
        respuesta_correcta = banco_preguntas[preg][0] # La primera opción en el banco original es la correcta
        
        if respuesta_usuario == respuesta_correcta:
            respuestas_correctas += 1
            
    # Mostrar resultados
    if respuestas_correctas == 5:
        st.success(f"¡Excelente! Has acertado todas las preguntas ({respuestas_correctas}/5). ¡Eres un experto en ML!")
        st.balloons() # Animación de globos
        st.snow() # Animación de nieve (opcional, puedes quitar esta línea si quieres)
    elif respuestas_correctas >= 3:
        st.warning(f"¡Buen trabajo! Acertaste {respuestas_correctas} de 5. Sigue estudiando.")
    else:
        st.error(f"Acertaste {respuestas_correctas} de 5. ¡No te desanimes, repasa los conceptos y vuelve a intentarlo!")
        
    # Botón para reiniciar el quiz (recarga la página y genera nuevas preguntas)
    if st.button("Intentar de nuevo con otras preguntas"):
        # Limpiar el estado para forzar una nueva selección aleatoria
        del st.session_state.preguntas_actuales
        del st.session_state.opciones
        del st.session_state.respuestas_usuario
        st.rerun()
