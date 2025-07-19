from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Quad
from kivy.properties import Clock
from kivy.core.window import Window
import platform

class MainWidget(Widget):
    from transforms import transform, transform_2D, transform_perspective
    from user_actions import keyboard_closed, on_touch_down, on_touch_up, on_keyboard_down, on_keyboard_up
    
    perspective_point_x = NumericProperty(0.0)
    perspective_point_y = NumericProperty(0.0)

    V_NB_LINES = 4
    V_LINES_SPACING = .1 # percentage in screen 
    vertical_lines = []

    H_NB_LINES = 8
    H_LINES_SPACING = .15 # percentage in screen
    horizontal_lines = []

    SPEED = 2
    current_offset_y = 0

    SPEED_X = 12
    current_speed_x = 0
    current_offset_x = 0

    tile = None
    ti_x = 0
    ti_y = 2

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print("INIT W:" + str(self.width) + " H:" + str(self.height))
        self.init_vertical_lines()
        self.init_horizontal_lines()
        self.init_tiles()

        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)
        Clock.schedule_interval(self.update, 1.0 / 60.0)
    
    def is_desktop(self):
        if platform.system() in ('Linux', 'Windows', 'Darwin'):
            return True
        return False
    
    def init_vertical_lines(self):
        with self.canvas:
            Color(1,1,1)
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())
    
    def init_tiles(self):
        with self.canvas:
            Color(1, 1, 1)
            self.tile = Quad()

    def get_line_x_from_index(self, index):
        central_line_x = self.perspective_point_x
        spacing = self.V_LINES_SPACING * self.width
        offset = index - 0.5
        line_x = central_line_x + offset * spacing + self.current_offset_x
        return line_x
    
    def get_line_y_from_index(self, index):
        spacing_y = self.H_LINES_SPACING * self.height
        line_y = index * spacing_y - self.current_offset_y
        return line_y
    
    def get_tile_coordinates(self, ti_x, ti_y):
        x = self.get_line_x_from_index(ti_x)
        y = self.get_line_y_from_index(ti_y)
        return x, y

    def update_tiles(self):
        xmin, ymin = self.get_tile_coordinates(self.ti_x, self.ti_y)
        xmax, ymax = self.get_tile_coordinates(self.ti_x + 1, self.ti_y + 1)
        x1, y1 = self.transform(xmin, ymin)
        x2, y2 = self.transform(xmin, ymax)
        x3, y3 = self.transform(xmax, ymax)
        x4, y4 = self.transform(xmax, ymin)
        self.tile.points = [ x1, y1, x2, y2, x3, y3, x4, y4 ]

    def update_vertical_lines(self):
        start_index = -int(self.V_NB_LINES / 2) + 1

        for i in range(start_index, start_index + self.V_NB_LINES):
            line_x = self.get_line_x_from_index(i)
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]

    def init_horizontal_lines(self):
        with self.canvas:
            Color(1,1,1)
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())
    
    def update_horizontal_lines(self):
        start_index = -int(self.V_NB_LINES / 2) + 1
        end_index = start_index + self.V_NB_LINES - 1

        xmin = self.get_line_x_from_index(start_index)
        xmax = self.get_line_x_from_index(end_index)
        for i in range(0, self.H_NB_LINES):
            line_y = self.get_line_y_from_index(i)
            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax, line_y)
            self.horizontal_lines[i].points = [x1, y1, x2, y2]
    
    def update(self, dt):
        time_factor = dt * 60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.update_tiles()
        # self.current_offset_y += self.SPEED * time_factor

        spacing_y = self.H_LINES_SPACING * self.height
        if self.current_offset_y >= spacing_y:
            self.current_offset_y -= spacing_y

        # self.current_offset_x += self.current_speed_x * time_factor
class GalaxyApp(App):
    pass

GalaxyApp().run()