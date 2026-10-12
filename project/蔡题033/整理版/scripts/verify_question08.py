"""由两个质点的轨道分别计算力、角动量、能量，核验约化质量解。"""
from pathlib import Path
from decimal import Decimal, localcontext
from fractions import Fraction
import json
import math
import random

ROOT=Path(__file__).resolve().parents[1]


def main():
    rng=random.Random(3308)
    errors=[]
    for _ in range(1000):
        m=10**rng.uniform(-3,1);M=m*10**rng.uniform(0,5)
        kappa=10**rng.uniform(-2,2);hbar=10**rng.uniform(-2,2)
        n=rng.randint(1,10)
        mu=m*M/(m+M)
        r=n*n*hbar*hbar/(mu*kappa)
        re=M*r/(m+M);rn=m*r/(m+M)
        # 两物体独立向心方程求共同角速度，随后直接相加。
        force=kappa/r**2
        omega=math.sqrt(force/(m*re))
        assert math.isclose(M*omega**2*rn,force,rel_tol=2e-14)
        J=(m*re**2+M*rn**2)*omega
        kinetic=(m*re**2+M*rn**2)*omega**2/2
        energy=kinetic-kappa/r
        expected=-mu*kappa*kappa/(2*n*n*hbar*hbar)
        errors.extend([abs(J/(n*hbar)-1),abs(energy/expected-1)])
        assert math.isclose(J,n*hbar,rel_tol=2e-14)
        assert math.isclose(energy,expected,rel_tol=2e-14)
        assert math.isclose(re,n*n*hbar*hbar/(m*kappa),rel_tol=2e-14)
    with localcontext() as context:
        context.prec=60
        m=Decimal('0.51');M=Decimal('938')
        muH=m*M/(m+M);muD=m*2*M/(m+2*M)
        independent=(muD-muH)/muH
        formula=m/(2*M+m)
        assert abs(independent-formula)<Decimal('1e-58')
        leading=m/(2*M)
        report=dict(status="pass",two_body_cases=1000,max_relative_error=max(errors),
                    relative_shift_H=str(independent),leading_order=str(leading),
                    leading_absolute_error=str(leading-formula))
    m=Fraction(51,100);M=Fraction(938)
    for eta in range(2,102):
        mu1=m*M/(m+M);mu2=m*eta*M/(m+eta*M)
        assert (mu2-mu1)/mu1==(eta-1)*m/(eta*M+m)
    report["isotope_ratio_exact_cases"]=100
    (ROOT/"build/question08-verification.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__=="__main__":main()
