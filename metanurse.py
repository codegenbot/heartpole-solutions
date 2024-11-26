import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if sleep deprived or high hypertension/intoxication is detected
    if time_since_slept >= 5 or hypertension > 0.01 or intoxication > 0.1:
        return 3
    # Use coffee only if alertness is low and it's been a reasonable time since sleep
    if alertness < 0.4 and time_since_slept < 4:
        return 1
    # Regular work if alertness and health parameters are adequate
    if 0.6 <= alertness and hypertension < 0.008 and intoxication < 0.05:
        return 0
    # If caffeine is not advisable, safest work with caution
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)