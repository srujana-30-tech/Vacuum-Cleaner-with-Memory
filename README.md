# Vacuum Cleaner Problem with Memory in Python

## Aim

To implement a Vacuum Cleaner Agent with Memory in Python that cleans two rooms, A and B, while keeping track of previously visited states.

## Description

The Vacuum Cleaner Problem is a classic Artificial Intelligence (AI) problem that demonstrates how an intelligent agent interacts with its environment.

The environment consists of two rooms, A and B. Each room can be either Clean or Dirty. The vacuum cleaner starts in a randomly selected room, and the initial condition of each room is also determined randomly.

The agent checks the current room's condition and performs the appropriate action:

* If the current room is Dirty, it cleans the room.
* If the current room is Clean and the agent is in Room A, it moves to Room B.
* If the current room is Clean and the agent is in Room B, it moves to Room A.
* The program terminates when both rooms are clean.

### Role of Memory

The program uses a Python `set` named `memory` to store previously visited states.

Each state consists of three values:

* Current location of the vacuum cleaner.
* Cleanliness status of Room A.
* Cleanliness status of Room B.

For example, `('A', 'Dirty', 'Clean')` represents the vacuum cleaner being in Room A, with Room A dirty and Room B clean.

Before processing a state, the program checks whether it already exists in memory. If the state has been visited before, a message is displayed. Otherwise, the state is added to memory.

**Note:** Memory tracks repeated states, but the program continues performing actions even when a repeated state is encountered.

## Technologies Used

* Python
* Random module
* Set data structure
* Dictionary data structure

## Algorithm

1. Import the `random` module.
2. Randomly assign Clean or Dirty status to rooms A and B.
3. Randomly select the starting location of the vacuum cleaner.
4. Initialize an empty set called `memory`.
5. Display the initial room conditions and starting location.
6. Create a state using the current location and the cleanliness status of both rooms.
7. Check whether the state is already present in memory.
8. If the state has been visited, display a message. Otherwise, add it to memory.
9. If the current room is Dirty, clean it.
10. If the current room is Clean, move to the other room.
11. Check whether both rooms are clean.
12. If both rooms are clean, display the final status and the total number of unique states visited.
13. Terminate the program.

## How to Run

1. Install Python on your computer.
2. Save the program as `vacuum_cleaner.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the file.
5. Execute the following command:

```bash
python vacuum_cleaner.py
```

## Sample Output

```text
Initial States: {'A': 'Dirty', 'B': 'Clean'}
Vacuum cleaner starting from room A
-----Cleaning Process-----

Vacuum is in Room A | Status: Dirty
Action: Suck the dirt in room A

Vacuum is in Room A | Status: Clean
Action: Move right to room B

Vacuum is in Room B | Status: Clean
Action: Move left to room A
Both the rooms are clean!
Final Status: {'A': 'Clean', 'B': 'Clean'}
Total unique states visited 3
```

**Note:** The output may vary each time because the initial room conditions and starting location are selected randomly.

## AI Concepts Used

### 1. Intelligent Agent

The vacuum cleaner observes the current room and performs actions based on its cleanliness.

### 2. Environment

The environment consists of two rooms, A and B.

### 3. Percepts

The agent uses its current location and the room's cleanliness status to decide what action to perform.

### 4. Actions

The available actions are:

* **Suck:** Clean the current room.
* **Move Right:** Move from Room A to Room B.
* **Move Left:** Move from Room B to Room A.

### 5. State Space

A state represents the vacuum cleaner's current location and the cleanliness status of both rooms.

### 6. Memory

The `memory` set stores previously visited states to track unique states and identify repeated visits.

### 7. Goal State

The goal is achieved when both rooms A and B are clean.

## Advantages

* Easy to understand and implement.
* Demonstrates the working of a basic AI agent.
* Uses memory to track previously visited states.
* Helps understand state-space representation.
* Uses random initialization to simulate different environments.

## Applications

* Understanding AI agents and their environments.
* Learning state-space representation and memory.
* Studying intelligent cleaning systems.
* Understanding basic AI problem-solving techniques.

## Conclusion

The Vacuum Cleaner Problem with Memory demonstrates how an AI agent interacts with an environment, cleans dirty rooms, and moves between locations. The memory component records previously visited states, helping illustrate how an agent can track its past experiences while working toward its goal of cleaning both rooms.
