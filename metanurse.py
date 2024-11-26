import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is very low or sleep is overdue
    if alertness < 0.4 or time_since_slept > 7.0:
        return 3

    # Avoid worsening health; moderate hypertension and intoxication require rest
    if hypertension > 0.05 or intoxication > 0.05:
        return 3

    # Use coffee to boost alertness if it's not too high, ensure hypertension is low
    if 0.4 <= alertness < 0.6 and hypertension <= 0.02:
        return 1

    # Use beer when alertness is good and intoxication is very low
    if alertness >= 0.7 and intoxication <= 0.01:
        return 2

    # Default to working if alertness is sufficient and health is stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)