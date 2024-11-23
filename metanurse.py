import sys

for line in sys.stdin:
    (
        alertness,
        hypertension,
        intoxication,
        time_since_slept,
        time_elapsed,
        work_done,
    ) = map(float, line.split())

    if hypertension > 0.5 or intoxication > 0.3 or time_since_slept > 16:
        print(3)  # sleep
    elif alertness < 0.3 or hypertension > 0.4:
        print(3)  # sleep
    elif alertness < 0.5 and time_since_slept < 14:
        print(1)  # drink coffee and work
    elif alertness < 0.7 and 0.1 <= intoxication <= 0.3:
        print(2)  # drink beer and work
    elif alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.2:
        print(0)  # just work
    else:
        print(3)  # sleep