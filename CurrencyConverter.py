import requests

#Selecting the 2 different types of currencies to convert and the amount
def convert_curr():
    init_currency = input("Enter the initial currency: ")
    target_currency = input("Enter the target currency: ")

    while True:
        try:
            amount = float(input('Enter the amount: '))
        except:
            print('The amount needs to be a number')
            continue

        if not amount > 0:
            print('Amount needs to be greater than 0')
            continue
        else:
            break

#Pulling the information from a website by taking the inputs from def convert_curr
    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"

    payload = {}
    headers= {
      "apikey": "WovJCO28LoLnxRvrYCznoHAGzkAxHyAA"
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code

    if status_code != 200:
        result = response.json()
        print('Error response: ' + str(result))
        quit()

    result = response.json()
    print('Conversion Result: ' +str(result['result']))

#Results
if __name__ == '__main__':
    convert_curr()