import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep with stricter health conditions
    if hypertension > 0.18 or intoxication > 0.09 or alertness < 0.6 or time_since_slept > 6:
        return 3
    # Use coffee more conservatively to avoid health impacts
    if alertness < 0.8 and hypertension < 0.12 and intoxication < 0.05:
        return 1
    # Default to work if conditions are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)