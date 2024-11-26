import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Strict health risk management
    if hypertension > 0.04 or intoxication > 0.05:
        return 3
    if time_since_slept > 5:
        return 3

    # Adjusted caffeine management
    if alertness < 0.6:
        if hypertension < 0.03 and intoxication < 0.03:
            return 1

    # Optimize work conditions with slightly relaxed alertness
    if alertness > 0.65 and hypertension < 0.02 and intoxication < 0.02:
        return 0

    # Make sure sleep is chosen if exhaustion tends to stack over time
    if work_done > 20 and time_elapsed > 50:
        return 3

    # Default: Sleep
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)