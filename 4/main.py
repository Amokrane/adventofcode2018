import sys
import re
import operator

def select_guard_and_minute(input_file):

    lines = [line.rstrip('\n') for line in open(input_file)]
    lines.sort()


    begin_shit_regex = "\[\d\d\d\d-\d\d-\d\d\s\d\d\:(\d\d)\]\sGuard\s#(\d+)\sbegins shift"
    falls_asleep_regex = "\[\d\d\d\d-\d\d-\d\d\s\d\d\:(\d\d)\]\sfalls asleep"
    wakes_up_regex = "\[\d\d\d\d-\d\d-\d\d\s\d\d\:(\d\d)\]\swakes up"

    guards_schedule = {} # key: guard_id, value: number of minutes asleep
    guards_schedule_segments = {}
    
    current_guard = -1
    last_guard_slept_at_minute = -1
    current_day_index = -1

    for line in lines:
        match_begin_shift = re.match(begin_shit_regex, line)
        match_falls_asleep = re.match(falls_asleep_regex, line)
        match_wakes_up = re.match(wakes_up_regex, line)

        if match_begin_shift:
            current_guard = match_begin_shift.group(2)
            current_day_index += 1
        
        if match_falls_asleep:
            last_guard_slept_at_minute = int(match_falls_asleep.group(1)) 
        
        if match_wakes_up:
            sleep_duration_in_minutes = int(match_wakes_up.group(1)) - last_guard_slept_at_minute

            for i in range(sleep_duration_in_minutes):
                guards_schedule[current_guard] = guards_schedule.get(current_guard, 0) + sleep_duration_in_minutes 

            guards_schedule_segments.setdefault(current_guard, []).append((last_guard_slept_at_minute, int(match_wakes_up.group(1))))


    sorted_guards_schedule = sorted(guards_schedule.items(), key=operator.itemgetter(1))
    print("The sleepy guard is ", sorted_guards_schedule[-1][0])
    sleepy_guard = sorted_guards_schedule[-1][0]

    sleepy_guard_emom = [0 for x in range(60)]
    liste = guards_schedule_segments[sleepy_guard]

    for l in liste:
        for i in range(l[1] - l[0]):
            sleepy_guard_emom[i + l[0]] += 1
        
    max = 0    
    index = 0
    for i in range(60):
        if (sleepy_guard_emom[i] > max):
            index = i
            max = sleepy_guard_emom[i]

    print("The sleepiest guard is mostly awake at min: ", index)

    # part 2
    guard_sleepiest_at_any_min = -1
    sleepiest_min = -1
    any_max = 0
    for key, value in guards_schedule_segments.iteritems():
        emom = [0 for x in range(60)]
        for t in value:
            for i in range(t[1] - t[0]):
                emom[i + t[0]] += 1
        
        for e in range(60):
            if (emom[e] > any_max):
                guard_sleepiest_at_any_min = key
                any_max = emom[e]
                sleepiest_min = e
    
    print(guard_sleepiest_at_any_min, sleepiest_min)

if __name__ == "__main__":
    select_guard_and_minute(sys.argv[1])

