class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Factorize t into prime factors 2, 3, 5, and 7
        a = b = c = d = 0
        temp_t = t
        for prime, count_var in [(2, 'a'), (3, 'b'), (5, 'c'), (7, 'd')]:
            cnt = 0
            while temp_t % prime == 0:
                cnt += 1
                temp_t //= prime
            if count_var == 'a': a = cnt
            elif count_var == 'b': b = cnt
            elif count_var == 'c': c = cnt
            elif count_var == 'd': d = cnt
        
        # If t has prime factors other than 2, 3, 5, 7, impossible
        if temp_t > 1:
            return "-1"
        
        # Helper: Minimum digits required to get factor powers 2^req_a * 3^req_b
        def min_digits(req_a, req_b):
            req_a = max(0, req_a)
            req_b = max(0, req_b)
            cnt = (req_a // 3) + (req_b // 2)
            ra = req_a % 3
            rb = req_b % 2
            if ra == 0 and rb == 0:
                extra = 0
            elif ra == 0 and rb == 1:
                extra = 1  # Digit 3
            elif ra == 1 and rb == 0:
                extra = 1  # Digit 2
            elif ra == 2 and rb == 0:
                extra = 1  # Digit 4
            elif ra == 1 and rb == 1:
                extra = 1  # Digit 6
            elif ra == 2 and rb == 1:
                extra = 2  # Digits 4 and 3 (or 2 and 6)
            return cnt + extra

        # Helper: Factor decomposition of a single digit
        def factor_digit(digit):
            fa = fb = fc = fd = 0
            if digit == 2: fa = 1
            elif digit == 3: fb = 1
            elif digit == 4: fa = 2
            elif digit == 5: fc = 1
            elif digit == 6: fa = 1; fb = 1
            elif digit == 7: fd = 1
            elif digit == 8: fa = 3
            elif digit == 9: fb = 2
            return fa, fb, fc, fd

        # Check if remaining length can fit the required prime factor powers
        def can_fulfill(rem_len, req_a, req_b, req_c, req_d):
            req_c = max(0, req_c)
            req_d = max(0, req_d)
            needed = min_digits(req_a, req_b) + req_c + req_d
            return needed <= rem_len

        # Greedily build the lexicographically smallest suffix
        def build_suffix(length, req_a, req_b, req_c, req_d):
            res = []
            cur_a, cur_b, cur_c, cur_d = req_a, req_b, req_c, req_d
            for pos in range(length):
                rem_pos = length - 1 - pos
                for digit in range(1, 10):
                    fa, fb, fc, fd = factor_digit(digit)
                    na, nb, nc, nd = cur_a - fa, cur_b - fb, cur_c - fc, cur_d - fd
                    if can_fulfill(rem_pos, na, nb, nc, nd):
                        res.append(str(digit))
                        cur_a, cur_b, cur_c, cur_d = na, nb, nc, nd
                        break
            return "".join(res)

        L = len(num)
        
        # Step 2: Check if `num` itself is valid
        if '0' not in num:
            cur_a, cur_b, cur_c, cur_d = a, b, c, d
            for ch in num:
                fa, fb, fc, fd = factor_digit(int(ch))
                cur_a -= fa
                cur_b -= fb
                cur_c -= fc
                cur_d -= fd
            if cur_a <= 0 and cur_b <= 0 and cur_c <= 0 and cur_d <= 0:
                return num

        # Find prefix without '0'
        first_zero = num.find('0')
        valid_prefix_len = L if first_zero == -1 else first_zero

        # Precompute cumulative factors along the valid prefix
        pref_a = [0] * (valid_prefix_len + 1)
        pref_b = [0] * (valid_prefix_len + 1)
        pref_c = [0] * (valid_prefix_len + 1)
        pref_d = [0] * (valid_prefix_len + 1)

        for i in range(valid_prefix_len):
            fa, fb, fc, fd = factor_digit(int(num[i]))
            pref_a[i+1] = pref_a[i] + fa
            pref_b[i+1] = pref_b[i] + fb
            pref_c[i+1] = pref_c[i] + fc
            pref_d[i+1] = pref_d[i] + fd

        # Step 3: Try to find a valid number of length L
        for i in range(valid_prefix_len, -1, -1):
            if i == L:
                continue
            
            start_digit = int(num[i]) + 1
            rem_len = L - 1 - i
            
            cur_req_a = a - pref_a[i]
            cur_req_b = b - pref_b[i]
            cur_req_c = c - pref_c[i]
            cur_req_d = d - pref_d[i]

            for digit in range(start_digit, 10):
                fa, fb, fc, fd = factor_digit(digit)
                na = cur_req_a - fa
                nb = cur_req_b - fb
                nc = cur_req_c - fc
                nd = cur_req_d - fd

                if can_fulfill(rem_len, na, nb, nc, nd):
                    prefix_str = num[:i] + str(digit)
                    suffix_str = build_suffix(rem_len, na, nb, nc, nd)
                    return prefix_str + suffix_str

        # Step 4: If length L fails, build minimal valid number of larger length
        min_req_len = min_digits(a, b) + max(0, c) + max(0, d)
        target_len = max(L + 1, min_req_len)
        return build_suffix(target_len, a, b, c, d)