import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from app import app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "Soul Foods: Pink Morsel Sales Visualiser"

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None               #test function uses assert to confirm that output is as expected

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    picker = dash_duo.find_element("#region-filter")
    assert picker is not None