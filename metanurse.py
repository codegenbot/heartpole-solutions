import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep in case of high hypertension or intoxication
    if hypertension > 0.6 or intoxication > 0.4:
        return 3
    # Ensure regular sleep if too long awake
    if time_since_slept > 12:
        return 3
    # Use coffee to boost low alertness but only if time since sleep is reasonable
    if alertness < 0.4 and time_since_slept <= 10:
        return 1
    # Avoid risky actions if alertness and work_done suggest fatigue; ensure respite
    if work_done < 0.5 or alertness < 0.5:
        return 3
    # Keep working if alertness is adequate and work needs to be done
    if work_done < 0.8 and alertness > 0.5:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)