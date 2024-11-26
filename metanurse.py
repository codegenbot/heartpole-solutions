import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Adjust health thresholds and prioritize health safety
    if hypertension > 0.02 or intoxication > 0.2:
        return 3  # sleep immediately to counteract high risk
    if time_since_slept >= 4:
        return 3  # ensure sleep after extended periods
    if alertness < 0.3:
        return 3  # sleep prioritized for very low alertness
    if 0.3 <= alertness < 0.5:
        if hypertension < 0.01 and intoxication < 0.1:
            return 1  # boost alertness safely with coffee
        else:
            return 3  # sleep if health risks exist
    return 0  # prioritize work when all conditions are favorable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)