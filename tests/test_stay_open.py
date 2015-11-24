# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import time

import pytest

pytestmark = pytest.mark.nondestructive


def test_stay_open(base_url, selenium):
    """Open a page and stay there"""
    selenium.get(base_url)
    for x in range(100):
        selenium.title
        time.sleep(30)
