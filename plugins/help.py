from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Hello, It's not Difficult!!!\n\n<b>Follow these Steps...</b>\n\n⛳️ Send Custom Thumbnail if required (It will be saved permenantly!).\n\n⛳️ Send your youtube link and select desired option.\n\n⛳️ That's all, It's simple.\n\n📝 Currently Only supports Youtube Single Video (No playlist)."
