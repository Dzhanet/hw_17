from application.app import create_app

#импортируем функцию, объявляющую фласк и запускаем приложение
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)