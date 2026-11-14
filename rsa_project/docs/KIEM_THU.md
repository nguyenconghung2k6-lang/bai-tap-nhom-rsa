# Bộ kiểm thử chính: 4 ca

Chạy `python main.py test` hoặc F5 cấu hình kiểm thử trong VS Code. Cả bốn đều phải PASS. Sau đó chương trình mới chạy phần đối chiếu Python chuẩn riêng.

## TC01 – Ví dụ trong slides thầy

- Nguồn: tài liệu lớp đính kèm, trang 43–44.
- Đầu vào: p=17, q=11, e=7, M=88.
- Tính khoá: n=187; phi(n)=160; d=23 vì 7*23=161=1 mod 160.
- Mã hoá: C=88^7 mod 187=11.
- Giải mã: M'=11^23 mod 187=88.
- Mong đợi: đúng n,d,C,M'; giải mã trực tiếp và CRT đều ra 88.
- Đạt khi tất cả giá trị thực tế bằng giá trị đã biết từ slide.

## TC02 – Ca tự làm, ngoài ví dụ slide

- Đầu vào tự chọn cho bài: p=61, q=53, e=17, M=65.
- Tính khoá: n=3233; phi(n)=60*52=3120; gcd(17,3120)=1.
- Tính d=2753 vì 17*2753=46801=15*3120+1.
- Mã hoá: C=65^17 mod 3233=2790.
- Giải mã: M'=2790^2753 mod 3233=65.
- Mong đợi: n=3233,d=2753,C=2790,M'=65; kết quả CRT cũng bằng 65.
- Đạt khi chương trình khớp các giá trị đã tính trên, không chỉ kiểm tra round-trip.

Ca này do dự án viết riêng ngoài ví dụ slide; bộ số 61,53 thường được dùng để minh hoạ RSA, không tuyên bố là một test vector mới hoặc chuẩn NIST.

## TC03 – Ca lỗi

- Đầu vào: p=17, q=11, e=2.
- phi(n)=160; gcd(2,160)=2 khác 1.
- Không có số nguyên d thoả 2*d=1 mod 160 vì vế trái chẵn, không thể đồng dư số lẻ theo modulo chẵn.
- Mong đợi: từ chối tạo khoá, ném `ValueError` với thông báo `Không tồn tại nghịch đảo: gcd(a, modulo) != 1.`
- Đạt khi kiểm thử bắt đúng loại lỗi và thông báo. Nếu chương trình vẫn tạo khoá hoặc báo một lỗi khác, ca này thất bại.

Có thể demo lỗi trực tiếp:

```bash
python main.py number --p 17 --q 11 --e 2 --message 88
```

Lệnh báo lỗi và trả mã thoát 1. Ngược lại, bộ kiểm thử trả mã thoát 0 khi đã bắt đúng lỗi dự kiến.

## TC04 – Số lớn RSA 1024 bit

- Bộ dữ liệu cố định: [`../tests/vectors/rsa_1024.json`](../tests/vectors/rsa_1024.json). Lưu p, q, e, M và đáp án n, phi, d, C dưới dạng chuỗi thập phân để giữ nguyên mọi chữ số.
- p và q đều dài 512 bit; n=p*q dài đúng 1024 bit; e=65537.
- M là chuỗi `1234567890` lặp 8 lần, tức số dài 80 chữ số (263 bit), thoả 0 ≤ M < n.
- Bộ số được tự sinh một lần bằng thuật toán của dự án. Các đáp án cố định được tính độc lập bằng Python chuẩn: `d=pow(e,-1,phi)`, `C=pow(M,e,n)`. Đây không phải test vector NIST/RFC.
- TC04 gọi thuật toán tự cài để tạo khoá, mã hoá, giải mã thường và giải mã CRT. Kiểm tra độ dài p/q/n, các giá trị n/phi/d/C với đáp án cố định, và cả hai bản giải mã với M ban đầu.
- `reference_checks.py` đọc cùng dữ liệu rồi tính lại bằng `pow` để đối chiếu độc lập; log in C tự viết cạnh C chuẩn và xác nhận giải mã thường = CRT = pow = M.
- Log TC04 in đầy đủ p,q,e,M,n,d,C và thời gian riêng cho tạo khoá từ p,q có sẵn, mã hoá, giải mã thường và CRT. Không tính đọc JSON, kiểm tra đáp án hoặc in log vào thời gian từng phép toán. Tổng thời gian kiểm thử trên web còn gồm khởi động Python, đọc tệp và phần đối chiếu.
- Đạt khi tất cả phép so sánh khớp. Dữ liệu giữ nguyên giữa các lần chạy; thời gian có thể khác theo máy và tải hệ thống.

Chạy riêng trong thư mục `rsa_project`:

```bash
python -m unittest tests.test_rsa.RSATests.test_04_so_lon_1024_bit -v
```

Trên web: tab **Kiểm thử** → **Chạy cả 4 ca kiểm thử** → tìm `[TC04 — SỐ LỚN 1024 BIT]` trong log. Số lớn được giữ dưới dạng chuỗi trong log, không chuyển sang `Number` của JavaScript. Khoá công khai trong fixture chỉ phục vụ kiểm thử; p,q,d cũng được lưu công khai.

## Phần đối chiếu chuẩn riêng

Đề bài còn yêu cầu đối chiếu test vector chuẩn **hoặc thư viện chuẩn**. Dự án chọn thư viện chuẩn Python: `pow(a,e,n)`, `pow(a,-1,n)` và `math.gcd`, đặt trong `reference_checks.py`, tách khỏi bốn ca trên. Mã RSA và thuật toán nền trong `rsa_core/` không gọi các oracle này.

Kết quả mã hoá của TC01, TC02 và TC04 được in cạnh kết quả `pow` để dễ trình bày. Ngoài ra đối chiếu toàn bộ 187 đại diện của modulo lớp, một khoá sinh 512 bit, nhiều bộ số phép toán và kiểm tra Miller–Rabin bằng chia thử độc lập. Các kiểm tra byte/tệp bổ sung chứng minh khả năng khôi phục UTF-8 và byte 0; chúng không thay đổi số lượng **bốn ca chính** trong unittest.

Log chạy thực tế được lưu ở `evidence/tests.txt`.
