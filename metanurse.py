import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for recovery if any critical health parameter is high
    if time_since_slept > 8 or hypertension > 0.7 or intoxication > 0.5:
        return 3
    # Drink coffee to increase alertness if it's safe
    if alertness < 0.6 and hypertension < 0.5 and intoxication <= 0.3:
        return 1
    # Just work if alertness is adequate and intoxication low
    if alertness >= 0.6 and intoxication <= 0.3:
        return 0
    # Safest default action is to continue working
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)