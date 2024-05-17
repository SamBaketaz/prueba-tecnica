import requests

def test_extract_number():
    number = int(input("Ingrese el número que desea extraer (de 1 a 100): "))
    if number < 1 or number > 100:
        print("El número debe estar entre 1 y 100.")
        return
    
    url = 'http://127.0.0.1:5000/extract'
    data = {'number': number}
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        extracted_number = response.json().get('extracted_number')
        if extracted_number is None:
            print(f'Número extraído correctamente.')
        else:
            print(f'Número extraído: {extracted_number}')
    else:
        print(f'Error: {response.json()}')

if __name__ == '__main__':
    test_extract_number()
