VOW = 'aeiouyäö'
FRONT = 'äöy'
BACK = 'aou'
NEUTRAL = 'ie'
#OPEN_ENDS= 'eoö'

# harmoniset sanakirjat
ftb = {'ä':'a', 'ö':'o', 'y':'u'}
btf = {'a':'ä', 'o':'ö', 'u':'y'}

# piirrekorjaussanakirja
featadj = {'io':'ie', 'iö':'ie', 'ue':'uo', 'ye':'yö'}

def spoon(w1, w2):

    #vokaaliharmoniatesti:
    #if w1 == "kota" and w2 == "sintti":
    #    return [("sitä", "kontti"), ("sita", "kontti")]

    vpos1 = None
    w1_long = False
    w2_long = False
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
    #    return "N/A", sanassa ei ollut vokaalia, ei voida muuntaa mielekkäästi
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
                    w2_long = True
                    w2_sp += w1[vpos1]
                    i += 1
        i += 1
    if vpos2 == None:
     #   return "N/A"
        return

    w1_sp = w1_sp_beg + w1_sp



    #piirrekorjailu:

    #ensin laillistetaan diftongit ensimmäiselle sanalle:
    seq = w1_sp[vpos2:vpos2+2]
    if not w1_long and seq in featadj:
        w1_sp = w1_sp.replace(seq, featadj[seq])

    # sitten vokaaliharmonia ensimmäiselle sanalle
    w1_sp_candidates = set()
    result = ""
    dec_vow = w2[vpos2] # deciding vowel
    if dec_vow in FRONT or dec_vow in NEUTRAL:
        for i in range(len(w1_sp)):
            c = w1_sp[i]
            result += btf[c] if c in btf else c
        w1_sp_candidates.add(result)
        result = ""

    if dec_vow in BACK or dec_vow in NEUTRAL:
        for i in range(len(w1_sp)):
            c = w1_sp[i]
            result += ftb[c] if c in ftb else c
        w1_sp_candidates.add(result)

    #laillistetaan diftongit toiselle sanalle:
    seq = w2_sp[vpos1:vpos1+2]
    if not w2_long and seq in featadj:
        w2_sp = w2_sp.replace(seq, featadj[seq])

    # sitten vokaaliharmonia toiselle sanalle
    w2_sp_candidates = set()
    result = ""
    dec_vow = w1[vpos1] # deciding vowel
    if dec_vow in FRONT or dec_vow in NEUTRAL:
        for i in range(len(w2_sp)):
            c = w2_sp[i]
            result += btf[c] if c in btf else c
        w2_sp_candidates.add(result)
        result = ""

    if dec_vow in BACK or dec_vow in NEUTRAL:
        for i in range(len(w2_sp)):
            c = w2_sp[i]
            result += ftb[c] if c in ftb else c
        w2_sp_candidates.add(result)

    # kootaan muunnosvaihtoehdot (max 4?) yhteen
    candidates = [(w1, w2) for w1 in w1_sp_candidates for w2 in w2_sp_candidates]

    # joku vanha alustava ratkaisu:
    #w1_sp = w2[:vpos2+1] + w1[vpos1+1:]
    #w2_sp = w1[:vpos1+1] + w2[vpos2+1:]

    return candidates

if __name__ == "__main__":

    while True:
        w1 = input("Anna 1. sana: ")
        w2 = input("Anna 2. sana: ")
        print(spoon(w1, w2))