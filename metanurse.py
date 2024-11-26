import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize addressing severe health alerts
    if hypertension > 0.05 or intoxication > 0.05:
        return 3
    if time_since_slept > 5:
        return 3

    # Enhance productivity while moderately managing caffeine
    if alertness < 0.7:
        if hypertension < 0.03 and intoxication < 0.03:
            return 1

    # Continue working if alertness is high and health is stable
    if alertness > 0.75:
        if hypertension < 0.02 and intoxication < 0.02:
            return 0

    # Ensure rest if productivity parameters trigger significantly
    if work_done > 20 and time_elapsed > 50:
        return 3

    # Default action: Sleep to maintain health
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)