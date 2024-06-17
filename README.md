# Hướng Dẫn Sử Dụng API

## POST: [https://apikey.phukhuong79.com/libs/transACB.php](https://apikey.phukhuong79.com/libs/transACB.php)

API này cho phép bạn lấy thông tin các giao dịch từ tài khoản của bạn.

### Tham Số Yêu Cầu

Khi gửi yêu cầu POST đến API, bạn cần cung cấp các tham số sau:

- `username`: Tên đăng nhập của bạn.
- `password`: Mật khẩu của bạn.
- `account`: Số tài khoản mà bạn muốn truy vấn.
- `row`: Số lượng giao dịch mà bạn muốn lấy.

### Ví Dụ Yêu Cầu

```http
POST https://apikey.phukhuong79.com/libs/transACB.php
Content-Type: application/x-www-form-urlencoded

username=your_username&password=your_password&account=your_account_number&row=number_of_transactions
```
### Định Dạng Phản Hồi
Phản hồi từ API sẽ là một đối tượng JSON chứa danh sách các giao dịch. Mỗi giao dịch bao gồm các thông tin sau:

- `ID`: ID của giao dịch.
- `AMOUNT`: Số tiền giao dịch.
- `TYPE`: Loại giao dịch, có thể là "IN" (vào) hoặc "OUT" (ra).
- `DESCRIPTION`: Mô tả của giao dịch.
- `CURRENCY`: Đơn vị tiền tệ của giao dịch.
- `DATE`: Ngày thực hiện giao dịch.

### Ví Dụ Phản Hồi
```json
[
    {
        "ID": "123456789",
        "AMOUNT": 500000,
        "TYPE": "IN",
        "DESCRIPTION": "Salary payment",
        "CURRENCY": "VND",
        "DATE": "2024-06-13T10:00:00Z"
    },
    {
        "ID": "987654321",
        "AMOUNT": 200000,
        "TYPE": "OUT",
        "DESCRIPTION": "Electricity bill",
        "CURRENCY": "VND",
        "DATE": "2024-06-12T15:30:00Z"
    }
]
```

## Bản quyền

- Mã nguồn của dịch vụ này được công khai, cho phép bất kỳ ai xem, sửa đổi, và cải thiện nó.
- Được phép sử dụng vào mục đích thương mại: tạo cổng thanh toán cho website, thông báo giao dịch cho nhân viện cửa hàng,...
- Không sử dụng thương mại

## Miễn trừ trách nhiệm

- **Miễn Trừ Trách Nhiệm Pháp Lý**: Người phát triển mã nguồn không chịu trách nhiệm pháp lý cho bất kỳ thiệt hại hay tổn thất nào xuất phát từ việc sử dụng hoặc không thể sử dụng dịch vụ.

- **Sử Dụng API Ngân Hàng Không Chính Thức**: Dịch vụ này hiện đang sử dụng các API của ngân hàng mà không có sự đồng ý chính thức từ các ngân hàng hoặc tổ chức tài chính liên quan. Do đó, người sáng lập và nhóm phát triển:
  - Không chịu trách nhiệm cho bất kỳ vấn đề pháp lý hoặc hậu quả nào phát sinh từ việc sử dụng các API này.
  - Không đảm bảo tính chính xác, độ tin cậy, hoặc tính sẵn có của dữ liệu lấy từ các API này.
  - Khuyến cáo người dùng cần cân nhắc rủi ro pháp lý và an toàn thông tin khi sử dụng dịch vụ.

**Ghi Chú Quan Trọng:**

- Việc sử dụng các API không chính thức này có thể vi phạm các quy định pháp lý và chính sách của ngân hàng.
- Chúng tôi khuyến khích người dùng và các bên liên quan cân nhắc kỹ lưỡng trước khi sử dụng dịch vụ này cho các mục đích tài chính hoặc thanh toán quan trọng.
- Người dùng nên tham khảo ý kiến từ chuyên gia pháp lý hoặc tài chính trước khi đưa ra quyết định dựa trên dữ liệu hoặc dịch vụ được cung cấp qua dịch vụ này.
