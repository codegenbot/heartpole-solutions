import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any critical threshold is crossed
    if (
        alertness < 0.6
        or time_since_slept >= 6
        or intoxication > 0.1
        or hypertension > 0.07
    ):
        return 3  # Sleep to recover

    # Drink coffee if alertness is low but ensure hypertension is controlled
    if 0.6 <= alertness < 0.75 and hypertension < 0.04:
        return 1  # Coffee to boost alertness moderately

    # Avoid beer unless all health indicators and alertness are optimal
    if alertness > 0.85 and intoxication == 0.0 and hypertension < 0.01 and time_since_slept < 2:
        return 2  # Beer in optimal state, sparingly

    # Default to work if health indicators are stable and productivity remains high
    if time_elapsed < 24:  # Assuming 24 hours is a work day cap for productivity concern
        return 0

    return 3  # Force rest if worked too long regardless of conditions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)