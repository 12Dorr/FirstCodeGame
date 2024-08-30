import turtle as t
import random

# 创建窗口
game_window = t.Screen()
# 设置窗口大小
game_window.setup(width=800, height=600)
#设置标题
game_window.title("双人乒乓对抗")
# 设置背景颜色
game_window.bgcolor("orange")



# 创建p1球拍
p1=t.Turtle()
p1.ht()#先隐藏
p1.up()
p1.speed(0)#设置速度为0，即最快
# 设置球拍的形状和颜色
p1.color("red")
p1.shape("square")
# 设置球拍的大小
p1.shapesize(4,0.5)
# 设置球拍的位置
p1.goto(-350,0)
p1.st()#再显示

# 创建p2球拍
p2=t.Turtle()
p2.ht()#先隐藏
p2.up()
p2.speed(0)#设置速度为0，即最快
# 设置球拍的形状和颜色
p2.color("blue")
p2.shape("square")
# 设置球拍的大小
p2.shapesize(4,0.5)
# 设置球拍的位置
p2.goto(350,0)
p2.st()#再显示

#统计得分
p1_score=0
p2_score=0

# 显示得分
score_board = t.Turtle()
score_board.ht()
score_board.up()
score_board.speed(0)
score_board.color("white")

def show_score():
    score_board.clear()
    score_board.goto(-300, 250)
    score_board.write("Player 1得分： {}".format(p1_score), align="center", font=("Arial", 16, "normal"))
    score_board.goto(300, 250)
    score_board.write(f"{p2_score}：Player 2得分", align="center", font=("Arial", 16, "normal"))
show_score()

def p1_move_up():
    y=p1.ycor()#获取y坐标
    y+=10#移动5像素
    p1.sety(y)#设置y坐标

def p1_move_down():
    y = p1.ycor()  # 获取y坐标
    y -= 10 # 移动5像素
    p1.sety(y)  # 设置y坐标

game_window.listen()#监听键盘事件
game_window.onkey(p1_move_up, "w")#按下w键向上移动
game_window.onkey(p1_move_down, "s")#按下s键向下移动

# 定义p2移动函数
def p2_move_up():
    y=p2.ycor()#获取y坐标
    y+=10#移动5像素
    p2.sety(y)#设置y坐标

def p2_move_down():
    y = p2.ycor()  # 获取y坐标
    y -= 10  # 移动5像素
    p2.sety(y)  # 设置y坐标

game_window.listen()#监听键盘事件
game_window.onkey(p2_move_up, "Up")#按下键盘上的Up键向上移动
game_window.onkey(p2_move_down, "Down")#按下键盘上的Down键向下移动

#创建乒乓球
ball=t.Turtle()
ball.up()
ball.speed(0)
# 设置球的形状和颜色
ball.color("white")
ball.shape("circle")
# 设置球的大小
ball.shapesize(1,1)
ball.dx=5#设置x方向速度
ball.dy=-5#设置y方向速度

# 判定是否退出游戏
running=True
def exit_game():
    global running
    running=False

#获取窗口得Tkinter对象,并绑定退出函数
root=game_window.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", exit_game)


#球动
while running:

    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)
    # 边界检测
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
    # 接球
    y_up=p1.ycor()+50
    y_down=p1.ycor()-50
    if ball.ycor() < y_up and ball.ycor() > y_down and ball.xcor()<-330 :
        ball.dx *= -1
        ball.setx(-329)
    if ball.ycor() < p2.ycor()+50 and ball.ycor() > p2.ycor()-50 and ball.xcor() > 330:
        ball.dx *= -1
        ball.setx(329)

    #球出界
    if ball.xcor() > 340 :
        ball.goto(0,0)
        ball.dx *= -1
        p1_score += 1
        show_score()
    if ball.xcor() < -340:
        ball.goto(0,0)
        ball.dx *= -1
        p2_score += 1
        show_score()



# 保持窗口打开，直到用户关闭
#t.done()# 等同于game_window.mainloop()