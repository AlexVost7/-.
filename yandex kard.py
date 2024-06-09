https://yandex.ru/maps/org/novgorodskiy_kreml/1210926578/?ll=31.277543%2C58.521278&mode=search&sctx=ZAAAAAgBEAAaKAoSCZ5eKcsQz0JAEdOgaB7A4EtAEhIJGLX7VYBv8D8R7fMY5ZmX1z8iBgABAgMEBSgKOABAGEgBagJydZ0BzcxMPaABAKgBAL0BHonPrMIBBfKLtcEEggIl0J3QvtCy0LPQvtGA0L7QtNGB0LrQuNC5INC60YDQtdC80LvRjIoCAJICAJoCDGRlc2t0b3AtbWFwcw%3D%3D&sll=31.277543%2C58.521278&sspn=0.009744%2C0.003244&text=Новгородский%20кремль&z=16.72
31.277543%2C58.521278
https://static-maps.yandex.ru/v1?ll=31.274922,58.52014&z=16&apikey=f3a0fe3a-b07e-4840-a1da-06f18b2ddf13


https://yandex.ru/maps/11409/primorsky-krai/geo/bukhta_zolotoy_rog/2523721457/?ll=131.899539%2C43.105823&z=15.64
131.9,43.1
а если попробовать свои
131.899539,43.105823
https://static-maps.yandex.ru/v1?ll=131.899539,43.105823&z=13&apikey=f3a0fe3a-b07e-4840-a1da-06f18b2ddf13

60.842656,31.460618
https://static-maps.yandex.ru/v1?ll=31.38,60.842656&z=7&apikey=f3a0fe3a-b07e-4840-a1da-06f18b2ddf13

151.215377,-33.857298
https://static-maps.yandex.ru/v1?ll=151.215377,-33.857298&z=13&spn=0.002,0.002&apikey=f3a0fe3a-b07e-4840-a1da-06f18b2ddf13

117.235,40.696
https://static-maps.yandex.ru/v1?bbox=117.235,40.696~117.237,40.67&apikey=f3a0fe3a-b07e-4840-a1da-06f18b2ddf13

https://yandex.ru/maps/org/gora_everest_8848_m/238268748040/?ll=86.927255%2C27.986187&z=13.01
86.927255,27.986187
https://static-maps.yandex.ru/v1?ll=86.927255,27.986187&z=12&l=sat,skl&pt=86.927255,27.986187,flag&apikey=f3a0fe3a-b07e-4840-a1da-06f18b2ddf13
если поставить перед z как в учебнике

with open('request.json') as file:
    params = json.load(file)
    request = f'''{params["url"]}{"&".join("=".join((k, v))
                                           for k, v in params.items() if k != "url")}'''
    response = requests.get(request)
    im = Image.open(BytesIO(response.content))
    im.save('image.png')


