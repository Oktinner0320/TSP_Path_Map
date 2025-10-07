import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 16 个城市的坐标，来自 ulysses16.tsp（键使用 1..16）
data = {
    1: (38.24, 20.42),
    2: (39.57, 26.15),
    3: (40.56, 25.32),
    4: (36.26, 23.12),
    5: (33.48, 10.54),
    6: (37.56, 12.19),
    7: (38.42, 13.11),
    8: (37.52, 20.44),
    9: (41.23, 9.10),
    10: (41.17, 13.05),
    11: (36.08, -5.21),
    12: (38.47, 15.13),
    13: (38.15, 15.35),
    14: (37.51, 15.17),
    15: (35.49, 14.32),
    16: (39.36, 19.56)
}

# 原文件中的 Tour order（0 基准）:
tour_zero_based = [2, 1, 3, 7, 0, 15, 12, 13, 11, 6, 5, 14, 4, 9, 8, 10]

# 转换为 1 基准并闭合回路（在末尾追加起点）
best_path = [v + 1 for v in tour_zero_based]
best_path.append(best_path[0])

def plot_tour(data, best_path, is_save=False):
    """
    绘制旅行图（自包含实现）
    :param data: 坐标字典，键为城市编号，值为 (x,y)
    :param best_path: 城市访问顺序（包含回到起点）
    :param is_save: 是否保存生成的动画 gif
    """
    fig, ax = plt.subplots()
    x = []
    y = []
    frames = []
    for v in best_path:
        x.append(data[v][0])
        y.append(data[v][1])

        # 标记点并加编号
        ax.plot(x, y, 'c^', linewidth=2, markersize=8)
        ax.text(data[v][0], data[v][1], str(v), ha='center', va='center_baseline', size=8)

        # 当前帧的连线
        line = ax.plot(x, y, '--', linewidth=2)
        frames.append(line)

    ani = animation.ArtistAnimation(fig, frames, interval=300, repeat_delay=0)
    if is_save:
        # 使用 pillow 保存为 gif，设置帧率
        ani.save("ulysses16.gif", writer='pillow', fps=3)
    plt.show()

if __name__ == "__main__":
    # 运行并保存生成的 GIF
    plot_tour(data, best_path, True)
