class msgClass:
    def __init__(self, owner, dog, msg):
        self.owner = owner
        self.dog = dog
        self.msg = msg

def sendmsg(owner, dog, msg):
    file = open("msg.txt", "a")
    text = owner + '/' + dog + '/' + msg + "\n"
    file.write(text)
    file.close()

def getmsg(userId):
    file = open("msg.txt", 'r')
    msgs = []
    for line in file:
        li = line.split('/')
        if li[0] == userId:
            msgs.append(msgClass(li[0], li[1], li[2]))
    file.close()
    return msgs
