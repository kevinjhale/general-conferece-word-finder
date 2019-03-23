class Talk:

    def __init__(self, speaker, title, link):
        self.speaker = speaker
        self.title = title
        self.link = link
        self.content = ''
        self.paragraphs = []
        self.invitations = []

    def getLink():
        return self.link

    def toString(self):
        return "\nSpeaker: " + self.speaker + \
               "\nTitle: " + self.title + \
               "\nLink: " + self.link + '\n'
