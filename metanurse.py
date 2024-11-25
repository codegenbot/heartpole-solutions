import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if either alertness is too low, hypertension or intoxication is too high or long time since last sleep
    if time_since_slept > 6 or alertness < 0.6 or hypertension > 0.08 or intoxication > 0.1:
        return 3

    # Use coffee very sparingly: only if slightly less alert while maintaining safe health thresholds
    if alertness < 0.7 and hypertension < 0.05 and intoxication < 0.03:
        return 1

    # Optimal work: high alertness and stable health
    if alertness >= 0.75 and hypertension < 0.05 and intoxication < 0.02:
        return 0

    # Default: conservatively just work, to not overuse coffee or any high-risk actions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)