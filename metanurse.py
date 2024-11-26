import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for high hypertension or intoxication or if not slept for a long time
    if hypertension > 0.012 or intoxication > 0.035 or time_since_slept > 8:
        return 3

    # Ensure adequate alertness, and use coffee for focus when reasonably alert but not ideal
    if alertness < 0.5:
        return 3
    elif 0.5 <= alertness < 0.7 and hypertension < 0.01 and intoxication < 0.02:
        return 1

    # Use beer strategically to boost productivity when health is very stable
    elif 0.7 <= alertness < 0.85 and hypertension < 0.006 and intoxication < 0.01:
        return 2

    # Default to working if alertness and health are optimal or near optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)