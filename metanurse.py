import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # If critical health conditions exist, prioritize sleep
    if alertness < 0.5 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 8:
        return 3  # Sleep

    # Optimal condition just for work without stimulants
    if alertness > 0.75 and hypertension < 0.6 and intoxication < 0.2:
        return 0  # Just work

    # Use coffee to boost productivity only if alertness is moderately low
    if 0.5 <= alertness <= 0.75 and hypertension < 0.65 and intoxication < 0.25:
        return 1  # Coffee and work

    # Use beer only if alertness is critically low and hypertension is controlled
    if alertness < 0.5 and intoxication < 0.2 and hypertension < 0.55:
        return 2  # Beer and work

    # When in doubt or unpredictability, prefer sleep
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)