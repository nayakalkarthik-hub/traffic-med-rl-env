import tkinter as tk
import random

root = tk.Tk()
root.title("Traffic RL with Ambulance Priority")
root.geometry("500x500")

canvas = tk.Canvas(root, width=500, height=500, bg="gray")
canvas.pack()

# Each lane will store tuples: (position, type)
# type = "car" or "ambulance"
lanes = [[], [], [], []]

current_green = 0

q_table = [[0]*4 for _ in range(4)]

def get_state():
    # Priority: if ambulance exists, pick that lane
    for i in range(4):
        for vehicle in lanes[i]:
            if vehicle[1] == "ambulance":
                return i
    return max(range(4), key=lambda i: len(lanes[i]))

def choose_action(state):
    return state  # force priority action

def update_q(state, action, reward):
    lr = 0.1
    gamma = 0.9
    q_table[state][action] += lr * (reward + gamma * max(q_table[action]) - q_table[state][action])

def spawn_vehicles():
    for i in range(4):
        if random.random() < 0.5:
            # 10% chance ambulance
            if random.random() < 0.1:
                lanes[i].append((0, "ambulance"))
            else:
                lanes[i].append((0, "car"))

def move_vehicles():
    for i in range(4):
        if i == current_green:
            new_lane = []
            for pos, vtype in lanes[i]:
                new_pos = pos + 20
                if new_pos < 250:
                    new_lane.append((new_pos, vtype))
            lanes[i] = new_lane

def update():
    global current_green

    spawn_vehicles()

    state = get_state()
    action = choose_action(state)
    current_green = action

    move_vehicles()

    reward = -sum(len(l) for l in lanes)
    update_q(state, action, reward)

    draw()
    root.after(500, update)

def draw():
    canvas.delete("all")

    # Roads
    canvas.create_line(0, 250, 500, 250, width=5, fill="white")
    canvas.create_line(250, 0, 250, 500, width=5, fill="white")

    # Signals
    positions = [(240, 100), (400, 240), (260, 400), (100, 260)]
    for i, (x, y) in enumerate(positions):
        color = "green" if i == current_green else "red"
        canvas.create_oval(x, y, x+30, y+30, fill=color)

    # Draw vehicles
    for i in range(4):
        for pos, vtype in lanes[i]:
            color = "red" if vtype == "ambulance" else "blue"

            if i == 0:
                canvas.create_rectangle(240, pos, 260, pos+20, fill=color)
            elif i == 1:
                canvas.create_rectangle(500-pos, 240, 480-pos, 260, fill=color)
            elif i == 2:
                canvas.create_rectangle(260, 500-pos, 240, 480-pos, fill=color)
            elif i == 3:
                canvas.create_rectangle(pos, 260, pos+20, 240, fill=color)

update()
root.mainloop()