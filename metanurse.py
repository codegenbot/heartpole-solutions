import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health: sleep if seriously needed
    if alertness < 0.4 or hypertension > 0.8 or intoxication > 0.3 or time_since_slept > 6:
        return 3  # Sleep if any health condition is risky or enough time has passed since last sleep

    # Optimal working condition
    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.1:
        return 0  # Just work if in perfect health and alertness

    # Use coffee to boost alertness when moderately low
    if 0.4 <= alertness <= 0.6 and hypertension < 0.6 and intoxication < 0.2:
        return 1  # Coffee and work under safe conditions and moderate alertness
    
    # Default to sleep to maintain health if other conditions aren't met
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)