from flask import Flask, jsonify, request
from logic import NumberSet

app = Flask(__name__)
number_set = NumberSet()

@app.route('/extract', methods=['POST'])
def extract_number():
    data = request.get_json()
    if 'number' not in data:
        return jsonify({'error': 'No se proporcionó el número a extraer'}), 400
    
    number = data['number']
    if not isinstance(number, int) or number < 1 or number > 100:
        return jsonify({'error': 'Número inválido, debe ser un entero entre 1 y 100'}), 400
    
    extracted_number = number_set.extract(number)
    if extracted_number is None:
        print(f'Se extrajo el número: {number}')  # Agregar este print
        return jsonify({'extracted_number': 'Número extraído correctamente.'})
    else:
        return jsonify({'extracted_number': extracted_number})

if __name__ == '__main__':
    app.run(debug=True)
