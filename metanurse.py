import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep only when serious concerns exist
    if alertness < 0.4 or hypertension > 0.7 or intoxication >= 0.4 or time_since_slept > 6:
        return 3  # Prioritize sleep if feeling unwell

    # Use coffee if alertness needs boosting without high hypertension
    if 0.4 <= alertness < 0.6 and hypertension < 0.6 and intoxication <= 0.2:
        return 1  # Drink coffee and work

    # Opt for just working when health is stable
    if alertness >= 0.6 and hypertension <= 0.5 and intoxication < 0.1:
        return 0  # Just work

    # Limit beer usage to very good health periods
    if intoxication < 0.15 and hypertension < 0.3:
        return 2  # Drink beer and work

    return 3  # Default to sleep if no other option feels safe

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)