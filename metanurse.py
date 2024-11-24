import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep sooner to manage alertness and health
    if time_since_slept > 6 or hypertension >= 0.75 or intoxication >= 0.65 or alertness < 0.4:
        return 3
    # Opt for coffee if alertness is low and other conditions are moderately safe
    if alertness < 0.5 and hypertension < 0.5 and intoxication < 0.4:
        return 1
    # Default to work if alertness is sufficiently high and health metrics are safe
    if alertness >= 0.7 and hypertension < 0.25 and intoxication < 0.2:
        return 0
    # Use beer strategically in specific balanced health states
    return 2 if intoxication < 0.4 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)