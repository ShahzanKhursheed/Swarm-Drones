import time
from dronekit import VehicleMode


class SwarmManager:

    def __init__(self, drones):

        self.drones = drones
        self.leader = drones[0]
        self.followers = drones[1:]


    def wait_armable(self):

        for d in self.drones:

            while not d.is_armable:

                print("Waiting armable")

                time.sleep(1)


    def set_guided(self):

        for d in self.drones:

            d.mode = VehicleMode("GUIDED")

        time.sleep(3)


    def arm_all(self):

        for d in self.drones:

            d.armed = True

        for d in self.drones:

            while not d.armed:

                time.sleep(0.5)


    def takeoff_all(self, alt):

        print("Takeoff start")

        for d in self.drones:

            d.simple_takeoff(alt)
            time.sleep(2)

        # wait until ALL reach altitude

        while True:

            ok = True

            for d in self.drones:

                h = d.location.global_relative_frame.alt

                print("ALT:", h)

                if h < alt * 0.9:
                    ok = False

            if ok:
                break

            time.sleep(1)

        print("All at altitude")


    def rtl_all(self):

        for d in self.drones:

            d.mode = VehicleMode("RTL")
