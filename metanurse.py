import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 16:
        return 3  # sleep if health is critically affected
    if alertness < 0.2:
        return 3  # sleep if alertness is critically low
    if alertness < 0.5 and time_since_slept > 12:
        return 1  # drink coffee to maintain productivity
    if hypertension < 0.25 and intoxication < 0.3 and alertness > 0.6:
        return 0  # just work if health is stable
    return 1  # default to coffee and work if none of the above conditions are met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)