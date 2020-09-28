class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

Happy_bday = Song(["Happy Birthday to you",
"I don't want to get used", "So I'll stop right there"])

bulls_on_parade = Song(['TYhey really around the family',
 "With pockets full of shells"])

Happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

