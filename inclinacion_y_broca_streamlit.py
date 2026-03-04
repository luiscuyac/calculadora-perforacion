import streamlit as st
import math


# Cambio en la pestaña del navegador
st.set_page_config(page_title="Calculadora Perforación", page_icon="📐")


# --- FUNCIONES DE CÁLCULO ---
def inclinacion(grosor, desviacion):
    inclinar = math.atan2(desviacion, grosor)
    grados = round((math.degrees(inclinar)), 2)
    return grados


def longitud_broca(grosor, desviacion):
    agujero = round((math.hypot(grosor, desviacion)), 2)
    return agujero


# --- INTERFAZ PROFESIONAL ---
st.title("🔌 Mi Calculadora de Perforación")

# Entradas de texto como pediste
g_input = st.text_input("Ingresa el grosor de la pared (cm):", value="", placeholder="Escribe aquí el grosor...")
d_input = st.text_input("Ingresa cuánto baja, sube o lateral (cm):", value="", placeholder="Escribe aquí la desviación...")

# Botón para ejecutar la acción
if st.button("Calcular"):
    # Verificamos que no estén vacíos
    if g_input and d_input:
        try:
            # Limpiamos comas y convertimos a número
            grosor = float(g_input.replace(",", "."))
            desviacion = float(d_input.replace(",", "."))
            
            if grosor > 0:
                # Ejecutamos la lógica técnica
                taladrar = inclinacion(grosor, desviacion)
                broca = longitud_broca(grosor, desviacion)

                # Mostramos los resultados
                st.divider()
                st.success(f"### Ángulo de inclinación: {taladrar}°")
                st.success(f"### Longitud del agujero: {broca} cm")
                
                # Cálculo de brocas según tipo de anclaje
                st.info(f"Broca: {broca:.2f} cm de longitud de trabajo o superior.")
                st.warning("Nota: Es importante mantener la inclinación del taladro en la ejecución del agujero.")
            else:
                st.error("❌ El grosor debe ser mayor a 0.")
                
        except ValueError:
            st.error("❌ Por favor, ingresa solo números válidos (puedes usar coma o punto).")
    else:
        st.warning("⚠️ Debes rellenar ambos campos para calcular.")

st.caption("Gracias por usar la calculadora técnica de perforación.")
st.caption("Autor: Luis Eduardo Cuya Carranza.")