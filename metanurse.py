import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for health recovery when critical
    if hypertension > 0.20 or intoxication > 0.20 or time_since_slept > 4.5:
        return 3
    # Drink coffee to boost low alertness while maintaining safe health levels
    if alertness < 0.5 and hypertension < 0.10 and intoxication < 0.05:
        return 1
    # Work if alertness is adequate and health indicators are healthy
    if alertness >= 0.7 and hypertension < 0.10 and intoxication < 0.05:
        return 0
    # Allow beer as a reward mechanism when work is significantly done
    if work_done > 7 and alertness > 0.5 and intoxication < 0.10:
        return 2
    # Default to sleeping if unsure about health or productivity
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)