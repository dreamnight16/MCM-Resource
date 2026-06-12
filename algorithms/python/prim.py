# -*- coding: utf-8 -*-
"""
Prim 最小生成树算法 — Python 实现
适用于稠密图，O(n^2)

用法：
    python prim.py
"""

import numpy as np


def prim(n_vertices, edges):
    """
    Prim 最小生成树算法

    Parameters
    ----------
    n_vertices : int
        顶点数
    edges : list of (u, v, weight)
        边列表

    Returns
    -------
    dict: {
        'mst_edges': 最小生成树的边列表,
        'total_weight': 总权重
    }
    """
    # 构建邻接矩阵
    INF = np.inf
    adj = np.full((n_vertices, n_vertices), INF)
    for u, v, w in edges:
        adj[u, v] = min(adj[u, v], w)
        adj[v, u] = min(adj[v, u], w)

    # Prim
    selected = np.zeros(n_vertices, dtype=bool)
    selected[0] = True
    mst = []
    total = 0.0

    for _ in range(n_vertices - 1):
        min_edge = (INF, -1, -1)
        for u in range(n_vertices):
            if not selected[u]:
                continue
            for v in range(n_vertices):
                if selected[v]:
                    continue
                if adj[u, v] < min_edge[0]:
                    min_edge = (adj[u, v], u, v)

        if min_edge[0] == INF:
            break  # 图不连通

        w, u, v = min_edge
        selected[v] = True
        mst.append((u, v, w))
        total += w

    return {'mst_edges': mst, 'total_weight': total}


# ==========================================
# 示例运行
# ==========================================

if __name__ == '__main__':
    print("=" * 60)
    print("Prim 最小生成树算法示例")
    print("=" * 60)

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

    result = prim(5, edges)

    print(f"\n最小生成树 (总权重={result['total_weight']}):")
    for u, v, w in result['mst_edges']:
        print(f"  ({u}, {v}, {w})")
