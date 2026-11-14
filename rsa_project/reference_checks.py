"""Đối chiếu chuẩn độc lập, tách khỏi bốn ca kiểm thử chính.

pow/math.gcd chỉ là oracle. Không được import module này vào thuật toán lõi.
"""
import json
import math
import random
from pathlib import Path
from rsa_core.arithmetic import extended_gcd, mod_inverse, mod_exp
from rsa_core.primes import is_probable_prime
from rsa_core.keys import key_from_primes, generate_keypair
from rsa_core.rsa import encrypt_int, decrypt_int
from rsa_core.blocks import encrypt_bytes, decrypt_bytes, block_sizes


def require(condition, label):
    # Không dùng assert: chạy Python -O vẫn thực hiện đối chiếu.
    if not condition:
        raise ValueError("Đối chiếu thất bại: " + label)


def run_reference_checks():
    print("\n=== ĐỐI CHIẾU THƯ VIỆN CHUẨN (tách khỏi TC01–TC04) ===")
    for a, b in ((240, 46), (7, 160), (-31, 12), (0, 0), (0, -5), (-5, 0)):
        g, x, y = extended_gcd(a, b)
        require(g == math.gcd(a, b) and a*x+b*y == g, "Euclid/Bezout")
    print("[math.gcd] 6 cặp và đồng nhất thức Bezout: PASS")
    for a, n in ((7, 160), (17, 3120), (-3, 11), (23, 101)):
        require(mod_inverse(a, n) == pow(a, -1, n), "nghịch đảo modulo")
    print("[pow(a,-1,n)] 4 nghịch đảo: PASS")
    rng = random.Random(20261111)
    for _ in range(120):
        a, e, n = rng.randrange(-10000, 10000), rng.randrange(1000), rng.randrange(1, 10000)
        require(mod_exp(a, e, n) == pow(a, e, n), "bình phương và nhân")
    print("[pow(a,e,n)] 120 bộ số xác định: PASS")
    for p, q, e, message in ((17, 11, 7, 88), (61, 53, 17, 65)):
        public, private = key_from_primes(p, q, e)
        cipher = encrypt_int(message, public)
        plain = decrypt_int(cipher, private)
        require(cipher == pow(message, e, public.n), "RSA mã hoá")
        require(plain == pow(cipher, private.d, public.n) == message, "RSA giải mã")
        print(f"[RSA với pow] M={message}, C tự viết={cipher}, C chuẩn={pow(message,e,public.n)}, M'={plain}: PASS")
    # Cùng bộ số TC04, nhưng đáp án được tính lại bằng pow của Python chuẩn.
    vector = json.loads((Path(__file__).parent / "tests/vectors/rsa_1024.json").read_text(encoding="utf-8"))
    p, q, e, message = (int(vector[name]) for name in ("p", "q", "e", "message"))
    n, phi = p * q, (p - 1) * (q - 1)
    expected_d = pow(e, -1, phi)
    expected_c = pow(message, e, n)
    require(n.bit_length() == vector["bits"] == 1024, "TC04 độ dài khoá")
    require((int(vector["n"]), int(vector["phi"]), int(vector["d"]), int(vector["ciphertext"]))
            == (n, phi, expected_d, expected_c), "TC04 dữ liệu đáp án cố định")
    public, private = key_from_primes(p, q, e)
    cipher = encrypt_int(message, public)
    require(private.d == expected_d and cipher == expected_c, "TC04 nghịch đảo và mã hoá")
    plain = decrypt_int(cipher, private)
    plain_crt = decrypt_int(cipher, private, use_crt=True)
    require(plain == plain_crt == pow(cipher, expected_d, n) == message, "TC04 giải mã thường/CRT/pow")
    print(f"[TC04 / pow / 1024 bit] C tự viết={cipher}")
    print(f"  C chuẩn={expected_c}")
    print(f"  d khớp pow(e,-1,phi); giải mã thường = CRT = pow = M ({message}): PASS")
    public, private = key_from_primes(17, 11, 7)
    for message in range(public.n):
        cipher = encrypt_int(message, public)
        require(cipher == pow(message, public.e, public.n), "toàn bộ đại diện RSA")
        require(decrypt_int(cipher, private) == decrypt_int(cipher, private, use_crt=True) == message,
                "RSA trực tiếp và CRT")
    print("[pow / trực tiếp / CRT] toàn bộ 187 đại diện, gồm bội của p,q: PASS")
    for n in range(2000):
        expected = n >= 2 and all(n % d for d in range(2, math.isqrt(n)+1))
        require(is_probable_prime(n, bases=[2, 3] if n >= 5 else None) == expected, "Miller–Rabin")
    print("[Chia thử độc lập] Miller–Rabin với 0..1999: PASS")
    # Các đối chiếu bổ sung cho byte/tệp và khoá sinh ngẫu nhiên.
    public, private = generate_keypair(512)
    for message in (0, 1, private.p, private.q, public.n-1, 123456789):
        cipher = encrypt_int(message, public)
        require(cipher == pow(message, public.e, public.n), "RSA 512 bit")
        require(decrypt_int(cipher, private, use_crt=True) == pow(cipher, private.d, public.n) == message,
                "giải mã RSA 512 bit")
    print("[RSA số lớn với pow] khoá sinh 512 bit, 6 bản rõ: PASS")
    b, _ = block_sizes(public.n)
    samples = [b"", b"\x00\x00A\x00\x00", "Nhóm RSA tiếng Việt 🔐".encode()]
    samples += [bytes(i % 256 for i in range(length)) for length in (1, b-1, b, b+1, 2*b)]
    samples += [(Path(__file__).parent/'examples/message_vi.txt').read_bytes()]
    for data in samples:
        require(decrypt_bytes(encrypt_bytes(data, public), private) == data, "khôi phục byte/tệp")
    print("[So sánh byte gốc] UTF-8, byte 0, ranh giới khối và tệp thật: PASS")
    print("KẾT QUẢ ĐỐI CHIẾU: TẤT CẢ KHỚP")


if __name__ == "__main__":
    run_reference_checks()
