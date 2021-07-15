from flsk import Flask, jsonify, request
import time

app = Flask(__name__)
@app.roure("/bot", method=["POST"])

def response():
    query = dict(request.form)['query']
    result = query + " "+ time.ctime()
    return "HelloNuwan" #jsonify({"response": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0",)