import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.35 or intoxication > 0.09 or alertness < 0.65 or time_since_slept > 4.5:
        return 3  # Sleep necessary to reset and recover
    if alertness < 0.75 and hypertension < 0.18:
        return 1  # Use coffee to boost alertness safely
    if 0.03 < intoxication < 0.08 and hypertension < 0.22 and alertness > 0.72:
        return 2  # Use beer only under very safe conditions
    return 0  # Default to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)