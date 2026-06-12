"""Tests for AHP implementation (ahp.py)."""

import numpy as np
import pytest
from ahp import ahp_weights, ahp_hierarchy, sensitivity_check

# Known-good 3x3 judgment matrix (Saaty scale)
JUDGMENT_3x3 = np.array([
    [1,   2,   4],
    [1/2, 1,   3],
    [1/4, 1/3, 1]
])
# Expected (geometric mean method):
# w ≈ [0.5584, 0.3196, 0.1220], λ_max ≈ 3.0183


class TestAhpWeights:
    def test_output_shape_and_sum(self):
        w, lam, ci, cr, ok = ahp_weights(JUDGMENT_3x3)
        assert np.allclose(np.sum(w), 1.0, atol=1e-6)
        assert w.shape == (3,)

    def test_known_values_geometric(self):
        w, lam, ci, cr, ok = ahp_weights(JUDGMENT_3x3, method='geometric')
        expected_w = np.array([0.5584, 0.3196, 0.1220])
        assert np.allclose(w, expected_w, atol=1e-3)
        assert np.isclose(lam, 3.0183, atol=1e-2)
        assert cr < 0.10
        assert ok

    def test_three_methods_similar(self):
        w_geo, *_ = ahp_weights(JUDGMENT_3x3, method='geometric')
        w_ari, *_ = ahp_weights(JUDGMENT_3x3, method='arithmetic')
        w_eig, *_ = ahp_weights(JUDGMENT_3x3, method='eigenvalue')
        assert np.allclose(w_geo, w_ari, atol=0.05)
        assert np.allclose(w_geo, w_eig, atol=0.05)

    def test_2x2_always_consistent(self):
        A = np.array([[1, 3], [1/3, 1]])
        w, lam, ci, cr, ok = ahp_weights(A)
        assert ok
        assert np.isclose(cr, 0)

    def test_inconsistent_matrix_fails_cr(self):
        rng = np.random.default_rng(42)
        A = rng.uniform(1, 9, (6, 6))
        for i in range(6):
            for j in range(i+1, 6):
                A[j, i] = 1 / A[i, j]
        np.fill_diagonal(A, 1)
        w, lam, ci, cr, ok = ahp_weights(A)
        assert cr > 0

    def test_invalid_non_square(self):
        A = np.array([[1, 2, 4], [1/2, 1, 3]])
        with pytest.raises(ValueError, match="方阵"):
            ahp_weights(A)

    def test_invalid_negative(self):
        A = np.array([[1, -2], [-1/2, 1]])
        with pytest.raises(ValueError, match="为正"):
            ahp_weights(A)

    def test_invalid_diagonal(self):
        A = np.array([[2, 2], [1/2, 1]])
        with pytest.raises(ValueError, match="对角线"):
            ahp_weights(A)

    def test_large_matrix_runs(self):
        n = 10
        A = np.ones((n, n))
        for i in range(n):
            for j in range(i+1, n):
                val = 1 + (i + j) % 8
                A[i, j] = val
                A[j, i] = 1/val
        w, lam, ci, cr, ok = ahp_weights(A)
        assert np.allclose(np.sum(w), 1.0)

    def test_scalar_returns(self):
        w, lam, ci, cr, ok = ahp_weights(JUDGMENT_3x3)
        assert np.isscalar(lam)
        assert np.isscalar(ci)
        assert np.isscalar(cr)


class TestAhpHierarchy:
    def test_hierarchy_weights_sum_to_one(self):
        criteria = np.array([
            [1,   3,   5],
            [1/3, 1,   3],
            [1/5, 1/3, 1]
        ])
        sub1 = np.array([
            [1,   2,   4,   6],
            [1/2, 1,   3,   5],
            [1/4, 1/3, 1,   3],
            [1/6, 1/5, 1/3, 1]
        ])
        sub2 = np.array([
            [1,   1/3, 2,   4],
            [3,   1,   4,   6],
            [1/2, 1/4, 1,   3],
            [1/4, 1/6, 1/3, 1]
        ])
        sub3 = np.array([
            [1,   5,   3,   7],
            [1/5, 1,   1/3, 2],
            [1/3, 3,   1,   5],
            [1/7, 1/2, 1/5, 1]
        ])
        total_w = ahp_hierarchy(criteria, [sub1, sub2, sub3])
        assert total_w.shape == (4,)
        assert np.allclose(np.sum(total_w), 1.0, atol=1e-6)

    def test_all_weights_positive(self):
        criteria = np.array([[1, 2, 3], [1/2, 1, 2], [1/3, 1/2, 1]])
        subs = [np.array([[1, 2], [1/2, 1]]) for _ in range(3)]
        total_w = ahp_hierarchy(criteria, subs)
        assert np.all(total_w > 0)


class TestSensitivityCheck:
    def test_returns_correct_count(self):
        results = sensitivity_check(JUDGMENT_3x3, (0, 1))
        assert len(results) == 5

    def test_contains_expected_keys(self):
        results = sensitivity_check(JUDGMENT_3x3, (0, 1))
        for r in results:
            assert 'perturbation' in r
            assert 'CR' in r
            assert 'consistent' in r
