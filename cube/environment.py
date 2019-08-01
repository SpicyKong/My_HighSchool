class cube_env:
    def __init__(self):
        self.cube_state = []
        self.cube_rewqard=[]
        self.cube_dict={}

    def R(self,cube):
        self.cube_save = list(cube)
        cube[1] = self.cube_save[5]
        cube[3] = self.cube_save[7]
        cube[5] = self.cube_save[9]
        cube[7] = self.cube_save[11]
        cube[9] = self.cube_save[13]
        cube[11] = self.cube_save[15]
        cube[13] = self.cube_save[1]
        cube[15] = self.cube_save[3]

        cube[20] = self.cube_save[22]
        cube[21] = self.cube_save[20]
        cube[22] = self.cube_save[23]
        cube[23] = self.cube_save[21]
        return cube
        #print(1)
    def F(self,cube):
        self.cube_save = list(cube)
        cube[2] = self.cube_save[19]
        cube[3] = self.cube_save[17]
        cube[8] = self.cube_save[22]
        cube[9] = self.cube_save[20]
        cube[17] = self.cube_save[8]
        cube[19] = self.cube_save[9]
        cube[20] = self.cube_save[2]
        cube[22] = self.cube_save[3]
        
        cube[4] = self.cube_save[6]
        cube[6] = self.cube_save[7]
        cube[7] = self.cube_save[5]
        cube[5] = self.cube_save[4]
        return cube
        #print(2)
    def U(self,cube):
        self.cube_save = list(cube)
        cube[6] = self.cube_save[18]
        cube[7] = self.cube_save[19]
        cube[18] = self.cube_save[13]
        cube[19] = self.cube_save[12]
        cube[12] = self.cube_save[23]
        cube[13] = self.cube_save[22]
        cube[23] = self.cube_save[7]
        cube[22] = self.cube_save[6]

        cube[8] = self.cube_save[10]
        cube[10] = self.cube_save[11]
        cube[11] = self.cube_save[9]
        cube[9] = self.cube_save[8]
        return cube

    def Rr(self,cube):
        cube = self.R(cube)
        cube = self.R(cube)
        cube = self.R(cube)
        return cube

    def Fr(self,cube):
        cube = self.F(cube)
        cube = self.F(cube)
        cube = self.F(cube)
        return cube

    def Ur(self,cube):
        cube = self.U(cube)
        cube = self.U(cube)
        cube = self.U(cube)
        return cube

    def cleaned_cube_state(self,cube_state):
        cube_state = cube_state.reverse()

        self.cu=[]
        [self.cu.append(a) for a in cube_state if not a in self.cu]
        self.re = [1000-a*0.1 for a in range(len(self.cu)) if 1000-a*0.1 > 0]

        return self.cu,self.re
        #[cu.append(a) for a in cube_state if not a in cu]
        #cu_reward = [1000-a*0.1 for a in range(len(cube_state)) if 1000-a*0.1 > 0]
        #print(cu_reward)

    def save_list(self,list_state, list_reward):# 파일 결과 저장

        with open('cube_state.txt', "a") as file_s:
            file_s.write(str(list_state)[1:-1]+', ')

        with open('cube_reward.txt', "a") as file_r:
            file_r.write(str(list_reward)[1:-1]+', ')
