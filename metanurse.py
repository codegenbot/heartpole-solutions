import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Updated logic to improve decision-making:
    # Prioritize sleep if alertness is very low or not slept for a long while
    if alertness < 0.6 or time_since_slept > 8:
        return 3
    # Avoid increasing hypertension and intoxication
    if hypertension > 0.5:
        return 3
    if intoxication >= 0.3:
        return 3
    # Increase alertness with coffee only if it's low and safe to do so
    if alertness < 0.7 and hypertension <= 0.4 and intoxication < 0.2:
        return 1
    # Default to working if health parameters are satisfactory
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)