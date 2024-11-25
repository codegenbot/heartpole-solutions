import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 12:
        return 3  # Requires sleep urgently
    if alertness < 0.6 and hypertension < 0.5 and intoxication < 0.2:
        return 1  # Drink coffee safely when alertness is low
    if alertness >= 0.7 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work if all conditions are stable
    if intoxication >= 0.2 and intoxication < 0.4:
        return 2  # Use beer to mellow manageable intoxication
    return 0  # Default action is to just work if no specific condition is met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)