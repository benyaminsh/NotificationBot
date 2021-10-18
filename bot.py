from pyrogram import Client
from time import sleep

app = Client("my_account",config_file='config.ini')


admin = [1784783874]
texts = []

@app.on_message()
async def main(app, message):

    if len(texts) != 0:
        for tx in texts:
            if tx in message.text:
                try:
                    await app.send_message("me", f"یک اعلان جدید 🛎\n\n📃 متن اعلانی که داخل پیامه : \n\n{message.text} \n\n➖➖➖➖➖\n\n اعلان از چنل یا گروهی با این نام ارسال شده ↙️\n\n {message.chat.title}")
                except: pass
            else: pass
    else: pass

    if message.text == 'اضافه کردن':
        if message.from_user.id in admin:
            if not message.reply_to_message.text in texts:
                texts.append(message.reply_to_message.text)
                await message.reply_text(f"اضافه شد ✅",quote=True)
            else:
                await message.reply_text(f"از قبل اضافه شده 🚫",quote=True)
        pass
    pass


    if message.text == 'حذف کردن':
        if message.from_user.id in admin:
            if message.reply_to_message.text in texts:
                texts.remove(message.reply_to_message.text)
                await message.reply_text(f"حذف شد ✅",quote=True)
            else:
                await message.reply_text(f"همچین متنی اضافه نشده ❌",quote=True)
        pass
    pass


    if message.text == 'متن ها':
        if message.from_user.id in admin:
            try:
                result = ""
                for text in texts:
                    result += f"{text}\n"

                await message.reply_text(f"{result}",quote=True)
            except:
                await message.reply_text(f"لیست خالی است",quote=True)
        pass
    pass


    if message.text == 'ربات':
        if message.from_user.id in admin:
            await message.reply_text(f"ربات انلاین است ✅",quote=True)
        pass
    pass




app.run()