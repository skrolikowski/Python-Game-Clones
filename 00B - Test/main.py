import pybox
import pyglet

from pybox.containers import stack
from pyglet.window import key

class Registry:
    def __init__(self):
        self._window = None
        self._states = stack.Stack()
        self._init_states = []
        self._commands = {}

    def add_command(self, name, command):
        command_name = command.__qualname__
        state, func  = command_name.split(".")

        if name not in self._commands:
            self._commands[name] = {}

        if state not in self._commands[name]:
            self._commands[name][state] = []

        self._commands[name][state].append(command)

    def get_command(self, name):
        state = self.current.__class__.__name__

        if name in self._commands:
            if state in self._commands[name]:
                return self._commands[name][state]

        return []

    def change_state(self, from_state, to_state, *args, **kwargs):
        if from_state is not None:
            self._window.on_leave(*args, **kwargs)

        self._states.push(to_state)

        if to_state.__class__.__name__ not in self._init_states:
            self._window.on_load()
            self._init_states.append(to_state.__class__.__name__)

        self._window.on_enter(from_state, *args, **kwargs)

    def switch(self, to_state, *args, **kwargs):
        self.change_state(self._states.pop(), to_state, *args, **kwargs)

    def push(self, state, *args, **kwargs):
        self.change_state(self.current, state, *args, **kwargs)

    def pop(self, *args, **kwargs):
        if len(self._states) <= 1:
            raise Exception("Nothing to pop!")

        self._window.on_leave(*args, **kwargs)
        self._states.pop()
        self._window.on_resume(*args, **kwargs)

    @property
    def current(self):
        return self._states.peek()

    @property
    def states(self):
        return self._states

    @property
    def commands(self):
        return self._commands

    @property
    def window(self):
        return self._window

    @window.setter
    def window(self, value):
        self._window = value

# ------------------------------------------

class GameWindow(pybox.graphics.window.Window):
    def __init__(self, registry, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.registry = registry

    def on_load(self):
        for func in self.registry.get_command("load"):
            func(self.registry, self)

    def on_enter(self, prev, *args, **kwargs):
        for func in self.registry.get_command("state_enter"):
            func(self.registry, prev, *args, **kwargs)

    def on_leave(self, *args, **kwargs):
        for func in self.registry.get_command("state_leave"):
            func(self.registry, *args, **kwargs)

    def on_resume(self):
        for func in self.registry.get_command("state_resume"):
            func(self.registry)

    def on_update(self, dt):
        for func in self.registry.get_command("update"):
            func(self.registry, dt)

    def on_draw(self):
        super().on_draw()

        for func in self.registry.get_command("draw"):
            func(self.registry)

        super().debug()

    def on_key_press(self, symbol, modifiers):
        for func in self.registry.get_command("key_press"):
            func(self.registry, symbol, modifiers)

# ------------------------------------------

class Game:
    registry = Registry()

    @classmethod
    def load(cls, func):
        cls.registry.add_command("load", func)
        return func

    @classmethod
    def update(cls, func):
        cls.registry.add_command("update", func)
        return func

    @classmethod
    def draw(cls, func):
        cls.registry.add_command("draw", func)
        return func

    @classmethod
    def key_press(cls, func):
        cls.registry.add_command("key_press", func)
        return func

    @classmethod
    def enter(cls, func):
        cls.registry.add_command("state_enter", func)
        return func

    @classmethod
    def leave(cls, func):
        cls.registry.add_command("state_leave", func)
        return func

    @classmethod
    def resume(cls, func):
        cls.registry.add_command("state_resume", func)
        return func

    @classmethod
    def switch(cls, state, *args, **kwargs):
        cls.registry.switch(state, *args, **kwargs)

    @classmethod
    def push(cls, state, *args, **kwargs):
        cls.registry.push(state, *args, **kwargs)

    @classmethod
    def pop(cls, *args, **kwargs):
        cls.registry.pop(*args, **kwargs)

    @classmethod
    def run(cls, width=640, height=480, caption="Game"):
        cls.registry.window = GameWindow(
            cls.registry,
            width=width,
            height=height,
            caption=caption
        )

# ------------------------------------------

class PauseScreen:
    def __init__(self):
        self.window = None
        self.prev = None

    @Game.load
    def on_load(self, win):
        self.window = win
        print("Pause - load")

    @Game.enter
    def on_enter(self, prev, *args, **kwargs):
        print("Pause - enter")
        self.prev = prev

    @Game.draw
    def on_draw(self):
        self.prev.on_draw()

    @Game.key_press
    def on_key_press(self, symbol, modifiers):
        if symbol == key.P:
            Game.pop()

class GameScreen:
    def __init__(self):
        self.window = None
        self.foo = "bar"

    @Game.load
    def on_load(self, win):
        self.window = win
        print("Game - load")

    @Game.enter
    def on_enter(self, prev, *args, **kwargs):
        print("Game - enter")
        pass

    @Game.leave
    def on_leave(self, *args, **kwargs):
        print("Game - leave")
        pass

    @Game.resume
    def on_resume(self, *args, **kwargs):
        print("Game - resume")
        pass

    @Game.draw
    def on_draw(self):
        pass

    @Game.key_press
    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.window.close()
        elif symbol == key.P:
            Game.push(PauseScreen())

# ------------------------------------------

if __name__ == "__main__":
    Game.run(width=640, height=480, caption="Test")
    Game.switch(GameScreen())

    pyglet.app.run()
