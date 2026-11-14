# Tình huống tấn công toán học: phân tích n nhỏ để khôi phục khoá RSA

## Bối cảnh và dữ liệu kẻ tấn công có

Người gửi dùng khoá công khai `(n,e)` để mã hoá. Kẻ nghe lén thấy được khoá công khai và bản mã C; chưa biết p,q,d hoặc bản rõ M. Do chọn n quá nhỏ, kẻ tấn công thử các ước của n, khôi phục hai thừa số p,q rồi tự tính lại d.

Hàm `factorization_attack(n,e,ciphertext)` chỉ nhận đúng ba giá trị công khai. Endpoint `/api/attack` xử lý trước phần đọc khoá p,q của các chức năng mã hoá, không lấy khoá bí mật từ bảng thiết lập khoá.

## Cách chạy trên web

1. Khởi động bằng `python web_app.py`, mở http://127.0.0.1:8000/.
2. Chọn **Tấn công** trên thanh chức năng bên trái.
3. Giữ bộ dữ liệu mặc định n=187, e=7, C=11 rồi nhấn **Thực hiện tấn công**.
4. Giới thiệu bốn giá trị được khôi phục p,q,d,M, bảng chia thử, phép tính phi(n), nghịch đảo modulo và thời gian thực hiện.
5. Mở phần **Xem Euclid mở rộng và từng bước giải mã** để giải thích chi tiết.
6. Có thể chọn **Ví dụ khác: n=3233** để thử bộ dữ liệu thứ hai.

Bảng p,q dùng để mã hoá được ẩn ở tab này nhằm thể hiện đúng dữ liệu kẻ tấn công có.

## Tính tay bộ dữ liệu mặc định

Dữ liệu đầu vào: n=187, e=7, C=11.

| Ước đang thử t | 187 mod t | Kết luận |
|---|---|---|
| 3 | 1 | Không phải ước |
| 5 | 2 | Không phải ước |
| 7 | 5 | Không phải ước |
| 9 | 7 | Không phải ước |
| 11 | 0 | Tìm được p=11, q=187/11=17 |

Tiếp theo:

- phi(n)=(11-1)(17-1)=160.
- Tìm d sao cho 7*d=1 mod 160. Euclid mở rộng cho 1=23*7-160, nên d=23.
- Giải mã M=11^23 mod 187=88.
- Kiểm tra mã hoá lại 88^7 mod 187=11, trùng bản mã đầu vào.

Thứ tự p,q được tìm ra có thể ngược thứ tự của ví dụ trong slide; tích n, phi và khoá giải mã không thay đổi.

Bộ dữ liệu thứ hai: n=3233,e=17,C=2790. Tìm p=53,q=61,phi=3120,d=2753,M=65.

## Thuật toán và giới hạn

Phần lõi tự viết trong `rsa_core/attacks.py` thử các số lẻ từ 3 đến căn bậc hai của n. Khi tìm được ước, chia n để thu thừa số còn lại; kiểm tra hai thừa số là các số nguyên tố lẻ phân biệt; dùng Euclid mở rộng tìm d và bình phương/nhân để giải mã. Bộ demo từ chối n quá 10^12, modulo nguyên tố, modulo nhiều hơn hai thừa số nguyên tố, p=q và các đầu vào không hợp lệ.

Với k là độ dài bit của n, số phép chia thử trong trường hợp xấu tăng theo O(sqrt(n)), tương đương O(2^(k/2)); đây chỉ là đếm phép chia, chưa tính chi phí xử lý số nguyên lớn. Không phù hợp để thử trực tiếp khoá RSA lớn. Vết chỉ lưu 8 ước đầu và ước tìm được khi số lần thử dài hơn, nhưng số lần thử hiển thị là tổng số thực tế.

Tình huống minh hoạ hậu quả của modulo quá nhỏ. Không kết luận đã phá được RSA dùng khoá lớn được tạo đúng cách. Tăng cường padding không sửa được việc đã để lộ khoá riêng do n bị phân tích thừa số; khoá cần được tạo với kích thước và tham số phù hợp.

## Chạy bằng Terminal và kiểm tra

```bash
python main.py attack-factor --n 187 --e 7 --ciphertext 11
python checks/check_factorization.py
```

Script kiểm tra riêng cho tính năng này bao gồm 2 bộ đáp án đã biết, toàn bộ 187 đại diện bản rõ của modulo lớp, 9 đầu vào lỗi và giới hạn demo. Ba ca kiểm thử chính ở `tests/test_rsa.py` được giữ riêng như yêu cầu của nhóm. `pow` chỉ được dùng làm kết quả chuẩn ở script kiểm tra, không nằm trong thuật toán tấn công.

Demo sửa bản mã nhờ tính nhân trước đây vẫn chạy qua `python main.py attack`.

## Tham khảo

RFC 8017, mục 3 và 5, định nghĩa khoá RSA và các phép toán mã hoá/giải mã: https://www.rfc-editor.org/rfc/rfc8017.html . Phần chia thử, bảng minh hoạ và ca kiểm tra được dự án tự xây dựng dựa trên các quan hệ toán học RSA, không phải test vector NIST/RFC.
