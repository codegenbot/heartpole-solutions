import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize rest if health risks are high
    if hypertension >= 0.25 or intoxication >= 0.1 or time_since_slept >= 7:
        return 3  # Sleep

    # Rest if alertness is low or it's been a while since sleeping
    if alertness < 0.6 or time_since_slept >= 6:
        return 3  # Sleep

    # Use coffee conservatively to boost alertness
    if 0.6 <= alertness < 0.75 and hypertension < 0.15 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Use beer only when alertness is high but within safe boundaries
    if 0.75 <= alertness < 0.85 and intoxication < 0.05:
        return 2  # Drink beer and work

    # Work efficiently without substances when alertness is adequate
    return 0  # Just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)