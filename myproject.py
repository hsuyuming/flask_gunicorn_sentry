from flask import Flask
import sentry_sdk
import logging
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    "http://255796a7e03a45c8bf05324c3bbbb61f:ee71e8c470bb418eb9dda1650a1743a2@192.168.2.125:9000/2",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.debug("this is a DEBUG message")
    app.logger.info("this is an INFO message")
    app.logger.warning("this is a WARNING message")
    app.logger.error("this is an ERROR message")
    app.logger.critical("this is a CRITICAL message")
    try:
        10 * (1/0)
    except:
        raise
    return "Hello World!"


if __name__ == "__main__":
    app.run()

if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)