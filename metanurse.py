import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any health indicator hits dangerous levels
    if hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 10:
        return 3  # Sleep

    # Preemptively sleep to prevent health stretch when nearing danger thresholds
    if 8 <= time_since_slept and (hypertension > 0.5 or intoxication > 0.3):
        return 3  # Sleep

    # Use coffee effectively as a productivity boost under safe conditions
    if alertness < 0.6 and hypertension < 0.3 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Always aim to work when alertness and health conditions are sufficient
    if 0.6 <= alertness <= 0.85 and hypertension < 0.4 and intoxication < 0.3:
        return 0  # Just work

    # Preventively sleep as a deterrent to deferred stress accumulation
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)