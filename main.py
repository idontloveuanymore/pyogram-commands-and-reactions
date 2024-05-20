from pyrogram import Client, filters
from random_content import get_funny_cat
from config import App_api_id, App_api_hash, My_number

app = Client("my_account", api_id=App_api_id, api_hash=App_api_hash, phone_number=My_number)

def read_messages_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        messages = file.read().splitlines()
    return messages

async def react_to_message(client, message, reactions):
    for reaction in reactions:
        try:
            if hasattr(message, 'id'):
                await client.send_reaction(message.chat.id, message.id, reaction)
                return True
            else:
                print("Message object does not have id attribute.")
                return False
        except Exception as e:
            continue
    return False

@app.on_message(filters.command("cat"))
async def send_cat_image(client, message):
    cat_url = get_funny_cat()
    if hasattr(message, 'id'):
        reply_to_message_id = message.id
    else:
        print("Message object does not have id attribute.")
        return

    if cat_url.endswith('.gif'):
        await client.send_animation(message.chat.id, animation=cat_url, reply_to_message_id=reply_to_message_id)
    elif cat_url.endswith('.mp4'):
        await client.send_video(message.chat.id, video=cat_url, reply_to_message_id=reply_to_message_id)
    else:
        await client.send_photo(message.chat.id, photo=cat_url, reply_to_message_id=reply_to_message_id)

@app.on_message()
async def handle_incoming_messages(client, message):
    positive_messages_to_react = read_messages_from_file('messages/positive.txt')
    negative_messages_to_react = read_messages_from_file('messages/negative.txt')
    
    if message.text and message.text.lower() in positive_messages_to_react:
        if not await react_to_message(client, message, ['😍', '👍']):
            print("All positive reactions failed.")
            return
    elif message.text and message.text.lower() in negative_messages_to_react:
        if not await react_to_message(client, message, ['😢', '💊']):
            print("All negative reactions failed.")
            return

if __name__ == "__main__":
    print("Starting the client...")
    app.run()