import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 52 个城市坐标，来自 berlin52.tsp（键使用 1..52）
data = {
    1: (565.0, 575.0),
    2: (25.0, 185.0),
    3: (345.0, 750.0),
    4: (945.0, 685.0),
    5: (845.0, 655.0),
    6: (880.0, 660.0),
    7: (25.0, 230.0),
    8: (525.0, 1000.0),
    9: (580.0, 1175.0),
    10: (650.0, 1130.0),
    11: (1605.0, 620.0),
    12: (1220.0, 580.0),
    13: (1465.0, 200.0),
    14: (1530.0, 5.0),
    15: (845.0, 680.0),
    16: (725.0, 370.0),
    17: (145.0, 665.0),
    18: (415.0, 635.0),
    19: (510.0, 875.0),
    20: (560.0, 365.0),
    21: (300.0, 465.0),
    22: (520.0, 585.0),
    23: (480.0, 415.0),
    24: (835.0, 625.0),
    25: (975.0, 580.0),
    26: (1215.0, 245.0),
    27: (1320.0, 315.0),
    28: (1250.0, 400.0),
    29: (660.0, 180.0),
    30: (410.0, 250.0),
    31: (420.0, 555.0),
    32: (575.0, 665.0),
    33: (1150.0, 1160.0),
    34: (700.0, 580.0),
    35: (685.0, 595.0),
    36: (685.0, 610.0),
    37: (770.0, 610.0),
    38: (795.0, 645.0),
    39: (720.0, 635.0),
    40: (760.0, 650.0),
    41: (475.0, 960.0),
    42: (95.0, 260.0),
    43: (875.0, 920.0),
    44: (700.0, 500.0),
    45: (555.0, 815.0),
    46: (830.0, 485.0),
    47: (1170.0, 65.0),
    48: (830.0, 610.0),
    49: (605.0, 625.0),
    50: (595.0, 360.0),
    51: (1340.0, 725.0),
    52: (1740.0, 245.0)
}

# 原文件中给出的 Tour order（0 基准）
tour_zero_based = [22, 19, 49, 15, 43, 33, 34, 35, 38, 39, 37, 36, 47, 23, 4, 14, 5, 3, 24, 45, 48, 31, 0, 21, 30, 17, 2, 18, 44, 40, 7, 9, 8, 42, 32, 50, 11, 27, 26, 25, 46, 12, 13, 51, 10, 28, 29, 20, 16, 41, 6, 1]

# 转为 1 基准并闭合回路
best_path = [v + 1 for v in tour_zero_based]
best_path.append(best_path[0])

def plot_tour(data, best_path, is_save=False, gif_name="berlin52.gif", fps=5):
    """
    自包含绘制并可保存 GIF（与 bays29/ulysses16 保持相同逻辑）
    :param data: 坐标字典
    :param best_path: 包含回到起点的访问顺序（以 1 为基准）
    :param is_save: 是否保存 GIF
    :param gif_name: 输出 GIF 文件名
    :param fps: 帧率
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    xs = [c[0] for c in data.values()]
    ys = [c[1] for c in data.values()]
    ax.set_xlim(min(xs) - 50, max(xs) + 50)
    ax.set_ylim(min(ys) - 50, max(ys) + 50)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Berlin52 tour")

    x_seq = []
    y_seq = []
    frames = []
    for v in best_path:
        x_seq.append(data[v][0])
        y_seq.append(data[v][1])

        # 绘制当前帧内容（点、编号与连线），保持与 bays29/ulysses16 风格一致
        pts = ax.plot(x_seq, y_seq, 'c^', markersize=6)
        txts = [ax.text(data[v][0], data[v][1], str(v), ha='center', va='center_baseline', size=6)]
        line = ax.plot(x_seq, y_seq, '--', linewidth=1, color='gray')
        frames.append(pts + line + txts)

    ani = animation.ArtistAnimation(fig, frames, interval=int(1000/fps), repeat_delay=0)
    if is_save:
        ani.save(gif_name, writer='pillow', fps=fps)
    plt.show()

if __name__ == "__main__":
    # 运行并保存 berlin52.gif（与 bays29/ulysses16 行为一致）
    plot_tour(data, best_path, True)
    plot_tour(data, best_path, True)
