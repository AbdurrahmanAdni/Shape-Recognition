import itertools 
# import GUI

global rules
global facts 
global hitRules
global allRules

# knowledge based
rules = {
    "sisi = 3 sudut = 3 " : "segitiga",
    "sisi = 4 sudut = 4 " : "segiempat",
    "sisi = 5 sudut = 5 " : "segilima",
    "sisi = 6 sudut = 6 " : "segienam",

    "segitiga sudutTerbesar < 88 " : "segitigaLancip",
    "segitiga sudutTerbesar > 92 " : "segitigaTumpul",
    "segitiga sudutTerbesar >= 88 sudutTerbesar <= 91 " : "segitigaSiku",

    "segitiga sisiSamaPanjang = 2  " : "segitigaSamaKaki",
    "segitigaSamaKaki segitigaLancip  " : "segitigaSamaKakiLancip",
    "segitigaSamaKaki segitigaTumpul  " : "segitigaSamaKakiTumpul",
    "segitigaSamaKaki segitigaSiku  " : "segitigaSamaKakiSiku",

    "segitigaSamaKakiLancip sudutTerbesar >= 58 sudutTerbesar <= 62 " : "segitigaSamaSisi",

    "segiempat pasangSisiSamaPanjang = 2 " : "jajaranGenjang",
    "segiempat pasangSisiSamaPanjang < 2 " : "trapesium",

    "jajaranGenjang pasangSisi = sama " : "segiempatBeraturan",
    "jajaranGenjang pasangSisi != sama " : "layangLayang",
    "trapesium pasangSisiSamaPanjang = 1 " : "trapesiumSamaKaki",
    "trapesium sudut90 = 2 " : "trapesiumRata",

    "trapesiumRata posisi90 = kiri " : "trapesiumRataKiri",
    "trapesiumRata posisi90 = kanan " : "trapesiumRataKanan",

    "segilima sisiSamaPanjang = 5 " : "segilimaSamaSisi",

    "segienam sisiSamaPanjang = 6 " : "segienamSamaSisi",
}

# facts list
facts = ["sisi = 3", "sudut = 3", "sudutTerbesar > 92"]

# hit rules list
hitRules = []

# Untuk menyimpan rules yang telah diproses berdasarkan fakta (akan terurut berdasarkan type engine yang akan diproses)
allRules = []

# fungsi untuk mengembalikan list of facts yang sesuai rules
def generatePatternFacts(myList):
    # inisialisasi
    patternFacts = []

    for L in range(0, len(myList)+1):
        for subset in itertools.permutations(myList, L):
            if(len(subset) > 1):
                string = ""
                for i in subset:
                    string = string + i + " " 
                patternFacts.append(string)

    return patternFacts 

# fungsi untuk mendapatkan hit rules
def getHitRules(ruleList, factList):
    global allRules
    global hitRules

    tempRules = []

    # mendapatkan semua LHS dari rules 
    rules = ruleList.keys() 

    # memasukan ke list hit rules yang baru jika fakta sesuai dengan rules dan belum pernah dibangkitkan
    for rule in rules:
        if rule in factList and rule not in allRules and rule not in hitRules:
            tempRules.append(rule)
    
    return tempRules

# fungsi untuk update facts
def updateNewFacts(rule):
    global facts
    global rules

    InsertedFact = rules.get(rule)
    facts.append(InsertedFact)

# Proses inference engine
# Hanya ada 2 tipe yaitu secara DFS atau BFS
def inferenceEngine(tipe, shape):
    global rules
    global facts 
    global hitRules
    global allRules

    print(shape)

    if(tipe == "DFS"):
        # inisialisasi proses
        factList = generatePatternFacts(facts)
        hitRules = getHitRules(rules, factList)

        while(len(hitRules) != 0):
            # inisialisasi
            tempRules = []

            # update fakta baru berdasarkan rule pada antrian pertama
            updateNewFacts(hitRules[0])
            allRules.append(hitRules[0])

            # delete rule pertama pada antrian hit rules
            del hitRules[0]

            factList = generatePatternFacts(facts)
            tempRules = getHitRules(rules, factList)

            # memasukan hasil hit rules terbaru ke depan antrian
            temp = hitRules
            del hitRules[0 : len(hitRules)]
            tempRules.extend(temp)
            hitRules = tempRules
            
            # break proses jika sudah ditemukan
            if(shape in facts):
                del hitRules[0 : len(hitRules)]

        if(len(hitRules) == 0):
            if shape in facts:
                return True
            else:
                return False
        else:
            return True

    elif(tipe == "BFS"):
        # inisialisasi proses
        factList = generatePatternFacts(facts)
        hitRules = getHitRules(rules, factList)

        while(len(hitRules) != 0):
            # inisialisasi
            tempRules = []

            # update fakta baru berdasarkan rule pada antrian pertama
            updateNewFacts(hitRules[0])
            allRules.append(hitRules[0])

            # delete rule pertama pada antrian hit rules 
            del hitRules[0]

            factList = generatePatternFacts(facts)
            tempRules = getHitRules(rules, factList)

            # memasukan hasil hit rules terbaru ke belakang antrian
            hitRules.extend(tempRules)

            # break proses jika sudah ditemukan
            if(shape in facts):
                del hitRules[0 : len(hitRules)]

        if(len(hitRules) == 0):
            if shape in facts:
                return True
            else:
                return False
        else:
            return True
    else:
        return("Tidak ada tipe")

# testing
# print(inferenceEngine("BFS", "segitigaLancip"))
# print(allRules)
# print(facts)
# # for x in rules:
#     print (x, "=>", rules[x])