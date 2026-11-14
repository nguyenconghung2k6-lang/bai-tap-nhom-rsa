# RSA Lab — Hướng dẫn từng bước cho người mới

Đây là bài tập nhóm về hệ mã **RSA**, viết bằng **Python**, có giao diện web và menu Terminal. Bạn có thể làm theo tài liệu này ngay cả khi chưa từng chạy code.

**Hướng dẫn chính dành cho Windows 10/11 và Visual Studio Code (VS Code).** Dự án cần Python 3.10 trở lên, không cần cài thư viện bằng `pip`. Khi đã tải đủ mã nguồn và cài công cụ, các chức năng RSA chạy được không cần Internet.

Kho mã nguồn của nhóm: **[nguyenconghung2k6-lang/bai-tap-nhom-rsa](https://github.com/nguyenconghung2k6-lang/bai-tap-nhom-rsa)**.

> **Nhớ hai file:** `web_app.py` mở giao diện web; `main.py` mở menu trong Terminal. Khi chạy web, giữ chương trình Python hoạt động. Mở lại trang trình duyệt khi chương trình đã dừng sẽ báo từ chối kết nối.

## Chọn phần cần đọc

| Bạn đang ở tình huống nào? | Bắt đầu ở đâu? |
|---|---|
| Lần đầu dùng, chưa biết gì | Đọc lần lượt từ mục 1 đến mục 6 |
| Đã cài xong và từng chạy được | [Mục 7: Mở lại vào những lần sau](#mo-lai) |
| Cần trình bày các chức năng trên web | [Mục 8: Hướng dẫn từng tab](#dung-web) |
| Cần xem thời gian chạy | [Mục 9: Đọc số đo thời gian](#thoi-gian) |
| Gặp lỗi | [Mục 10: Tìm lỗi và cách sửa](#xu-ly-loi) |
| Muốn lấy bản mới từ GitHub | [Mục 11: Cập nhật mã nguồn](#cap-nhat) |
| Thành viên muốn sửa, commit, gửi trưởng nhóm duyệt | [Mục 12: Làm việc nhóm trên GitHub](#github) |
| Chuẩn bị thuyết trình | [Mục 13: Kịch bản demo](#thuyet-trinh) |
| Muốn chạy bằng lệnh hoặc tìm file thuật toán | [Mục 14](#dong-lenh) và [mục 15](#cau-truc) |

Nếu đang đọc trong VS Code: bấm file `README.md`, rồi nhấn **Ctrl+Shift+V** để xem bản trình bày dễ đọc. Đây chỉ là mở hướng dẫn, chưa phải chạy chương trình RSA.

<a id="khai-niem"></a>
## 1. Hiểu nhanh những từ sẽ gặp

| Từ | Hiểu đơn giản |
|---|---|
| Mã nguồn / code | Các file chứa hướng dẫn để máy tính thực hiện công việc |
| File `.py` | File mã nguồn Python |
| Python | Phần mềm thực thi các file `.py` |
| VS Code | Ứng dụng để mở thư mục dự án, xem/sửa code và mở Terminal |
| Terminal | Ô để gõ lệnh; thường nằm phía dưới VS Code |
| PowerShell | Một loại Terminal trên Windows; hướng dẫn này dùng loại này |
| Thư mục / folder | Nơi chứa nhiều file, ví dụ `rsa_project` |
| GitHub / repository / repo | Nơi nhóm lưu mã nguồn và lịch sử thay đổi trên mạng |
| Git | Công cụ trên máy giúp tải, lưu lịch sử và đồng bộ mã nguồn với GitHub |
| Commit | Một lần ghi lại các thay đổi vào lịch sử Git |
| Push / pull | Đưa commit từ máy lên GitHub / lấy thay đổi từ GitHub về máy |
| Branch / nhánh | Một luồng chỉnh sửa; `main` là bản chung của nhóm |
| Pull request / PR | Đề nghị gộp các chỉnh sửa từ nhánh riêng vào bản chung |
| Localhost / `127.0.0.1` | Địa chỉ quay về chính máy đang dùng |

**Nơi nhập cần phân biệt:**

- Lệnh như `python web_app.py`: nhập trong **Terminal**.
- Giá trị `p`, `q`, `e`, bản rõ: nhập vào **ô trên web**, hoặc theo câu hỏi trong menu Terminal.
- Không gõ lệnh hoặc số chọn menu vào nội dung `main.py`.
- Trong hướng dẫn, mỗi dòng lệnh được thực hiện bằng cách **dán/gõ rồi nhấn Enter**. Không gõ các dấu bao quanh khung code.
- Nếu Terminal có sẵn `PS C:\...>` hoặc `$`, đó là dấu nhắc của máy. Chỉ nhập phần lệnh, không chép dấu nhắc này.

<a id="tai-code"></a>
## 2. Lấy mã nguồn và giải nén

### 2.1. Nếu đã được gửi file ZIP

1. Tải file `.zip` về máy, ví dụ `RSA_Source_4Tests_1024bit.zip`.
2. Mở **File Explorer** bằng **Windows+E**.
3. Vào **Downloads / Tải xuống**.
4. Nhấp chuột phải vào file ZIP → **Extract All… / Giải nén tất cả…**.
5. Chọn nơi lưu rồi bấm **Extract / Giải nén**.
6. Mở thư mục vừa giải nén, tìm thư mục **`rsa_project`**.
7. Mở `rsa_project` để kiểm tra: phải thấy **cả `main.py` và `web_app.py`**.

**Đã đúng khi:** `main.py`, `web_app.py`, `README.md`, `rsa_core`, `web`, `tests` nằm cùng một thư mục.

Không mở và chạy file ngay bên trong cửa sổ xem ZIP. Phải giải nén trước để Python tìm đủ các module đi kèm.

### 2.2. Nếu tải từ GitHub

1. Mở [repository của nhóm](https://github.com/nguyenconghung2k6-lang/bai-tap-nhom-rsa).
2. Trong trang **Code**, kiểm tra đang chọn nhánh **`main`**.
3. Bấm nút **Code** → **Download ZIP**.
4. Giải nén theo mục 2.1.
5. Bản ZIP từ GitHub thường có thư mục ngoài `bai-tap-nhom-rsa-main`.
6. Mở thư mục ngoài đó rồi mở tiếp **`rsa_project`**.

**Nếu chỉ muốn chạy bài:** dùng ZIP là đủ, không cần cài Git. **Nếu muốn sửa code và đồng bộ thường xuyên:** dùng cách clone ở [mục 12.2](#clone). Bản ZIP không chứa lịch sử Git nên không dùng được `git pull` ngay sau khi giải nén.

<a id="cai-dat"></a>
## 3. Cài công cụ — chỉ cần làm lần đầu

### 3.1. Kiểm tra máy đã có Python chưa

1. Bấm nút **Start** trên Windows.
2. Gõ **PowerShell**, mở ứng dụng **Windows PowerShell** hoặc **PowerShell**.
3. Nhập:

```powershell
python --version
```

Nếu hiện `Python 3.13.x`, `Python 3.14.x` hoặc một bản Python từ **3.10 trở lên**, có thể chuyển sang mục 3.3. Ký hiệu `x` ở đây là số phiên bản nhỏ; kết quả trên máy sẽ là số cụ thể.

Nếu báo không tìm thấy `python`, thử:

```powershell
py -3 --version
```

Nếu lệnh này chạy được, máy đã có Python. Sau này có thể dùng `py -3` thay cho `python`, ví dụ `py -3 web_app.py`.

Nếu cả hai đều không chạy được, làm tiếp mục 3.2. Nếu vô tình thấy dấu nhắc `>>>`, bạn đang ở màn hình nhập Python; gõ `exit()` rồi Enter để quay lại PowerShell.

### 3.2. Cài Python khi máy chưa có

1. Truy cập **[python.org/downloads](https://www.python.org/downloads/)**.
2. Tải **Python Install Manager** dành cho Windows và mở file vừa tải.
3. Bấm **Install**. Theo dõi cửa sổ cấu hình xuất hiện sau đó.
4. Nếu hỏi `Add directory to your PATH now? [y/N]`, gõ **`y`** rồi **Enter**. Đây là thêm thư mục chứa các lệnh tắt; một số thay đổi chỉ có hiệu lực khi mở Terminal mới.
5. Để cài Python 3.13 bằng manager, mở PowerShell mới và chạy:

```powershell
py install 3.13
```

Nếu `py install` lại báo không mở được file `install`, máy có thể đang gọi launcher cũ. Dùng manager bằng tên đầy đủ:

```powershell
pymanager install 3.13
```

6. Chờ tải và cài xong. Đóng rồi mở lại PowerShell/VS Code.
7. Kiểm tra:

```powershell
py -3.13 --version
```

Nếu bạn dùng bộ cài Python kiểu cũ có nút **Install Now**, chọn **Add python.exe to PATH** trước khi cài. Không cần cài lại nếu mục 3.1 đã thành công.

Tham khảo cách cài chính thức: [Python trên Windows](https://docs.python.org/3/using/windows.html). Không cần chọn bản thử nghiệm, bản embeddable hoặc cài thêm thư viện mật mã cho bài này.

### 3.3. Cài VS Code

Nếu đã dùng được VS Code thì bỏ qua bước này.

1. Truy cập **[code.visualstudio.com](https://code.visualstudio.com/)**.
2. Tải bộ cài Windows, mở file tải về.
3. Làm theo trình cài đặt và bấm **Install**.
4. Mở **Visual Studio Code** sau khi hoàn tất.

Tên cần dùng là **Visual Studio Code**, không phải phần mềm **Visual Studio**. Hướng dẫn cài của Microsoft: [VS Code trên Windows](https://code.visualstudio.com/docs/setup/windows).

<a id="mo-thu-muc"></a>
## 4. Mở đúng thư mục trong VS Code

### 4.1. Chọn thư mục dự án

1. Trong VS Code, bấm **File → Open Folder…**.
2. Tìm nơi đã giải nén ở mục 2.
3. Bấm chọn **`rsa_project`**, rồi bấm **Select Folder / Chọn thư mục**.
4. Nếu VS Code hỏi có tin tưởng tác giả của thư mục không, xác nhận khi đây đúng là mã nguồn nhóm bạn vừa tải.
5. Nhìn cột **Explorer** bên trái. Nếu không thấy cột này, nhấn **Ctrl+Shift+E**.

**Dấu hiệu mở đúng:** tiêu đề thư mục là `RSA_PROJECT` hoặc `rsa_project`; bên dưới có `main.py`, `web_app.py`, `rsa_core`, `web`, `tests`.

Nếu bên trái chỉ có **Open Editors** và tên một file, hãy làm lại **File → Open Folder**. Mở một file riêng lẻ chưa thay thế cho việc mở cả thư mục dự án.

### 4.2. Cài phần hỗ trợ Python trong VS Code

1. Nhấn **Ctrl+Shift+X** để mở **Extensions**.
2. Tìm **Python** và chọn extension có nhà phát hành **Microsoft**.
3. Bấm **Install** nếu chưa cài.
4. Tìm thêm **Python Debugger** của **Microsoft**, cài nếu chưa có. Phần này dùng khi chạy bằng F5.
5. Quay lại Explorer bằng **Ctrl+Shift+E**, mở `web_app.py`.
6. Nhấn **Ctrl+Shift+P**, gõ **Python: Select Interpreter**, bấm kết quả tương ứng.
7. Chọn bản Python đã cài, ví dụ **Python 3.13**.

Không cần cài Code Runner hoặc Live Server để chạy bài này. Nếu chưa thấy Python trong danh sách, kiểm tra lại mục 3.1 rồi đóng/mở VS Code.

### 4.3. Chọn PowerShell làm Terminal

Để tránh lỗi dấu nháy đường dẫn từng gặp với Git Bash:

1. Nhấn **Ctrl+Shift+P**.
2. Gõ và chọn **Terminal: Select Default Profile**.
3. Chọn **PowerShell** hoặc **Windows PowerShell**.
4. Chọn **Terminal → New Terminal** để mở một Terminal mới.

Việc đổi profile không biến Terminal cũ thành PowerShell; cần mở Terminal mới. Cửa sổ mới thường có dòng bắt đầu bằng `PS`.

### 4.4. Kiểm tra Terminal đang ở đúng chỗ

Bấm chuột vào vùng Terminal ở phía dưới, nhập:

```powershell
dir
```

Đọc danh sách trả về:

| Bạn thấy gì? | Làm tiếp thế nào? |
|---|---|
| Có `main.py` và `web_app.py` | Đã đúng; chuyển sang mục 5 |
| Chỉ có thư mục `rsa_project`, chưa thấy hai file trên | Gõ `cd rsa_project`, Enter, rồi gõ `dir` lại |
| Chỉ có thư mục ngoài như `bai-tap-nhom-rsa-main` | Dùng File → Open Folder mở thẳng `rsa_project`, rồi mở Terminal mới |
| Không có `web_app.py` dù đã ở trong `rsa_project` | Có thể đang dùng bản cũ hoặc chưa giải nén đủ; tải lại bản mới |

`cd` nghĩa là chuyển vào thư mục. Nếu đã ở `rsa_project` thì không gõ thêm `cd rsa_project`, vì sẽ tìm nhầm một thư mục con cùng tên.

<a id="chay-web"></a>
## 5. Chạy web lần đầu bằng Terminal

### Bước 1 — Nhập lệnh chạy

Sau khi `dir` đã hiện `web_app.py`, nhập:

```powershell
python web_app.py
```

Nếu máy chỉ nhận lệnh `py`, dùng lệnh này thay thế:

```powershell
py -3 web_app.py
```

**Chọn một trong hai lệnh**, không chạy cả hai cùng lúc vì chúng sẽ cùng dùng cổng 8000.

### Bước 2 — Kiểm tra thông báo

Khi chạy đúng, Terminal xuất hiện:

```text
Giao diện RSA đang chạy tại: http://127.0.0.1:8000/
Giữ cửa sổ Terminal mở; nhấn Ctrl+C để dừng.
```

Đây là **kết quả để đọc**, không cần gõ lại hai dòng này.

Terminal chưa quay lại dấu nhắc `PS ...>` là bình thường: chương trình đang chờ xử lý các thao tác từ web. Những dòng kiểu `GET /` hoặc `POST /api/...` xuất hiện khi sử dụng cũng là nhật ký hoạt động.

### Bước 3 — Mở trang web

1. Trình duyệt thường tự mở.
2. Nếu chưa tự mở, mở Chrome hoặc Edge.
3. Bấm vào **thanh địa chỉ trên cùng**, nhập **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** rồi Enter.
4. Khi thấy **RSA Lab** với các mục **Số nguyên**, **Văn bản**, **Tệp dữ liệu**, **Kiểm thử**, **Tấn công**, bạn đã chạy thành công.

Không mở trực tiếp `web/index.html` bằng cách nhấp đúp. Nếu thanh địa chỉ bắt đầu bằng `file:///`, bạn đang mở file HTML chứ chưa mở ứng dụng qua máy chủ Python; giao diện có thể mất định dạng và các nút không hoạt động.

### Bước 4 — Giữ chương trình chạy

Có thể thu nhỏ VS Code và dùng trình duyệt. Không bấm biểu tượng thùng rác của Terminal đang chạy web. Đóng trình duyệt không nhất thiết dừng Python; ngược lại, dừng Python thì web không xử lý được thao tác nữa.

`127.0.0.1` là máy của chính bạn. Gửi đường dẫn này cho bạn khác không làm họ mở được chương trình trên máy bạn; mỗi người cần tải và chạy dự án trên máy của mình.

<a id="chay-f5"></a>
## 6. Chạy bằng F5 để không phải gõ lệnh mỗi lần

Dự án đã có sẵn các cấu hình chạy trong `.vscode/launch.json`.

1. Hoàn thành cài đặt và mở đúng thư mục `rsa_project` ở mục 3–4.
2. Nếu đã chạy web bằng Terminal, bấm vào Terminal đó rồi **Ctrl+C** để dừng trước.
3. Nhấn **Ctrl+Shift+D** để mở **Run and Debug**.
4. Ở ô chọn cấu hình phía trên, chọn đúng **RSA: Giao diện web**.
5. Nhấn **F5** hoặc bấm nút tam giác màu xanh cạnh cấu hình.
6. Nếu laptop dùng F5 cho chức năng khác, thử **Fn+F5** hoặc bấm nút tam giác trong Run and Debug.
7. Mở địa chỉ được in trong Terminal nếu trình duyệt chưa tự mở.

**Lưu ý:** nút tam giác ở góc phải của file đang mở có thể chạy chính file đó. Để mở web ổn định, dùng cấu hình **RSA: Giao diện web** trong Run and Debug.

Nếu danh sách không có cấu hình RSA, kiểm tra đã mở **cả thư mục `rsa_project`** chưa và đã cài Python Debugger chưa. Nếu chọn **RSA: Menu chính**, bạn sẽ thấy menu Terminal; đó là chế độ khác, không phải lỗi.

<a id="mo-lai"></a>
## 7. Mỗi lần mở lại, dừng chương trình và chạy sau khi sửa code

### 7.1. Quy trình mở lại hằng ngày

Nếu đã cài xong một lần, lần sau chỉ cần:

1. Mở VS Code → mở lại thư mục `rsa_project`.
2. **Run and Debug → RSA: Giao diện web → F5**.
3. Chờ dòng địa chỉ trong Terminal, rồi dùng web.

Hoặc mở Terminal tại đúng thư mục và chạy `python web_app.py`.

**Không cần cài lại Python hoặc giải nén lại mỗi lần.** Nhưng nếu máy chủ Python đã dừng thì cần khởi động nó lại. Bản hiện tại không tự chạy máy chủ chỉ vì bạn mở VS Code.

### 7.2. Dừng đúng cách

- Chạy bằng Terminal: bấm vào Terminal đang chạy rồi nhấn **Ctrl+C**.
- Chạy bằng F5: bấm nút **Stop** hình vuông trên thanh debug, hoặc **Shift+F5**.

Khi Terminal quay lại dấu nhắc, chương trình đã dừng. Lúc này truy cập địa chỉ web có thể báo `ERR_CONNECTION_REFUSED`; đó là điều bình thường.

### 7.3. Sau khi sửa hoặc tải code mới

1. Lưu file đang sửa bằng **Ctrl+S**.
2. Dừng web đang chạy theo mục 7.2.
3. Chạy lại bằng F5 hoặc `python web_app.py`.
4. Trong Chrome/Edge, nhấn **Ctrl+F5** để tải lại giao diện.

Chương trình không có chức năng tự nạp lại toàn bộ code Python khi bạn lưu file. Chỉ tải lại trang trình duyệt có thể chưa áp dụng thay đổi ở phía Python.

<a id="dung-web"></a>
## 8. Dùng từng chức năng trên giao diện web

### 8.1. Tab Số nguyên — ví dụ trong slide

1. Bấm **Số nguyên** ở thanh điều hướng.
2. Trong phần **Thiết lập khoá**, bấm **Ví dụ trong slide**.
3. Kiểm tra các ô lần lượt là `p = 17`, `q = 11`, `e = 7`.
4. Ô **Bản rõ M** phải là `88`.
5. Bấm **Mã hoá & giải mã**.
6. Đọc ba ô kết quả:

| Nội dung | Kết quả đúng |
|---|---|
| Bản rõ M | 88 |
| Bản mã C | 11 |
| Giải mã M′ | 88 |
| Modulo n | 187 |
| Phi φ(n) | 160 |
| Số mũ riêng d | 23 |

7. Kéo xuống để xem thời gian **Tạo khoá**, **Mã hoá**, **Giải mã**.
8. Bấm **Quan sát từng bước tính toán** để mở các bước Euclid, bình phương và nhân khi mã hoá/giải mã.

Ví dụ lấy từ trang 43–44 tài liệu lớp. Đây là dữ liệu nhỏ để giải thích trong cùng chương trình RSA, không phải một phiên bản thu nhỏ riêng.

**Nếu muốn nhập bộ số khác:** thay trực tiếp p, q, e, M rồi bấm chạy lại. Điều kiện là p và q là hai số nguyên tố lẻ khác nhau; `1 < e < φ(n)`, `gcd(e, φ(n)) = 1`; `0 ≤ M < n`. Một bộ để thử là `p=61, q=53, e=17, M=65`, cho `65 → 2790 → 65`.

### 8.2. Tab Văn bản — mã hoá tiếng Việt

1. Bấm **Văn bản**.
2. Trong **Thiết lập khoá**, bấm **Văn bản & tệp** để dùng `p=61, q=53, e=17`. Nút **Áp dụng** ở gợi ý trong tab cũng chọn bộ này.
3. Tại ô **Bản rõ**, nhập thử:

```text
Xin chào, nhóm RSA! Đây là bài thuyết trình của chúng mình. 🔐
```

4. Bấm **Mã hoá văn bản**.
5. Ô **Bản mã** hiện một chuỗi Base64. Base64 là cách hiển thị dữ liệu byte dưới dạng chữ; phép mã hoá bên trong vẫn là RSA.
6. Giữ nguyên p, q, e và chuỗi bản mã; bấm **Giải mã bản mã**.
7. Kiểm tra ô **Văn bản sau giải mã** giống hệt câu đã nhập, kể cả dấu, dấu cách và emoji.
8. Đọc thông báo khớp nội dung và bảng thời gian.

Bộ khoá slide có `n=187`, không đủ cho mã hoá dữ liệu byte. Vì thế hãy chọn **Văn bản & tệp** hoặc **Sinh khoá 512 bit** cho tab này.

Nếu bấm **Sinh khoá 512 bit**, hãy chờ chương trình điền p, q, e. Không sinh lại khoá giữa mã hoá và giải mã. Khi cần giải mã sau khi tải lại trang, bạn phải giữ lại đúng bộ khoá đã dùng; giao diện không tự lưu khoá cho phiên sau.

### 8.3. Tab Tệp dữ liệu — demo với tệp thật

**Lần đầu nên dùng tệp có sẵn:** `examples/message_vi.txt`.

1. Bấm **Tệp dữ liệu**.
2. Bấm **Văn bản & tệp** để dùng bộ khoá mẫu, hoặc bấm **Sinh khoá 512 bit** và đợi sinh xong.
3. Bấm **Duyệt tệp**.
4. Trong cửa sổ chọn file, vào thư mục dự án → `examples` → chọn `message_vi.txt` → **Open**.
5. Tên file và số byte xuất hiện trên trang. Tệp gốc phải nhỏ hơn hoặc bằng 1 MiB (1.048.576 byte; giao diện ghi 1 MB).
6. Bấm **Mã hoá & tải xuống**.
7. Mở danh sách tải xuống của Chrome/Edge bằng **Ctrl+J** để tìm `message_vi.txt.rsa`.
8. Quay lại web, giữ nguyên p, q, e.
9. Bấm **Duyệt tệp** lần nữa, chọn **file `.rsa` vừa tải**.
10. Bấm **Giải mã & tải xuống**.
11. Tìm file khôi phục trong Downloads rồi mở bằng VS Code/Notepad để đối chiếu với file gốc.

Nếu tên file trùng với file đã có trong Downloads, trình duyệt có thể thêm `(1)` hoặc hỏi nơi lưu. Hãy xem danh sách tải xuống để xác định đúng file vừa tạo. Đây không phải lỗi giải mã.

Có thể làm tương tự với ảnh PNG/JPG nhỏ. Nếu cần chứng minh khớp từng byte và tự lưu cặp khoá ra file, dùng lệnh **demo-file** ở [mục 14.3](#demo-file).

**Không mở file `.rsa` rồi mong đọc được nội dung gốc.** Nó chứa dữ liệu đã mã hoá và header riêng của dự án, cần giải mã trước.

### 8.4. Tab Kiểm thử — chạy cả 4 ca

1. Bấm **Kiểm thử**.
2. Kiểm tra danh sách có **TC01, TC02, TC03, TC04**.
3. Bấm **Chạy cả 4 ca kiểm thử** một lần, chờ nút hết trạng thái đang xử lý.
4. Đọc trạng thái thành công/thất bại phía trên khung log.
5. Cuộn bên trong khung log để xem đủ kết quả.

| Ca | Dữ liệu | Điều cần kiểm tra |
|---|---|---|
| TC01 — Slide | p=17, q=11, e=7, M=88 | n=187, d=23, C=11, giải mã về 88 |
| TC02 — Tự làm | p=61, q=53, e=17, M=65 | n=3233, d=2753, C=2790, giải mã về 65 |
| TC03 — Lỗi | p=17, q=11, e=2 | Từ chối khoá vì e không có nghịch đảo modulo φ(n) |
| TC04 — Số lớn | n 1024 bit, p/q 512 bit, e=65537, M 80 chữ số | n, φ, d, C khớp đáp án cố định; giải mã thường và CRT đều khôi phục M |

**TC03 có chữ “lỗi” nhưng vẫn phải PASS:** ca này cố ý đưa đầu vào sai. Chương trình xử lý đúng khi từ chối nó và kiểm thử bắt được đúng lỗi mong đợi.

**Cách đọc TC04:** tìm `[TC04 — SỐ LỚN 1024 BIT]`; so hai dòng **C kỳ vọng** và **C thực tế**, rồi so **Giải mã thường M′**, **Giải mã CRT M′** với M ban đầu. Ngay bên dưới có thời gian từng công đoạn.

TC04 dùng số cố định trong [`tests/vectors/rsa_1024.json`](tests/vectors/rsa_1024.json), không sinh một bộ khác mỗi lần. Vì thế giá trị số phải giống nhau qua các lần chạy; thời gian có thể khác. M dài 80 chữ số là `1234567890` lặp 8 lần, tương ứng 263 bit. Không cần tự gõ các số rất dài này.

Kết quả tốt cần có cả:

```text
Ran 4 tests in ...s
OK
```

và ở phần đối chiếu cuối log:

```text
KẾT QUẢ ĐỐI CHIẾU: TẤT CẢ KHỚP
```

Dấu `...` trong ví dụ trên thay cho thời gian thực tế. Phần đối chiếu dùng `pow` và `math.gcd` của Python làm kết quả tham chiếu độc lập. Đây là nhánh **đối chiếu với thư viện chuẩn** trong yêu cầu bài tập; TC04 không được gọi là vector chuẩn NIST/RFC.

Bốn ca kiểm thử dùng dữ liệu riêng, không phụ thuộc những ô p, q, e bạn đang nhập ở tab khác. Xem chi tiết tại [`docs/KIEM_THU.md`](docs/KIEM_THU.md).

### 8.5. Tab Tấn công — phân tích n thành p × q

1. Bấm **Tấn công**. Bảng thiết lập khoá p, q, e dùng cho mã hoá sẽ được ẩn.
2. Giữ dữ liệu mặc định: **n = 187**, **e = 7**, **C = 11**.
3. Bấm **Thực hiện tấn công**.
4. Đọc kết quả: **p = 11**, **q = 17**, **d = 23**, **M = 88**.
5. Xem lần lượt bảng chia thử, cách tính φ(n), tìm d và giải mã.
6. Mở phần **Xem Euclid mở rộng và từng bước giải mã** nếu cần giải thích chi tiết.
7. Đọc thời gian ở bảng kết quả.
8. Bấm **Ví dụ khác: n = 3233**, rồi **Thực hiện tấn công** lần nữa; kết quả bản rõ là **65**.

Điểm cần giải thích: người tấn công chỉ cung cấp **n, e và C**, chưa nhập p, q hoặc d. Do n quá nhỏ, phép chia thử tìm được thừa số, từ đó tính lại khoá riêng và đọc bản rõ.

Demo giới hạn **n ≤ 10¹²**, chỉ nhận n là tích hai số nguyên tố lẻ khác nhau cùng các điều kiện khoá phù hợp. Nó không chứng minh phá được khoá 1024 bit của TC04. Xem kịch bản đầy đủ ở [`docs/TAN_CONG_PHAN_TICH_THUA_SO.md`](docs/TAN_CONG_PHAN_TICH_THUA_SO.md).

<a id="thoi-gian"></a>
## 9. Thời gian chạy nằm ở đâu và đọc như thế nào?

Không cần sửa code hay tự bấm đồng hồ. Chương trình tự đo bằng `time.perf_counter()`.

| Khi bạn làm gì? | Xem ở đâu? | Đang đo gì? |
|---|---|---|
| Mã hoá số nguyên trên web | Bảng dưới kết quả | Tạo/kiểm tra khoá, mã hoá, giải mã |
| Mã hoá/giải mã văn bản hoặc tệp trên web | Bảng thời gian của tab | Tạo/kiểm tra khoá và thao tác vừa thực hiện |
| Sinh khoá 512 bit trên web | Dòng thông báo sau khi sinh xong | Sinh và kiểm tra khoá |
| Chạy kiểm thử trên web | Bảng cuối kết quả | Toàn bộ tiến trình kiểm thử: khởi động Python, đọc dữ liệu, 4 ca và đối chiếu |
| Xem riêng TC04 | Dòng “Thời gian” trong log TC04 | Tạo khoá từ p/q có sẵn, mã hoá, giải mã thường, giải mã CRT |
| Chạy tấn công | Bảng thời gian trong kết quả tấn công | Xử lý đầu vào, phân tích n, tìm d, giải mã và kiểm tra lại |
| Chạy demo bằng `main.py` | Bảng “THỜI GIAN THỰC HIỆN” | Các công đoạn được ghi tên trong bảng |

- **ms** là mili giây; **1.000 ms = 1 giây**.
- Thời gian từng phép toán không gồm thời gian bạn suy nghĩ/nhập dữ liệu, trình duyệt đọc/tải file hoặc in bảng kết quả. Thu thập bước trung gian bên trong thuật toán vẫn có thể nằm trong phép đo.
- **Tổng kiểm thử** là phạm vi rộng hơn, gồm cả đọc dữ liệu và khởi động tiến trình; không so trực tiếp với một phép mã hoá.
- Trong CLI, tổng của demo số nguyên gồm **cả giải mã thường lẫn CRT** vì chương trình chạy cả hai.
- TC04 tạo khoá từ p/q cố định; thời gian này không phải thời gian tìm hai số nguyên tố mới.
- Số đo thay đổi theo máy và tải hệ thống. Một lần CRT nhanh hơn hay chậm hơn chưa phải kết luận thống kê.

Muốn đo theo kích thước dữ liệu, chạy trong Terminal của `rsa_project`:

```powershell
python main.py benchmark --bits 512
```

Kết quả có các cột `bytes,encrypt_seconds,decrypt_seconds,match`, tương ứng 1 KiB, 4 KiB, 16 KiB; thời gian ở đây tính bằng **giây**. `match=True` nghĩa là byte giải mã khớp byte gốc. Mỗi cỡ chỉ đo một lượt, không tính sinh khoá và đọc/ghi file.

<a id="xu-ly-loi"></a>
## 10. Gặp lỗi thì tìm đúng trường hợp dưới đây

### 10.1. `can't open file ... web_app.py` hoặc `[Errno 2] No such file or directory`

Thường do Terminal đang ở thư mục ngoài, hoặc bạn dùng bản code chưa có web.

1. Gõ `dir`.
2. Nếu chỉ thấy thư mục `rsa_project`, gõ `cd rsa_project`.
3. Gõ `dir` lần nữa, phải thấy `web_app.py`.
4. Chạy lại `python web_app.py`.

Cách dễ nhất khi không biết đang ở đâu: **File → Open Folder → chọn đúng `rsa_project` → Terminal → New Terminal**.

Nếu cần đi bằng đường dẫn: mở thư mục `rsa_project` trong File Explorer, bấm thanh địa chỉ rồi **Ctrl+C**. Trong Terminal gõ `cd "`, dán đường dẫn, thêm `"`, Enter. Đường dẫn có khoảng trắng vẫn dùng được khi đặt trong một cặp dấu nháy kép.

### 10.2. `[Errno 22] Invalid argument`, đường dẫn bị lặp hoặc có dấu nháy thừa

1. Chuyển Terminal mặc định sang **PowerShell** theo mục 4.3.
2. Mở Terminal mới; kiểm tra đúng thư mục bằng `dir`.
3. Tự gõ `python web_app.py` hoặc `python main.py`.
4. Dùng cấu hình F5 ở mục 6 cho các lần sau.

Không sao chép nguyên dòng chạy dài có đường dẫn Python và nhiều lớp dấu nháy từ Terminal cũ. Thư mục có dấu cách hoặc `(1)` không bắt buộc phải đổi tên; điều quan trọng là đúng thư mục và cách đặt dấu nháy.

### 10.3. `python is not recognized`, `Python was not found` hoặc bị mở Microsoft Store

1. Đóng rồi mở lại VS Code sau khi cài Python.
2. Thử `py -3 --version`.
3. Nếu lệnh này chạy được, dùng `py -3 web_app.py`.
4. Nếu cả `python` và `py` không chạy được, quay lại mục 3.2 để cài/kiểm tra Python.
5. Nếu đã cài Python Install Manager mà lệnh vẫn mở sai ứng dụng, xem phần **Troubleshooting** trong [hướng dẫn Python chính thức](https://docs.python.org/3/using/windows.html#troubleshooting) để kiểm tra App execution aliases.

### 10.4. Trình duyệt báo `127.0.0.1 refused to connect` hoặc `ERR_CONNECTION_REFUSED`

1. Quay lại VS Code, nhìn Terminal chạy web.
2. Nếu có lỗi màu đỏ hoặc đã trở lại `PS ...>`, máy chủ đã dừng/chưa khởi động thành công. Xử lý lỗi đầu tiên trước.
3. Chạy lại `python web_app.py`.
4. Chờ thấy dòng “Giao diện RSA đang chạy tại…”.
5. Mở **đúng địa chỉ và cổng vừa được in**. Chạy cổng 8001 thì phải truy cập 8001, không phải 8000.

Mở lại tab trình duyệt không tự khởi động Python. Với lỗi này, kiểm tra máy chủ trước; chưa cần đổi mạng hoặc tắt tường lửa.

### 10.5. Python báo đang chạy nhưng trình duyệt không tự bật

Giữ Terminal đó mở, tự nhập `http://127.0.0.1:8000/` vào thanh địa chỉ Chrome/Edge. Việc tự bật trình duyệt phụ thuộc cài đặt máy; web vẫn chạy được bằng cách mở thủ công.

### 10.6. Giao diện chỉ có chữ thô, hình biểu tượng rất to hoặc nút không chạy

1. Kiểm tra thanh địa chỉ: nếu có `file:///.../web/index.html`, đóng tab đó.
2. Chạy `python web_app.py`.
3. Mở `http://127.0.0.1:8000/` bằng Chrome/Edge.
4. Nhấn **Ctrl+F5**.
5. Nếu vẫn lỗi, kiểm tra đã tải đủ `web/index.html`, `web/style.css`, `web/app.js` từ cùng một phiên bản chưa.

Không cần mở bằng Live Server; ứng dụng cần cả các API Python trong `web_app.py`.

### 10.7. Cổng 8000 đã được sử dụng / `WinError 10048` / `Address already in use`

Có thể một cửa sổ Terminal khác vẫn đang chạy web. Tìm và dừng đúng cửa sổ đó bằng Ctrl+C, rồi chạy lại. Hoặc dùng cổng khác:

```powershell
python web_app.py --port 8001
```

Sau đó mở **[http://127.0.0.1:8001/](http://127.0.0.1:8001/)**. Không chạy thêm nhiều cửa sổ rồi mở nhầm web của bản cũ.

### 10.8. Không thấy cấu hình F5 hoặc F5 chạy menu thay vì web

Mở đúng **thư mục `rsa_project`**, cài **Python** và **Python Debugger**, rồi chọn **RSA: Giao diện web** trong Run and Debug. Không chọn **RSA: Menu chính** nếu muốn mở web.

Nếu thông báo lỗi nhắc `debugpy`, kiểm tra extension Python Debugger; dự án không yêu cầu bạn tự cài một thư viện mật mã nào để sửa lỗi này.

### 10.9. Menu hỏi `Chọn:` nhưng gõ không có tác dụng, hoặc số xuất hiện trong file code

Bấm chuột vào **Terminal** ngay sau `Chọn:`, gõ số rồi Enter. Ví dụ gõ `1` để demo số nguyên, `0` để thoát. Không nhập trong **Debug Console**, **Output** hoặc vùng soạn thảo `main.py`.

Nếu đã lỡ gõ vào code, dùng **Ctrl+Z** trong đúng file để hoàn tác thao tác vừa nhập, rồi kiểm tra nội dung trước khi lưu.

### 10.10. Kiểm thử lỗi dấu tiếng Việt, ký tự `�` hoặc `UnicodeEncodeError: ... cp1252`

1. Cập nhật đầy đủ code theo mục 11, đặc biệt `web_app.py`.
2. Dừng máy chủ cũ, chạy lại, rồi Ctrl+F5 trên trình duyệt.
3. Bản hiện tại đã buộc tiến trình kiểm thử dùng UTF-8; chỉ đổi font CSS không giải quyết được lỗi mã hoá ký tự.
4. Nếu chạy kiểm thử riêng trong Terminal, thử:

```powershell
python -X utf8 main.py test
```

Khi lưu/sửa file trong VS Code, giữ encoding **UTF-8**. Nếu vẫn lỗi, chụp phần cuối log chứa tên lỗi cụ thể, không chỉ dòng “CÓ KIỂM THỬ THẤT BẠI”.

### 10.11. Văn bản/tệp báo `n phải >= 256`

Bạn đang dùng bộ khoá slide `p=17, q=11`, có n=187. Bấm **Văn bản & tệp** hoặc **Sinh khoá 512 bit**, sau đó mã hoá lại từ bản rõ/tệp gốc bằng bộ khoá mới.

### 10.12. Không giải mã được hoặc `Modulo khoá không khớp tệp`

Kiểm tra đã chọn đúng file `.rsa` và giữ đúng p, q, e lúc mã hoá chưa. Nếu tải lại trang, đổi preset hoặc sinh lại khoá, bộ khoá có thể đã đổi. Phải nhập lại bộ khoá cũ để giải mã file cũ; khoá mới không thay thế được khoá cũ.

### 10.13. Báo p/q không nguyên tố, không có nghịch đảo hoặc M ngoài phạm vi

Với lần demo đầu, quay về **Ví dụ trong slide**, dùng p=17, q=11, e=7, M=88. Nếu tự nhập: p/q phải nguyên tố lẻ khác nhau, e phải nguyên tố cùng nhau với φ(n), M phải nằm từ 0 đến n−1. TC03 cố ý vi phạm điều kiện e để kiểm tra xử lý lỗi.

### 10.14. `ModuleNotFoundError: No module named 'rsa_core'` hoặc thiếu file dữ liệu test

Không chỉ tải riêng `main.py`, `web_app.py` hoặc `test_rsa.py`. Hãy tải/giải nén **toàn bộ dự án** rồi mở `rsa_project`. `rsa_core` là module của nhóm, không phải thứ cần cài bằng `pip install rsa_core`.

### 10.15. `FileExistsError` khi chạy demo-file/keygen

CLI cố ý không ghi đè các file kết quả. Dùng thư mục đầu ra mới, ví dụ:

```powershell
python main.py demo-file --out demo_output_2
```

Không cần xoá tệp gốc để chạy lại.

### 10.16. GitHub đã cập nhật nhưng máy vẫn hiện bản cũ/3 ca kiểm thử

GitHub và thư mục trên máy là hai bản khác nhau. Cập nhật theo mục 11, kiểm tra đang mở đúng bản `rsa_project`, rồi dừng/chạy lại Python và Ctrl+F5. Nếu có nhiều thư mục giải nén, xem đường dẫn của file đang mở trong VS Code để tránh chạy nhầm.

<a id="cap-nhat"></a>
## 11. Lấy phiên bản mới sau khi GitHub được cập nhật

### 11.1. Nếu đang dùng bản tải ZIP

1. Giữ bản cũ nếu có phần bạn tự sửa hoặc khoá/tệp demo cần dùng lại.
2. Vào repository → nhánh **main** → **Code → Download ZIP**.
3. Giải nén vào một thư mục mới để dễ phân biệt.
4. Dừng máy chủ Python của bản cũ.
5. Trong VS Code chọn **File → Open Folder**, mở `rsa_project` của bản mới.
6. Chạy lại web, rồi Ctrl+F5 trong trình duyệt.
7. Kiểm tra tab **Kiểm thử** đã có TC04 và nút **Chạy cả 4 ca kiểm thử**.

Không gõ `git init` để “sửa” việc ZIP không pull được. Nếu muốn chuyển sang cách đồng bộ bằng Git, clone một bản riêng theo mục 12.2 rồi chuyển có chọn lọc những chỉnh sửa của bạn sang bản đó.

### 11.2. Nếu đang dùng bản đã clone bằng Git

1. Lưu file bằng Ctrl+S, dừng web đang chạy.
2. Mở Terminal trong dự án, chạy:

```powershell
git status
```

3. Nếu còn file đã sửa mà chưa commit, **giữ các thay đổi đó**, hoàn thành commit ở nhánh riêng theo mục 12 hoặc sao lưu ra ngoài trước. Không dùng lệnh xoá/reset để ép đồng bộ.
4. Khi thư mục làm việc sạch, chuyển về nhánh chung:

```powershell
git switch main
```

5. Lấy bản mới:

```powershell
git pull --ff-only origin main
```

6. Chạy lại `python web_app.py`, rồi Ctrl+F5.

`Already up to date.` nghĩa là Git không thấy commit mới để kéo về nhánh đó; không có nghĩa máy chủ đang chạy đã nạp code mới. Vẫn cần khởi động lại Python nếu trước đó đã có thay đổi.

Nếu `--ff-only` báo hai lịch sử đã tách nhau, dừng tại đó và nhờ trưởng nhóm xem `git status` cùng `git log --oneline -5`. Lệnh này giúp tránh tự tạo một lần gộp ngoài ý muốn; không cần force push.

<a id="github"></a>
## 12. Hướng dẫn thành viên sửa code và commit GitHub

Chỉ cần phần này khi muốn đóng góp mã nguồn. Nếu chỉ trình bày demo, có thể chuyển thẳng đến mục 13.

### 12.1. Hiểu luồng làm việc của nhóm

**Sửa và lưu trên máy → commit → push nhánh riêng → tạo PR → trưởng nhóm xem và merge → mọi người pull main.**

| Việc vừa làm | Thay đổi đã lên bản chung `main` chưa? |
|---|---|
| Chỉ sửa file và Ctrl+S | Chưa; file mới thay đổi trên máy |
| Commit trên máy | Chưa; mới ghi lịch sử cục bộ |
| Push nhánh riêng | Đã lên GitHub, nhưng nằm ở nhánh riêng |
| Tạo PR | Đã đề nghị gộp, chưa chắc được gộp |
| PR được merge vào main | Đã có trong bản chung; các máy khác cần pull/tải mới |

Chủ repository có thể mời người khác trong **Settings → Collaborators → Add people**; thành viên cần đăng nhập đúng tài khoản và chấp nhận lời mời. Tên mục có thể hiển thị là quản lý quyền truy cập. Việc mời chỉ làm một lần cho từng thành viên.

<a id="clone"></a>
### 12.2. Clone để mỗi thành viên có bản làm việc

1. Cài **Git for Windows** từ [trang chính thức](https://git-scm.com/install/win), dùng các lựa chọn mặc định nếu không có yêu cầu riêng.
2. Đóng và mở lại VS Code/PowerShell sau khi cài.
3. Trong PowerShell, kiểm tra:

```powershell
git --version
```

4. Chuyển đến thư mục Downloads của chính tài khoản Windows đang dùng:

```powershell
cd "$env:USERPROFILE\Downloads"
```

5. Tải repository về thư mục mới tên `rsa-nhom`:

```powershell
git clone https://github.com/nguyenconghung2k6-lang/bai-tap-nhom-rsa.git rsa-nhom
```

Nếu thư mục `rsa-nhom` đã có, mở bản đã clone đó hoặc đổi tên thư mục đích mới; không clone chồng vào dự án đang làm.

6. Trong VS Code, chọn **File → Open Folder** → `Downloads` → `rsa-nhom` → **`rsa_project`**.
7. Mở Terminal mới, chạy `git status` để xác nhận Git nhận ra repository.
8. Thiết lập tên/email của **chính bạn**, chỉ cho repository này:

```powershell
git config user.name "TEN CUA BAN"
git config user.email "EMAIL CUA BAN"
```

Thay nội dung bên trong dấu nháy bằng thông tin thật trước khi chạy. Dùng email gắn với tài khoản GitHub hoặc địa chỉ noreply GitHub cung cấp nếu muốn commit được nhận đúng tác giả. Không dùng tên/email của trưởng nhóm cho mọi người.

### 12.3. Mỗi lần bắt đầu sửa: lấy bản mới và tạo nhánh

Các lệnh sau chạy trong Terminal của **`rsa_project`**. Trước hết kiểm tra không còn thay đổi dở dang bằng `git status`.

```powershell
git switch main
git pull --ff-only origin main
git switch -c tenban-sua-kiem-thu
```

Thực hiện lần lượt từng dòng. Đổi `tenban-sua-kiem-thu` thành tên nhánh dễ nhớ, không dấu, không khoảng trắng, ví dụ `hung-sua-kiem-thu`. Nếu đã có nhánh đó, chuyển vào bằng `git switch ten-nhanh-thuc-te` thay vì tạo lại.

Chỉ tạo nhánh sau khi đã xử lý hoặc lưu lại công việc dở dang; không kéo bản mới đè lên file đang sửa.

### 12.4. Sửa, lưu và kiểm tra trên máy

1. Bấm vào file được phân công trong Explorer.
2. Sửa phần cần sửa, nhấn **Ctrl+S**.
3. Nếu sửa chức năng, chạy thử đúng thao tác đó; nếu sửa Python của web, dừng/chạy lại máy chủ.
4. Chạy bộ kiểm thử:

```powershell
python main.py test
```

5. Chỉ khi kết quả đúng, tiếp tục ghi commit.
6. Xem danh sách file đã thay đổi:

```powershell
git status
```

7. Xem nội dung khác biệt:

```powershell
git diff
```

Nếu màn hình hiển thị diff có `(END)` ở cuối, nhấn **q** để thoát phần xem đó về dấu nhắc lệnh.

### 12.5. Chọn file, commit và push

Ví dụ dưới đây giả sử bạn thực sự sửa `tests/test_rsa.py` và Terminal đang ở **`rsa_project`**. Nếu sửa file khác, thay bằng đường dẫn file tương ứng tính từ thư mục này.

1. Chọn file đưa vào commit:

```powershell
git add -- tests/test_rsa.py
```

2. Xem lại phần đã chọn:

```powershell
git diff --cached
```

3. Ghi commit với mô tả công việc thật:

```powershell
git commit -m "Bo sung kiem tra RSA so lon"
```

4. Đưa nhánh lên GitHub; thay tên nhánh bằng tên đã tạo ở mục 12.3:

```powershell
git push -u origin tenban-sua-kiem-thu
```

5. Nếu Git mở trình duyệt yêu cầu đăng nhập, dùng tài khoản của chính bạn. Khi hiện **Authentication Succeeded**, quay lại Terminal và chờ lệnh push hoàn tất.

Nếu chỉ sửa README, lệnh chọn file là `git add -- README.md`. Không cần đưa `.venv`, `__pycache__`, khoá riêng hoặc tệp đầu ra demo vào commit; xem `git status` trước khi chọn file.

**Quan trọng:** thông báo đăng nhập thành công chỉ xác nhận bước đăng nhập. Muốn biết code đã được đưa lên chưa, đọc kết quả cuối của `git push` và kiểm tra nhánh trên GitHub.

### 12.6. Tạo PR để trưởng nhóm duyệt

1. Mở repository trên GitHub sau khi push thành công.
2. Bấm **Compare & pull request** nếu GitHub gợi ý nhánh vừa push.
3. Nếu không thấy, vào **Pull requests → New pull request**.
4. Chọn **base: main**, **compare: nhánh của bạn**.
5. Đọc danh sách file thay đổi để chắc đúng phần mình sửa.
6. Viết tiêu đề và mô tả ngắn: đã sửa gì, đã chạy kiểm tra nào.
7. Bấm **Create pull request**.
8. Gửi đường dẫn PR cho trưởng nhóm.

Trưởng nhóm mở PR, xem **Files changed**, kiểm tra kết quả rồi **Merge pull request → Confirm merge** nếu phù hợp. Chỉ “Approve” mà chưa merge thì thay đổi vẫn chưa vào main. Nếu có xung đột hoặc điều kiện của repository chưa đạt, cần xử lý trước khi merge.

Sau khi đã merge, các thành viên quay lại mục 11.2 để cập nhật main trên máy.

### 12.7. Nếu chỉ sửa một file ngay trên trang GitHub

1. Mở đúng repository của nhóm và đúng file trong `rsa_project`.
2. Bấm biểu tượng **bút chì / Edit**.
3. Sửa nội dung rồi bấm **Commit changes…**.
4. Ghi lời nhắn mô tả thay đổi.
5. Chọn tạo **nhánh mới** để đề nghị sửa; bấm nút xác nhận **Commit changes / Propose changes**.
6. Hoàn thành bước **Create pull request** nếu GitHub chuyển sang màn hình tạo PR.

Nếu không có quyền ghi, GitHub có thể tạo fork trong tài khoản của bạn; cần PR về repository của nhóm. Chỉ sửa ở fork không tự cập nhật bản chung.

Trình soạn thảo trên GitHub không chạy thử chương trình cho bạn. Với thay đổi code, nên tải/clone về kiểm tra trước khi gộp.

### 12.8. Xem commit ở đâu? Vì sao bạn sửa mà main chưa đổi?

- [Lịch sử commit nhánh main](https://github.com/nguyenconghung2k6-lang/bai-tap-nhom-rsa/commits/main/).
- [Danh sách pull request](https://github.com/nguyenconghung2k6-lang/bai-tap-nhom-rsa/pulls).
- Trên trang Code, đổi ô chọn nhánh từ `main` sang nhánh thành viên để xem file và commit ở nhánh đó.
- Trên máy, dùng `git log --oneline -5` để xem 5 commit gần nhất của nhánh hiện tại.

Nếu chưa thấy thay đổi, kiểm tra lần lượt: đã Ctrl+S chưa → đã commit chưa → đã push chưa → đang xem đúng repository/nhánh chưa → PR đã được **merge** chưa → máy đã pull và khởi động lại web chưa.

### 12.9. Một số lỗi Git thường gặp

| Thông báo | Cách xử lý |
|---|---|
| `git is not recognized` | Cài Git, đóng/mở Terminal mới rồi thử lại |
| `not a git repository` | Đang ở ngoài thư mục clone hoặc dùng ZIP; mở bản clone, không init thêm repo trong `rsa_project` |
| `nothing to commit, working tree clean` | Không có thay đổi đã lưu để commit; kiểm tra đúng file, thư mục và Ctrl+S |
| `Please tell me who you are` | Thiết lập `git config user.name` và `user.email` bằng thông tin của mình |
| `Permission denied` / HTTP 403 | Kiểm tra tài khoản đăng nhập, lời mời cộng tác và repository đích |
| `non-fast-forward` hoặc pull không thể fast-forward | Nhánh trên máy và GitHub có thay đổi khác nhau; giữ công việc, nhờ trưởng nhóm hỗ trợ gộp |
| `Your local changes would be overwritten` | Có chỉnh sửa chưa lưu vào lịch sử; commit ở nhánh riêng hoặc sao lưu trước khi cập nhật |
| GitHub hiện `rsa_project` như liên kết và bấm vào bị 404 | Có thể trước đây đã commit nhầm một repository lồng bên trong; nhờ trưởng nhóm kiểm tra trước khi sửa cấu trúc, không tự xoá `.git` |

Không cần khởi tạo thêm repository trong `rsa_project` sau khi đã clone; Git nhận repository từ thư mục cha `rsa-nhom`.

<a id="thuyet-trinh"></a>
## 13. Kịch bản thuyết trình gợi ý

### Trước buổi trình bày

1. Tải/pull bản mới, cài xong Python và extension khi còn Internet.
2. Mở `rsa_project`, chạy `python main.py test`; xác nhận 4 ca và đối chiếu đều đạt.
3. Chạy web, thử đủ 5 tab một lần.
4. Chuẩn bị sẵn `examples/message_vi.txt` và một ảnh nhỏ nếu muốn demo ảnh.
5. Biết vị trí Downloads để tìm file `.rsa` và file khôi phục.
6. Giữ các file code cần giải thích sẵn trong VS Code, tránh mở hàng loạt thư mục khác phiên bản.

### Trong buổi trình bày

| Thứ tự | Thao tác | Điều giải thích |
|---|---|---|
| 1 | Mở Explorer trong VS Code | Thuật toán chia module; giao diện tách khỏi lõi |
| 2 | Chạy `web_app.py` hoặc F5 cấu hình web | Đây là điểm vào cho demo giao diện |
| 3 | Tab Số nguyên, ví dụ slide | 88 → 11 → 88; mở các bước Euclid và bình phương/nhân |
| 4 | Tab Văn bản | Tiếng Việt/emoji giải mã đúng |
| 5 | Tab Tệp dữ liệu | Mã hoá một tệp thật rồi khôi phục |
| 6 | Tab Kiểm thử | 4 ca: slide, tự làm, lỗi, số lớn; đối chiếu thư viện chuẩn |
| 7 | Chỉ vào bảng thời gian và dòng TC04 | Phân biệt thời gian phép toán với tổng kiểm thử |
| 8 | Tab Tấn công | Chỉ từ n,e,C tìm p,q,d,M khi n quá nhỏ |
| 9 | Mở phần giới hạn dưới đây | Đây là mô hình học tập RSA textbook |

Nếu cần in rõ Miller–Rabin và CRT từng bước trong Terminal, chạy `python main.py number` theo mục 14.2. Web số nguyên hiện Euclid và luỹ thừa; không có bảng minh hoạ riêng mọi vòng Miller–Rabin như CLI.

<a id="dong-lenh"></a>
## 14. Các cách chạy bằng Terminal

Mọi lệnh trong mục này chạy trong **thư mục `rsa_project`**, tại dấu nhắc PowerShell. Nếu một Terminal đang chạy web, mở Terminal mới hoặc dừng web trước khi nhập lệnh khác.

### 14.1. Mở menu

```powershell
python main.py
```

| Nhập tại `Chọn:` | Chức năng |
|---|---|
| 1 | Nhập p,q,e,M và demo số nguyên từng bước |
| 2 | Nhập p,q,e rồi nhập văn bản UTF-8 |
| 3 | Demo tệp thật, tự sinh khoá |
| 4 | Chạy 4 ca kiểm thử và đối chiếu chuẩn |
| 5 | Demo sửa bản mã dựa vào tính nhân của RSA textbook |
| 6 | Đo thời gian theo kích thước dữ liệu |
| 0 | Thoát menu |

Sau mỗi giá trị phải nhấn Enter. Với mục 3, có thể Enter ở câu hỏi tệp nguồn để dùng `examples/message_vi.txt`; dùng thư mục đầu ra mới nếu đã demo trước đó.

### 14.2. Chạy trực tiếp ví dụ số nguyên

```powershell
python main.py number --p 17 --q 11 --e 7 --message 88
```

Kết quả cuối phải có:

```text
p=17; q=11; n=187; phi=160
KU=(e=7, n=187); KR=(d=23, p=17, q=11)
M=88 -> C=11 -> M'=88; CRT=88; KHỚP=True
```

Chương trình còn in các bảng Miller–Rabin minh hoạ, Euclid, bình phương/nhân, CRT và thời gian. Thêm `--quiet` vào cuối lệnh nếu muốn ẩn bảng từng bước.

Ví dụ tự làm:

```powershell
python main.py number --p 61 --q 53 --e 17 --message 65
```

Kỳ vọng `n=3233`, `d=2753`, `65 → 2790 → 65`.

<a id="demo-file"></a>
### 14.3. Tự sinh khoá và demo tệp thật trong một lệnh

```powershell
python main.py demo-file --out demo_output
```

Sau khi chạy xong, mở thư mục `demo_output` trong Explorer của VS Code:

| File được tạo | Nội dung |
|---|---|
| `public.json` | Khoá công khai |
| `private.json` | Khoá riêng của lượt demo |
| `encrypted.rsa` | Tệp đã mã hoá |
| `restored.bin` | Dữ liệu đã khôi phục đúng từng byte |

Terminal phải có **`KHỚP TỪNG BYTE=True`**. Nguồn mặc định là `examples/message_vi.txt`; có thể mở `restored.bin` trong VS Code để đọc văn bản, hoặc đổi tên bản sao sang `.txt`.

Muốn demo ảnh/tệp khác: thay đường dẫn sau `--input` bằng đường dẫn thực tế. Đường dẫn có khoảng trắng đặt trong nháy kép. Ví dụ sau chỉ dùng khi bạn đã đặt ảnh `anh_mau.png` vào thư mục `examples`:

```powershell
python main.py demo-file --input examples/anh_mau.png --out demo_output_anh
```

Với ảnh, đổi đuôi bản sao `restored.bin` thành `.png` để mở bằng trình xem ảnh. Lần chạy tiếp dùng một thư mục kết quả mới như `demo_output_2` vì chương trình từ chối ghi đè.

### 14.4. Sinh khoá rồi mã hoá/giải mã riêng

Thực hiện theo đúng thứ tự, mỗi dòng xong mới chạy dòng sau:

```powershell
python main.py keygen --bits 1024 --out keys
python main.py encrypt --key keys/public.json --input examples/message_vi.txt --output message.rsa
python main.py decrypt --key keys/private.json --input message.rsa --output restored.txt
```

Mở `restored.txt` và so với `examples/message_vi.txt`. Không sinh cặp khoá khác trước khi giải mã file vừa mã hoá.

Với chính cặp khoá đó, nhập văn bản qua Terminal bằng:

```powershell
python main.py text --public keys/public.json --private keys/private.json
```

Lần đầu dùng ví dụ này cần chưa có file `keys/public.json`, `keys/private.json`, `message.rsa`, `restored.txt`. Nếu đã có kết quả trước, dùng tên/thư mục mới và sửa các đường dẫn tương ứng trong cả chuỗi lệnh.

### 14.5. Các lệnh kiểm thử

**4 ca chính và toàn bộ đối chiếu:**

```powershell
python main.py test
```

**Chỉ 4 ca chính:**

```powershell
python -m unittest discover -s tests -v
```

**Chỉ TC04:**

```powershell
python -m unittest tests.test_rsa.RSATests.test_04_so_lon_1024_bit -v
```

**Chỉ phần đối chiếu với Python chuẩn:**

```powershell
python reference_checks.py
```

**Kiểm tra riêng demo tấn công phân tích thừa số:**

```powershell
python checks/check_factorization.py
```

Kiểm tra tấn công riêng không làm tăng số lượng 4 ca chính trong `tests/test_rsa.py`. Log mẫu ở `evidence/` là kết quả đã chạy khi đóng gói; hãy chạy lại trên máy trình bày để có số đo của chính máy đó.

### 14.6. Hai demo tấn công khác nhau

Phân tích n để tìm khoá riêng — cùng tình huống trong tab **Tấn công**:

```powershell
python main.py attack-factor --n 187 --e 7 --ciphertext 11
```

Sửa bản mã nhờ tính nhân của RSA textbook — cùng menu **mục 5**:

```powershell
python main.py attack
```

Demo thứ hai biến bản rõ giải mã từ 88 thành 176 với hệ số r=2, không phải phép phân tích thừa số. Xem [`docs/THUYET_TRINH.md`](docs/THUYET_TRINH.md) để giải thích tính nhân.

Muốn xem tất cả tham số hỗ trợ:

```powershell
python main.py --help
```

<a id="cau-truc"></a>
## 15. File nào làm việc gì?

| File / thư mục | Vai trò |
|---|---|
| `README.md` | Hướng dẫn này |
| `main.py` | Điểm vào menu và các lệnh CLI; file ngắn vì gọi `rsa_core/cli.py` |
| `web_app.py` | Máy chủ web cục bộ, nhận thao tác giao diện và gọi thuật toán |
| `web/index.html` | Nội dung và các ô/nút trên trang |
| `web/style.css` | Màu sắc, font, bố cục |
| `web/app.js` | Xử lý bấm nút, gửi yêu cầu và hiển thị kết quả |
| `rsa_core/arithmetic.py` | Euclid mở rộng, nghịch đảo modulo, bình phương và nhân |
| `rsa_core/primes.py` | Kiểm tra Miller–Rabin và sinh số nguyên tố |
| `rsa_core/keys.py` | Tạo, kiểm tra cặp khoá |
| `rsa_core/rsa.py` | RSA số nguyên, giải mã trực tiếp và CRT |
| `rsa_core/blocks.py` | Chia khối byte và khôi phục tệp |
| `rsa_core/key_io.py` | Lưu/nạp khoá JSON |
| `rsa_core/attacks.py` | Tấn công phân tích n nhỏ và demo sửa bản mã |
| `rsa_core/cli.py` | Menu, tham số lệnh, kết quả và đo thời gian CLI |
| `tests/test_rsa.py` | 4 ca kiểm thử chính |
| `tests/vectors/rsa_1024.json` | Bộ số/đáp án cố định TC04 |
| `reference_checks.py` | Đối chiếu độc lập bằng Python chuẩn |
| `checks/check_factorization.py` | Kiểm tra bổ sung cho demo tấn công |
| `examples/message_vi.txt` | Tệp tiếng Việt có sẵn để demo |
| `docs/KIEM_THU.md` | Giải thích từng ca kiểm thử |
| `docs/TAN_CONG_PHAN_TICH_THUA_SO.md` | Tình huống tấn công và các phép tính |
| `docs/THUYET_TRINH.md` | Ghi chú thuật toán và thuyết trình |
| `docs/PHAN_CONG.md` | Phân công thành viên |
| `HUONG_DAN_WEB.md` | Bản hướng dẫn web ngắn |
| `evidence/` | Log mẫu và kết quả minh chứng |
| `.vscode/` | Cấu hình chạy F5 và kiểm thử trong VS Code |
| `.gitignore` | Các loại file đầu ra/môi trường không cần đưa vào Git |

Khi trình bày giao diện: chạy `web_app.py`. Khi thầy yêu cầu giải thích thuật toán: mở module tương ứng trong `rsa_core/`, không cần tìm toàn bộ thuật toán trong `main.py`.

## 16. Phạm vi bài tập và giới hạn

- Lõi RSA và các thuật toán nền được tự cài đặt. Không gọi `pow`, `math.gcd`, `hashlib`, Crypto, cryptography hoặc OpenSSL trong lõi. `pow`/`math.gcd` dùng ở phần kiểm tra độc lập; `secrets` cung cấp số ngẫu nhiên của hệ điều hành.
- Chương trình có mã hoá/giải mã số nguyên, UTF-8 và tệp. Định dạng tệp `RSALAB1` là định dạng riêng, không phải PKCS#1/OAEP. Header giữ độ dài để khôi phục cả byte 0.
- Đây là **RSA textbook phục vụ học tập**, chưa có padding OAEP, xác thực thông điệp, chống kênh kề hoặc quản lý khoá cho sản phẩm. Không dùng để bảo vệ dữ liệu nhạy cảm.
- Nút sinh khoá trên web đang tạo **512 bit**. TC04 dùng **1024 bit** cố định. CLI cho chọn số bit khi sinh khoá, ví dụ `--bits 2048`; thời gian tăng theo độ dài khoá. “Độ dài khoá” ở đây là số bit của **n**, không phải số chữ số thập phân.
- Backend sinh khoá của web chấp nhận 512 hoặc 1024 bit; giới hạn này không phải giới hạn toán học của RSA. Hàm sinh khoá trong lõi không đặt trần bit cụ thể, nhưng chịu giới hạn thời gian và tài nguyên máy.
- Tăng số bit không tự bổ sung padding/xác thực còn thiếu. Demo chia thử n nhỏ không chứng minh phá được RSA với khoá lớn được tạo đúng cách.
- Đối chiếu đáp ứng lựa chọn **thư viện chuẩn** của đề bài. Không tự nhận bộ dữ liệu dự án là test vector NIST; RFC 8017 chỉ được dùng tham khảo công thức RSA primitive.

## 17. Tài liệu tham khảo và hướng dẫn chính thức

- Tài liệu lớp: **Chương 3 - Mã hoá khoá công khai (1).pdf**, ví dụ RSA trang 43–44; tệp PDF này không nằm trong gói mã nguồn hiện tại.
- [Python trên Windows và Python Install Manager](https://docs.python.org/3/using/windows.html).
- [Cài VS Code trên Windows](https://code.visualstudio.com/docs/setup/windows).
- [Chọn môi trường Python trong VS Code](https://code.visualstudio.com/docs/python/environments).
- [Chạy và debug Python trong VS Code](https://code.visualstudio.com/docs/python/debugging).
- [Git for Windows](https://git-scm.com/install/win).
- [Clone repository — GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
- [Sửa file trên GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).
- [Mời cộng tác viên — GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository).
- [Gộp pull request — GitHub](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/merging-a-pull-request).
- [RFC 8017, mục 5.1 — RSA primitives](https://www.rfc-editor.org/rfc/rfc8017.html#section-5.1).
- [Python `pow`](https://docs.python.org/3/library/functions.html#pow) và [Python `math.gcd`](https://docs.python.org/3/library/math.html#math.gcd).
