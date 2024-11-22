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

    if hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 12:
        print(3)  # sleep
    elif alertness < 0.4 and time_since_slept < 6:
        print(1)  # drink coffee and work
    elif intoxication < 0.1:
        print(0)  # just work
    else:
        print(2)  # drink beer and work