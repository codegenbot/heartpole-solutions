import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical health concerns: Sleep if any serious issues are present
    if time_since_slept > 7 or hypertension >= 0.5 or intoxication >= 0.3:
        return 3
    # Sleep if alertness is low or moderate sleep deprivation
    if alertness < 0.6 or time_since_slept > 5:
        return 3
    # Use coffee if alertness is medium and health is manageable
    if alertness < 0.75 and hypertension < 0.3 and intoxication < 0.2:
        return 1
    # Safe to work: High alertness and health is good
    if alertness >= 0.75 and hypertension < 0.2 and intoxication < 0.1:
        return 0
    # Default to working sober or taking a break if intoxicated
    return 0 if intoxication >= 0.2 else 2

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)