# ------------------------------
# run.py
# ------------------------------

print("Running file...")

from tasks import EasyTrafficEnv
from agent import SimpleAgent

env = EasyTrafficEnv()
agent = SimpleAgent()

episodes = 10
total_reward = 0

for ep in range(episodes):
    state = env.reset()
    done = False
    step = 0

    while not done:
        action = agent.choose_action(state)
        state, reward, done = env.step(action)

        # ------------------------------
        # Visualization of traffic
        # ------------------------------
        print(f"\nEpisode: {ep}, Step: {step}")
        for i in range(4):
            lane_visual = "|" * state["traffic"][i]

            if i == state["ambulance_lane"]:
                lane_visual += " 🚑"

            print(f"Lane {i+1}: {lane_visual}")

        print("Reward:", reward)

        total_reward += reward
        step += 1

avg_reward = total_reward / episodes
print("\nFinal Average Reward:", avg_reward)