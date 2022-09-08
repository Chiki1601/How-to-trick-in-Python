!pip install screen-brightness-control
import screen-brightness-control as pp

print(pp.get_brightness())
level = input("Enter the brightness level")

pp.set_brightness(level)

print(pp.set_brightness)
