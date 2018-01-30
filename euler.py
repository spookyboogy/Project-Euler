#!/usr/bin/env python3
##
## Euler problems
##

from copy import deepcopy
from math import sqrt, floor, ceil, factorial
from numpy import arange
from decimal import *

def is_odd(n):

    """Returns True if n is odd, False otherwise."""
    if n//2 == n/2:
        return False
    return True


def is_prime(n):

    """Returns True if n is prime, False otherwise."""

    if n == 2:
        return True
    elif not is_odd(n) or n <= 1:
        return False

    for i in range(2, ceil(sqrt(n)) + 1):
        if n//i == n/i:
            return False

    return True

def one():

    """Find the sum of all the multiples of 3 or 5 below 1000."""

    n = sum(range(3,1000,3)) + sum(range(5,1000,5)) - \
        sum(range(15,1000,15))

    return n

def two(n):

    """ Compute the sum of the even fibonnaci numbers <= n """

    def fib(n):
        fibs = []
        a = b = 1
        while b <= n:
            fibs += [b]
            temp = b
            b += a
            a = temp
        return fibs

    fibs = fib(n)
    even_fibs = [i for i in fibs if i//2 == i/2]

    print(fibs)
    print(even_fibs)
    return sum(even_fibs)


def three(n):

    """Find the greatest prime factor of n."""

    prime_factor = 1

    for i in range(3, ceil(sqrt(n)), 2):
        if n//i == n/i:
            if is_prime(i):
                prime_factor = i

    return prime_factor




def four():

    """
    Find the largest palindrome number made from the
    product of two 3-digit numbers.
    """

    def is_palindrome(n):

        "n -> str(n)"

        if len(n) <= 2:
            return False
        else:
            for i in range((len(n)//2)):
                if n[i] != n[len(n) - 1 - i]:
                    return False
            return True

    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(str(i * j)):
                palindromes += [i * j]
    return max(palindromes)


def five():

    """
    Find the smallest positive integer evenly divisible by
    the first 20 integers.
    """

    n0 = 1*2*3*5*7*11*13*17*19; i = 1;

    divisors = [4, 6, 8, 9, 10, 12,
                14, 15, 16, 18, 20]

    found = False
    while not found:

        i += 1
        n = n0 * i

        happyflag = False #should be outside of the while loop, I think
                          #can condense found and happyflag into one flag

        for d in divisors:
            if n//d != n/d:
                break
            else:
                if d == 20 and n//d == n/d:
                    happyflag = True

        if happyflag:
            found = True

    return n


def six():

    """Find the difference between the... yeah.. whatever.."""

    sum_of_squares = sum([i**2 for i in range(101)])
    square_of_sums = sum([i for i in range(101)]) ** 2

    return sum_of_squares - square_of_sums


def seven():

    """Find the 10,001st prime number."""

    i = 1
    n = 3

    while i < 10001:
        if is_prime(n):
            print("{}. {}".format(i, n))
            i += 1
        n += 2

    return n


def eight():

    """
    Find the largest product of ten consecutive digits in
    the following 1000-digit integer.
    """

    n = (
        '73167176531330624919225119674426574742355349194934'
        '96983520312774506326239578318016984801869478851843'
        '85861560789112949495459501737958331952853208805511'
        '12540698747158523863050715693290963295227443043557'
        '66896648950445244523161731856403098711121722383113'
        '62229893423380308135336276614282806444486645238749'
        '30358907296290491560440772390713810515859307960866'
        '70172427121883998797908792274921901699720888093776'
        '65727333001053367881220235421809751254540594752243'
        '52584907711670556013604839586446706324415722155397'
        '53697817977846174064955149290862569321978468622482'
        '83972241375657056057490261407972968652414535100474'
        '82166370484403199890008895243450658541227588666881'
        '16427171479924442928230863465674813919123162824586'
        '17866458359124566529476545682848912883142607690042'
        '24219022671055626321111109370544217506941658960408'
        '07198403850962455444362981230987879927244284909188'
        '84580156166097919133875499200524063689912560717606'
        '05886116467109405077541002256983155200055935729725'
        '71636269561882670428252483600823257530420752963450'
        )

    res = 0
    for i in range(len(n) - 12):
        factors = [int(j) for j in n[i:i+13]]
        product = 1
        for i in factors:
            product *= i
        if product >= res:
            res = product
    return res


def nine():

    """
    Find the product of the pythagorean triplet for which
    a^2 + b^2 = c^2 ; a + b + c = 1000.
    """

    for a in range(500):
        for b in range(500):
            c = sqrt(a**2 + b**2)
            if c == int(c):
                if a + b + c == 1000:
                    return a, b, c, int(a*b*c)


def ten():

    """Find the sum of the primes less than 2x10^6."""

    primes_sum = 2
    n = 1
    i = 1

    while n < 2E6:
        n += 2
        if is_prime(n):
            i += 1
            primes_sum += n
            print("{}. {}    sum = {}"
                  .format(i, n, primes_sum))

    return i, n, primes_sum


def eleven():

    """
    Find the greatest product of four adjacent numbers in the
    same direction (up, down, left, right, or diagonally)
    in the 20×20 matrix.
    Caution: Very painful to read. Very unreadable.
    Also: Would be cool to generalize this to search variable
          lengths in variably sized matrices.
    """

    m = [
        [ 8, 2,22,97,38,15, 0,40, 0,75, 4, 5, 7,78,52,12,50,77,91, 8],
        [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48, 4,56,62, 0],
        [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30, 3,49,13,36,65],
        [52,70,95,23, 4,60,11,42,69,24,68,56, 1,32,56,71,37, 2,36,91],
        [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
        [24,47,32,60,99, 3,45, 2,44,75,33,53,78,36,84,20,35,17,12,50],
        [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
        [67,26,20,68, 2,62,12,20,95,63,94,39,63, 8,40,91,66,49,94,21],
        [24,55,58, 5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
        [21,36,23, 9,75, 0,76,44,20,45,35,14, 0,61,33,97,34,31,33,95],
        [78,17,53,28,22,75,31,67,15,94, 3,80, 4,62,16,14, 9,53,56,92],
        [16,39, 5,42,96,35,31,47,55,58,88,24, 0,17,54,24,36,29,85,57],
        [86,56, 0,48,35,71,89, 7, 5,44,44,37,44,60,21,58,51,54,17,58],
        [19,80,81,68, 5,94,47,69,28,73,92,13,86,52,17,77, 4,89,55,40],
        [ 4,52, 8,83,97,35,99,16, 7,97,57,32,16,26,26,79,33,27,98,66],
        [88,36,68,87,57,62,20,72, 3,46,33,67,46,55,12,32,63,93,53,69],
        [ 4,42,16,73,38,25,39,11,24,94,72,18, 8,46,29,32,40,62,76,36],
        [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74, 4,36,16],
        [20,73,35,29,78,31,90, 1,74,31,49,71,48,86,81,16,23,57, 5,54],
        [ 1,70,54,71,83,51,54,69,16,92,33,48,61,43,52, 1,89,19,67,48]
        ]

    greatest_product = 0
    # horizontal test
    for row in range(len(m)):
        for col in range(len(m[row]) - 3):
            product = 1
            for i in m[row][col:col+4]:
                product *= i
            if product >= greatest_product:
                greatest_product = product
    #vertical test
    for col in range(len(m[0])):
        for row in range(len(m) - 3):
            product = 1
            quadruple = []
            for i in range(4):
                quadruple += [m[row+i][col]]
            for i in quadruple:
                product *= i
            if product >= greatest_product:
                greatest_product = product
    #left-to-right diagonal test
    for matrix_index in [0,1]:
        pos0 = [0, 0]
        for index in range(len(m)-3):
            pos0[matrix_index] = index
            pos = [pos0[0], pos0[1]]
            while pos[0] < len(m)-3 and pos[1] < len(m[0])-3:
                product = 1
                quadruple = []
                for i in range(4):
                    quadruple += [m[pos[0]+i][pos[1]+i]]
                for i in quadruple:
                    product *= i
                if product >= greatest_product:
                    greatest_product = product
                pos[0] += 1; pos[1] += 1
    #right-to-left diagonal test
    for matrix_index in [0,1]:
        pos0 = [0, len(m[0])-1]
        for index in range(len(m)-3):
            if matrix_index == 0:
                pos0[matrix_index] = index
            else:
                pos0[matrix_index] = len(m[0]) - 1 -index
            pos = [pos0[0], pos0[1]]
            while pos[0] < len(m)-3 and pos[1] > 2:
                product = 1
                quadruple = []
                for i in range(4):
                    quadruple += [m[pos[0]+i][pos[1]-i]]
                for i in quadruple:
                    product *= i
                if product >= greatest_product:
                    greatest_product = product
                pos[0] += 1; pos[1] -= 1

    return greatest_product

def twelve():

    """
    Find the first triangle number to have over 500 divisors.
    Very inefficient algorithm.
    Better way is to improve the number_of_divisors function
    by doing a check for parity and whatever else and
    start the divs testing at some efficient lower bound
    Whatever. i=12375 is the answer.
    """

    triangle_number = 1
    divisors = 1
    i = 1

    def number_of_divisors(n):

        divisors = 1
        for i in range(1, ceil(n/2)+ 1):
            if n//i == n/i:
                divisors += 1
        return divisors

    while divisors <= 500:
        i += 1
        triangle_number += i
        #if i > 8500:
        if not is_odd(triangle_number):
            divisors = number_of_divisors(triangle_number)

    return triangle_number, divisors


def thirteen():

    """
    Find the first ten digits of the sum of these 100 50-digit
    numbers. This would be a task using C or another language,
    but there is no INT_MAX in python, ie integers can be
    arbitrarily large.
    """

    l = [37107287533902102798797998220837590246510135740250,
         46376937677490009712648124896970078050417018260538,
         74324986199524741059474233309513058123726617309629,
         91942213363574161572522430563301811072406154908250,
         23067588207539346171171980310421047513778063246676,
         89261670696623633820136378418383684178734361726757,
         28112879812849979408065481931592621691275889832738,
         44274228917432520321923589422876796487670272189318,
         47451445736001306439091167216856844588711603153276,
         70386486105843025439939619828917593665686757934951,
         62176457141856560629502157223196586755079324193331,
         64906352462741904929101432445813822663347944758178,
         92575867718337217661963751590579239728245598838407,
         58203565325359399008402633568948830189458628227828,
         80181199384826282014278194139940567587151170094390,
         35398664372827112653829987240784473053190104293586,
         86515506006295864861532075273371959191420517255829,
         71693888707715466499115593487603532921714970056938,
         54370070576826684624621495650076471787294438377604,
         53282654108756828443191190634694037855217779295145,
         36123272525000296071075082563815656710885258350721,
         45876576172410976447339110607218265236877223636045,
         17423706905851860660448207621209813287860733969412,
         81142660418086830619328460811191061556940512689692,
         51934325451728388641918047049293215058642563049483,
         62467221648435076201727918039944693004732956340691,
         15732444386908125794514089057706229429197107928209,
         55037687525678773091862540744969844508330393682126,
         18336384825330154686196124348767681297534375946515,
         80386287592878490201521685554828717201219257766954,
         78182833757993103614740356856449095527097864797581,
         16726320100436897842553539920931837441497806860984,
         48403098129077791799088218795327364475675590848030,
         87086987551392711854517078544161852424320693150332,
         59959406895756536782107074926966537676326235447210,
         69793950679652694742597709739166693763042633987085,
         41052684708299085211399427365734116182760315001271,
         65378607361501080857009149939512557028198746004375,
         35829035317434717326932123578154982629742552737307,
         94953759765105305946966067683156574377167401875275,
         88902802571733229619176668713819931811048770190271,
         25267680276078003013678680992525463401061632866526,
         36270218540497705585629946580636237993140746255962,
         24074486908231174977792365466257246923322810917141,
         91430288197103288597806669760892938638285025333403,
         34413065578016127815921815005561868836468420090470,
         23053081172816430487623791969842487255036638784583,
         11487696932154902810424020138335124462181441773470,
         63783299490636259666498587618221225225512486764533,
         67720186971698544312419572409913959008952310058822,
         95548255300263520781532296796249481641953868218774,
         76085327132285723110424803456124867697064507995236,
         37774242535411291684276865538926205024910326572967,
         23701913275725675285653248258265463092207058596522,
         29798860272258331913126375147341994889534765745501,
         18495701454879288984856827726077713721403798879715,
         38298203783031473527721580348144513491373226651381,
         34829543829199918180278916522431027392251122869539,
         40957953066405232632538044100059654939159879593635,
         29746152185502371307642255121183693803580388584903,
         41698116222072977186158236678424689157993532961922,
         62467957194401269043877107275048102390895523597457,
         23189706772547915061505504953922979530901129967519,
         86188088225875314529584099251203829009407770775672,
         11306739708304724483816533873502340845647058077308,
         82959174767140363198008187129011875491310547126581,
         97623331044818386269515456334926366572897563400500,
         42846280183517070527831839425882145521227251250327,
         55121603546981200581762165212827652751691296897789,
         32238195734329339946437501907836945765883352399886,
         75506164965184775180738168837861091527357929701337,
         62177842752192623401942399639168044983993173312731,
         32924185707147349566916674687634660915035914677504,
         99518671430235219628894890102423325116913619626622,
         73267460800591547471830798392868535206946944540724,
         76841822524674417161514036427982273348055556214818,
         97142617910342598647204516893989422179826088076852,
         87783646182799346313767754307809363333018982642090,
         10848802521674670883215120185883543223812876952786,
         71329612474782464538636993009049310363619763878039,
         62184073572399794223406235393808339651327408011116,
         66627891981488087797941876876144230030984490851411,
         60661826293682836764744779239180335110989069790714,
         85786944089552990653640447425576083659976645795096,
         66024396409905389607120198219976047599490197230297,
         64913982680032973156037120041377903785566085089252,
         16730939319872750275468906903707539413042652315011,
         94809377245048795150954100921645863754710598436791,
         78639167021187492431995700641917969777599028300699,
         15368713711936614952811305876380278410754449733078,
         40789923115535562561142322423255033685442488917353,
         44889911501440648020369068063960672322193204149535,
         41503128880339536053299340368006977710650566631954,
         81234880673210146739058568557934581403627822703280,
         82616570773948327592232845941706525094512325230608,
         22918802058777319719839450180888072429661980811197,
         77158542502016545090413245809786882778948721859617,
         72107838435069186155435662884062257473692284509516,
         20849603980134001723930671666823555245252804609722,
         53503534226472524250874054075591789781264330331690]

    return int(str(sum(l))[:10])


def fourteen():

    """
    Find the longest collatz sequence with the first term below
    1 million.
    """

    def collatz(n):

        if is_odd(n):
            n = (3*n) + 1
        else:
            n = n/2

        return int(n)

    c0_max = 0; greatest_length = 0

    for c in range(2, int(1E6)):

        c0 = c
        length = 1
        while c > 1:
            c = collatz(c)
            length += 1
        if length > greatest_length:
            greatest_length = length; c0_max = c0

    return c0_max, greatest_length


def fifteen():

    """
    Starting in the top left corner of a 2×2 grid, and only being
    able to move to the right and down, there are exactly 6 routes
    to the bottom right corner. Find the number of such routes are
    through a 20×20 grid. The answer is 2nCn for an nxn grid, so
    programming a solution isn't really necessary.
    """

    return int(factorial(40)/(factorial(20)**2))


def sixteen():

    """ Find the sum of the digits of 2**1000."""

    return sum([int(i) for i in str(2**1000)])


def seventeen():

    """
    Find the number of letters used to write in words the numbers
    1 through 1000 (inclusive), not counting spaces or hyphens, and
    including the use of the word and as in "one hundred and
    fifteen" (20 letters). I wrote this in an exhaustive/shitty way.
    It could be better written using recursion and allowing for
    numbers greater than 1000.
    """

    l0 = ["", "one", "two", "three", "four", "five", "six", "seven",
          "eight", "nine"]

    l1 = ["", "ten", "eleven", "twelve", "thirteen", "fourteen",
          "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    l2 = ["ten", "twenty", "thirty", "forty", "fifty", "sixty",
          "seventy", "eighty", "ninety"]

    count = 0

    for i in range(1, 1001):
        i = str(i)
        if len(i) == 1:
            word = l0[int(i)]
        elif len(i) == 2:
            if int(i[0]) == 1:
                word = l1[int(i) - 9]
            else:
                word = l2[int(i[0]) - 1] + l0[int(i[1])]
        else:
            if len(i) == 3:
                word = l0[int(i[0])] + "hundred"
                if int(i[1]) == 0:
                    if int(i[2]) != 0:
                        word += "and" + l0[int(i[2])]
                elif int(i[1]) == 1:
                    word += "and" + l1[int(i[2]) - 10]
                else:
                    word += "and" + l2[int(i[1]) - 1] + l0[int(i[2])]
            else: #janky
                word = "onethousand"
        count += len(word)
        print(i, word, len(word))

    return count


def eighteen():

    """
    Find the maximum sum generated by starting at the top
    of the triangle below and moving to adjacent numbers on
    the row below it (meaning the numbers below or to the right)
    (meaning numbers with the same row index or an index greater).
    """

    t = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
        ]

    tt = deepcopy(t)

    for row in range(len(t))[::-1]:
        for index in range(len(t[row])-1):
            t[row-1][index] += max(t[row][index], t[row][index + 1])

    total = tt[0][0]
    ind = 0
    for row in range(1, len(tt)):
        ind = t[row].index(max(t[row][ind], t[row][ind + 1]))
        total += tt[row][ind]

    return total

def nineteen():

    """
    Find the number of sundays that fell on the first of the month
    in the twentieth century, ie between 1 Jan 1901 - 31 Dec 2000.
    1 Jan 1900 was a monday. Leap years occur on years evenly
    divisible by 4 and on centuries if divisble by 400.
    Feb. has 29 days on leap years.
    """

    sun_count = 0

    cur_day = 2 # Monday
    cur_month = 1 # Jan = 1, Feb = 2, ...
    cur_year = 1900

    weekdays = [0, 1, 2, 3, 4, 5, 6] # Sun = 1, Mon = 2, ...
    month_lengths = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    while cur_year <= 2000:
        cur_month = 1
        if cur_year//4 == cur_year/4:
            month_lengths[1] = 29
        else:
            month_lengths[1] = 28
        while cur_month <= 12:
            for day in range(1, month_lengths[cur_month - 1]):
                if cur_day == 1 and day == 1 and cur_year != 1900:
                    sun_count += 1
                else:
                    pass
                if cur_day == 7:
                    cur_day = 1
                else:
                    cur_day += 1
            cur_month +=1
        cur_year += 1
    return sun_count


def twenty():

    """
    Find the sum of the digits in the number 100!
    """

    return sum([int(i) for i in str(factorial(100))])


def twentyone():

    """
    Let d(n) be defined as the sum of proper divisors of n
    (numbers less than n which divide evenly into n). If d(a) = b
    and d(b) = a, where a != b, then a and b are an amicable pair
    and each of a and b are called amicable numbers. Find the
    sum of all amicable numbers under 10000."
    """

    amicables = []

    def d(n):

        d_vals = []
        if n in [0, 1]:
            pass
        else:
            for i in range(1, ceil(n/2)+1):
                if n//i == n/i:
                    d_vals += [i]
        return sum(d_vals)


    for a in range(int(1E4)):
        b = d(a)
        if a != b and a == d(b):
            amicables += [a, b]

    return sum(set(amicables))


def twentytwo():

    """
    Using the file p022_names.txt, a file container over 5k names,
    begin by sorting it into alphabetical order. Then working out
    the alphabetical value for each name, multiply this value by its
    alphabetical position in the list to obtain a name score.
    For example, when the list is sorted into alphabetical order,
    COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name
    in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
    What is the total of all the name scores in the file?
    """

    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    def score(name):
        return sum([alphabet.index(i)+1 for i in name])

    f = open('p022_names.txt', 'r')
    names = f.read().split(',')
    names = sorted([name.strip('"') for name in names])

    score_total = 0
    for name in names:
        score_total += score(name) * (names.index(name) + 1)
    return score_total


def twentythree():

    """
    A perfect number is one for which the sum of its proper divisors is
    equal to the number. A deficient number is one for which the sum is
    less than the number, and a number is abundant if the sum exceeds the
    number. As 12 is the smallest abundant number, the smallest number that
    can be written as the sum of two abundant numbers is 24. It can be shown
    that all integers greater than 28123 can be written as the sum of two
    abundant numbers. However, this upper limit cannot be reduced any
    further by analysis even though it is known that the greatest number
    that cannot be expressed as the sum of two abundant numbers is less
    than this limit. Find the sum of all the positive integers which cannot
    be written as the sum of two abundant numbers.
    """

    def divisors(n):

        return sum([i for i in range(1, ceil(n/2)+1) if n//i == n/i])

    abundants = list(i for i in range(28124) if divisors(i) > i)
    abundant_sums = []

    print("{}\n{}\n{}\n..."
          .format(abundants[:10], abundants[10:20], abundants[20:30]))
    print(len(abundants))

    for i in range(len(abundants)):
        a = abundants[i]
        for j in range(len(abundants[i:])):
            b = abundants[j]
            if (a + b) < 28123:
                abundant_sums += [a + b]

    return sum([i for i in range(28124) if i not in abundant_sums])

    ## This works but should be optimized beacuse it takes ~10 mins


def twentyfour():

    """
    A permutation is an ordered arrangement of objects.
    For example, 3124 is one possible permutation of the digits
    1, 2, 3 and 4. If all of the permutations are listed numerically
    or alphabetically, we call it lexicographic order. The lexicographic
    permutations of 0, 1 and 2 are:   012   021   102   120   201   210
    What is the millionth lexicographic permutation of the digits
    0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """

    s = '0123456789'
    ss = '0123456789'
    magic_number = ''
    place = 1
    indexes = []
    perms_left = 1E6

    while perms_left > 0 and place <= 10:

        print("\ns = {}, n = {}".format(s, magic_number))
        f_of_interest = len(s) - 1
        f_factor = floor(perms_left/factorial(f_of_interest))
        indexes += [f_factor]

        magic_number += s[f_factor]
        s = s[:f_factor] + s[f_factor + 1:]

        print("Place = {}\nPerms left = {}\n{}! = {}\n{}/{}! = {}"
              .format(place, perms_left, f_of_interest,
                      factorial(f_of_interest),
                      perms_left, f_of_interest, f_factor))
        print("indexes = {}".format(indexes))
        print("s = {}, n = {}\n".format(s, magic_number))

        perms_left -= f_factor * factorial(f_of_interest)
        place += 1

    ##
    ## indexes should result as [2, 6, 6, 2, 5, 1, 2, 1, 1]
    ## instead of               [2, 6, 6, 2, 5, 1, 2, 2, 0]
    ## because it's impossible to arrange something 0 ways.
    ## answer found by hand is 2783915460. moving on...
    ##


def twentyfive():

    """
    Find the sequence index of the first fibonnaci number to contain
    1000 digits.
    """

    a = 1; b = 1; i = 2
    while len(str(b)) < 1000:
        a, b = b, b+a
        i += 1
    return i


def twentysix():

    """
    Find the value of d < 1000 for which 1/d contains the longest
    recurring cycle in its decimal fraction part.
    """

    getcontext().prec = 5000
    periods = []

    for i in range(3, 1000):

        dec = str(Decimal(1)/Decimal(i))

        if len(dec) < 5000:
            pass
        else:
            if i < 10:
                start_ind = 2
            elif i > 10 and i < 100:
                start_ind = 3
            else:
                start_ind = 4

            pattern_found = False
            for start_shift in range(500):
                if pattern_found:
                    break
                start_ind += start_shift

                for t_len in range(1, 2500):
                    test_pattern = dec[start_ind : start_ind + t_len]
                    test = dec[start_ind + t_len : start_ind +(2*t_len)]
                    if test_pattern == test:
                        periods += [(i, len(test_pattern))]
                        pattern_found = True
                        break

    lengths = [i[1] for i in periods]
    return periods[lengths.index(max(lengths))][0]


def twentyseven():

    """
    Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    Find the product of the coefficients, a and b, for the quadratic
    expression that produces the maximum number of primes for
    consecutive values of n, starting with n = 0.
    """

    f = lambda n: n**2 + a*n + b

    primes = [i for i in range(1,1000,2) if is_prime(i)]
    primes += [-i for i in primes]
    primes += [-2, -1, 1, 2]

    streaks = []

    for a in primes:
        for b in primes:
            streak = True
            streak_length = 0
            n = 0
            while streak:
                res = f(n)
                if is_prime(res):
                    streak_length += 1
                    n += 1
                else:
                    streaks += [(a, b, streak_length)]
                    break

    lengths = [i[2] for i in streaks]
    z = lengths.index(max(lengths))
    x = streaks[z][0]
    y = streaks[z][1]

    return x * y, streaks[z]


def twentyeight():

    """
    Starting with the number 1 and moving to the right in a clockwise
    direction a 5 by 5 spiral is formed as follows:

                            21 22 23 24 25
                            20  7  8  9 10
                            19  6  1  2 11
                            18  5  4  3 12
                            17 16 15 14 13

    It can be verified that the sum of the numbers on the
    diagonals is 101.
    What is the sum of the numbers on the diagonals in
    a 1001 by 1001 spiral formed in the same way?
    """

    topleftsum = 1
    cur = 1
    a = 2
    for i in range(1000):
        cur += a
        a += 2
        topleftsum += cur

    bottomleftsum = 0
    b = 3; c = 2
    for i in range(500):
        bottomleftsum += b**2
        b += 2
    for i in range(500):
        bottomleftsum += 1 + c**2
        c += 2

    return topleftsum + bottomleftsum

    ##challenge mode: generate the entire array and add afterwords
    ##l = [[0 for i in range(1001)] for j in range(1001)]
    ##n = 1
    ##o = [500, 500]
    ##distance = 1


def twentynine():

    """
    How many distinct terms are in the sequence generated by a^b
    for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
    """

    terms = []

    for a in range(2,101):
        for b in range(2,101):
            terms += [a ** b]

    return len(set(terms))


def thirty():

    """
    Surprisingly there are only three numbers that can be written as
    the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

    Find the sum of all the numbers that can be written as the sum of
    fifth powers of their digits.
    """

    def sum_of_digit_powers(n):

        return sum([int(i)**5 for i in str(n)])

    return sum([i for i in range(2, int(1E6)) if i==sum_of_digit_powers(i)])

#############################################
### LONG LONG HIATUS FROM PROGRAMMING T-T ###
#############################################

def thirtyone():

    """
    In England the currency is made up of pound, £, and pence, p,
    and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

    How many different ways can £2 be made using any number of
    coins?
    """

    #interwebs helped me with this one...

    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    x = coins[-1]
    ways = [1] + [0]*x

    for coin in coins:
        for i in range(coin, x + 1):
            ways[i] += ways[i - coin]

    return ways[-1]


def thirtytwo():


    """
    Find the sum of all products whose multiplicand/multiplier/produc
    identity can be written as a 1 through 9 pandigital, with each digit
    appearing only once.

    For example, 39 × 186 = 7254.
    """

    def list_divisors(n):
        "only returns the kind of divisors we're looking for here"

        divpairs = []
        for i in range(2, floor(sqrt(n)) + 1):
            if norepeats(i) and n % i == 0:
                j = n // i
                if i != j and norepeats(j):
                    divpairs += [(i, j)]
        return divpairs

    def norepeats(n):
        "helper function, not sure if it's cost efficient"

        n = str(n)
        if '0' in n:
            return False
        for i in n:
            if n.count(i) > 1:
                return False
        return True

    def ispan(n):
        "a la primitive"

        n = str(n)
        if len(n) != 9:
            return False
        else:
            for i in n:
                if n.count(i) > 1:
                    return False
        return True


    pan_products = []

    mmp_peak_len = 0
    n = 1234 #let's start here because I can't deduce a better starting point

    while mmp_peak_len <= 10:
        n += 1
        if norepeats(n):
            divs = list_divisors(n)
            for div in divs:
                a, b = div[0], div[1]
                mmp = str(div[0]) + str(div[1]) + str(n)
                if len(mmp) > mmp_peak_len:
                    mmp_peak_len = len(mmp)
                if ispan(mmp):
                    pan_products += [n]
    return sum(set(pan_products))


def thirtythree():

    """
    The fraction 49/98 is a curious fraction, as an inexperienced
    mathematician in attempting to simplify it may incorrectly believe that
    49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction,
    less than one in value, and containing two digits in the numerator and
    denominator.

    If the product of these four fractions is given in its lowest common
    terms, find the value of the denominator.
    """

    def isreducible(num, denom):
        "is num/denom reducible, assuming num < denom, inefficient af"

        for i in range(2, denom):
            if num % i == 0 and denom % i == 0:
                return True

    def lcd(num, denom):
        "returns lcd of num/denom, assuming num < denom"

        x = max([i for i in range(2, denom+1) if [denom % i, num % i] == [0, 0]])
        return denom/x


    box = []

    for denom in range(99, 11, -1):
        for num in range(11, denom):
            if isreducible(num, denom):
                n, d = str(num), str(denom)
                if (n + d).count('0') == 0:
                    for i in n:
                        if i in d:
                            n_faux = n[n.index(i) - 1]
                            d_faux = d[d.index(i) - 1]
                            erreur = int(n_faux) / int(d_faux)
                            if erreur == num/denom:
                                box += [(num, denom)]

    numnum, denomnom = 1, 1
    for i in box:
        numnum *= i[0]
        denomnom *= i[1]
    answer = lcd(numnum, denomnom)

    print(answer)
    return answer


def thirtyfour():

    """
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial
    of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    """

    S = 0
    for n in range(145, int(1E5)):
        ns = [int(i) for i in str(n)]
        sn = sum([factorial(i) for i in ns])
        if sn == n:
            S += n
    return S


def permute(n, indent=0):

    """
    n -> string (intended to represent an integer)

    Returns all distinct permutations of n
    """

    perms = []

    if len(n) <= 1:
        return n
    else:
        for i in range(len(n)):
            i_perms = permute(n[:i] + n[i + 1:], indent + 2)
            perms += [n[i] + perm for perm in i_perms]
        return list(set(perms))


def thirtyfive():

    """
    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.

    How many circular primes are there below one million?
    """

    primes = ['2'] + [str(n) for n in range(3, int(1E6), 2) if is_prime(n)]
    circles = []

    for prime in primes:
        if len(prime) == 1:
            circles += [prime]
        else:
            rotations = []
            rotation = ''.join(i for i in prime)
            for i in range(len(prime) - 1):
                rotation = rotation[1:] + rotation[0]
                rotations += [rotation]
            if sum([int(i in primes) for i in rotations]) == len(rotations):
                circles += [prime]
    return circles


def is_palindrome(n):

    "n -> str(n)"

    if len(n) == 1:
        return True
    elif len(n) == 2:
        return n[0] == n[1]
    else:
        for i in range((len(n)//2)):
            if n[i] != n[len(n) - 1 - i]:
                return False
    return True


def thirtysix():

    """
    The decimal number, 585 = 1001001001 (binary), is palindromic in both
    bases.

    Find the sum of all numbers, less than one million, which are palindromic
    in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include
    leading zeros.)
    """

    ten_pals = [n for n in range(1, int(1E6)) if is_palindrome(str(n))]
    return sum([n for n in ten_pals if is_palindrome(bin(n)[2:])])


def thirtyseven():

    """
    The number 3797 has an interesting property. Being prime itself, it is
    possible to continuously remove digits from left to right, and remain
    prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
    right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left
    to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    """

    i, N = 0, 13
    speshuls = []

    while i < 11:
        N += 2

        if is_prime(N):

            n = str(N)
            left_truncs = [n[i:] for i in range(1, len(n))][::-1]
            right_truncs = [n[:i] for i in range(1, len(n))]
            truncs = [[left_truncs[i], right_truncs[i]] for i in range(len(n)-1)]

            spesh = True
            ii = 0
            while ii < len(truncs):
                if not is_prime(int(truncs[ii][0])):
                    spesh = False
                    break
                elif not is_prime(int(truncs[ii][1])):
                    spesh = False
                    break
                ii += 1
            if spesh:
                speshuls += [N]
                i += 1

    return sum(speshuls)


def thirtyeight():

    """
    Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192, 192 × 2 = 384, 192 × 3 = 576
    By concatenating each product we get the 1 to 9 pandigital, 192384576. We
    will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
    and 5, giving the pandigital, 918273645, which is the concatenated product
    of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated product of an integer with (1,2, ... , n) where n > 1?
    """

    def ispan(n):
        "a la primitive"

        return set(n) == set('123456789') and len(n) == 9

    cat_pans = []
    n = 2

    while len(str(n)) <= 4:

        cat_max = range(1, ceil(9 / len(str(n))))
        cat_arr = [list(cat_max[:i]) for i in range(1, len(cat_max) + 1)]

        for cat in cat_arr:
            ncat = ''.join(str(n * i) for i in cat)
            if len(ncat) == 9:
                if ispan(ncat):
                    cat_pans += [ncat]
        n += 1

    return max(cat_pans)


def thirtynine():

    """
    If p is the perimeter of a right angle triangle with integral length
    sides, {a,b,c}, there are exactly three solutions for p = 120:

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?

    Solved in a very janky, brutish and inefficient manner
    """

    max_sols = [0, 0]
    for p in range(4, 1000):
        p_sols = 0
        for a in range(1, p // 2):
            for b in range(1, p // 2)[::-1]:
                c = p - a - b
                if c ** 2 == a ** 2 + b ** 2:
                    p_sols += 1
        if p_sols > max_sols[1]:
            max_sols = [p, p_sols]
    return max_sols


def forty():

    """
    An irrational decimal fraction is created by concatenating the positive
    integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of
    the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
    """

    d_arr = [1 * (10 ** i) for i in range(7)]
    c = ''.join(str(i) for i in range(1, d_arr[-1] + 1))
    d_factors = [c[i-1] for i in d_arr]

    p = 1
    for i in d_factors:
        p *= int(i)
    return p

def fortyone():

    """
    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once. For example, 2143 is a 4-digit
    pandigitaland is also prime.

    What is the largest n-digit pandigital prime that exists?
    """

    n = 9
    while n > 1:
        perms = permute(''.join(str(i) for i in range(1, n + 1)))
        primperms = [i for i in perms if is_prime(int(i))]
        if primperms:
            return max(primperms)
        else:
            n -= 1


def fortytwo():

    """
    The nth term of the sequence of triangle numbers is given by,
    tn = ½n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value. For
    example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
    value is a triangle number then we shall call the word a triangle word.

    Uses "words.txt", provided by project euler, how many words are
    triangle words?
    """

    try:
        with open('words.txt') as f:
            f = f.read().split(',')
            words = [i.strip('\"') for i in f]
    except:
        print('Missing words.txt from projecteuler.net/problem=42')

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',\
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',\
                'W', 'X', 'Y', 'Z']

    t_cap = 26 * len(max(words, key=len))
    triangles = [.5 * i * (i + 1) for i in range(1, t_cap)]

    t_word_count = 0
    for word in words:
        wordsworth = sum(alphabet.index(c) + 1 for c in word)
        t_word_count += int(wordsworth in triangles)
    return t_word_count


def fortythree():

    """
    The number, 1406357289, is a 0 to 9 pandigital number because it is made
    up of each of the digits 0 to 9 in some order, but it also has a rather
    interesting sub-string divisibility property.

    Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way,
    we note the following:

    d_2d_3d_4=406 is divisible by 2
    d_3d_4d_5=063 is divisible by 3
    d_4d_5d_6=635 is divisible by 5
    d_5d_6d_7=357 is divisible by 7
    d_6d_7d_8=572 is divisible by 11
    d_7d_8d_9=728 is divisible by 13
    d_8d_9d_10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.
    """

    d = [2, 3, 5, 7, 11, 13, 17]

    pans = permute('0123456789')
    pans = [i for i in pans if i[0] != '0']
    gewds = []

    for pan in pans:
        gewd = True
        i = 0
        while i < 7:
            if int(pan[i + 1: i + 4]) % d[i] != 0:
                gewd = False
                break
            else:
                i += 1
        if gewd:
            gewds += [int(pan)]
    return sum(gewds)


def fortyfour():

    """
    Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first
    ten pentagonal numbers are:

    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

    It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their
    difference, 70 − 22 = 48, is not pentagonal.

    Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
    difference are pentagonal and D = |Pk − Pj| is minimised; what is the
    value of D?

    Personal note:

    P(n) - P(n-1) grows as n grows, so the first pair will be the pair with the
    smallest difference. This simplifies the problem to finding the first pair.

    Also, to check if a given number n is pentagonal, it suffices to check if
    the inverse pentagonal formula n = ((24x + 1)^1/2 + 1) / 6
    is an integer for x = n.
    """

    def p(n):
        "I should be a lambda"
        return int((n * ((3 * n) - 1)) / 2)

    def inv_p(n):
        "I should also be a lambda"
        return (sqrt((24 * n) + 1) + 1) / 6

    pents = [1]
    n = 1

    while True:
        n += 1
        pn = p(n)
        pents += [pn]
        for i in pents[:-1][::-1]:
            if inv_p(pn + i) % 1 == 0 and inv_p(pn - i) % 1 == 0:
                d = pn - i
                return d


def fortyfive():

    """
    Triangle, pentagonal, and hexagonal numbers are generated by the following
    formulae:

    Triangle        Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
    Pentagonal      Pn=n(3n−1)/2    1, 5, 12, 22, 35, ...
    Hexagonal       Hn=n(2n−1)      1, 6, 15, 28, 45, ...

    It can be verified that T285 = P165 = H143 = 40755.

    Find the next triangle number that is also pentagonal and hexagonal.

    Personal note: The inverse hexagonal function is n = (sqrt(8x + 1) + 1)/ 4
    """

    def t(n):
        "I should be a lambda"
        return (n * (n + 1)) / 2

    def inv_p(n):
        "I should also be a lambda"
        return (sqrt((24 * n) + 1) + 1) / 6

    def inv_h(n):
        "I should also be a lambda"
        return (sqrt((8 * n) + 1) + 1) / 4

    trouves = 0
    n = 1
    tn = t(n)

    while trouves < 2:
        n += 1
        tn = t(n)
        if inv_p(tn) % 1 == 0 and inv_h(tn) % 1 == 0:
            trouves += 1
            if trouves == 2:
                return tn


def fortysix():

    """
    It was proposed by Christian Goldbach that every odd composite number can
    be written as the sum of a prime and twice a square.

    9 = 7 + 2×1^2
    15 = 7 + 2×2^2
    21 = 3 + 2×3^2
    25 = 7 + 2×3^2
    27 = 19 + 2×2^2
    33 = 31 + 2×1^2

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of
    a prime and twice a square?
    """

    n = 3
    primes = [2]
    yoku = True

    while yoku:
        if is_prime(n):
            primes += [n]
        else:
            satis = False
            for i in primes[::-1]:
                d = n - i
                if d % 2 == 0:
                    for s in range(1, (.5 * d) + 1):
                        if 2 * (s ** 2) == d:
                            satis = True
                            break
                if satis:
                    break
            if not satis:
                return n
        n += 2


def fortyseven():

    """
    The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors
    are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime
    factors each. What is the first of these numbers?
    """

    n = 1000
    conseq = 0
    primes = []

    while n < 10000:

        factors = []
        prime = True

        for i in range(1, ceil(sqrt(n)) + 1):
            if n % i == 0 and is_odd(i):
                prime = False
        if prime:
            primes += [n]

        n += 1



