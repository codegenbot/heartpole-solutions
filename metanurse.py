import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any critical indicators are present or approaching critical
    if alertness < 0.4 or hypertension > 0.8 or intoxication > 0.5 or time_since_slept > 10:
        return 3  # Need to sleep

    # Prioritize work if conditions are favorable
    if alertness > 0.8 and hypertension < 0.6 and intoxication < 0.3:
        return 0  # Just work

    # Use coffee to maintain productivity if alertness is compromised but not critical
    if 0.4 <= alertness < 0.8 and hypertension < 0.7 and intoxication < 0.3:
        return 1  # Coffee and work

    # Default back to sleep if ambiguity or multiple moderate conditions present
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)