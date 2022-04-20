from DecoratorsGuide.decorators import timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])


waste_some_time(1)
waste_some_time(999)
