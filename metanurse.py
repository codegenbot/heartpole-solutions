import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.15 or intoxication > 0.08 or time_since_slept > 4:
        return 3  # Sleep

    if alertness < 0.85:
        return 3  # Sleep to ensure alertness

    if 0.85 <= alertness < 0.95 and hypertension < 0.1 and intoxication < 0.05:
        return 1  # Drink coffee and work

    if hypertension < 0.05 and intoxication < 0.03 and alertness >= 0.95:
        return 0  # Work is preferred over beer if alert and healthy

    return 0  # Default to just work if all conditions are favorable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)