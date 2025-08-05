class Solution:
    def defangIPaddr(self, address: str) -> str:
        n = address.replace(".","[.]")
        return n
        