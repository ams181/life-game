# ---Life Game---

import numpy as np

class App():
    # 0 = dead
    # 1 = live
    
    def __init__(self, ires):
        self.ires = ires
        self.iarr = np.zeros((ires, ires), dtype=int)
        self.ibuf = np.zeros((ires, ires), dtype=int)
        self.irepeat_num = 0
        
    def decide_firstcell(self):
        self.iarr[10][11] = 1
        self.iarr[11][12] = 1
        self.iarr[12][10] = 1
        self.iarr[12][11] = 1
        self.iarr[12][12] = 1
            
    def check_cell(self, ix, iy):
        ilive_count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                inx = ix + i
                iny = iy + j
                
                try:
                    if self.iarr[inx][iny] == 1:
                        ilive_count += 1
                except IndexError:
                    # Ignore out of bounds
                    continue
        return ilive_count
    
    def change_cell(self, ix, iy):
        ilive_count = self.check_cell(ix, iy)
        
        # birth
        if self.iarr[ix][iy] == 0 and ilive_count == 3:
            self.ibuf[ix][iy] = 1
            return 0

        if self.iarr[ix][iy] == 1:
            # survive
            if ilive_count == 2 or ilive_count == 3:
                self.ibuf[ix][iy] = 1
                return 0
            # death
            elif ilive_count <= 1 or ilive_count >= 4:
                self.ibuf[ix][iy] = 0
                return 0
        else:
            self.ibuf[ix][iy] = self.iarr[ix][iy]
            return 0
    
    def update(self):
        
        self.ibuf = np.zeros((self.ires, self.ires), dtype=int)
        
        for i in range(self.ires):
            for j in range(self.ires):
                self.change_cell(i, j)
                
        self.iarr = self.ibuf.copy()

    def run(self):
        self.decide_firstcell()
        for i in range(self.irepeat_num):
            self.update()
            print(self.iarr)

app = App(20)
app.irepeat_num = 10 # repeat
app.run()