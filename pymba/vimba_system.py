from .vimba_object import VimbaObject


class VimbaSystem(VimbaObject):
    """
    A Vimba system object. This class provides the minimal access to Vimba functions required to control the system.
    """
    def __init__(self):
        super().__init__(handle=1)
