from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'super_secret_coffee_key_123' 

reviews_db = []

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/reviews", methods=['GET', 'POST'])
def reviews():
    if request.method == 'POST':
        if 'user_name' in session:
            name = session['user_name']
        else:
            name = request.form.get('client_name')
            session['user_name'] = name
        
        text = request.form.get('client_review')
        reviews_db.append({"name": name, "text": text})
        return redirect('/reviews')

    return render_template('reviews.html', reviews=reviews_db)

if __name__ == '__main__':
    app.run(debug=True)