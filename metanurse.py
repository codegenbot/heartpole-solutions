import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if health indicators are critical or if not alert enough
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 7:
        return 3  # Sleep if any health indicator is high or alertness low

    # Use coffee strategically, with stricter conditions
    if 0.3 <= alertness < 0.7 and hypertension <= 0.5 and intoxication <= 0.2:
        return 1  # Coffee if slight alertness boost needed, but with strict health requirements

    # Work when conditions are optimal for productivity without health risk
    if alertness >= 0.7 and hypertension <= 0.4 and intoxication <= 0.1:
        return 0  # Just work

    # Beer under stringent conditions
    if intoxication < 0.2 and hypertension < 0.5:
        return 2  # Beer can be an option, but only when risks are very low

    # Default to sleep as a safe fallback
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)