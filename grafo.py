from turtle import (
    Screen,
    setup,
    delay,
    penup,
    goto,
    pendown,
    pencolor,
    pensize,
    onkeypress,
    listen,
    bye,
    done
)

setup(1200, 700)

campo = Screen()


def escenario():
    delay(0)
    penup()
    goto(-500, 700)
    pendown()
    goto(-500, -700)

    penup()
    goto(-480, -700)
    pendown()
    goto(-480, 700)

    penup()
    goto(500, 700)
    pendown()
    pencolor("blue")
    goto(500, -700)

    penup()
    goto(0, 700)
    pendown()
    pencolor("red")
    pensize(5)
    goto(0, -700)


escenario()

onkeypress(bye, 'q')
listen()
done()
