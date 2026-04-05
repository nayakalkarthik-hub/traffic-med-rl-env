import random

# ---- YOUR CLASS ----
class TrafficMedEnv:
    def __init__(self):
        self.lanes = 4
        self.time = 0

    def reset(self):
        self.traffic = [random.randint(5, 20) for _ in range(self.lanes)]
        self.ambulance_lane = random.choice([-1, 0, 1, 2, 3])
        self.severity = random.randint(1, 3) if self.ambulance_lane != -1 else 0
        self.time = 0
        return self.state()

    def state(self):
        return {
            "traffic": self.traffic,
            "ambulance_lane": self.ambulance_lane,
            "severity": self.severity
        }

    def step(self, action):
        self.time += 1
        reward = 0.0

        passed = min(5, self.traffic[action])
        self.traffic[action] -= passed

        for i in range(self.lanes):
            if i != action:
                self.traffic[i] += random.randint(0, 3)

        if self.ambulance_lane != -1:
            if action == self.ambulance_lane:
                # 🚑 Higher severity = more reward
                reward += 0.5 + (0.2 * self.severity)
            else:
                # ❌ Heavy penalty if you ignore serious ambulance
                reward -= 0.5 * self.severity
                
        reward += 0.4 * (passed / 5)
        reward = max(0.0, min(1.0, reward))

        done = self.time >= 20
        return self.state(), reward, done


# ---- TEST BLOCK (PUT IT HERE 👇) ----
if __name__ == "__main__":
    from tasks import EasyTrafficEnv   # ✅ HERE
    import random                      # (optional, already imported above)

    env = EasyTrafficEnv()
    state = env.reset()

    print("Initial State:", state)

    for _ in range(5):
        action = random.randint(0, 3)
        state, reward, done = env.step(action)
        print("Next State:", state, "Reward:", reward)