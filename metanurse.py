import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping when health risks are noticeable
    if hypertension > 0.1 or intoxication > 0.1:
        return 3

    # Sleep if sleep deprived over a moderate threshold
    if time_since_slept > 5:
        return 3

    # Coffee when slightly low on alertness, avoiding risks
    if alertness < 0.6 and hypertension < 0.08 and intoxication < 0.08:
        return 1

    # Work if well-balanced and reasonably alert
    if alertness >= 0.6 and hypertension < 0.05 and intoxication < 0.05:
        return 0

    # Avoid beer; it should be very context-specific due to relaxation intent
    if work_done > 20 and alertness > 0.65 and intoxication < 0.03:
        return 2

    # Default to working, but check health regularly
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)