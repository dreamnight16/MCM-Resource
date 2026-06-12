# -*- coding: utf-8 -*-
"""
Kruskal 最小生成树算法 — Python 实现
使用并查集优化，O(E log E)

用法：
    python kruskal.py
"""

import numpy as np


class UnionFind:
    """并查集（路径压缩 + 按秩合并）"""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True


def kruskal(n_vertices, edges):
    """
    Kruskal 最小生成树算法

    Parameters
    ----------
    n_vertices : int
        顶点数
    edges : list of (u, v, weight)
        边列表，u 和 v 为顶点索引，weight 为权重

    Returns
    -------
    dict: {
        'mst_edges': 最小生成树的边列表,
        'total_weight': 总权重
    }
    """
    sorted_edges = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(n_vertices)
    mst = []
    total = 0.0

    for u, v, w in sorted_edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == n_vertices - 1:
                break

    return {'mst_edges': mst, 'total_weight': total}


# ==========================================
# 示例运行
# ==========================================

if __name__ == '__main__':
    print("=" * 60)
    print("Kruskal 最小生成树算法示例")
    print("=" * 60)

    # 5 个顶点，7 条边
    # 边格式: (u, v, weight)
    edges = [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9),
    ]

    print("边列表 (u, v, weight):")
    for u, v, w in edges:
        print(f"  ({u}, {v}, {w})")

    result = kruskal(5, edges)

    print(f"\n最小生成树 (总权重={result['total_weight']}):")
    for u, v, w in result['mst_edges']:
        print(f"  ({u}, {v}, {w})")
