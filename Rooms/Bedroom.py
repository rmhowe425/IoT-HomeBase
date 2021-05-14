from Rooms.Room import Room

'''
    Represents a bedroom that contains IoT devices 
    specific to a bedroom.
    
    Inherits from the Room abstract class. 
'''
class Bedroom(Room):

    '''
        Constructor for the Bedroom class.
    '''
    def __init__(self):
        self.location = 'Bedroom'
