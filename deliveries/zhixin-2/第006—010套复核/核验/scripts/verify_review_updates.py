"""本轮新增核查：有限差分、源功路径、表面应力、极小量高精度计算。"""
from pathlib import Path
import json,math
from scipy.integrate import quad
import mpmath as mp
checks=[]
def ck(name,got,want,tol):
 checks.append(dict(name=name,got=float(got),expected=float(want),tolerance=tol,passed=abs(got-want)<=tol))
# 007-05：对固定电荷场能分别改变内、外半径，核查净表面力。
la=2.;eps=3.;a=4.;b=5.;dh=1e-5
energy=lambda x,y:la**2*math.log(y/x)/(4*math.pi*eps)
fa=-(energy(a+dh,b)-energy(a-dh,b))/(2*dh)/(2*math.pi*a)
fb=-(energy(a,b+dh)-energy(a,b-dh))/(2*dh)/(2*math.pi*b)
ck('007-05-场能微分恢复内膜向外应力',fa,la**2/(8*math.pi**2*eps*a*a),1e-11)
ck('007-05-场能微分恢复外膜向内应力',fb,-la**2/(8*math.pi**2*eps*b*b),1e-11)
# 008-03：完整源功一形式的两条路径，只有互感系数相等才无路径差。
L1,L2,M12,M21,I1,I2=2.,3.,.4,.7,1.2,1.8
w1=quad(lambda x:L1*x,0,I1)[0]+quad(lambda y:L2*y+M12*I1,0,I2)[0]
w2=quad(lambda y:L2*y,0,I2)[0]+quad(lambda x:L1*x+M21*I2,0,I1)[0]
ck('008-03-两源路径差揭示互感对称条件',w1-w2,(M12-M21)*I1*I2,1e-12)
# 008-05：有限位置微调核对新增的两个物距灵敏度。
f=10.;distance=lambda t:f*t/(t-f)
for t,slope in [(30.,-.25),(50.,-.0625)]:
 ck(f'008-05-物距灵敏度t={t}',(distance(t+dh)-distance(t-dh))/(2*dh),slope,1e-9)
# 008-08：65位精度比较精确时差及四阶误差。
mp.mp.dps=65
T0=mp.mpf('7.5e9')*mp.mpf('365.25')*86400
E1,E2=mp.mpf('1e5'),mp.mpf('1e8')
e0=mp.sqrt(1/(T0*(1/E1**2-1/E2**2)))
x1,x2=(e0/E1)**2,(e0/E2)**2
stable=lambda x:x/(mp.sqrt(1-x)*(1+mp.sqrt(1-x)))
dt=T0*(stable(x1)-stable(x2));quartic=3*T0*e0**4/8*(1/E1**4-1/E2**4)
ck('008-08-精确时差的高阶增量',dt-mp.mpf('.5'),quartic,1e-34)
ck('008-08-四阶相对贡献',quartic/mp.mpf('.5'),3*e0**2/4*(1/E1**2+1/E2**2),1e-60)
ck('008-08-低高能超额时间之差',T0*stable(x1)-T0*stable(x2),mp.mpf('.5'),1e-17)
# 010-06：波函数积分，检验变分能量和平均高度，非只代入现成公式。
bv=(.75)**(1/3)
psi=lambda z:2*bv**1.5*z*math.exp(-bv*z)
dpsi=lambda z:2*bv**1.5*(1-bv*z)*math.exp(-bv*z)
norm=quad(lambda z:psi(z)**2,0,math.inf)[0]
mean=quad(lambda z:z*psi(z)**2,0,math.inf)[0]
kin=quad(lambda z:dpsi(z)**2,0,math.inf)[0]
ck('010-06-半直线试探态归一化',norm,1.,1e-12)
ck('010-06-平均高度积分',mean,1.5/bv,1e-12)
ck('010-06-变分能量积分',kin+mean,3*(.75)**(2/3),1e-12)
result=dict(all_passed=all(x['passed'] for x in checks),check_count=len(checks),checks=checks,high_precision_digits=65)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
assert result['all_passed'],[x for x in checks if not x['passed']]
print('PASS',len(checks),'本轮新增核查')
