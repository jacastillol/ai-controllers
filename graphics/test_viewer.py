from viewer import Viewer, FilledPolygon, Transform 

viewer = Viewer(600,400)

cartwidth = 50.0
cartheight = 30.0
l,r,t,b = -cartwidth/2, cartwidth/2, cartheight/2, -cartheight/2
cart = FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
cart.set_color(.0,.8,.8)
carttrans = Transform()
cart.add_attr(carttrans)
viewer.geoms.append(cart)
for i in range(100):
    viewer.render()
    print(i)

viewer.close()