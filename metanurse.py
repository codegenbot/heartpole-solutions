import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        hypertension > 0.5
        or intoxication > 0.5
        or alertness < 0.5
        or time_since_slept > 9
    ):
        return 3  # Sleep for minimizing health risks and regaining alertness

    if alertness < 0.65:
        if hypertension < 0.6 and intoxication < 0.3:
            return 1  # Drink coffee to boost alertness safely
        else:
            return 3  # Sleep if stimulant usage is unsafe

    if alertness >= 0.8 and hypertension < 0.4:
        return 0  # Work efficiently

    return 2  # Cautiously use beer when alertness needs slight improvement


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)