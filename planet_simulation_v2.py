import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches
from matplotlib.widgets import Slider, Button, CheckButtons
from dataclasses import dataclass, field

# ── Константы ────────────────────────────────────────────────────────────────
G = 4 * np.pi**2   # [а.е.³ / (M☉ · год²)]

# ── Тело ─────────────────────────────────────────────────────────────────────
@dataclass
class Body:
    name:  str
    mass:  float
    pos:   np.ndarray
    vel:   np.ndarray
    color: str   = "white"
    size:  float = 6
    trail: list  = field(default_factory=list)

    def __post_init__(self):
        self.pos = np.array(self.pos, dtype=float)
        self.vel = np.array(self.vel, dtype=float)

# ── Начальные тела ────────────────────────────────────────────────────────────
def create_solar_system():
    bodies = [
        Body("Солнце",   1.0,    [ 0.000, 0.0], [0.0,  0.00], "#FFD700", 20),
        Body("Меркурий", 1.65e-7,[ 0.387, 0.0], [0.0, 10.10], "#B5B5B5",  4),
        Body("Венера",   2.45e-6,[ 0.723, 0.0], [0.0,  7.39], "#E8C46A",  6),
        Body("Земля",    3.00e-6,[ 1.000, 0.0], [0.0,  6.28], "#4FC3F7",  6),
        Body("Марс",     3.23e-7,[ 1.524, 0.0], [0.0,  5.09], "#EF5350",  5),
        Body("Юпитер",   9.55e-4,[ 5.203, 0.0], [0.0,  2.76], "#F4A460", 14),
        Body("Сатурн",   2.86e-4,[ 9.537, 0.0], [0.0,  2.04], "#DAA520", 12),
        # Кометы
        Body("Комета-1", 1e-12,  [ 0.500, 0.0], [0.0, 14.00], "#88FFFF",  3),
        Body("Комета-2", 1e-12,  [-0.300, 0.5], [5.0, -12.00],"#FF88FF",  3),
    ]
    return bodies

# ── Физика ───────────────────────────────────────────────────────────────────
def compute_accelerations(bodies):
    n = len(bodies)
    accs = [np.zeros(2) for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            r = bodies[j].pos - bodies[i].pos
            d = np.linalg.norm(r)
            if d < 1e-10:
                continue
            f = G * bodies[i].mass * bodies[j].mass / d**2 * r / d
            accs[i] += f / bodies[i].mass
            accs[j] -= f / bodies[j].mass
    return accs

def velocity_verlet(bodies, accs_old, dt):
    for b, a in zip(bodies, accs_old):
        b.pos += b.vel * dt + 0.5 * a * dt**2
    accs_new = compute_accelerations(bodies)
    for b, a0, a1 in zip(bodies, accs_old, accs_new):
        b.vel += 0.5 * (a0 + a1) * dt
    return accs_new

def total_energy(bodies):
    """Полная механическая энергия системы."""
    ke = sum(0.5 * b.mass * np.dot(b.vel, b.vel) for b in bodies)
    pe = 0.0
    for i in range(len(bodies)):
        for j in range(i + 1, len(bodies)):
            d = np.linalg.norm(bodies[j].pos - bodies[i].pos)
            if d > 1e-10:
                pe -= G * bodies[i].mass * bodies[j].mass / d
    return ke + pe

# ── Главная симуляция ─────────────────────────────────────────────────────────
def run_simulation():
    bodies = create_solar_system()

    # Состояние
    state = {
        "paused":       False,
        "show_trails":  True,
        "dt":           0.005,
        "speed":        5,        # шагов на кадр
        "max_trail":    200,
        "elapsed":      0.0,
        "energy_hist":  [],
        "time_hist":    [],
        "selected":     None,
    }

    accs = compute_accelerations(bodies)

    # ── Фигура ───────────────────────────────────────────────────────────────
    fig = plt.figure(figsize=(14, 9), facecolor="#0d0d1f")
    fig.canvas.manager.set_window_title("🪐 Симуляция планет v2.0")

    # Основная область
    ax = fig.add_axes([0.0, 0.05, 0.72, 0.95], facecolor="#0a0a1a")
    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Солнечная система", color="white", fontsize=13, pad=8)

    # График энергии
    ax_e = fig.add_axes([0.74, 0.55, 0.24, 0.30], facecolor="#0d0d2f")
    ax_e.set_title("Полная энергия", color="white", fontsize=9)
    ax_e.tick_params(colors="gray", labelsize=7)
    ax_e.spines[:].set_color("#333366")
    energy_line, = ax_e.plot([], [], color="#44FFAA", lw=1)
    ax_e.set_xlabel("Годы", color="gray", fontsize=7)

    # ── Виджеты ──────────────────────────────────────────────────────────────
    ax_speed  = fig.add_axes([0.74, 0.44, 0.24, 0.03], facecolor="#1a1a3f")
    ax_trail  = fig.add_axes([0.74, 0.38, 0.24, 0.03], facecolor="#1a1a3f")
    ax_pause  = fig.add_axes([0.74, 0.30, 0.11, 0.05], facecolor="#1a1a3f")
    ax_add    = fig.add_axes([0.87, 0.30, 0.11, 0.05], facecolor="#1a1a3f")

    sl_speed = Slider(ax_speed, "Скорость", 1, 20, valinit=5, valstep=1,
                      color="#4455FF")
    sl_trail = Slider(ax_trail, "След", 20, 500, valinit=200, valstep=10,
                      color="#FF4455")
    btn_pause = Button(ax_pause, "⏸ Пауза",  color="#1a2a5a", hovercolor="#2a3a7a")
    btn_add   = Button(ax_add,   "➕ Тело",   color="#1a4a2a", hovercolor="#2a6a3a")

    for ax_ in [ax_speed, ax_trail]:
        ax_.title.set_color("white") if hasattr(ax_, 'title') else None

    sl_speed.label.set_color("white")
    sl_speed.valtext.set_color("#88AAFF")
    sl_trail.label.set_color("white")
    sl_trail.valtext.set_color("#FF8888")
    btn_pause.label.set_color("white")
    btn_add.label.set_color("white")

    # Инструкции
    ax_info = fig.add_axes([0.74, 0.06, 0.24, 0.22], facecolor="#0d0d2f")
    ax_info.axis("off")
    info_text = (
        "🖱 Колёсико — зум\n"
        "🖱 ПКМ+тащи — перемещение\n"
        "🖱 ЛКМ по планете — инфо\n"
        "⌨  [A] — добавить астероид\n"
        "⌨  [S] — сохранить GIF\n"
        "⌨  [Пробел] — пауза"
    )
    ax_info.text(0.05, 0.95, info_text, transform=ax_info.transAxes,
                 color="#AAAACC", fontsize=8, va="top", linespacing=1.7)

    time_text  = ax.text(0.02, 0.97, "", transform=ax.transAxes,
                         color="white", fontsize=10, va="top")
    info_label = ax.text(0.02, 0.06, "", transform=ax.transAxes,
                         color="#FFDD88", fontsize=9, va="bottom",
                         bbox=dict(boxstyle="round,pad=0.4", fc="#0a0a2a", alpha=0.8))

    # ── Графические объекты планет ────────────────────────────────────────────
    dots   = [ax.plot([], [], "o", color=b.color, ms=b.size, zorder=3)[0]
              for b in bodies]
    trails = [ax.plot([], [], "-", color=b.color, lw=0.8, alpha=0.45, zorder=2)[0]
              for b in bodies]
    labels = [ax.text(0, 0, b.name, color=b.color, fontsize=7,
                      ha="left", va="bottom", zorder=4)
              for b in bodies]

    # ── Callbacks ─────────────────────────────────────────────────────────────
    def on_speed(val):
        state["speed"] = int(sl_speed.val)

    def on_trail(val):
        state["max_trail"] = int(sl_trail.val)

    def on_pause(event):
        state["paused"] = not state["paused"]
        btn_pause.label.set_text("▶ Старт" if state["paused"] else "⏸ Пауза")

    def add_body(event=None):
        angle = np.random.uniform(0, 2*np.pi)
        r     = np.random.uniform(1.5, 8.0)
        pos   = [r * np.cos(angle), r * np.sin(angle)]
        v_circ = np.sqrt(G * 1.0 / r)
        vel   = [-v_circ * np.sin(angle) * np.random.uniform(0.6, 1.3),
                  v_circ * np.cos(angle) * np.random.uniform(0.6, 1.3)]
        b = Body(f"Астер-{len(bodies)-8}", 1e-12, pos, vel,
                 color=np.random.choice(["#FF8844","#44FF88","#8844FF","#FFFF44"]),
                 size=3)
        bodies.append(b)
        dots.append(ax.plot([], [], "o", color=b.color, ms=b.size, zorder=3)[0])
        trails.append(ax.plot([], [], "-", color=b.color, lw=0.6,
                              alpha=0.35, zorder=2)[0])
        labels.append(ax.text(0, 0, b.name, color=b.color, fontsize=6,
                              ha="left", va="bottom", zorder=4))
        nonlocal accs
        accs = compute_accelerations(bodies)

    def on_scroll(event):
        factor = 0.85 if event.button == "up" else 1.15
        xl = ax.get_xlim()
        yl = ax.get_ylim()
        cx = (xl[0]+xl[1])/2; cy = (yl[0]+yl[1])/2
        ax.set_xlim(cx + (xl[0]-cx)*factor, cx + (xl[1]-cx)*factor)
        ax.set_ylim(cy + (yl[0]-cy)*factor, cy + (yl[1]-cy)*factor)

    # Перетаскивание
    drag = {"active": False, "x0": 0, "y0": 0,
            "xl": None, "yl": None}

    def on_press(event):
        if event.inaxes != ax:
            return
        if event.button == 3:  # ПКМ — перетаскивание
            drag.update({"active": True, "x0": event.xdata, "y0": event.ydata,
                         "xl": ax.get_xlim(), "yl": ax.get_ylim()})
        elif event.button == 1:  # ЛКМ — выбор планеты
            for i, b in enumerate(bodies):
                if np.linalg.norm(b.pos - [event.xdata, event.ydata]) < 0.5:
                    state["selected"] = i
                    return
            state["selected"] = None
            info_label.set_text("")

    def on_release(event):
        drag["active"] = False

    def on_motion(event):
        if drag["active"] and event.inaxes == ax and event.xdata:
            dx = event.xdata - drag["x0"]
            dy = event.ydata - drag["y0"]
            ax.set_xlim(drag["xl"][0]-dx, drag["xl"][1]-dx)
            ax.set_ylim(drag["yl"][0]-dy, drag["yl"][1]-dy)

    def on_key(event):
        if event.key == " ":
            on_pause(None)
        elif event.key in ("a", "A", "ф", "Ф"):
            add_body()
        elif event.key in ("s", "S", "ы", "Ы"):
            save_gif()

    def save_gif():
        print("💾 Сохраняю GIF (200 кадров)… подожди ~30 сек")
        Writer = animation.PillowWriter(fps=30)
        ani_save = animation.FuncAnimation(fig, update, frames=200,
                                           init_func=init, blit=False)
        ani_save.save("solar_system.gif", writer=Writer)
        print("✅ Сохранено: solar_system.gif")

    sl_speed.on_changed(on_speed)
    sl_trail.on_changed(on_trail)
    btn_pause.on_clicked(on_pause)
    btn_add.on_clicked(add_body)
    fig.canvas.mpl_connect("scroll_event",        on_scroll)
    fig.canvas.mpl_connect("button_press_event",  on_press)
    fig.canvas.mpl_connect("button_release_event",on_release)
    fig.canvas.mpl_connect("motion_notify_event", on_motion)
    fig.canvas.mpl_connect("key_press_event",     on_key)

    # ── Анимация ──────────────────────────────────────────────────────────────
    def init():
        for d in dots:   d.set_data([], [])
        for t in trails: t.set_data([], [])
        return dots + trails + labels + [time_text, info_label, energy_line]

    def update(_frame):
        nonlocal accs
        if state["paused"]:
            return dots + trails + labels + [time_text, info_label, energy_line]

        for _ in range(state["speed"]):
            accs = velocity_verlet(bodies, accs, state["dt"])
            state["elapsed"] += state["dt"]
            for b in bodies:
                b.trail.append(b.pos.copy())
                if len(b.trail) > state["max_trail"]:
                    b.trail.pop(0)

        # Энергия каждые 10 кадров
        if int(state["elapsed"] / state["dt"]) % 10 == 0:
            state["energy_hist"].append(total_energy(bodies))
            state["time_hist"].append(state["elapsed"])
            if len(state["energy_hist"]) > 300:
                state["energy_hist"].pop(0)
                state["time_hist"].pop(0)
            energy_line.set_data(state["time_hist"], state["energy_hist"])
            ax_e.relim(); ax_e.autoscale_view()

        # Обновить точки и следы
        for i, b in enumerate(bodies):
            dots[i].set_data([b.pos[0]], [b.pos[1]])
            if state["show_trails"] and len(b.trail) > 1:
                tr = np.array(b.trail)
                trails[i].set_data(tr[:, 0], tr[:, 1])
            else:
                trails[i].set_data([], [])
            off = 0.15
            labels[i].set_position((b.pos[0]+off, b.pos[1]+off))

        # Время
        y = int(state["elapsed"])
        d = int((state["elapsed"] - y) * 365.25)
        time_text.set_text(f"⏱  {y} лет  {d} дней")

        # Инфо о выбранной планете
        s = state["selected"]
        if s is not None and s < len(bodies):
            b = bodies[s]
            v = np.linalg.norm(b.vel)
            r = np.linalg.norm(b.pos)
            info_label.set_text(
                f"🪐 {b.name}\n"
                f"r = {r:.3f} а.е.\n"
                f"v = {v:.3f} а.е./год\n"
                f"m = {b.mass:.2e} M☉"
            )

        return dots + trails + labels + [time_text, info_label, energy_line]

    ani = animation.FuncAnimation(
        fig, update, init_func=init,
        interval=20, blit=False, cache_frame_data=False
    )

    plt.show()
    return ani

# ── Запуск ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("🪐 Планетарная симуляция v2.0")
    print("─" * 40)
    print("  Колёсико мыши   — зум")
    print("  ПКМ + тащи      — перемещение")
    print("  ЛКМ по планете  — показать инфо")
    print("  [A]             — добавить астероид")
    print("  [S]             — сохранить GIF")
    print("  [Пробел]        — пауза/старт")
    print("─" * 40)
    run_simulation()
