"""
    # Copyright © 2024 By Nguyễn Phú Khương (KDevTeam)
    # Telegram : @khuongdev79
    # Email : dev.phukhuong0709@hotmail.com
    # Github : npk-0709
"""

import os
import hashlib
import requests
import datetime


class LicenseAuth:
    __version__ = "v1.0"

    def __init__(self, clientApi, dayRegisterNew):
        self.clientApi = clientApi
        self.flex_code = "KDevTeam"
        self.licensekey = self.generateLicenseCode()
        self.access_token = ' YOUR ACCESSTOKEN '
        self.serverUrl = 'https://license.phukhuong79.com'
        self.serverUrlEnpoint = '/client/v1/client.php'
        self.timeOut = 10
        self.dayRegisterNew = dayRegisterNew

    def generateLicenseCode(self):
        x = hashlib.sha1(os.getlogin().encode()).hexdigest().upper()
        code = self.flex_code
        for i in range(25):
            if i % 5 == 0:
                code += '-'+x[i]
            else:
                code += x[i]
        return code

    def auth(self):
        data = {
            'licensekey': self.licensekey,
            'client_api': self.clientApi,
            'access_token': self.access_token

        }
        try:
            response = requests.request(
                method='GET',
                url=self.serverUrl+self.serverUrlEnpoint,
                params=data,
                timeout=self.timeOut

            )
            return response.json()
        except Exception as e:
            return None

    def register(self, day):
        new_date = datetime.datetime.now() + datetime.timedelta(days=day)
        data = {
            'licensekey': self.licensekey,
            'client_api': self.clientApi,
            'ngay_het_han': new_date,
            'access_token': self.access_token
        }
        try:
            response = requests.request(
                method='POST',
                url=self.serverUrl+self.serverUrlEnpoint,
                data=data,
                timeout=self.timeOut
            )
            return response.json()
        except Exception as e:
            return None

    def authApplication(self):
        """return Type = json
        - status -> True ['ngay_het_han','trang_thai'->['Active','Expires']]
        - status -> False ['msg']
        """
        r = self.auth()
        if r and r['status'] == 'success':
            return {'status': True, 'ngay_het_han': r['ngay_het_han'], 'trang_thai': r['trang_thai']}
        elif r and r['status'] == 'error' and r['msg'] == 'Not Found':
            x = self.register(self.dayRegisterNew)
            if x:
                return {'status': True, 'ngay_het_han': x['ngay_het_han'], 'trang_thai': x['trang_thai']}
            else:
                return {'status': False, 'msg': 'KHÔNG THỂ GIA HẠN MỚI - VUI LÒNG LIÊN HỆ ADMIN CỦA TOOL'}
        else:
            return {'status': False, 'msg': 'LỖI KẾT NỐI ĐẾN MÁY CHỦ - VUI LÒNG KHỞI ĐỘNG LẠI'}

    def main(self):
        AUTHapp = LicenseAuth('CLIENT API TEST', -1)
        data = AUTHapp.authApplication()
        if data['status'] == True:
            if data['trang_thai'] == 'Expires':
                print('-> TOOL ĐÃ HẾT HẠN TRUY CẬP - VUI LÒNG LIÊN HỆ ADMIN ĐỂ GIA HẠN')
                print(f'KEY CỦA BẠN LÀ `{AUTHapp.generateLicenseCode()}`')
                input()
                exit()
            else:
                print(data)
        else:
            print('-> HỆ THỐNG BẬN . VUI LÒNG THỬ LẠI SAU')
            print(data['msg'])
            input()
            exit()


if __name__ == '__main__':

    AUTHapp = LicenseAuth('CLIENT API TEST', 0)
    data = AUTHapp.authApplication()
    if data['status'] == True:
        if data['trang_thai'] == 'Expires':
            print('-> TOOL ĐÃ HẾT HẠN TRUY CẬP - VUI LÒNG LIÊN HỆ ADMIN ĐỂ GIA HẠN')
            print(f'KEY CỦA BẠN LÀ `{AUTHapp.generateLicenseCode()}`')
            input()
            exit()
        else:
            print(data)
    else:
        print('-> HỆ THỐNG BẬN . VUI LÒNG THỬ LẠI SAU')
        print(data['msg'])
        input()
        exit()
