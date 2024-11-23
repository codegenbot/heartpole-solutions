import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep based on severe health risks
    if hypertension > 0.30 or intoxication > 0.15 or time_since_slept > 8:
        return 3  # Sleep

    # Sleep if alertness is too low
    if alertness < 0.6:
        return 3  # Sleep

    # Use coffee to boost alertness and prioritize health
    if 0.6 <= alertness < 0.75 and hypertension <= 0.20 and intoxication <= 0.10:
        return 1  # Drink coffee and work

    # Work when health parameters are optimized and coffee isn't needed
    return 0  # Just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)