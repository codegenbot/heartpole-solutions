import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any health indicator is in a concerning state
    if alertness < 0.4 or hypertension > 0.2 or intoxication > 0.2 or time_since_slept > 5:
        return 3

    # Work if good alertness and safe health levels
    if alertness >= 0.6 and hypertension <= 0.15 and intoxication <= 0.1:
        return 0

    # Use coffee if alertness is declining, keeping health in check
    if alertness < 0.6 and hypertension <= 0.2 and intoxication <= 0.15:
        return 1

    # Occasionally take a break, considering low work done and mild state
    if work_done < 0.3 and alertness > 0.5 and hypertension < 0.15:
        return 2

    # Default to sleep if conditions aren't optimal or understood
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)