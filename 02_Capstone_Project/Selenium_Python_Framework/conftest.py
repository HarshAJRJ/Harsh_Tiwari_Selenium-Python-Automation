import os
from datetime import datetime

import pytest

from utilities.driver_factory import DriverFactory


@pytest.fixture
def driver(request):

    driver = DriverFactory.get_driver()

    yield driver

    # Take screenshot if the test failed
    if request.node.rep_call.failed:

        screenshots_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "screenshots"
        )

        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_path = os.path.join(
            screenshots_dir,
            f"{request.node.name}_{timestamp}.png"
        )

        driver.save_screenshot(screenshot_path)

        print(f"\nScreenshot saved: {screenshot_path}")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)