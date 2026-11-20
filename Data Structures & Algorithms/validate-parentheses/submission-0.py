class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        closeToOpen = {")" : "(","]" : "[", "}" : "{" }
        for char in s:
            if char in closeToOpen:
                if st and st[-1] == closeToOpen[char]:
                    st.pop()
                else:
                    return False
            else:
                st.append(char)
        return True if not st else False