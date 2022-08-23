import requests


r = requests.get(input())
r_code = r.status_code

if r_code == 200:
    print(r.text)
else:
    print("Упс, произошла ошибка!..", f"Код ошибки - {r.status_code}", sep='\n')
