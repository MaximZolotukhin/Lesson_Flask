from flask import Flask    # сперва подключим модуль

app = Flask(__name__)      # объявим экземпляр фласка

@app.route('/')            # объявим путь /
def render_main():               # объявим функцию для пути /
    return 'Здесь будет главная страница!' # выведем текст, который будет при обращении на /

@app.route('/products/')
def render_products():
    return "Здесь будут продукты"

@app.route('/about/')
def render_about():
    return 'Информация о проекте'

@app.route('/profiles/') #Страничики находятся в разработке
@app.route('/contacts/')
def render_under_construction():
    return "Страничка находятся в разработке" #render_template('under_construction.html')


if __name__ == '__main__':
    app.run()