import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if hypertension or intoxication is high, or if not slept enough
    if hypertension > 0.7 or intoxication > 0.5 or time_since_slept >= 8:
        return 3
    # Sleep if alertness is critically low
    if alertness < 0.3:
        return 3
    # Coffee can be used to boost alertness effectively when needed
    if alertness < 0.6 and hypertension < 0.6 and intoxication <= 0.2:
        return 1
    # If conditions are optimal, prioritize working
    if alertness >= 0.7 and hypertension < 0.5 and intoxication <= 0.1:
        return 0
    # Optionally have a beer to stabilize, but be cautious with usage
    if hypertension < 0.55 and intoxication < 0.2:
        return 2
    # Default action is to sleep to ensure recovery
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)