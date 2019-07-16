import random
from tkinter import *
import tkinter.messagebox
import time
import threading
import winsound
global x
global digs
global reum
global lonk
global ranc
global pond
global site
global exot
global inst
global mrkt

global W1
global W2
global W3
global W4
global W5
global W6
global W7

global n1
global n2
global n3
global n4
global n5
global n6
global n7
global n8

global X1
global X2
global X3
global X4
global X5
global X6
global X7

global Z1
global Z2
global Z3
global Z4
global Z5
global Z6
global Z7

global M

global BHN
W1 = 100
W2 = 200
W3 = 300
W4 = 500
W5 = 1000
W6 = 1500
W7 = 2000

n1 = 10
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0

X1 = 0
X2 = 0
X3 = 0
X4 = 0
X5 = 0
X6 = 0
X7 = 0

Z1 = 109
Z2 = 109
Z3 = 109
Z4 = 109
Z5 = 110
Z6 = 110
Z7 = 110

M = 49


x = 0

BHN = 1
inst = 0
exot = 0
digs = 0
mrkt = 0
lonk = 10
ranc = 0
pond = 0
site = 0
reum = 500
def bonusplus():
    global digs
    global reum
    global lonk
    global ranc
    global pond
    global site
    global exot
    global inst
    global mrkt
    global W1
    global W2
    global W3
    global W4
    global W5
    global W6
    global W7
    global n1
    global n2
    global n3
    global n4
    global n5
    global n6
    global n7
    global X1
    global X2
    global X3
    global X4
    global X5
    global X6
    global X7
    global Z1
    global Z2
    global Z3
    global Z4
    global Z5
    global Z6
    global Z7
    global M
    global digs
    global reum
    global lonk
    global ranc
    global pond
    global site
    global exot
    global inst
    global mrkt
    global n8

    X1 = random.randint(-109, Z1)
    if X1 < 0:
        if Z1 > 0:
            Z1 = Z1 - 1
            sspeed.config(fg="red")
    else:
        Z1 = Z1 + 1
        sspeed.config(fg="green")
    W1 = W1 + (X1 // 20)
    if W1 > 1000:
        if Z1 > 100:
            Z1 = Z1 + random.randint(-100, -1)
        elif Z1 > 80:
            Z1 = Z1 + random.randint(-80, -1)
        elif Z1 > 60:
            Z1 = Z1 + random.randint(-60, -1)
        elif Z1 > 40:
            Z1 = Z1 + random.randint(-40, -1)
    if W1 < 10:
        Z1 = Z1 + random.randint(1, 100)

    X2 = random.randint(-109, Z2)
    if X2 < 0:
        if Z2 > 0:
            Z2 = Z2 - 1
            mspeed.config(fg="red")
    else:
        Z2 = Z2 + 1
        mspeed.config(fg="green")
    W2 = W2 + (X2 // 20)
    if W2 > 2000:
        if Z2 > 100:
            Z2 = Z2 + random.randint(-100, -1)
        elif Z2 > 80:
            Z2 = Z2 + random.randint(-80, -1)
        elif Z2 > 60:
            Z2 = Z2 + random.randint(-60, -1)
        elif Z2 > 40:
            Z2 = Z2 + random.randint(-40, -1)
    if W2 < 20:
        Z2 = Z2 + random.randint(1, 100)
    X3 = random.randint(-109, Z3)
    if X3 < 0:
        if Z3 > 0:
            Z3 = Z3 - 1
            bspeed.config(fg="red")
    else:
        Z3 = Z3 + 1
        bspeed.config(fg="green")
    W3 = W3 + (X3 // 20)
    if W3 > 3000:
        if Z3 > 100:
            Z3 = Z3 + random.randint(-100, -1)
        elif Z3 > 80:
            Z3 = Z3 + random.randint(-80, -1)
        elif Z3 > 60:
            Z3 = Z3 + random.randint(-60, -1)
        elif Z3 > 40:
            Z3 = Z3 + random.randint(-40, -1)
    if W3 < 30:
        Z3 = Z3 + random.randint(1, 100)
    X4 = random.randint(-109, Z4)
    if X4 < 0:
        if Z4 > 0:
            Z4 = Z4 - 1
            cspeed.config(fg="red")
    else:
        Z4 = Z4 + 1
        cspeed.config(fg="green")
    W4 = W4 + (X4 // 20)
    if W4 > 5000:
        if Z4 > 100:
            Z4 = Z4 + random.randint(-100, -1)
        elif Z4 > 80:
            Z4 = Z4 + random.randint(-80, -1)
        elif Z4 > 60:
            Z4 = Z4 + random.randint(-60, -1)
        elif Z4 > 40:
            Z4 = Z4 + random.randint(-40, -1)
    if W4 < 40:
        Z4 = Z4 + random.randint(1, 100)
    X5 = random.randint(-109, Z5)
    if X5 < 0:
        if Z5 > 0:
            Z5 = Z5 - 1
            aspeed.config(fg="red")
    else:
        Z5 = Z5 + 1
        aspeed.config(fg="green")
    W5 = W5 + (X5 // 20)
    if W5 > 10000:
        if Z5 > 100:
            Z5 = Z5 + random.randint(-100, -1)
        elif Z5 > 80:
            Z5 = Z5 + random.randint(-80, -1)
        elif Z5 > 60:
            Z5 = Z5 + random.randint(-60, -1)
        elif Z5 > 40:
            Z5 = Z5 + random.randint(-40, -1)
    if W5 < 50:
        Z5 = Z5 + random.randint(1, 100)
    X6 = random.randint(-109, Z6)
    if X6 < 0:
        if Z6 > 0:
            Z6 = Z6 - 1
            jspeed.config(fg="red")
    else:
        Z6 = Z6 + 1
        jspeed.config(fg="green")
    W6 = W6 + (X6 // 20)
    if W6 > 15000:
        if Z6 > 100:
            Z6 = Z6 + random.randint(-100, -1)
        elif Z6 > 80:
            Z6 = Z6 + random.randint(-80, -1)
        elif Z6 > 60:
            Z6 = Z6 + random.randint(-60, -1)
        elif Z6 > 40:
            Z6 = Z6 + random.randint(-40, -1)
    if W6 < 60:
        Z6 = Z6 + random.randint(1, 100)
        
    X7 = random.randint(-109, Z7)
    if X7 < 0:
        if Z7 > 0:
            Z7 = Z7 - 1
            hspeed.config(fg="red")
    else:
        Z7 = Z7 + 1
        hspeed.config(fg="green")
    W7 = W7 + (X7 // 20)
    if W7 > 20000:
        if Z7 > 100:
            Z7 = Z7 + random.randint(-100, -1)
        elif Z7 > 80:
            Z7 = Z7 + random.randint(-80, -1)
        elif Z7 > 60:
            Z7 = Z7 + random.randint(-60, -1)
        elif Z7 > 40:
            Z7 = Z7 + random.randint(-40, -1)
    if W7 < 10:
        Z7 = Z7 + random.randint(1, 100)


    for i in range(1, n8):
        reum = reum + 1

    if n1 > 999:
        reum = reum + (W1 // 10)
    if n2 > 1999:
        reum = reum + (W2 // 10)
    if n3 > 2999:
        reum = reum + (W3 // 10)
    if n4 > 4999:
        reum = reum + (W4 // 10)
    if n5 > 9999:
        reum = reum + (W5 // 10)
    if n6 > 14999:
        reum = reum + (W6 // 10)
    if n7 > 19999:
        reum = reum + (W7 // 10)



    _reumamount.config(text=reum)
    scost.config(text=(1000 - n1))
    sspeed.config(text=W1)

    mcost.config(text=(2000 - n2))
    mspeed.config(text=W2)

    bcost.config(text=(3000 - n3))
    bspeed.config(text=W3)

    ccost.config(text=(5000 - n4))
    cspeed.config(text=W4)

    acost.config(text=(10000 - n5))
    aspeed.config(text=W5)

    jcost.config(text=(15000 - n6))
    jspeed.config(text=W6)

    hcost.config(text=(20000 - n7))
    hspeed.config(text=W7)

    ecost.config(text=(20 - n8))


def augustus():
    lab = Label(utheroot, text="YOU ARE THE WEALTHIEST PERSON IN HISTORY***" )
    lab.grid(row=1, column=15)
    lob = Label(utheroot, text="as rich as augustus ceasar")
    lob.grid(row=2, column=15)
    und = Label(utheroot, text="***this cant be proven since wealth is difficult to measure with all of the leaders of nations")
    und.grid(row=6, column=15)





def clickz():
    global x
    if x == 0:
        def f(f_stop):
            bonusplus()
            if not f_stop.is_set():
                threading.Timer(.5, f, [f_stop]).start()

        f_stop = threading.Event()
        # start calling f now and every 60 sec thereafter
        f(f_stop)
        x = 1


def ba1():
    for i in range(0, 1000):
        lonkshack()
def bh1():
    for i in range(1, 100):
        lonkshack()
def sh1():
    for i in range(1, 100):
        lonkacqu()

def ba2():
    for i in range(0, 2000):
        digsshack()
def bh2():
    for i in range(1, 100):
        lonkshack()
def sh2():
    for i in range(1, 100):
        lonkacqu()

def ba3():
    for i in range(0, 3000):
        rancshack()
def bh3():
    for i in range(1, 100):
        lonkshack()
def sh3():
    for i in range(1, 100):
        lonkacqu()
def ba4():
    for i in range(0, 5000):
        pondshack()
def bh4():
    for i in range(1, 100):
        lonkshack()
def sh4():
    for i in range(1, 100):
        lonkacqu()

def ba5():
    for i in range(0, 10000):
        siteshack()
def bh5():
    for i in range(1, 100):
        lonkshack()
def sh5():
    for i in range(1, 100):
        lonkacqu()

def ba6():
    for i in range(0, 15000):
        instshack()
def bh6():
    for i in range(1, 100):
        lonkshack()
def sh6():
    for i in range(1, 100):
        lonkacqu()


def ba7():
    for i in range(0, 20000):
        mrktshack()
def bh7():
    for i in range(1, 100):
        lonkshack()
def sh7():
    for i in range(1, 100):
        lonkacqu()

def bshwshack():
    global reum
    global BHN
    global n1
    global n8
    if n8 < 20:
        if reum > 1999:
            BHN = BHN - 0.3
            _lonkamount.config(text=lonk)
            reum = reum - 2000
            _reumamount.config(text=reum)
            
            n8 = n8 + 1
            if n8 > 19:
                BHNadd.config(fg="red")

def lonkshack():
    global reum
    global lonk
    global n1
    global W1
    if n1 < 1000:
        if reum > W1:
            lonk = lonk + 1
            _lonkamount.config(text=lonk)
            reum = reum - (W1 * BHN)
            _reumamount.config(text=reum)
            
            n1 = n1 + 1
            if n1 > 100:
                W1 = W1 + 1
            if n1 > 999:
                lonkadd.config(fg="red")






def lonkacqu():
    global reum
    global lonk
    global n1
    global W1
    if n1 > 0:
        if n1 < 1000:
            lonk = lonk - 1
            _lonkamount.config(text=lonk)
            reum = reum + (W1 // BHN)
            _reumamount.config(text=reum)
            n1 = n1 - 1
            if n1 > 100:
                W1 = W1 - 1

         

def digsshack():
    global reum
    global digs
    global n2
    global W2
    if n2 < 2000:
        if reum > W2:
            digs = digs + 1
            _digsamount.config(text=digs)
            reum = reum - (W2 * BHN)
            _reumamount.config(text=reum)
            
            n2 = n2 + 1
            if n2 > 200:
                W2 = W2 + 1
            if n2 > 1999:
                digsadd.config(fg="red")


def digsacqu():
    global reum
    global digs
    global n2
    global W2
    if n2 > 0:
        if n2 < 2000:
            digs = digs - 1
            _digsamount.config(text=digs)
            reum = reum + (W2 // BHN)
            _reumamount.config(text=reum)
            n2 = n2 - 1
            if n2 > 200:
                W2 = W2 - 1


         

def rancshack():
    global reum
    global ranc
    global n3
    global W3
    if n3 < 3000:
        if reum > W3:
            ranc = ranc + 1
            _rancamount.config(text=ranc)
            reum = reum - (W3 * BHN)
            _reumamount.config(text=reum)
            
            n3 = n3 + 1
            if n3 > 300:
                W3 = W3 + 1
            if n3 > 2999:
                rancadd.config(fg="red")



def rancacqu():
    global reum
    global ranc
    global n3
    global W3
    if n3 > 0:
        if n3 < 3000:
            ranc = ranc - 1
            _rancamount.config(text=ranc)
            reum = reum + (W3 // BHN)
            _reumamount.config(text=reum)
            n3 = n3 - 1
            if n3 > 300:
                W3 = W3 - 1



def pondshack():
    global reum
    global pond
    global n4
    global W4
    if n4 < 5000:
        if reum > W4:
            pond = pond + 1
            _pondamount.config(text=pond)
            reum = reum - (W4 * BHN)
            _reumamount.config(text=reum)
            
            n4 = n4 + 1
            if n4 > 500:
                W4 = W4 + 1
            if n4 > 4999:
                pondadd.config(fg="red")


def pondacqu():

    global reum
    global pond
    global n4
    global W4
    if n4 > 0:
        if n4 < 5000:
            pond = pond - 1
            _pondamount.config(text=pond)
            reum = reum + (W4 // BHN)
            _reumamount.config(text=reum)
            n4 = n4 - 1
            if n4 > 500:
                W4 = W4 - 1

def siteshack():
    global reum
    global site
    global n5 
    global W5
    if n5 < 10000:
        if reum > W5:
            site = site + 1
            _siteamount.config(text=site)
            reum = reum - (W5 * BHN)
            _reumamount.config(text=reum)
            
            n5 = n5 + 1
            if n5 > 1000:
                W5 = W5 + 1
            if n5 > 9999:
                siteadd.config(fg="red")

def siteacqu():

    global reum
    global site
    global n5
    global W5
    if n5 > 0:
        if n5 < 10000:
            site = site - 1

            _siteamount.config(text=site)
            reum = reum + (W5 // BHN)
            _reumamount.config(text=reum)
            n5 = n5 - 1
            if n5 > 1000:
                W5 = W5 - 1


    time.sleep(.25)

def instshack():
    global reum
    global inst
    global n6
    global W6
    if n6 < 15000:
        if reum > W6:
            inst = inst + 1
            _instamount.config(text=inst)
            reum = reum - (W6 * BHN)
            _reumamount.config(text=reum)
            
            n6 = n6 + 1
            if n6 > 1500:
                W6 = W6 + 1
            if n6 > 14999:
                instadd.config(fg="red")


         
def instacqu():

    global reum
    global inst
    global n6
    global W6
    if n6 > 0:
        if n6 < 15000:
            inst = inst - 1

            _instamount.config(text=inst)
            reum = reum + (W6 // BHN)
            _reumamount.config(text=reum)
            n6 = n6 - 1
            if n6 > 1500:
                W6 = W6 - 1



def mrktshack():
    global reum
    global mrkt
    global n7
    global W7
    if n7 < 20000:
        if reum > W7:
            mrkt = mrkt + 1
            _mrktamount.config(text=mrkt)
            reum = reum - (W7 * BHN)
            _reumamount.config(text=reum)
            n7 = n7 + 1
            if n7 > 2000:
                W7 = W7 + 1
            if n7 > 19999:
                mrktadd.config(fg="red")


         
def mrktacqu():

    global reum
    global mrkt
    global n7
    global W7
    if n7 > 0:
        if n7 < 20000:
            mrkt = mrkt - 1

            _mrktamount.config(text=mrkt)
            reum = reum + (W7 // BHN)
            _reumamount.config(text=reum)
            n7 = n7 - 1
            if n7 > 2000:
                W7 = W7 - 1

utheroot = Tk()
utheroot.title("wall street")
chinas = PhotoImage(file="app.png")
morgan = PhotoImage(file="alp.png")
americ = PhotoImage(file="mic.png")
centra = PhotoImage(file="jpm.png")
bigban = PhotoImage(file="exx.png")
medban = PhotoImage(file="sam.png")
smaban = PhotoImage(file="toy.png")
ban1 = PhotoImage(file="boa.png")
ban2 = PhotoImage(file="wel.png")
ban3 = PhotoImage(file="rds.png")
ban4 = PhotoImage(file="che.png")
ban5 = PhotoImage(file="int.png")
ban6 = PhotoImage(file="nvi.png")
ban7 = PhotoImage(file="vol.png")
ban8 = PhotoImage(file="dai.png")
berhat = PhotoImage(file="BHI.png")

clicko = Button(utheroot, text='start game', command=clickz)
clicko.grid(row=0, column=3)

r_my = Label(utheroot, text='MY')
r_my.grid(row=2, column=0, sticky=W)

r_wallet = Label(utheroot, text='MONEY')
r_wallet.grid(row=3, column=0, sticky=W)

_reumamount = Label(utheroot, text=reum)
_reumamount.grid(row=4, column=0, sticky=E)

r_wallet = Label(utheroot, text='$')
r_wallet.grid(row=4, column=1, sticky=W)

# number 1 is empty #

m_title = Label(utheroot, text='WALL STREET')
m_title.grid(row=0, column=2)

vba1 = Button(utheroot, text='buy toyota', command=ba1)
vba1.grid(row=18, column=2)

vba2 = Button(utheroot, text='buy samsung', command=ba2)
vba2.grid(row=19, column=2)

vba3 = Button(utheroot, text='buy exxonmobil', command=ba3)
vba3.grid(row=20, column=2)

vba4 = Button(utheroot, text='buy JPM chase', command=ba4)
vba4.grid(row=21, column=2)

vba5 = Button(utheroot, text='buy microsoft', command=ba5)
vba5.grid(row=20, column=1)

vba6 = Button(utheroot, text='buy alphabet', command=ba6)
vba6.grid(row=21, column=1)

vba7 = Button(utheroot, text='buy apple', command=ba7)
vba7.grid(row=19, column=1)

BHNadd = Button(utheroot, text='buy 1 berkshire', command=bshwshack)
BHNadd.grid(row=24, column=1)

espeed = Label(utheroot, text="2000", fg="green")
espeed.grid(row=25, column=1)

ecost = Label(utheroot, text=(20 - n8), fg="gray")
ecost.grid(row=26, column=1)

lberhat = Label(utheroot, image=berhat)
lberhat.grid(row=23, column=1)
m_lonk = Label(utheroot, text='toyota')
m_lonk.grid(row=2, column=3)

lsmaban = Label(utheroot, image=smaban)
lsmaban.grid(row=1, column=3)

_lonkamount = Label(utheroot, text=lonk)
_lonkamount.grid(row=3, column=3)

lonkadd = Button(utheroot, text='buy shares', command=lonkshack)
lonkadd.grid(row=4, column=3)

lonkadd2 = Button(utheroot, text='sell shares', command=lonkacqu)
lonkadd2.grid(row=5, column=3)

sspeed = Label(utheroot, text=W1, fg="green")
sspeed.grid(row=6, column=3)
scost = Label(utheroot, text=(1000 - n1), fg="gray")
scost.grid(row=7, column=3)
m_digs = Label(utheroot, text='samsung')
m_digs.grid(row=2, column=6)

_digsamount = Label(utheroot, text=digs)
_digsamount.grid(row=3, column=6)

lmedban = Label(utheroot, image=medban)
lmedban.grid(row=1, column=6)

digsadd = Button(utheroot, text='buy shares', command=digsshack)
digsadd.grid(row=4, column=6)

digsadd2 = Button(utheroot, text='sell shares', command=digsacqu)
digsadd2.grid(row=5, column=6)
mspeed = Label(utheroot, text=W2, fg="green")
mspeed.grid(row=6, column=6)
mcost = Label(utheroot, text=(2000 - n2), fg="gray")
mcost.grid(row=7, column=6)
m_ranc = Label(utheroot, text='exxon mobil')
m_ranc.grid(row=2, column=9)

_rancamount = Label(utheroot, text=ranc)
_rancamount.grid(row=3, column=9)

lbigban = Label(utheroot, image=bigban)
lbigban.grid(row=1, column=9)

rancadd = Button(utheroot, text='buy shares', command=rancshack)
rancadd.grid(row=4, column=9)

rancadd2 = Button(utheroot, text='sell shares', command=rancacqu)
rancadd2.grid(row=5, column=9)
bspeed = Label(utheroot, text=W3, fg="green")
bspeed.grid(row=6, column=9)
bcost = Label(utheroot, text=(3000 - n3), fg="gray")
bcost.grid(row=7, column=9)
m_pond = Label(utheroot, text='JPM chase')
m_pond.grid(row=2, column=12)

_pondamount = Label(utheroot, text=pond)
_pondamount.grid(row=3, column=12)

lcentra = Label(utheroot, image=centra)
lcentra.grid(row=1, column=12)

pondadd = Button(utheroot, text='buy shares', command=pondshack)
pondadd.grid(row=4, column=12)

pondadd2 = Button(utheroot, text='sell shares', command=pondacqu)
pondadd2.grid(row=5, column=12)
cspeed = Label(utheroot, text=W4, fg="green")
cspeed.grid(row=6, column=12)
ccost = Label(utheroot, text=(5000 - n4), fg="gray")
ccost.grid(row=7, column=12)





m_site = Label(utheroot, text='microsoft', fg="purple")
m_site.grid(row=17, column=15)

_siteamount = Label(utheroot, text=site)
_siteamount.grid(row=18, column=15)

lameric = Label(utheroot, image=americ)
lameric.grid(row=16, column=15)

siteadd = Button(utheroot, text='buy shares', command=siteshack)
siteadd.grid(row=19, column=15)

siteadd2 = Button(utheroot, text='sell shares', command=siteacqu)
siteadd2.grid(row=20, column=15)
aspeed = Label(utheroot, text=W5, fg="green")
aspeed.grid(row=21, column=15)
acost = Label(utheroot, text=(10000 - n5), fg="gray")
acost.grid(row=22, column=15)






m_inst = Label(utheroot, text='alphabet', fg="purple")
m_inst.grid(row=10, column=15)

_instamount = Label(utheroot, text=inst)
_instamount.grid(row=11, column=15)
lmorgan = Label(utheroot, image=morgan)
lmorgan.grid(row=9, column=15)
instadd = Button(utheroot, text='buy shares', command=instshack)
instadd.grid(row=12, column=15)

instadd2 = Button(utheroot, text='sell shares', command=instacqu)
instadd2.grid(row=13, column=15)
jspeed = Label(utheroot, text=W6, fg="green")
jspeed.grid(row=14, column=15)
jcost = Label(utheroot, text=(15000 - n6), fg="gray")
jcost.grid(row=15, column=15)




m_mrkt = Label(utheroot, text='apple', fg="purple")
m_mrkt.grid(row=2, column=15)

_mrktamount = Label(utheroot, text=mrkt)
_mrktamount.grid(row=3, column=15)

lchinas = Label(utheroot, image=chinas)
lchinas.grid(row=1, column=15)

mrktadd = Button(utheroot, text='buy shares', command=mrktshack)
mrktadd.grid(row=4, column=15)

mrktadd2 = Button(utheroot, text='sell shares', command=mrktacqu)
mrktadd2.grid(row=5, column=15)

b1 = Label(utheroot, image=ban1)
b1.grid(row=9, column=12)

m1 = Label(utheroot, text="bank of america")
m1.grid(row=10, column=12)

p1 = Button(utheroot, text="WIP")
p1.grid(row=12, column=12)

b4 = Label(utheroot, image=ban3)
b4.grid(row=9, column=9)

m4 = Label(utheroot, text="royal dutch shell")
m4.grid(row=10, column=9)

p4 = Button(utheroot, text="WIP")
p4.grid(row=12, column=9)

b5 = Label(utheroot, image=ban5)
b5.grid(row=9, column=6)

m5 = Label(utheroot, text="intel")
m5.grid(row=10, column=6)

p5 = Button(utheroot, text="WIP")
p5.grid(row=12, column=6)

b7 = Label(utheroot, image=ban7)
b7.grid(row=9, column=3)

m7 = Label(utheroot, text="volkswagen")
m7.grid(row=10, column=3)

p7 = Button(utheroot, text="WIP")
p7.grid(row=12, column=3)


b2 = Label(utheroot, image=ban2)
b2.grid(row=16, column=12)

m2 = Label(utheroot, text="wells fargo")
m2.grid(row=17, column=12)

p2 = Button(utheroot, text="WIP")
p2.grid(row=19, column=12)

b3 = Label(utheroot, image=ban4)
b3.grid(row=16, column=9)

m3 = Label(utheroot, text="chevron")
m3.grid(row=17, column=9)

p3 = Button(utheroot, text="WIP")
p3.grid(row=19, column=9)

b6 = Label(utheroot, image=ban6)
b6.grid(row=16, column=6)

m6 = Label(utheroot, text="nvidia")
m6.grid(row=17, column=6)

p6 = Button(utheroot, text="WIP")
p6.grid(row=19, column=6)

b8 = Label(utheroot, image=ban8)
b8.grid(row=16, column=3)

m8 = Label(utheroot, text="daimler")
m8.grid(row=17, column=3)

p8 = Button(utheroot, text="WIP")
p8.grid(row=19, column=3)

hspeed = Label(utheroot, text=W7, fg="green")
hspeed.grid(row=6, column=15)
hcost = Label(utheroot, text=(20000 - n7), fg="gray")
hcost.grid(row=7, column=15)
uspeed = Label(utheroot, text="green digits are the prices of the shares in the companys", fg="green")
uspeed.grid(row=13, column=18)
ubspeed = Label(utheroot, text="gray digits are the amount of shares in company", fg="gray")
ubspeed.grid(row=15, column=18)
utheroot.mainloop()