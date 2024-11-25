import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when alertness is critically low or sleep deprivation is high
    if alertness < 0.3 or time_since_slept > 6 or hypertension > 0.15 or intoxication > 0.05:
        return 3

    # Use coffee when alertness is too low for work but health allows it
    if alertness < 0.5 and hypertension <= 0.1 and intoxication < 0.03:
        return 1

    # Limit beer consumption to extremely rare conditions to avoid intoxication
    if alertness > 0.8 and hypertension < 0.05 and intoxication < 0.01 and work_done < 0.1:
        return 2

    # Default to working only in optimal health conditions
    if alertness >= 0.6 and hypertension <= 0.1 and intoxication < 0.02:
        return 0

    # Fallback to resting or routine work if none of above are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)