import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if any severe health condition is present
    if hypertension > 0.10 or intoxication > 0.04 or time_since_slept > 6:
        return 3
    # Opt for coffee if alertness deteriorates moderately and health is stable
    if alertness < 0.8 and hypertension < 0.08 and intoxication < 0.02:
        return 1
    # Reduce dependency on coffee as work progresses or conditions are good
    if work_done > 0.7 or alertness > 0.75:
        return 0
    # If none of the above, continue working to maximize productivity
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)