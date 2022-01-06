class EventManager:
    def __init__(self) -> None:
        self.listeners = []

    def subscribe(self, object):
        self.listeners.append(object)
    
    def unsubscribe(self, object):
        self.listeners.remove(object)
    
    def notify(self, getFunction, *args):
        for listener in self.listeners:
            getFunction(listener)(args)
                