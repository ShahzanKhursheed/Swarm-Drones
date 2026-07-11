import time


class SwarmLoop:

    def __init__(self, swarm, formation):

        self.swarm = swarm
        self.formation = formation


    def update(self):

        leader = self.swarm.leader

        leader_pos = leader.location.global_relative_frame

        offsets = self.formation.get_offsets()

        followers = self.swarm.followers

        for i in range(len(followers)):

            drone = followers[i]

            off = offsets[i]

            target = drone.location.global_relative_frame

            target.lat = leader_pos.lat + off[0] * 0.00001
            target.lon = leader_pos.lon + off[1] * 0.00001
            target.alt = leader_pos.alt

            drone.simple_goto(target)


    def run(self):

        print("Swarm loop")

        while True:

            self.update()

            time.sleep(1.0)
