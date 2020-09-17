#!/usr/bin/env python
# coding: utf-8

# In[1]:


import vector as v
import math as m

a=v.VectorCartesiano(1.5,0,2.4)
b=v.VectorCartesiano(0,1,9)
c=v.VectorCartesiano(4.2,0.05,0)


# In[2]:


print("Componentes esféricas del vector a:")
#se convierte los atributos cartesianos x,y,z a los atributos polares r,theta,phi
ap=v.VectorPolar(v.VectorCartesiano.Transcoord(a)[0],v.VectorCartesiano.Transcoord(a)[1],v.VectorCartesiano.Transcoord(a)[2])

#se usa el metodo vectoresfericas de VectorPolar para hallar las componentes esféricas e_r, e_theta, e_phi 
print("Componente en la dirección radial e_r: ",v.VectorPolar.vectoresfericas(ap)[0])
print("Componente en la dirección polar e_theta: ", v.VectorPolar.vectoresfericas(ap)[1])
print("Componente en la dirección asimutal e_phi: ",v.VectorPolar.vectoresfericas(ap)[2])


# In[3]:


print("Componentes esféricas del vector b:")

bp=v.VectorPolar(v.VectorCartesiano.Transcoord(b)[0],v.VectorCartesiano.Transcoord(b)[1],v.VectorCartesiano.Transcoord(b)[2])

print("Componente en la dirección radial e_r: ",v.VectorPolar.vectoresfericas(bp)[0])
print("Componente en la dirección polar e_theta: ", v.VectorPolar.vectoresfericas(bp)[1])
print("Componente en la dirección asimutal e_phi: ",v.VectorPolar.vectoresfericas(bp)[2])


# In[4]:


print("Componentes esféricas del vector c:")

cp=v.VectorPolar(v.VectorCartesiano.Transcoord(c)[0],v.VectorCartesiano.Transcoord(c)[1],v.VectorCartesiano.Transcoord(c)[2])

print("Componente en la dirección radial e_r: ",v.VectorPolar.vectoresfericas(cp)[0])
print("Componente en la dirección polar e_theta: ", v.VectorPolar.vectoresfericas(cp)[1])
print("Componente en la dirección asimutal e_phi: ",v.VectorPolar.vectoresfericas(cp)[2])


# In[5]:


a.b=a*b #se calcula el producto interno con el metodo sobrecargado de la clase VectorCartesiano
print("Producto interno entre a y b: a*b= ", a.b)
a.c=a*c
print("Producto interno entre a y c: a*c= ", a.c)
b.c=b*c
print("Producto interno entre b y c: b*c= ", b.c)


# In[6]:


axb=a.Cruz(b).cartesiano #se calcula el producto cruz con el método .Cruz()
print("Producto cruz entre a y b: axb= ",axb)
axc=a.Cruz(c).cartesiano
print("Producto cruz entre a y c: axc= ",axc)
bxc=b.Cruz(c).cartesiano
print("Producto cruz entre b y c: bxc= ",bxc)


# In[7]:


angulo_ab=m.acos(a.b/(a.magnitud*b.magnitud)) #se calcula el ángulo entre vectores como angulo= arccos (a . b/(|a| |b|)
print("El ángulo entre a y b (en radianes) es: ", angulo_ab)
angulo_ac=m.acos(a.c/(a.magnitud*c.magnitud))
print("El ángulo entre a y c (en radianes) es: ", angulo_ac)
angulo_bc=m.acos(b.c/(b.magnitud*c.magnitud))
print("El ángulo entre b y c (en radianes) es: ", angulo_bc)


# In[ ]:




