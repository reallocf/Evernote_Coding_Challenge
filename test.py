from word_counter import word_counter
from termcolor import cprint

def test(string, number, resList):
    res = word_counter(string, number)
    if res == resList:
        cprint("Pass " + str(res) + " == " + str(resList), "green")
    else:
        cprint("Fail " + str(res) + " =/= " + str(resList), "red")

if __name__ == '__main__':
    test("", 1, [""])
    test("    		", 2, ["", ""])
    test("a", 1, ["a"])
    test("a", 2, ["a", ""])
    test("a b", 2, ["a", "b"])
    test("a b b", 2, ["b", "a"])
    test("a b b c c c", 3, ["c", "b", "a"])
    test("a b b c c c", 2, ["c", "b"])
    test("a b b c c c", 1, ["c"])
    test("Test test the best.", 1, ["test"])
    test("big big big big words big words big words are really really nice big words are so cool are big words", 4, ["big", "words", "are", "really"])
    with open("all_star.txt") as f:
        test(f.read(), 13, ['the', 'get', 'and', 'to', 'on', 'all', 'i', 'now', "you're", 'your', 'hey', 'a', 'star'])
    with open("all_of_shakespeare.txt") as f:
        test(text, 3, ['the', 'and', 'i'])
