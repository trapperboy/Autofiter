class script(object):
    START_TXT = """đˇđ´đģđž {},
đŧđĸ đđđđ , <a href='https://t.me/Emiliabetter_bot'>EMILIA</a>, đ¸đ'đ đđđđĸ đđđđĸ đđđđ đđđ đđ đđ đĸđđđ đđđđđ đđđ đđđđ đđ đđđđđ, đđđđđ đđđ đ¸'đđ đđđđđđđ đđđđđđ đđđđđ đ¤
"""
    HELP_TXT = """đˇđ´đ {}
đđĻđŗđĻ đđ´ đđŠđĻ đđĻđ­đą đđ°đŗ đđē đđ°đŽđŽđĸđ¯đĨđ´."""
    ABOUT_TXT = """
đ§đđđĻ EMILIA đđđĸđ¨đ§ đ đĻđ
âĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩâĩ
ââââââ° ęĒáĨęĒŽęĒđŊ ęĒđ´á§ âąâââąâÛĒÛĒ
ââ­ââââââââââââââââŖ 
ââŖâĒŧ đđ đđŧđđ - <a href="https://t.me/Emiliabetter_bot"> EMILIA </a>
ââŖâĒŧ âšī¸âēī¸âī¸1 - <a href="https://t.me/moviesbotchannel"> admin </a>
ââŖâĒŧ âšī¸âēī¸âī¸2 - <a href="https://t.me/moviesbot_1"> â¸ę ę ę ę ę ę ę ę ę ę ę ę ę ę ę ę ę  group </a>
ââŖâĒŧ đđ˛đĢđģđĒđģđģđ - đŋđđđžđļđđ°đŧ
ââŖâĒŧ đđĒđˇđ°đžđĒđ°đŽ - đŋđđđˇđžđŊ đš
ââŖâĒŧ đđĒđŊđĒ đđĒđŧđŽ - đŧđžđŊđļđž đŗđą
ââŖâĒŧ đđ¸đŊ đŧđŽđģđŋđŽđģ -  đˇđ´đđžđēđ
ââŖâĒŧ đđžđ˛đĩđ­ đĸđŊđĒđŊđžđŧ - v1.0.1 [ đąđ´đđ° ]
ââ°ââââââââââââââââŖ âââââââââââââââââââââąâÛĒÛĒ"""
    SOURCE_TXT = """<b>NOTE:</b>
- đ° đđ  đ đđđđ đđđđđđ đđđđđđđ. 
- ÕOáááá´ áOáĒá´ - <a href="https://t.me/moviesbotchannel"> đđđđđ đđđĨđ </a>

đ đđĻđ§đđĨ:
<a href="https://t.me/moviesbot_1"> đģđŦđ¨đ´ EMILIA </a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details

âĸ/whois :-give a user full details"""
    SONG_TXT ="""<b>SONG MODULE</b>
Song Download
Song Download Module, For Those Who Love Music

đ Command

- /song [Song Name] - To Download Music

Usage
- working pm and groups"""
    JSON_TXT ="""<b>JSON MODULE</b>
JSON:
Bot returns json for all replied messages with /json

Features:
Message Editting JSON
Pm Support
Group Support

Note:
Everyone can use this command , if spaming happens bot will automatically ban you from the group"""
    PIN_TXT ="""<b>PIN MODULE</b>

<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>đ Commands & Usage:</b>

â /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members

â /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    FUN_TXT ="""<b>FUN MODULE</b> 
    
<b>đ˛ NOTHING MUCH JUST SOME FUN THINGS</b>
tđđ đđđđ đŽđđ: 
đŖ. /dice - Roll The Dice 
đ¤. /Throw đđ /Dart - đŗđ đŦđēđđž Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot"""
    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. IMDb should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âĸ /filter - add a filter in chat.
âĸ /filters - list all the filters of a chat.
âĸ /del - delete a specific filter in chat.
âĸ /delall - delete the whole filters in a chat (chat owner only)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- tgmoviebot support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. IMDb supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/josprojects)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âĸ /connect  - connect a particular chat to your PM.
âĸ /disconnect  - disconnect from a chat.
âĸ /connections - list all your connections."""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
âĸ /paste [text] - paste the given text on Pasty
âĸ /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
âĸ IMDb should have admin privillage.
âĸ These commands works on both pm and group.
âĸ These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
âĸ /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
âĸ IMDb should have admin privillage.
âĸ These commands works on both pm and group.
âĸ These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
âĸ /id - get id of a specifed user.
âĸ /info  - get information about a user.
âĸ /json - get the json details of a message.

<b>NOTE:</b>
âĸ IMDb should have admin privillage.
âĸ These commands works on both pm and group.
âĸ These commands can be used by any group member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
âĸ /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
âĸ IMDb should have admin privillage.
âĸ These commands works on both pm and group.
âĸ IMDb can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
âĸ /imdb  - get the film information from IMDb source.
âĸ /search  - get the film information from various sources.

<b>NOTE:</b>
âĸ IMDb should have admin privillage.
âĸ More search tools can be found on inline.
âĸ Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
âĸ /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
âĸ IMDb should have admin privillage.
âĸ These commands works on group.
âĸ These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
âĸ /ban - ban a user.
âĸ /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
âĸ /mute - mute a user.
âĸ /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
âĸ /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
âĸ IMDb should have admin privillage.
âĸ These commands works on group.
âĸ These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âĸ /logs - to get the rescent errors.
âĸ /stats - to get status of files in db.
âĸ /delete - to delete a specific file from db.
âĸ /users - to get list of my users and ids.
âĸ /chats - to get list of the my chats and ids.
âĸ /leave - to leave from a chat.
âĸ /disable - do disable a chat.
âĸ /ban_users - to ban a user.
âĸ /unban_users - to unban a user.
âĸ /channel - to get list of total connected channels.
âĸ /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""

    FORCESUB_TXT = """**âĻī¸ READ THIS INSTRUCTION âĻī¸**

__đŖ In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately đ__

**đ JOIN THIS CHANNEL & TRY AGAIN đ**"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
âĸ /inkick - command with required arguments and i will kick members from group.
âĸ /instatus - to check current status of chat member from group.
âĸ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
âĸ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
âĸ /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """âYou have to be the group creator to do that."""
      
    INPUT_REQUIRED = "â **Arguments Required**"
      
    KICKED = """âī¸ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """đŽ Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """âI am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """âī¸ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
