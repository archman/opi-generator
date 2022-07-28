from opimodel.widgets import ImageBoolButton
import os

# absolute path for current working directory
CWD_PATH = os.path.abspath(os.path.dirname(__file__))


class SlideButton(ImageBoolButton):
    def __init__(self, x, y, width, height, pv_name):
        super(self.__class__, self).__init__(x, y, width, height, pv_name)
        self.on_image = "images/toggle_on.svg"
        self.off_image = "images/toggle_off.svg"

    def get_resources(self):
        """Get required resource files and distribute with the final generate OPI.
        """
        return [(os.path.abspath(os.path.join(CWD_PATH, self.on_image)), self.on_image),
                (os.path.abspath(os.path.join(CWD_PATH, self.off_image)), self.off_image)]
