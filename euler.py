from textwrap import dedent

sudokus = {
    "Grid 01": (dedent("""\
        003020600
        900305001
        001806400
        008102900
        700000008
        006708200
        002609500
        800203009
        005010300
    """), dedent("""\
        483921657
        967345821
        251876493
        548132976
        729564138
        136798245
        372689514
        814253769
        695417382
    """)),
    "Grid 02": (dedent("""\
        200080300
        060070084
        030500209
        000105408
        000000000
        402706000
        301007040
        720040060
        004010003
    """), dedent("""\
        245981376
        169273584
        837564219
        976125438
        513498627
        482736951
        391657842
        728349165
        654812793
    """)),
    "Grid 03": (dedent("""\
        000000907
        000420180
        000705026
        100904000
        050000040
        000507009
        920108000
        034059000
        507000000
    """), dedent("""\
        462831957
        795426183
        381795426
        173984265
        659312748
        248567319
        926178534
        834259671
        517643892
    """)),
    "Grid 04": (dedent("""\
        030050040
        008010500
        460000012
        070502080
        000603000
        040109030
        250000098
        001020600
        080060020
    """), dedent("""\
        137256849
        928314567
        465897312
        673542981
        819673254
        542189736
        256731498
        391428675
        784965123
    """)),
    "Grid 05": (dedent("""\
        020810740
        700003100
        090002805
        009040087
        400208003
        160030200
        302700060
        005600008
        076051090
    """), dedent("""\
        523816749
        784593126
        691472835
        239145687
        457268913
        168937254
        342789561
        915624378
        876351492
    """)),
    "Grid 06": (dedent("""\
        100920000
        524010000
        000000070
        050008102
        000000000
        402700090
        060000000
        000030945
        000071006
    """), dedent("""\
        176923584
        524817639
        893654271
        957348162
        638192457
        412765398
        265489713
        781236945
        349571826
    """)),
    "Grid 07": (dedent("""\
        043080250
        600000000
        000001094
        900004070
        000608000
        010200003
        820500000
        000000005
        034090710
    """), dedent("""\
        143986257
        679425381
        285731694
        962354178
        357618942
        418279563
        821567439
        796143825
        534892716
    """)),
    "Grid 08": (dedent("""\
        480006902
        002008001
        900370060
        840010200
        003704100
        001060049
        020085007
        700900600
        609200018
    """), dedent("""\
        487156932
        362498751
        915372864
        846519273
        593724186
        271863549
        124685397
        738941625
        659237418
    """)),
    "Grid 09": (dedent("""\
        000900002
        050123400
        030000160
        908000000
        070000090
        000000205
        091000050
        007439020
        400007000
    """), dedent("""\
        814976532
        659123478
        732854169
        948265317
        275341896
        163798245
        391682754
        587439621
        426517983
    """)),
    "Grid 10": (dedent("""\
        001900003
        900700160
        030005007
        050000009
        004302600
        200000070
        600100030
        042007006
        500006800
    """), dedent("""\
        761928453
        925743168
        438615927
        357461289
        894372615
        216589374
        689154732
        142837596
        573296841
    """)),
    "Grid 11": (dedent("""\
        000125400
        008400000
        420800000
        030000095
        060902010
        510000060
        000003049
        000007200
        001298000
    """), dedent("""\
        976125438
        158436927
        423879156
        234761895
        867952314
        519384762
        782513649
        395647281
        641298573
    """)),
    "Grid 12": (dedent("""\
        062340750
        100005600
        570000040
        000094800
        400000006
        005830000
        030000091
        006400007
        059083260
    """), dedent("""\
        962341758
        148975623
        573268149
        321694875
        487512936
        695837412
        834726591
        216459387
        759183264
    """)),
    "Grid 13": (dedent("""\
        300000000
        005009000
        200504000
        020000700
        160000058
        704310600
        000890100
        000067080
        000005437
    """), dedent("""\
        397681524
        645279813
        218534976
        823956741
        169742358
        754318692
        472893165
        531467289
        986125437
    """)),
    "Grid 14": (dedent("""\
        630000000
        000500008
        005674000
        000020000
        003401020
        000000345
        000007004
        080300902
        947100080
    """), dedent("""\
        639218457
        471539268
        825674139
        564823791
        793451826
        218796345
        352987614
        186345972
        947162583
    """)),
    "Grid 15": (dedent("""\
        000020040
        008035000
        000070602
        031046970
        200000000
        000501203
        049000730
        000000010
        800004000
    """), dedent("""\
        697128345
        428635197
        315479682
        531246978
        286397451
        974581263
        149852736
        752963814
        863714529
    """)),
    "Grid 16": (dedent("""\
        361025900
        080960010
        400000057
        008000471
        000603000
        259000800
        740000005
        020018060
        005470329
    """), dedent("""\
        361725948
        587964213
        492831657
        638259471
        174683592
        259147836
        746392185
        923518764
        815476329
    """)),
    "Grid 17": (dedent("""\
        050807020
        600010090
        702540006
        070020301
        504000908
        103080070
        900076205
        060090003
        080103040
    """), dedent("""\
        359867124
        648312597
        712549836
        876924351
        524731968
        193685472
        931476285
        465298713
        287153649
    """)),
    "Grid 18": (dedent("""\
        080005000
        000003457
        000070809
        060400903
        007010500
        408007020
        901020000
        842300000
        000100080
    """), dedent("""\
        786945312
        219863457
        534271869
        165482973
        327619548
        498537126
        951728634
        842356791
        673194285
    """)),
    "Grid 19": (dedent("""\
        003502900
        000040000
        106000305
        900251008
        070408030
        800763001
        308000104
        000020000
        005104800
    """), dedent("""\
        743512986
        589346217
        126987345
        934251768
        671498532
        852763491
        398675124
        417829653
        265134879
    """)),
    "Grid 20": (dedent("""\
        000000000
        009805100
        051907420
        290401065
        000000000
        140508093
        026709580
        005103600
        000000000
    """), dedent("""\
        782614359
        439825176
        651937428
        293471865
        568392714
        147568293
        326749581
        975183642
        814256937
    """)),
    "Grid 21": (dedent("""\
        020030090
        000907000
        900208005
        004806500
        607000208
        003102900
        800605007
        000309000
        030020050
    """), dedent("""\
        428531796
        365947182
        971268435
        214896573
        697453218
        583172964
        849615327
        752389641
        136724859
    """)),
    "Grid 22": (dedent("""\
        005000006
        070009020
        000500107
        804150000
        000803000
        000092805
        907006000
        030400010
        200000600
    """), dedent("""\
        425781936
        178369524
        369524187
        894157362
        652843791
        713692845
        987216453
        536478219
        241935678
    """)),
    "Grid 23": (dedent("""\
        040000050
        001943600
        009000300
        600050002
        103000506
        800020007
        005000200
        002436700
        030000040
    """), dedent("""\
        348267951
        571943628
        269185374
        697351482
        123874596
        854629137
        415798263
        982436715
        736512849
    """)),
    "Grid 24": (dedent("""\
        004000000
        000030002
        390700080
        400009001
        209801307
        600200008
        010008053
        900040000
        000000800
    """), dedent("""\
        124986735
        867435912
        395712684
        478359261
        259861347
        631274598
        712698453
        983547126
        546123879
    """)),
    "Grid 25": (dedent("""\
        360020089
        000361000
        000000000
        803000602
        400603007
        607000108
        000000000
        000418000
        970030014
    """), dedent("""\
        361524789
        789361425
        524879361
        893157642
        412683597
        657942138
        148796253
        235418976
        976235814
    """)),
    "Grid 26": (dedent("""\
        500400060
        009000800
        640020000
        000001008
        208000501
        700500000
        000090084
        003000600
        060003002
    """), dedent("""\
        581479263
        329156847
        647328159
        956731428
        238964571
        714582936
        172695384
        893247615
        465813792
    """)),
    "Grid 27": (dedent("""\
        007256400
        400000005
        010030060
        000508000
        008060200
        000107000
        030070090
        200000004
        006312700
    """), dedent("""\
        387256419
        469781325
        512439867
        123548976
        758963241
        694127583
        835674192
        271895634
        946312758
    """)),
    "Grid 28": (dedent("""\
        000000000
        079050180
        800000007
        007306800
        450708096
        003502700
        700000005
        016030420
        000000000
    """), dedent("""\
        345871269
        279653184
        861429537
        197346852
        452718396
        683592741
        738264915
        516937428
        924185673
    """)),
    "Grid 29": (dedent("""\
        030000080
        009000500
        007509200
        700105008
        020090030
        900402001
        004207100
        002000800
        070000090
    """), dedent("""\
        235761489
        419328576
        867549213
        746135928
        521896734
        983472651
        394287165
        652913847
        178654392
    """)),
    "Grid 30": (dedent("""\
        200170603
        050000100
        000006079
        000040700
        000801000
        009050000
        310400000
        005000060
        906037002
    """), dedent("""\
        298175643
        657394128
        134286579
        821649735
        573821496
        469753281
        312468957
        785912364
        946537812
    """)),
    "Grid 31": (dedent("""\
        000000080
        800701040
        040020030
        374000900
        000030000
        005000321
        010060050
        050802006
        080000000
    """), dedent("""\
        761543289
        832791645
        549628137
        374215968
        128936574
        695487321
        417369852
        953872416
        286154793
    """)),
    "Grid 32": (dedent("""\
        000000085
        000210009
        960080100
        500800016
        000000000
        890006007
        009070052
        300054000
        480000000
    """), dedent("""\
        132649785
        758213649
        964785123
        543897216
        276531894
        891426537
        619378452
        327154968
        485962371
    """)),
    "Grid 33": (dedent("""\
        608070502
        050608070
        002000300
        500090006
        040302050
        800050003
        005000200
        010704090
        409060701
    """), dedent("""\
        698173542
        354628179
        172549368
        531897426
        946312857
        827456913
        765931284
        213784695
        489265731
    """)),
    "Grid 34": (dedent("""\
        050010040
        107000602
        000905000
        208030501
        040070020
        901080406
        000401000
        304000709
        020060010
    """), dedent("""\
        852716943
        197843652
        463925187
        278634591
        645179328
        931582476
        786491235
        314258769
        529367814
    """)),
    "Grid 35": (dedent("""\
        053000790
        009753400
        100000002
        090080010
        000907000
        080030070
        500000003
        007641200
        061000940
    """), dedent("""\
        453218796
        629753481
        178496532
        796582314
        314967825
        285134679
        542879163
        937641258
        861325947
    """)),
    "Grid 36": (dedent("""\
        006080300
        049070250
        000405000
        600317004
        007000800
        100826009
        000702000
        075040190
        003090600
    """), dedent("""\
        516289347
        849173256
        732465918
        698317524
        327954861
        154826739
        961732485
        275648193
        483591672
    """)),
    "Grid 37": (dedent("""\
        005080700
        700204005
        320000084
        060105040
        008000500
        070803010
        450000091
        600508007
        003010600
    """), dedent("""\
        945681723
        781234965
        326759184
        269175348
        138942576
        574863219
        457326891
        612598437
        893417652
    """)),
    "Grid 38": (dedent("""\
        000900800
        128006400
        070800060
        800430007
        500000009
        600079008
        090004010
        003600284
        001007000
    """), dedent("""\
        365942871
        128756493
        974813562
        819435627
        537268149
        642179358
        296384715
        753691284
        481527936
    """)),
    "Grid 39": (dedent("""\
        000080000
        270000054
        095000810
        009806400
        020403060
        006905100
        017000620
        460000038
        000090000
    """), dedent("""\
        134587296
        278169354
        695234817
        359816472
        821473569
        746925183
        917348625
        462751938
        583692741
    """)),
    "Grid 40": (dedent("""\
        000602000
        400050001
        085010620
        038206710
        000000000
        019407350
        026040530
        900020007
        000809000
    """), dedent("""\
        193672485
        462358971
        785914623
        538296714
        674135298
        219487356
        826741539
        941523867
        357869142
    """)),
    "Grid 41": (dedent("""\
        000900002
        050123400
        030000160
        908000000
        070000090
        000000205
        091000050
        007439020
        400007000
    """), dedent("""\
        814976532
        659123478
        732854169
        948265317
        275341896
        163798245
        391682754
        587439621
        426517983
    """)),
    "Grid 42": (dedent("""\
        380000000
        000400785
        009020300
        060090000
        800302009
        000040070
        001070500
        495006000
        000000092
    """), dedent("""\
        384567921
        126439785
        759821346
        563798214
        847312659
        912645873
        231974568
        495286137
        678153492
    """)),
    "Grid 43": (dedent("""\
        000158000
        002060800
        030000040
        027030510
        000000000
        046080790
        050000080
        004070100
        000325000
    """), dedent("""\
        469158372
        712463859
        538297641
        927634518
        385719426
        146582793
        653941287
        294876135
        871325964
    """)),
    "Grid 44": (dedent("""\
        010500200
        900001000
        002008030
        500030007
        008000500
        600080004
        040100700
        000700006
        003004050
    """), dedent("""\
        316549278
        987321645
        452678931
        594236817
        238417569
        671985324
        845162793
        129753486
        763894152
    """)),
    "Grid 45": (dedent("""\
        080000040
        000469000
        400000007
        005904600
        070608030
        008502100
        900000005
        000781000
        060000010
    """), dedent("""\
        586127943
        723469851
        491853267
        135974628
        279618534
        648532179
        917246385
        352781496
        864395712
    """)),
    "Grid 46": (dedent("""\
        904200007
        010000000
        000706500
        000800090
        020904060
        040002000
        001607000
        000000030
        300005702
    """), dedent("""\
        954213687
        617548923
        832796541
        763851294
        128974365
        549362178
        281637459
        475129836
        396485712
    """)),
    "Grid 47": (dedent("""\
        000700800
        006000031
        040002000
        024070000
        010030080
        000060290
        000800070
        860000500
        002006000
    """), dedent("""\
        159743862
        276589431
        348612759
        624978315
        917235684
        583164297
        435821976
        861497523
        792356148
    """)),
    "Grid 48": (dedent("""\
        001007090
        590080001
        030000080
        000005800
        050060020
        004100000
        080000030
        100020079
        020700400
    """), dedent("""\
        861357294
        597482361
        432619785
        916275843
        358964127
        274138956
        789541632
        143826579
        625793418
    """)),
    "Grid 49": (dedent("""\
        000003017
        015009008
        060000000
        100007000
        009000200
        000500004
        000000020
        500600340
        340200000
    """), dedent("""\
        294863517
        715429638
        863751492
        152947863
        479386251
        638512974
        986134725
        521678349
        347295186
    """)),
    "Grid 50": (dedent("""\
        300200000
        000107000
        706030500
        070009080
        900020004
        010800050
        009040301
        000702000
        000008006
    """), dedent("""\
        351286497
        492157638
        786934512
        275469183
        938521764
        614873259
        829645371
        163792845
        547318926
    """)),
}
