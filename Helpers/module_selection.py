import inquirer
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Function to select module
def ModuleSelection():
    questions = [
        inquirer.List(
            'module',
            message="Which module would you like to run?",
            choices=['Message Spammer'],
        ),
    ]
    return inquirer.prompt(questions)['module']
