class Dog:

    def __init__(self, dogId, ownId, dogName):
        self.id = dogId
        self.owner = ownId
        self.name = dogName

class Owner:

    def __init__(self, ownId, ownUser, ownPwd, ownName, ownEmail, ownPhone):
        self.id = ownId
        self.user = ownUser
        self.pwd = ownPwd
        self.name = ownName
        self.email = ownEmail
        self.phone = ownPhone


def doglist():
    file = open("dogs.txt", 'r')
    dogs = []
    for line in file:
        li = line.split('/')
        dogs.append(Dog(li[0], li[1], li[2]))
    file.close()
    return dogs


def dogfind(dogId):

    dogli = doglist()
    for dog in dogli:
        if dog.id == dogId:
            return dog
    return None

def dogbyuser(userId):
    file = open("dogs.txt", 'r')
    dogs = []
    for line in file:
        li = line.split('/')
        if li[1] == userId:
            dogs.append(Dog(li[0], li[1], li[2]))
    file.close()
    return dogs

def userlist():
    file = open("users.txt", 'r')
    users = []
    for line in file:
        li = line.split('/')
        users.append(Owner(li[0], li[1], li[2], li[3], li[4], li[5]))
    file.close()
    return users

def userfind(userId):
    userli = userlist()
    for user in userli:
        if user.id == userId:
            return user
    return None

def userlog(userUser, userPwd):
    userli = userlist()
    for user in userli:
        if (user.user == userUser) and (user.pwd == userPwd):
            return user
    return None


