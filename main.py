from Helpers.module_selection import ModuleSelection
from Modules.message_sender import send_message
from Helpers.case_print import cprint as cprint
import os
from dotenv import load_dotenv
import inquirer

load_dotenv()
Token = os.getenv('DISCORD_TOKEN')

if Token is None:
    raise ValueError("DISCORD_TOKEN not found in environment variables.")

selected = ModuleSelection()

# Message Spammer Start

if selected == "Message Spammer":

    questions = [
        inquirer.Text('ChannelID', message="Which Channel ID would you like to send this message to?"),
        inquirer.Text('Message', message="What's the message you'd like to send?"),
    ]
    answers = inquirer.prompt(questions)

    if not answers['ChannelID'] or not answers['Message']:
        raise ValueError("ChannelID and Message must be provided.")
    response = send_message(answers['ChannelID'], answers['Message'], Token)
    if response.status_code == 200:
        cprint("G", "Message sent successfully.")
    else:
        cprint("R", f"Failed to send message. Status code: {response.status_code}")

# Message Spammer End