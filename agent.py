import random

class SimpleAgent:
    def choose_action(self, state):
        ambulance_lane = state["ambulance_lane"]
        severity = state["severity"]
        traffic = state["traffic"]

        # 🚑 If ambulance exists, go there
        if ambulance_lane != -1:
            # For severity 3 → always pick ambulance lane
            if severity == 3:
                return ambulance_lane
            # For severity 1-2 → pick ambulance lane only if traffic not too high
            elif traffic[ambulance_lane] < max(traffic):
                return ambulance_lane

        # Otherwise pick lane with highest traffic reduction potential
        max_vehicles = max(traffic)
        best_lanes = [i for i, v in enumerate(traffic) if v == max_vehicles]

        return random.choice(best_lanes)