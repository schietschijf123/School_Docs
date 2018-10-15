



def new_password(oldpassword , newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        return print(True)
    else:
        return print(False)

oldpassword = input("what was your old password:")
newpassword = input("what was your new password:")
new_password(oldpassword, newpassword)



















