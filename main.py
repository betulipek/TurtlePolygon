import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("orange")
drawing_board.title("Python Turtle")
turtle_polygon = turtle.Turtle()

polygon_side = 8
polygon_angle = 360 / polygon_side
polygon_lenght = 100

for i in range(polygon_side):
    turtle_polygon.left(polygon_angle)
    turtle_polygon.forward(polygon_lenght)

turtle.done()

