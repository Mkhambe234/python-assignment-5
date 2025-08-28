# Base Class
class CrochetProject:
    def __init__(self, name, yarn_type, hook_size):
        self.name = name            # e.g. "Granny Square Blanket"
        self.yarn_type = yarn_type  # e.g. "Cotton", "Acrylic"
        self.hook_size = hook_size  # e.g. "4.5mm"
        self.stitches = 0           # Start with 0 stitches

    def start_project(self):
        return f"Starting {self.name} using {self.yarn_type} yarn with a {self.hook_size} hook."

    def add_stitches(self, number):
        self.stitches += number
        return f"Added {number} stitches. Total stitches: {self.stitches}"

    def finish_project(self):
        return f"Finished {self.name} with {self.stitches} stitches!"


# Subclass: Blanket
class Blanket(CrochetProject):
    def __init__(self, name, yarn_type, hook_size, size):
        super().__init__(name, yarn_type, hook_size)
        self.size = size  # e.g. "Queen", "Baby"

    def project_details(self):
        return f"{self.name} is a {self.size} size blanket."


# Subclass: Scarf
class Scarf(CrochetProject):
    def __init__(self, name, yarn_type, hook_size, length):
        super().__init__(name, yarn_type, hook_size)
        self.length = length  # in cm

    def measure(self):
        return f"{self.name} scarf will be {self.length} cm long."


# Subclass: Amigurumi (crochet toys)
class Amigurumi(CrochetProject):
    def __init__(self, name, yarn_type, hook_size, character):
        super().__init__(name, yarn_type, hook_size)
        self.character = character  # e.g. "Bear", "Bunny"

    def describe(self):
        return f"{self.name} is an amigurumi of a {self.character}."


# --- Testing the Crochet Classes ---
project1 = CrochetProject("Basic Granny Square", "Cotton", "4.5mm")
print(project1.start_project())
print(project1.add_stitches(120))
print(project1.finish_project())

blanket = Blanket("Rainbow Blanket", "Acrylic", "5mm", "Queen")
print(blanket.start_project())
print(blanket.project_details())

scarf = Scarf("Winter Warmth", "Wool", "6mm", 150)
print(scarf.start_project())
print(scarf.measure())

toy = Amigurumi("Cute Bunny", "Cotton", "3mm", "Bunny")
print(toy.start_project())
print(toy.describe())
