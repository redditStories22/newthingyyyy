import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

N = int(input("Enter the number of disks: "))

colors = plt.cm.viridis(np.linspace(0, 1, N))

disks = []
pegs = {'A': [], 'B': [], 'C': []}

for i in range(N, 0, -1):
    pegs['A'].append(i)

disk_moves = []

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    disk_moves.append((from_rod, to_rod))
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

TowerOfHanoi(N, 'A', 'C', 'B')

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-1, 3)
ax.set_ylim(-1, N + 3)
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['A', 'B', 'C'], fontsize=14, fontweight='bold')
ax.set_title("Tower of Hanoi", fontsize=16, fontweight='bold', color='darkblue')
ax.set_facecolor("lightgray")

cost_display = ax.text(1, N + 1.5, "Total Cost: 0", fontsize=14, fontweight='bold', color='red', ha='center')

def draw_pegs():
    for i in range(3):
        ax.plot([i, i], [-0.5, N + 1], color='black', lw=5)

def draw_disks():
    global disks
    disks = []
    for peg_idx, peg_name in enumerate(['A', 'B', 'C']):
        peg_disks = pegs[peg_name]
        for disk_idx, disk_size in enumerate(sorted(peg_disks, reverse=True)):
            rect = plt.Rectangle((peg_idx - disk_size * 0.1, disk_idx), disk_size * 0.2, 0.8, 
                                 color=colors[disk_size - 1], edgecolor='black', linewidth=1.5)
            ax.add_patch(rect)
            disks.append(rect)

def update(frame):
    if frame < len(disk_moves):
        from_rod, to_rod = disk_moves[frame]
        if pegs[from_rod] and (not pegs[to_rod] or pegs[to_rod][-1] > pegs[from_rod][-1]):
            disk = pegs[from_rod].pop()
            pegs[to_rod].append(disk)
    ax.clear()
    ax.set_xlim(-1, 3)
    ax.set_ylim(-1, N + 3)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(['A', 'B', 'C'], fontsize=14, fontweight='bold')
    ax.set_title("Tower of Hanoi", fontsize=16, fontweight='bold', color='darkblue')
    ax.set_facecolor("lightgray")
    draw_pegs()
    draw_disks()
    cost_display.set_text(f"Total Cost: {frame + 1}")
    ax.text(1, N + 1.5, f"Total Cost: {frame + 1}", fontsize=14, fontweight='bold', color='red', ha='center')

draw_pegs()
draw_disks()
ani = animation.FuncAnimation(fig, update, frames=len(disk_moves), interval=800, repeat=False)
plt.show()

print(f"Total cost of the path: {len(disk_moves)}")