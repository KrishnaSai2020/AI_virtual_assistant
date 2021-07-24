import Skills
from modules.User_Input import get_user_command
from modules.AI_Speech import speak


def run_commands(statement):
    user_satisfied = False
    if 'wikipedia' in statement:
        Skills.search_wikipedia(statement)

    if 'youtube' in statement:
        Skills.youtube()

    speak('Is this what you wanted?')
    statement = get_user_command().lower()
    if 'yes' or 'yep' in statement:
        user_satisfied = True

    return user_satisfied
