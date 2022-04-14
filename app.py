from flask import Flask    # сперва подключим модуль

app = Flask(__name__)      # объявим экземпляр фласка

@app.route('/')            # объявим путь /
def hello():               # объявим функцию для пути /
    return 'Hello, World!' # выведем текст, который будет при обращении на /


if __name__ == '__main__':
    app.run()