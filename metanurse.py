import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize critical health conditions immediately with rest
    if hypertension > 0.3 or intoxication > 0.2 or alertness < 0.5:
        return 3
    # Need rest after extended periods without sleep
    if time_since_slept > 4:
        return 3
    # Use coffee to boost alertness if under fatigue but health indicators are stable
    if alertness < 0.75 and hypertension < 0.2 and intoxication < 0.1:
        return 1
    # Stimulate by drinking beer if very alert and relaxed for minor productivity gain
    if alertness >= 0.85 and hypertension <= 0.1 and intoxication < 0.02 and work_done < 0.3:
        return 2
    # Default to productive work otherwise
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)