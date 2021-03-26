def calc_bmi(weight,height):
    bmi = weight / (height * height)

    if bmi < 18.5 :
        return "低体重"
    elif bmi >= 18.5 and bmi < 25 :
        return "普通体重"
    elif bmi >= 25 :
        return "肥満"

