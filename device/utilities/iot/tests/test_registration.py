# Import standard python libraries
import os, sys, pytest, time

# Set system path
sys.path.append(os.environ["OPENAG_BRAIN_ROOT"])

# Import manager elements
from device.utilities.iot import registration


def test_init() -> None:
    assert True
