# Hướng Dẫn Sử Dụng API LICENSE v1.0

### ENDPOINT PANEL MANAGER: <a href="https://license.phukhuong79.com" target="_blank" >https://license.phukhuong79.com</a>

### ENDPOINT API: <a href="https://license.phukhuong79.com/client/v1/client.php" target="_blank" >https://license.phukhuong79.com/client/v1/client.php</a>

### ACCESS_TOKEN Lấy Ở : <a href="https://license.phukhuong79.com/views/info.php" target="_blank" >https://license.phukhuong79.com/views/info.php</a>

## Method : GET
- Với yêu cầu GET bạn sẽ truy vấn xem api của bạn có còn hạn , hết hạn hoặc đã đăng kí chưa.
### Tham Số Yêu Cầu
Khi gửi yêu cầu GET đến API, bạn cần cung cấp các tham số sau:

- `licensekey`:[TYPE=string] Mã Bản Quyền Của Bạn (Bắt Buộc). 
- `client_api`:[TYPE=string] Mã Công Cụ Phía Máy Khách Của Bạn (Bắt Buộc).
- `access_token`:[TYPE=string] AccessToken Lấy Ở Phần Thông Tin Cá Nhân Của Tài Khoản (Bắt Buộc).

### Định Dạng Phản Hồi
Phản hồi từ API sẽ là một đối tượng JSON chứa Thông Tin:
### Nếu API Tồn Tại

- `status`: Trạng Thái Của Truy Vấn -> 'success'.
- `licensekey`: Mã Bản Quyền Của Bạn.
- `client_api`: Mã Công Cụ Phía Máy Khách Của Bạn.
- `ngay_kich_hoat`: Ngày Kích Hoạt Lần Đầu Của API.
- `ngay_het_han`: Ngày Hết Hạn Của API .
- `trang_thai`: 1 Trong 2 'Expires'(Hết Hạn) hoặc 'Active'(Còn Hạn).

### Nếu API Không Tồn Tại
- `status`: Trạng Thái Của Truy Vấn -> 'error'.
- `msg`: Thông Báo Lỗi.

### Ví Dụ Phản Hồi Thành Công ( Tìm Thấy API Trong CSDL)
```json
{
    "status": "success",
    "licensekey": "KAUTO-4E7AF-EBCFB-xxxxx-xxxx-xxxxx",
    "client_api": "ToolV1",
    "ngay_kich_hoat": "2024-06-16 22:54:08",
    "ngay_het_han": "2024-09-24 22:54:08",
    "trang_thai": "Active"
}
```
### Ví Dụ Phản Hồi Thất Bại( Không Tìm Thấy API Trong CSDL)
```json
{
    "status": "error",
    "msg":"Not Found"
}
```

## Method : POST
- Với yêu cầu POST bạn sẽ đăng kí mới 1 API nếu API đó kiểm tra là chưa được đăng kí.
### Tham Số Yêu Cầu
Khi gửi yêu cầu POST đến API, bạn cần cung cấp các tham số sau:

- `licensekey`:[TYPE=string] Mã Bản Quyền Của Bạn (Bắt Buộc). 
- `client_api`:[TYPE=string] Mã Công Cụ Phía Máy Khách Của Bạn (Bắt Buộc).
- `ngay_het_han`:[TYPE=string Format: "YYYY/MM/DD H:I:S"] Thời Gian Hết Hạn Của API  (Bắt Buộc).
- `access_token`:[TYPE=string] AccessToken Lấy Ở Phần Thông Tin Cá Nhân Của Tài Khoản (Bắt Buộc).

### Định Dạng Phản Hồi
Phản hồi từ API sẽ là một đối tượng JSON chứa Thông Tin:
### Nếu Đăng Kí Mới

- `status`: Trạng Thái Của Truy Vấn -> 'success' .
- `type`: Loại Truy Vấn -> 'register' .
- `ngay_het_han`: Ngày Hết Hạn Của API .
- `trang_thai`: 1 Trong 2 'Expires'(Hết Hạn) hoặc 'Active'(Còn Hạn).

### Nếu API Đã Tồn Tại , Thì Sẽ UPDATE Lại Ngày Hết Hạn
- `status`: Trạng Thái Của Truy Vấn -> 'success' .
- `type`: Loại Truy Vấn -> 'extend' .

### Ví Dụ Phản Hồi Thành Công ( Đăng Kí Mới )
```json
{
    "status": "success",
    "type": "register",
    "ngay_het_han": "2024-09-24 22:54:08",
    "trang_thai": "Active"
}
```
### Ví Dụ Phản Hồi Thành Công ( Nếu API Đã Tồn Tại )
```json
{
    "status": "error",
    "msg":"extend"
}
```

## Thông Báo Lỗi Khác 
### Không Có Access_Token or Access_Token Không Chính Xác
```json
{
    "status": "error",
    "msg": "XÁC THỰC THẤT BẠI"
}
```
Hoặc
```json
{
    "status": "error",
    "msg": "Thiếu Trường `access_token`"
}
```

# --------------------------------------------
# Code mẫu Demo
```python
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
        self.access_token = '1ecc5d344277f7d5532bee1179a424df'
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

```
