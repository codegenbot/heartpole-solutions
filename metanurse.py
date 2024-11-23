import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.7 or intoxication > 0.5:
        return 3  # Immediate sleep due to high health risks.
    if time_since_slept > 6:
        return 3  # Prioritize sleep if awake for too long.
    if alertness < 0.4:
        return 3  # Sleep due to low alertness.
    if alertness < 0.5 and hypertension < 0.4:
        return 1  # Coffee only if it can boost low alertness safely.
    if work_done < 0.9 and alertness >= 0.6:
        return 0  # Encourage work if high alertness and moderate work done.
    return 1  # Default to drinking coffee and working if neither requires immediate attention.

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)