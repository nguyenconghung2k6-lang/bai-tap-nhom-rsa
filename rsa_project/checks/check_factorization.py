"""Kiểm tra bổ sung demo tấn công; tách khỏi 4 ca chính trong tests/."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from rsa_core.attacks import factorization_attack, MAX_TRIAL_MODULUS


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def main():
    for n, e, cipher, p, q, d, m in ((187, 7, 11, 11, 17, 23, 88),
                                    (3233, 17, 2790, 53, 61, 2753, 65)):
        result = factorization_attack(n, e, cipher)
        require((result['p'], result['q'], result['d'], result['message']) == (p, q, d, m),
                'Sai kết quả đã biết')
        require(result['verified'], 'Mã hoá ngược không khớp')
        require(result['factor_trace'][-1]['remainder'] == 0, 'Thiếu ước trong vết')
    # Toàn bộ đại diện, bao gồm 0 và bội của p/q. pow chỉ làm oracle tại checks/.
    for m in range(187):
        result = factorization_attack(187, 7, pow(m, 7, 187))
        require(result['message'] == m, f'Sai bản rõ {m}')
    for args in ((17, 7, 1), (49, 5, 1), (45, 7, 1), (187, 2, 11),
                 (187, 7, 187), (187, 7, -1), (10, 3, 1),
                 (MAX_TRIAL_MODULUS + 1, 7, 11), (True, 7, 11)):
        try:
            factorization_attack(*args)
        except ValueError:
            pass
        else:
            raise AssertionError(f'Phải từ chối đầu vào {args}')
    print('PASS: 2 ví dụ có đáp án, toàn bộ 187 bản rõ, 9 đầu vào lỗi và giới hạn demo.')


if __name__ == '__main__':
    main()
