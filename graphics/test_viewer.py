from viewer import Viewer, FilledPolygon, Transform 

viewer = Viewer(600,400)

cart_w = 50.0
cart_h = 30.0
l,r,t,b = -cart_w/2, cart_w/2, cart_h/2, -cart_h/2
cart = FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
cart.set_color(.0,.8,.8)
carttrans = Transform()
cart.add_attr(carttrans)
viewer.geoms.append(cart)

pole_w = 10.0
pole_l = 125.0
l,r,t,b = -pole_w/2,pole_w/2,pole_l-pole_w/2,-pole_w/2
pole = FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
pole.set_color(.8,.6,.4)
poletrans = Transform(translation=(0, cart_h/4.0))
pole.add_attr(poletrans)
pole.add_attr(carttrans)
viewer.geoms.append(pole)

for i in range(100):
    viewer.render()
    print(i)

viewer.close()