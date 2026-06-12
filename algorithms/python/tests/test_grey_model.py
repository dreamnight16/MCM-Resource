"""Tests for Grey Model GM(1,1) implementation (grey_model.py)."""

import numpy as np
import pytest
from grey_model import gm11, post_residual_gm11

POPULATION = np.array([89677, 90859, 92148, 93769, 95050,
                       96450, 97812, 99256, 100729, 102034])

MIN_DATA = np.array([100, 110, 120, 130])

CONSTANT_DATA = np.ones(6) * 100


class TestGm11:
    def test_returns_all_expected_keys(self):
        result = gm11(POPULATION, forecast_num=3)
        expected = {'forecast', 'fitted', 'residuals', 'relative_errors',
                    'C', 'P', 'grade', 'grade_name', 'lambdas_ok', 'params'}
        assert expected.issubset(result.keys())

    def test_forecast_shape(self):
        result = gm11(POPULATION, forecast_num=5)
        assert len(result['forecast']) == 5

    def test_fitted_shape_matches_input(self):
        result = gm11(POPULATION)
        assert len(result['fitted']) == len(POPULATION)

    def test_residuals_match_definition(self):
        result = gm11(POPULATION)
        assert np.allclose(result['residuals'],
                           POPULATION - result['fitted'], atol=1)

    def test_params_are_scalars(self):
        result = gm11(POPULATION)
        assert np.isscalar(result['params']['a'])
        assert np.isscalar(result['params']['b'])

    def test_forecast_values_positive(self):
        result = gm11(POPULATION, forecast_num=3)
        assert np.all(result['forecast'] > 0)

    def test_grade_is_1_or_2_for_clean_data(self):
        result = gm11(POPULATION)
        assert result['grade'] in (1, 2)

    def test_minimum_4_points_works(self):
        result = gm11(MIN_DATA)
        assert len(result['fitted']) == 4

    def test_constant_data_constant_forecast(self):
        result = gm11(CONSTANT_DATA, forecast_num=2)
        assert np.allclose(result['fitted'], 100, atol=1)
        assert np.allclose(result['forecast'], 100, atol=1)

    def test_lambdas_ok_is_bool(self):
        result = gm11(POPULATION)
        assert isinstance(result['lambdas_ok'], (bool, np.bool_))

    def test_relative_errors_non_negative(self):
        result = gm11(POPULATION)
        assert np.all(result['relative_errors'] >= 0)


class TestPostResidualGm11:
    def test_returns_same_keys(self):
        result = post_residual_gm11(POPULATION, forecast_num=2)
        expected = {'forecast', 'fitted', 'residuals', 'relative_errors',
                    'C', 'P', 'grade', 'grade_name', 'lambdas_ok', 'params'}
        assert expected.issubset(result.keys())

    def test_runs_on_clean_data(self):
        result = post_residual_gm11(POPULATION[:8], forecast_num=2)
        assert len(result['fitted']) == 8
        assert len(result['forecast']) == 2
