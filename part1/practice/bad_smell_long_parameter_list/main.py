# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, state, field):
        self.speed = 1
        self.state = state
        self.field = field

    def speed(self):
        if self.state == 'fly':
            self.speed *= 1.2
        elif self.state == 'crawl':
            self.speed *= 0.5
        else:
            raise ValueError('Рожденный ползать летать не должен!')

    def move(self,x_coord, y_coord, direction):
        if direction == 'UP':
            self.field.set_unit(x=x_coord, y=y_coord + self.speed, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(x=x_coord, y=y_coord + self.speed, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(x=x_coord, y=y_coord + self.speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(x=x_coord, y=y_coord + self.speed, unit=self)


#     ...
