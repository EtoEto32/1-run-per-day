class User:
    def __init__(self, nickname, old, birth, state):
        self.nickname = nickname
        self.old = old
        self.birth = birth
        self.state = state

    def __str__(self):
        return f"""User{{
nickname : {self.nickname}
old : {self.old}
birth : {self.birth}
state : {self.state}
}}"""


n = int(input())
users = []
for _ in range(n):
    nickname, old, birth, state = input().split()
    user = User(nickname, old, birth, state)
    users.append(user)
for user in users:
    print(user)
