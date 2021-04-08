from string_search import BoyerMoore

if __name__ == "__main__":
    text = "CAUAAAAUUAUAAUGCAUCGUUAUCAGCUGGGUCAUAUGUUAUGACAACGACUUGGCGGA AUACUAGUAAGUUGUCCUUUCCACUUAAUUGAAACGAUUUGCGCAGGAAUUUUGUGAUAA UUAUCAAAAAAA"
    pattern = "AAAAAAA"
    print(len(text))
    algo = BoyerMoore(text, pattern)
    if algo.search() >= 0:
        print('Found')
    else:
        print('Not found')
