from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


@pytest.fixture
def create_files(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file3 = tmp_path / "file3.txt"

    result = [file1, file2, file3]
    return result


def test_when_files_are_duplicate(create_files):
    for file in create_files:
        file.write_text("equal content")
    file1, file2, file3 = create_files
    context = {"all_files": [str(file1), str(file2), str(file3)]}

    assert find_duplicate_files(context) == [
        (str(file1), str(file2)),
        (str(file1), str(file3)),
        (str(file2), str(file3))
    ]


def test_when_files_are_different(create_files):
    for file in create_files:
        file.write_text(f"different content {file.name}")
    file1, file2, file3 = create_files
    context = {"all_files": [str(file1), str(file2), str(file3)]}

    assert find_duplicate_files(context) == []


def test_when_file_doesnt_exist(create_files):
    for file in create_files:
        file.write_text(f"different content {file.name}")
    file1, file2, file3 = create_files
    context = {"all_files": [str(file1), str(file2), str(file3), 'xablau.txt']}

    with pytest.raises(ValueError):
        find_duplicate_files(context)
