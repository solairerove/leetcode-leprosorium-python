import collections


# O(1) time || O(n) space
class UndergroundSystem:

    def __init__(self):
        self.check_in_map = {}  # id -> [station_time, time]
        self.route_total_time = collections.defaultdict(int)
        self.route_count = collections.defaultdict(int)

    def check_in(self, id: int, station_name: str, t: int) -> None:
        self.check_in_map[id] = [station_name, t]

    def check_out(self, id: int, station_name: str, t: int) -> None:
        check_in = self.check_in_map.pop(id)
        route_name = (check_in[0], station_name)

        self.route_total_time[route_name] += t - check_in[1]
        self.route_count[route_name] += 1

    def get_average_time(self, start_station: str, end_station: str) -> float:
        route_name = (start_station, end_station)

        return self.route_total_time[route_name] / self.route_count[route_name]
