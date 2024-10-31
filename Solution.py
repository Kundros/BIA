import abc

from Animation import Animation


class Solution(abc.ABC):
    def __init__(self, function, lower_bound, upper_bound, dimensions, name="algorithm"):
        self.function = function
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.dimensions = dimensions
        self.name = name
        self.results = []

    ### Used to execute search algorithm
    @abc.abstractmethod
    def execute(self, *args):
        ...

    ### Takes results after execute, creates animated gif with history progress of finding global minimum
    def animate_result(self, segments = 60, wired = False):
        animation = Animation(
            self.results,
            self.lower_bound,
            self.upper_bound,
            segments,
            self.function,
            self.name,
            wire_width=.25,
            wired=wired,
            rotation_deg_per_frame=2,
            duration=25
        )

        animation.animate_3d()

    def animate_heatmap(self, segments = 150):
        animation = Animation(
            self.results,
            self.lower_bound,
            self.upper_bound,
            segments,
            self.function,
            self.name,
            wired=False,
            duration=50
        )

        animation.animate_heatmap()

    def animate_path(self, segments = 150):
        animation = Animation(
            self.results,
            self.lower_bound,
            self.upper_bound,
            segments,
            self.function,
            self.name,
            wired=False,
            duration=200
        )

        animation.animate_path()