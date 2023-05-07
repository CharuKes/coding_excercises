from twttr import shorten

def main():
    print(test_shorten())

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("what") == "wht"
    assert shorten("Twitter123") == "Twttr123"
    assert shorten("Able") == "bl"
    assert shorten("Twitter:") == "Twttr:"

if __name__ == "__main__":
    main()