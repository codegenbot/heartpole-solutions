import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for high-risk health indicators
    if hypertension > 0.03 or intoxication > 0.08:
        return 3

    # Adjusted sleep condition: Prioritize sleeping enough
    if time_since_slept > 5 or alertness < 0.5:
        return 3

    # Use beer only if moderate hypertension and low intoxication
    if 0.02 < hypertension <= 0.03 and intoxication < 0.04 and alertness > 0.6:
        return 2

    # Use coffee for low alertness if other health indicators are low
    if 0.45 <= alertness < 0.6 and hypertension < 0.02 and intoxication < 0.04:
        return 1

    # Default action to work if all health indicators are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)