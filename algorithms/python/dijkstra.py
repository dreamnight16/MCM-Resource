# -*- coding: utf-8 -*-
"""
Dijkstra 最短路径算法 — Python 实现
单源最短路径，适用于非负权图

用法：
    python dijkstra.py
"""

import numpy as np


def dijkstra(adj_matrix, source=0):
    """
    Dijkstra 算法

    Parameters
    ----------
    adj_matrix : ndarray (n, n)
        邻接矩阵，adj_matrix[i, j] 为边 i→j 的权重
        无穷大表示无边
    source : int
        源点索引

    Returns
    -------
    dict: {
        'dist': 最短距离数组,
        'prev': 前驱节点数组（用于重建路径）,
        'paths': 各节点的最短路径（节点列表）
    }
    """
    A = np.asarray(adj_matrix, dtype=float)
    n = A.shape[0]

    INF = np.inf
    dist = np.full(n, INF)
    dist[source] = 0
    prev = np.full(n, -1, dtype=int)
    visited = np.zeros(n, dtype=bool)

    for _ in range(n):
        # 选择未访问的最近节点
        unvisited_dist = np.where(visited, INF, dist)
        u = np.argmin(unvisited_dist)
        if np.isinf(dist[u]):
            break
        visited[u] = True

        # 松弛操作
        for v in range(n):
            if not visited[v] and A[u, v] < INF:
                alt = dist[u] + A[u, v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    # 重建路径
    paths = []
    for v in range(n):
        path = []
        curr = v
        while curr != -1:
            path.append(curr)
            curr = prev[curr]
        path.reverse()
        paths.append(path if path[0] == source else [])

    return {'dist': dist, 'prev': prev, 'paths': paths}


# ==========================================
# 示例运行
# ==========================================

if __name__ == '__main__':
    INF = np.inf
    graph = np.array([
        [0,   4,   2,   INF, INF],
        [4,   0,   1,   5,   INF],
        [2,   1,   0,   8,   10],
        [INF, 5,   8,   0,   2],
        [INF, INF, 10,  2,   0],
    ])

    print("=" * 60)
    print("Dijkstra 最短路径算法示例")
    print("=" * 60)
    print(f"邻接矩阵:\n{graph}")

    result = dijkstra(graph, source=0)

    print(f"\n从节点 0 出发:")
    for v in range(len(graph)):
        if result['dist'][v] < INF:
            path_str = ' → '.join(str(p) for p in result['paths'][v])
            print(f"  到节点 {v}: 距离={result['dist'][v]:.0f}, 路径={path_str}")
        else:
            print(f"  到节点 {v}: 不可达")
