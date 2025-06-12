# ---Life Game---

import numpy as np

class App():
    # 0 = dead
    # 1 = live
    
    def __init__(self, ires):
        self.ires = ires
        self.iarr = np.zeros((ires, ires), dtype=int)
        self.ibuf = np.zeros((ires, ires), dtype=int)
        
    def decide_firstcell(self):
        self.iarr[10][10] = 1
        self.iarr[10][11] = 1
        self.iarr[11][10] = 1
        self.iarr[11][11] = 1
        
    def check_cell(self, ix, iy):
        icount = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                inx = ix + i
                iny = iy + j
                
                try:
                    if self.iarr[ix][iy] != self.iarr[inx][iny]:
                        icount += 1
                except IndexError:
                    # Ignore out of bounds
                    continue
        return icount
    
    def change_cell(self, ix, iy):
        icount = self.check_cell(ix, iy)
        
        # birth
        if self.iarr[ix][iy] == 0 and icount == 3:
            self.ibuf[ix][iy] = 1

        if self.iarr[ix][iy] == 1:
            # survive
            if icount == 2 or icount == 3:
                self.ibuf[ix][iy] = 1
            # death
            elif icount <= 1 or icount >= 4:
                self.ibuf[ix][iy] = 0
        else:
            self.ibuf[ix][iy] = self.iarr[ix][iy]
    
    def update(self):
        
        for i in range(self.ires):
            for j in range(self.ires):
                self.ibuf = np.zeros((self.ires, self.ires), dtype=int)
                self.change_cell(i, j)
                self.iarr = self.ibuf

    def run(self):
        self.decide_firstcell()
        for i in range(5):
            self.update()
            
        print(self.iarr)

app = App(20)
app.run()

# バッファーに保存してから一気に移す