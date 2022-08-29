import tkinter as tk
import traceback
from app.resize_tracker import ResizeTracker
from app.scenes import Scene

from app.object_selector_treeview import SceneSelectorTreeview

class SceneControllerApp():
    def __init__(self):
        self.window_title = "RPG Scene Controller"
        self.scenes : list[Scene] = []
        self.soundtracks = [] # TODO: Implement soundtracks

    def __enter__(self):
        self.root = tk.Tk()

        self.root.title(self.window_title)

        # Resize tracker
        self.resize_tracker = ResizeTracker(self.root)
        self.resize_tracker.enforce_aspect_ratio(self.screen_aspect_ratio)

        # Scene treeview
        self.scene_treeview = SceneSelectorTreeview(self, columns=["scene", "type", "details"], headings=["Scene", "Type", "Details"])
        self.scene_treeview(self.root)

        return self.root

    def __exit__(self, type : object, value : str, traceback : traceback):
        if not type and not value and not traceback:
            # Exited program without errors
            print("Exited Program")

    @property
    def screen_aspect_ratio(self):
        return self.root.winfo_screenwidth() / self.root.winfo_screenheight()