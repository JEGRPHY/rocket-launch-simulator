import streamlit as st
from simulation import simulate_rocket
import plotly.graph_objects as go

# App Header
st.title("Rocket Launch Simulation")
st.markdown("### Simulate and visualize a rocket launch in 3D!")

# Input Parameters
st.sidebar.header("Rocket Parameters")
thrust = st.sidebar.number_input("Thrust (N)", 100000, 500000, step=5000, value=300000)
rocket_mass = st.sidebar.number_input("Rocket Mass (kg)", 5000, 50000, step=1000, value=20000)
fuel_mass = st.sidebar.number_input("Fuel Mass (kg)", 500, 20000, step=500, value=10000)
payload_mass = st.sidebar.number_input("Payload Mass (kg)", 100, 5000, step=100, value=2000)
drag_coeff = st.sidebar.slider("Drag Coefficient", 0.1, 1.0, step=0.1, value=0.5)
area = st.sidebar.number_input("Cross-Sectional Area (m^2)", 1, 50, step=1, value=10)
burn_rate = st.sidebar.number_input("Fuel Burn Rate (kg/s)", 10, 500, step=10, value=50)

# Simulate Rocket
if st.button("Launch Rocket!"):
    mass = {'rocket': rocket_mass, 'fuel': fuel_mass, 'payload': payload_mass}
    results = simulate_rocket(thrust, mass, drag_coeff, area, burn_rate)
    
    # Visualization
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(
        x=results['time'], 
        y=results['altitude'], 
        z=results['velocity'],
        mode='lines',
        name='Rocket Trajectory'
    ))
    fig.update_layout(
        title='Rocket Launch Simulation',
        scene=dict(
            xaxis_title='Time (s)',
            yaxis_title='Altitude (m)',
            zaxis_title='Velocity (m/s)',
        )
    )
    st.plotly_chart(fig)

import numpy as np

def create_earth():
    # Create a spherical grid for Earth
    phi = np.linspace(0, np.pi, 50)  # Latitude
    theta = np.linspace(0, 2 * np.pi, 50)  # Longitude
    phi, theta = np.meshgrid(phi, theta)
    
    # Earth's radius
    r = 6371  # Approximate radius in km

    # Convert spherical coordinates to Cartesian for 3D surface
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    return x, y, z

def visualize_trajectory(results):
    from plotly.graph_objects import Figure, Scatter3d, Surface

    # Create Earth Model
    x, y, z = create_earth()

    # Plot Earth
    fig = Figure()
    fig.add_trace(Surface(
        x=x, y=y, z=z,
        colorscale="Earth",  # Earth-like texture
        opacity=0.8,
        showscale=False,
    ))

    # Plot Rocket Trajectory
    fig.add_trace(Scatter3d(
        x=results['time'],  # Rocket moving over time
        y=results['altitude'],  # Altitude
        z=results['velocity'],  # Velocity as a proxy for z-axis motion
        mode='lines+markers',
        marker=dict(size=5, color='red'),
        line=dict(color='red', width=2),
        name='Rocket Trajectory'
    ))

    # Set layout
    fig.update_layout(
        scene=dict(
            xaxis_title='Time (s)',
            yaxis_title='Altitude (km)',
            zaxis_title='Velocity (m/s)',
            aspectmode='data',
        ),
        title="3D Rocket Launch Simulation",
    )

    # Display with Streamlit
    st.plotly_chart(fig)


