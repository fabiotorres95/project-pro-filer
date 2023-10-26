import os
import pytest
from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date


@pytest.fixture
def create_file(tmp_path):
    file = tmp_path / "good-file.txt"
    file.write_text("good content")
    return file


@pytest.fixture
def no_extension_file(tmp_path):
    file = tmp_path / "no-extension"
    file.write_text("good content but no extension")
    return file


def test_if_good_file_is_good(create_file, capsys):
    path = str(create_file)

    file_date = date.fromtimestamp(os.path.getmtime(path))
    context = {
        "base_path": path,
    }
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == f"""File name: good-file.txt
File size in bytes: 12
File type: file
File extension: .txt
Last modified date: {file_date}
"""


def test_when_no_file_exists(capsys):
    context = {
        "base_path": "no-file.txt",
    }
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == "File 'no-file.txt' does not exist\n"


def test_when_no_file_extension(no_extension_file, capsys):
    path = str(no_extension_file)
    file_date = date.fromtimestamp(os.path.getmtime(path))
    context = {
        "base_path": path,
    }
    show_details(context)
    capture = capsys.readouterr()
    assert capture.out == f"""File name: no-extension
File size in bytes: 29
File type: file
File extension: [no extension]
Last modified date: {file_date}
"""
