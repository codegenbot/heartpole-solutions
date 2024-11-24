import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Adjust Sleep Conditions
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Sleep if necessary

    # Improve Coffee Strategy
    if 0.3 <= alertness < 0.5 and hypertension <= 0.5 and intoxication <= 0.3:
        return 1  # Coffee when more productivity is beneficial

    # Moderate Work Decision
    if alertness >= 0.5 and hypertension <= 0.4 and intoxication <= 0.2:
        return 0  # Sustain working under optimal conditions

    # Reassess Beer Decisions
    return 2 if intoxication <= 0.2 and hypertension <= 0.5 else 3  # Use beer if beneficial, else sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)