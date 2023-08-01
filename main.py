import os
from pyrogram import Client
from os import mkdir

app_id = int(os.environ.get("14631157"))
app_key = os.environ.get('aa7c2b3be68a7488abdb9de6ce78d311')
token = os.environ.get('5927429053:AAGNa4VeQEOM5_Fj_mmq-21OqB6qr308DDU')

app = Client("zipBot", app_id, app_key, bot_token=token)


if __name__ == '__main__':

    try:
        mkdir("static")  # create static files folder
    except FileExistsError:
        pass

    app.run()
