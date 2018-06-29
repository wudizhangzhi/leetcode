import numpy as np


def A_Star(m, start, end):
    """A*搜索算法
    https://en.wikipedia.org/wiki/A*_search_algorithm

    Arg:
        m: map
        start: start point
        end: end point
    """

    def reconstruct_path(comeFrom, current):
        total_path = [current]
        while current in comeFrom:
            current = comeFrom[current]
            total_path.append(current)

        return total_path

    def heuristic_cost_estimate(s, d):
        return np.abs(np.sum(np.array(s) - np.array(d)))

    def get_lowest_score_point_estimated(fScore, open_set):
        min_score = 99999
        min_point = None
        for point in open_set:
            score = fScore[point]
            if score < min_score:
                min_score = score
                min_point = point
        return min_point

    def get_all_neighbor(point, m):
        w, h = m.shape
        p_w, p_h = point
        # 上下左右
        neighbors = []
        if p_w > 0:
            # 左
            p = (p_w - 1, p_h)
            neighbors.append(p)
        if p_h > 0:
            # 下
            p = (p_w, p_h - 1)
            neighbors.append(p)
        if p_w < w - 1:
            # 右
            p = (p_w + 1, p_h)
            neighbors.append(p)
        if p_h < h - 1:
            # 上
            p = (p_w, p_h + 1)
            neighbors.append(p)
        return neighbors

    def distance_between(a, b):
        return np.sum(np.array(b) - np.array(a))

    # 已经评估过的点
    closed_set = []
    # 待评估的点，初始化时候是起点
    open_set = [start]

    # 记录每个点的父节点
    comeFrom = {}

    # 每个点从起点到当前点的得分， 起点到起点是0
    gScore = {}
    gScore[start] = 0

    # 每个点从当起点到终点的预估得分, 起点因为gScore=0, 所以是单纯的heuristic_cost_estimate
    fScore = {}
    fScore[start] = heuristic_cost_estimate(start, end)

    while len(open_set) > 0:
        current = get_lowest_score_point_estimated(fScore, open_set)  # 分数最低的

        if current == end:
            return reconstruct_path(comeFrom, current)
        open_set.remove(current)
        closed_set.append(current)

        for neighbor in get_all_neighbor(current, m):

            if neighbor in closed_set:  # 已经评估过了
                continue

            if m[neighbor[0], neighbor[1]] == 1:  # 地图上的缺口不能前进
                continue

            if neighbor not in open_set:  # 加入评估
                open_set.append(neighbor)

            tentative_gScore = gScore[current] + distance_between(current, neighbor)
            # if tentative_gScore > gScore.get(neighbor, 99999):
            #     continue

            comeFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(neighbor, end)


def generate_map():
    m = np.zeros((10, 10))
    # for _ in range(10):
    #     idx = np.random.randint(0, 10)
    #     idy = np.random.randint(0, 10)
    #     m[idx, idy] = 1
    for i in range(7):
        m[i + 1, 5] = 1
    return m


if __name__ == '__main__':
    m = generate_map()
    print(m)
    start = (5, 0)
    end = (5, 8)
    total_path = A_Star(m, start, end)
    print(total_path)
    for p in total_path:
        m[p[0], p[1]] = '9'
    print(m)
