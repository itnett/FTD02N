python
def generate_meeting_invitation(meeting_date="2024-07-01", meeting_time="10:00", meeting_place="Room 101"):
    """
    Generer en møteinnkalling.

    Parametere:
    meeting_date (str): Dato for møtet (standardverdi "2024-07-01")
    meeting_time (str): Tid for møtet (standardverdi "10:00")
    meeting_place (str): Sted for møtet (standardverdi "Room 101")

    Returnerer:
    str: Møteinnkalling
    """
    invitation = (
        f"Meeting Invitation\n"
        f"Date: {meeting_date}\n"
        f"Time: {meeting_time}\n"
        f"Place: {meeting_place}\n\n"
        f"Agenda:\n"
        f"1. Opening and welcome\n"
        f"2. Approval of the agenda\n"
        f"3. Approval of the previous meeting minutes\n"
        f"4. Discussion points\n"
        f"5. Any other business\n"
        f"6. Conclusion and next meeting\n\n"
        f"Please confirm your attendance.\n"
    )
    return invitation

# Eksempel på bruk
invitation = generate_meeting_invitation()
print(invitation)