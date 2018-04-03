#battery part
import resistor


def voltage(i):
    r = resistor.resistor_s(0) + resistor.resistor_p(1)
    return i / r


def current(v, r):
    return v / r

