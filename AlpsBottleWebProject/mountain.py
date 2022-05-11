class MountainCondition:
    name: str
    description: str
    image_link: str

    def __init__(self, name: str, description: str, image_link: str):
        self.name = name
        self.description = description
        self.image_link = image_link
