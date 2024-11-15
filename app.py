import streamlit as st
from physics import simulate_trajectory
from visualization import plot_trajectory
from streamlit_lottie import st_lottie
import json

# Load Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_rocket = load_lottiefile("assets/rocket_launch.json")

# Title
st.title("🚀 Rocket Launch Simulation")

# Sidebar
st.sidebar.header("Rocket Parameters")
rocket_weight = st.sidebar.slider("Rocket Weight (kg)", 500, 5000, 100)
thrust = st.sidebar.slider("Thrust (kN)", 100, 5000, 100)
launch_angle = st.sidebar.slider("Launch Angle (°)", 0, 90, 1)

# Show parameters
st.write(f"Rocket Weight: {rocket_weight} kg")
st.write(f"Thrust: {thrust} kN")
st.write(f"Launch Angle: {launch_angle}°")

# Launch button
if st.button("Launch Rocket"):
    st_lottie(lottie_rocket, height=300)
    trajectory = simulate_trajectory(rocket_weight, thrust, launch_angle)
    fig = plot_trajectory(trajectory)
    st.plotly_chart(fig)
