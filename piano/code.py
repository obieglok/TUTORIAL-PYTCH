import pytch


class Room(pytch.Stage):
    Backdrops = ["music-room.jpg"]


class WhiteKey(pytch.Sprite):
    Costumes = [
        "C.png",
        "D.png",
        "E.png",
        "F.png",
        "G.png",
        "A.png",
        "B.png",
        "C2.png",
        "D2.png",
        "E2.png",
        "F2.png",
        "G2.png",
        "A2.png",
        "B2.png",
    ]
    Sounds = [
        "C6Sound.mp3",
        "D6Sound.mp3",
        "E6Sound.mp3",
        "F6Sound.mp3",
        "G6Sound.mp3",
        "A6Sound.mp3",
        "B6Sound.mp3",
    ]
    SoundNames = [
        "C6Sound",
        "D6Sound",
        "E6Sound",
        "F6Sound",
        "G6Sound",
        "A6Sound",
        "B6Sound",
    ]

    @pytch.when_green_flag_clicked
    def start(self):
    	for i in range(7):
            self.index = i
            self.sound = self.SoundNames[i]
            self.switch_costume(i)
            self.go_to_xy(-100 + i*28,0)
            self.set_size(0.3)
            pytch.create_clone_of(self)
        self.hide()

    @pytch.when_this_sprite_clicked
    def keyClicked(self):
        self.switch_costume(self.index+7)
        self.play_sound_until_done(self.sound)
        self.switch_costume(self.index)

    @pytch.when_key_pressed("a")
    def keyC(self):
        if self.index == 0:
            self.switch_costume(self.index+7)
            self.play_sound_until_done(self.sound)
            self.switch_costume(self.index)

    @pytch.when_key_pressed("s")
    def keyD(self):
        if self.index == 1:
            self.switch_costume(self.index+7)
            self.play_sound_until_done(self.sound)
            self.switch_costume(self.index)

    @pytch.when_key_pressed("d")
    def keyE(self):
        if self.index == 2:
            self.switch_costume(self.index+7)
            self.play_sound_until_done(self.sound)
            self.switch_costume(self.index)

    @pytch.when_key_pressed("f")
    def keyF(self):
        if self.index == 3:
            self.switch_costume(self.index+7)
            self.play_sound_until_done(self.sound)
            self.switch_costume(self.index)

    @pytch.when_key_pressed("g")
    def keyG(self):
        if self.index == 4:
            self.switch_costume(self.index+7)
            self.play_sound_until_done(self.sound)
            self.switch_costume(self.index)

    @pytch.when_key_pressed("h")
    def keyA(self):
        if self.index == 5:
            self.switch_costume(self.index+7)
            self.play_sound_until_done(self.sound)
            self.switch_costume(self.index)

    @pytch.when_key_pressed("j")
    def keyB(self):
        if self.index == 6:
            self.switch_costume(self.index+7)
            self.play_sound_until_done(self.sound)
            self.switch_costume(self.index)

    @pytch.when_I_receive("HappyBirthday")
    def playHappyBirthday(self):
        Keys = WhiteKey.all_clones()
        Notes = [
            4,4,5,4,0,6,-1,
            4,4,5,4,1,0,-1,
            4,4,4,2,0,6,5,-1,
            3,3,2,0,1,0,
        ]
        self.Notes = "GGAGCB-GGAGDC-GGGECBA-FFECDC"
        pytch.show_variable(self,"Notes", label="Notes:")
        for i in range (28):
            if Notes[i] == -1 :
                self.say_for_seconds("-", 0.5)
            else :
                Keys[Notes[i]].switch_costume(Notes[i]+7)
                self.start_sound(self.SoundNames[Notes[i]])
                Keys[Notes[i]].say_for_seconds(self.Notes[i], 1)
                Keys[Notes[i]].switch_costume(Notes[i])
        pytch.hide_variable(self,"Notes")
        Song.hideOrShow(self,False)

    @pytch.when_I_receive("JingleBells")
    def playJingleBells(self):
        Keys = WhiteKey.all_clones();
        Notes = [
            2,2,2,-1,
            2,2,2,-1,
            2,4,0,1,2,-1,
            3,3,3,3,3,2,2,2,2,1,1,2,2,1,-1,
            4,-1,
            2,2,2,-1,
            2,2,2,-1,
            2,4,0,1,2,-1,
            4,4,4,4,4,2,2,2,4,4,3,1,0,
        ]
        self.Notes = "EEE-EEE-EGCDE-FFFFFEEEEDDEED-G-EEE-EEE-EGCDE-GGGGGEEEGGFDC"
        pytch.show_variable(self,"Notes",label="Notes:")
        for i in range (58):
            if Notes[i] == -1 :
                self.say_for_seconds("-", 0.5)
            else :
                Keys[Notes[i]].switch_costume(Notes[i]+7)
                self.start_sound(self.SoundNames[Notes[i]])
                Keys[Notes[i]].say_for_seconds(self.Notes[i], 1)
                Keys[Notes[i]].switch_costume(Notes[i])
        pytch.hide_variable(self,"Notes")
        Song.hideOrShow(self,False)

class Song(pytch.Sprite):
    Costumes = ["Cake.png", "JingleBells.png"]

    @pytch.when_green_flag_clicked
    def start(self):
        for i in range(2):
            self.index = i
            self.switch_costume(i)
            self.go_to_xy(-180 + i * 100, 140)
            self.set_size(0.1)
            pytch.create_clone_of(self)
        self.hide()

    @pytch.when_this_sprite_clicked
    def playSong(self):
        if self.index == 0:
            self.say_for_seconds("Let's play Happy Birthday!", 3)
            pytch.broadcast("HappyBirthday")
            self.hideOrShow(True)
        if self.index == 1:
            self.say_for_seconds("Let's play Jingle Bells!", 3)
            pytch.broadcast("JingleBells")
            self.hideOrShow(True)

    def hideOrShow(self, hide):
        Songs = Song.all_clones()
        if hide == True:
            for i in range(2):
                Songs[i].hide()
        if hide == False:
            for i in range(2):
                Songs[i].show()

class BlackKey(pytch.Sprite):
    Costumes = ["BlackKey.png"]

    @pytch.when_green_flag_clicked
    def start(self):
        for i in range(6):
            if i != 2 :
                self.switch_costume(0)
                self.go_to_xy(-85 + i*28,27)
                self.set_size(0.3)
                pytch.create_clone_of(self)
        self.hide()
