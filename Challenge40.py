def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    months = 0
    aumento = 1
    saving = 0
    if startPriceOld > startPriceNew:
        return [months, startPriceOld-startPriceNew]
    while startPriceOld + saving < startPriceNew:
        if aumento % 2 == 0:
            percentLossByMonth += 0.5
        months += 1
        aumento += 1
        saving += savingperMonth
        startPriceNew -= startPriceNew * percentLossByMonth/100
        startPriceOld -= startPriceOld * percentLossByMonth/100
        
    return [months, round(startPriceOld + saving - startPriceNew)]


print(nbMonths(2000, 8000, 1000, 1.5))