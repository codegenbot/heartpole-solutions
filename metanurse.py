import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If the need for sleep is very critical, prioritize sleep
    if time_since_slept > 15 or alertness < 0.35 or hypertension > 0.75 or intoxication > 0.5:
        return 3  # Need sleep to maintain health

    # If alertness is good and health allows it, just work
    if alertness >= 0.65 and hypertension < 0.6 and intoxication < 0.4:
        return 0  # Just work when health conditions are safe

    # If alertness is moderate, consider coffee if health indicators allow
    if 0.4 <= alertness < 0.65 and hypertension < 0.7 and intoxication < 0.5:
        return 1  # Drink coffee to enhance alertness

    # Default to sleep to ensure health isn't compromised
    return 3  # Default to sleep to mitigate potential health risks

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)