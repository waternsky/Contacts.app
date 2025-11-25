from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/contacts")


@app.route("/contacts")
def contacts():
    """
    Can have search query in /contacts route
    Ex: https://example.com/contacts?q=12

    If there is query parameter (q above), should filter
    contacts to match the query. otherwise, should show
    all contacts.
    """
    contacts = [
        {
            "first": "Borrel",
            "last": "Load",
            "phone": "8798299467",
            "email": "borrel.load@gmail.com",
        },
        {
            "first": "Borrel",
            "last": "Sword",
            "phone": "9832213683",
            "email": "borrel.sword@gmail.com",
        },
    ]
    return render_template("contacts.html", contacts=contacts)


def main():
    app.run()


if __name__ == "__main__":
    main()
