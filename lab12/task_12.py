from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    title = 'Tic Tac Toe!'

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('design.kv')

    turn = 'X'
    winner = False
    x_win = 0
    o_win = 0

    def end_game(self, btn1, btn2, btn3):
        self.winner = True
        btn1.color = 'red'
        btn2.color = 'red'
        btn3.color = 'red'

        self.disable_all_buttons()
        self.root.ids.score.text = f'{btn1.text} Wins!'

        if btn1.text == 'O':
            self.o_win += 1
        else:
            self.x_win += 1

        self.root.ids.game.text = f'X WINS: {self.x_win} | O WINS: {self.o_win}'

    def disable_all_buttons(self):
        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True

    def no_winner(self):
        if self.winner == False and \
                self.root.ids.btn1.disabled == True and \
                self.root.ids.btn2.disabled == True and \
                self.root.ids.btn3.disabled == True and \
                self.root.ids.btn4.disabled == True and \
                self.root.ids.btn5.disabled == True and \
                self.root.ids.btn6.disabled == True and \
                self.root.ids.btn7.disabled == True and \
                self.root.ids.btn8.disabled == True and \
                self.root.ids.btn9.disabled == True:
            self.root.ids.score.text = 'It\'s a tie!'

    def check_win(self, btn1, btn2, btn3):
        if btn1.text != '' and btn1.text == btn2.text and btn2.text == btn3.text:
            self.end_game(btn1, btn2, btn3)

    def win(self):

        self.check_win(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)
        self.check_win(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)
        self.check_win(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)
        self.check_win(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)
        self.check_win(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)
        self.check_win(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)
        self.check_win(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)
        self.check_win(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)

        self.no_winner()

    def presser(self, btn):
        if self.turn == 'X':
            btn.text = 'X'
            btn.disabled = True
            self.root.ids.score.text = 'O\'s Turn!'
            self.turn = '0'
        else:
            btn.text = 'O'
            btn.disabled = True
            self.root.ids.score.text = 'X\'s Turn'
            self.turn = 'X'

        self.win()

    def restart(self):
        self.turn = 'X'

        for i in range(1, 10):
            self.root.ids[f'btn{i}'].disabled = False
            self.root.ids[f'btn{i}'].text = ''
            self.root.ids[f'btn{i}'].color = 'blue'

        self.root.ids.score.text = 'X\'s Turn'

        self.winner = False


if __name__ == '__main__':
    MainApp().run()
