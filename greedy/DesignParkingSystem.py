class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [big, medium, small]

    # O(1) time || O(1) space
    def add_car(self, car_type: int) -> bool:
        self.parking[car_type - 1] -= 1

        return self.parking[car_type - 1] >= 0
