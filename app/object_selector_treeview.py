import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
from typing import Optional
from app.scenes import Scene, ImageScene, SlideshowScene

class ObjectSelectorTreeview(ABC):
    def __init__(self, controller, columns : list[str], headings : list[str]):
        if headings and len(columns) != len(headings):
            raise ValueError("There must either be no headings, or the same number of headings and columns")

        self.controller = controller
        self.columns = columns
        self.headings = headings if headings else columns

    @abstractmethod
    def onSelect(self, event):
        pass

    def __call__(self, root : tk.Tk):
        self.treeview = ttk.Treeview(root, columns=self.columns, show='headings', selectmode="browse")

        for column, heading in zip(self.columns, self.headings):
            self.treeview.heading(column, text=heading)

        self.treeview.bind('<<TreeviewSelect>>', self.onSelect)
        self.treeview.bind("<Double-1>", self.onDoubleClick)
        self.treeview.grid(row=0, column=0, sticky=tk.NSEW)

        for i in range(3):
            scene = SlideshowScene(f"Slideshow Scene - {i}")
            self.add_scene(scene)
            self.treeview.insert('', tk.END, values=self.item(scene))

class SceneSelectorTreeview(ObjectSelectorTreeview):
    
    @property
    def scenes(self):
        return self.controller.scenes

    def onSelect(self, event):
        # This should never be more than once as longe as 'selectmode' is browse
        for selected_item in self.treeview.selection():
            index = self.treeview.index(selected_item)

            scene = self.controller.scenes[index]

            print(scene)


    def onDoubleClick(self, event):
        item = self.treeview.identify('item', event.x, event.y)
        index = self.treeview.index(item)

        if index is None:
            return
    
        scene = self.controller.scenes[index]

        print(scene)

    def bool_symbol(self, val : bool) -> str:
        if val:
            return "???"
        
        return "???"

    def item(self, scene : Scene) -> tuple[str, str, str]:
        return scene.name, scene.type.value, "\n".join(scene.details)
        

    def add_scene(self, scene : Scene) -> None:
        if not issubclass(type(scene), Scene):
            raise TypeError("Can only add scenes to scene list!")
        
        self.controller.scenes.append(scene)