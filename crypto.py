
class Caesar():
    MAX = 26
    @classmethod
    def encode(cls, string, rotation):
        print(f"String: {string}, Rotation: {rotation}")
        newString = ""
        rot = abs(int(rotation))
        for x in string:
            newChar = None
            if(rot > 26):
                rotate = rot % 26

            y = ord(x)+rot

            if(y > 122):
                newRot = (y - 122) + 96
                newChar = chr(newRot)
            elif(y > 90):
                newRot = (y - 90) + 64
                newChar = chr(newRot)
            else:
                newRot = y
                newChar = chr(newRot)
            print(f"BeforeC: {x}, BeforeO: {y}, NewC: {newChar}, NewO: {newRot}")
            newString = newString + newChar
        return newString

