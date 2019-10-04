from graph import *

x = 650
y = 1100
windowSize(x,y)
canvasSize(x,y)
c = canvas()

def fence(x1,y1,x2,y2):
    penColor("brown")
    brushColor(244, 164, 96)
    rectangle(x1,y1,x2,y2)
    for i in range(10):
        moveTo(x1+(i) * (x2//10), y1)
        lineTo(x1+i * (x2//10), y2)
        
def chain(x,y):
    for i in range (10):
        penColor('black')
        oval(x - 7*i, y + 7*i, x - 7*(i-1), y+ 7*i, 16)
        penColor('green')
        oval(x - 7*i, y+ 7*i, x - 7*(i-1), y+ 7*i, 12)

def sky(x1,y1,x2,y2):
    penColor(30, 144, 255)
    brushColor(30, 144, 255)
    rectangle(x1,y1,x2,y2)

def grass(x1,y1,x2,y2):
    penColor("green")
    brushColor("green")
    rectangle(x1,y1,x2,y2)


def oval(x1, y1, x2, y2, r):
    j = ((x1 + x2) / 2) - r
    k = ((y1 + y2) / 2) - r
    for j in range(((int(x1 + x2)) // 2) + int(r)):
        for k in range((int(y1 + y2) // 2) + int(r)):
            if ((j - x1) ** 2 + (k - y1) ** 2) ** (0.5) + ((j - x2) ** 2 + (k - y2) ** 2) ** (0.5) <= r:
                point(int(j), int(k))


def psina(x, y, m, k): #m - направление собаки, k - размер
    penColor(188, 143, 143)
    brushColor(188, 143, 143)

    oval(x * k, y * k, (x + 100 * m) * k, y * k, 130 * k)
    oval((x + m * 50) * k, (y - 20) * k, (x + m * 150) * k, (y - 20) * k, 125 * k)

    oval((x - 20 * m) * k, y * k, (x - 20 * m) * k, (y + 100) * k, 110 * k)
    oval((x + 35 * m) * k, (y + 20) * k, (x + m * 35) * k, (y + 120) * k, 110 * k)

    oval((x + m * 150) * k, y * k, (x + m * 150) * k, (y + 20) * k, k * 60)
    oval(k * (x + m * 80), k * (y - 40), k * (x + m * 80), k * (y - 20), k * 60)

    oval(k * (x + m * 35), k * (y + 120), k * x, k * (y + 120), k * 40)
    oval(k * (x - m * 20), k * (y + 100), k * (x - m * 55), k * (y + 100), k * 40)

    oval(k * (x + m * 160), k * (y + 15), k * (x + m * 160), k * (y + 105), k * 95)
    oval(k * (x + m * 90), k * y, k * (x + m * 90), k * (y + 90), k * 95)

    oval(k * (x + m * 130), k * (y + 100), k * (x + m * 165), k * (y + 100), k * 40)
    oval(k * (x + m * 60), k * (y + 85), k * (x + m * 95), k * (y + 85), k * 40)

    penColor('black')
    rectangle(k * (x - 30 * m), k * (y - 70), k * (x + m * 50), k * (y + 10))

    penColor('black')
    oval(k * (x + m * 50), k * (y - 65), k * (x + m * 50), k * (y - 50), k * 40)
    penColor(188, 143, 143)
    oval(k * (x + m * 50), k * (y - 65), k * (x + m * 50), k * (y - 50), k * 38)

    penColor('black')
    oval(k * (x - 30 * m), k * (y - 65), k * (x - 30 * m), k * (y - 50), k * 40)
    penColor(188, 143, 143)
    oval(k * (x - 30 * m), k * (y - 65), k * (x - 30 * m), k * (y - 50), k * 38)

    penColor('black')
    oval(k * (x + m * 20), k * (y - 40), k * (x + m * 35), k * (y - 40), k * 18)
    penColor('white')
    oval(k * (x + m * 20), k * (y - 40), k * (x + m * 35), k * (y - 40), k * 16)
    penColor('black')
    brushColor('black')
    circle(k * (x + m * 28), k * (y - 40), k * 3)

    penColor('black')
    oval(k * (x - m * 15), k * (y - 40), k * (x), k * (y - 40), k * 18)
    penColor('white')
    oval(k * (x - m * 15), k * (y - 40), k * (x), k * (y - 40), k * 16)
    penColor('black')
    brushColor('black')
    circle(k * (x - m * 8), k * (y - 40), k * 3)

    penColor('black')
    oval(k * (x - 15 * m), k * (y - 5), k * (x + m * 35), k * (y - 5), k * 55)
    penColor(188, 143, 143)
    oval(k * (x - m * 15), k * (y - 3), k * (x + m * 35), k * (y - 3), k * 55)

    penColor('white')
    brushColor('white')
    polygon([(k * (x - 10 * m), k * (y - 13)), (k * (x - 4 * m), k * (y - 23)), (k * (x - 2 * m), k * (y - 15))])
    polygon([(k * (x + m * 28), k * (y - 13)), (k * (x + m * 26), k * (y - 23)), (k * (x + m * 20), k * (y - 15))])


def doghouse(x0,y0):
    penColor('black')
    brushColor(244, 164, 96)
    polygon([(x0, y0), (x0, y0-150), (x0-100, y0-230), (x0-100, y0-80)])
    polygon([(x0, y0), (x0, y0-150), (x0+100, y0-230), (x0+100, y0-120)])
    brushColor(139, 69, 19)
    polygon([(x0, y0-150), (x0-100, y0-230), (x0-50, y0-320)])
    polygon([(x0, y0-150), (x0-50, y0-320), (x0+40, y0-340), (x0+100, y0-230)])
    oval(x0-50, y0-70, x0-50, y0-170, 115)

sky(0, 0, 650, 450)
grass(0, 450, 650, 1100)
penColor("blue")
fence(200, 100, 650, 450)
fence(400, 390, 650, 550)
fence(0, 270, 295, 570)
fence(0, 350, 360, 687)
psina(1200, 1350, -1, 0.5)
doghouse(x//2+100, y//2+300)
psina(100, y-150, 1, 0.9)
psina(190, y-40, -1, 0.65)
psina(600, 850, 1, 1)
chain(360,840)

run()
