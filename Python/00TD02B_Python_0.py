python
def generate_meeting_invitation(meeting_date="2024-09-01", meeting_time="10:00", meeting_place="Room 101"):
    """
    Generate a meeting invitation.
    
    Parameters:
    meeting_date (str): Date of the meeting.
    meeting_time (str): Time of the meeting.
    meeting_place (str): Place of the meeting.
    
    Returns:
    str: Meeting invitation.
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
    print(invitation)
    return invitation

# Example usage
generate_meeting_invitation()