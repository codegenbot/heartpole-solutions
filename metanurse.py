import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health: Sleep if hypertension or intoxication is high
    if hypertension > 0.6 or intoxication > 0.4:
        return 3
    # Sleep if severely sleep-deprived or alertness is very low
    if time_since_slept > 14 or alertness < 0.3:
        return 3
    # Drink coffee and work if moderate alertness is low
    if alertness < 0.5 and hypertension < 0.3:
        return 1
    # If alertness and health indicators allow, just work
    if alertness >= 0.6 and hypertension <= 0.3 and intoxication <= 0.2:
        return 0
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)