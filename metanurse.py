import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep with stricter health checks
    if time_since_slept > 5 or alertness < 0.5 or intoxication > 0.15:
        return 3

    # Use coffee if slightly tired but health can support it
    if alertness < 0.65 and hypertension < 0.07 and intoxication < 0.05:
        return 1

    # Optimal to work if high alertness and stable health
    if alertness >= 0.7 and hypertension < 0.05 and intoxication < 0.04:
        return 0

    # Avoid beer more, but use if nearly no work done and very low alertness
    if work_done < 0.01 and intoxication <= 0.02 and alertness < 0.4:
        return 2

    # Default to just work conservatively using coffee sparingly
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)