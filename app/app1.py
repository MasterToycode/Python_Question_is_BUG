import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
money = 1000

def DAME():
    global money
    a_list = []
    numbers = 3
    while numbers > 0:
        point = random.randrange(1, 7)
        a_list.append(point)
        numbers = numbers - 1

    if 11 <= sum(a_list) <= 18:
        right = 'Big'
    if 3 <= sum(a_list) <= 10:
        right = 'Small'

    return right, a_list

@app.route('/', methods=['GET', 'POST'])
def game():
    global money

    if request.method == 'POST':
        Your_answers = request.form['answer']
        bet_num = int(request.form['bet'])

        right, points = DAME()

        if Your_answers == right:
            money += bet_num
            result = "Congratulations! You are right! Points are [{}]".format(', '.join(map(str, points)))
        else:
            money -= bet_num
            result = "The points are [{}] You Lose!".format(', '.join(map(str, points)))

        if money <= 0:
            result += " You have no money. The game is over."
            money = 1000

    else:
        result = "Please place your bet and choose 'Big' or 'Small':"

    return render_template('index.html', money=money, result=result)

if __name__ == '__main__':
    app.run(debug=True)
