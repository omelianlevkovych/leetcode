class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        for i in range(0, len(command) - 1):
            if command[i] == "G":
                ans += "G"
            elif command[i] == "(" and command[i + 1] == "a":
                ans += "al"
            elif command[i] == "(":
                ans += "o"
        
        if command[len(command) - 1] == "G":
            ans += "G"
        
        return ans