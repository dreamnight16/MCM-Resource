"""Tests for integer programming (integer_programming.py)."""

import numpy as np
import pytest


@pytest.mark.optional
class TestAssignment:
    def test_assignment_solves(self):
        from integer_programming import solve_assignment

        cost = np.array([
            [4, 8, 7, 9],
            [7, 6, 9, 8],
            [6, 5, 8, 7],
            [9, 7, 6, 5],
        ])
        result = solve_assignment(cost)
        assert 'assignment' in result
        assert 'total_cost' in result
        assert len(result['assignment']) == 4

    def test_assignment_total_cost_reasonable(self):
        from integer_programming import solve_assignment

        cost = np.array([
            [4, 8],
            [7, 6],
        ])
        result = solve_assignment(cost)
        assert result['total_cost'] > 0
        # Optimal: (0,0)=4 + (1,1)=6 → total=10
        assert np.isclose(result['total_cost'], 10)
