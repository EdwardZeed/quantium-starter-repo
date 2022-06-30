import dash
from dash import html
from dash.testing.application_runners import import_app


# def pytest_setup_options():
#     options = Options()
#     options.add_argument('--disable-gpu')
#     return options

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# service = Service('/Users/edward/Downloads/chromedriver')
# service.start()
# driver = webdriver.Remote(service.service_url)
# driver.get('http://www.google.com/')
# time.sleep(5) # Let the user actually see something!
# driver.quit()

def test_bdv001_header_is_present(dash_duo):
    # app = dash.Dash(__name__)
    app = import_app("DataVisualiser.py")
    app.layout = html.Div(id="nully-wrapper", children=3)
    dash_duo.start_server(app)
#     test header is present
    dash_duo.wait_for_element('#nully-wrapper')
    check_header = dash_duo.find_element('#nully-wrapper')
    assert check_header is not None
    dash_duo.stop_server()

def test_bdv002_figure_is_present(dash_duo):
    # app = dash.Dash(__name__)
    app = import_app("DataVisualiser.py")
    app.layout = html.Div(id="nully-wrapper", children=3)
    dash_duo.start_server(app)

    dash_duo.wait_for_element('#nully-wrapper')
    check_figure = dash_duo.find_element('#example-graph')
    assert check_figure is not None
    dash_duo.stop_server()


def test_bdv003_picker_is_present(dash_duo):
    # app = dash.Dash(__name__)
    app = import_app("DataVisualiser.py")
    app.layout = html.Div(id="nully-wrapper", children=3)
    dash_duo.start_server(app)

    dash_duo.wait_for_element('#nully-wrapper')
    check_picker = dash_duo.find_element('#region-selector')
    assert check_picker is not None
    dash_duo.stop_server()


import dash
from dash import html
# 2. give each testcase a tcid, and pass the fixture
# as a function argument, less boilerplate
def test_bsly001_falsy_child(dash_duo):
    # 3. define your app inside the test function
    app = dash.Dash(__name__)
    app.layout = html.Div(id="nully-wrapper", children=0)
    # 4. host the app locally in a thread, all dash server configs could be
    # passed after the first app argument
    dash_duo.start_server(app)
    # 5. use wait_for_* if your target element is the result of a callback,
    # keep in mind even the initial rendering can trigger callbacks
    dash_duo.wait_for_text_to_equal("#nully-wrapper", "0", timeout=4)
    # 6. use this form if its present is expected at the action point
    assert dash_duo.find_element("#nully-wrapper").text == "0"
    # 7. to make the checkpoint more readable, you can describe the
    # acceptance criterion as an assert message after the comma.
    assert dash_duo.get_logs() == [], "browser console should contain no error"
    # 8. visual testing with percy snapshot
    dash_duo.percy_snapshot("bsly001-layout")
