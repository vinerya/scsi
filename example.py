from scsi.grid import Grid
from scsi.field import Field
from scsi.visualization import plot_scalar_field_interactive

# Initialize the grid
grid = Grid(levels=4)

# Initialize the field with an initial value function
def initial_temperature(coords):
    latitude, longitude = coords
    return 30 - abs(latitude)

field = Field(grid)
field.initialize_field(initial_temperature)

# Visualize the initial scalar field interactively
plot_scalar_field_interactive(grid, title='Initial Temperature Distribution')

# Simulate influence propagation
time_step = 0.1
diffusion_coefficient = 0.05
for _ in range(10):
    field.propagate_influence(time_step, diffusion_coefficient)

# Visualize the scalar field after propagation interactively
plot_scalar_field_interactive(grid, title='Temperature Distribution After Propagation')
