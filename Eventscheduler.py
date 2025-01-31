# Event Scheduler with Conflict Detection

# Define the Event class to store event details
class Event:
    def __init__(self, name, start_time, end_time, description=""):
        # Initialize event details: name, start and end times, and optional description
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.description = description

    def __str__(self):
        # This helps to print the event in a human-friendly format
        return f'"{self.name}", Start: "{self.start_time}", End: "{self.end_time}"'

# Function to check if two events overlap
def check_conflict(event1, event2):
    # Convert the times to 24-hour format for comparison
    if (event1.start_time < event2.end_time) and (event1.end_time > event2.start_time):
        return True
    return False

# Function to sort events by their start time
def sort_events(events):
    return sorted(events, key=lambda x: x.start_time)

# Function to display events in sorted order and detect conflicts
def display_schedule(events):
    sorted_events = sort_events(events)
    print("Sorted Schedule:")
    for i, event in enumerate(sorted_events):
        print(f"{i + 1}. {event}")

    print("\nConflicting Events:")
    conflicts = []
    
    # Check for conflicts between events
    for i in range(len(sorted_events)):
        for j in range(i + 1, len(sorted_events)):
            if check_conflict(sorted_events[i], sorted_events[j]):
                conflicts.append((sorted_events[i], sorted_events[j]))

    # Display conflicts, if any
    if conflicts:
        for conflict in conflicts:
            print(f'1. "{conflict[0].name}" and "{conflict[1].name}"')
    else:
        print("No conflicts detected!")

# Suggest alternative time slots for resolving conflicts
def suggest_resolution(events):
    # Example of a simple approach to resolving conflicts
    print("\nSuggested Resolutions:")
    for conflict in conflicts:
        event_to_reschedule = conflict[1]
        # Simple suggestion: Reschedule the second event to the next available time slot
        new_start_time = event_to_reschedule.end_time
        new_end_time = new_start_time + (event_to_reschedule.end_time - event_to_reschedule.start_time)
        print(f'1. Reschedule "{event_to_reschedule.name}" to Start: "{new_start_time}", End: "{new_end_time}"')

# Sample Events
events = [
    Event("Meeting A", 9.0, 10.5),
    Event("Workshop B", 10.0, 11.5),
    Event("Lunch Break", 12.0, 13.0),
    Event("Presentation C", 10.5, 12.0)
]

# Call the function to display the sorted schedule and detect conflicts
display_schedule(events)

# Call the function to suggest resolutions
suggest_resolution(events)
