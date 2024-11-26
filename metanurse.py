import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep when conditions are concerning health
    if (
        alertness < 0.2
        or hypertension > 0.08
        or intoxication > 0.05
        or time_since_slept >= 5.0
    ):
        return 3
    
    # Prefer working with coffee when alertness is moderate but not very low
    if 0.2 <= alertness < 0.5 and hypertension < 0.06 and intoxication < 0.04:
        return 1

    # Work when conditions are optimal for productivity
    if alertness >= 0.6 and hypertension < 0.04 and intoxication <= 0.03:
        return 0

    # Drink beer and work as last resort when alertness is low and work_done is minimal
    if work_done < 0.02 and intoxication < 0.02 and alertness < 0.3:
        return 2
        
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)