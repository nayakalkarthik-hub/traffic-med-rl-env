from env import TrafficMedEnv

# 🧠 Trained Q-table (from your training output)
q_table = [
    [125.55, 80.67, 79.36, 76.74],
    [101.53, 134.93, 104.93, 107.01],
    [97.61, 93.82, 118.74, 91.75],
    [95.29, 93.65, 89.52, 126.71]
]

def run_inference():
    print("[START]")

    env = TrafficMedEnv()
    state = env.reset()

    done = False
    total_reward = 0

    while not done:
        # 🚑 Get ambulance lane (our state)
        state_lane = state["ambulance_lane"]

        # 🧠 Choose best action from Q-table
        action = q_table[state_lane].index(max(q_table[state_lane]))

        next_state, reward, done = env.step(action)

        total_reward += reward

        print(f"[STEP] action={action}, reward={reward}, state={state}")

        state = next_state

    print(f"[END] Total Reward: {total_reward}")


if __name__ == "__main__":
    run_inference()