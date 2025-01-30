from datetime import datetime, timedelta

appointement = {}
comfirmed_appointements = {}

def make_appointment(id: str, name: str, date: str):
    """
    Registers an appointment by storing it in the 'appointment' dictionary.

    Parameters:
    - id (str): The unique identifier for the appointment.
    - name (str): The name of the person for whom the appointment is being made.
    - date (str): The date of the appointment in 'YYYY-MM-DD' format.

    Returns:
    - list: A list containing the name and the datetime.date object of the appointment.
    """
    appointement[id] = [name, datetime.strptime(date, "%Y-%m-%d").date()]
    return appointement[id]

def suggest_appointement():
    """
    Suggests the next available date for an appointment by finding the maximum date among confirmed appointments
    and adding one day to it.

    Returns:
    - datetime.date: The suggested date for the next available appointment.
    """
    dates = [datetime.strptime("2025-01-28", "%Y-%m-%d").date()]
    for appointment in comfirmed_appointements.values():
        dates.append(appointment[1])
    max_date = max(dates) + timedelta(days=1)
    return max_date

def check_availability(date: str):
    """
    Checks the availability of a given date for appointments.

    Parameters:
    - date (str): The date to check availability for, in 'YYYY-MM-DD' format.

    Returns:
    - bool: True if the date is available, False otherwise.
    """
    date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    for booked_date in comfirmed_appointements.values():
        if date_obj == booked_date[1]:
            return False
    return True

def confirm_appointment(id: str):
    """
    Confirms an appointment if it's available and moves it from the 'appointment' dictionary
    to the 'confirmed_appointments' dictionary.

    Parameters:
    - id (str): The unique identifier for the appointment.

    Returns:
    - bool: True if the appointment is confirmed, False if the appointment is not available or doesn't exist.
    """
    if id in appointement:
        if check_availability(str(appointement[id][1])):
            comfirmed_appointements[id] = appointement[id]
            del appointement[id]
            return True
        else:
            return False
    return False
