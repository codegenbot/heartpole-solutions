import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or time_since_slept >= 5 or intoxication > 0.10 or hypertension >= 0.03:
        return 3  # Sleep to sufficiently recover health and alertness
    if alertness < 0.6:
        return 1  # Coffee boosts productivity when alertness needs an increase
    if alertness >= 0.7 and intoxication < 0.05 and hypertension < 0.02:
        return 0  # Prefer work when health is stable and alertness is high
    return 2  # Use beer to moderate alertness while balancing slightly raised health indicators

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)