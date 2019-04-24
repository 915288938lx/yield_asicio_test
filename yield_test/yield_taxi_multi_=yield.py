from collections import namedtuple

Event = namedtuple('Event', 'time proc action')

def taxi_process(ident, trips, start_time=0):  # <1>
    """Yield to simulator issuing event at each state change"""
    time = yield Event(start_time, ident, 'leave garage')  # <2>
    for i in range(trips):  # <3>
        time = yield Event(time, ident, 'pick up passenger')  # <4>
        time = yield Event(time, ident, 'drop off passenger')  # <5>

    yield Event(time, ident, 'going home')  # <6>
    # end of taxi process # <7>
# END TAXI_PROCESS


taxi = taxi_process(ident = 13, trips= 15, start_time=0)
next(taxi)
taxi.send(5)



taxi.send(10)
taxi.send(15)
taxi.send(34)
taxi.send(40)
taxi.send(47)
taxi.send(55)
taxi.send(65)
taxi.send(78)
taxi.send(90)
taxi.send(100)
taxi.send(110)
taxi.send(132)
taxi.send(145)
taxi.send(178)
taxi.send(200)
taxi.send(245)
taxi.send(298)