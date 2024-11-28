import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        raise TypeError("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for number, attendee in enumerate(attendees, start=1):
        invitation = template.replace("{name}", str(attendee.get("name", "N/A")))
        invitation = invitation.replace("{event_title}", str(attendee.get("event_title", "N/A")))
        invitation = invitation.replace("{event_date}", str(attendee.get("event_date", "N/A")))
        invitation = invitation.replace("{event_location}", str(attendee.get("event_location", "N/A")))
    
        filename = f"output_{number}.txt"

        if  os.path.exists(filename):
            print(f"Warning: File {filename} already exists.")
    
        try:
            with open(filename, 'w') as file:
                file.write(invitation)
        except Exception as error:
            print(f"Error: Could not write to file {filename}. Exception: {error}")