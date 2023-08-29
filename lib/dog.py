class Dog:
    def __init__(self, name, breed="Labrado "):
        self._name = name
        self._breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        approved_breeds = ["Mutt", "Labrador", "Golden Retriever", "German Shepherd"]
        if value in approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    def sit(self):
        print("The dog is sitting.")
