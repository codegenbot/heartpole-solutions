import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.7 or intoxication > 0.5:
        return 3  # High health risk indicators, sleep
    if time_since_slept > 6 and alertness < 0.5:
        return 3  # More frequent sleep if alertness is low
    if alertness < 0.4 and hypertension < 0.5:
        return 1  # Drink coffee if alertness is relatively low and hypertension is safe
    if work_done < 0.7 and alertness >= 0.5:
        return 0  # Work if alertness is sufficient and work is not yet 70% complete
    return 0  # Default to working if no conditions are triggered

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)