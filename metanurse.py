import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep more aggressively under higher stress or low alertness
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 9:
        return 3

    # Encourage coffee use when alertness dips moderately but only if health metrics allow
    if 0.5 <= alertness < 0.7 and hypertension <= 0.4 and intoxication <= 0.15:
        return 1

    # Default to working if all conditions are favorable
    if alertness >= 0.7 and hypertension <= 0.2 and intoxication <= 0.05:
        return 0

    # Encourage sleep slightly more when workload reaches a critical mass even if some conditions don't trigger it
    if work_done >= 0.75:
        return 3

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)