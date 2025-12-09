from flask import Flask, request, jsonify, Response, send_from_directory
from datetime import datetime
import json
import time

app = Flask(__name__)

estado_tags = {}
clientes_SSE = []

# SERVIR EL DASHBOARD --------------------------------------
@app.route('/')
def index():
    return send_from_directory('static', 'dashboard.html')
# -------------------------------------------------------------

@app.route('/stream')
def stream():
    def eventStream():
        while True:
            if clientes_SSE:
                msg = clientes_SSE.pop(0)
                yield f"data: {json.dumps(msg)}\n\n"
            time.sleep(0.2)
    return Response(eventStream(), mimetype="text/event-stream")


@app.route('/rfid', methods=['POST'])
def rfid():
    data = request.get_json()
    uid = data["uid"]

    # Inicializar estado si no existe
    if uid not in estado_tags:
        estado_tags[uid] = "fuera"   # <<< empieza fuera

    # Alternar estado
    if estado_tags[uid] == "fuera":
        tipo = "entrada"
        estado_tags[uid] = "dentro"
    else:
        tipo = "salida"
        estado_tags[uid] = "fuera"

    registro = {
        "uid": uid,
        "tipo": tipo,
        "hora": datetime.now().strftime("%H:%M:%S")
    }

    clientes_SSE.append(registro)

    print("TAG recibido:", registro)
    print("Estado actual:", estado_tags)

    return jsonify({"status": "OK"}), 200

# INICIAR SERVIDOR
app.run(host="0.0.0.0", port=5000, debug=True)