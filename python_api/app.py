from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

@app.route('/processar/<nome>')
def processar_nome(nome):
    current_time = datetime.datetime.now().isoformat()
    # Retorna o nome processado e a hora atual
    data = {
        "status": "success",
        "input_name": nome,
        "processed_name_upper": nome.upper(),
        "timestamp": current_time,
        "is_long_name": len(nome) > 5 # Nova lógica
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)