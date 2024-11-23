import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.45 or intoxication > 0.45 or time_since_slept > 8:
        return 3  # Sleep with stricter thresholds to prevent health issues
    if alertness < 0.5 and hypertension < 0.25 and intoxication < 0.2:
        return 1  # Use coffee more often when close to needing sleep but under safe conditions
    if alertness >= 0.7 and hypertension < 0.25 and intoxication < 0.1:
        return 0  # Continue working when in good condition, prefers productivity
    if work_done > 12 and alertness > 0.4 and intoxication < 0.15 and hypertension < 0.25:
        return 2  # More liberal beer option to provide some downtime
    return 3  # Default to sleep if uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)