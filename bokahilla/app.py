from flask import *
app = Flask(__name__)

baekur = ["Hitchikers guide to the galaxy", "FIRE AND FURY, INSIDE THE TRUMP WHITE HOUSE", "The Disaster Artist"]
baekurinfo = [
    "Hitchikers guide to the galaxy er mjög fræg comedy sci-fi bók um síðasta lifandi manninn sem var bjargaður frá eyðileggingu jarðarinnar",
    "Þetta er örugglega bara einhver shitty drama bók um trump og eitthvað idk bandaríkin eru í einhverjum klandi ég nenni ekki að hugsa um það",
    "The Disaster Artist er sönn saga skrifuð af Greg Sestero, um hvernig besta versta mynd allra tíma, 'The room' varð til"]
beakurmynd = ["./static/galaxy.png", "./static/disaster.png", "./static/trump.png"]
@app.route("/")
def hello_world():
    return render_template('main.tpl', baekur=baekur)


@app.route("/book")
def book():
    return render_template('info.tpl',baekur=baekur,baekurinfo=baekurinfo,beakurmynd=beakurmynd)
app.run(host="localhost", port=8080)