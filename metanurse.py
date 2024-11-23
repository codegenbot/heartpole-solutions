import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any critical condition persists
    if alertness < 0.4 or hypertension > 0.6 or intoxication > 0.5 or time_since_slept > 10:
        return 3  # Sleep for recovery

    # Use coffee strategically to lift productivity when safe
    if 0.4 <= alertness < 0.6 and hypertension < 0.25 and intoxication < 0.3:
        return 1  # Use coffee to boost alertness cautiously

    # Conduct work when in a healthy, suitable state
    if alertness >= 0.6 and hypertension < 0.35 and intoxication < 0.3:
        return 0  # Favor productivity when in optimal condition

    # Consider beer only for moderate stress without intoxication risk
    if 0.4 <= hypertension < 0.5 and intoxication < 0.2:
        return 2  # Use beer selectively for stress management

    # Default action under any remaining uncertain conditions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)