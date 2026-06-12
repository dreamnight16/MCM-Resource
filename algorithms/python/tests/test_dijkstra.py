"""Tests for Dijkstra shortest path algorithm (dijkstra.py)."""

import numpy as np
import pytest
from dijkstra import dijkstra

INF = np.inf


@pytest.fixture
def graph_5():
    return np.array([
        [0,   4,   2,   INF, INF],
        [4,   0,   1,   5,   INF],
        [2,   1,   0,   8,   10],
        [INF, 5,   8,   0,   2],
        [INF, INF, 10,  2,   0],
    ])


class TestDijkstra:
    def test_returns_expected_keys(self, graph_5):
        result = dijkstra(graph_5, source=0)
        assert 'dist' in result
        assert 'prev' in result
        assert 'paths' in result

    def test_source_to_self_zero(self, graph_5):
        result = dijkstra(graph_5, source=0)
        assert result['dist'][0] == 0
        assert result['paths'][0] == [0]

    def test_correct_distances(self, graph_5):
        result = dijkstra(graph_5, source=0)
        assert result['dist'][0] == 0
        assert result['dist'][1] == 3   # 0→2→1 = 2+1
        assert result['dist'][2] == 2   # 0→2 = 2
        assert result['dist'][3] == 8   # 0→2→1→3 = 2+1+5 = 8

    def test_unreachable_node(self):
        g = np.array([[0, INF], [INF, 0]])
        result = dijkstra(g, source=0)
        assert np.isinf(result['dist'][1])

    def test_paths_are_valid(self, graph_5):
        result = dijkstra(graph_5, source=0)
        for v in range(len(graph_5)):
            path = result['paths'][v]
            if len(path) > 0:
                assert path[0] == 0
                assert path[-1] == v

    def test_different_source(self, graph_5):
        r0 = dijkstra(graph_5, source=0)
        r2 = dijkstra(graph_5, source=2)
        assert r0['dist'][0] == 0
        assert r2['dist'][2] == 0
        assert r0['dist'][1] != r2['dist'][1] or np.isclose(r0['dist'][1], r2['dist'][1])

    def test_single_node(self):
        g = np.array([[0]])
        result = dijkstra(g, source=0)
        assert result['dist'][0] == 0
