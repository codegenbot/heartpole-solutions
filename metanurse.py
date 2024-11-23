import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep conditions based on health risks and lack of alertness
    if hypertension > 0.7 or intoxication > 0.6 or alertness < 0.3:
        return 3  # Prioritize sleep for recovery

    if time_since_slept > 6:
        return 3  # Regular rest cycle if awake for a while

    # Coffee strategy for alertness boost without high hypertension
    if alertness < 0.5 and hypertension < 0.4:
        return 1  # Coffee intake when nearly optimal conditions allow

    # Beer for hypertension only if intoxication and alertness allow
    if hypertension > 0.5 and intoxication < 0.3 and alertness > 0.4:
        return 2  # Carefully manage hypertension with beer

    # Optimal work condition
    if alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.3:
        return 0  # Continue working under ideal conditions

    return 0  # Default action is to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)