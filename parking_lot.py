from collections import OrderedDict
from random import random, randint

MAX_PARKINGS_PER_FLOOR = 7


class Vehicle(object):
    def __init__(self, vid, floor_id=None, parking_lot_id=None):
        self.vid = vid
        self.floor_id = floor_id
        self.parking_lot_id = parking_lot_id

    def __str__(self):
        return self.vid


class ParkingLot(object):
    def __init__(self):
        self.parking_lot_odict = OrderedDict()
        for x in range(5):
            floor = "FL{0}".format(x)
            self.parking_lot_odict[floor] = []

    def vehicle_entry(self, vehicle):
        for floor in self.parking_lot_odict.keys():
            vehicle.floor_id = floor
            if len(self.parking_lot_odict[floor]) == 0:
                vehicle.parking_lot_id = 0
                self.parking_lot_odict[floor].append(vehicle)
                break
            else:
                for parking_lot_id in range(MAX_PARKINGS_PER_FLOOR):
                    if 0 <= parking_lot_id < len(self.parking_lot_odict[floor]):
                        if self.parking_lot_odict[floor][parking_lot_id] == 'EMPTY':
                            vehicle.parking_lot_id = parking_lot_id
                            self.parking_lot_odict[floor][parking_lot_id] = vehicle
                            break
                        else:
                            continue
                    else:
                        vehicle.parking_lot_id = parking_lot_id
                        self.parking_lot_odict[floor].append(vehicle)
                        break

            if vehicle.parking_lot_id != None:
                break


    def vehicle_exit(self, vehicle):
        self.parking_lot_odict[vehicle.floor_id][vehicle.parking_lot_id] = 'EMPTY'


    def display_all(self):
        for x in self.parking_lot_odict.keys():
            print("{0} => {1}".format(x, [str(x) for x in self.parking_lot_odict[x]]))


if __name__ == '__main__':
    parking_lot = ParkingLot()

    # Add a few vehicles
    for x in range(15):
        vehicle = Vehicle(vid="MH12JC{0}".format(randint(1, 5000)))
        parking_lot.vehicle_entry(vehicle)
    parking_lot.display_all()

    # remove few vehicles
    vehicle_to_exit = parking_lot.parking_lot_odict['FL0'][2]
    parking_lot.vehicle_exit(vehicle_to_exit)
    print("Removed vehicle: {0}".format(vehicle_to_exit.vid))

    vehicle_to_exit = parking_lot.parking_lot_odict['FL0'][4]
    parking_lot.vehicle_exit(vehicle_to_exit)
    print("Removed vehicle: {0}".format(vehicle_to_exit.vid))

    parking_lot.display_all()

    # Add a new vehicle
    vehicle = Vehicle(vid="MH12JC{0}".format(randint(1, 5000)))
    print("Adding new vehicle {0}".format(vehicle.vid))
    parking_lot.vehicle_entry(vehicle)
    parking_lot.display_all()

    vehicle = Vehicle(vid="MH12JC{0}".format(randint(1, 5000)))
    print("Adding new vehicle {0}".format(vehicle.vid))
    parking_lot.vehicle_entry(vehicle)
    parking_lot.display_all()