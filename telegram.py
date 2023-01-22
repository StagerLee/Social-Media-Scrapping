import pandas as pd
from telethon.sync import TelegramClient

#ossetiaFB, polkazov, mariupolrada, dvish_alive

name = 'XXX' 
api_id = XXX
api_hash = XXXX
chat = XXXXX

data = [] # stores all our data in the format SENDER_ID, MSG

async with TelegramClient(name, api_id, api_hash) as client:
  async for message in client.iter_messages(chat):
    data.append([message.sender_id, message.text])

df = pd.DataFrame(data, columns=['SENDER', 'MESSAGE']) # creates a new dataframe

df.to_csv('wargonzo.csv', encoding='utf-8') # save to a CSV file