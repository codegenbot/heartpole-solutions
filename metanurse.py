import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health: sleep if any health indicator is concerning
    if hypertension > 0.25 or intoxication > 0.15:
        return 3  # Sleep

    # Adjust alertness threshold for coffee
    if 0.6 <= alertness < 0.8 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Encourage more frequent rest if significant time has passed since last sleep
    if time_since_slept > 3:
        return 3  # Sleep

    # Introduce beer option for relaxation if slightly intoxicated and alert
    if alertness >= 0.8 and intoxication <= 0.05:
        return 2  # Drink beer and work

    # Default to working only when all parameters are within a healthy range
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)