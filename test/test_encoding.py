"""
 This module contains a set of unit tests dedicated to verify if the creation of quantum circuit
 in the mottonen module work properly.
"""
import unittest
from unittest import TestCase
from random import randint
import numpy as np
from qiskit import execute, Aer
from qclib.encoding import mottonen_quantum_circuit, _resize_feature_vectors


class TestCircuitCreation(TestCase):
    """
    Class dedicated to the implementation of the unittests for the creation of the quantum circuit.
    """

    def test_mottonen_initialization(self):
        """
        Load a 3 qubits state
        """
        input_vector = [-np.sqrt(0.03),
                        np.sqrt(0.02),
                        np.sqrt(0.02),
                        np.sqrt(0.03),
                        np.sqrt(0.1),
                        np.sqrt(0.4),
                        -np.sqrt(0.3),
                        -np.sqrt(0.1)]
        quantum_circuit = mottonen_quantum_circuit(input_vector)
        backend_sim = Aer.backends('statevector_simulator')[0]
        job = execute(quantum_circuit, backend_sim)
        result = job.result()

        out_state = result.get_statevector(quantum_circuit)

        for exp_amplitude, out_amplitude in zip(input_vector, out_state):
            self.assertTrue(np.abs(exp_amplitude - out_amplitude) < 10 ** (-5))

    def test_mottonen_initialization_basis_state(self):
        """
        Load a basis state
        """
        input_vector = [0,
                        0,
                        0,
                        0,
                        0,
                        1,
                        0,
                        0]
        quantum_circuit = mottonen_quantum_circuit(input_vector)
        backend_sim = Aer.backends('statevector_simulator')[0]
        job = execute(quantum_circuit, backend_sim)
        result = job.result()

        out_state = result.get_statevector(quantum_circuit)

        for exp_amplitude, out_amplitude in zip(input_vector, out_state):
            self.assertTrue(np.abs(exp_amplitude - out_amplitude) < 10 ** (-5))

    
if __name__ == "__main__":
    unittest.main()