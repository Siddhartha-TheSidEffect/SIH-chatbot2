# backend/sih-chatbot/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess, sys, json, shlex

app = Flask(__name__)
CORS(app)

# Try to import a callable from chatbot.py. Adjust name if needed.
try:
    # if chatbot.py defines get_reply(text)
    from chatbot import get_reply
    def run_bot(msg: str):
        return get_reply(msg)
except Exception:
    # fallback: run chatbot.py as a subprocess (adjust how the script takes input)
    def run_bot(msg: str):
        # If chatbot.py reads from stdin and prints reply:
        p = subprocess.Popen([sys.executable, 'chatbot.py'],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             text=True)
        out, err = p.communicate(msg + "\n")
        if err:
            # you can log err
            pass
        return out.strip()

@app.route("/api/chat", methods=["POST"])
def chat():
    payload = request.get_json(force=True)
    msg = payload.get("message") or payload.get("text") or ""
    if not msg:
        return jsonify({"error": "no message provided"}), 400
    try:
        reply = run_bot(msg)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
