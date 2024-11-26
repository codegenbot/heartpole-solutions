import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if any health issue is critical
    if hypertension > 0.03 or intoxication > 0.05 or alertness < 0.5:
        return 3
    # Sleep if alertness is too low or it's been a long time since sleeping
    if alertness < 0.7 or time_since_slept > 6:
        return 3
    # Drink coffee if slightly low on alertness but other metrics are safe
    if alertness < 0.75 and hypertension < 0.02 and intoxication < 0.03:
        return 1
    # Use beer to relax slightly if under stress but work is manageable
    if 0.7 <= alertness <= 0.8 and 0.02 < hypertension <= 0.03 and intoxication < 0.04:
        return 2
    # Otherwise, just work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)