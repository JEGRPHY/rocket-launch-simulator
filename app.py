import streamlit as st

# Title
st.title("🚀 Rocket Launch Simulation")
st.write("Configure the rocket parameters and watch it launch into space!")

# Sidebar for Input Parameters
st.sidebar.header("Rocket Parameters")
rocket_weight = st.sidebar.slider("Rocket Weight (kg)", 500, 5000, 100)
thrust = st.sidebar.slider("Thrust (kN)", 100, 5000, 100)
launch_angle = st.sidebar.slider("Launch Angle (°)", 0, 90, 1)

# Displaying Input Parameters
st.write("### Configured Parameters:")
st.write(f"Rocket Weight: {rocket_weight} kg")
st.write(f"Thrust: {thrust} kN")
st.write(f"Launch Angle: {launch_angle}°")

