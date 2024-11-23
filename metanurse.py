import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for critical alertness or health issues
    if alertness < 0.3 or hypertension > 0.5 or intoxication > 0.4 or time_since_slept > 16:
        return 3

    # Sleep if alertness is low and awake time is high
    if time_since_slept > 12 and alertness < 0.5:
        return 3

    # Drink coffee to maintain alertness, avoiding high hypertension or intoxication
    if alertness < 0.7 and hypertension <= 0.3 and intoxication <= 0.2:
        return 1

    # Work normally if alertness is adequate and health is stable
    if alertness >= 0.5 and hypertension <= 0.2 and intoxication <= 0.15:
        return 0

    # Drink beer and work if slightly tired and ready for boosts, but health is stable
    if alertness >= 0.4 and time_elapsed < 16 and hypertension <= 0.25 and intoxication <= 0.1:
        return 2

    # Default to work if none of the above conditions met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)