class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st = []
        for i in s:
            if i == "#":
                if st:
                    st.pop()
            else:
                st.append(i)
        st2 = []
        for i in t:
            if i == "#":
                if st2:
                    st2.pop()
            else:
                st2.append(i)
        return st == st2
