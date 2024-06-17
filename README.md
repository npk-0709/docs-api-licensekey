# Hướng Dẫn Sử Dụng API

## ENDPOINT: [https://apikey.phukhuong79.com/api/client.php](https://apikey.phukhuong79.com/api/client.php)

## Method : GET
- Với yêu cầu GET bạn sẽ truy vấn xem api của bạn có còn hạn , hết hạn hoặc đã đăng kí chưa.
### Tham Số Yêu Cầu
Khi gửi yêu cầu GET đến API, bạn cần cung cấp các tham số sau:

- `licensekey`:[TYPE=string] Mã Bản Quyền Của Bạn (Bắt Buộc). 
- `client_api`:[TYPE=string] Mã Công Cụ Phía Máy Khách Của Bạn (Bắt Buộc).
- `access_token`:[TYPE=string] AccessToken Lấy Ở Phần Thông Tin Cá Nhân Của Tài Khoản (Bắt Buộc).

### Ví Dụ Yêu Cầu

```bash
curl -G https://apikey.phukhuong79.com/api/client.php \
    --data-urlencode "licensekey=Mã_Bản_Quyền_Của_Bạn" \
    --data-urlencode "client_api=Mã_Công_Cụ_Phía_Máy_Khách_Của_Bạn" \
    --data-urlencode "access_token=AccessToken_Của_Bạn"

```
### Định Dạng Phản Hồi
Phản hồi từ API sẽ là một đối tượng JSON chứa Thông Tin:
### Nếu API Tồn Tại

- `status`: Trạng Thái Của Truy Vấn -> 'success'.
- `licensekey`: Mã Bản Quyền Của Bạn.
- `client_api`: Mã Công Cụ Phía Máy Khách Của Bạn.
- `ngay_kich_hoat`: Ngày Kích Hoạt Lần Đầu Của API.
- `ngay_het_han`: Ngày Hết Hạn Của API .
- `trang_thai`: 1 Trong 2 'Expires'(Hết Hạn) hoặc 'Active'(Còn Hạn).
- 
### Nếu API Không Tồn Tại
- `status`: Trạng Thái Của Truy Vấn -> 'error'.
- `msg`: Thông Báo Lỗi.
- 
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
