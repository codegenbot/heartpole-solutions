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

    if hypertension > 0.8 or intoxication > 0.6 or time_since_slept > 14:
        print(3)  # sleep
    elif alertness < 0.3 and time_since_slept < 8 and hypertension < 0.6:
        print(1)  # drink coffee and work
    elif intoxication < 0.2:
        print(0)  # just work
    elif intoxication < 0.5 and hypertension < 0.7:
        print(2)  # drink beer and work
    else:
        print(3)  # default to cautious sleep if conditions are not met