import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health by checking alertness and hypertension first
    if alertness < 0.6 or time_since_slept > 6 or hypertension > 0.4:
        return 3  # Sleep
    if intoxication > 0.2:
        return 3  # Sleep to recover
    # Use coffee only when alertness is a bit low but health is fine
    if alertness < 0.8 and hypertension < 0.2 and intoxication < 0.1:
        return 1  # Coffee and work
    if 0.1 <= intoxication < 0.2 and alertness > 0.7: 
        return 2  # Beer and work (use cautiously)
    return 0  # Work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)