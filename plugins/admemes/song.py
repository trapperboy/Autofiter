

from pyrogram import Client, filters

import youtube_dl
from youtube_search import YoutubeSearch
import requests

import os
import time

## Extra Fns -------------------------------

# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


## Commands --------------------------------

@Client.on_message(filters.command("song") & ~filters.channel & ~filters.edited)
def a(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('`ðð­ðððððð ðððð ððððð¸.....`')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            performer = f"[Êá´ÊÊá´s á´á´sÉªá´]" 
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('**ð ðð¦ ð§ð¨ð­ ðð¨ð®ð§ð ð«ðð¬ð®ð¥ð­ ð¢ð§ ð²ð¨ð®ð« ð«ððªð®ðð¬ð­ð. ðð¥ððð¬ð ð­ð«ð² ðð§ð¨ð­ð¡ðð« ð¬ð¨ð§ð  ð¨ð« ð®ð¬ð ðð¨ð«ð«ððð­ ð¬ð©ðð¥ð¥ð¢ð§ð ð!**')
            return
    except Exception as e:
        m.edit(
            "**ðð§ð­ðð« ðð¨ð§ð  ððð¦ð ð°ð¢ð­ð¡ ðð¨ð¦ð¦ðð§ðð**â\nFor ðð±ðð¦ð©ð¥ð: `/song Alone Marshmellow`"
        )
        print(str(e))
        return
    m.edit("`ð¼ððððððððð¸....ðððððð ððððð`")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'ð¹ <b>ð»ðððð:</b> <a href="{link}">{title}</a>\nðï¸ <b>ð«ððððððð:</b> <code>{duration}</code>\nðµ <b>ð½ðððð:</b> <code>{views}</code>\nð¸ <b>ð¹ðððððððð ðð:</b> {message.from_user.mention()} \nð¶ <b>ð¼ððððððð ð©ð: @MsBotTg </b> ð'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name)
        m.delete()
        message.delete()
    except Exception as e:
        m.edit('**ðð§ ðð«ð«ð¨ð« ðððð®ð«ðð. ðð¥ððð¬ð ððð©ð¨ð«ð­ ðð¡ð¢ð¬ ðð¨ @MsBotTg !!**')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
