from flask import Flask, render_template, request, redirect
from bot import bot_instance
import asyncio

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        token = request.form.get("token")
        action = request.form.get("action")
        act_type = request.form.get("activity_type")
        act_text = request.form.get("activity_text")

        if action == "start":
            bot_instance.start_bot(token, act_type, act_text)
        elif action == "stop":
            bot_instance.stop_bot()
        elif action == "set_activity":
            if bot_instance.client and bot_instance.client.is_ready():
                loop = asyncio.get_event_loop()
                loop.create_task(bot_instance.set_activity(act_type, act_text))

        return redirect("/")

    status = "Running" if bot_instance.running else "Stopped"
    return render_template("index.html", status=status)

if __name__ == "__main__":
    app.run(debug=True)
