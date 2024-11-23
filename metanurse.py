import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health: sleep if any health indicator is moderately concerning
    if hypertension > 0.3 or intoxication > 0.2:
        return 3  # Sleep

    # Adjust alertness threshold to avoid over-reliance on sleep
    if alertness < 0.7:
        return 3  # Sleep

    # Use coffee strategically for alertness while keeping health checks
    if 0.7 <= alertness < 0.85 and hypertension <= 0.2 and intoxication <= 0.15:
        return 1  # Drink coffee and work

    # Encourage more frequent rest if significant time has passed since last sleep
    if time_since_slept > 4:
        return 3  # Sleep

    # Default to working only when all parameters are within a healthy range
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)