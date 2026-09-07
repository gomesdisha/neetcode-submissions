class Solution:
    def reverseBits(self, n: int) -> int:
         # '032b' formats the integer as a 32-bit binary string with leading zeros, automatically removing '0b'
        binary_str = f"{n:032b}"
        reversed_str = binary_str[::-1]
        
        # Convert the reversed binary string back to an integer using base 2
        return int(reversed_str, 2)
        