import OlivOS
import OlivaNetMusic

def unity_reply(plugin_event, Proc):
    command_list = deleteBlank(plugin_event.data.message)
    if len(command_list) ==2:
        if command_list[0].lower() == "/netmusic":
            songs = OlivaNetMusic.NetMusic.NetMusicSongs(command_list[1])
            songs.SearchSongs()
            songs.GetMusicUrl()
            if songs !="":
                output=songs.checkover()
                plugin_event.reply(output)
    if len(command_list) ==3:
        if command_list[0].lower() == "/netmusic":
            songs = OlivaNetMusic.NetMusic.NetMusicSongs(command_list[1],command_list[2])
            songs.SearchSongs()
            songs.GetMusicUrl()
            if songs !="":
                output=songs.checkover()
                plugin_event.reply(output)
def deleteBlank(str):
    str_list = list(filter(None,str.split(" ")))
    return str_list