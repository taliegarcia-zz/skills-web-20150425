from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/application-form")
def load_form():
    return render_template("application-form.html")


@app.route("/application", methods=['POST'])
def form_recvd():
    firstname, lastname = request.form.get("firstname"), request.form.get("lastname")
    position = request.form.get("position")
    position = position.replace("-", " ")
    salary = request.form.get("salary")

    return render_template("application.html", 
        firstname=firstname, lastname=lastname,
        position=position, salary=salary)

if __name__ == "__main__":
    app.run(debug=True)