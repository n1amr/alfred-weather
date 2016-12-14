from alfred.modules.api.a_base_module import ABaseModule
from alfred.modules.api.a_heading import AHeading

class AlfredWeather(ABaseModule):
    def callback(self):
        pass

    def construct_view(self):
        h1 = AHeading(1, "Hello")
        h2 = AHeading(2, "Bye")

        self.add_component(h1)
        self.add_component(h2)
