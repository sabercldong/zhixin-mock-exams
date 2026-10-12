"""Independent constrained-motion ODE for a slowly flipped insulating ring."""
import numpy as np
from scipy.integrate import solve_ivp

def experiment(charge=1.0, duration=200.0, initial_speed=0.7):
    def rhs(t, y):
        theta, w, work = y
        lam = np.pi/2*(1-np.cos(np.pi*t/duration))
        omega = np.pi**2/(2*duration)*np.sin(np.pi*t/duration)
        domega = np.pi**3/(2*duration**2)*np.cos(np.pi*t/duration)
        st,ct,sl,cl=np.sin(theta),np.cos(theta),np.sin(lam),np.cos(lam)
        u=np.array([ct,st*cl,st*sl])
        ut=np.array([-st,ct*cl,ct*sl])
        ul=np.array([0,-st*sl,st*cl])
        utl=np.array([0,-ct*sl,ct*cl])
        ull=np.array([0,-st*cl,-st*sl])
        ddtheta=omega**2*st*ct-charge*omega*sl*st**2
        velocity=ut*w+ul*omega
        acceleration=-u*w*w+ut*ddtheta+2*utl*w*omega+ull*omega**2+ul*domega
        constraint=acceleration-charge*np.cross(velocity,np.array([0,0,-1.0]))
        power=np.dot(constraint,ul*omega)
        return [w,ddtheta,power]
    sol=solve_ivp(rhs,(0,duration),(np.pi/2,-initial_speed,0.0),rtol=2e-10,atol=2e-11,method='DOP853',max_step=.18)
    final_speed=-sol.y[1,-1]
    actual_work=sol.y[2,-1]
    kinetic_change=.5*(final_speed**2-initial_speed**2)
    assert abs(actual_work-kinetic_change)<2e-7
    return dict(q=charge,flip_time=duration,final_signed_speed=final_speed,
                adiabatic_prediction=initial_speed+charge,work=actual_work,
                work_energy_error=abs(actual_work-kinetic_change))

if __name__=='__main__':
    for q in (1.0,-.3,-1.0):
        for t in (160.0,480.0):
            print(experiment(q,t))
