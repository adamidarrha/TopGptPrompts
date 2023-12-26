import json

# Read the chat session from a text file
def read_chat_session(filename):
    chat_session = []
    with open(filename, 'r') as file:
        user_msg = ""
        gpt_msg = ""
        reading_user_msg = True  # Indicates whether we are currently reading a user message
        for line in file:
            line = line.strip()
            if reading_user_msg:
                if line.startswith("User"):
                    if gpt_msg:
                        chat_session.append({"user": gpt_msg, "GPT": user_msg})
                    user_msg = line[len("User "):]
                    gpt_msg = ""
                    reading_user_msg = False
                else:
                    user_msg += "\n" + line if user_msg else line
            else:
                if line.startswith("GPT"):
                    gpt_msg += line[len("GPT "):]
                else:
                    reading_user_msg = True
                    if user_msg:
                        chat_session.append({"user": gpt_msg, "GPT": user_msg})
                    gpt_msg = line
                    user_msg = ""
        if gpt_msg:
            chat_session.append({"user": gpt_msg, "GPT": user_msg})
    return chat_session

# Convert chat session to JSON
def convert_to_json(chat_session):
    json_chat = json.dumps(chat_session, indent=4)
    return json_chat

# Input and output filenames
input_filename = "Utility/session.txt"  # Replace with your input filename
output_filename = "chat_session.json"  # Replace with your desired output filename

# Read the chat session
chat_session = read_chat_session(input_filename)

# Convert chat session to JSON format
json_chat = convert_to_json(chat_session)

# Write JSON to a file
with open(output_filename, 'w') as output_file:
    output_file.write(json_chat)

print(f"Chat session converted to JSON and saved as {output_filename}")
