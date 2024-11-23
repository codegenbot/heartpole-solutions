import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if hypertension or intoxication is critically high
    if hypertension > 0.6 or intoxication > 0.4:
        return 3
    # Sleep if not alert enough and it has been a long time since last sleep
    if alertness < 0.35 or time_since_slept > 10:
        return 3
    # Use coffee to enhance alertness if below threshold and hypertension is manageable
    if alertness < 0.65 and hypertension < 0.35:
        return 1
    # Default action is to work if conditions are optimal
    if alertness >= 0.55 and hypertension <= 0.3 and intoxication <= 0.25:
        return 0
    # Sleep if too much time has elapsed and other conditions aren't met
    if time_elapsed >= 14:
        return 3
    # Default fallback action
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)