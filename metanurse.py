import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.7 or intoxication > 0.5:
        return 3  # Sleep to prioritize health
    if time_since_slept > 8 and alertness < 0.5:
        return 3  # Sleep when alertness is low and haven't slept enough
    if alertness < 0.3 and hypertension < 0.4:
        return 1  # Increase alertness with coffee if hypertension is acceptable
    if work_done < 0.6:  # Prioritize work completion over sleeping too soon
        return 0 if alertness > 0.6 else 1  # Work or use coffee to boost alertness
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)