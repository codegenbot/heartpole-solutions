import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if significant health issues
    if hypertension > 0.35 or intoxication > 0.25:
        return 3
    
    # Opt to sleep if time awake is excessive or alertness is critically low
    if time_since_slept > 10 or alertness < 0.3:
        return 3

    # Use coffee only if hypertension is manageable
    if alertness < 0.6 and time_elapsed < 8 and hypertension <= 0.2:
        return 1

    # Work if metrics are within reasonable health thresholds
    if alertness >= 0.45 and hypertension <= 0.2 and intoxication <= 0.15 and work_done < 0.75:
        return 0

    # Prioritize sleep in case of diminishing alertness later in the day
    if time_elapsed > 10 and alertness < 0.35:
        return 3

    # Default to work if unsure 
    return 0 if alertness >= 0.4 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)