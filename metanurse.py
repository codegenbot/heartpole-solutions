import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is significantly low or health markers indicate risk
    if alertness < 0.5 or hypertension > 0.2 or intoxication > 0.1 or time_since_slept > 8:
        return 3  # Sleep

    # Favor coffee if alertness is slightly low and other conditions are safe
    if alertness < 0.7 and hypertension <= 0.15 and intoxication <= 0.05:
        return 1  # Drink coffee and work

    # Choose neutral work when conditions are close to safe thresholds
    if 0.7 <= alertness < 0.8 and hypertension <= 0.1 and intoxication <= 0.05:
        return 0  # Just work

    # Avoid any additions if intoxication is creeping up
    if intoxication > 0.05:
        return 0  # Just work

    # Consider beer only if overall health is optimal and alertness is above average
    if alertness >= 0.8 and hypertension <= 0.1 and intoxication <= 0.03:
        return 2  # Drink beer and work

    # Default to just work as a safe fallback
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)