from project import print_options, validate_search_input, process_cli_args, process_choice

def test_print_options_without_start(capsys):
    options = [
        {"txt": "test", "func": None},
        {"txt": "option", "func": None},
    ]
    
    output = "Pick an option (number):\n1. test\n2. option\nType 0 to exit. Type nothing to go to previous menu."
    
    print_options(options)
    captured = capsys.readouterr()
    assert captured.out.strip() == output
    
    
def test_print_options_with_start(capsys):    
    options = [
        {"txt": "test", "func": None}
    ]
    
    output = "Pick an option (number):\n1. test\nType 0 to exit."
    
    print_options(options, start=True)
    captured = capsys.readouterr()
    assert captured.out.strip() == output


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