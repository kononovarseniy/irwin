from irwin.Materials.Material import Material


class SiliconMaterial(Material):
    def __init__(self):
        super().__init__()
        print(f'In ctor of Silicon Material')