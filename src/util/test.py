from colorama import Fore, Back, Style

"""
A beautiful way to print the test Result.
"""
def rep_test_result(msg: str, condi: bool) -> str:
    PASS = f'Test: {msg:30s} [ {Fore.GREEN}Pass{Fore.RESET} ]'
    FAIL = f'Test: {msg:30s} [ {Fore.RED}Fail{Fore.RESET} ]'
    return PASS if condi else FAIL