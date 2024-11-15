import plotly.graph_objects as go

def plot_trajectory(trajectory):
    x, y = trajectory[:, 0], trajectory[:, 1]

    fig = go.Figure()

    # Rocket trajectory
    fig.add_trace(go.Scatter3d(
        x=x, y=[0]*len(x), z=y,
        mode='lines',
        line=dict(color='red', width=4),
        name='Trajectory'
    ))

    # Launch pad
    fig.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[0],
        mode='markers',
        marker=dict(size=10, color='blue'),
        name='Launch Pad'
    ))

    fig.update_layout(
        title="Rocket Trajectory",
        scene=dict(
            xaxis_title='Distance (m)',
            yaxis_title='Lateral Drift (m)',
            zaxis_title='Altitude (m)',
        )
    )

    return fig
