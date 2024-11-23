import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for critical alertness or health issues
    if alertness < 0.3 or time_since_slept > 16 or hypertension > 0.6 or intoxication > 0.5:
        return 3

    # Sleep if alertness is low and awake time is high
    if time_since_slept > 12 and alertness < 0.5:
        return 3

    # Use coffee to boost alertness when health metrics are manageable
    if alertness < 0.7 and hypertension <= 0.3 and intoxication <= 0.2 and time_elapsed < 14:
        return 1

    # Use beer if alertness is moderate and health is stable
    if alertness >= 0.5 and intoxication <= 0.1 and hypertension <= 0.2 and work_done < 0.6:
        return 2

    # Default to work if health is stable and alertness is maintained
    return 0 if alertness >= 0.5 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)