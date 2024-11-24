import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if severely sleep-deprived or if health indicators are critical
    if time_since_slept > 8 or hypertension >= 0.4 or intoxication >= 0.3:
        return 3
    # Rest if alertness is low and sleep deprivation is not severe 
    if alertness < 0.5:
        return 3
    # Use coffee if alertness is medium and health is manageable
    if alertness < 0.7 and hypertension < 0.25 and intoxication < 0.15:
        return 1
    # Safe to work: High alertness and stable health indicators
    if alertness >= 0.8 and hypertension < 0.15 and intoxication < 0.1:
        return 0
    # Prefer sober work or a light stimulant if conditions are borderline 
    return 0 if alertness >= 0.6 else 2

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)