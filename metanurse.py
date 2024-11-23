import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if health metrics are bad
    if hypertension > 0.65 or intoxication > 0.35:
        return 3
    # If lacking sleep severely
    if time_since_slept > 10:
        return 3
    # Maintain balance between work and alertness
    if alertness < 0.3:
        return 3 if time_elapsed >= 4 else 1
    # Periodic rests if not done recently
    if time_since_slept > 8:
        return 3
    # Encourage productivity with moderate alertness
    if work_done < 0.4 and alertness > 0.6:
        return 0
    if time_since_slept > 4 and alertness < 0.6:
        return 1
    # Default work action
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)