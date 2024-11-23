import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.6 or intoxication > 0.3:
        return 3  # prioritize sleep more strictly for health risks
    if time_since_slept > 16 or alertness < 0.2:
        return 3  # ensure sleep when overly tired or time since sleep is excessive
    if alertness < 0.4:
        return 1  # use coffee to boost alertness
    if alertness > 0.5 and time_since_slept >= 7:
        return 0  # work if alert and recently slept
    return 0  # default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)