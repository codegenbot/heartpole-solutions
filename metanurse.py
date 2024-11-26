import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if health or rest indicators are problematic
    if alertness < 0.6 or hypertension > 0.03 or intoxication > 0.02 or time_since_slept >= 3:
        return 3
    
    # Drink coffee if alertness is not optimal but health metrics allow
    if 0.6 <= alertness < 0.7 and hypertension < 0.025 and intoxication < 0.015:
        return 1

    # Just work if alertness is high and health indicators are stable
    if alertness >= 0.7 and hypertension < 0.02 and intoxication < 0.01:
        return 0

    # Beer should generally not be used, except when productivity is almost at a dead stop and no health risk
    if work_done < 0.005 and intoxication <= 0.01 and alertness < 0.2:
        return 2

    # Default to working if conditions slightly mismatch
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)