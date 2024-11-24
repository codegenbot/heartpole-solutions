import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping when health risks are high
    if hypertension > 0.15 or intoxication > 0.15:
        return 3

    # Sleep if significantly sleep deprived
    if time_since_slept > 6:
        return 3

    # Use coffee only if alertness is too low and no health risks present
    if alertness < 0.5 and hypertension < 0.1 and intoxication < 0.1:
        return 1

    # Prefer working if alert and balanced
    if alertness >= 0.5 and hypertension < 0.05 and intoxication < 0.05:
        return 0

    # Consider beer for slight relaxation during high productivity, avoiding high intoxication
    if work_done > 15 and alertness > 0.6 and intoxication < 0.05:
        return 2

    # Default to working
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)