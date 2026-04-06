<<<<<<< HEAD
# Traffic Medical RL Environment 🚦🚑

## Description
This project simulates a real-world traffic signal control system using Reinforcement Learning concepts.  
The environment models a 4-lane intersection where an AI agent controls traffic lights to reduce congestion while prioritizing emergency vehicles like ambulances.

---

## Problem Statement
Traditional traffic signals are static and do not adapt to real-time conditions.  
This becomes critical when emergency vehicles need immediate clearance.

---

## Solution
We designed a custom RL environment where:
- Traffic varies dynamically
- Ambulances appear randomly
- Each ambulance has a severity level (1–3)
- The agent decides which lane gets the green signal

---

## Features
- 4-lane traffic simulation
- Ambulance priority handling 🚑
- Severity-based decision making
- Reward system (0.0 to 1.0)
- Easy, Medium, Hard tasks
- Visual traffic output in terminal

---

## Action Space
Discrete actions:
- 0 → Lane 0
- 1 → Lane 1
- 2 → Lane 2
- 3 → Lane 3

---

## Observation Space
The agent receives:
- `traffic`: list[int] → number of vehicles in each lane
- `ambulance_lane`: int → lane index (-1 if no ambulance)
- `severity`: int → urgency level (1 to 3)

---

## Reward Function
- High reward for prioritizing ambulance lane
- Higher reward for higher severity cases
- Partial reward for reducing traffic congestion
- Penalty for ignoring emergency vehicles

Reward range: **0.0 to 1.0**

---

## Tasks
- Easy → No ambulance (focus on traffic flow)
- Medium → Random ambulance
- Hard → Severity-based ambulance priority

---

## How to Run

```bash
=======
# Traffic Medical RL Environment 🚦🚑

## Description
This project simulates a real-world traffic signal control system using Reinforcement Learning concepts.  
The environment models a 4-lane intersection where an AI agent controls traffic lights to reduce congestion while prioritizing emergency vehicles like ambulances.

---

## Problem Statement
Traditional traffic signals are static and do not adapt to real-time conditions.  
This becomes critical when emergency vehicles need immediate clearance.

---

## Solution
We designed a custom RL environment where:
- Traffic varies dynamically
- Ambulances appear randomly
- Each ambulance has a severity level (1–3)
- The agent decides which lane gets the green signal

---

## Features
- 4-lane traffic simulation
- Ambulance priority handling 🚑
- Severity-based decision making
- Reward system (0.0 to 1.0)
- Easy, Medium, Hard tasks
- Visual traffic output in terminal

---

## Action Space
Discrete actions:
- 0 → Lane 0
- 1 → Lane 1
- 2 → Lane 2
- 3 → Lane 3

---

## Observation Space
The agent receives:
- `traffic`: list[int] → number of vehicles in each lane
- `ambulance_lane`: int → lane index (-1 if no ambulance)
- `severity`: int → urgency level (1 to 3)

---

## Reward Function
- High reward for prioritizing ambulance lane
- Higher reward for higher severity cases
- Partial reward for reducing traffic congestion
- Penalty for ignoring emergency vehicles

Reward range: **0.0 to 1.0**

---

## Tasks
- Easy → No ambulance (focus on traffic flow)
- Medium → Random ambulance
- Hard → Severity-based ambulance priority

---

## How to Run

```bash
>>>>>>> 85e45758f974eedc1504cf54d6431bd7544ce47b
python run.py