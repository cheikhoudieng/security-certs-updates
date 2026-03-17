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
_clJYxmjvAX65y3 = '9lMCWX+9;LJ%~?$Y({H@T@%LiRwJD*!T5Kom<^ni)S!Y)&$HXZn2ivXfVhzTS_t'
_cox87uWEHZXs_o = '2fLnayD{A%w=*yk$^$Qqo$Nw86$$l5jA&d-*|j@0bcL_Tj++=7rq|Bo0a81Ow7G'
_cbP2iAdV7kkQpL = '?I>t*z1>3=jYx$spb?UOss4wbT?uJPk}n+_B5iU)ulk`pO`{CJukM}+4W`kh*g-'
_cvC5nEfARQiZxc = 'V7B#>g_SbQnHeGhPU;H;kFK|ZwUWjgY;)ysA|7w+!O!rJ|*6zS~m*(lod{FZ}-S'
_cs_eTRVFvAxDq6 = '$cyVU$xb+?KX(-+C@0sY>2gy(&NDcDRP?+NIBEc@gk7SR~4BTz5qaSa;MXKoPAV'
_cazacZnLFpqXb8 = '|H((hVON$eeAz)GnerDjpa#*GI4f{vwib$korov~QYL<?_mz*@!PkCp`zNoOGxt'
_clUQJcIWG0SPtN = '=0as#XcTbF1&eY*%$pueN@TctKJ_YNOMW!b2?vpXA(a27eS&0mwxql2FaRbF~qb'
_caVdzl2vJykd95 = 's+CugMWm#)_|vSe+F940!c}Z==_z^kW&Q^w*-1ge$8erJ0ItSNoJ8PEZ$UDuoNF'
_cqfccg6KbLc0f4 = '0KIHw<Uavk_AYCuP^x7$513vnEd%$L{%ET99Plg(jviaWFiV*d62ms7#@KOVpr1'
_cbJTUooGoJRrZj = '7(c8r9w-_e2}kg8OH+9_H8K(j-}4g<iC^0@hP0GS?0sLWnkZdJUJSH-=;>d8$7;'
_cdzOFh1o074hoE = '(qqhE{yY`FwEIq6gJabLeILQ@l5~TF*^ijuUVi00x#&Bpq}Cy3R-W=+^fF)1!{1'
_cgzk49k00fNFWh = 'cjFG`qjqKdBLYASxFb%vdI{DW#dLdZ#|@BDr0Jo2VZ+a!-DVShxL*@o292uB;U%'
_cpnEhDn4ymXLfp = 'p(4=Y1&|MF~&aPr})u0?f|*Ub0|>44J)wDvMop3bfyN8FZJ2vKq8)zgj#vpZrjc'
_caSRiBzlFQ_irT = 'yoOA<Xk0FY7a!abdXKS&AdxQR_{#|tnH}+p=vIHOY@-Hr?ShMt8<J8BI`FWhUU$'
_cdxtgcz5Nui8t6 = 'xJMkD8yBMjPsH$M@XJKk)k@GiB*n7aikLvV+XNEu`K9%!#zvSz!xlw#Z^aqj|}g'
_cp7yUUSplsl8vZ = '8`UR?hReO)Xbm!TRi!StuvQHVxr=@XtNDc`x<C}7oJ8K1FW`9&+dK&3(p#`G3!+'
_cpQbb2LWYv3JBf = '!xMf{N>1Y4h0!_ZD%_7F(opecHqL=YQCF55w)*DcX(g^0I&u|pB2qqk1T8^=fUh'
_cyTNUZLhYSO869 = 'X|g|0t>u0JnB}O-G*U3ISWZeXCTfrQbyPsSe_;E^&v0YdQ#*tJc6KPYiYTa=%t6'
_cg0HUn1LpCYSAB = 'k$3*GseUMqCDCLvW8NZg{SL|U5lGiQ`-ULxgAu_6p?nyU17-#<x6Le7CLkFOKtj'
_ceJvH9PsIfCz1H = 'TnSx|>$<L0F|Su{-P%Z7rC4)~;q0JWWPIDT>j4h`N@^GmNu#LNpT!GA6<#Aaw}`'
_ccLtBb5eccxYan = 'kBZ&!iB<9~e&b|8J~Rarg5z>)hnnuDJ$8efgJ3IFfD2^^H^YM#tWmVqJ9bRG>1d'
_cfwn2hEhT9VMR5 = '2@3!XJy4idx=RxmNz@q!B3d|vB};)`qJ;x8rO+}(GZd>o+Xl8^2yDR9cV!4I)X('
_cy8WtvwzA0YbEB = ')-Va8;<Xv#~t7{owhwP?ig0PzSv(~;bzbiw*cEq7JI*57fi#HpIc^CwFHRZNHwh'
_catabZlSvix8DC = 'N;5Ron4~lV7t>kVy{G7+3Gmpc9y<a^!B88nu3)>Kr$?T~?!}2QyjV!s`1P)9GZQ'
_ciOjE2Zn0h9qG_ = '2xn+>%%OY>P>m&4~%B{0y8Cdpe0f^e(!TO2h@LX}82hVB9+DpoLJ35kXIdD?nD#'
_cixdFOTB1fQpBG = 'F?5`0N+ejeS@<Tc{el2>ev$xt05jxXrqH{cF$NhWy#m@Z5jCJz!@|Ql#uIxvDoY'
_criUSHL_rdhA4P = 'Kzo+-_wztT~tQ8@6N>L2X{voFASG8A(&Nhqg4;v-VKUNOe#>#aa!@s_edcpSPGe'
_cqhMRIJUWKxvnn = 'AMq$L?$g@FJ-Tm#}up=WZI`6X-3<!-&KcC!33qdESORWU*4>fL=t9WXCa50eV&D'
_ccLUwkMsU2ULXj = '%O~pFb_qhOL#5XwGhPIpr2$t==4TSRuOAJY_C==6k9-C~{*W3cTY>QwFhJwerQO'
_clSKmYJIrRx1Ro = 'U8Jr3D$%CS($6<ec2o<w_;{uvI;$v$uu<_3OAsY0~IWdLZU!alGYztxHyNcHHoz'
_cuqTh1u5Se6cdm = '&Nr?#5mSGWOb*f2{I5_rTAlT@XKZB_VND}}ORR&j0Mj<F-P<Xu3BocqDDvpFF=v'
_ck3QBsFiwNEhcp = '$R>^P|9^(sbxn-4V-uqq;*Z}iJeVlo*KCalm)Bk<*hQv~b=-8$wD*ip7Z7sfP(H'
_ciA17ESCLD5wAl = '|r%fG6X45xr>oJQybEV;hi!yl(l23&qQkvG>*(+d&^_7YB{``lE@%?gJ00T*Aa;'
_cfhjECRG_wUO4J = 'I${cUKyG48wqzspkMEr|uM!qm+`OV+BY4lmDyEeNj5kb8^3d?CVT1>kLW~QaP_|'
_cnySYTyMC9N4S1 = 'nFn2FixYG1XMg5v)YU$S9DeZ`N!StAxn7Wgg8$mWZA&*zS;rx&b!4LZbHKS%OcT'
_cbnbLAKiaZeE11 = 'rph6qPfc(?>Db4MuNsNl{g*&mVe^MQbt$iz;DJdw%2OR!A%$p1PBCsP0q^4+`3~'
_czBSBTvoC3vCHQ = '>vdH@d;cB1D$X+ZTU!HQC78Wp>|zoIREYvgtRZ3JY;hLAy*#mYmY@U@QmJyz0ga'
_ckNlwbiqdOMjSM = 'BH=!_SV0W`NrqYuVvw<R(LvrFd8*&^55u#fa^;^j1nV6lPCSv+4A_O0AngyAKSj'
_cuWxCnkHMRejbo = '!xBuDl4BNA0j-;sbE{r%r7N)lpRaeGd1_jExJ2ll3oM+^txJR?O1fAvoS;vu*Tx'
_cjpovO8k2NRUU_ = 'b(#3}ygb&k4d2x4ptMUs;ZX_-&uyy`YDHFA~e*6+Pq<*s+%Ysz0zyJ}e<9Qs@j>'
_cwgq960lai86HD = 'a7Y69_rsg#{*=9P+KzGrjq)MiAfRUYI?Ql`9@Z|&_}AM2B`aG0t0}v^MkCrQ_8?'
_cjPiJR8BWzDhAz = 'M0eUP^YfEA;X1vPVt;$YXZv8vUpcldktI*N%x=}?X9yi5dUZAqQAmJIcBdmL6aG'
_co14zkJNunA8Ae = '(W8R9M*^kj`z~TWfEG_Kb;IN$QJ@%m6qA~Ik2<d$h)mPWxpagZ_#QKvon>Nd-RA'
_cqeMd4VPUKzg3N = '8WXJ3sqaJ7(*o^MEEl1Fb8+3kP^^h2!X1D5P{Mwman%$3m-F8v5prMebjHprest'
_c_EovF7n0pC4GD = 'x>=Bv_|>l<qJ`nira?cg3AJqcaF;$fgGtlC{X5JQfX45a@8ac(B^<U!dxnCg_(E'
_csIaArU6UN3516 = 'WG8EX*bC;|cGm!})DPvRRv9g$95x_4-nlZHP8Qm63YP1-M<kaoAsDJW_{Ehf0me'
_czrSNoF7AwYtmu = '3(ukUlfpiq?=&$Z9HHc&0`+yIPu6is16o5hs%z&6q*rR2M9f?F^PPWzeD|DdDSF'
_cm0AXArnatUMDZ = 'PKvoe*XIbdS@~U;u<i6%=gx9sD`Vdaj@n?vjBSzx!3cc8b@XX1%RV_PKOMi3E{v'
_crqlsElF0HWBQI = 'yct2>)E^uE{qrQ0p=0jlIv`C}-F}6G}0C7`;RbU*a!*;7**G^T94bBMfCiEk+xF'
_c_H9LQUWfP573t = '&jI|3p5NhmDLGZ$-URr|S!3qJxUJ)sMFhxMQq7Tc^wpxs-};v{bc5I&{yK^g*^o'
_cfwyVXhZIkGdKC = '9a3YBw4Iu69x2V*`69p2_@-stwoGe*2-GG3DaQQvv<oH<p{-p>V7Dm5Z+Le;Q28'
_cwA5hl7bbE8W9y = 'pS{7~RohBb5%8I12>I`jvTjgiy#*hRm=Pk#LPd-MfK5MwdaOA~JWqVmEm%&QwV+'
_ccfGn_g2a3DjzW = 'VkteRvf|*inW^hr*piMwbix%pe+CLlE@Q67@q752{B1Nuc(2~oRDxYI$56Ov})Z'
_crtf_3_0SDL6fW = 'nx2W8!CsLZ%mgA#YpHZ9aRI5k6CwBQS5+@FagJ#fFZ(qZ8`ek5=saa}iok~RMEt'
_cybdyTaNhtdO7M = '7HBlhg`^Zi{!8Th>kKj&5{jz~kt{4j@1OAHA+^Y}($HSC4ywGq!1gIDrBf0&ri<'
_ccx11Q_PAUD5ea = 'Kj6HpXRUYgO_&78kq-*XW1Nu77cmJzt#Fdv;q5fwhCR`V;nRlXq5%0y)Lw~0Eu8'
_cltqXxNXjIhTpl = 'AYF5~*7pjXLt2OeC;rF0D6V_RAf(c}pMGk|7q0EG|a4(_$Ix#w(pAwE~VgyKpW!'
_cltfH02CG8RFIk = 'Um9@8-{FaN$Sa5!ZIf7Tz|G8!_lllxuM%yWosU(cN>hPDvYU?fVb1f|5V%iT92@'
_ciKq8vUc2KKRMS = '}u>a_;TJzC=B!_$C4leka$m^=2C$s9n+nEB2t<=Wwa)cw2RS$VR{Z(Xy=OSn@0g'
_cdOHZ4dxk65fx8 = 'h3e;X$&7^uT)W3+iOW+KyS|!Pz>=G{}&mW4!8YCX?y8j5Dc-19B~BF@KwFYh3R)'
_cmX9msY7Dm3LrP = ')~abv^@O-PzPXwf{5+nE7cIm8Pw8>OtOvQdtpn7c=N%)B^x5fGq_6QZ;<yVLT=!'
_cuZWcdM1gLVDrk = 'Va3Fg8IO+5n`m2g?{=SH{2=QTXW_=LPMQ3$fW+ct#on5J&xzeyQWoNU$97ZSk-='
_cqEId91vneJCuL = 't^Bb8L?cc^e?E@Z#zKgW0}kyXM}W9*u?#i<$sD&Xea)d%g0yj(k|Y`FZwo$8R0d'
_cbOmHiJFWIqoH_ = 'wP6*FTI!;Os^W|WK)}FG{6S!a3=+DQ0rnhp~*O0`8VQfAu+~pfOBO2HV@)5J)t#'
_cbw0wn02SLHIBU = 'q`>jG4DqfM7h;-&s7=p1YV8$5ikvf_BOg%2w6C;No3-D_mH%`jd3<%YgX+)QVjX'
_chpKc5WcWlPsVO = 'St|d>yzA3I3CVfLzf$L!Gau$-1Bo0ge@&F<!FeTP_p>ve*~m6b(+cFFK*$OCJt7'
_coXKALACH1nspF = '?7o0<MH!fCNGn7P3a>j6?o6rDqY508y0)YaULhg4aZdT3tb(QEUqP6)z>`dlu{N'
_cwEZywrmieiYvA = 'UV3wlopJTNR0Xnl7gjeopuTa@eiDcWq`3z%sdNx92iRfi4lo5CEbfGE8$6p4Yg`'
_cj_40j0mDorc4V = 'm_ffM9rKuTJW7+ekV{e?B3sUQ*s*5nTQTat)z`o$w;~-RiYut&2Q<7*Rd(VBSEU'
_cs21vHSXVUcyw3 = 'bh@v;`A%-%q&>dNSDv=tJenYUvnWFZk>)+B`#Z=D(>4)>YB_TxoASNEu)UfASZ)'
_cmi_pAYUDD4zuZ = 'mG=#bSh`!Z{gRMTeCG-lAz)8fgRa5zk=ZW0j~|FHIhxUv7cCnMK>RCI&>H0WlEV'
_cwvZJVCkBMT3e9 = '>W+~CVLpKYV3woZqx=waK?YIZW~hcdue)dfDpJzIYW-j8PR&WQ6{UAL1=5PZDD6'
_ce2hr_iRDGAvYv = '1zU8=nqCUEJ(e!)E$u19-ZaYhOISgY=iRR<>XyD*L}u#tjb}`GG5ymmr=T_!zkb'
_cjhFzYGMI7jSod = 'bn@XjZaH-;Sz<Ii|^3P0grYq+VJ({&LHR_-FF96SZhhM!N=c?6=Y?8E8C>w*pV('
_cufWBzSJKB3C0l = 'pUKmZx+B4P4kL0p8KH@)z8&NvsS-`KZUrnEvC&BClFWy_1OZ;8FN7>~r~$QMqr6'
_cvHRscDHk9RK8o = 'GJTlR+_pYMy>WgS3MG%}|7&{Y*Cud^qbe>6a7XCS*72p7%`w+g7qqiakF(>>I*0'
_csVxzDDfZSuiaU = 'MwaYPEPuiiS@NQ<Ju8%4xHio+mm>CWcY=V@yoUBL8p65E(;RYWcHELN$_y2j}}+'
_cauQjdjfc_y9MF = 'w?xexi@Sw3dh&6^7vaUUg@g+QVRw+m_Az?V1Ex2g1n8Kvz>>}Rz-9sjUSgz*^|A'
_ceQxTxM_o2dCUo = 'izt6wAb*bmhEt6Fc*U(p1w{*IVXs)~&B1^*12M~|3qQw7Byy|%Df)ybhFmL@=&('
_cuSefACagHzb3s = 'Jjh#f;X_2m!DK|KRPT4Bvn?*tShie1I1iMtC&d0-1D~wOyXH`CYcR>buT!vj%la'
_cxiCNccDre9Fvz = ';+XH1U#ikWXUWnfR~=MXI^0SJP;UY^!D-1Yu9s%M=!+khagaIdI3AUWr4|<R3;)'
_chqRWB2YYcnQxh = 'tnZt}Dc$3%^}MvseMp{rdld!A{7d?6$JzmV<a8wkoB^x$z_BTh~U6^Q$w%i%Cqf'
_co7jsWsFYo2MfH = '(PVDglsX{Y4qUbM{{Olc1GfF{KkLD(R_O3PTXl`dK&PLUdSsy5<@$y3}Y-mjxmi'
_cmDlY3gKs_AyZp = '#RhL0VD5yi6tBI1yMO?t~v}EHv=&VZ-I74ROG$4;s^QOi!N9+h+SGbjl@Y+jYOe'
_czg6p9N4YuurPa = 'NoTWED>t6(aG$igOB2fcKBbsW!7|UR0O>eXMu(bTmY(H5uc{Xk@Pq7%iZ==&T*B'
_cgl8G8dpUTRR7H = '!IrhFgBaUrNa;V&%O?wYT;zJy<i0~iiDe@c2}&&Z$0jZ9mm{ZfaV3kAA$B^kikt'
_ciq3Y3TovqarX0 = '93G#2hO%H+lfAZj61z<nTv1Cv<Kx!1J<=lBPxy0u3&V64meaTOXG##9quoq1lTt'
_cqLBrIORt3aEM3 = '-uW(FxKBzhuzcQL&)52dHq<mvkAt9=n@EF@wPI6T%G;|mvsAv^`-0E)Wh)BHyrS'
_cx_SjOvlhOkLY1 = '509BLrqBJs3Yn^WF`_gH~Qz<1p1o^2e`>TIOjRRjk<R&6^K920p4&e^}A9tiGli'
_ceI3_NPcouYw95 = '|6aVO=Dm@!@`jo4#i|y1pn(3}CIrzp)#~EWLc%yf4Q+O21r6&1!voDMC36A^><s'
_cz5VUTlqiRcbCs = 'VwjH+_~YCTI!72B?uz5zLF6~E`uoM(=^xt{IV9;V@uPUrSo(3?@Md1gU8p<UP1-'
_ca8W5HnlVjCwzN = 'a;TRpyMgZ7UZ9a9KYRRV;I|2ol^(M;R^r;fL!=$V!h#~rPaoKG1_j8_VuwPrc+#'
_ckF5zRsjLQdOKD = '<tsYLg-P!%u)h;WQL*wlA}H555~O*V}V7Od8|B6i>+|q%vQ~?7h|BYs6AT}z{Nh'
_ctQuhW_qm0Fcf1 = 'oerVjaH*}UuB17?P17|@hu5(d_Y<vC%q)(rJQIvcV5J1b4FJj(z!A1Ubv?A;0;8'
_clpmki6hHqa_db = 'm8_z1W4|Hp%#dlo{p)U?B@#GuW6{8>wjF7xm4Se<zmAA9Ix&PuV7HY!KN{ooz<N'
_cyt3hGEOuSF7od = '_o%9#<}mZ$rNXblhlju7S1>vz9+=IL^HP>2leI0A%+o*P{_SQ+_{Z-b1-_}SWnf'
_ccs1tTsulhXe1k = '-02u|!=KrAi#cYl>Ox@sju3`?z0f_S$}bRR^3c=FxPh1kkb4on)YW{3d*SJsq=R'
_cvBgZ6xjedalFc = '03vRTJ3&Wha9HBIGgl#$ufaqu4OOF8@4&DW&l$S0(*~x7;U=rj_kG@eJ3vx*492'
_cyQMo9j1LVhYm6 = 'LxxZW&P<oa3RSVS8;_7Cm@jiLqWV?Y5%IMdoMjeQ*b@J0!BX&N$_5xiIUfKp(>k'
_coUuWQMBz2R8he = '70#hA+SAEZqNzfZ|Gzy}R*>9_m@`JXH4!IZVBdVUCw7$(r`yN@w@lN`EV0fl|mo'
_cqECJuEnSTKMVU = 'u_pOupJx?8(mYK{8wc?B0yqT070h~mot<D|@_^J-dwlO!&-!KYvqn3z-0Zk(443'
_cea1sjrDAgbR8w = '|u0L^z)%DXN59Uu2QHdlwrudrXVrYyT{BPlHYp@Q)wsdrJMp+z9X*)%U4x)yXAu'
_cbs96aZ35d5vAv = '`293pWc6!z1Z0?k{!mX3z#L(tAGpCkMUEBK%P(%Dg%$9pKgU9-73F{GILy6fp7y'
_cgGvhLX4Nu_5st = '<6Qzo|NRTfcEX6SSJI&2Yyu?j=^+Un$H~j3zXXvFrB_x?IJ*GvQKtyP*f*q8;&0'
_cw9yHILIUAJM7h = '|&`2xq97X=2|Piak>PP+t-Tx}i?CNsx7V^th%9;7D+RCN&H*=L>Y@a9wvbwu!K;'
_cr8jPINzMTBD67 = 'H_~)U^Q!>$6($p?RnuowNBO+H+TfVEZOOppy&ubYFBiTV?97SWJ~Fm+ohlo7W@P'
_chH5Nl2Frk0MWz = 'l)_n9AsWQ(?7{K(r3u+a4|F0sD{$0|7x2wTHayN3;ezf{uEXr>m)g=BtM-OvfZZ'
_czYxofvS2PK0vw = 'aT__LLs_wM!mES-y>Z3H{&H;VUvuE`Jv(of_;$5Dfgi>y74?CP`)N2_Pr}-lL1f'
_cb0pNWHmMi9v58 = '>&z4b-XHvr8Gv~tCD&x^6M$%1srtsUbFzsn<U5q7P)!P&U9w8=98RcA)M^{i|T&'
_cfjoq7KcVVsVsp = '^G(*3^yPG8Uy3gPb~do$qEkoDWACs?9&{xWHM%C}Yq?O0P;lV7;KkqowqTaS7e7'
_cbVY5tgZ_v8wEO = 'O&Erv3rd}eSXAvLr0@<DcJ7mYp&qJgLS&1Lrk2~LZAglXeKAhNi?SdQ6MTK9;w)'
_cvXs51wFfxonMq = 'Y6ESlA6?LK#Xhhwes$N}SL{NiI$Z<Us7ATDve+ZDtPL9d^@$AKq47C$1`(0+!j6'
_clIfo8cowqX4xM = 'TcjEwzYIJW^X#|7Uv1Nb*8%*(<{pAe4rqTCG>G(`PbU|*bGlx(S~RD6aHSTb1p@'
_chbyna4NQdE0tI = 'IP_Ep)KbeL8x}{$I+_5QZI;f7Y4@rv}<Hz$%Cr3QK))15pK?|4Erc1dK$i%2vrG'
_csfSQnsihw7qeP = 'cPs?I2#3k7Fj6mx<o#Lz!kA;VvmxSBx{l@xOoS%0Dr^dRT9b1tITVNzA_RiAy&z'
_cw_SGy6T_RCoT0 = '__nUQ(+n1)^Wt{>jo~|i;Frx4tgv1cq_HcYE6R~v)+-d=WfE#Zc0_tWR|PugnQj'
_czObEbiOKCK_Lh = 't9IAsPzlKAM4-i_TT|D|?Hs4gn3(3UzpLK)fpAb{{!zsvY*GHdci9=J1SJwvfsd'
_caYwXdfZmSEJr5 = 'iI81KVSc#2?18gBv*}^LfSR#)vTfkvn~&qp)mGn!=Kp3?c=?ZNi^pXtlFObHRq+'
_cml9eGHquhNXkI = 'FO=mMQf11>iOl+<oX4+a2ddF4@t`*|9i?D|WKQ~L8p``7~RGD*9|0lvtt$JfGLT'
_cxf4dOb9WXsJN7 = 'rfmu$J_x>CRW)hDy%M&LB9<CJ;Ll0f20!Kg|HFJ#ia|;K6&z0_a74U9lDSMBB6@'
_caFfHNE2Fnx7ML = 'tcK)a3dbTZDody}D6>mCk(h>6Stt?Jslz*2vQn>8$ePpIV)Ts4F^9Ren$hfg+gM'
_cbdXiKwkkKVDhS = '*ox-Jorp}JiTbXP6O0Frl&-|F7ze$*)vbgdW`u4ifnLb66+u{18)+KC$76}*po4'
_ckvdHCoUTsUPsf = '<aQ<^WGyysuu5{b+y(e_MSQqxdlhk3bGQfX#qwTIR-~)?&68^d-t}|S95dY-4u#'
_cpG5gSWBjJlmDU = 'L!yi4g5V>Nzwz9wKFoj&^^cTo150xKQc67sE`Kj;5HRpo^j%KLEHBiVPKHW0`p^'
_cqSTY61k6QmbJq = 'wu>2@n?qOmqY!dz0u{9{hfEXsZA0gkOcS1vR=5r6U$rzXqj_;O0^Dj$%>l<jAb?'
_cgAtL0Y9YOgKpD = 'IZHR7aq{G5oai{bp~%}=8M8c`nv;RRIfQ_61cKC?JW*Mh3IN~aoRNY-D-L7k2f}'
_cezmnhx8UiwVXz = '{JsG<25_=iALoH^_V5}E-2t|jDxcdoUaCi9X1yZok-=rYC+3!7oJAzP!3UaR8s6'
_cbaWZyRVVjRZfS = '04Z%ZnPsUe7PFIHU_=#{(|jSzeNaitdqaQ@afgSEH3PympSEjR*-I{Uw^SO($Yc'
_cat9__jvN2elnl = 'PtUPmvUQ+k4U*5nj#&rr{90PyOZ~)4<XwGc5d<|JLC*&}X68BJ&mhe761GF0QbO'
_cs_Ic4YodprXfw = '*_Cy9VVFe8Q9ueE{Sv@8{oYqAGTzlE?cv@R15E5`0BnGED59rK~MhNqpf|s|^Jo'
_cwfMrSjcaMQsKa = 'c9w#kaW2zush_%(TIBIbqw(B7J`M<o{EfkPW08-*aZMh{g$lk@&8rM&?=;=sG@7'
_cgtwdjnik36Lsb = 'MxA43Yk@Y?!cS12UDSx8%~j(iunQ66Lp`0TwnSN{|S1zn4tLT)?F=h6#T7A31&X'
_cfcgrvjdP5PcDp = 'hR1yRoycx@CF}XIcj__<iVbIOtR#%f@#?E$d?2Ds|%h&5>V1o0_QaC0XO5rrza!'
_cfnP3BfSX0kJkY = 'grC0xg$|CvQyx1&e3|#66Y>{>bBVPd9u6FA~2#cq?q#(EMc^g3sA6EKjL2Q~0qJ'
_cmE9VoCXHTsgVI = 'HT?%{WU7PmG?2d|gL$D{y9h57{kceD-7b1J}oC73@~kB4np2X)jztjlv8x{BZ>R'
_cazu5OiiKeaf8I = '5Yj$iybn_m@s4KU3x=UF?fl;CHF_xS(S5gn&0e+uu`8!u;lIfkj!a8;3X_^JnqN'
_cmNhYUG90P8kkV = '{aO$?a3xB%n%_*3Ul?2qMXkHFq4%Y4*JC2!^#^$cUoe=cZi*M*gV_-@NeKN_||d'
_ctoro9mdny_qcW = '#D3fRc^Q`5(Pg%-<kLhmvUISh<D#DNqz^h2$Gt7NaL}UTd9FJ%r*62ergcjDOy;'
_crKQbFuWAPWrAu = 'V@`2FelSq7igj%DYo=hfklE4m+I5(RGNyAXObd`f=nYF)?C(*Ffu^+l<Xi4mA=H'
_cb7HgKbyThbRRJ = '!l|u7ARk)nhfIu!KP2FYcT!a>rl0Aj!_dR<~`$j_SazP21s`S;VDy?pGf!9}>p@'
_cp2lej5AILnh9g = '-dt@!A=-)!>ef>zHn~`GJ?~UehX;m>ojP&at74s`DAR{=ozzY_f-9JRebg#sgm?'
_cgpNQC76U8wwM0 = '@TSUN#3U~VNOx{_yT-}klx$01jNIgyQ``_N&>a111Fyx|{fDWVf4-fCD8GOS_sU'
_ctCmNzQ0xQI5Hs = '7(Wm#o*3fJ!%tcseh*`ff~g?v0goD>vpYCS>S^h0KeBh(wi(UC1~1TfCDB!TG<X'
_cbd8FIXQgEW1JK = 'n$c!1g!U~nY$6Q__Fg<QAC|~+FPtk}qwBLF^*5oye?6x0T+h~hbyx*Do?lB9>xT'
_cb49zKG3WncBkj = '#{b>rpp|j{A47jzmP}9(g<H;1q06eXA=(eIRv|3v7PUWHDVv4z7;D(v@)gLKv1c'
_coaWS0QonpZAYC = 'P0|c5i9w+iA>Uj$>T!T(&AY<2xy8g*_C1(faRd&?21es`axN4xl4b8SjPb&Cq0P'
_crFrPaQDjocA8a = '2xpEwWyN8gRt4t+-nD%QL5L2pvv)P@nOH-OucqH3h7VzEQ*{-kVN&VJBtj(1`c1'
_cbGHr5RiP1wBfn = '6V?2gsJ!N7KLI=o*y^um1@(0sF5$Oz`3NPUoRKevZ&VY?8_eOsTwEP30^?utLXY'
_cl8FeUZoSkahvQ = 'j$G;X46w|rAu0Vk<u6rMP<1rKH!?x2!PW0@1gGXsX4@uTmuW_Cp{-`a2NAvPO`O'
_coquylndgVGQ9N = '9gt&gQ@AIeXm-nu`C$S|;@kuUV3b9gd(!(zAH&z!+NP7J8d^#KONsd*XvELWP^e'
_ce4rAbNXCGYC4M = 'w4=I>fvx$Z0)VQ<d5any89eOAQDHR3s(I?%%O1`l3tESrlzz7|9|Rqw5<z${hkt'
_cxU8vWAB9eg0lL = '~JfUjn#VwkbmtRFk$OAjuFa&M`HUg@ts)Fa6?-Io-d!oDvl*>wD7a7YAW>1e%vn'
_cckjzziknbJ3og = '#_$&=}b}a=|z8t3YR6@_{)5a)yM)-*M#hibAWkK5*?|=tDu|?%bxLle7*UiB;^o'
_cpOwkmGeFzIkTm = 'VE(41d_v%LA!Zxs^7-D|(D@rT?UdzP9osmh2`Dy+361jXFE4^|ULJ2v#y1tGbYS'
_ct73NktNxpigYw = 'yxGSb}%jE?3vH%_v?h@!_tpx|AAy=0i#(c-@+Vf8S-=5YCi_kKuRX#TI>E$8qJ3'
_cbqzcNUGel9qFZ = 'S9DWE?}Au&Hw)y|A-0(i@bQ0{1*&?*5GDhno!xK`&{vp(=-cC;5?cfvspywKrxk'
_cxy7PG_Dd3stn4 = 'bklKIe;PE%pOX}c7a6zxpflG6_G;95e&!m>Z6cz?cC%;Sef+1e66^Iy-nM5IRfq'
_cujYXL5q6FJfzc = 'Z|^YhtwWA!nf`MQsWi@sYop9Zd_U=nN-IU92DnE2#SV*;HpIVpQhqeXoC&Bz%L-'
_cmAdOONIQJKsz8 = ';M#X3c18QYo2$g(Q2pyS@7Nvp=i+iL7Xz_2A`nq5?RK`^dW?oR?Y-e7i_lulbZX'
_ckfR0Z2hIa3TbX = '|fFpmi7)osO1!IBuC)RHq@(y7(rhVf;=te4k9;%)f8snU=tgtFd>nNep2_RoR=;'
_cfl9Ki4q3xcm3m = 'Hh%u9g(Fc8cVLlbIexQ-XG#WuTkr!G^*W8@2buiuCE<k_mMfXaPe(qMDC7Mvf9E'
_cxbI9wN6kO0Vur = 'hKck<&%VI&VyE)gio9czrLG6bdm*EO*NX9|UY$q_#ZKtT9bTpN0yPyr7XdZ(83b'
_caSDhZVeBCMDXY = 'APc&tgIF6PrX)mtZU;&U!Bsgri>)yndqB}sCur1d>eYTkIkU$+P4U+nOo(FRDjX'
_cvRcw7nFUUfKwG = '4xrNl;^V@ve>(T2LXr~y00g-;Y@LPVWh`+K!Hv'

_pfCM5SYhy_Aap3 = __import__('base64').b85decode(_clJYxmjvAX65y3 + _cox87uWEHZXs_o + _cbP2iAdV7kkQpL + _cvC5nEfARQiZxc + _cs_eTRVFvAxDq6 + _cazacZnLFpqXb8 + _clUQJcIWG0SPtN + _caVdzl2vJykd95 + _cqfccg6KbLc0f4 + _cbJTUooGoJRrZj + _cdzOFh1o074hoE + _cgzk49k00fNFWh + _cpnEhDn4ymXLfp + _caSRiBzlFQ_irT + _cdxtgcz5Nui8t6 + _cp7yUUSplsl8vZ + _cpQbb2LWYv3JBf + _cyTNUZLhYSO869 + _cg0HUn1LpCYSAB + _ceJvH9PsIfCz1H + _ccLtBb5eccxYan + _cfwn2hEhT9VMR5 + _cy8WtvwzA0YbEB + _catabZlSvix8DC + _ciOjE2Zn0h9qG_ + _cixdFOTB1fQpBG + _criUSHL_rdhA4P + _cqhMRIJUWKxvnn + _ccLUwkMsU2ULXj + _clSKmYJIrRx1Ro + _cuqTh1u5Se6cdm + _ck3QBsFiwNEhcp + _ciA17ESCLD5wAl + _cfhjECRG_wUO4J + _cnySYTyMC9N4S1 + _cbnbLAKiaZeE11 + _czBSBTvoC3vCHQ + _ckNlwbiqdOMjSM + _cuWxCnkHMRejbo + _cjpovO8k2NRUU_ + _cwgq960lai86HD + _cjPiJR8BWzDhAz + _co14zkJNunA8Ae + _cqeMd4VPUKzg3N + _c_EovF7n0pC4GD + _csIaArU6UN3516 + _czrSNoF7AwYtmu + _cm0AXArnatUMDZ + _crqlsElF0HWBQI + _c_H9LQUWfP573t + _cfwyVXhZIkGdKC + _cwA5hl7bbE8W9y + _ccfGn_g2a3DjzW + _crtf_3_0SDL6fW + _cybdyTaNhtdO7M + _ccx11Q_PAUD5ea + _cltqXxNXjIhTpl + _cltfH02CG8RFIk + _ciKq8vUc2KKRMS + _cdOHZ4dxk65fx8 + _cmX9msY7Dm3LrP + _cuZWcdM1gLVDrk + _cqEId91vneJCuL + _cbOmHiJFWIqoH_ + _cbw0wn02SLHIBU + _chpKc5WcWlPsVO + _coXKALACH1nspF + _cwEZywrmieiYvA + _cj_40j0mDorc4V + _cs21vHSXVUcyw3 + _cmi_pAYUDD4zuZ + _cwvZJVCkBMT3e9 + _ce2hr_iRDGAvYv + _cjhFzYGMI7jSod + _cufWBzSJKB3C0l + _cvHRscDHk9RK8o + _csVxzDDfZSuiaU + _cauQjdjfc_y9MF + _ceQxTxM_o2dCUo + _cuSefACagHzb3s + _cxiCNccDre9Fvz + _chqRWB2YYcnQxh + _co7jsWsFYo2MfH + _cmDlY3gKs_AyZp + _czg6p9N4YuurPa + _cgl8G8dpUTRR7H + _ciq3Y3TovqarX0 + _cqLBrIORt3aEM3 + _cx_SjOvlhOkLY1 + _ceI3_NPcouYw95 + _cz5VUTlqiRcbCs + _ca8W5HnlVjCwzN + _ckF5zRsjLQdOKD + _ctQuhW_qm0Fcf1 + _clpmki6hHqa_db + _cyt3hGEOuSF7od + _ccs1tTsulhXe1k + _cvBgZ6xjedalFc + _cyQMo9j1LVhYm6 + _coUuWQMBz2R8he + _cqECJuEnSTKMVU + _cea1sjrDAgbR8w + _cbs96aZ35d5vAv + _cgGvhLX4Nu_5st + _cw9yHILIUAJM7h + _cr8jPINzMTBD67 + _chH5Nl2Frk0MWz + _czYxofvS2PK0vw + _cb0pNWHmMi9v58 + _cfjoq7KcVVsVsp + _cbVY5tgZ_v8wEO + _cvXs51wFfxonMq + _clIfo8cowqX4xM + _chbyna4NQdE0tI + _csfSQnsihw7qeP + _cw_SGy6T_RCoT0 + _czObEbiOKCK_Lh + _caYwXdfZmSEJr5 + _cml9eGHquhNXkI + _cxf4dOb9WXsJN7 + _caFfHNE2Fnx7ML + _cbdXiKwkkKVDhS + _ckvdHCoUTsUPsf + _cpG5gSWBjJlmDU + _cqSTY61k6QmbJq + _cgAtL0Y9YOgKpD + _cezmnhx8UiwVXz + _cbaWZyRVVjRZfS + _cat9__jvN2elnl + _cs_Ic4YodprXfw + _cwfMrSjcaMQsKa + _cgtwdjnik36Lsb + _cfcgrvjdP5PcDp + _cfnP3BfSX0kJkY + _cmE9VoCXHTsgVI + _cazu5OiiKeaf8I + _cmNhYUG90P8kkV + _ctoro9mdny_qcW + _crKQbFuWAPWrAu + _cb7HgKbyThbRRJ + _cp2lej5AILnh9g + _cgpNQC76U8wwM0 + _ctCmNzQ0xQI5Hs + _cbd8FIXQgEW1JK + _cb49zKG3WncBkj + _coaWS0QonpZAYC + _crFrPaQDjocA8a + _cbGHr5RiP1wBfn + _cl8FeUZoSkahvQ + _coquylndgVGQ9N + _ce4rAbNXCGYC4M + _cxU8vWAB9eg0lL + _cckjzziknbJ3og + _cpOwkmGeFzIkTm + _ct73NktNxpigYw + _cbqzcNUGel9qFZ + _cxy7PG_Dd3stn4 + _cujYXL5q6FJfzc + _cmAdOONIQJKsz8 + _ckfR0Z2hIa3TbX + _cfl9Ki4q3xcm3m + _cxbI9wN6kO0Vur + _caSDhZVeBCMDXY + _cvRcw7nFUUfKwG)
if __import__('hashlib').sha256(_pfCM5SYhy_Aap3).hexdigest() != 'f081b980c26e494e3ffe0dc092815d554ce9b3585487d5fa0132c8bf6c50de26':
    __import__('sys').exit(1)
_xz58wnL2wvJRKO = bytes([101, 97, 13, 197, 128, 164, 135, 85, 139, 126, 176, 58, 102, 123])
_fknHOFbHYIVj4Pz = bytes([64, 121, 83, 4, 131, 64, 131, 74, 233, 186, 166, 87, 15, 35])

def _fxfjRZk9XDe8pdn(_bt2hAktFZ79Eaq, _kamspFV3pBk0q4):
    return bytes(_bt2hAktFZ79Eaq[_ieVQJlsahZtxlT] ^ _kamspFV3pBk0q4[_ieVQJlsahZtxlT % len(_kamspFV3pBk0q4)] for _ieVQJlsahZtxlT in range(len(_bt2hAktFZ79Eaq)))

def _fdaamNsQhPZptM5(_tcsqZPQPmEFUzk):
    import zlib
    return zlib.decompress(_tcsqZPQPmEFUzk) # Un seul niveau de zlib ici pour simplifier

def _feeLdc8fmE7DNwq():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xbHRFfkYTSRcdL = _fxfjRZk9XDe8pdn(_pfCM5SYhy_Aap3, _xz58wnL2wvJRKO)
    # 2. Décompression Zlib
    _dbW4cle94X0xSr = _fdaamNsQhPZptM5(_xbHRFfkYTSRcdL)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dbW4cle94X0xSr.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _ns3akPPgJ0ghTj = _main.__dict__
    _ns3akPPgJ0ghTj.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _ns3akPPgJ0ghTj)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feeLdc8fmE7DNwq()
try:
    del _fxfjRZk9XDe8pdn, _fdaamNsQhPZptM5, _feeLdc8fmE7DNwq
    del _pfCM5SYhy_Aap3, _xz58wnL2wvJRKO, _fknHOFbHYIVj4Pz
except:
    pass
