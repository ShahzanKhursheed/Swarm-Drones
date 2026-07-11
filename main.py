import time

from drone_connection import connect_drone
from swarm_manager import SwarmManager
from formation_manager import FormationManager
from swarm_loop import SwarmLoop


connections = [

    "udp:127.0.0.1:14550",
    "udp:127.0.0.1:14560",
    "udp:127.0.0.1:14570",

]


time.sleep(10)

drones = []

for c in connections:

    d = connect_drone(c)

    drones.append(d)


swarm = SwarmManager(drones)

swarm.wait_armable()

swarm.set_guided()

swarm.arm_all()
time.sleep(10)
swarm.takeoff_all(5)

time.sleep(5)
formation = FormationManager()

loop = SwarmLoop(swarm, formation)

loop.run()


swarm.rtl_all()

swarm.wait_landed()

print("DONE")
