import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep to avoid health issues
    if hypertension > 0.4 or intoxication > 0.2 or alertness < 0.3 or time_since_slept > 12:
        return 3

    # Optimal condition to work without stimulants
    if alertness >= 0.8 and hypertension <= 0.2 and intoxication == 0.0:
        return 0

    # Use coffee if alertness is low but hypertension is under control
    if 0.3 <= alertness < 0.5 and hypertension <= 0.25:
        return 1

    # Avoid using beer altogether unless it's guaranteed no intoxication
    if 0.25 <= alertness < 0.35 and intoxication == 0.0:
        return 2

    # Default to working if conditions are safe
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)