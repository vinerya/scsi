# scsi/visualization.py

import plotly.graph_objects as go
import numpy as np

def plot_scalar_field_interactive(grid, title='Scalar Field Visualization'):
    """
    Interactive visualization of the scalar field on a global map.

    :param grid: Grid object containing nodes with scalar values.
    :param title: Title of the plot.
    """
    lats = [node.coordinates[0] for node in grid.nodes.values()]
    lons = [node.coordinates[1] for node in grid.nodes.values()]
    values = [node.scalar_value for node in grid.nodes.values()]

    fig = go.Figure(go.Scattergeo(
        lon = lons,
        lat = lats,
        text = values,
        marker = dict(
            color = values,
            colorscale = 'RdBu',
            reversescale = True,
            colorbar = dict(title = 'Scalar Value'),
            size = 4,
            opacity = 0.8,
        )
    ))

    fig.update_layout(
        title = title,
        geo = dict(
            projection = dict(type = 'orthographic'),
            showland = True,
            landcolor = 'rgb(243, 243, 243)',
            countrycolor = 'rgb(204, 204, 204)',
        ),
    )

    fig.show()
