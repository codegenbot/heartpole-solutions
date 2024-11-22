import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.7 or intoxication > 0.5:
        return 3  # prioritize sleep for high health risks
    if time_since_slept > 16:
        return 3  # ensure sleep after too long awake
    if alertness < 0.4:
        if alertness < 0.2 or time_since_slept > 12:
            return 3  # sleep if very low alertness or long since slept
        return 1  # drink coffee and work if low alertness
    if time_since_slept >= 8 and alertness > 0.5:
        return 0  # just work if rested enough
    return 0  # default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)