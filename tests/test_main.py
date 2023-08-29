from typing import List, Pattern

import mockish
import pytest
from _pytest.capture import CaptureFixture, CaptureResult

from tuiview.__main__ import main
from tuiview.__main__ import sys as target_sys


def test_main_version(capsys: CaptureFixture, version_pattern: Pattern):
    # 1. ARRANGE
    args: List[str] = ["--version"]

    # 2. ACT
    with mockish.patch.object(target_sys, "argv", ["", *args]), pytest.raises(
        SystemExit,
    ) as e:
        main()

    # 3. ASSERT
    assert e.value.code == 0

    captured: CaptureResult = capsys.readouterr()
    assert not captured.err
    assert captured.out
    assert version_pattern.search(captured.out.split()[-1]), "invalid version"
