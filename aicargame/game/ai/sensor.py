from pygame import Vector2

class Sensor:
    sensors: list['Sensor']

    def __init__(self):
        self._position = None
        Sensor.sensors.append(self)

    def update(self, vector: Vector2):
        self._position = vector 

    @property
    def position(self):
        return self._position

    def relposition(self, sensor: 'Sensor'):
        if (isinstance(sensor.position, Vector2) 
            and isinstance(self.position, Vector2)):
            return self.position - sensor.position
        else:
            return None
    
    def distance(self, sensor: 'Sensor'):
        pass

    def delete(self):
        Sensor.sensors.remove(self)
