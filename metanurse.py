import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if signs of severe fatigue or poor health
    if alertness < 0.4 or hypertension >= 0.03 or intoxication > 0.15 or time_since_slept >= 7:
        return 3
    # Consider coffee when alertness is moderate and health flags are low
    if 0.4 <= alertness < 0.7 and hypertension < 0.02 and intoxication < 0.1 and time_since_slept < 5:
        return 1
    # Prefer working if highly alert and health indicators are favorable
    if alertness >= 0.7 and hypertension < 0.02 and intoxication < 0.1:
        return 0
    # Use relaxation (beer) sparingly and conditionally
    if intoxication >= 0.1 and hypertension < 0.025:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)