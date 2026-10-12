# 第017套第4题核验备忘

2026-10-09 02:35，已重新实际读取原卷第3页及手写第4页左栏。手写能量法、半根劲度2k、纵向总劲度4k及60、4、7.5 cm结论正确，保留该路线；补充半根劲度依据、横向几何伸长二阶项乘预拉伸所形成的二次势能、方向投影与小幅条件。原件“初始长度l0”依手写和模型解释为原长，不能把第一次拉伸后长度当作原长。均匀对称、无阻尼及桌面内小幅运动是本题通常使用的理想模型，正式解析明示，不改原始PDF。

统一记原长l0、当前伸长Delta、端点距L=l0+Delta、半跨a=L/2、半根原长b=l0/2；整根劲度k、每半根2k。两半串联，1/k=1/kh+1/kh，kh=2k。中点小球向右x时左长a+x、右长a-x，左力向左、右力向右；Tleft=kDelta+2kx、Tright=kDelta-2kx，净Fx=-4kx。纵向势能k[(Delta/2+x)^2+(Delta/2-x)^2]=kDelta²/2+2kx²，交叉项抵消。因此Tlong=2pi sqrt[m/(4k)]，不因Delta改变。若按只能受拉的细弹簧处理，纵向振幅小于Delta/2以免一侧松弛。

横向中点位移y时，两半长度ell=sqrt[(L/2)^2+y²]，均受拉T=2k(ell-l0/2)，sin(alpha)=y/ell。两水平分量抵消、两个竖向分量同向恢复，Fy=-2T*y/ell=-4ky[1-l0/sqrt(L²+4y²)]。固定Delta>0后在y=0线性化，Ktrans=4kDelta/L，Ttrans=2pi sqrt[mL/(4kDelta)]。无需假设Delta远小于l0。

手写能量保留并逐项补算：Utrans=2*(1/2*2k)*(ell-l0/2)²=k/2*(sqrt[L²+4y²]-l0)²。sqrt=L+2y²/L-2y⁴/L³+O(y6)。最终U=kDelta²/2+2kDelta*y²/L+2kl0*y⁴/L³-4kl0*y⁶/L5+O(y8)。求线性回复力必须保留几何长度中的y²，因为预拉伸Delta与该项交叉后正好产生二次势能；绝非需要先设伸长Delta很小。

周期比n=Ttrans/Tlong=sqrt[L/Delta]=sqrt[1+l0/Delta]，n>1。第一次l0=15Delta1，第二次l0=8Delta2；Delta2-Delta1=.035 m，故l0=.6 m、Delta1=.04 m、Delta2=.075 m。复代L1=.64 m、L2=.675 m，平方比分别16、9，非4、3。一般反求：l0=d(n1²-1)(n2²-1)/(n1²-n2²)、Delta1=d(n2²-1)/(n1²-n2²)、Delta2=d(n1²-1)/(n1²-n2²)，d>0要求n1>n2>1。

真正的小幅条件是A/L小，且三次力对一次力的比2l0*A²/(Delta L²)小。Delta趋零时此条件不均匀，不能固定A后仍套线性周期；Delta=0时U首项为2ky⁴/l0²，Fy首项为-8ky³/l0²，没有非零线性频率。

独立程序scripts/verify_question_04.py从两个锚点至小球的实际长度和空间矢量力计算，不直接代入周期比自证。通过5组差分刚度、5条纵向Newton积分、20条横向Newton积分与独立精确能量周期积分、6组反求参数根、16组势能梯度与矢量力比较、3条零预伸长非线性积分。初步记录build/verification-q04-preliminary.json SHA 205fac5208f37b79e99ada4b807f06f663a0536e3d1007aa3d017b12786e436f，document_complete=false，不把数学预核验计成解答交付。

有限幅周期积分可消除端点表面奇点：令D_A=sqrt[L²+4A²]、D_y=sqrt[L²+4y²]，差势能=2k(A²-y²)(D_A+D_y-2l0)/(D_A+D_y)；再y=A sin(psi)，T=2sqrt(m/k)积分0至pi/2 sqrt[(D_A+D_y)/(D_A+D_y-2l0)] dpsi。小幅Duffing项给T/Tlinear=1-3l0 A²/(4Delta L²)+O(A4)。原题第一次条件取k=.8pi²、m=.05、A=.0064 m，Tlinear=1 s，二阶.998875 s；矢量ODE和精确积分均.9988772799 s。

零预伸长四次势能近似给T=2l0 sqrt(m/k) I/A，I=积分0至1 du/sqrt(1-u4)=1.311028777146293。l0=.6、k=8、m=.05、A=.003时四次势能近似41.458370 s，原几何矢量ODE41.459599 s。该段只讨论横向模式，不声称无预拉伸的两根只能受拉细弹簧仍保持原来纵向双边回复模型。

必要图：原题横/纵两个桌面内方向；均匀半弹簧及预张力；纵向位移的a+x、a-x与自由体力；横向真实三角几何、ell与alpha及两斜向拉力。图放在相应建式前并使用其符号，不加无推导用途的装饰图。以上是编写前备忘，已按下方最新状态完成，不从此重复启动。

2026-10-09 03:00：九模块、12步核心、四带解变式及四幅TikZ完成分题工作核验。学生9/教师15页正文；当前26页全部总览和24个版次高清实际审读，源稿、数学、图、质量报告、PDF/PNG及101模板绑定一致。当前数学记录build/verification-q04.json SHA 0031fcede7a758bf4677f3af31f991780c28d86460a291319f8e845b07e9b7db，视觉记录preview/visual-reviewed-q04.json SHA 4495118558dcf946a3a373721e27bb9866f7e669989d82bcf127bdc4c59f693e。document_complete=true仅指分题，不等于整套；set_accepted=false。下一题第5题，不重做1—4，017尚无完整三版本。
