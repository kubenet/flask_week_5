from app import app, render_template, request


@app.route('/')  # главная
def index():
    return render_template("index.html")


@app.route('/cart/')  # для корзины
def cart():
    return render_template("cart.html")


@app.route('/account/')  # для личного кабинета
def account():
    return render_template("account.html")


@app.route('/register/')  # для регистрации
def register():
    return render_template("register.html")


@app.route('/logout/')  # для аутентификации
def logout():
    return render_template("logout.html")


@app.route('/ordered/')  # для подтверждения отправки
def ordered():
    return render_template("ordered.html")
