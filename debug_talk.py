import random


class DebugTalk:
    @staticmethod
    def get_random_str(min_number, max_number):
        return str(random.randint(int(min_number), int(max_number)))

    @staticmethod
    def get_random_num(min_num, max_num):
        return random.randint(int(min_num), int(max_num))
