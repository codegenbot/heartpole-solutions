import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 6:
        return 3  # Prioritize sleep
    if alertness < 0.35:
        return 3  # Sleep if alertness is low
    if alertness < 0.55 and hypertension <= 0.65 and intoxication <= 0.2:
        return 1  # Use coffee cautiously
    if alertness >= 0.7 and hypertension <= 0.5 and intoxication <= 0.1:
        return 0  # Work when conditions are ideal
    return 3  # Default to sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)