from .grid import Grid

class Field:
    def __init__(self, grid):
        """
        Initialize the field with a grid.

        :param grid: Grid object.
        """
        self.grid = grid

    def initialize_field(self, initial_value_function):
        """
        Initialize the scalar field across the grid.

        :param initial_value_function: Function to compute initial values.
        """
        for node_id, node in self.grid.nodes.items():
            node.scalar_value = initial_value_function(node.coordinates)

    def propagate_influence(self, time_step, diffusion_coefficient):
        """
        Update the scalar field values based on diffusion.

        :param time_step: Time step for the simulation.
        :param diffusion_coefficient: Diffusion coefficient.
        """
        new_values = {}
        for node_id, node in self.grid.nodes.items():
            total_flux = 0.0
            for adj_node in node.adjacent_nodes:
                flux = diffusion_coefficient * (adj_node.scalar_value - node.scalar_value)
                total_flux += flux
            new_value = node.scalar_value + total_flux * time_step
            new_values[node_id] = new_value

        # Update scalar values while conserving energy
        total_energy_before = sum(node.scalar_value for node in self.grid.nodes.values())
        for node_id, value in new_values.items():
            self.grid.nodes[node_id].scalar_value = value
        total_energy_after = sum(node.scalar_value for node in self.grid.nodes.values())

        # Adjust for conservation of energy
        energy_difference = total_energy_before - total_energy_after
        adjustment = energy_difference / len(self.grid.nodes)
        for node in self.grid.nodes.values():
            node.scalar_value += adjustment
