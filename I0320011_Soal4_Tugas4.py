usia = 21
a = int(input("Berapa usia Anda : "))
if usia <= a :
    print("Anda memenuhi usia")
    b = str(input("Apakah anda lulus ujian kualifikasi (Y/T) "))
    if b == "Y" :
        print("Anda boleh mengikuti kursus")
    elif b == "T" :
        print("Anda tidak boleh mengikuti kursus")

else :
    print("Anda tidak memenuhi usia")

