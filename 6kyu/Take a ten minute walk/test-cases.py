def tests():
    passwalk = [['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'], ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'],
                ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's'], ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']]
    failwalk = [['n'], ['n', 's'], ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'],
                ['n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's', 'e', 'w', 'n', 's', 'e', 'w'],
                ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 'n'], ['e', 'e', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w']]

    test.describe("Walk Validator - basic tests")
    test.it("should return false if walk is too short")
    test.expect(not isValidWalk(failwalk[0]))
    test.expect(not isValidWalk(failwalk[1]))
    test.it("should return false if walk is too long")
    test.expect(not isValidWalk(failwalk[2]))
    test.expect(not isValidWalk(failwalk[3]))
    test.it("should return false if walk does not bring you back to start")
    test.expect(not isValidWalk(failwalk[4]));
    test.expect(not isValidWalk(failwalk[5]))
    test.it("should return true for a valid walk")
    test.expect(isValidWalk(passwalk[0]))
    test.expect(isValidWalk(passwalk[1]))
    test.expect(isValidWalk(passwalk[2]))
    test.expect(isValidWalk(passwalk[3]))

    print("<COMPLETEDIN::>")
    print("<COMPLETEDIN::>")

    test.describe("Walk Validator - random tests")

    from random import randint, choice

    def valid_sol(walk):
        return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')

    for i in range(0, 100):
        number = randint(1, 7)
        testw = passwalk[number % 4]
        if number < 4:
            testw[randint(0, 9)] = ['n', 's', 'w', 'e'][randint(0, 3)]
        test.it("Testing a [" + ", ".join(testw) + "] walk")
        test.assert_equals(isValidWalk(list(testw)), valid_sol(testw),
                           "It should work also for a [" + ", ".join(testw) + "] walk")
    for i in range(100):
        testw = [choice('nswe') for _ in range(randint(4, 5))]
        testw += ['snew'['nswe'.index(c)] for c in testw]
        if randint(0, 1) == 0:
            testw[0] = 'swen'['nswe'.index(testw[0])]
        test.it("Testing a [" + ", ".join(testw) + "] walk")
        test.assert_equals(isValidWalk(list(testw)), valid_sol(testw),
                           "It should work also for a [" + ", ".join(testw) + "] walk")


tests()
