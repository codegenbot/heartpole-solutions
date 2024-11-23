import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep conditions based on safety and overall health balance
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept >= 6:
        return 3  # Prioritize sleep for recovery

    # Coffee for alertness with more lenient hypertension condition
    if alertness < 0.6 and hypertension < 0.5:
        return 1  # Use coffee to boost alertness when needed

    # Beer for managing controllable hypertension levels
    if hypertension > 0.5 and intoxication < 0.3:
        return 2  # Reduce stress with beer, if intoxication allows

    # Optimal working conditions refined
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.3:
        return 0  # Work without distractions

    return 0  # Default action remains to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)