import random
def vacuum_cleaner():
    rooms={'A': random.choice(['Clean', 'Dirty']),
           'B': random.choice(['Clean', 'Dirty'])}
    
    current_loc = random.choice(['A', 'B'])
    memory=set()
    print("Initial States:",rooms)
    print("Vacuum cleaner starting from room",current_loc)
    print("-----Cleaning Process-----")
    while True:
        state=(current_loc,rooms['A'],rooms['B'])
        if state in memory:
            print(f"\nState{state}already visited-skipping redundant actions")
        else:
            memory.add(state)
            print(f"\nVacuum is in Room {current_loc} | Status: {rooms[current_loc]}")

        if rooms[current_loc] == 'Dirty':
            print(f"Action: Suck the dirt in room {current_loc}")
            rooms[current_loc] = 'Clean'
        else:
            if current_loc == 'A':
                print("Action: Move right to room B")
                current_loc = 'B'
            else:
                print("Action: Move left to room A")
                current_loc = 'A'

        if rooms['A'] == 'Clean' and rooms['B'] == 'Clean':
            print("Both the rooms are clean!")
            print("Final Status:", rooms)
            print("Total unique states visited",len(memory))
            break

vacuum_cleaner()
    

