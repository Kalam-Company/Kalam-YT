from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔥 Developer 🔥", url="https://t.me/kalam_company")],
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>,\n\n     <b>I'm A Simple but POWERFUL You Tube URL Uploader Bot With Permanent Thumbnail Support!!! 💯</b> \n\n<b>Please send me a You Tube video Link, I can upload to telegram as File/Video!!!</b>\n\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
