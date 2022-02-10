def solution(roman):
        numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        romans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        last = 0
        output = 0
        for letter in roman:
            for c in range(0, 13):
                if letter == romans[c]:
                    if last == 0: 
                        last = numbers[c]   
                        output += numbers[c]
                    else:
                        
                        if last < numbers[c]: 
                            output -= last
                            output += numbers[c] - last
                        else:
                            output += numbers[c]
                    last = numbers[c]
        return output


print(solution('MCMLXXXI')) #MCML