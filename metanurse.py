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

    if hypertension > 0.5 or intoxication > 0.5 or time_since_slept >= 10:
        print(3)  # sleep
    elif alertness < 0.6 and hypertension < 0.3 and time_since_slept < 7:
        print(1)  # drink coffee and work
    elif alertness >= 0.7 and intoxication < 0.2:
        print(0)  # just work
    else:
        print(2)  # drink beer and work