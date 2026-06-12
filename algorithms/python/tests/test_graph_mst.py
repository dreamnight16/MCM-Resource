"""Tests for Kruskal and Prim MST algorithms."""

import numpy as np
import pytest
from kruskal import kruskal
from prim import prim


@pytest.fixture
def edges_5():
    return [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9),
    ]


class TestKruskal:
    def test_returns_expected_keys(self, edges_5):
        result = kruskal(5, edges_5)
        assert 'mst_edges' in result
        assert 'total_weight' in result

    def test_mst_has_n_minus_1_edges(self, edges_5):
        result = kruskal(5, edges_5)
        assert len(result['mst_edges']) == 4  # n-1 = 4

    def test_mst_total_weight_is_correct(self, edges_5):
        result = kruskal(5, edges_5)
        assert result['total_weight'] == 16  # 2+3+5+6

    def test_mst_edges_are_subset(self, edges_5):
        result = kruskal(5, edges_5)
        edge_set = {(min(u,v), max(u,v), w) for u,v,w in edges_5}
        mst_set = {(min(u,v), max(u,v), w) for u,v,w in result['mst_edges']}
        assert mst_set.issubset(edge_set)

    def test_single_edge(self):
        result = kruskal(2, [(0, 1, 5)])
        assert len(result['mst_edges']) == 1
        assert result['total_weight'] == 5


class TestPrim:
    def test_returns_expected_keys(self, edges_5):
        result = prim(5, edges_5)
        assert 'mst_edges' in result
        assert 'total_weight' in result

    def test_mst_has_n_minus_1_edges(self, edges_5):
        result = prim(5, edges_5)
        assert len(result['mst_edges']) == 4

    def test_mst_total_weight_is_correct(self, edges_5):
        result = prim(5, edges_5)
        # Prim may find different MST with same total weight
        assert result['total_weight'] == 16

    def test_both_algorithms_same_weight(self, edges_5):
        r_kruskal = kruskal(5, edges_5)
        r_prim = prim(5, edges_5)
        assert r_kruskal['total_weight'] == r_prim['total_weight']

    def test_triangle_graph(self):
        edges = [(0, 1, 2), (1, 2, 3), (0, 2, 1)]
        result = prim(3, edges)
        assert result['total_weight'] == 3  # edges (0,2)=1 + (0,1)=2
        assert len(result['mst_edges']) == 2
