import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if health indicators are high or alertness is very low
    if (
        hypertension > 0.25 
        or intoxication > 0.25 
        or time_since_slept > 5
        or alertness < 0.3
    ):
        return 3
    # Drink coffee to boost alertness only if time_since_slept is low and under thresholds
    if alertness < 0.5 and hypertension < 0.15 and intoxication < 0.1 and time_since_slept <= 3:
        return 1
    # Work if alertness is high and health indicators are very low
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 0
    # Drink beer only if work done is high, but ensure health is maintained
    if (
        work_done > 8
        and alertness > 0.4
        and intoxication < 0.1
        and hypertension < 0.1
        and time_since_slept <= 3
    ):
        return 2
    # Default to sleeping to recover
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)