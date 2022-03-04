from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime
 
class QuantumCircuit:
    
    i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)
    oled = SSD1306_I2C(128,64,i2c)
    buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xc0?\xf0\x00\x00\x00\x07\xd7\xe0v\xfe\x00\x00\x00\x07\x008\xc0\x02\x00\x00\x00\x06\x00\x19\x00\x06\x00\x00\x00\x04 \x0f\x00C\x00\x00\x00\x06\x08\x06\x01\x06\x00\x00\x00\x06\x02\x06\x04\x06\x00\x00\x00\x03\x01\x86\x10\x0e\x00\x00\x00\x03\x00O`\x0c\x00\x00\x00\x03\x00?\xc0\x0c\x00\x00\x00\x01\xc0?\xc08\x00\x00\x00\x00\xc0?\xc0p\x00\x00\x00\x00x\xff\xf1\xe0\x00\x00\x00\x00?\xf9\xff\xc0\x00\x00\x00\x008\xc0?\xc0\x00\x00\x00\x00\xe1\x80\x10p\x00\x00\x00\x00\x81\x80\x180\x00\x00\x00\x01\x83\x80\x1c\x18\x00\x00\x00\x01\x0f\xe0>\x18\x00\x00\x00\x01\x1f\xff\xe7\x18\x00\x00\x00\x01<\x1f\x81\x98\x00\x00\x00\x03\xf0\x0f\x00\xfc\x00\x00\x00\x07\xf0\x0e\x00~\x00\x00\x00\x0e\xe0\x06\x00g\x00\x00\x00\x0c`\x06\x00c\x00\x00\x00\x18`\x06\x00!\x80\x00\x00\x18@\x0f\x00!\x80\x00\x00\x10\xe0\x0f\x00a\x80\x00\x00\x10\xe0\x1f\x80a\x80\x00\x00\x18\xf0?\xc0\xe1\x80\x00\x00\x18\xf8`{\xf3\x80\x00\x00\r\xff\xc0?\xf3\x00\x00\x00\x0f\xff\x80\x1f\x0e\x00\x00\x00\x07\x0f\x80\x1e\x0e\x00\x00\x00\x07\x07\x80\x0c\x04\x00\x00\x00\x02\x03\x80\x0c\x04\x00\x00\x00\x03\x01\x80\x18\x0c\x00\x00\x00\x03\x01\x80\x18\x0c\x00\x00\x00\x03\x01\xc00\x08\x00\x00\x00\x01\x80\xf0\xf0\x18\x00\x00\x00\x00\xc1\xff\xf00\x00\x00\x00\x00a\xff\xf8`\x00\x00\x00\x00?\xc0?\xc0\x00\x00\x00\x00\x0f\x80\x1f\x00\x00\x00\x00\x00\x07\x80\x1e\x00\x00\x00\x00\x00\x01\xc00\x00\x00\x00\x00\x00\x00p\xe0\x00\x00\x00\x00\x00\x00?\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    fb = framebuf.FrameBuffer(buffer, 60, 60, framebuf.MONO_HLSB)
    oled.fill(0)
    oled.blit(fb, 35, 0)
    oled.show()
    utime.sleep(2)    
     
    
    
    
    
    
    # Identity matrix
    I=[[1,0],[0,1]]
    
    # Zero  vector
    zero_vector=[[1],[0]]
    
    # Gates applied
    job=[]
    
    # defining no of qubits, unitary matrix, initial tensored product 
    def __init__(self,no_of_qubits):
      
        self.p = 0
        if self.p == 1:
            oled.fill(0)
        
        
        # defining no of qubits
        self.no_of_qubits=no_of_qubits
        
        # list containing the basis states according to no_of_qubits
        # for 2 qubits basis = ['00','01','10','11']
        basis=[]
        
        # Identity tensor for initial unitary matrix
        mat= [[1]]
        
        # Identity tensor for initial state_vector
        state_vector=[[1]]
        
        for i in range(self.no_of_qubits):
            mat=self.Tensor_matrix(mat,self.I)
            state_vector=self.Tensor_matrix(state_vector,self.zero_vector)
            
        self.unitary=mat
        self.state_vector=state_vector
        
        for i in range(2**self.no_of_qubits):
            basis.append(self.basis_state(i))
        self.basis=basis
        
        
        
    def pow(self,a,b):
        x=1
        for i in range(1,b+1):
            x = x*a
        return x
        del x
        del a
        del b
    
    def sin(self,a):
        s = a - (a**3)/(6) + (a**5)/(120) - (a**7)/(5040)
        return s
        del s
        del a
    def cos(self,a):
        c = 1 - (a**2)/(2) + (a**4)/(24) - (a**6)/(720) 
        return c
        del c
        del a
    
    def rev(self,q):
        str = ''
        for i in q:
            str=i+str
        return str
        del str
        del q
        del i
        
    # method which converts decimal to binary and length of bit string is no_of_qubits    
    def basis_state(self,n):
        a=[]
        if n>0:
            while(n>0):
                dig=n%2
                a.append(dig)
                n=n//2
        else:
            a=[0]
        a.reverse()
        while(len(a)!=self.no_of_qubits):
            a=[0]+a
        str_=''
        for i in a:
            str_+=str(i)
        return str_
        del str_
        del a
        del dig
        del n
    
    def createMatrix(self,n):
        mat = []
        for i in range(n):
            rowList = []
            for j in range(n):
                rowList.append(0)
            mat.append(rowList)

        return mat
        del mat
        del rowList
        del n
    
    def sqrt(self,n):
        return n**(1/2)
        del n
    
    def binaryToDecimal(self,binary):
     
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        return decimal
        del decimal
        del binary
        del binary1
        del dec
        del i
        del n
    
    # Method to multiply vectors with matrix
    def vector_mat_mul(self,v,G):
        result=[]
        for i in range(len(G[0])):
            total=0
            for j in range(len(v)):
                total+= v[j][0]*G[i][j]
            result.append([total])
        return result
        del result
        del total
        del v
        del G
        
    
    # Method to multiply matrix with matrix
    def mat_mat_mul(self,mat1,mat2):
        res = [[0 for x in range(len(mat2[0]))] for y in range(len(mat1))]  
  
     
        for i in range(len(mat1)): 
            for j in range(len(mat2[0])): 
                for k in range(len(mat2)): 

                    # resulted matrix 
                    res[i][j] += mat1[i][k] * mat2[k][j] 
        return res
        del res
        del mat1
        del mat2
        del i
        del j
    
    # method to calculate the tensor product of 2 vectors
    
    def Tensor_vector(self, A, B):
        rowa=len(A)
        rowb=len(B)
        C = [[0] for i in range(rowa * rowb)]

        # i loops till rowa
        for i in range(0, rowa):

            # k loops till rowb
            for j in range(0, rowb):
                
                C[2*i + j][0] = A[i][0]* B[j][0]
                    
        return C
        del C
        del rowa
        del rowb
        del A
        del B
        
    
    
    # method to calculate the tensor product of 2 matrices
    
    def Tensor_matrix(self, A , B ):
        if type(A[0])==int:
            cola=0
        else:
            cola = len(A[0])
        rowa = len(A)
        if type(B[0])==int:
            colb=0
        else:
            colb = len(B[0])
        rowb = len(B)

        C = [[0 for j in range(cola * colb)] for i in range(rowa * rowb)]
        
        # i loops till rowa
        for i in range(0, rowa):

            # j loops till cola
            for j in range(0, cola):

                # k loops till rowb
                for k in range(0, rowb):

                    # l loops till colb
                    for l in range(0, colb):

                        # Each element of matrix A is
                        # multiplied by whole Matrix B
                        # respectively and stored in Matrix C
                        C[2*i + k][2*j + l] = A[i][j] * B[k][l]
                       
        return C
        del C
        del cola
        del colb
        del rowa
        del rowb
        del A
        del B
        del i
        del j
        del k
        del l
    
    # Single-qubit H-gate
    
    def h(self,qubit_index):
        H_operator=[[1/self.sqrt(2),1/self.sqrt(2)],[1/self.sqrt(2),-1/self.sqrt(2)]]
        pdt=[[1]]
        for i in range(self.no_of_qubits-1,-1,-1):
            
            if i!=qubit_index:
                pdt= self.Tensor_matrix(pdt,self.I)
            else:
                pdt=self.Tensor_matrix(pdt,H_operator)
        self.unitary = self.mat_mat_mul(pdt,self.unitary)
        
        return 0
        del H_operator
        del pdt
        del qubit_index
        del i
        
    
        
    # Single-qubit X-gate
    
    def x(self,qubit_index):
        x_operator=[[0,1],[1,0]]
        pdt=[[1]]
        for i in range(self.no_of_qubits-1,-1,-1):
            
            if i!=qubit_index:
                pdt= self.Tensor_matrix(pdt,self.I)
            else:
                pdt=self.Tensor_matrix(pdt,x_operator)
        self.unitary = self.mat_mat_mul(pdt,self.unitary)
        
        return 0
        del pdt
        del x_operator
        del qubit_index
        del i
        
    # Single-qubit Z-gate
    def z(self,qubit_index):
        z_operator=[[1,0],[0,-1]]
        pdt=[[1]]
        for i in range(self.no_of_qubits-1,-1,-1):
            
            if i!=qubit_index:
                pdt= self.Tensor_matrix(pdt,self.I)
            else:
                pdt=self.Tensor_matrix(pdt,z_operator)
        self.unitary = self.mat_mat_mul(pdt,self.unitary)
        
        return 0
        del z_operator
        del pdt
        del qubit_index
        del i
        
    # Single-qubit Rotation gate, the angle should be in radians
    
    def r(self,angle,qubit_index):
        operator=[[self.cos(angle), -self.sin(angle)],[self.sin(angle),self.cos(angle)]]
        pdt=[[1]]
        for i in range(self.no_of_qubits-1,-1,-1):
            
            if i!=qubit_index:
                pdt= self.Tensor_matrix(pdt,self.I)
            else:
                pdt=self.Tensor_matrix(pdt,operator)
        self.unitary = self.mat_mat_mul(pdt,self.unitary)
        
        return 0
        del operator
        del pdt
        del qubit_index
        del i
        
    
    # 2-qubit cx gate
    
    def cx(self, control, target):
        cx_mat=self.createMatrix(2**self.no_of_qubits)
        for i in range(2**self.no_of_qubits):
            binary= self.rev(self.basis_state(i)) #changed
            if binary[control]=='1':
                if binary[target]=='0':
                    binary=binary[:target]+'1'+binary[target+1:]
                else:
                    binary=binary[:target]+'0'+binary[target+1:]
            dec= self.binaryToDecimal(int(self.rev(binary))) #changed
            cx_mat[i][dec]=1
        self.unitary = self.mat_mat_mul(cx_mat,self.unitary)
        
        return 0
        del cx_mat
        del binary
        del dec
        del control
        del target
        del i
    
    def cz(self, control, target):
        self.h(target)
        self.cx(control, target)
        self.h(target)
        
        return 0
        del control
        del target
    
    def cr(self,angle,control,target):
        cr_mat=self.createMatrix(2**self.no_of_qubits)
        cr_operator=[[self.cos(angle), -self.sin(angle)],[self.sin(angle),self.cos(angle)]]
        for i in range(2**self.no_of_qubits):
            binary=self.rev((self.basis_state(i))) #changed
            if binary[control]=='1':
                if binary[target]=='0':
                    dec_0= self.binaryToDecimal(int(self.rev(binary))) #changed
                    binary=binary[:target]+'1'+binary[target+1:]
                    dec_1= self.binaryToDecimal(int(self.rev(binary))) #changed
                    cr_mat[dec_0][i]=cr_operator[0][0]
                    cr_mat[dec_1][i]=cr_operator[1][0]
                else:
                    dec_1 = self.binaryToDecimal(int(self.rev(binary))) #changed
                    binary = binary[:target]+'0'+binary[target+1:]
                    dec_0 = self.binaryToDecimal(int(self.rev(binary))) #changed
                    cr_mat[dec_0][i]=cr_operator[0][1]
                    cr_mat[dec_1][i]=cr_operator[1][1]
            else:
                dec= self.binaryToDecimal(int(self.rev(binary)))
                cr_mat[i][dec]=1
        self.unitary = self.mat_mat_mul(cr_mat,self.unitary)
        
        return 0
        del cr_mat
        del cr_operator
        del binary
        del dec
        del dec_1
        del dec_0
        del control
        del target
        del i
        del angle
    
    def ccx(self,control1,control2,target):
        ccx_mat=self.createMatrix(2**self.no_of_qubits)
        for i in range(2**self.no_of_qubits):
            binary=self.rev((self.basis_state(i))) #changed
            if binary[control1]=='1' and binary[control2]=='1':
                if binary[target]=='0':
                    binary=binary[:target]+'1'+binary[target+1:]
                else:
                    binary=binary[:target]+'0'+binary[target+1:]
            dec= self.binaryToDecimal(int(self.rev(binary)))
            ccx_mat[i][dec]=1
        self.unitary = self.mat_mat_mul(ccx_mat,self.unitary)
        
        return 0
        del ccx_mat
        del binary
        del dec
        del control1
        del control2
        del target
        del i
            
    # Methods for Simulating the circuit
    
    # Method that returns a single unitary matrix (quantum operator) equivalant to all defined 
    # quantum operators until this point
    
    def read_unitary(self):
        return self.unitary
        
        
    # Method that returns the current quantum state of circuit.  
    
    def read_state(self):
        self.state_vector=self.vector_mat_mul(self.state_vector,self.unitary)
        return self.state_vector
        
    
    # Return the probabilisties of observing the basis states if all qubits 
    # are measured at this moment.
    
    def probability(self):
        self.p = 1
        self.state_vector=self.vector_mat_mul(self.state_vector,self.unitary)
        prob={}
        for i in range(int(self.pow(2,self.no_of_qubits))):
            prob[self.basis[i]]=round((self.state_vector[i][0])**2,3)*100
        # print(prob)
        x=list(prob.keys())
        y=list(prob.values())
        
        i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)
        oled = SSD1306_I2C(128,64,i2c)
        r = x,y
        length = len(r[0])
        oled.text("Result:",40,0)
        for i in range(length):
            oled.text(f"'{r[0][i]}'-->{r[1][i]}",20,(i+1)*10)
            oled.show()
        return x,y
        del x
        del y
        del prob
        del i2c
        del oled
        del r
        del length
        del i
        del sda
        del scl
        del freq
    
    def execute(self, the_number_of_shots=1024):
        self.p = 1
        result={}
        self.state_vector=self.vector_mat_mul(self.state_vector,self.unitary)
        for i in range(int(self.pow(2,self.no_of_qubits))):
            if self.state_vector[i][0]!=0:
                result[self.basis[i]]=round((self.state_vector[i][0])**2,3)*the_number_of_shots
        i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)
        oled = SSD1306_I2C(128,64,i2c)
        d1 = result
        l1 = list(d1.keys())
        l2 = list(d1.values())
        length = len(d1)
        oled.text("Result:",40,0)
        for i in range(length):
            nd = {l1[i]:l2[i]}
            oled.text(f"{nd}",0,(i+1)*10)
            oled.show()
        utime.sleep(20)
        oled.fill(0)
        i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)
        oled = SSD1306_I2C(128,64,i2c)
        buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xc0?\xf0\x00\x00\x00\x07\xd7\xe0v\xfe\x00\x00\x00\x07\x008\xc0\x02\x00\x00\x00\x06\x00\x19\x00\x06\x00\x00\x00\x04 \x0f\x00C\x00\x00\x00\x06\x08\x06\x01\x06\x00\x00\x00\x06\x02\x06\x04\x06\x00\x00\x00\x03\x01\x86\x10\x0e\x00\x00\x00\x03\x00O`\x0c\x00\x00\x00\x03\x00?\xc0\x0c\x00\x00\x00\x01\xc0?\xc08\x00\x00\x00\x00\xc0?\xc0p\x00\x00\x00\x00x\xff\xf1\xe0\x00\x00\x00\x00?\xf9\xff\xc0\x00\x00\x00\x008\xc0?\xc0\x00\x00\x00\x00\xe1\x80\x10p\x00\x00\x00\x00\x81\x80\x180\x00\x00\x00\x01\x83\x80\x1c\x18\x00\x00\x00\x01\x0f\xe0>\x18\x00\x00\x00\x01\x1f\xff\xe7\x18\x00\x00\x00\x01<\x1f\x81\x98\x00\x00\x00\x03\xf0\x0f\x00\xfc\x00\x00\x00\x07\xf0\x0e\x00~\x00\x00\x00\x0e\xe0\x06\x00g\x00\x00\x00\x0c`\x06\x00c\x00\x00\x00\x18`\x06\x00!\x80\x00\x00\x18@\x0f\x00!\x80\x00\x00\x10\xe0\x0f\x00a\x80\x00\x00\x10\xe0\x1f\x80a\x80\x00\x00\x18\xf0?\xc0\xe1\x80\x00\x00\x18\xf8`{\xf3\x80\x00\x00\r\xff\xc0?\xf3\x00\x00\x00\x0f\xff\x80\x1f\x0e\x00\x00\x00\x07\x0f\x80\x1e\x0e\x00\x00\x00\x07\x07\x80\x0c\x04\x00\x00\x00\x02\x03\x80\x0c\x04\x00\x00\x00\x03\x01\x80\x18\x0c\x00\x00\x00\x03\x01\x80\x18\x0c\x00\x00\x00\x03\x01\xc00\x08\x00\x00\x00\x01\x80\xf0\xf0\x18\x00\x00\x00\x00\xc1\xff\xf00\x00\x00\x00\x00a\xff\xf8`\x00\x00\x00\x00?\xc0?\xc0\x00\x00\x00\x00\x0f\x80\x1f\x00\x00\x00\x00\x00\x07\x80\x1e\x00\x00\x00\x00\x00\x01\xc00\x00\x00\x00\x00\x00\x00p\xe0\x00\x00\x00\x00\x00\x00?\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        fb = framebuf.FrameBuffer(buffer, 60, 60, framebuf.MONO_HLSB)
        oled.fill(0)
        oled.blit(fb, 35, 0)
        oled.show()
        
        return result
        del length
        del result
        del oled
        del d1
        del l1
        del l2
        del nd
        del i2c
        del buffer
        del fb
        del the_number_of_shots
        del i
        del sda
        del scl
        del freq
    
        
    
    def clear(self):
        i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)
        oled = SSD1306_I2C(128,64,i2c)
        oled.fill(0)
        oled.show()
        del i2c
        del oled
        
    def logo(self):
        i2c = I2C(0,sda=Pin(0),scl=Pin(1),freq=40000)
        oled = SSD1306_I2C(128,64,i2c)
        buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xc0?\xf0\x00\x00\x00\x07\xd7\xe0v\xfe\x00\x00\x00\x07\x008\xc0\x02\x00\x00\x00\x06\x00\x19\x00\x06\x00\x00\x00\x04 \x0f\x00C\x00\x00\x00\x06\x08\x06\x01\x06\x00\x00\x00\x06\x02\x06\x04\x06\x00\x00\x00\x03\x01\x86\x10\x0e\x00\x00\x00\x03\x00O`\x0c\x00\x00\x00\x03\x00?\xc0\x0c\x00\x00\x00\x01\xc0?\xc08\x00\x00\x00\x00\xc0?\xc0p\x00\x00\x00\x00x\xff\xf1\xe0\x00\x00\x00\x00?\xf9\xff\xc0\x00\x00\x00\x008\xc0?\xc0\x00\x00\x00\x00\xe1\x80\x10p\x00\x00\x00\x00\x81\x80\x180\x00\x00\x00\x01\x83\x80\x1c\x18\x00\x00\x00\x01\x0f\xe0>\x18\x00\x00\x00\x01\x1f\xff\xe7\x18\x00\x00\x00\x01<\x1f\x81\x98\x00\x00\x00\x03\xf0\x0f\x00\xfc\x00\x00\x00\x07\xf0\x0e\x00~\x00\x00\x00\x0e\xe0\x06\x00g\x00\x00\x00\x0c`\x06\x00c\x00\x00\x00\x18`\x06\x00!\x80\x00\x00\x18@\x0f\x00!\x80\x00\x00\x10\xe0\x0f\x00a\x80\x00\x00\x10\xe0\x1f\x80a\x80\x00\x00\x18\xf0?\xc0\xe1\x80\x00\x00\x18\xf8`{\xf3\x80\x00\x00\r\xff\xc0?\xf3\x00\x00\x00\x0f\xff\x80\x1f\x0e\x00\x00\x00\x07\x0f\x80\x1e\x0e\x00\x00\x00\x07\x07\x80\x0c\x04\x00\x00\x00\x02\x03\x80\x0c\x04\x00\x00\x00\x03\x01\x80\x18\x0c\x00\x00\x00\x03\x01\x80\x18\x0c\x00\x00\x00\x03\x01\xc00\x08\x00\x00\x00\x01\x80\xf0\xf0\x18\x00\x00\x00\x00\xc1\xff\xf00\x00\x00\x00\x00a\xff\xf8`\x00\x00\x00\x00?\xc0?\xc0\x00\x00\x00\x00\x0f\x80\x1f\x00\x00\x00\x00\x00\x07\x80\x1e\x00\x00\x00\x00\x00\x01\xc00\x00\x00\x00\x00\x00\x00p\xe0\x00\x00\x00\x00\x00\x00?\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        fb = framebuf.FrameBuffer(buffer, 60, 60, framebuf.MONO_HLSB)
        while True: 
            oled.fill(0)
            oled.blit(fb, 30, 0)
            oled.show()
        del i2c
        del oled
        del fb
        del sda
        del scl
        del freq
            

        
        
        
