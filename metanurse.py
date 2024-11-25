import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or hypertension > 0.15 or intoxication > 0.1 or time_since_slept >= 6:
        return 3  # Prioritize sleep for severe conditions
    if alertness < 0.6 and hypertension < 0.07 and intoxication < 0.03:
        return 1  # Coffee if reasonably safe
    if alertness < 0.5 and hypertension < 0.05 and intoxication < 0.02:
        return 2  # Beer as a last resort if conditions are ideal
    return 0  # Just work when conditions are safe

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)