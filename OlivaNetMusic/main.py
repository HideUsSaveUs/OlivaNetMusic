
import OlivOS
import OlivaNetMusic

class Event(object):
    def init(plugin_event, Proc):        
        pass

    def private_message(plugin_event, Proc):
        OlivaNetMusic.Reply.unity_reply(plugin_event, Proc)

    def group_message(plugin_event, Proc):
        OlivaNetMusic.Reply.unity_reply(plugin_event, Proc)

    def poke(plugin_event, Proc):
        pass

    def save(plugin_event, Proc):
        pass