import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 29 个城市的坐标，来自 bays29.tsp DISPLAY_DATA_SECTION（键使用 1..29）
data = {
    1: (1150.0, 1760.0),
    2: (630.0, 1660.0),
    3: (40.0, 2090.0),
    4: (750.0, 1100.0),
    5: (750.0, 2030.0),
    6: (1030.0, 2070.0),
    7: (1650.0, 650.0),
    8: (1490.0, 1630.0),
    9: (790.0, 2260.0),
    10: (710.0, 1310.0),
    11: (840.0, 550.0),
    12: (1170.0, 2300.0),
    13: (970.0, 1340.0),
    14: (510.0, 700.0),
    15: (750.0, 900.0),
    16: (1280.0, 1200.0),
    17: (230.0, 590.0),
    18: (460.0, 860.0),
    19: (1040.0, 950.0),
    20: (590.0, 1390.0),
    21: (830.0, 1770.0),
    22: (490.0, 500.0),
    23: (1840.0, 1240.0),
    24: (1260.0, 1500.0),
    25: (1280.0, 790.0),
    26: (490.0, 2130.0),
    27: (1460.0, 1420.0),
    28: (1260.0, 1910.0),
    29: (360.0, 1980.0)
}

# 原文件中的 Tour order（0 基准）
tour_zero_based = [22, 26, 23, 7, 0, 27, 5, 11, 8, 4, 25, 28, 2, 1, 20, 19, 9, 3, 14, 17, 13, 21, 16, 10, 18, 15, 12, 24, 6]

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
    # 可选：设置坐标轴范围以包含所有点并保持固定
    xs = [coord[0] for coord in data.values()]
    ys = [coord[1] for coord in data.values()]
    ax.set_xlim(min(xs) - 50, max(xs) + 50)
    ax.set_ylim(min(ys) - 50, max(ys) + 50)

    for v in best_path:
        x.append(data[v][0])
        y.append(data[v][1])

        # 标记点并加编号（每帧都会重画，效果同动画逐步连接）
        ax.plot(x, y, 'c^', linewidth=2, markersize=8)
        ax.text(data[v][0], data[v][1], str(v), ha='center', va='center_baseline', size=8)

        # 当前帧的连线
        line = ax.plot(x, y, '--', linewidth=2)
        frames.append(line)

    ani = animation.ArtistAnimation(fig, frames, interval=300, repeat_delay=0)
    if is_save:
        # 使用 pillow 保存为 gif，设置帧率
        ani.save("bays29.gif", writer='pillow', fps=3)
    plt.show()

if __name__ == "__main__":
    # 运行并保存生成的 GIF
    plot_tour(data, best_path, True)
