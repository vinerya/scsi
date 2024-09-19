# Satellite Constellation Spatial Index (SCSI)

SCSI is a Python package for efficient indexing, querying, and management of geospatial data on spherical surfaces, inspired by satellite constellations.

## WiP

## Features

- Spherical tessellation using hierarchical grids.
- Efficient spatial queries (point, range, nearest neighbor).
- Continuous scalar field representation with conservation laws.
- Suitable for applications in GIS, meteorology, environmental science, and more.

## Visualization

You can visualize the scalar field using the built-in visualization functions.

```python
from scsi.grid import Grid
from scsi.field import Field
from scsi.visualization import plot_scalar_field

# Initialize the grid
grid = Grid(levels=4)  # Increase levels for higher resolution

# Initialize the field with an initial value function
def initial_temperature(coords):
    # Example: Set temperature based on latitude (simple model)
    latitude, longitude = coords
    return 30 - abs(latitude)  # Hotter at the equator

field = Field(grid)
field.initialize_field(initial_temperature)

# Visualize the initial scalar field
plot_scalar_field(grid, title='Initial Temperature Distribution')

# Simulate influence propagation
time_step = 0.1
diffusion_coefficient = 0.05
for _ in range(10):  # Simulate over 10 time steps
    field.propagate_influence(time_step, diffusion_coefficient)

# Visualize the scalar field after propagation
plot_scalar_field(grid, title='Temperature Distribution After Propagation')
