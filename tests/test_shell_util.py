
from shell_util import shell
from pathlib import Path


def test_shell_util_1(tmp_path: Path):

    one_file_path_object = tmp_path.joinpath('one.txt')
    one_file_path_object.touch()

    result = shell.run_command('echo -n test', stdout=one_file_path_object.open(mode='w'), in_dir=str(tmp_path))
    assert result is True
    text = one_file_path_object.read_text()

    assert text == 'test'
