import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.4:
        return 3  # Sleep when health indicators are high
    if time_since_slept > 6 and alertness < 0.5:
        return 3  # Prevent cumulative alertness drop by sleeping earlier
    if alertness < 0.4 and hypertension < 0.4:
        return 1  # Use coffee if alertness is low and hypertension is not too high
    if work_done < 0.7:  # Aim for higher work completion
        return 0 if alertness > 0.5 else 1  # Work or use coffee based on alertness
    return 0  # Default action is to just work if conditions are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)