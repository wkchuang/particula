"""
Tests for BrownianCoagulationStrategy.
"""

import unittest
import numpy as np
from particula.particles.representation import ParticleRepresentation
from particula.dynamics.coagulation.strategy.brownian_coagulation_strategy import BrownianCoagulationStrategy

class TestBrownianCoagulationStrategy(unittest.TestCase):
    def setUp(self):
        # Setup a particle representation for testing
        self.particle = ParticleRepresentation(
            distribution=np.array([1.0, 2.0, 3.0]),
            density=1.0,
            concentration=np.array([10, 20, 30]),
            charge=1.0
        )
        self.strategy = BrownianCoagulationStrategy(distribution_type="discrete")
        self.temperature = 298.15  # Kelvin
        self.pressure = 101325  # Pascal

    def test_kernel(self):
        # Test the kernel calculation
        kernel = self.strategy.kernel(
            particle=self.particle,
            temperature=self.temperature,
            pressure=self.pressure
        )
        self.assertIsInstance(kernel, np.ndarray)

    def test_step(self):
        # Test the step method
        initial_concentration = self.particle.get_concentration().copy()
        self.strategy.step(
            particle=self.particle,
            temperature=self.temperature,
            pressure=self.pressure,
            time_step=1.0
        )
        updated_concentration = self.particle.get_concentration()
        self.assertFalse(np.array_equal(initial_concentration, updated_concentration))

if __name__ == '__main__':
    unittest.main()
