from flask import Flask, render_template
import requests
import json

my_url = "http://horoscope-api.herokuapp.com/horoscope/year/libra"
my_info = requests.session()

info = json.loads(my_info.get(my_url).content)

# ?? ???????? ???????????? html ?????? ??????????.
new_file = open("horoscope.txt", "w")
written = new_file.writelines(str(info))
new_file.close()


app = Flask(__name__)

# ???? ?????????????, ???????? ?? ??? ?????
print(info)
@app.route('/')
def horoscope_for_you():
    return render_template('horos.html')


if __name__ == '__main__':

    app.run()
