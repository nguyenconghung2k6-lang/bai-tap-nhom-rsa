"""Các minh hoạ toán học RSA dùng khoá của bài tập."""
from .arithmetic import mod_exp, mod_inverse
from .primes import is_probable_prime
from .rsa import encrypt_int, decrypt_int

# Giới hạn bài demo chia thử, không chạy chia thử trên khoá RSA lớn.
MAX_TRIAL_MODULUS = 10**12


def factorization_attack(n, e, ciphertext):
    """Khôi phục p,q,d,M chỉ từ n,e,C bằng chia thử n nhỏ.

    Không nhận khoá riêng hay bản rõ. Mọi phép toán dùng lõi tự viết.
    Lưu 8 phép chia đầu và phép chia tìm được ước để bảng không quá dài.
    """
    if any(type(value) is not int for value in (n, e, ciphertext)):
        raise ValueError("n, e, C phải là số nguyên.")
    if not 4 < n <= MAX_TRIAL_MODULUS:
        raise ValueError(f"Demo chia thử chỉ nhận 4 < n <= {MAX_TRIAL_MODULUS}.")
    if n % 2 == 0:
        raise ValueError("Demo dùng n là tích của hai số nguyên tố lẻ khác nhau.")
    if not 1 < e < n or not 0 <= ciphertext < n:
        raise ValueError("Cần 1 < e < n và 0 <= C < n.")

    factor_trace, attempts, divisor = [], 0, 3
    while divisor * divisor <= n:
        attempts += 1
        remainder = n % divisor
        if attempts <= 8 or remainder == 0:
            factor_trace.append(dict(divisor=divisor, remainder=remainder))
        if remainder == 0:
            p, q = divisor, n // divisor
            break
        divisor += 2
    else:
        raise ValueError("Không tìm được ước: n là số nguyên tố, không phải modulo RSA hai nguyên tố.")

    if p == q or not is_probable_prime(p) or not is_probable_prime(q):
        raise ValueError("n phải là tích của đúng hai số nguyên tố lẻ khác nhau.")
    phi = (p-1)*(q-1)
    if e >= phi:
        raise ValueError("Khoá demo cần 1 < e < phi(n).")
    euclid, decrypt_trace = [], []
    d = mod_inverse(e, phi, euclid)
    message = mod_exp(ciphertext, d, n, decrypt_trace)
    verified = mod_exp(message, e, n) == ciphertext
    return dict(n=n, e=e, ciphertext=ciphertext, p=p, q=q, phi=phi, d=d,
                message=message, verified=verified, attempts=attempts,
                factor_trace=factor_trace, euclid=euclid,
                decrypt_trace=decrypt_trace)


def multiplicative_demo(public, private, message=88, factor=2):
    ciphertext = encrypt_int(message, public)
    # Kẻ sửa bản mã chỉ cần e,n và hệ số factor.
    changed = ciphertext * encrypt_int(factor, public) % public.n
    recovered = decrypt_int(changed, private)
    return dict(message=message, ciphertext=ciphertext, factor=factor,
                changed_ciphertext=changed, recovered=recovered,
                expected=message*factor % public.n)
