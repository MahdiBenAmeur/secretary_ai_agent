
# Secretary AI Assistant 📖

## Project Overview 🌟
This project implements an AI-driven secretarial assistant designed to manage and schedule appointments for a medical office. The assistant interacts with users to create, check, suggest, and confirm appointments using pre-defined commands and functions within a controlled conversational flow.

## Project Structure 🏗️
- `functions.py`: Contains all backend logic for managing appointments, including creating, confirming, and checking the availability of appointments.
- `hard_coded.py` and `secretary_ai_agent.py`: Implements the conversational AI logic using the `ollama` library, handling the flow of appointment scheduling based on user interactions.

## Requirements 📋
- Python 3.x
- Ollama Library
- Datetime Module

## Setup 🔧
1. Ensure Python 3.x is installed on your system.
2. Install the `ollama` library if not already installed:
   ```
   pip install ollama
   ```
3. Clone this repository or download the scripts to your local machine.

## Usage 🚀
Run `hard_coded.py` or `secretary_ai_agent.py` in your terminal:
```
python hard_coded.py
```
or
```
python secretary_ai_agent.py
```
Follow the on-screen prompts to interact with the secretary AI. You can make, check, suggest, and confirm appointments using specific commands detailed in the prompts.

## Functionality 🔍
- **Make Appointment**: Create a new appointment entry. 📅
- **Check Availability**: Check if a specific date is available for an appointment. ✔️
- **Suggest Appointment**: Suggest the next available date if the requested date is not available. 📆
- **Confirm Appointment**: Confirm a previously created appointment. ✅

## Example 💬
Here's how you might interact with the system:
```
user: I need to book an appointment.
bot: Please provide the ID, name, and date for the appointment.
user: <Enter details>
bot: Appointment created and confirmed for [details].
```

## Contributing 🤝
Feel free to fork this project, make improvements, and submit pull requests. All contributions are welcome!
