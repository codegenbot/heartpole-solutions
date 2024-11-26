import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health by lowering hypertension and intoxication thresholds
    if hypertension > 0.03 or intoxication > 0.04:
        return 3
    if time_since_slept > 4:
        return 3

    # Adjusted caffeine management with a more relaxed approach
    if alertness < 0.65:
        if hypertension < 0.025 and intoxication < 0.025:
            return 1

    # Optimize working conditions and manage alertness more conservatively
    if alertness > 0.7:
        if hypertension < 0.015 and intoxication < 0.015:
            return 0

    # Make sure sleep is chosen if work done exceeds early limit significantly
    if work_done > 15 and time_elapsed > 40:
        return 3

    # Default: Sleep
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)