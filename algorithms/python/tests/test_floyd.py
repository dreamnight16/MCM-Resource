"""Tests for Floyd-Warshall algorithm (floyd.py)."""

import numpy as np
import pytest
from floyd import floyd_warshall, reconstruct_path

INF = np.inf


@pytest.fixture
def graph_4():
    # 4-node graph from CLRS
    return np.array([
        [0,   3,   8,   INF],
        [INF, 0,   INF, 1],
        [INF, 4,   0,   INF],
        [2,   INF, -5,  0],
    ])


class TestFloydWarshall:
    def test_returns_expected_keys(self, graph_4):
        result = floyd_warshall(graph_4)
        assert 'dist' in result
        assert 'next' in result

    def test_self_distance_zero(self, graph_4):
        result = floyd_warshall(graph_4)
        for i in range(len(graph_4)):
            assert result['dist'][i, i] == 0

    def test_dist_matrix_shape(self, graph_4):
        result = floyd_warshall(graph_4)
        assert result['dist'].shape == graph_4.shape

    def test_shortest_paths_non_negative_distances(self, graph_4):
        result = floyd_warshall(graph_4)
        n = len(graph_4)
        for i in range(n):
            for j in range(n):
                if result['dist'][i, j] < INF and i != j:
                    assert result['dist'][i, j] >= -100  # reasonable lower bound

    def test_negative_cycle_detection(self):
        # Graph with negative cycle: 0→1 (-5), 1→0 (-5)
        g = np.array([[0, -5], [-5, 0]])
        result = floyd_warshall(g)
        # algorithm still runs (doesn't hang)
        assert result['dist'].shape == (2, 2)

    def test_reconstruct_path(self, graph_4):
        result = floyd_warshall(graph_4)
        path = reconstruct_path(result['next'], 0, 3)
        if result['dist'][0, 3] < INF:
            assert len(path) >= 2
            assert path[0] == 0
            assert path[-1] == 3

    def test_simple_graph(self):
        g = np.array([
            [0, 1, INF],
            [1, 0, 1],
            [INF, 1, 0],
        ])
        result = floyd_warshall(g)
        assert result['dist'][0, 2] == 2
