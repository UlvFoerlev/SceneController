

class ResizeTracker:
    """ Toplevel windows resize event tracker. """

    def __init__(self, toplevel):
        self.toplevel = toplevel
        self.width, self.height = toplevel.winfo_width(), toplevel.winfo_height()
        self._func_id = None

        self.skip = False

        self.enforced_aspect_ratio = None
        self.min_size = (self.width, self.height)

        self.bind_config()

    def bind_config(self) -> None:
        self._func_id = self.toplevel.bind("<Configure>", self.resize)

    def unbind_config(self) -> None:  # Untested.
        if self._func_id:
            self.toplevel.unbind("<Configure>", self._func_id)
            self._func_id = None

    def resize(self, event) -> None:
        if self.skip:
            return

        if(event.widget == self.toplevel and
           (self.width != event.width or self.height != event.height)):

            # if self.enforced_aspect_ratio:            
            #     x_change = (event.width != self.width)
            #     y_change = (event.height !=self.height)

            #     self.skip = True

            #     if x_change and not y_change:
            #         print("x change")
            #         self.toplevel.winfo_toplevel().minsize(event.width, int(event.width * self.enforced_aspect_ratio))
            #         # self.toplevel.winfo_toplevel().minsize(*self.min_size)
            #         # self.toplevel.config(height=int(event.width * self.enforced_aspect_ratio))
            #     elif y_change and not x_change:
            #         self.toplevel.winfo_toplevel().minsize(event.height, int(event.height * self.enforced_aspect_ratio))
            #         # self.toplevel.winfo_toplevel().minsize(*self.min_size)
                    
            #     else:
            #         print("x/y change")

            #     self.skip = False

            #     self.width, self.height = self.toplevel.winfo_width(), self.toplevel.winfo_height()

            # else:
            self.width, self.height = event.width, event.height

    def enforce_min_size(self, width : int, height : int):
        self.min_size = (width, height)
        self.toplevel.minsize(width, height)

    def enforce_aspect_ratio(self, aspect_ratio : float) -> None:
        self.enforced_aspect_ratio = aspect_ratio