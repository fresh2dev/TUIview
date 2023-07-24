from typing import List, Pattern

import mockish
from _pytest.capture import CaptureFixture, CaptureResult

from tuiview.__main__ import main
from tuiview.__main__ import sys as target_sys


def test_main_version(capsys: CaptureFixture, version_pattern: Pattern):
    # 1. ARRANGE
    args: List[str] = ["--version"]

    # 2. ACT
    with mockish.patch.object(target_sys, "argv", ["", *args]):
        main()

    # 3. ASSERT
    captured: CaptureResult = capsys.readouterr()
    assert not captured.err
    assert captured.out
    assert version_pattern.search(captured.out.split()[-1]), "invalid version"
