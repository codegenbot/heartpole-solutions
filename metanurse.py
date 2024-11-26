def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health checks first
    if hypertension >= 0.015 or intoxication >= 0.08:
        return 3  # sleep if there's a risk of worsening hypertension or intoxication
    # Prioritize sleep if alertness is too low
    if alertness < 0.55 or time_since_slept >= 6:
        return 3  # rest when alertness is getting low or a long time has passed since last sleep
    # Coffee to work efficiently given safe health scores
    if alertness < 0.75 and hypertension < 0.010 and intoxication < 0.04:
        return 1  # caffeine is a buffer to alertness when it's not optimal but health parameters are safe
    return 0  # default to just working if everything is optimal

import sys
for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)