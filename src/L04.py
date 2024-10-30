class Stadium:
    def __init__(self, viewers=100, name="Example", light=100, public_numeric=100, public_string="Example"):
        self.__viewers = viewers
        self.__name = name
        self.__light = light
        self.public_numeric = public_numeric
        self.public_string = public_string

    def get_viewers(self):
        return self.__viewers

    def get_name(self):
        return self.__name

    def get_light(self):
        return self.__light

    def __repr__(self):
        return (f"Stadium: name={self.__name}, viewers={self.__viewers}, light={self.__light}, "
                f"Public Number: {self.public_numeric}, Public String: {self.public_string}")

    def __str__(self):
        return (f"Stadium(name={self.__name}, viewers={self.__viewers}, light={self.__light}, "
                f"Public Number: {self.public_numeric}, Public String: {self.public_string}")

    def __del__(self):
        print(f"Stadium'{self.__name}' has been deleted.")

def main():
    stadium1 = Stadium(10000, "Stadium1", 1500, 25000, "Football")
    stadium2 = Stadium(30000, "Stadium2", 1200, 18000, "Basketball")
    stadium3 = Stadium(40000, "Stadium3", 1800, 22000, "Tennis")
    stadium4 = Stadium()

    print(repr(stadium1))
    print(repr(stadium2))
    print(repr(stadium3))
    print(repr(stadium4))
    print(stadium1)
    print(stadium2)
    print(stadium3)
    print(stadium4)

if __name__ == "__main__":
    main()
