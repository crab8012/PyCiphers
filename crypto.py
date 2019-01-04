
class Caesar():
    MAX = 26
    @classmethod
    def encode(cls, string, rotation):
        print("ENCODE")
        newString = ""
        
        rot = abs(int(rotation))%26

        print(f"String: {string}, Rotation: {rotation}, Rot: {rot}")

        for x in string:
            newChar = None
            y = ord(x)
            newOrd = y + rot
            if(newOrd > 90 and newOrd < 97):
                newOrd = (newOrd - 90) + 64
            elif(newOrd > 122):
                newOrd = (newOrd - 122) + 96

            newChar = chr(newOrd)
            print(f"BeforeC: {x}, BeforeO: {y}, NewC: {newChar}, NewO: {newOrd}")
            newString = newString + newChar
        return newString
    
    @classmethod
    def decode(cls, string, rotation):
        newString = ""
        print("DECODE")
        modRot = abs(int(rotation))%26
        rot = 0-modRot

        print(f"String: {string}, Rotation: {rotation}, Rot: {rot}")

        for x in string:
            newChar = None
            y = ord(x)
            newOrd = y + rot
            if(newOrd > 90 and newOrd < 97):
                newOrd = (123 - newOrd)
            elif(newOrd < 65):
                newOrd = (91 - newOrd)
                
            newChar = chr(newOrd)
            print(f"BeforeC: {x}, BeforeO: {y}, NewC: {newChar}, NewO: {newOrd}")
            newString = newString + newChar
        return newString

