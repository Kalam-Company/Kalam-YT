from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💬 Feedback 💬", "https://t.me/kalam_feedback_bot"),
                        InlineKeyboardButton("♐️ Share Me ♐️", url="https://tg://msg?text=Hai%20Friend%20%E2%9D%A4%EF%B8%8F%2C%0AToday%20I%20just%20found%20out%20an%20Simple%20and%20Powerful%20%2A%2AYouTube%20URL%20Uploader%20Bot%2A%2A%20for%20Free%F0%9F%A5%B0.%20%0A%2A%2ABot%20Link%20%3A%2A%2A%20%40Kalam_YT_Bot%20%F0%9F%94%A5"),
                    ],
                    [
                        InlineKeyboardButton(
                            "🔥 Developer 🔥",
                            url="https://t.me/kalam_feedback_bot",
                        )
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    welcomed = f"Hey <b>{message.from_user.first_name}</b>,    \n<b>I'm A Simple But POWERFUL You Tube URL Uploader Bot With Permanent Thumbnail Support!!! 💯</b> \n\n<b>Please send me a You Tube video Link (or) Share me a Video from You Tube, I can upload to telegram as File/Video</b>\n\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
