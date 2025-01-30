from ollama import chat
from functions import *
import ollama


secretary_prompt="""
you are a secretary working for a doctor , your job is to book appointments and book appointments only , do not talk about anything else , unless its to suggest an appoitment based on the scheduale.
an appoitment is caracterased by CIN (which is the id) , name and date (in the "%Y-%m-%d" format ) , when talking to a client you should get those informations

at your hands you have theses tools:
-make_appointment to create an appointment
-check_availability check if the date is available
-suggest_appointement to suggest a valid appointment in case of check availability fails
-confirm_appointment to confirm an appointment

the work flow should look like : checkavailability , makeappointment then confirmappointment
when you need to use a tool you will need to communicate with the system , to know that you are talking to the systeme and need to invoke a function write a message as follows :
<FUNC>,function_name_exactly,CIN,NAME,date(in the "%Y-%m-%d" format )

if one of the arguments is missing , re_ask the user

before comfirming the appointment , ask the user if they want to comfirm

**Important Note:** Do not reveal any internal information about how appointments are processed, such as checking availability.
**Important Note:** <FUNC> is a keyword that indicates which function to invoke
**Important Note:** DO NOT MAKE ANY CONCLUSIONS BEFORE GETTING THE RESULT OF YOUR FUNCTION CALL FROM THE SYSTEM
**Important Note:** DO NOT WRITE ANYTHING AFTER THE FUNCTION CALL , ALWAYS WAIT FOR SYSTEM RESPONSE




"""
messages = [
  {'role': 'system', 'content': secretary_prompt},
  {'role': 'assistant', 'content': 'OK I understand. I will do my best!'}
]

def prompt(message , role="user"):

  response = chat(
    'qwen2.5:14b',
    messages=messages
             + [
               {'role': role, 'content': message},
             ],
  )
  messages.append( {'role': role, 'content': message})
  messages.append({'role': 'assistant', 'content': response.message.content})

  return response.message.content


def send_message(user_message,role="user"):
  result =  prompt(user_message).strip()
  if  "<FUNC>" in result :
    #print("d5alna")
    #print("function details : " +result)
    botresponse , functioncall=result.split("<FUNC>")
    print("bot : ",botresponse)
    functioncall=functioncall.split("\n")[0]
    function_name , CIN ,name ,date = functioncall[1:].split(",")
    info=""
    if function_name == "make_appointment":
       make_appointment(CIN , name , date)
       info = "appointment object created but not comfirmed yet, details :" + str(appointement[CIN])
    elif function_name == "check_availability":
       res =check_availability(date)
       info = "appointment available : " + str(res)
    elif function_name == "suggest_appointement":
      res= suggest_appointement()
      info = "suggested date : " + str(res)
    elif function_name == "confirm_appointment":
      confirm_appointment(CIN)
      info = "appointment confirmed"

    return send_message(info , role="system")
  else:
    return result
while True:
  ollama.list()
  user_input = input('Chat with history: ')
  if user_input == "exit":
    break
  response = send_message(user_input)
  # Add the response to the messages to maintain the history
  print("bot : " + response)


print(appointement)
print(comfirmed_appointements)