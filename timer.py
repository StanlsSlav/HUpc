import datetime


class Timer:
    def __init__(self, num_of_secs: int):
        self.num_of_secs = num_of_secs

    def tick(self):
        m, s = divmod(self.num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(f"{datetime.datetime.now().second.real} -- {min_sec_format}")
        self.num_of_secs -= 1
