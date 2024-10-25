VOW = 'aeiouyäö'

def spoon(w1, w2):

    vpos1 = None
    w1_long = False
    w1_sp = ""
    w2_sp = ""
    l = len(w1)
    i = 0
    while i < l:
        if not vpos1 == None:
            w1_sp += w1[i]
        else:
            w2_sp += w1[i]
            if w1[i] in VOW:
                vpos1 = i
                if i+1 < l and w1[i+1] == w1[i]: # jos ekan sanan eka vokaali on pitkä
                    w1_long = True
                    i += 1
        i += 1
    if vpos1 == None:
    #    return "N/A"
        return


    vpos2 = None
    w1_sp_beg = ""
    l = len(w2)
    i = 0
    while i < l:
        if not vpos2 == None:
            w2_sp += w2[i]
        else:
            w1_sp_beg += w2[i]
            if w2[i] in VOW:
                vpos2 = i
                if w1_long:            # jos ekan sanan eka vokaali oli pitkä,
                    w1_sp_beg += w2[i] # lisää vielä toinen samanmoinen
                if i+1 < l and w2[i+1] == w2[i]:
                    w2_sp += w1[vpos1]
                    i += 1
        i += 1
    if vpos2 == None:
     #   return "N/A"
        return

    w1_sp = w1_sp_beg + w1_sp

    #w1_sp = w2[:vpos2+1] + w1[vpos1+1:]
    #w2_sp = w1[:vpos1+1] + w2[vpos2+1:]

    return w1_sp, w2_sp

if __name__ == "__main__":

    while True:
        w1 = input("Anna 1. sana: ")
        w2 = input("Anna 2. sana: ")
        print(spoon(w1, w2))