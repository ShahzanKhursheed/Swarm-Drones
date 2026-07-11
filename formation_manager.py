import math


class FormationManager:

    def __init__(self):

        radius = 10

        self.offsets = [

            (radius, 0),

            (-radius/2, radius * 0.86),

            (-radius/2, -radius * 0.86),

        ]


    def get_offsets(self):

        return self.offsets
