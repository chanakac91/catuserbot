"""
By:- @sandy1709 & @CHATHURANGA_91
idea from @PRAVEEN_KAVINDU
"""
import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import admin_cmd
from userbot import CMD_HELP


@borg.on(admin_cmd("md ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    reply_id = event.reply_to_msg_id
    await event.edit("🎶**Initiating Download!**🎶")

    async with borg.conversation("@vkmusic_bot") as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(d_link)
            details = await conv.get_response()

            if details.message == "I found nothing 😔":
                await event.edit(details.message)
            else:
                await details.click(0)
                songh = await conv.get_response()
                await borg.send_file(event.chat_id, songh, caption="🔆**Here's the requested song!**🔆", reply_to=reply_id)
                await event.delete()
        except YouBlockedUserError:
            await event.edit("**Error:** `unblock` @vkmusic_bot `and retry!`")

CMD_HELP.update({
    "music_downloader": "**Plugin :**`music_downloader`\
     \n\nDownload Music \
     \n**Version :** `1.1.0`\
     \n**Syntax :** `.md song title`\
     \n**Usage :** will download your requested song\
"
})
