"""Tests for TOPSIS implementation (topsis.py)."""

import numpy as np
import pytest
from topsis import topsis, topsis_sensitivity

TEST_DATA = np.array([
    [8.0, 7.0, 2.0, 4.5, 4.0],
    [6.0, 8.0, 3.0, 5.2, 3.5],
    [9.0, 6.0, 1.5, 4.8, 5.5],
    [7.0, 9.0, 2.5, 3.5, 2.0],
])


class TestTopsis:
    def test_output_shapes(self):
        scores, ranking, rank_order, details = topsis(TEST_DATA)
        assert scores.shape == (4,)
        assert ranking.shape == (4,)
        assert rank_order.shape == (4,)

    def test_scores_in_01_range(self):
        scores, _, _, _ = topsis(TEST_DATA)
        assert np.all(scores >= 0)
        assert np.all(scores <= 1)

    def test_ranking_is_permutation(self):
        _, ranking, _, _ = topsis(TEST_DATA)
        assert sorted(ranking) == [1, 2, 3, 4]

    def test_rank_order_is_unique_indices(self):
        _, _, rank_order, _ = topsis(TEST_DATA)
        assert len(set(rank_order)) == 4

    def test_identical_rows_same_score(self):
        data = np.ones((3, 4))
        scores, _, _, _ = topsis(data)
        assert np.allclose(scores, scores[0])

    def test_single_alternative_gives_zero(self):
        """Single alternative: D_plus = D_minus = 0, so score = 0."""
        data = np.array([[1.0, 2.0, 3.0]])
        scores, _, _, _ = topsis(data)
        assert np.isclose(scores[0], 0.0)

    def test_cost_cols_reverse_ranking(self):
        data = np.array([[10, 100], [20, 80], [30, 60]])
        scores_benefit, _, _, _ = topsis(data, benefit_cols=[0, 1])
        scores_cost, _, _, _ = topsis(data, benefit_cols=[0], cost_cols=[1])
        assert not np.allclose(scores_benefit, scores_cost)

    def test_target_col_handling(self):
        data = np.array([[5, 10], [5, 20], [5, 30]])
        scores, _, _, _ = topsis(data, benefit_cols=[0],
                                 target_cols=[1], target_values=[15])
        assert len(scores) == 3

    def test_interval_col_handling(self):
        scores, _, _, _ = topsis(TEST_DATA,
                                 benefit_cols=[0, 1],
                                 interval_cols=[4],
                                 interval_bounds=[(3, 5)])
        assert len(scores) == 4

    def test_custom_weights_change_result(self):
        n = TEST_DATA.shape[1]
        scores_eq, _, _, _ = topsis(TEST_DATA)
        custom_w = np.array([0.5] + [0.5/(n-1)]*(n-1))
        scores_custom, _, _, _ = topsis(TEST_DATA, weights=custom_w)
        assert not np.allclose(scores_eq, scores_custom)


class TestTopsisDetails:
    def test_details_contains_intermediate_matrices(self):
        _, _, _, details = topsis(TEST_DATA)
        for key in ['X_positive', 'Z_normalized', 'Z_weighted',
                     'Z_plus', 'Z_minus', 'D_plus', 'D_minus']:
            assert key in details, f"Missing key: {key}"

    def test_normalized_columns_have_unit_norm(self):
        _, _, _, details = topsis(TEST_DATA)
        Z = details['Z_normalized']
        col_norms = np.sqrt(np.sum(Z ** 2, axis=0))
        assert np.allclose(col_norms, 1.0, atol=1e-6)


class TestTopsisSensitivity:
    def test_returns_correct_length(self):
        n = TEST_DATA.shape[1]
        weights = np.ones(n) / n
        results = topsis_sensitivity(TEST_DATA, weights, 0, [-0.2, 0, 0.2])
        assert len(results) == 3

    def test_each_result_has_scores(self):
        n = TEST_DATA.shape[1]
        weights = np.ones(n) / n
        results = topsis_sensitivity(TEST_DATA, weights, 0, [-0.1, 0.1])
        for r in results:
            assert 'delta' in r
            assert 'scores' in r
            assert r['scores'].shape == (4,)
