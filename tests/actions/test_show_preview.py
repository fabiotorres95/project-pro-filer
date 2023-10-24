from pro_filer.actions.main_actions import show_preview  # NOQA

good_context = {
    'all_files': ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
    'all_dirs': ["src", "src/utils"],
    }

empty_keys_context = {
    'all_files': [],
    'all_dirs': [],
}

big_context = {
    'all_files': [
        "src/__init__.py",
        "src/app.py",
        "src/utils/__init__.py",
        "src/utils/other.py",
        "src/xablau.py",
        "src/bla.py",
        ],
    'all_dirs': ["src", "src/utils"],
    }


def test_if_good_input_is_good(capsys):
    show_preview(good_context)
    captured = capsys.readouterr()
    assert captured.out == """Found 3 files and 2 directories
First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']
First 5 directories: ['src', 'src/utils']
"""


def test_when_keys_are_empty(capsys):
    show_preview(empty_keys_context)
    captured = capsys.readouterr()
    assert captured.out == """Found 0 files and 0 directories
"""


def test_if_first_five_are_shown(capsys):
    show_preview(big_context)
    captured = capsys.readouterr()
    temp1 = "['src/__init__.py', 'src/app.py', 'src/utils/__init__.py',"
    temp2 = "'src/utils/other.py', 'src/xablau.py']"
    assert captured.out == f"""Found 6 files and 2 directories
First 5 files: {temp1} {temp2}
First 5 directories: ['src', 'src/utils']
"""
