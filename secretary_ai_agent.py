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

the work flow should look like : checking availability , then creating the appointment , and lastly confirming it 


if one of the arguments is missing , re_ask the user

before comfirming the appointment , ask the user if they want to comfirm

**Important Note:** Do not reveal any internal information about how appointments are processed, such as checking availability.
**Important Note:** Do not reveal any internal computations or functions or calls.
**Important Note:** Do not forget to confirm the created appointments

"""
messages = [
  {'role': 'system', 'content': secretary_prompt},
  {'role': 'assistant', 'content': 'OK I understand. I will do my best!'}
]
available_functions = {
    'make_appointment': make_appointment,
    'suggest_appointement': suggest_appointement,
    'check_availability': check_availability,
    'confirm_appointment': confirm_appointment
}
tools=[make_appointment,suggest_appointement,check_availability,confirm_appointment]

def prompt(message , role="user"):

  response = chat(
    'qwen2.5:14b',
    messages=messages
             + [
               {'role': role, 'content': message},
             ],
    tools=tools
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
    user_input = input('user : ')
    if user_input == "exit":
        break
    response =  chat(
    'qwen2.5:14b',
    messages=messages
             + [
               {'role': "user", 'content': user_input},
             ],
    tools=tools
    )
    messages.append({'role': "user", 'content': user_input})
    result = ""
    messages.append(response.message)

    if response.message.tool_calls:
      #print("function called")
      print(response.message.tool_calls)
      for tool in response.message.tool_calls :
          #print(tool.function.name)

          if tool.function.name in available_functions:
              funct = available_functions[tool.function.name]
              result = str(funct(**tool.function.arguments))+"\n"
          else :
              continue
          #print(result)
          # Add the function response to messages for the model to use
          messages.append({'role': 'tool', 'content': str(result), 'name': tool.function.name})
      final_response = chat('qwen2.5:14b', messages=messages)
      print('bot:', final_response.message.content)
      messages.append(final_response.message)
    else :
        print('bot:', response.message.content)

    # Add the response to the messages to maintain the history


print(appointement)
print(comfirmed_appointements)