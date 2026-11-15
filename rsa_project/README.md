# RSA Lab — Cài đặt và chạy

Hướng dẫn dành cho **Windows 10/11 và Visual Studio Code**. Cần Python từ **3.10 trở lên**; không cần cài thêm thư viện.

## Bước 1 — Tải mã nguồn

1. Mở [GitHub của nhóm](https://github.com/nguyenconghung2k6-lang/bai-tap-nhom-rsa).
2. Chọn **Code → Download ZIP**. Nếu đã được gửi file ZIP, dùng file đó.
3. Nhấp chuột phải vào file ZIP → **Extract All / Giải nén tất cả**.
4. Mở thư mục vừa giải nén và tìm **rsa_project**.

## Bước 2 — Cài Python

Nếu máy đã có Python từ 3.10 trở lên, bỏ qua bước này.

1. Vào [python.org/downloads](https://www.python.org/downloads/), tải **Python Install Manager** dành cho Windows.
2. Mở file tải về và bấm **Install**. Nếu được hỏi thêm thư mục vào **PATH**, gõ **y** rồi nhấn **Enter**.
3. Mở **PowerShell** mới, nhập lệnh sau rồi nhấn **Enter**:

```powershell
pymanager install 3.13
```

4. Cài xong, đóng rồi mở lại PowerShell và kiểm tra:

```powershell
py -3.13 --version
```

Thấy dòng **Python 3.13.x** là đã cài thành công.

## Bước 3 — Cài Visual Studio Code

1. Vào [code.visualstudio.com](https://code.visualstudio.com/), tải bản Windows và cài đặt.
2. Mở VS Code, nhấn **Ctrl+Shift+X**, tìm **Python** của **Microsoft** rồi bấm **Install**.

## Bước 4 — Mở thư mục dự án

1. Trong VS Code, chọn **File → Open Folder**.
2. Chọn thư mục **rsa_project** đã giải nén → **Select Folder**.
3. Kiểm tra cột bên trái có **web_app.py**, **main.py**, **rsa_core** và **web**.
4. Chọn **Terminal → New Terminal** để mở ô nhập lệnh phía dưới.

## Bước 5 — Chạy giao diện web

Nhập lệnh này trong **Terminal** rồi nhấn **Enter**:

```powershell
py -3 web_app.py
```

Nếu máy chỉ nhận lệnh `python`, dùng `python web_app.py` thay thế.

Trình duyệt sẽ tự mở. Nếu chưa mở, nhập địa chỉ **http://127.0.0.1:8000/** vào trình duyệt.

**Giữ Terminal đang chạy khi sử dụng web.** Khi muốn dừng, nhấn **Ctrl+C**. Những lần sau chỉ cần mở lại thư mục trong VS Code và chạy lệnh ở bước 5.
