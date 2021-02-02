

import datetime

from flask import Flask, render_template, make_response, request, redirect, session


app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.secret_key = "hD4GbkeacT3KXuwZ"


@app.route('/')
def home():
   """
   Home
   :return:
   :rtype:
   """
   response_data = dict(
      message="Eduardo"
   )
   return render_template("first_template.html", **response_data), 201


@app.route('/edit-cookie', methods=['GET', 'POST'])
def edit_cookie():
   if request.method == 'GET':
      return render_template("edit_cookie.html")

   if request.method == 'POST':
      cookie_value = request.form.get('cookie-value')
      session['cookie-value'] = cookie_value
      return redirect('/cookie')


@app.route('/cookie')
def cookie_content():
   """
   Cookie content
   :return:
   :rtype:
   """
   cookies = request.cookies
   resp = make_response(render_template('cookie_content.html', cookies=cookies))
   cookie_value = session.get('cookie-value', '')
   resp.set_cookie('cookie-value', cookie_value)
   return resp


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8080)

