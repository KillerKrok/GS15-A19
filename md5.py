import struct
from enum import Enum
from math import (
    floor,
    sin,
)
from bitarray import bitarray

class MD5(object):
    _string = None
    _A = None
    _B = None
    _C = None
    _D = None
    _hashed = None

    def __init__(self, arg=None):
        self.__md5(arg)
        
        self.digest_size = 16


    @classmethod
    def __md5(self, string):
        self._string = string

        preprocessed_bit_array = self._step_2(self._step_1())
        self._step_3()
        self._step_4(preprocessed_bit_array)
        self._step_5()

    @classmethod
    def _step_1(self):
        # Convert the string to a bit array.
        bit_array = bitarray()
        #bit_array.frombytes(self._string.encode("utf-8"))
        bit_array = self._string

        # Pad the string with a 1 bit and as many 0 bits required such that
        # the length of the bit array becomes congruent to 448 modulo 512.
        # Note that padding is always performed, even if the string's bit
        # length is already conguent to 448 modulo 512, which leads to a
        # new 512-bit message block.
        bit_array.append(1)
        while bit_array.length() % 512 != 448:
            bit_array.append(0)

        # For the remainder of the MD5 algorithm, all values are in
        # little endian, so transform the bit array to little endian.
        #return bitarray(bit_array, endian="little")
        return bit_array

    @classmethod
    def _step_2(self, step_1_result):
        # Extend the result from step 1 with a 64-bit little endian
        # representation of the original message length (modulo 2^64).
        length = (len(self._string) * 8) % pow(2, 64)
        length_bit_array = bitarray()
        length_bit_array.frombytes(struct.pack("<Q", length))

        result = step_1_result.copy()
        result.extend(length_bit_array)

        return result

    @classmethod
    def _step_3(self):
        # Initialize the buffers to their default values.
        self._A = 0x67452301
        self._B = 0xEFCDAB89
        self._C = 0x98BADCFE
        self._D = 0x10325476

    @classmethod
    def _step_4(self, step_2_result):
        # Define the four auxiliary functions that produce one 32-bit word.
        F = lambda x, y, z: (x & y) | (~x & z)
        G = lambda x, y, z: (x & z) | (y & ~z)
        H = lambda x, y, z: x ^ y ^ z
        I = lambda x, y, z: y ^ (x | ~z)

        # Define the left rotation function, which rotates `x` left `n` bits.
        rotate_left = lambda x, n: (x << n) | (x >> (32 - n))

        # Define a function for modular addition.
        modular_add = lambda a, b: (a + b) % pow(2, 32)

        # Compute the T table from the sine function. Note that the
        # RFC starts at index 1, but we start at index 0.
        T = [floor(pow(2, 32) * abs(sin(i + 1))) for i in range(64)]

        # The total number of 32-bit words to process, N, is always a
        # multiple of 16.
        N = len(step_2_result) // 32

        # Process chunks of 512 bits.
        for chunk_index in range(N // 16):
            # Break the chunk into 16 words of 32 bits in list X.
            start = chunk_index * 512
            X = [step_2_result[start + (x * 32) : start + (x * 32) + 32] for x in range(16)]

            # Convert the `bitarray` objects to integers.
            X = [int.from_bytes(word.tobytes(), byteorder="little") for word in X]

            # Make shorthands for the buffers A, B, C and D.
            A = self._A
            B = self._B
            C = self._C
            D = self._D

            # Execute the four rounds with 16 operations each.
            for i in range(4 * 16):
                if 0 <= i <= 15:
                    k = i
                    s = [7, 12, 17, 22]
                    temp = F(B, C, D)
                elif 16 <= i <= 31:
                    k = ((5 * i) + 1) % 16
                    s = [5, 9, 14, 20]
                    temp = G(B, C, D)
                elif 32 <= i <= 47:
                    k = ((3 * i) + 5) % 16
                    s = [4, 11, 16, 23]
                    temp = H(B, C, D)
                elif 48 <= i <= 63:
                    k = (7 * i) % 16
                    s = [6, 10, 15, 21]
                    temp = I(B, C, D)

                # The MD5 algorithm uses modular addition. Note that we need a
                # temporary variable here. If we would put the result in `A`, then
                # the expression `A = D` below would overwrite it. We also cannot
                # move `A = D` lower because the original `D` would already have
                # been overwritten by the `D = C` expression.
                temp = modular_add(temp, X[k])
                temp = modular_add(temp, T[i])
                temp = modular_add(temp, A)
                temp = rotate_left(temp, s[i % 4])
                temp = modular_add(temp, B)

                # Swap the registers for the next operation.
                A = D
                D = C
                C = B
                B = temp

            # Update the buffers with the results from this chunk.
            self._A = modular_add(self._A, A)
            self._B = modular_add(self._B, B)
            self._C = modular_add(self._C, C)
            self._D = modular_add(self._D, D)

    @classmethod
    def _step_5(self):
        A = bitarray(bin(self._A)[2:])
        B = bitarray(bin(self._B)[2:])
        C = bitarray(bin(self._C)[2:])
        D = bitarray(bin(self._D)[2:])

        #return bit_array
        bit_array = bitarray()
        bit_array = A + B + C + D
        self._hashed = bit_array

    def getmd5hash(self):
        return self._hashed


    def new(arg=None):
        return MD5(arg)
    