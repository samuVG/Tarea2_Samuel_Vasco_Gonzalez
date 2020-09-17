#!/usr/bin/env python
# coding: utf-8

# In[6]:


class VectorCartesiano:
   
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y    #se crean los atributos de las coordenadas
        self.z=z
        self.cartesiano=[x,y,z] #me permite mostrar el vector como un arreglo de python
        self.magnitud=(x**2+y**2+z**2)**0.5 #se crea el atributo magnitud y se calcula en el momento de la instanciacon del objeto.
    
    def __mul__(self, other): #sobrecarga método multiplicación (*) (producto interno)
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def Cruz(self, other): #se crea el método producto cruz
        return VectorCartesiano(self.y*other.z-self.z*other.y, -self.x*other.z+self.z*other.x, self.x*other.y-self.y*other.x)
    
    def __add__(self,other): #Sobrecarga del método suma (+)
        return VectorCartesiano(self.x + other.x, self.y + other.y, self.z + other.z)
           
    def __sub__(self,other): #Sobrecarga del método resta (-)
        return VectorCartesiano(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __getitem__(self,index): #sobrecarga método operador []
        return self.cartesiano[index]
    
    def __eq__(self, other): #sobrecarga método operador ==
        if self.x==other.x and self.y==other.y and self.z==other.z:
            s=True
        else: 
            s=False
        return s
    
    def Transcoord(self): #se trasnforma de los atributos cartesianos x,y,z a los atributos polares r,theta,phi
        import math as m

        #Se usan los condicionales para reescalar de 0 a 2pi la coordenada phi, ya que la tangente inversa
        #arroja valores solo de -pi/2 a pi/2.
        
        if self.x==0:
            if abs(self.y)==self.y:
                u=VectorCartesiano(self.magnitud,m.acos(self.z/self.magnitud),m.pi/2)
            else:
                u=VectorCartesiano(self.magnitud,m.acos(self.z/self.magnitud),-m.pi/2)
    
        elif self.x>0 and self.y>=0:
            u=VectorCartesiano(self.magnitud,m.acos(self.z/self.magnitud),m.tan(self.y/self.x))
        elif self.x>0 and self.y<=0:
            u=VectorCartesiano(self.magnitud,m.acos(self.z/self.magnitud),2*m.pi+m.atan(self.y/self.x))
        elif self.x<0 :
            u=VectorCartesiano(self.magnitud,m.acos(self.z/self.magnitud),m.pi+m.atan(self.y/self.x))
        return u
        


# In[2]:


class VectorPolar(VectorCartesiano):
    
    
    def __init__(self,r,theta,phi):
        import math as m
        
        self.r=abs(r)  #se toman solo valores positivos para r
        self.theta=theta
        self.phi=phi
        
        y=theta          #se reescala el atributo theta
        l=int(y/m.pi)
        angu=y-l*m.pi
        if y==0:
            theta=0
        elif y>0:
            if angu==0:
                theta=m.pi+angu
            else:
                theta=angu
        else:
            theta=m.pi+angu
        
        self.theta=theta
        
        x=phi              #se reescala el atributo phi
        n=int(x/(2*m.pi))
        ang=x-2*n*m.pi
        if x>0:    
            phi=ang
        else:
            phi=2*m.pi+ang
        self.phi=phi
        
        self.polar=[self.r,self.theta,self.phi]
        
        VectorCartesiano.__init__(self, self.r*m.sin(self.theta)*m.cos(self.phi), self.r*m.sin(self.theta)*
                                  m.sin(self.phi), self.r*m.cos(self.theta)) #permite mostrar en un directorio todos los
        #métodos definidos para un VectorCartesiano a partir de un VectorPolar, como motrar su magnitud, el vector en forma
        #de arreglo y a lo que equivale cada atributo, usando el comando x.__dict__
        
        
    def vectorcartesianas(self): #vector en coordenas cartesianas, apartir de los atributos r,theta, phi
        import math as m
        return VectorCartesiano(self.r*m.sin(self.theta)*m.cos(self.phi), self.r*m.sin(self.theta)*m.sin(self.phi), 
                                self.r*m.cos(self.theta))
    
    def vectoresfericas(self):  #vector en coordenadas esféricas, apartir de los atributos r,theta, phi. Este vector 
                                #tiene en su primera entrada la componente radial en la direción e_r, en su segunda 
                                #entrada la componente polar en la dirección e_theta y en su tercera entrada 
                                #la componente asimutal en la dirección e_phi.
        import math as m
        return VectorCartesiano(self.r*m.sin(self.theta)*m.cos(self.phi)*m.sin(self.theta)*m.cos(self.phi)+self.r*
                          m.sin(self.theta)*m.sin(self.phi)*m.sin(self.theta)*m.sin(self.phi)+self.r*m.cos(self.theta)*
                          m.cos(self.theta), self.r*m.sin(self.theta)*m.cos(self.phi)*m.cos(self.theta)*m.cos(self.phi)+
                          self.r*m.sin(self.theta)*m.sin(self.phi)*m.cos(self.theta)*m.sin(self.phi)-self.r*m.cos(self.theta)*
                          m.sin(self.theta), -self.r*m.sin(self.theta)*m.cos(self.phi)*m.sin(self.phi)+self.r*m.sin(self.theta)
                          *m.sin(self.phi)*m.cos(self.phi))
        
#El método magnitud se calcula correctamente, ya que el vector en coordenadas esféricas se transforma con la clase 
#VectorPolar y se transforma en un vector perteneciente a la clase VectorCartesiano, heredando todos los métodos
#allí definidos, incluyendo el método magnitud. Esto es debido a que se "reparó" por medio de la transformación de los  
#atributos a la base de coordenadas esféricas, pudiendo heredar todos los métodos.

