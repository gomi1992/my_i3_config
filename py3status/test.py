from time import time

class Py3status:

    def __init__(self):
        self.count = 0

    """
    Empty and basic py3status class.

    NOTE: py3status will NOT execute:
        - methods starting with '_'
        - methods decorated by @property and @staticmethod

    NOTE: reserved method names:
        - 'kill' method for py3status exit notification
        - 'on_click' method for click events from i3bar
    """
    def kill(self, i3status_output_json, i3status_config):
        """
        This method will be called upon py3status exit.
        """
        pass

    def on_click(self, i3status_output_json, i3status_config, event):
        """
        This method will be called when a click event occurs on this module's
        output on the i3bar.

        Example 'event' json object:
        {'y': 13, 'x': 1737, 'button': 1, 'name': 'empty', 'instance': 'first'}
        """
        self.count += 1
        self.response_str = "click:"+str(self.count)
        # pass

    def _empty(self, i3status_output_json, i3status_config):
        """
        This method will return an empty text message
        so it will NOT be displayed on your i3bar.

        If you want something displayed you should write something
        in the 'full_text' key of your response.

        See the i3bar protocol spec for more information:
        http://i3wm.org/docs/i3bar-protocol.html
        """
        if self.count ==  0:
            self.response_str = "click:"+str(self.count)
        response = {'full_text': self.response_str, 'name': 'empty', 'instance': 'first'}
        response['cached_until'] = time()
        return (5, response)
