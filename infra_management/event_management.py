# Problem Statement: Use the existing Event class by adding an instance attribute to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date

#Expected Outcome: Completion of the Event class with the participant tracking attribute and methods to add participants and retrieve the count.
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count
    
# Creating instances of Event

event1 = Event("Music Festival", "2022-07-15")

# Adding participants

event1.add_participant()
event1.add_participant()
event1.add_participant()

# Retrieving participant count

print(event1.get_participant_count())


