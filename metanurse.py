import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if hypertension or intoxication levels are moderate
    if hypertension > 0.25 or intoxication > 0.2:
        return 3
    
    # Opt to sleep based on low alertness or long awake period
    if time_since_slept > 6 or alertness < 0.35:
        return 3

    # Use coffee cautiously; only when alertness is low and early in the day
    if alertness < 0.5 and time_elapsed < 5 and hypertension < 0.15:
        return 1

    # Be very cautious with beer
    if intoxication <= 0.05 and alertness < 0.45 and work_done < 0.4:
        return 2

    # Work if all health metrics are stable and productivity is moderate
    if (
        alertness >= 0.4
        and hypertension < 0.15
        and intoxication <= 0.05
        and work_done < 0.8
    ):
        return 0

    # Default: at late hours or low alertness, rest
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)