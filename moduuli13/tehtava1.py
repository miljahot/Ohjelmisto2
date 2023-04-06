from flask import Flask

app = Flask(__name__)

@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)
    flag = False
    if luku <= 1:
        flag = True
    else:
        for i in range(2, luku):
            if luku % i == 0:
                flag = True
                break
    if flag:
        flag = False
    else:
        flag = True

    vastaus = {
        "Number": luku,
        "isPrime": flag
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)