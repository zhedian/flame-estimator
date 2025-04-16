import streamlit as st
from core.flame_temperature import estimate_flame_temperature

st.title("Flame Temperature Estimator")

fuel = st.text_input("Fuel (e.g., CH4, C2H6)", "CH4")
oxidizer = st.text_input("Oxidizer (e.g., O2, Air)", "O2")
phi = st.slider("Equivalence Ratio (Φ)", 0.5, 2.0, 1.0, 0.05)

if st.button("Estimate Flame Temperature"):
    try:
        T_ad = estimate_flame_temperature(fuel, oxidizer, phi)
        st.success(f"Adiabatic Flame Temperature: {T_ad:.2f} K")
    except Exception as e:
        st.error(f"Error: {e}")
