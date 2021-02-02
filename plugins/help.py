from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"""Hello, It's not Difficult!!!

<b>Follow these Steps...</b>

⛳️ Send Custom Thumbnail if required (It will be saved permenantly!).

⛳️ Send your youtube link and select desired option.

⛳️ That's all, It's simple.

📝 Currently Only supports Youtube Single Video (No playlist)."""
