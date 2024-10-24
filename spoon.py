VOW = 'aeiouyäö'

def spoon(w1, w2):

    vpos1 = None
    w1_sp = ""
    w2_sp = ""
    l = len(w1)
    i = 0
    while i < l:
        if vpos1:
            w1_sp += w1[i]
        else:
            w2_sp += w1[i]
            if w1[i] in VOW:
                vpos1 = i
        i += 1
    if vpos1 == None:
    #    return "N/A"
        return


    vpos2 = None
    w1_sp_beg = ""
    l = len(w2)
    i = 0
    while i < l:
        if vpos2:
            w2_sp += w2[i]
        else:
            w1_sp_beg += w2[i]
            if w2[i] in VOW:
                vpos2 = i
        i += 1
    if vpos2 == None:
     #   return "N/A"
        return

    w1_sp = w1_sp_beg + w1_sp

    #w1_sp = w2[:vpos2+1] + w1[vpos1+1:]
    #w2_sp = w1[:vpos1+1] + w2[vpos2+1:]

    return w1_sp, w2_sp