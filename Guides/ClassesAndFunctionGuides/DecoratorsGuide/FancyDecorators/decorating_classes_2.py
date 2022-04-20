from DecoratorsGuide.decorators import debug, timer


# can decorate class methods with any function
# can also decorate the entire class to give the class itself properties
class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])


tw = TimeWaster(1000)
tw.waste_time(999)
