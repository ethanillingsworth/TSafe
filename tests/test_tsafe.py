from tsafe import safe, StringList

def test_empty():
    
    @safe
    def random(s: str, n: int, n2: float, l: list, d: dict, a: object, sl: StringList):
        assert True

    random("String", 10, 1.123, ["types", 10, "multiple"], {"Hello": 10}, "Anything", ["Strings", "Only!!"])