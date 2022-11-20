from itertools import pairwise, groupby

start = list(str(125730))
end = list(str(579381))

# should convert to generator if memory is an issue
non_decreasing = []

# flatten any decreasing values for start
for i, (prev, next) in enumerate(pairwise(start)):
    if next < prev:
        start = start[:i] + [prev] * (6 - i)
        break

non_decreasing.append(start)
digits = start[:]

# find remaining non-decreasing numbers (really sloppy 😬)
while digits < end:
    # 1. increment last digit
    digit = str(int(digits[-1]) + 1)
    # *. if we incremented into a 9 from (.3), we could end up at '10' here
    # just reset 
    if digit == '10': 
        digit = '9'
    else: 
        digits[-1] = digit
        # append a copy of digits to remove any references to modified [-1] digit
        non_decreasing.append(digits[:])
    # if last digit was 9, increment next non-9 and flatten
    if digit == '9':
        # 2. find next non-9
        i = 5
        while digits[i] == '9':
            i -= 1
        # 3. increment and flatten
        digit = str(int(digits[i]) + 1)
        digits = digits[:i] + [digit] * (6 - i)
        # check if overshot end
        if digits < end:
            non_decreasing.append(digits[:])

def part_one():
    print(
        sum(
            [
                any([a == b for (a, b) in pairwise(number)])
                for number in non_decreasing
            ]
        )        
    )

def part_two():
    print(
        sum(
            [ 
                2 in [len(list(group)) for _, group in groupby(number)]
                for number in non_decreasing  
            ]
        )
    )    

part_one()
part_two()