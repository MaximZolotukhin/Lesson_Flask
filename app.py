from flask import Flask, render_template    # сперва подключим модуль

app = Flask(__name__)      # объявим экземпляр фласка

@app.route('/')  # объявим путь /
@app.route('/index/')
def render_main():               # объявим функцию для пути /
    return render_template('index.html') # выведем текст, который будет при обращении на /

@app.route('/products/')
def render_products():
    return "Здесь будут продукты"

@app.route('/about/')
def render_about():
    return render_template('about.html')

# Передача аргументов
@app.route('/video/<video_id>/')
def render_video_items(video_id):
    return "Здесь будет видео " + video_id

@app.route('/book/<author>/<title>/')
def render_book(author, title):
    return "Здесь будет страница книги " + title + " автора " + author

@app.route('/profiles/') #Страничики находятся в разработке
@app.route('/contacts/')
def render_under_construction():
    return "Страничка находятся в разработке" #render_template('under_construction.html')

# Страничика ошибки
@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"

@app.route("/example/")
def render_example():
    return "<h2>Привет, я функция Example </h2>"

@app.route("/test/")
def template():
    output = render_template('test.html', name="Alex", place="Lab")
    return output

if __name__ == '__main__':
    app.run()