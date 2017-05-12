from flask import Flask

app = Flask(__name__)


def main():
    app.run()


@app.route('/')
def index():
    return "Yay! Trackr is online..."

if __name__ == "__main__":
    main()