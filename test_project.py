from project import validate_search_input, process_cli_args, process_choice

def test_validate_search_input():
    assert validate_search_input("test") == True
    assert validate_search_input("test query") == True
    assert validate_search_input("testtesttesttesttesttesttesttest") == False
    assert validate_search_input("") == False

def test_process_cli_args():
    assert process_cli_args([])["tts"] == False
    assert process_cli_args(["-s"])["tts"] == True

def test_process_choice():
    assert process_choice("1") == 1
    assert process_choice(" 5 ") == 5
    assert process_choice("asd") == float("inf")
    assert process_choice("7.") == float("inf")