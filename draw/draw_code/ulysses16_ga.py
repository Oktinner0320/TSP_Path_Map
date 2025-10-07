import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 16 个城市的坐标（来自 ulysses16.tsp）
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

# ulysses16_ga.tsp 中的 Tour order（0 基准）
tour_zero_based = [0, 7, 3, 1, 2, 15, 9, 8, 10, 4, 14, 5, 6, 11, 12, 13]

# 转换为 1 基准并闭合回路
best_path = [v + 1 for v in tour_zero_based]
best_path.append(best_path[0])

def plot_tour(data, best_path, is_save=False, gif_name="ulysses16_ga.gif", fps=3):
    """
    自包含绘图并可保存 GIF（与其他脚本一致的逻辑）
    """
    fig, ax = plt.subplots()
    xs = [c[0] for c in data.values()]
    ys = [c[1] for c in data.values()]
    ax.set_xlim(min(xs) - 1, max(xs) + 1)
    ax.set_ylim(min(ys) - 1, max(ys) + 1)
    x_seq = []
    y_seq = []
    frames = []
    for v in best_path:
        x_seq.append(data[v][0])
        y_seq.append(data[v][1])

        pts = ax.plot(x_seq, y_seq, 'c^', markersize=8)
        txt = ax.text(data[v][0], data[v][1], str(v), ha='center', va='center_baseline', size=8)
        line = ax.plot(x_seq, y_seq, '--', linewidth=2, color='gray')

        frames.append(pts + line + [txt])

    ani = animation.ArtistAnimation(fig, frames, interval=int(1000/fps), repeat_delay=0)
    if is_save:
        ani.save(gif_name, writer='pillow', fps=fps)
    plt.show()

if __name__ == "__main__":
    # 运行并保存 ulysses16_ga.gif
    plot_tour(data, best_path, True)
