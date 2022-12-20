import requests
userLogin = ""
myData = ""

def loginEticket(username, password):
    URL = "https://eticket.vnpt.vn/api/PublicApi/authenticate"
    headers = {'Accept': 'application/json'}

    response = requests.post(
        URL, {'Username': username, 'Password': password}, headers)

    return response.json()['data']


def checkEticket(veID, token):
    # URL = "https://eticket.vnpt.vn/api/PrivateApi/getthongtinve"
    URL = "https://eticket.vnpt.vn/api/PrivateApi/sudungve"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"veId": veID}
    response = requests.post(URL, data=data, headers=headers)

    return response.json()


while True:

    if userLogin == "":
        print("Bắt đầu!!!!!")
        print("Vui lòng đăng nhập để soát vé")
        #myData = input()
        # if myData[0:4] == "USER":
        #     user = myData[5:len(myData)]
            # username = user.split('/')[0]
            # password = user.split('/')[1]
        username = "soatve_agg"
        password = "Vnpt@123"
        if (username != '' and password != ''):
            res = loginEticket(username, password)
            if res['id'] != "":
                print("Login Successfully!!!!")
                userLogin = res
                # print(userLogin)
            else:
                print("Login Failed!!!!")

    else:
        qrcode_scanner_data = ""
        qrcode_scanner_data = input()
        if qrcode_scanner_data == "":
            print("Chưa có vé quyét")
        else:
            res_soatve = checkEticket(qrcode_scanner_data, userLogin['token'])
            print(res_soatve['Messages'])
        
