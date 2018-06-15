# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self, app):
        BaseTest.__init__(self, app)
        self.meta = 'This is a test that opens a page from the History sidebar.'

    def setup(self):
        """ Test case setup
        This overrides the setup method in the BaseTest class,
        so that it can use a brand new profile.
        """
        self.profile = Profile.BRAND_NEW
        launch_firefox(path=self.app.fx_path, profile=self.profile, url='about:blank')
        return

    def run(self):
        wikipedia_logo = 'wikipedia.png'
        google_search = 'google_search.png'
        history_sidebar_wikipedia = 'history_sidebar_wikipedia.png'
        search_history_box = 'search_history_box.png'
        expand_button_history_sidebar = 'expand_button_history_sidebar.png'

        # Open some pages to create some history.
        navigate('https://www.wikipedia.org/')
        expected_1 = exists(wikipedia_logo, 10)
        assert_true(self, expected_1, 'Page loaded successfully.')

        new_tab()
        navigate('https://www.google.com/?hl=EN')
        expected_2 = exists(google_search, 10)
        assert_true(self, expected_2, 'Page loaded successfully.')

        # Open the History sidebar.
        history_sidebar()
        expected_3 = exists(search_history_box, 10)
        assert_true(self, expected_3, 'Sidebar was opened successfully.')
        expected_4 = exists(expand_button_history_sidebar, 10)
        assert_true(self, expected_4, 'Expand history button displayed properly')
        click(expand_button_history_sidebar)

        # Open a page from the history sidebar
        expected_5 = exists(history_sidebar_wikipedia, 10)
        assert_true(self, expected_5, 'Page displayed in the History list successfully.')
        click(history_sidebar_wikipedia)
        expected_6 = exists(wikipedia_logo, 10)
        assert_true(self, expected_6, 'Page loaded successfully.')
