"""Bốn ca chính: slide, tự làm, lỗi và bộ số RSA 1024 bit cố định."""
import json
import unittest
from pathlib import Path
from time import perf_counter
from rsa_core.keys import key_from_primes
from rsa_core.rsa import encrypt_int, decrypt_int


class RSATests(unittest.TestCase):
    def test_01_vi_du_slide(self):
        """TC01: trang 43–44, p=17,q=11,e=7,M=88."""
        public, private = key_from_primes(17, 11, 7)
        cipher = encrypt_int(88, public)
        plain = decrypt_int(cipher, private)
        self.assertEqual((public.n, private.d), (187, 23))
        self.assertEqual(cipher, 11)
        self.assertEqual(plain, 88)
        self.assertEqual(decrypt_int(cipher, private, use_crt=True), 88)
        print("\n[TC01 — SLIDE] p=17, q=11, e=7, M=88")
        print(f"  Kỳ vọng: n=187, d=23, C=11, M'=88")
        print(f"  Thực tế: n={public.n}, d={private.d}, C={cipher}, M'={plain} => PASS")

    def test_02_ca_tu_lam(self):
        """TC02: bộ số ngoài ví dụ lớp, p=61,q=53,e=17,M=65."""
        public, private = key_from_primes(61, 53, 17)
        cipher = encrypt_int(65, public)
        plain = decrypt_int(cipher, private)
        self.assertEqual((public.n, private.d), (3233, 2753))
        self.assertEqual(cipher, 2790)
        self.assertEqual(plain, 65)
        self.assertEqual(decrypt_int(cipher, private, use_crt=True), 65)
        print("\n[TC02 — TỰ LÀM] p=61, q=53, e=17, M=65")
        print("  Kỳ vọng: n=3233, d=2753, C=2790, M'=65")
        print(f"  Thực tế: n={public.n}, d={private.d}, C={cipher}, M'={plain} => PASS")

    def test_03_khoa_loi(self):
        """TC03: e=2 không nguyên tố cùng nhau với phi=160."""
        expected = "Không tồn tại nghịch đảo: gcd(a, modulo) != 1."
        with self.assertRaises(ValueError) as captured:
            key_from_primes(17, 11, 2)
        self.assertEqual(str(captured.exception), expected)
        print("\n[TC03 — LỖI] p=17, q=11, e=2; phi=160; gcd(2,160)=2")
        print("  Kỳ vọng: từ chối tạo khoá, báo ValueError không tồn tại nghịch đảo")
        print(f"  Thực tế: {captured.exception} => PASS (bắt đúng lỗi mong đợi)")

    def test_04_so_lon_1024_bit(self):
        """TC04: n 1024 bit, M 80 chữ số; so đáp án cố định và giải mã CRT."""
        # Đáp án đã tính độc lập bằng Python chuẩn, không tự sinh lại mỗi lần test.
        path = Path(__file__).parent / "vectors" / "rsa_1024.json"
        vector = json.loads(path.read_text(encoding="utf-8"))
        p, q, e, message = (int(vector[name]) for name in ("p", "q", "e", "message"))
        start = perf_counter()
        public, private = key_from_primes(p, q, e)
        key_ms = (perf_counter() - start) * 1000
        start = perf_counter()
        cipher = encrypt_int(message, public)
        enc_ms = (perf_counter() - start) * 1000
        start = perf_counter()
        plain = decrypt_int(cipher, private)
        dec_ms = (perf_counter() - start) * 1000
        start = perf_counter()
        plain_crt = decrypt_int(cipher, private, use_crt=True)
        crt_ms = (perf_counter() - start) * 1000

        self.assertEqual((p.bit_length(), q.bit_length()), (512, 512))
        self.assertEqual(public.n.bit_length(), vector["bits"])
        self.assertGreater(message, 2**53 - 1)  # Vượt giới hạn số nguyên chính xác của JS.
        self.assertEqual(public.n, int(vector["n"]))
        self.assertEqual((p - 1) * (q - 1), int(vector["phi"]))
        self.assertEqual(private.d, int(vector["d"]))
        self.assertEqual(cipher, int(vector["ciphertext"]))
        self.assertEqual(plain, message)
        self.assertEqual(plain_crt, message)

        print("\n[TC04 — SỐ LỚN 1024 BIT] Bộ dữ liệu cố định, không phải vector NIST/RFC")
        print(f"  p={p}\n  q={q}\n  e={e}\n  M={message}")
        print(f"  Độ dài n={public.n.bit_length()} bit; p,q=512 bit; M={message.bit_length()} bit")
        print(f"  n={public.n}\n  d={private.d}")
        print(f"  C kỳ vọng (đã đối chiếu pow)={vector['ciphertext']}")
        print(f"  C thực tế={cipher}")
        print(f"  Giải mã thường M'={plain}\n  Giải mã CRT M'={plain_crt}")
        print(f"  Thời gian: tạo khoá từ p,q={key_ms:.4f} ms; mã hoá={enc_ms:.4f} ms; "
              f"giải mã={dec_ms:.4f} ms; giải mã CRT={crt_ms:.4f} ms")
        print("  Kết quả: n, phi, d, C khớp đáp án; cả hai cách giải mã khôi phục M => PASS")


if __name__ == "__main__":
    unittest.main(verbosity=2)
