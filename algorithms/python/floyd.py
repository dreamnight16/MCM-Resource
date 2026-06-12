# -*- coding: utf-8 -*-
"""
Floyd-Warshall 全源最短路径算法 — Python 实现
O(n^3)，支持负权边（无负环）

用法：
    python floyd.py
"""

import numpy as np


def floyd_warshall(adj_matrix):
    """
    Floyd-Warshall 全源最短路径

    Parameters
    ----------
    adj_matrix : ndarray (n, n)
        邻接矩阵，0 表示自身，INF 表示无边

    Returns
    -------
    dict: {
        'dist': 最短距离矩阵 (n, n),
        'next': 路径后继矩阵 (n, n)，用于重建路径
    }
    """
    A = np.asarray(adj_matrix, dtype=float)
    n = A.shape[0]
    INF = np.inf

    dist = A.copy()
    next_node = np.full((n, n), -1, dtype=int)

    for i in range(n):
        for j in range(n):
            if dist[i, j] < INF and i != j:
                next_node[i, j] = j

    # 三重循环：k 为中间节点
    for k in range(n):
        for i in range(n):
            if dist[i, k] == INF:
                continue
            for j in range(n):
                through_k = dist[i, k] + dist[k, j]
                if through_k < dist[i, j]:
                    dist[i, j] = through_k
                    next_node[i, j] = next_node[i, k]

    return {'dist': dist, 'next': next_node}


def reconstruct_path(next_matrix, start, end):
    """
    从 next 矩阵重建 start → end 的最短路径
    """
    if next_matrix[start, end] == -1:
        return []
    path = [start]
    while start != end:
        start = next_matrix[start, end]
        path.append(start)
    return path


# ==========================================
# 示例运行
# ==========================================

if __name__ == '__main__':
    INF = np.inf
    graph = np.array([
        [0,   3,   8,   INF, -4],
        [INF, 0,   INF, 1,   7],
        [INF, 4,   0,   INF, INF],
        [2,   INF, -5,  0,   INF],
        [INF, INF, INF, 6,   0],
    ])

    print("=" * 60)
    print("Floyd-Warshall 全源最短路径算法示例")
    print("=" * 60)
    print(f"邻接矩阵:\n{graph}")

    result = floyd_warshall(graph)

    print("\n最短距离矩阵:")
    dist_display = np.where(np.isinf(result['dist']), -1, result['dist']).astype(int)
    print(dist_display)

    print("\n各点对最短路径:")
    n = len(graph)
    for i in range(n):
        for j in range(n):
            if i != j and result['dist'][i, j] < INF:
                path = reconstruct_path(result['next'], i, j)
                path_str = ' → '.join(str(p) for p in path)
                print(f"  {i}→{j}: 距离={result['dist'][i,j]:.0f}, 路径={path_str}")
