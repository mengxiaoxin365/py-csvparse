from csvline import parse_line


def test_quotes():
    assert parse_line('a,"b,c",d') == ["a", "b,c", "d"]
    assert parse_line('"he said ""hi"""') == ['he said "hi"']
