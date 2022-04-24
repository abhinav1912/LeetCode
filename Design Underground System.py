class UndergroundSystem:

    def __init__(self):
        self.stations = {}
        self.customers = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        x = self.customers[id]
        time = t - x[1]
        if x[0] not in self.stations:
            self.stations[x[0]] = {stationName: (time, 1)}
        elif stationName not in self.stations[x[0]]:
            self.stations[x[0]][stationName] = (time, 1)
        else:
            y = self.stations[x[0]][stationName]
            self.stations[x[0]][stationName] = (y[0] + time, y[1] + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        x = self.stations[startStation][endStation]
        return x[0]/x[1]
