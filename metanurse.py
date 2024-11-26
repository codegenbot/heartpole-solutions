import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health concerns
    if hypertension >= 0.05 or intoxication >= 0.15:
        return 3  # Must sleep if health is at risk

    # Ensure adequate rest
    if alertness < 0.3 or time_since_slept >= 8:
        return 3  # Sleep to recover alertness

    # Consider caffeine only if safe and productive
    if 0.3 <= alertness < 0.6 and hypertension < 0.02:
        return 1  # Drink coffee and work to boost alertness

    # Work if conditions are optimal
    return 0  # Default: just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)