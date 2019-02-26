from random import randint

test.describe("Basic Tests")
test.it("Basic Tests")
test.assert_equals(expanded_form(2), '2')
test.assert_equals(expanded_form(12), '10 + 2')
test.assert_equals(expanded_form(42), '40 + 2')
test.assert_equals(expanded_form(70304), '70000 + 300 + 4')
test.assert_equals(expanded_form(4982342), '4000000 + 900000 + 80000 + 2000 + 300 + 40 + 2')

test.describe("Edge Cases")
test.it("Zeros")
test.assert_equals(expanded_form(420370022), '400000000 + 20000000 + 300000 + 70000 + 20 + 2');
test.assert_equals(expanded_form(70304), '70000 + 300 + 4');
test.assert_equals(expanded_form(9000000), '9000000');
test.it("Big Numbers")
test.assert_equals(expanded_form(92093403034573), '90000000000000 + 2000000000000 + 90000000000 + 3000000000 + 400000000 + 3000000 + 30000 + 4000 + 500 + 70 + 3');
test.assert_equals(expanded_form(2096039485293), '2000000000000 + 90000000000 + 6000000000 + 30000000 + 9000000 + 400000 + 80000 + 5000 + 200 + 90 + 3');


def solution(num):

    string = str(num)
    answer = ''
    for i in range(1, len(string)+1):
        num = string[len(string)-i]
        if num == '0':
            pass
        else:
            for j in range(0, i-1):
                num += '0'
            if answer == '':
                answer = num
            else:
                answer = num + ' + ' + answer
    return answer


test.describe("Random Tests")
for x in range(0, 100):
    num = randint(0,1000000)
    test.it("Random Tests")
    test.assert_equals(expanded_form(num), solution(num))
