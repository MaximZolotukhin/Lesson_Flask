from flask import Flask    # сперва подключим модуль

app = Flask(__name__)      # объявим экземпляр фласка

@app.route('/')            # объявим путь /
def hello():               # объявим функцию для пути /
    return 'Hello, World!' # выведем текст, который будет при обращении на /

@app.route('/products/')
def render_products():
    return "Здесь будут продукты"

if __name__ == '__main__':
    app.run()