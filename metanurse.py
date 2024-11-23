import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for critical health states or very low alertness
    if hypertension > 0.5 or intoxication > 0.3 or alertness < 0.5:
        return 3  # Sleep

    # Use coffee to improve alertness if alertness is moderately low
    if alertness < 0.7 and time_since_slept <= 12 and work_done < 0.7:
        return 1  # Drink coffee and work

    # Encourage just work if alertness and health metrics are optimal
    if alertness >= 0.7 and hypertension < 0.3 and intoxication < 0.2:
        return 0  # Just work

    # Sleep if alertness is low during later hours
    if time_elapsed >= 16 and alertness < 0.6:
        return 3  # Sleep

    # Default to monitoring situation closely with sleep
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)