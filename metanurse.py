import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness <= 0.5 or hypertension > 0.25 or intoxication > 0.1 or time_since_slept >= 8:
        return 3  # Sleep to recover if low alertness, high hypertension, high intoxication, or long hours awake
    if alertness < 0.75 and hypertension < 0.15 and intoxication < 0.05:
        return 1  # Drink coffee to boost if under controlled conditions
    if alertness > 0.85 and intoxication < 0.02 and hypertension < 0.15:
        return 2  # Drink beer in highly alert, low intoxication/pressure state
    return 0  # Continue working if other conditions don't necessitate an action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)